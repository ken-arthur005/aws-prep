param([string]$InputFolder = "public/new set", [string]$OutputFile = "data/new-ocr.json", [int]$Limit = 0)
# Offline Windows OCR, without Python ABI-specific packages. No answer marks are interpreted.
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Runtime.WindowsRuntime
Add-Type -AssemblyName System.Drawing
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$null = [Windows.Storage.Streams.IRandomAccessStream, Windows.Storage.Streams, ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrResult, Windows.Foundation, ContentType=WindowsRuntime]
$asTask = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq "AsTask" -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' } | Select-Object -First 1
function Await($Operation, [Type]$ResultType) {
    $task = $asTask.MakeGenericMethod($ResultType).Invoke($null, @($Operation))
    $task.Wait()
    $task.Result
}
$root = Split-Path $PSScriptRoot -Parent
$inputPath = Join-Path $root $InputFolder
$outputPath = Join-Path $root $OutputFile
if (!(Test-Path -LiteralPath $inputPath) -or !(Test-Path -LiteralPath (Split-Path $outputPath -Parent))) { throw "Check input and output directories" }
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if (!$engine) { throw "A Windows OCR language pack is required" }
$items = [System.Collections.Generic.List[object]]::new()
if (Test-Path -LiteralPath $outputPath) { foreach ($item in (Get-Content -LiteralPath $outputPath -Raw | ConvertFrom-Json)) { $items.Add($item) } }
$done = @{}; foreach ($item in $items) { $done[$item.source] = $true }
$files = @(Get-ChildItem -LiteralPath $inputPath -Filter "*.png" | Sort-Object Name)
if ($Limit -gt 0) { $files = @($files | Select-Object -First $Limit) }
foreach ($path in $files) {
    if ($done.ContainsKey($path.Name)) { continue }
    $file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($path.FullName)) ([Windows.Storage.StorageFile])
    $stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $result = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
    $lines = @(); foreach ($line in $result.Lines) {
        $words = @(); foreach ($word in $line.Words) { $b = $word.BoundingRect; $words += @{ text=$word.Text; x=$b.X; y=$b.Y; w=$b.Width; h=$b.Height } }
        $lines += @{ text=$line.Text; words=$words }
    }
    $image = [System.Drawing.Bitmap]::new($path.FullName)
    $divider = 0; $best = 0
    if (@($lines | Where-Object { $_.text -eq "Description" }).Count -gt 0) {
        for ($x = [int]($image.Width * .28); $x -lt [int]($image.Width * .65); $x++) {
            $score = 0
            for ($y = 12; $y -lt $image.Height - 8; $y += 4) { $p = $image.GetPixel($x,$y); if ($p.R -gt 215 -and $p.R -lt 250 -and [Math]::Abs([int]$p.R - [int]$p.G) -lt 15 -and $p.B -ge $p.R) { $score++ } }
            if ($score -gt $best) { $best=$score; $divider=$x }
        }
    }
    $items.Add(@{ source=$path.Name; width=$decoder.PixelWidth; height=$decoder.PixelHeight; divider=$divider; lines=$lines })
    $image.Dispose(); $bitmap.Dispose(); $stream.Dispose()
    if ($items.Count % 10 -eq 0 -or $path -eq $files[-1]) {
        [System.IO.File]::WriteAllText($outputPath, (ConvertTo-Json -InputObject @($items.ToArray()) -Depth 12), [System.Text.UTF8Encoding]::new($false))
        "OCR $($items.Count)/$($files.Count)"
    }
}
