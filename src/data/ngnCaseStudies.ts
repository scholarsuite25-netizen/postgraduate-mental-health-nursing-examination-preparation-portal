/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { NGNCaseStudy } from '../types/clinicalExams';

export const NGN_CASE_STUDIES: NGNCaseStudy[] = [
  {
    id: 'ngn-case-1-clozapine',
    title: 'Clozapine Titration, Mandatory ANC Monitoring & Early Cardiotoxicity',
    subtitle: 'NCSBN Clinical Judgment Model: Treatment-Resistant Schizophrenia Management',
    clinicalSummary:
      'A 31-year-old male with treatment-resistant schizophrenia (failed trials of Risperidone and Olanzapine at maximal doses) was initiated on Clozapine 3 weeks ago, currently titrated to 250 mg/day. He presents to the outpatient clinic with complaints of severe flu-like fatigue, dry cough, dizziness, and shortness of breath upon climbing stairs.',
    patientDemographics: {
      name: 'Ibrahim Musa',
      age: 31,
      gender: 'Male',
      admissionDiagnosis: 'Treatment-Resistant Schizophrenia on Clozapine Titration'
    },
    stages: [
      {
        stageNumber: 1,
        cognitiveLevel: 'Recognize Cues',
        clinicalProgressNote:
          'Week 3 Day 4 of Clozapine titration. Dose reached 250 mg PO daily. Patient appears pale, diaphoretic, and tachypneic. Complains of chest tightness, palpitations, and non-productive cough for 48 hours. Temperature 38.3 °C, Heart rate 124 bpm, Blood pressure 96/60 mmHg (sitting) and 82/52 mmHg (standing), SpO2 95% on room air. Electrocardiogram (ECG) reveals sinus tachycardia with non-specific ST-T wave inversions. Cardiac troponin I is 0.18 ng/mL (elevated, ref < 0.04 ng/mL). CRP is 48 mg/L (elevated, ref < 5 mg/L).',
        vitalTrends: {
          bloodPressure: '96/60 mmHg (Sitting) / 82/52 mmHg (Standing)',
          heartRate: '124 bpm',
          respiratoryRate: '24 cpm',
          temperature: '38.3 °C',
          oxygenSaturation: '95% on room air'
        },
        diagnosticOrLabData: {
          'Clozapine Dose': '250 mg daily (Week 3)',
          'Cardiac Troponin I': '0.18 ng/mL (HIGH)',
          'C-Reactive Protein (CRP)': '48 mg/L (HIGH)',
          'Total WBC': '6,200 /mcL',
          'Absolute Neutrophil Count (ANC)': '3,800 /mcL',
          'ECG': 'Sinus tachycardia (124 bpm), ST-T depressions in V4-V6'
        },
        questionPrompt:
          'Based on the clinical presentation and diagnostic findings, which combination of cues should the postgraduate mental health nurse recognize as highly indicative of an early, life-threatening adverse reaction to Clozapine?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'Normal psychotropic sedation and expected benign drug-induced fever',
            isCorrect: false,
            explanation: 'While benign fever occurs, elevated troponin, tachycardia out of proportion to fever, and chest tightness are red flags for myocarditis.'
          },
          {
            id: 'B',
            text: 'Clozapine-induced acute myocarditis signaled by resting tachycardia, fever, elevated cardiac troponin I, and high CRP during the first 4 weeks of titration',
            isCorrect: true,
            explanation: 'Clozapine-induced myocarditis occurs predominantly within the first 2–6 weeks of titration. The triad of fever, resting tachycardia, elevated CRP, and raised cardiac troponin is diagnostic of drug-induced myocarditis until proven otherwise.'
          },
          {
            id: 'C',
            text: 'Severe Clozapine-induced agranulocytosis with secondary bacterial pneumonia',
            isCorrect: false,
            explanation: 'The ANC is 3,800 /mcL (well within the normal "Green" safe range > 1,500 /mcL), ruling out agranulocytosis.'
          },
          {
            id: 'D',
            text: 'Typical orthostatic hypotension alone without myocardial involvement',
            isCorrect: false,
            explanation: 'Orthostasis is present, but elevated troponin and CRP indicate active myocardial inflammation and damage.'
          }
        ],
        clinicalRationale:
          'Clozapine-induced myocarditis occurs in up to 3% of patients, predominantly within the first 4 weeks. Early recognition of elevated inflammatory and cardiac markers saves lives.'
      },
      {
        stageNumber: 2,
        cognitiveLevel: 'Analyze Cues',
        clinicalProgressNote:
          'The nurse reviews the patient’s weekly complete blood count (CBC) with differential against the Clozapine Risk Evaluation and Mitigation Strategy (REMS) statutory monitoring registry. The nurse compares baseline and current laboratory parameters to assess systemic involvement.',
        diagnosticOrLabData: {
          'Baseline ANC (Pre-treatment)': '4,200 /mcL',
          'Current ANC (Week 3)': '3,800 /mcL',
          'Serum Clozapine Level': '320 mcg/L (Therapeutic range: 350–600 mcg/L)',
          'Echocardiogram': 'Left ventricular ejection fraction (LVEF) decreased to 44% with mild apical hypokinesia'
        },
        questionPrompt:
          'In analyzing these findings, what is the underlying pathophysiology driving the patient’s cardiac decompensation, and what is the status of the hematopoietic system?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'Severe eosinophilic myocardial hypersensitivity reaction with preserved bone marrow granulopoiesis',
            isCorrect: true,
            explanation: 'Clozapine-induced myocarditis is an IgE/eosinophil-mediated type I/IV hypersensitivity reaction causing myocardial necrosis. Granulopoiesis is intact because ANC remains normal.'
          },
          {
            id: 'B',
            text: 'Direct toxic dose-dependent cardiac overdose because serum clozapine level is in the toxic range',
            isCorrect: false,
            explanation: 'Serum level is 320 mcg/L, which is actually below the typical therapeutic threshold (350 mcg/L); myocarditis is idiosyncratic, not dose-dependent.'
          },
          {
            id: 'C',
            text: 'Severe viral pericarditis completely unrelated to Clozapine therapy',
            isCorrect: false,
            explanation: 'Attributing this to a viral syndrome in a patient during the 3-week clozapine initiation window without ruling out drug-induced myocarditis is dangerous malpractice.'
          },
          {
            id: 'D',
            text: 'Subacute bacterial endocarditis requiring only antibiotic therapy while continuing clozapine',
            isCorrect: false,
            explanation: 'Endocardial vegetations are absent; the presentation is classic drug-induced myocardial necrosis.'
          }
        ],
        clinicalRationale:
          'Understanding that clozapine myocarditis is an idiosyncratic hypersensitivity phenomenon enables nurses to act swiftly regardless of dose or serum levels.'
      },
      {
        stageNumber: 3,
        cognitiveLevel: 'Prioritize Hypotheses',
        clinicalProgressNote:
          'The multidisciplinary psychiatric team evaluates potential differential diagnoses for the patient’s deteriorating cardiopulmonary status: (1) Clozapine-induced myocarditis, (2) Clozapine-induced agranulocytosis with sepsis, (3) Pulmonary embolism due to Clozapine-induced sedation and venous stasis, (4) Benign transient drug-induced fever.',
        questionPrompt:
          'Which diagnostic hypothesis carries the highest immediate risk of mortality and must be prioritized for urgent intervention?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'Benign Clozapine titration fever: continue titration and administer oral paracetamol',
            isCorrect: false,
            explanation: 'Elevated troponin and decreased LVEF rule out benign fever.'
          },
          {
            id: 'B',
            text: 'Clozapine-induced Acute Myocarditis with emerging congestive heart failure and cardiogenic shock',
            isCorrect: true,
            explanation: 'Clozapine myocarditis has a case-fatality rate of up to 10–20% if clozapine is not discontinued immediately. Left ventricular dysfunction (LVEF 44%) signals imminent cardiogenic collapse.'
          },
          {
            id: 'C',
            text: 'Mild upper respiratory tract infection: initiate azithromycin and increase clozapine to 300 mg',
            isCorrect: false,
            explanation: 'Increasing the clozapine dose would be lethal.'
          },
          {
            id: 'D',
            text: 'Severe Clozapine constipation with paralytic ileus',
            isCorrect: false,
            explanation: 'While clozapine causes hypomotility, the clinical presentation here is unambiguously cardiopulmonary.'
          }
        ],
        clinicalRationale:
          'Prioritization must always target the condition presenting the most immediate threat to life (Airway/Circulation/Myocardial integrity).'
      },
      {
        stageNumber: 4,
        cognitiveLevel: 'Generate Solutions',
        clinicalProgressNote:
          'The nurse consults clinical clozapine management guidelines (Australian/New Zealand and US FDA REMS protocols) to establish a comprehensive management plan.',
        questionPrompt:
          'Which set of clinical actions constitutes the definitive evidence-based management protocol for confirmed Clozapine-induced myocarditis?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'Reduce clozapine dose by 50%, start high-dose aspirin, and review in 1 week',
            isCorrect: false,
            explanation: 'Clozapine cannot be reduced; it must be stopped immediately.'
          },
          {
            id: 'B',
            text: 'Permanent, immediate discontinuation of Clozapine, emergency cardiology transfer, strict prohibition of future Clozapine rechallenge, and supportive heart failure therapy',
            isCorrect: true,
            explanation: 'Guidelines dictate immediate and PERMANENT cessation of Clozapine upon confirmation of myocarditis (elevated troponin > 2x upper limit or new LV dysfunction). Future rechallenge is strictly contraindicated due to near-100% fatal recurrence.'
          },
          {
            id: 'C',
            text: 'Withhold Clozapine for 48 hours until fever resolves, then resume titration with prophylactic propranolol',
            isCorrect: false,
            explanation: 'Re-exposing a patient to clozapine after confirmed myocarditis triggers catastrophic fulminant myocarditis.'
          },
          {
            id: 'D',
            text: 'Switch from oral clozapine to intramuscular haloperidol depot immediately',
            isCorrect: false,
            explanation: 'Depot haloperidol is contraindicated in an unstable, cardiotoxic state.'
          }
        ],
        clinicalRationale:
          'Permanent cessation and strict lifetime contraindication to clozapine rechallenge are mandatory in clozapine-induced myocarditis.'
      },
      {
        stageNumber: 5,
        cognitiveLevel: 'Take Action',
        clinicalProgressNote:
          'The nurse implements the emergency protocol. The psychiatric prescriber is alerted, Clozapine is marked as an absolute allergy in the health record, and cardiology takes over ICU care. The nurse must now formulate a safe transition plan for the patient’s psychiatric symptoms.',
        questionPrompt:
          'Which nursing intervention is essential to prevent severe "cholinergic rebound" and acute rebound psychosis following the abrupt discontinuation of Clozapine?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'Administer an anticholinergic agent (such as Diphenhydramine or Benztropine) and consider bridging with a non-clozapine atypical antipsychotic once cardiac status stabilizes',
            isCorrect: true,
            explanation: 'Clozapine has potent anticholinergic and antimuscarinic activity. Abrupt cessation precipitates severe cholinergic rebound (sweating, vomiting, diarrhea, severe insomnia) and rapid rebound supersensitivity psychosis. Anticholinergic cover mitigates this crisis.'
          },
          {
            id: 'B',
            text: 'Administer high-dose intravenous Neostigmine to enhance cholinergic neurotransmission',
            isCorrect: false,
            explanation: 'Neostigmine would drastically worsen cholinergic excess.'
          },
          {
            id: 'C',
            text: 'Withhold all psychiatric support and isolate the patient in seclusion for 3 weeks',
            isCorrect: false,
            explanation: 'Isolating a critically ill medical patient is severe malpractice.'
          },
          {
            id: 'D',
            text: 'Immediately administer Olanzapine 30 mg IV stat',
            isCorrect: false,
            explanation: 'Olanzapine shares structural similarities with clozapine and poses cardiac risks in an unstable myocarditis patient.'
          }
        ],
        clinicalRationale:
          'Nurses must anticipate the physiological consequences of abrupt clozapine withdrawal—principally cholinergic rebound—while safeguarding cardiac stability.'
      },
      {
        stageNumber: 6,
        cognitiveLevel: 'Evaluate Outcomes',
        clinicalProgressNote:
          'Day 10 post-Clozapine cessation. The patient has been managed in the coronary care unit with ACE inhibitors and beta blockers. Cardiac troponin has normalized to < 0.02 ng/mL, CRP is 4.2 mg/L, resting heart rate is 76 bpm, and repeat echocardiogram shows recovery of LVEF to 52%. The patient’s auditory hallucinations are re-emerging.',
        questionPrompt:
          'In evaluating the outcome and future psychiatric plan for this patient with treatment-resistant schizophrenia, which alternative evidence-based treatment modality should the nurse advocate for in the multidisciplinary conference?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'A cautious re-trial of Clozapine at micro-doses with daily troponin monitoring',
            isCorrect: false,
            explanation: 'Rechallenge with clozapine after confirmed myocarditis is strictly prohibited due to fatal recurrence risk.'
          },
          {
            id: 'B',
            text: 'Electroconvulsive Therapy (ECT) augmentation or treatment with an alternative antipsychotic with low cardiotoxicity (e.g., Aripiprazole or Amisulpride) once full cardiac clearance is granted',
            isCorrect: true,
            explanation: 'ECT is highly effective in treatment-resistant schizophrenia refractory to or unable to tolerate clozapine. Aripiprazole/Amisulpride have minimal cardiac toxicity and no cross-reactivity for clozapine myocarditis.'
          },
          {
            id: 'C',
            text: 'Immediate discharge with no further antipsychotic medications ever prescribed',
            isCorrect: false,
            explanation: 'The patient has treatment-resistant schizophrenia and requires ongoing compassionate psychiatric care.'
          },
          {
            id: 'D',
            text: 'Initiation of high-dose Tricyclic Antidepressants',
            isCorrect: false,
            explanation: 'TCAs are cardiotoxic and would worsen cardiac recovery while failing to treat schizophrenia.'
          }
        ],
        clinicalRationale:
          'Successful psychiatric nursing care balances absolute physical safety with long-term recovery planning for refractory psychiatric illness.'
      }
    ]
  },
  {
    id: 'ngn-case-2-bipolar-lithium',
    title: 'Bipolar I Disorder with Acute Lithium Toxicity & Renal Dehydration',
    subtitle: 'NCSBN Clinical Judgment Model: TDM, Drug Interactions & Hemodialysis Criteria',
    clinicalSummary:
      'A 42-year-old female with Bipolar I Disorder maintained on Lithium Carbonate 900 mg/day for 6 years develops acute enteritis with vomiting and diarrhea. She self-medicated with over-the-counter Ibuprofen 400 mg TDS for musculoskeletal pain. She is brought to the emergency department by her sister with coarse hand tremors, unsteady gait, slurred speech, and lethargy.',
    patientDemographics: {
      name: 'Victoria Obi',
      age: 42,
      gender: 'Female',
      admissionDiagnosis: 'Bipolar I Disorder with Acute-on-Chronic Lithium Toxicity'
    },
    stages: [
      {
        stageNumber: 1,
        cognitiveLevel: 'Recognize Cues',
        clinicalProgressNote:
          'Patient arrives disoriented to date. Sister states the patient developed gastrointestinal gastroenteritis 4 days ago with watery diarrhea (6-8 stools/day) and poor oral fluid intake. Two days ago, the patient started taking Ibuprofen 400 mg three times daily. On examination: gross coarse tremors of hands, fasciculations, dysarthria, ataxia (unable to walk unassisted), hyperreflexia, and myoclonus.',
        vitalTrends: {
          bloodPressure: '92/58 mmHg (Severe Dehydration)',
          heartRate: '106 bpm',
          respiratoryRate: '18 cpm',
          temperature: '36.8 °C',
          oxygenSaturation: '98% on room air'
        },
        diagnosticOrLabData: {
          'Serum Lithium Level': '2.85 mmol/L (Therapeutic: 0.6–1.0 mmol/L)',
          'Serum Creatinine': '210 mcmol/L (Baseline: 74 mcmol/L)',
          'Blood Urea Nitrogen (BUN)': '22 mmol/L (Elevated)',
          'Serum Sodium': '131 mmol/L',
          'Serum Potassium': '3.2 mmol/L',
          'Estimated GFR': '24 mL/min/1.73m² (Baseline: 88)'
        },
        questionPrompt:
          'Which clinical and laboratory cues recognized by the postgraduate mental health nurse confirm acute severe Lithium toxicity?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'Mild fine postural tremor and therapeutic lithium level < 1.0 mmol/L',
            isCorrect: false,
            explanation: 'The tremor is coarse, and the lithium level is 2.85 mmol/L (severe toxicity).'
          },
          {
            id: 'B',
            text: 'Coarse tremors, ataxia, dysarthria, serum lithium level of 2.85 mmol/L, and acute kidney injury with creatinine tripled above baseline',
            isCorrect: true,
            explanation: 'Serum lithium > 2.5 mmol/L constitutes severe, life-threatening toxicity manifested by neurotoxicity (coarse tremor, ataxia, dysarthria, myoclonus) and acute renal impairment.'
          },
          {
            id: 'C',
            text: 'Expected minor side effects of nonsteroidal anti-inflammatory therapy with normal lithium levels',
            isCorrect: false,
            explanation: 'The patient has severe neurotoxicity and renal failure directly caused by the NSAID-induced reduction of lithium excretion.'
          },
          {
            id: 'D',
            text: 'Catatonic schizophrenia with mutism and water intoxication',
            isCorrect: false,
            explanation: 'The clinical picture is classic lithium poisoning with elevated laboratory confirmation.'
          }
        ],
        clinicalRationale:
          'Recognizing the difference between benign fine tremors (therapeutic) and coarse tremors with ataxia/dysarthria (severe toxicity) is a foundational psychiatric nursing competency.'
      },
      {
        stageNumber: 2,
        cognitiveLevel: 'Analyze Cues',
        clinicalProgressNote:
          'The nurse analyzes the pharmacokinetic mechanism that precipitated this severe toxic surge in a patient previously stable on lithium for 6 years.',
        questionPrompt:
          'What two convergent pharmacological and physiological mechanisms precipitated this dangerous rise in serum lithium concentration?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'Volume depletion from diarrhea causing compensatory proximal renal sodium/lithium reabsorption, combined with Ibuprofen inhibiting renal prostaglandin synthesis and reducing GFR',
            isCorrect: true,
            explanation: 'Lithium is handled identically to sodium in the proximal renal tubule. Volume depletion triggers aldosterone and proximal sodium/lithium avidity. NSAIDs (Ibuprofen) inhibit renal vasodilatory prostaglandins, decreasing afferent arteriolar perfusion and slashing lithium clearance by 30–50%.'
          },
          {
            id: 'B',
            text: 'Hepatic CYP450 enzyme induction by Ibuprofen accelerating lithium activation in the liver',
            isCorrect: false,
            explanation: 'Lithium is an elemental cation; it is 100% renally excreted and undergoes zero hepatic metabolism.'
          },
          {
            id: 'C',
            text: 'Allergic cross-reaction between Ibuprofen and enteric-coated lithium pills',
            isCorrect: false,
            explanation: 'This is a pharmacokinetic interaction altering renal excretion, not an allergic reaction.'
          },
          {
            id: 'D',
            text: 'Excessive renal tubular secretion of lithium stimulated by dehydration',
            isCorrect: false,
            explanation: 'Dehydration decreases lithium clearance, causing massive drug accumulation.'
          }
        ],
        clinicalRationale:
          'Lithium has no hepatic metabolism; renal clearance and sodium balance dictate toxicity. NSAIDs, ACE inhibitors, and thiazide diuretics are notorious high-risk precipitants.'
      },
      {
        stageNumber: 3,
        cognitiveLevel: 'Prioritize Hypotheses',
        clinicalProgressNote:
          'Serum lithium level is re-checked on a stat blood draw: confirmed at 2.92 mmol/L. The patient is increasingly somnolent, experiencing generalized myoclonic jerks and oliguria (urine output 15 mL/hour over past 2 hours).',
        questionPrompt:
          'Which clinical complication must the nurse prioritize as the most imminent threat to the patient’s neurological and physical survival?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'Irreversible cerebellar neurotoxicity (SILENT syndrome), status epilepticus, and permanent anuric acute tubular necrosis',
            isCorrect: true,
            explanation: 'Severe lithium toxicity (> 2.5 mmol/L) causes permanent neurological damage, particularly cerebellar Purkinje cell loss (Syndrome of Irreversible Lithium-Effectuated Neurotoxicity - SILENT), non-convulsive status epilepticus, and renal shutdown.'
          },
          {
            id: 'B',
            text: 'Transient insomnia and rapid switch to hypomania',
            isCorrect: false,
            explanation: 'The patient is toxic and somnolent, not manic.'
          },
          {
            id: 'C',
            text: 'Mild thyroid goiter development',
            isCorrect: false,
            explanation: 'Goiter is a chronic side effect of lithium, not an acute emergency.'
          },
          {
            id: 'D',
            text: 'Excessive weight gain',
            isCorrect: false,
            explanation: 'Completely irrelevant to an acute toxic crisis.'
          }
        ],
        clinicalRationale:
          'The priority is preventing permanent cerebellar disability (SILENT syndrome) and multiorgan failure.'
      },
      {
        stageNumber: 4,
        cognitiveLevel: 'Generate Solutions',
        clinicalProgressNote:
          'The nurse reviews nephrology and toxicology consultation criteria for hemodialysis in lithium toxicity.',
        questionPrompt:
          'Based on statutory psychiatric toxicology guidelines, which definitive intervention is indicated for this patient with a lithium level of 2.9 mmol/L and acute renal impairment?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'Increase oral fluid intake with 2 liters of plain water and recheck levels tomorrow',
            isCorrect: false,
            explanation: 'The patient is obtunded (aspiration risk) and water alone worsens hyponatremia; oral fluids cannot clear a level of 2.9 mmol/L.'
          },
          {
            id: 'B',
            text: 'Immediate discontinuation of Lithium and Ibuprofen, IV 0.9% Normal Saline hydration, and urgent preparation for Emergent Hemodialysis',
            isCorrect: true,
            explanation: 'Hemodialysis is the treatment of choice for lithium toxicity when serum level is > 2.5 mmol/L with neurotoxicity or severe renal impairment (EXTRIP criteria).'
          },
          {
            id: 'C',
            text: 'Administer activated charcoal 50g orally',
            isCorrect: false,
            explanation: 'Activated charcoal does NOT bind elemental metals or lithium ions; it is useless in lithium poisoning.'
          },
          {
            id: 'D',
            text: 'Administer intravenous loop diuretics (Furosemide 80 mg) to force lithium diuresis',
            isCorrect: false,
            explanation: 'Loop and thiazide diuretics worsen volume depletion and sodium loss, drastically increasing lithium toxicity.'
          }
        ],
        clinicalRationale:
          'Hemodialysis directly and rapidly clears lithium ions from the intravascular compartment before irreversible neuronal uptake occurs.'
      },
      {
        stageNumber: 5,
        cognitiveLevel: 'Take Action',
        clinicalProgressNote:
          'The nephrology team is placing a vascular catheter for hemodialysis. While preparing the patient, the nurse initiates immediate intravenous crystalloid resuscitation.',
        questionPrompt:
          'Which IV crystalloid solution must the nurse infuse, and what is the pharmacological rationale for its specific selection?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: '5% Dextrose in Water (D5W) to provide calories to the brain',
            isCorrect: false,
            explanation: 'D5W contains no sodium; it causes hyponatremia and worsens proximal tubular lithium reabsorption.'
          },
          {
            id: 'B',
            text: '0.9% Normal Saline (isotonic NaCl) at 200 mL/hr to restore intravascular volume, replenish sodium, and promote renal competitive excretion of lithium',
            isCorrect: true,
            explanation: 'Normal Saline (0.9% NaCl) restores renal perfusion and delivers sodium ions to the proximal tubule, competitively inhibiting lithium reabsorption and promoting urinary excretion.'
          },
          {
            id: 'C',
            text: '0.45% Half-Normal Saline with 40 mEq Potassium Chloride bolus',
            isCorrect: false,
            explanation: 'Hypotonic saline is suboptimal; isotonic saline is required for volume restoration and sodium delivery.'
          },
          {
            id: 'D',
            text: 'Colloid albumin infusion exclusively without crystalloid',
            isCorrect: false,
            explanation: 'Crystalloid sodium chloride is the standard evidence-based solution.'
          }
        ],
        clinicalRationale:
          'Isotonic normal saline restores renal perfusion and sodium balance, reducing tubular lithium uptake.'
      },
      {
        stageNumber: 6,
        cognitiveLevel: 'Evaluate Outcomes',
        clinicalProgressNote:
          'Following a 6-hour session of hemodialysis, the patient’s post-dialysis serum lithium level falls to 0.95 mmol/L. She is more alert and speech is clearer. However, 8 hours later, the laboratory alerts the nurse that the serum lithium level has risen back to 1.70 mmol/L.',
        questionPrompt:
          'How should the postgraduate mental health nurse explain this secondary rebound rise in serum lithium level, and what is the necessary clinical response?',
        questionType: 'multiple-choice',
        options: [
          {
            id: 'A',
            text: 'The patient secretly ingested more lithium tablets while in the dialysis unit',
            isCorrect: false,
            explanation: 'Unfounded suspicion; this is a known pharmacokinetic property of lithium.'
          },
          {
            id: 'B',
            text: 'Lithium has a large volume of distribution and slowly redistributes from intracellular tissues (brain, muscle) back into the intravascular space; repeat hemodialysis or continuous renal replacement therapy (CRRT) may be required',
            isCorrect: true,
            explanation: 'Lithium equilibrates slowly between intracellular and extracellular compartments. Hemodialysis clears the vascular compartment rapidly, but intracellular stores rebound over 6–12 hours, frequently necessitating second-stage dialysis or CRRT.'
          },
          {
            id: 'C',
            text: 'Laboratory error; discard the result and take no action',
            isCorrect: false,
            explanation: 'Assuming a lab error when dealing with rebound neurotoxicity is dangerous negligence.'
          },
          {
            id: 'D',
            text: 'The patient has developed nephrogenic diabetes insipidus and requires desmopressin stat',
            isCorrect: false,
            explanation: 'Rebound elevation reflects tissue equilibration, not central diabetes insipidus.'
          }
        ],
        clinicalRationale:
          'Postgraduate nurses must anticipate the two-compartment pharmacokinetics of lithium and the post-dialysis rebound phenomenon.'
      }
    ]
  }
];
