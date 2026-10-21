export type DifficultyLevel = 'Foundation' | 'Intermediate' | 'Advanced' | 'Expert';

export interface QuestionOption {
  id: 'A' | 'B' | 'C' | 'D';
  text: string;
  explanation?: string; // Why this option is incorrect or correct
}

export interface Question {
  id: string;
  module: string;
  topic: string;
  difficulty: DifficultyLevel;
  questionText: string;
  options: QuestionOption[];
  correctAnswer: 'A' | 'B' | 'C' | 'D';
  explanation: string; // Detailed explanation of why correct answer is correct
  incorrectExplanations?: Partial<Record<'A' | 'B' | 'C' | 'D', string>>; // Specific explanations for each option
  learningObjective: string;
  reference?: string;
  contentReviewStatus: 'Verified Demo' | 'Pending Review' | 'Peer Reviewed';
}

export type AssessmentMode = 'practice' | 'learning' | 'mock';

export interface AssessmentConfig {
  mode: AssessmentMode;
  module?: string; // if practicing a specific module, or 'all'
  title: string;
  timeLimitMinutes?: number; // e.g. 60 mins for mock
  questionCount: number;
}

export interface CandidateAnswer {
  questionId: string;
  selectedOption: 'A' | 'B' | 'C' | 'D' | null; // null if unanswered
  isCorrect: boolean;
  timeSpentSeconds?: number;
}

export interface AssessmentReport {
  id: string; // Unique report ID, e.g. WAPCNM-REP-XXXX
  candidateName: string;
  assessmentTitle: string;
  mode: AssessmentMode;
  module?: string;
  dateTimestamp: number;
  totalQuestions: number;
  answeredCount: number;
  correctCount: number;
  incorrectCount: number;
  unansweredCount: number;
  percentage: number; // Unrounded percentage e.g. 70.0 or 69.99
  passMark: number; // Always 70%
  status: 'PASS' | 'FAIL';
  timeTakenSeconds: number;
  questionsSnapshot: Question[]; // Snapshot of questions at time of assessment
  candidateAnswers: Record<string, 'A' | 'B' | 'C' | 'D' | null>; // questionId -> selected option
}

export interface CandidateSettings {
  candidateName: string;
  email?: string;
  darkTheme?: boolean;
}

export interface IncorrectRecord {
  questionId: string;
  module: string;
  lastAttemptDate: number;
  lastSelected: 'A' | 'B' | 'C' | 'D' | null;
  timesFailed: number;
}
