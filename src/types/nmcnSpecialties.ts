/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { PatientVitals, ChecklistItem, StationMCQ } from './clinicalExams';

export interface NMCNSpecialty {
  id: string;
  code: string; // e.g. NMCN-MEDSURG-01
  title: string;
  regulatoryTitle: string; // e.g. Post-Basic Medical-Surgical Nursing
  description: string;
  statutoryAuthority: string; // e.g. NMCN Act, Cap N143 LFN 2004
  competencyDomains: string[];
  passMarkPercentage: number; // Strictly 50.0% Statutory Council Benchmark
  distinctionPercentage: number; // 75.0%
  station: NMCNSpecialtyStation;
}

export interface NMCNSpecialtyStation {
  id: string;
  title: string;
  subTitle: string;
  clinicalScenario: string;
  doorBriefing: string;
  candidateInstructions: string[];
  patientProfile: {
    name: string;
    age: number | string;
    gender: string;
    setting: string;
    chiefComplaint: string;
    historyOfPresentIllness: string;
    currentMedications: string[];
    allergies: string[];
  };
  entryVitals: PatientVitals;
  equipmentTray: string[];
  checklist: ChecklistItem[];
  mcqs: StationMCQ[];
  fatalErrorNotice: string;
}

export interface NMCNSpecialtySubmission {
  specialtyId: string;
  practicalScore: number; // raw points out of 100
  mcqScore: number; // raw correct out of 10
  criticalFailTriggered: boolean;
  criticalFailItems: ChecklistItem[];
  practicalPercentage: number;
  mcqPercentage: number;
  compositePercentage: number;
  isPassed: boolean; // >= 50% and !criticalFailTriggered
  isDistinction: boolean; // >= 75% and !criticalFailTriggered
}
