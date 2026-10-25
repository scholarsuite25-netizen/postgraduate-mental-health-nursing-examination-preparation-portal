/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { PsychopharmMathProblem } from '../types/clinicalExams';

export const PSYCHOPHARM_MATH_PROBLEMS: PsychopharmMathProblem[] = [
  {
    id: 'math-1-clozapine-anc',
    title: 'Absolute Neutrophil Count (ANC) Calculation & Clozapine Action Criteria',
    category: 'Clozapine ANC Monitoring',
    clinicalScenario:
      'A 36-year-old female with treatment-resistant schizophrenia has been maintained on Clozapine 300 mg daily for 5 months. She presents for her scheduled bi-weekly hematological safety audit. Her laboratory report returns with the following values: Total White Blood Cell (WBC) count = 3,400 /mcL; Segmented Neutrophils = 28%; Band Forms = 4%; Lymphocytes = 58%; Monocytes = 8%; Eosinophils = 2%.',
    parameters: {
      'Total WBC': '3,400 /mcL',
      'Segmented Neutrophils': '28%',
      'Band Forms': '4%',
      'Current Clozapine Dose': '300 mg daily (Month 5)',
      'Baseline Pre-treatment ANC': '4,100 /mcL'
    },
    questionPrompt:
      'Calculate the Absolute Neutrophil Count (ANC) for this patient and determine the mandatory clinical action according to statutory Clozapine REMS guidelines.',
    formulaHint: 'ANC (/mcL) = [Total WBC (/mcL) × (% Segmented Neutrophils + % Band Forms)] / 100',
    options: [
      {
        id: 'A',
        text: 'ANC = 1,488 /mcL; Normal "Green Zone"; continue current Clozapine dose and maintain routine bi-weekly testing',
        isCorrect: false,
        explanation: 'Math error: 3400 * (28 + 4)% = 1088, not 1488.'
      },
      {
        id: 'B',
        text: 'ANC = 1,088 /mcL; "Yellow Zone" (Mild Neutropenia); continue Clozapine, increase monitoring frequency to 3 times weekly until ANC ≥ 1,500 /mcL',
        isCorrect: true,
        explanation: 'Calculation: ANC = 3,400 × (28% + 4%) / 100 = 3,400 × 0.32 = 1,088 /mcL. An ANC between 1,000 and 1,499 /mcL falls into the REMS "Yellow Zone" (Mild Neutropenia). Clozapine is continued, but monitoring is immediately intensified to 3 times weekly with differential until ANC rebounds to Green (≥ 1,500 /mcL).'
      },
      {
        id: 'C',
        text: 'ANC = 952 /mcL; "Red Zone" (Severe Neutropenia); immediately and permanently discontinue Clozapine',
        isCorrect: false,
        explanation: 'Only calculating segmented neutrophils (28%) without bands (4%) gives 952, but statutory guidelines require adding bands to polymorphonuclears.'
      },
      {
        id: 'D',
        text: 'ANC = 2,176 /mcL; Normal range; no change in care',
        isCorrect: false,
        explanation: 'Calculation error: 2176 includes lymphocytes, which must never be included in ANC.'
      }
    ],
    stepByStepSolution: [
      'Step 1: Identify Total WBC = 3,400 /mcL.',
      'Step 2: Add % Segmented Neutrophils (28%) + % Band Forms (4%) = 32% total neutrophils.',
      'Step 3: Apply formula: ANC = 3,400 × (32 / 100) = 3,400 × 0.32 = 1,088 /mcL.',
      'Step 4: Categorize by statutory Clozapine REMS benchmarks:',
      '  - Green Zone (ANC ≥ 1,500 /mcL): Normal; continue treatment.',
      '  - Yellow Zone (ANC 1,000–1,499 /mcL): Mild Neutropenia; CONTINUE Clozapine, increase monitoring to 3x/week until ANC ≥ 1,500 /mcL.',
      '  - Red Zone (ANC < 1,000 /mcL): Severe Neutropenia; STOP Clozapine immediately, daily CBC, hematology consultation, no rechallenge unless BEN (Benign Ethnic Neutropenia) approved.'
    ],
    clinicalSignificance:
      'Accurate ANC calculation prevents inappropriate early termination of life-saving clozapine therapy in the Yellow Zone while ensuring vigilant monitoring against agranulocytosis.'
  },
  {
    id: 'math-2-cockcroft-gault-lithium',
    title: 'Creatinine Clearance (Cockcroft-Gault) & Lithium Dose Adjustment',
    category: 'Lithium Titration',
    clinicalScenario:
      'A 64-year-old female patient with Bipolar I Disorder has a steady body weight of 60 kg and a serum creatinine of 140 mcmol/L (1.58 mg/dL). She is currently prescribed Lithium Carbonate 800 mg nocte with a 12-hour trough level of 1.25 mmol/L (upper toxic threshold). The clinical team plans to titrate her dose to target a safer maintenance trough level of 0.70 mmol/L.',
    parameters: {
      'Age': '64 years',
      'Gender': 'Female',
      'Weight': '60 kg',
      'Serum Creatinine': '140 mcmol/L (1.58 mg/dL)',
      'Current Lithium Dose': '800 mg daily',
      'Current Serum Level': '1.25 mmol/L',
      'Target Serum Level': '0.70 mmol/L'
    },
    questionPrompt:
      'Calculate the patient’s estimated Creatinine Clearance (CrCl) using the Cockcroft-Gault formula (with female correction factor 0.85) and determine the new proportional daily Lithium Carbonate dose needed to achieve the target serum level of 0.70 mmol/L.',
    formulaHint:
      'Cockcroft-Gault (Female) = {[(140 - Age) × Weight (kg)] / [72 × Serum Cr (mg/dL)]} × 0.85\nLinear Dose Titration = New Dose = Current Dose × (Target Level / Current Level)',
    options: [
      {
        id: 'A',
        text: 'CrCl ≈ 34 mL/min; New Lithium Dose = 448 mg (round to nearest practical tablet: 450 mg daily)',
        isCorrect: true,
        explanation: 'Cockcroft-Gault: [(140 - 64) × 60] / [72 × 1.58] = 4,560 / 113.76 ≈ 40.08 mL/min. Applying female correction factor 0.85: 40.08 × 0.85 ≈ 34.07 mL/min (moderate renal impairment). Linear dose proportional adjustment: New Dose = 800 mg × (0.70 / 1.25) = 800 × 0.56 = 448 mg ≈ 450 mg daily.'
      },
      {
        id: 'B',
        text: 'CrCl ≈ 68 mL/min; New Lithium Dose = 600 mg daily',
        isCorrect: false,
        explanation: 'Failing to apply the female 0.85 correction factor and inaccurate dosage calculation.'
      },
      {
        id: 'C',
        text: 'CrCl ≈ 18 mL/min; Immediately discontinue all lithium permanently',
        isCorrect: false,
        explanation: 'CrCl is 34 mL/min, which allows continued lithium with lower dosing and careful TDM.'
      },
      {
        id: 'D',
        text: 'CrCl ≈ 85 mL/min; Maintain 800 mg daily because serum level is normal',
        isCorrect: false,
        explanation: 'Serum level of 1.25 mmol/L is at toxic threshold, particularly in a 64-year-old with impaired clearance.'
      }
    ],
    stepByStepSolution: [
      'Step 1: Calculate CrCl using Cockcroft-Gault:',
      '  - (140 - 64) = 76',
      '  - 76 × 60 kg = 4,560',
      '  - 72 × 1.58 mg/dL = 113.76',
      '  - Male equivalent = 4,560 / 113.76 = 40.08 mL/min',
      '  - Female factor = 40.08 × 0.85 = 34.07 mL/min (Moderate Renal Impairment).',
      'Step 2: Calculate proportional dose reduction (lithium exhibits linear first-order pharmacokinetics):',
      '  - Target Level / Current Level = 0.70 / 1.25 = 0.56',
      '  - New Daily Dose = 800 mg × 0.56 = 448 mg.',
      'Step 3: Round to nearest clinical sustained-release tablet (400 mg or 450 mg nocte), with repeat 12-hour trough check in 5–7 days.'
    ],
    clinicalSignificance:
      'Lithium is excreted 100% unchanged by the kidneys. Renal clearance declines with age; calculating CrCl prevents fatal accumulation and nephrogenic diabetes insipidus.'
  },
  {
    id: 'math-3-haloperidol-depot-conversion',
    title: 'Oral to Long-Acting Injectable (Depot) Haloperidol Conversion & Loading Math',
    category: 'Depot Conversions',
    clinicalScenario:
      'A 34-year-old male with chronic Schizophrenia who has achieved remission on oral Haloperidol 10 mg/day defaults frequently due to forgetfulness. The clinical team decides to switch him to monthly Intramuscular Haloperidol Decanoate depot injections. The target maintenance monthly dose is calculated using the standard 10–15× oral daily dose conversion factor. Because of his high relapse risk, the team elects a conservative 10× factor with a loading dose strategy divided across two bi-weekly injections to avoid acute extrapyramidal saturation.',
    parameters: {
      'Current Oral Dose': '10 mg daily',
      'Conversion Factor': '10× daily oral dose (monthly equivalent)',
      'Injection Formulation': 'Haloperidol Decanoate 100 mg/mL ampoules'
    },
    questionPrompt:
      'Calculate the total monthly Haloperidol Decanoate depot maintenance dose and the corresponding volume in milliliters (mL) to administer per monthly injection.',
    formulaHint:
      'Monthly Depot Dose (mg) = Daily Oral Dose (mg) × Conversion Factor (10)\nInjection Volume (mL) = Target Dose (mg) / Concentration (mg/mL)',
    options: [
      {
        id: 'A',
        text: 'Total Monthly Dose = 100 mg; Volume = 1.0 mL IM once every 4 weeks',
        isCorrect: true,
        explanation: 'Calculation: Daily oral dose (10 mg) × 10 = 100 mg monthly depot dose. Volume = 100 mg / (100 mg/mL) = 1.0 mL deep IM in the gluteal muscle every 4 weeks.'
      },
      {
        id: 'B',
        text: 'Total Monthly Dose = 300 mg; Volume = 3.0 mL IM weekly',
        isCorrect: false,
        explanation: '300 mg would represent 30x the daily oral dose, causing severe extrapyramidal toxicity.'
      },
      {
        id: 'C',
        text: 'Total Monthly Dose = 50 mg; Volume = 0.5 mL IM once every 3 months',
        isCorrect: false,
        explanation: '50 mg is a 5x factor and insufficient to maintain therapeutic antipsychotic levels.'
      },
      {
        id: 'D',
        text: 'Total Monthly Dose = 10 mg; Volume = 0.1 mL IM daily',
        isCorrect: false,
        explanation: 'Depot formulations are designed for monthly intervals, not daily injections.'
      }
    ],
    stepByStepSolution: [
      'Step 1: Calculate target monthly depot dose in milligrams:',
      '  - Target Monthly Dose = Daily Oral Dose (10 mg) × Conversion Factor (10) = 100 mg/month.',
      'Step 2: Calculate injection volume based on formulation strength (100 mg/mL):',
      '  - Volume = 100 mg / 100 mg/mL = 1.0 mL.',
      'Step 3: Formulate oral taper: Because depot haloperidol takes 2–3 months to reach steady-state therapeutic plasma levels, oral haloperidol must be co-prescribed and gradually tapered over 4–6 weeks post-first injection.'
    ],
    clinicalSignificance:
      'Correct depot conversion calculations ensure stable therapeutic plasma levels without precipitating disabling acute dystonia or breakthrough psychosis during the transition.'
  },
  {
    id: 'math-4-bazett-qtc-polypharmacy',
    title: 'Bazett QTc Interval Calculation & Psychotropic Arrhythmia Risk',
    category: 'QTc Prolongation Risk',
    clinicalScenario:
      'A 52-year-old female with Schizoaffective Disorder and Diabetic Neuropathy is admitted with worsening depression. Her current medications include Haloperidol 5 mg PO BD, Citalopram 40 mg PO daily, and Amitriptyline 25 mg PO nocte. A routine 12-lead ECG is recorded, showing a resting heart rate of 75 bpm and an absolute raw QT interval of 440 milliseconds (0.44 seconds).',
    parameters: {
      'Heart Rate': '75 bpm',
      'Raw QT Interval': '440 ms (0.44 s)',
      'Current Medications': 'Haloperidol 10 mg/day + Citalopram 40 mg/day + Amitriptyline 25 mg/day'
    },
    questionPrompt:
      'Calculate the corrected QT interval (QTc) using Bazett’s formula and identify the clinical risk and mandatory psychotropic adjustment.',
    formulaHint:
      'RR Interval (seconds) = 60 / Heart Rate (bpm)\nBazett QTc = Raw QT (seconds) / √[RR Interval (seconds)]\nOr: QTc (ms) = Raw QT (ms) / √[RR (seconds)]',
    options: [
      {
        id: 'A',
        text: 'QTc ≈ 492 ms; Prolonged (borderline/critical in female > 470 ms); high risk of Torsades de Pointes due to triple QTc-prolonging psychotropics; reduce Citalopram to max 20 mg and taper Amitriptyline',
        isCorrect: true,
        explanation: 'Calculation: RR = 60 / 75 = 0.80 seconds. √0.80 ≈ 0.8944 seconds. QTc = 440 ms / 0.8944 ≈ 491.9 ms (≈ 492 ms). For females, normal QTc is < 450 ms; borderline is 450–470 ms; abnormal/prolonged is > 470 ms. At 492 ms with polypharmacy (Haloperidol + Citalopram + Amitriptyline), the patient is at extreme risk of Torsades de Pointes. FDA specifically mandates Citalopram maximum 20 mg in patients > 60 years or with interacting medications.'
      },
      {
        id: 'B',
        text: 'QTc ≈ 390 ms; Normal interval; continue all medications unchanged',
        isCorrect: false,
        explanation: 'Calculation error: 390 ms underestimates the corrected interval.'
      },
      {
        id: 'C',
        text: 'QTc ≈ 580 ms; Patient in active ventricular fibrillation; initiate immediate CPR',
        isCorrect: false,
        explanation: 'Calculation error: 580 ms is an overestimation and ECG shows sinus rhythm, not VF.'
      },
      {
        id: 'D',
        text: 'QTc ≈ 440 ms; Heart rate does not affect QT intervals in psychotropic care',
        isCorrect: false,
        explanation: 'Heart rate directly affects raw QT; correction for heart rate (Bazett or Fridericia) is mandatory.'
      }
    ],
    stepByStepSolution: [
      'Step 1: Calculate the cardiac cycle length (RR interval in seconds):',
      '  - RR = 60 / 75 bpm = 0.80 seconds.',
      'Step 2: Calculate the square root of the RR interval:',
      '  - √0.80 ≈ 0.8944.',
      'Step 3: Calculate Bazett Corrected QT (QTc):',
      '  - QTc = Raw QT (440 ms) / 0.8944 = 491.9 ms ≈ 492 ms.',
      'Step 4: Clinical interpretation and risk audit:',
      '  - Female normal < 450 ms; High risk > 470 ms; Extreme arrhythmia/TdP danger > 500 ms.',
      '  - The patient is taking 3 synergistic QTc-prolonging drugs. Immediate action: discontinue Citalopram or reduce to 20 mg, avoid tricyclics, correct serum potassium and magnesium.'
    ],
    clinicalSignificance:
      'Psychotropic polypharmacy is the leading cause of drug-induced fatal Torsades de Pointes. Correct Bazett calculation enables prompt risk mitigation before sudden cardiac death occurs.'
  }
];
