export function Cloud({ className = "", variant = "hero" }: { className?: string; variant?: "hero" | "small" | "celebrate" }) {
  const small = variant === "small";
  return <svg className={className} viewBox="0 0 340 290" fill="none" aria-hidden="true">
    {!small && <><path d="m55 64 5 11 12 2-9 8 1 12-11-6-11 5 2-12-8-9 12-1Z" fill="#F4BD52" stroke="#26372F" strokeWidth="2.5"/><path d="m292 173 4 8 9 1-6 7 1 9-8-4-9 3 2-9-6-7 9-1Z" fill="#F4BD52" stroke="#26372F" strokeWidth="2.5"/><path d="m266 49 9-12m-1 27 16-3M46 172l-13 4m24 10-6 13" stroke="#26372F" strokeWidth="3" strokeLinecap="round"/><ellipse cx="178" cy="262" rx="91" ry="12" fill="#26372F" opacity=".09"/>
      <path d="m236 132 26-58" stroke="#26372F" strokeWidth="5" strokeLinecap="round"/><path d="m263 74 12-32 48 17-24 12 8 17Z" fill="#F4BD52" stroke="#26372F" strokeWidth="3" strokeLinejoin="round"/><path d="m277 53 22 7" stroke="#26372F" strokeWidth="2.5"/>
      <path d="m118 211-8 36-25 7c-7 3-6 10 1 10h35c5 0 7-4 8-9l6-40m62-2 8 36 24 7c7 2 5 10-2 10h-32c-5 0-8-3-9-8l-7-42" fill="#668BB8" stroke="#26372F" strokeWidth="3.5"/>
      <path d="m91 131-23 14c-12 8-13 20-7 27 6 6 14 3 23-4l18-13m126-13 17 12c13 8 22 4 26-5 3-6-1-12-4-17" fill="#FFFDF4" stroke="#26372F" strokeWidth="3.5" strokeLinecap="round"/>
      <path d="M212 114c20-17 36-4 38 12l4 64c1 10-3 17-13 20l-32-6Z" fill="#E99B73" stroke="#26372F" strokeWidth="3.5"/>
    </>}
    <path d="M90 189c-28 0-44-18-44-40 0-23 15-39 36-42-1-29 21-52 49-52 18 0 33 9 42 23 10-7 20-9 31-6 20 4 33 20 34 40 23 1 42 20 42 44 0 25-20 43-45 43H90Z" fill="#FFFDF4" stroke="#26372F" strokeWidth={small ? "9" : "3.5"} strokeLinejoin="round" transform={small ? "translate(-19 2) scale(1.12)" : undefined}/>
    <path d="M101 173c8 8 18 10 27 10h98c20 0 33-9 39-23-1 22-18 39-39 39H90c-22 0-39-14-43-32 9 7 16 8 24 8" fill="#E7EBDA" opacity=".7"/>
    <ellipse cx="127" cy="137" rx="4.5" ry="7" fill="#26372F"/><ellipse cx="192" cy="137" rx="4.5" ry="7" fill="#26372F"/>
    <path d={variant === "celebrate" ? "M146 151c2 20 26 21 29 0Z" : "M148 153c6 9 16 9 23 0"} fill={variant === "celebrate" ? "#E99B73" : "none"} stroke="#26372F" strokeWidth="3.5" strokeLinecap="round"/>
    <ellipse cx="110" cy="151" rx="10" ry="5" fill="#F2B8A1"/><ellipse cx="209" cy="151" rx="10" ry="5" fill="#F2B8A1"/>
    {!small && <><path d="M103 193c20 12 84 16 115 0l-5 23c-29 13-68 11-98-1Z" fill="#668BB8" stroke="#26372F" strokeWidth="3"/><path d="m132 199 2 21m54-20-2 22" stroke="#26372F" strokeWidth="2.5"/><path d="m157 218 4 9 10-2 7-8" fill="#F4BD52" stroke="#26372F" strokeWidth="2.5" strokeLinejoin="round"/></>}
  </svg>;
}
