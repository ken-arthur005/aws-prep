import StudyApp from "@/components/study-app";
import bank from "@/data/questions.json";
import type { Question } from "@/lib/types";

export default function Home() {
  return <StudyApp questions={bank.questions as Question[]} sourceCount={bank.sourceCount} />;
}
