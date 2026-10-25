/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

export interface ChecklistItem {
  id: string;
  stepNumber: number;
  instruction: string;
  rationale: string;
  points: number;
  isCriticalFail: boolean; // "Red Flag" criteria - omitting or violating triggers automatic referral / score cap
  criticalFailReason?: string;
  category: 'Preparation & Safety' | 'Assessment & Communication' | 'Intervention & Procedure' | 'Evaluation & Documentation';
}

export interface StationMCQOption {
  id: 'A' | 'B' | 'C' | 'D';
  text: string;
}

export interface StationMCQ {
  id: string;
  questionNumber: number;
  questionText: string;
  options: StationMCQOption[];
  correctAnswer: 'A' | 'B' | 'C' | 'D';
  explanation: string;
  learningDomain: string;
}

export interface PatientVitals {
  bloodPressure: string;
  heartRate: string;
  respiratoryRate: string;
  temperature: string;
  oxygenSaturation: string;
  painOrDistressScore?: string;
  additionalParameters?: Record<string, string>;
}

export interface CAOSCEStation {
  id: string;
  stationNumber: number;
  title: string;
  subTitle: string;
  specialtyDomain: string;
  clinicalScenario: string;
  doorBriefing: string;
  candidateInstructions: string[];
  patientProfile: {
    name: string;
    age: number;
    gender: string;
    setting: string;
    chiefComplaint: string;
    historyOfPresentIllness: string;
    pastPsychiatricHistory: string;
    medicalAndSubstanceHistory: string;
    currentMedications: string[];
    allergies: string[];
  };
  entryVitals: PatientVitals;
  equipmentTray: string[];
  checklist: ChecklistItem[];
  mcqs: StationMCQ[];
  fatalErrorNotice: string;
}

export type CAOSCEMode = 'strict-exam' | 'self-paced';

export interface StationCandidateSubmission {
  stationId: string;
  stationNumber: number;
  checklistSelections: Record<string, boolean>; // checklist item id -> checked
  mcqAnswers: Record<string, 'A' | 'B' | 'C' | 'D' | null>; // mcq id -> answer
  practicalScore: number; // raw points earned
  practicalMaxScore: number;
  mcqScore: number; // raw correct
  mcqMaxScore: number;
  criticalFailTriggered: boolean;
  criticalFailItems: ChecklistItem[];
  practicalPercentage: number;
  mcqPercentage: number;
  stationCompositePercentage: number; // (practicalPercentage + mcqPercentage) / 2 (or capped at 49% if critical fail)
  isStationPassed: boolean;
  timeSpentPracticalSeconds: number;
  timeSpentMcqSeconds: number;
}

export interface CAOSCEReport {
  id: string; // e.g. CAOSCE-REP-XXXX
  candidateName: string;
  examinationTitle: string;
  dateTimestamp: number;
  mode: CAOSCEMode;
  passMarkPercentage: number; // 70% postgraduate fellowship standard
  distinctionMarkPercentage: number; // 85%
  overallCompositePercentage: number;
  overallStatus: 'PASS' | 'DISTINCTION' | 'REFERRAL (SAFETY VIOLATION)' | 'FAIL (BELOW BENCHMARK)';
  totalCriticalFails: number;
  stationSubmissions: StationCandidateSubmission[];
  totalPracticalPointsEarned: number;
  totalPracticalPointsAvailable: number;
  totalMcqCorrect: number;
  totalMcqAvailable: number;
  totalTimeSeconds: number;
  remedialDirectives: string[];
}

// Next Generation NCLEX (NGN) Clinical Judgment Case Studies
export type NCSBNCognitiveLevel =
  | 'Recognize Cues'
  | 'Analyze Cues'
  | 'Prioritize Hypotheses'
  | 'Generate Solutions'
  | 'Take Action'
  | 'Evaluate Outcomes';

export interface NGNCaseStage {
  stageNumber: number;
  cognitiveLevel: NCSBNCognitiveLevel;
  clinicalProgressNote: string;
  vitalTrends?: PatientVitals;
  diagnosticOrLabData?: Record<string, string>;
  questionPrompt: string;
  questionType: 'multiple-choice' | 'multi-select' | 'matrix-radio';
  options: {
    id: string;
    text: string;
    isCorrect: boolean;
    explanation: string;
  }[];
  clinicalRationale: string;
}

export interface NGNCaseStudy {
  id: string;
  title: string;
  subtitle: string;
  clinicalSummary: string;
  patientDemographics: {
    name: string;
    age: number;
    gender: string;
    admissionDiagnosis: string;
  };
  stages: NGNCaseStage[];
}

// Psychopharmacology Titration & Math Lab
export interface PsychopharmMathProblem {
  id: string;
  title: string;
  category: 'Lithium Titration' | 'Clozapine ANC Monitoring' | 'Depot Conversions' | 'Pediatric/Geriatric Dosing' | 'QTc Prolongation Risk';
  clinicalScenario: string;
  parameters: Record<string, string>;
  questionPrompt: string;
  formulaHint?: string;
  options: {
    id: 'A' | 'B' | 'C' | 'D';
    text: string;
    isCorrect: boolean;
    explanation: string;
  }[];
  stepByStepSolution: string[];
  clinicalSignificance: string;
}
