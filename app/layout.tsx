import type { Metadata } from "next";
import { Bricolage_Grotesque, Nunito_Sans } from "next/font/google";
import "./globals.css";

const heading = Bricolage_Grotesque({
  variable: "--font-heading",
  subsets: ["latin"],
});

const body = Nunito_Sans({
  variable: "--font-body",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Cloudbound — Your AWS SAA-C03 Study Basecamp",
  description: "One concept at a time. Personal AWS Solutions Architect Associate practice, timed mock exams, detailed explanations, and study analytics.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="en"
      className={`${heading.variable} ${body.variable}`}
    >
      <body>{children}</body>
    </html>
  );
}
