/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { CAOSCEStation } from '../types/clinicalExams';

export const CAOSCE_STATIONS: CAOSCEStation[] = [
  {
    id: 'station-1-acute-agitation',
    stationNumber: 1,
    title: 'Acute Psychiatric Emergency & Rapid Tranquilization',
    subTitle: 'Verbal De-escalation, Environmental Safety, MSE & Emergency Medication Protocol',
    specialtyDomain: 'Psychiatric Emergency & Crisis Intervention',
    clinicalScenario:
      'A 24-year-old male university undergraduate is escorted to the psychiatric emergency crisis room by campus security. He is acutely restless, pacing aggressively, shouting at auditory hallucinations, and gripping a jagged broken glass ornament in his right hand. He exhibits persecutory delusions believing security personnel and the nursing team are government agents sent to extract microchips from his brain. His roommate reports he has been completely sleepless for 96 hours, has ceased food/fluid intake, and posted a farewell suicide note on social media.',
    doorBriefing:
      'Candidate Door Brief: You are the Senior Postgraduate Mental Health Nurse in charge of the Psychiatric Emergency Assessment Unit. A 24-year-old acutely agitated, psychotic patient with a sharp glass object is in the interview room. You have 10 minutes to execute a safe verbal de-escalation, secure the environment, perform a focused mental state examination, and initiate the emergency rapid tranquilization protocol. You will then have 10 minutes to answer 10 scenario-linked clinical MCQs.',
    candidateInstructions: [
      'Maintain personal and environmental safety throughout the encounter.',
      'Establish therapeutic communication and execute verbal de-escalation.',
      'Safely negotiate the surrender of the sharp object without physical struggle.',
      'Assess risk of imminent violence, suicide, and medical deterioration.',
      'Select and prepare appropriate rapid tranquilization medications adhering to statutory guidelines.',
      'Plan post-sedation clinical monitoring parameters and dystonic reaction prophylaxis.'
    ],
    patientProfile: {
      name: 'Chinedu Eze',
      age: 24,
      gender: 'Male',
      setting: 'Psychiatric Emergency Crisis Suite (Dual Exit Room)',
      chiefComplaint: 'Violent agitation, persecutory delusions, sleeplessness for 4 days, carrying a sharp glass object.',
      historyOfPresentIllness: 'Rapidly deteriorating over the past 2 weeks following university exam failure. Ceased sleep 4 days ago. Auditory command hallucinations instructing him to cleanse the world before 24:00.',
      pastPsychiatricHistory: 'One previous brief psychotic episode at age 21, defaulted outpatient follow-up.',
      medicalAndSubstanceHistory: 'Occasional cannabis use reported by roommate; no known cardiac or respiratory disease.',
      currentMedications: ['None currently (defaulted risperidone 2 years ago)'],
      allergies: ['No known drug allergies (NKDA)']
    },
    entryVitals: {
      bloodPressure: '148/94 mmHg',
      heartRate: '116 bpm (Sinus Tachycardia)',
      respiratoryRate: '24 cpm',
      temperature: '37.2 °C',
      oxygenSaturation: '98% on ambient air',
      painOrDistressScore: 'Severe Agitation (BVC Score: 5/6, Agitation Calming Score: 1/7)'
    },
    equipmentTray: [
      'Therapeutic crisis room with two unobstructed egress doors',
      'Columbia-Suicide Severity Rating Scale (C-SSRS) instrument',
      'Brøset Violence Checklist (BVC) tracking sheet',
      'Rapid tranquilization medications: Haloperidol 5mg/mL, Lorazepam 2mg/mL, Olanzapine 10mg IM vial, Promethazine 25mg/mL',
      'Emergency physical restraint equipment and portable vitals monitor with pulse oximeter'
    ],
    fatalErrorNotice:
      'CRITICAL RED FLAG / FATAL ERROR: Any attempt to physically lunge or tackle the patient to grab the weapon, blocking your own emergency exit path, or administering high-dose haloperidol without obtaining baseline ECG/cardiac risk assessment or dystonia antidote on standby triggers an automatic Station Referral (Score capped at 49%).',
    checklist: [
      {
        id: 'st1-c1',
        stepNumber: 1,
        instruction: 'Establish environmental safety, position self between patient and exit door with an unobstructed egress route, and ensure security backup is visible but outside the room.',
        rationale: 'Personal safety is paramount in psychiatric crises. Never position the patient between yourself and the exit.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Cornering yourself without an egress route compromises clinical safety and creates a severe hostage/assault hazard.',
        category: 'Preparation & Safety'
      },
      {
        id: 'st1-c2',
        stepNumber: 2,
        instruction: 'Assume a non-threatening, open posture (45-degree angle, hands visible and open, maintaining a minimum physical distance of two arm lengths).',
        rationale: 'Direct frontal eye-to-eye squaring is perceived by paranoid, delusional patients as an aggressive challenge.',
        points: 10,
        isCriticalFail: false,
        category: 'Preparation & Safety'
      },
      {
        id: 'st1-c3',
        stepNumber: 3,
        instruction: 'Communicate with a low, calm, modulated pitch, introduce self clearly, and validate the patient’s fear without validating or arguing with delusional content.',
        rationale: 'Delusions are fixed false beliefs; challenging them heightens paranoia, while validating the underlying terror builds rapport.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st1-c4',
        stepNumber: 4,
        instruction: 'De-escalate and verbally negotiate the surrender of the sharp object by directing the patient to set it down on a designated table (zero physical lunging).',
        rationale: 'Physical force when an agitated patient holds a sharp object dramatically escalates trauma risk for both patient and staff.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Attempting to physically wrestle or snatch a sharp glass weapon from an acutely agitated psychotic patient is dangerous malpractice.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st1-c5',
        stepNumber: 5,
        instruction: 'Administer the Brøset Violence Checklist (BVC) and screen for acute command hallucinations and suicidal intent (Columbia C-SSRS).',
        rationale: 'Standardized violence and suicide risk tools provide evidence-based justification for restrictive interventions or sedation.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st1-c6',
        stepNumber: 6,
        instruction: 'Offer oral rapid tranquilization first (e.g. Oral Lorazepam 1-2 mg + Oral Olanzapine 10 mg or Risperidone 2 mg) before moving to involuntary parenteral administration.',
        rationale: 'National and international guidelines (NICE NG10, WAPCNM) dictate that oral medication must be offered before intramuscular injection.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st1-c7',
        stepNumber: 7,
        instruction: 'When oral therapy is refused and violence is imminent, prepare guideline-approved IM rapid tranquilization: IM Lorazepam 1-2 mg OR IM Haloperidol 2.5-5 mg combined with Promethazine 25-50 mg.',
        rationale: 'Co-administering an anticholinergic/antihistamine (promethazine) with haloperidol prevents acute dystonic reactions and oculogyric crises.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Administering parenteral haloperidol without promethazine or diphenhydramine available risks catastrophic acute laryngeal dystonia and airway compromise.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st1-c8',
        stepNumber: 8,
        instruction: 'Execute physical restraint only as a last resort using a trained 5-person team under nursing leadership, ensuring prone position is strictly avoided.',
        rationale: 'Prone restraint carries high risk of positional asphyxiation and cardiac arrest; supine with head elevated is mandatory.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Restraining a patient in the prone position or applying downward thoracic pressure violates human rights and causes positional asphyxiation.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st1-c9',
        stepNumber: 9,
        instruction: 'Implement post-tranquilization continuous monitoring: record BP, pulse, SpO2, respiratory rate, and sedation depth (AVPU/RASS) every 15 minutes for 1 hour, then every 30 minutes.',
        rationale: 'Rapid tranquilization carries risks of respiratory depression, severe hypotension, and cardiac arrhythmias.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      },
      {
        id: 'st1-c10',
        stepNumber: 10,
        instruction: 'Conduct post-incident debriefing with the patient once settled, document all interventions in statutory legal ledgers, and inform the multidisciplinary consultant psychiatrist.',
        rationale: 'Therapeutic alliance reconstruction and legal documentation are required under mental health legislation.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      }
    ],
    mcqs: [
      {
        id: 'st1-q1',
        questionNumber: 1,
        questionText: 'According to international psychiatric emergency guidelines (NICE, WAPCNM), what is the first-line pharmacologic approach for an acutely agitated patient requiring rapid tranquilization who is willing to take oral medication?',
        options: [
          { id: 'A', text: 'Intramuscular Haloperidol 10 mg combined with Diazepam 10 mg' },
          { id: 'B', text: 'Oral Lorazepam 1–2 mg alone or combined with Oral Olanzapine 10 mg' },
          { id: 'C', text: 'Intravenous Midazolam 5 mg bolus followed by infusion' },
          { id: 'D', text: 'Oral Chlorpromazine 200 mg with oral Clonazepam 4 mg' }
        ],
        correctAnswer: 'B',
        explanation: 'Oral medication (Oral Lorazepam 1-2 mg with an atypical antipsychotic like Olanzapine 10 mg) is always preferred over parenteral injection as it preserves autonomy and reduces physical confrontation trauma.',
        learningDomain: 'Psychopharmacology'
      },
      {
        id: 'st1-q2',
        questionNumber: 2,
        questionText: 'When administering intramuscular Haloperidol for rapid tranquilization, why is promethazine or diphenhydramine routinely co-administered or immediately accessible?',
        options: [
          { id: 'A', text: 'To accelerate the hepatic clearance of the antipsychotic' },
          { id: 'B', text: 'To prevent acute extrapyramidal dystonic reactions such as laryngospasm and torticollis' },
          { id: 'C', text: 'To elevate systolic blood pressure and prevent orthostatic syncope' },
          { id: 'D', text: 'To prevent metabolic syndrome and rapid weight gain' }
        ],
        correctAnswer: 'B',
        explanation: 'High-potency first-generation antipsychotics carry a high incidence of acute dystonia in young males. Anticholinergic antihistamines (promethazine/diphenhydramine) prevent severe dystonic crises, including life-threatening laryngospasm.',
        learningDomain: 'Adverse Drug Reaction Prevention'
      },
      {
        id: 'st1-q3',
        questionNumber: 3,
        questionText: 'A score of 4 or higher on the Brøset Violence Checklist (BVC) indicates which of the following clinical realities?',
        options: [
          { id: 'A', text: 'Low risk of violence; patient can be discharged home safely' },
          { id: 'B', text: 'Moderate risk requiring routine ward nursing rounds every 4 hours' },
          { id: 'C', text: 'High risk of imminent physical violence within the next 24 hours requiring proactive preventative measures' },
          { id: 'D', text: 'Definite psychogenic malingering requiring immediate disciplinary discharge' }
        ],
        correctAnswer: 'C',
        explanation: 'A BVC score of 3 or greater indicates a high risk of imminent violence, demanding immediate de-escalation, environmental controls, and medication intervention.',
        learningDomain: 'Risk Assessment'
      },
      {
        id: 'st1-q4',
        questionNumber: 4,
        questionText: 'Why is physical restraint in the prone (face-down) position strictly condemned in modern postgraduate psychiatric nursing standards?',
        options: [
          { id: 'A', text: 'It increases the rate of intramuscular drug absorption' },
          { id: 'B', text: 'It causes positional asphyxiation, restriction of chest wall excursion, and sudden cardiac arrest' },
          { id: 'C', text: 'It causes severe peripheral neuropathies in the upper extremities' },
          { id: 'D', text: 'It makes obtaining radial pulse readings impossible' }
        ],
        correctAnswer: 'B',
        explanation: 'Prone restraint restricts diaphragmatic movement and thoracic expansion, leading to hypercapnia, hypoxia, and fatal positional asphyxia, especially in agitated tachycardic patients.',
        learningDomain: 'Patient Safety & Human Rights'
      },
      {
        id: 'st1-q5',
        questionNumber: 5,
        questionText: 'Following rapid tranquilization with parenteral benzodiazepines and antipsychotics, what is the mandatory frequency for recording vital signs during the initial hour?',
        options: [
          { id: 'A', text: 'Every 5 minutes for 2 hours' },
          { id: 'B', text: 'Every 15 minutes for the first hour, then every 30 minutes until ambulating' },
          { id: 'C', text: 'Once at 60 minutes post-injection' },
          { id: 'D', text: 'Every 2 hours provided the patient appears to be sleeping comfortably' }
        ],
        correctAnswer: 'B',
        explanation: 'NICE guidelines and professional psychiatric standards mandate vital sign monitoring (BP, HR, RR, SpO2, sedation level) every 15 minutes for the first hour post-rapid tranquilization to detect early respiratory depression and hypotension.',
        learningDomain: 'Clinical Monitoring'
      },
      {
        id: 'st1-q6',
        questionNumber: 6,
        questionText: 'Which physical finding during de-escalation of a psychotic patient serves as the most reliable indicator of imminent physical assault?',
        options: [
          { id: 'A', text: 'Prolonged silences and refusal to eat' },
          { id: 'B', text: 'Clenched fists, jaw tightening, scanning the room for weapons, and sudden invasion of personal space' },
          { id: 'C', text: 'Sitting slumped in an armchair crying silently' },
          { id: 'D', text: 'Politely requesting a glass of warm water' }
        ],
        correctAnswer: 'B',
        explanation: 'Motor signs of autonomic arousal, clenched fists, jaw clenching, room scanning, and proxemic violations are hallmark behavioral precursors to physical violence.',
        learningDomain: 'Clinical Observation'
      },
      {
        id: 'st1-q7',
        questionNumber: 7,
        questionText: 'If a patient exhibits acute respiratory depression (respiratory rate 6 cpm, SpO2 86%) 20 minutes following intramuscular Lorazepam administration, which antidote should the postgraduate mental health nurse prepare immediately?',
        options: [
          { id: 'A', text: 'Naloxone' },
          { id: 'B', text: 'Flumazenil' },
          { id: 'C', text: 'Physostigmine' },
          { id: 'D', text: 'Atropine' }
        ],
        correctAnswer: 'B',
        explanation: 'Flumazenil is a specific competitive antagonist at the benzodiazepine receptor and reverses benzodiazepine-induced respiratory depression.',
        learningDomain: 'Emergency Pharmacology'
      },
      {
        id: 'st1-q8',
        questionNumber: 8,
        questionText: 'When communicating verbally with a delusional patient gripped by intense paranoia, which nursing response adheres to evidence-based therapeutic communication?',
        options: [
          { id: 'A', text: '"You know that the government cannot implant microchips in human brains, that is scientifically impossible."' },
          { id: 'B', text: '"I can see how terrified and overwhelmed you feel right now. You are safe here with us, and no one will harm you."' },
          { id: 'C', text: '"Yes, the government agents are outside, but I have locked the doors so they cannot enter."' },
          { id: 'D', text: '"If you do not drop the glass immediately, security officers will use force against you."' }
        ],
        correctAnswer: 'B',
        explanation: 'Validating the authentic emotional distress (terror) while explicitly refusing to reinforce or argue with the delusion establishes therapeutic safety and defuses panic.',
        learningDomain: 'Therapeutic Communication'
      },
      {
        id: 'st1-q9',
        questionNumber: 9,
        questionText: 'What is the maximum cumulative dose of Intramuscular Haloperidol recommended within a 24-hour period during rapid tranquilization?',
        options: [
          { id: 'A', text: '5 mg' },
          { id: 'B', text: '20 mg' },
          { id: 'C', text: '50 mg' },
          { id: 'D', text: '100 mg' }
        ],
        correctAnswer: 'B',
        explanation: 'The maximum recommended 24-hour dose of Haloperidol in acute psychiatric emergencies is 20 mg (often restricted to 10–15 mg in frail patients) to minimize ventricular arrhythmia and QTc prolongation risks.',
        learningDomain: 'Pharmacokinetics & Safety'
      },
      {
        id: 'st1-q10',
        questionNumber: 10,
        questionText: 'Which post-incident clinical intervention is essential to prevent psychological traumatization and re-establish a therapeutic alliance following mechanical restraint?',
        options: [
          { id: 'A', text: 'Restricting patient family visiting rights for 14 days' },
          { id: 'B', text: 'Structured debriefing with the candidate/patient exploring triggers, feelings, and future early-warning signals once settled' },
          { id: 'C', text: 'Immediate transfer to a maximum-security prison ward' },
          { id: 'D', text: 'Withholding ward privileges until the patient submits a written apology' }
        ],
        correctAnswer: 'B',
        explanation: 'Post-restraint debriefing explores the emotional experience, repairs trust, clarifies the rationale for safety interventions, and updates the patient crisis prevention plan.',
        learningDomain: 'Post-Crisis Care'
      }
    ]
  },
  {
    id: 'station-2-suicide-risk-safety-plan',
    stationNumber: 2,
    title: 'High-Lethality Suicide Assessment & Structured Safety Planning',
    subTitle: 'Columbia C-SSRS Execution, Lethality Stratification, Means Restriction & Stanley-Brown Protocol',
    specialtyDomain: 'Clinical Suicide Assessment & Safety Architecture',
    clinicalScenario:
      'A 32-year-old female secondary school teacher, mother of two, is brought into the psychiatric outpatient consultation room by her husband. She was discovered 2 hours ago sitting in her car in a closed garage with the engine running, holding an unsealed bottle of 60 tablets of Amitriptyline and a detailed handwritten suicide note dividing her jewelry among her children. She appears severely psychomotor retarded, tearful, avoids eye contact, and whispers: "My children deserve a mother who is not a hopeless burden. If you do not let me finish this tonight, I will find another way before dawn."',
    doorBriefing:
      'Candidate Door Brief: You are the Postgraduate Mental Health Clinical Specialist. A 32-year-old mother with imminent high-lethality suicidal intent and access to lethal means has been admitted. You have 10 minutes to conduct a comprehensive lethality assessment using the Columbia C-SSRS, enforce lethal means restriction, execute a collaborative Stanley-Brown Safety Plan, and determine the legal level of observation. You will then have 10 minutes to complete 10 scenario-linked clinical MCQs.',
    candidateInstructions: [
      'Establish a non-judgmental, compassionate therapeutic climate.',
      'Systematically administer the Columbia-Suicide Severity Rating Scale (C-SSRS).',
      'Assess suicidal ideation intensity, intent, plan, and preparatory behavior.',
      'Identify acute and chronic risk factors versus protective factors.',
      'Collaborate on a 6-step Stanley-Brown Safety Plan with immediate means restriction.',
      'Formulate the mandatory level of nursing observation (Level 3 / 1-to-1 constant line-of-sight).'
    ],
    patientProfile: {
      name: 'Grace Adeleke',
      age: 32,
      gender: 'Female',
      setting: 'Inpatient Psychiatric Admissions Office',
      chiefComplaint: 'Attempted carbon monoxide poisoning and planned tricyclic antidepressant overdose with suicide note.',
      historyOfPresentIllness: 'Severe Major Depressive Disorder, single episode, severe with melancholic features. Insomnia with early morning awakening (03:00) for 8 weeks, 10 kg weight loss, profound anhedonia.',
      pastPsychiatricHistory: 'Postpartum depressive symptoms following birth of second child 18 months ago, untreated.',
      medicalAndSubstanceHistory: 'Chronic tension headaches; prescribed Amitriptyline 50 mg nocte by GP.',
      currentMedications: ['Amitriptyline 50 mg PO at bedtime (stock of 60 tablets sequestered by husband)'],
      allergies: ['NKDA']
    },
    entryVitals: {
      bloodPressure: '108/68 mmHg',
      heartRate: '92 bpm',
      respiratoryRate: '16 cpm',
      temperature: '36.6 °C',
      oxygenSaturation: '99% on ambient air',
      painOrDistressScore: 'Profound Hopelessness (Beck Hopelessness Scale: 18/20; C-SSRS: Level 5 High Lethality)'
    },
    equipmentTray: [
      'Columbia-Suicide Severity Rating Scale (C-SSRS) Lifetime/Recent Protocol',
      'Stanley-Brown Collaborative Safety Planning Template (6-Step)',
      'Lethal means custody surrender form',
      'High-Risk Psychiatric Inpatient Observation Protocol Ledger (Level 3 Constant Line-of-Sight)'
    ],
    fatalErrorNotice:
      'CRITICAL RED FLAG / FATAL ERROR: Relying on a verbal "Contract for Safety" to discharge the patient home, failing to enforce immediate lethal means restriction (sequestering the amitriptyline/car keys), or assigning unsupervised observation to a patient with active high lethality triggers an automatic Station Referral (Score capped at 49%).',
    checklist: [
      {
        id: 'st2-c1',
        stepNumber: 1,
        instruction: 'Create a safe, supportive, private interview setting, ensure privacy, and validate the candidate’s psychological pain with authentic empathy.',
        rationale: 'Patients in deep despair require radical empathy and psychological safety to overcome shame and disclose lethal plans.',
        points: 10,
        isCriticalFail: false,
        category: 'Preparation & Safety'
      },
      {
        id: 'st2-c2',
        stepNumber: 2,
        instruction: 'Directly and unambiguously ask about suicidal ideation, intent, plan, and timing ("Are you thinking about killing yourself? Have you decided how and when?").',
        rationale: 'Direct questioning about suicide does not implant suicidal ideas; it reduces isolation and provides crucial risk data.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Failing to ask direct, explicit questions about suicidal ideation and intent leaves lethal risk unassessed.',
        category: 'Assessment & Communication'
      },
      {
        id: 'st2-c3',
        stepNumber: 3,
        instruction: 'Systematically execute the C-SSRS: evaluate suicidal ideation frequency, duration, controllability, deterrents, and preparatory acts (writing farewell note, gathering pills).',
        rationale: 'Preparatory behaviors significantly correlate with near-term completed suicide.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st2-c4',
        stepNumber: 4,
        instruction: 'Enforce immediate, irreversible lethal means restriction: formally take custody of all medications (Amitriptyline) and ensure vehicle keys/garage access are secured.',
        rationale: 'Means restriction is the most effective evidence-based suicide prevention strategy worldwide (WHO, CDC).',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Failing to secure lethal means (toxic medication and car keys) allows immediate access to fatal completion.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st2-c5',
        stepNumber: 5,
        instruction: 'Explicitly reject the use of a "No-Suicide Contract" (Contract for Safety) as a legal or clinical safeguard, recognizing its lack of empirical validity.',
        rationale: 'Contracts for safety have zero scientific evidence of preventing suicide and induce false complacency among clinical staff.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Relying on a verbal or written "contract for safety" instead of clinical observation and safety planning is gross professional negligence.',
        category: 'Assessment & Communication'
      },
      {
        id: 'st2-c6',
        stepNumber: 6,
        instruction: 'Collaboratively construct Step 1 & 2 of the Stanley-Brown Safety Plan: identify patient-specific warning signs (03:00 insomnia, feeling like a burden) and internal coping strategies.',
        rationale: 'Personalized warning signs alert the patient to execute self-soothing behaviors before suicidal urges become overwhelming.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st2-c7',
        stepNumber: 7,
        instruction: 'Construct Step 3, 4 & 5 of Safety Plan: identify healthy social contacts, trusted family/friends for distraction, and professional crisis hotlines/emergency facilities.',
        rationale: 'Layered social and clinical contacts establish an external safety perimeter during acute escalation.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st2-c8',
        stepNumber: 8,
        instruction: 'Engage the husband in psychoeducation regarding lethal means restriction, environmental safety at home, and the signs of acute depressive relapse.',
        rationale: 'Family involvement provides a crucial buffer and verifies environmental weapon/medication sequestration.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st2-c9',
        stepNumber: 9,
        instruction: 'Assign mandatory Level 3 Constant 1-to-1 Line-of-Sight Observation within an inpatient setting, ensuring the patient is never left unmonitored even in the bathroom.',
        rationale: 'Imminent high lethality requires continuous physical presence within arm reach or direct line of sight.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Leaving an actively suicidal patient with explicit intent unmonitored or in a low-observation bed leads directly to inpatient suicide.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st2-c10',
        stepNumber: 10,
        instruction: 'Complete statutory risk documentation, detail rationale for admission, and schedule immediate psychiatric consultant review for antidepressant initiation/ECT evaluation.',
        rationale: 'High-risk psychiatric decisions require clear defensible clinical records and prompt senior medical review.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      }
    ],
    mcqs: [
      {
        id: 'st2-q1',
        questionNumber: 1,
        questionText: 'Why do modern psychiatric and mental health nursing guidelines universally advise against the clinical use of "No-Suicide Contracts"?',
        options: [
          { id: 'A', text: 'They take too much nursing time to negotiate with patients' },
          { id: 'B', text: 'They have no empirical evidence of reducing suicide and can provide clinical staff with a false sense of security' },
          { id: 'C', text: 'They are legally binding documents that expose the nurse to civil damages' },
          { id: 'D', text: 'They prevent patients from receiving psychopharmacological treatment' }
        ],
        correctAnswer: 'B',
        explanation: 'Extensive psychiatric research demonstrates that "No-Suicide Contracts" do not prevent suicide, can deter patients from expressing escalating suicidal crises, and inappropriately displace clinical responsibility onto a despairing patient.',
        learningDomain: 'Suicide Prevention Methodology'
      },
      {
        id: 'st2-q2',
        questionNumber: 2,
        questionText: 'In the Stanley-Brown Safety Planning Intervention, which of the following represents Step 1 of the protocol?',
        options: [
          { id: 'A', text: 'Contacting professional mental health crisis services' },
          { id: 'B', text: 'Identifying personal warning signs that a suicidal crisis is developing' },
          { id: 'C', text: 'Making the physical environment safe by removing weapons' },
          { id: 'D', text: 'Calling family members to request child care support' }
        ],
        correctAnswer: 'B',
        explanation: 'Step 1 of the Stanley-Brown Safety Plan is recognizing the unique personal warning signs (thoughts, mood changes, physical sensations, behaviors) that signal an approaching crisis.',
        learningDomain: 'Safety Planning'
      },
      {
        id: 'st2-q3',
        questionNumber: 3,
        questionText: 'A patient with severe depression begins treatment on an SSRI (Escitalopram). At day 12, the nurse observes a sudden surge in physical energy and mobility, but the patient remains profoundly hopeless. What is the immediate nursing priority?',
        options: [
          { id: 'A', text: 'Discharge the patient because the depressive episode is resolving' },
          { id: 'B', text: 'Intensify suicide monitoring, as psychomotor energy often improves before depressive cognitions, creating a high-risk window for suicide execution' },
          { id: 'C', text: 'Immediately discontinue the SSRI due to acute mania' },
          { id: 'D', text: 'Encourage the patient to go for an unescorted weekend home pass' }
        ],
        correctAnswer: 'B',
        explanation: 'Antidepressants frequently resolve psychomotor retardation before relieving hopeless suicidal ideation, granting the patient the physical energy required to carry out a pre-existing lethal plan.',
        learningDomain: 'Clinical Pharmacology & Lethality'
      },
      {
        id: 'st2-q4',
        questionNumber: 4,
        questionText: 'Which class of psychiatric medications carries the highest cardiotoxicity and mortality rate in acute overdose and must be strictly restricted in suicidal patients?',
        options: [
          { id: 'A', text: 'Selective Serotonin Reuptake Inhibitors (SSRIs)' },
          { id: 'B', text: 'Tricyclic Antidepressants (TCAs, e.g., Amitriptyline)' },
          { id: 'C', text: 'Atypical Antipsychotics (e.g., Aripiprazole)' },
          { id: 'D', text: 'Melatonin Receptor Agonists (e.g., Agomelatine)' }
        ],
        correctAnswer: 'B',
        explanation: 'TCAs block cardiac fast sodium channels, causing QRS widening, ventricular tachycardia (torsades de pointes), and fatal refractory cardiogenic shock even in modest overdoses.',
        learningDomain: 'Toxicology & Medication Safety'
      },
      {
        id: 'st2-q5',
        questionNumber: 5,
        questionText: 'Under the Columbia-Suicide Severity Rating Scale (C-SSRS), which level of suicidal ideation is considered the most clinically severe?',
        options: [
          { id: 'A', text: 'Wish to be dead' },
          { id: 'B', text: 'Active suicidal ideation with specific plan and intent' },
          { id: 'C', text: 'Non-specific active suicidal thoughts without methods' },
          { id: 'D', text: 'Active suicidal ideation with any methods (not plan) without intent' }
        ],
        correctAnswer: 'B',
        explanation: 'Level 5 on the C-SSRS represents active suicidal ideation with explicit plan and intent to carry it out, demanding the highest tier of immediate psychiatric containment.',
        learningDomain: 'Psychometric Assessment'
      },
      {
        id: 'st2-q6',
        questionNumber: 6,
        questionText: 'When managing a patient on Level 3 Constant (1-to-1) Line-of-Sight Observation in an inpatient unit, what is the mandatory rule regarding bathroom and shower privacy?',
        options: [
          { id: 'A', text: 'Allow the patient 20 minutes of locked, unmonitored privacy to preserve dignity' },
          { id: 'B', text: 'Maintain continuous visual line-of-sight and physical proximity even while the patient uses the toilet or showers' },
          { id: 'C', text: 'Stand outside the closed bathroom door and knock every 10 minutes' },
          { id: 'D', text: 'Permit unobserved showers provided the husband stays inside the stall' }
        ],
        correctAnswer: 'B',
        explanation: 'Bathrooms and showers are the most common locations for inpatient suicide attempts (hanging, self-strangulation). Level 3 observation requires uninterrupted line of sight at all times.',
        learningDomain: 'Inpatient Safety Standards'
      },
      {
        id: 'st2-q7',
        questionNumber: 7,
        questionText: 'Which cognitive symptom in depressive disorders has the strongest statistical correlation with completed suicide?',
        options: [
          { id: 'A', text: 'Mild forgetfulness' },
          { id: 'B', text: 'Profound hopelessness and perceived burdensomeness' },
          { id: 'C', text: 'Subjective word-finding difficulty' },
          { id: 'D', text: 'Perfectionism regarding work deadlines' }
        ],
        correctAnswer: 'B',
        explanation: 'Hopelessness (Beck Hopelessness Scale) and perceived burdensomeness (Joiner’s Interpersonal Theory) are the most robust cognitive predictors of suicidal behavior.',
        learningDomain: 'Suicide Psychopathology'
      },
      {
        id: 'st2-q8',
        questionNumber: 8,
        questionText: 'A patient with severe depression refuses voluntary inpatient admission, insists on returning home to her car in the garage, and expresses explicit intent to die. What legal action must the postgraduate mental health nurse initiate?',
        options: [
          { id: 'A', text: 'Allow her to leave after signing an Against Medical Advice (AMA) discharge form' },
          { id: 'B', text: 'Initiate emergency statutory involuntary commitment under the relevant Mental Health Legislation for immediate protection of life' },
          { id: 'C', text: 'Advise her husband to monitor her closely at home without medication' },
          { id: 'D', text: 'Give her an appointment to return to the outpatient clinic next week' }
        ],
        correctAnswer: 'B',
        explanation: 'When a patient presents imminent danger of death to herself due to a severe mental disorder and lacks capacity or refuses life-saving care, involuntary commitment is legally and ethically mandated.',
        learningDomain: 'Mental Health Law & Ethics'
      },
      {
        id: 'st2-q9',
        questionNumber: 9,
        questionText: 'Which evidence-based non-pharmacological somatic treatment is considered first-line for patients with severe psychotic depression presenting with imminent suicide risk and complete food/fluid refusal?',
        options: [
          { id: 'A', text: 'Psychoanalytic psychotherapy' },
          { id: 'B', text: 'Electroconvulsive Therapy (ECT)' },
          { id: 'C', text: 'Sleep deprivation therapy' },
          { id: 'D', text: 'Acupuncture' }
        ],
        correctAnswer: 'B',
        explanation: 'Electroconvulsive therapy (ECT) has the most rapid onset of clinical antidepressant action and is life-saving in severe depression with acute high-lethality suicidality, catatonia, or physical exhaustion.',
        learningDomain: 'Somatic Treatments'
      },
      {
        id: 'st2-q10',
        questionNumber: 10,
        questionText: 'In the Interpersonal-Psychological Theory of Suicide (Joiner), what two psychological states combined with the acquired capability for suicide lead to lethal suicidal behavior?',
        options: [
          { id: 'A', text: 'Hypomania and excessive spending' },
          { id: 'B', text: 'Thwarted belongingness and perceived burdensomeness' },
          { id: 'C', text: 'Generalized anxiety and somatic preoccupations' },
          { id: 'D', text: 'Obsessive cleanliness and agoraphobia' }
        ],
        correctAnswer: 'B',
        explanation: 'Joiner’s theory posits that suicidal desire is ignited by the convergence of thwarted belongingness ("I am alone") and perceived burdensomeness ("My loved ones would be better off without me").',
        learningDomain: 'Suicidology Theories'
      }
    ]
  },
  {
    id: 'station-3-nms-vs-serotonin',
    stationNumber: 3,
    title: 'Psychopharmacologic Emergencies: NMS vs Serotonin Toxicity',
    subTitle: 'Differential Diagnosis, Hunter Criteria, Hyperthermia Management, Antidotes & ICU Escalation',
    specialtyDomain: 'Neuropsychiatric Pharmacology & Acute Toxicology',
    clinicalScenario:
      'A 28-year-old male with Schizoaffective Disorder treated with oral Haloperidol 10 mg/day and Fluoxetine 40 mg/day was administered an intramuscular injection of Haloperidol 10 mg and Promethazine 50 mg 14 hours ago in a private clinic for psychomotor agitation. He is rushed to the psychiatric intensive care ward in an acutely obtunded state. His skin is diaphoric and burning hot, his muscles display severe generalized "lead-pipe" rigidity, his jaw is tightly clenched with sialorrhea, and he is mutistic and unresponsive to verbal questions. His family reports his urine in the catheter bag is dark brown like Coca-Cola.',
    doorBriefing:
      'Candidate Door Brief: You are the Senior Postgraduate Mental Health Nurse. A 28-year-old psychiatric patient has developed acute hyperthermia, severe generalized rigidity, altered mental state, and tea-colored urine. You have 10 minutes to differentiate Neuroleptic Malignant Syndrome (NMS) from Serotonin Syndrome and Malignant Catatonia, execute immediate life-saving physical cooling, discontinue offending neuroleptics, initiate medical resuscitation, and monitor for rhabdomyolysis and renal failure. You will then have 10 minutes to answer 10 scenario-linked clinical MCQs.',
    candidateInstructions: [
      'Perform rapid neurological and physical assessment to differentiate NMS from Serotonin Toxicity.',
      'Assess muscle tone ("lead-pipe" rigidity vs hyperreflexia and spontaneous clonus).',
      'Immediately order the cessation of all dopamine-blocking neuroleptics.',
      'Initiate aggressive core cooling protocols for severe hyperthermia.',
      'Assess for rhabdomyolysis and acute kidney injury (dark urine, serum creatine kinase).',
      'Prepare emergency pharmacologic antidotes (Dantrolene, Bromocriptine) and arrange ICU transfer.'
    ],
    patientProfile: {
      name: 'Emeka Nwosu',
      age: 28,
      gender: 'Male',
      setting: 'Psychiatric Intensive Care Unit (PICU) Resuscitation Bay',
      chiefComplaint: 'Profound muscle rigidity, high fever, altered consciousness, and dark brownish urine.',
      historyOfPresentIllness: 'Treated for Schizoaffective Disorder with Haloperidol 10 mg daily for 2 years. Fluoxetine 40 mg added 3 weeks ago. Received Haloperidol 10 mg IM 14 hours ago for agitation.',
      pastPsychiatricHistory: 'Two prior psychiatric admissions; no previous history of malignant hyperthermia.',
      medicalAndSubstanceHistory: 'No chronic physical illness. Family reports severe dehydration during the past 48 hours.',
      currentMedications: ['Haloperidol 10 mg PO daily', 'Fluoxetine 40 mg PO daily', 'Haloperidol 10 mg IM stat (14h ago)'],
      allergies: ['NKDA']
    },
    entryVitals: {
      bloodPressure: '178/104 mmHg (Labile Autonomic Instability)',
      heartRate: '134 bpm (Sinus Tachycardia)',
      respiratoryRate: '28 cpm (Tachypnea)',
      temperature: '40.2 °C (Life-threatening Hyperthermia)',
      oxygenSaturation: '94% on room air',
      painOrDistressScore: 'Glasgow Coma Scale: 9/15 (E2 V2 M5); Severe Lead-Pipe Rigidity'
    },
    equipmentTray: [
      'Core temperature Foley bladder catheter or rectal continuous thermocouple',
      'Active external cooling equipment: ice packs, cooling blankets, electric misting fans',
      'Normal Saline 0.9% IV fluid bags with rapid infusion sets',
      'Serum Creatine Kinase (CK) and renal function test requisition vials',
      'Antidote ampoules: Dantrolene sodium IV, Bromocriptine mesylate (oral/NGT), Cyproheptadine'
    ],
    fatalErrorNotice:
      'CRITICAL RED FLAG / FATAL ERROR: Continuing to administer haloperidol or other dopamine receptor antagonists, failing to initiate immediate core cooling for temperature > 40°C, or omitting IV fluid resuscitation in rhabdomyolysis triggers an automatic Station Referral (Score capped at 49%).',
    checklist: [
      {
        id: 'st3-c1',
        stepNumber: 1,
        instruction: 'Recognize the medical emergency: immediately assess Airway, Breathing, Circulation, and neurological status (GCS) and call for the medical resuscitation team.',
        rationale: 'NMS has a mortality rate up to 10-20% if unrecognized; rapid airway and circulatory stabilization are critical.',
        points: 10,
        isCriticalFail: false,
        category: 'Preparation & Safety'
      },
      {
        id: 'st3-c2',
        stepNumber: 2,
        instruction: 'Immediately identify and discontinue ALL dopamine receptor antagonists (Haloperidol) and withhold any serotonergic agents.',
        rationale: 'Offending neuroleptics perpetuate dopamine D2 receptor blockade in the hypothalamus and basal ganglia, driving the syndrome.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Administering further antipsychotic doses to an NMS patient is fatal malpractice.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st3-c3',
        stepNumber: 3,
        instruction: 'Perform differential neurological exam: check muscle tone for classic "lead-pipe" rigidity across all four extremities versus spontaneous/inducible ocular or ankle clonus.',
        rationale: 'Lead-pipe rigidity is hallmark of NMS; spontaneous or ocular clonus and hyperreflexia point to Serotonin Toxicity (Hunter Criteria).',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st3-c4',
        stepNumber: 4,
        instruction: 'Recognize malignant hyperpyrexia (temp 40.2 °C) and immediately initiate active external cooling: ice packs to axillae/groin, cooling blanket, and fanning.',
        rationale: 'Temperatures above 40°C cause irreversible neuronal death, cerebellar purkinje cell lysis, and multiorgan failure.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Failing to initiate emergency core cooling in a patient with temperature > 40°C leads directly to permanent brain damage and death.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st3-c5',
        stepNumber: 5,
        instruction: 'Establish two wide-bore (16G/18G) IV lines and infuse cold 0.9% Normal Saline at 200–300 mL/hour to correct severe dehydration and protect renal tubules.',
        rationale: 'High fluid rates maintain renal tubular flow and prevent acute myoglobinuric tubular necrosis.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st3-c6',
        stepNumber: 6,
        instruction: 'Identify myoglobinuria from tea-colored urine, insert an indwelling urinary catheter, and order emergency stat serum Creatine Kinase (CK), electrolytes, urea, and creatinine.',
        rationale: 'Massive muscle breakdown liberates myoglobin; CK levels in NMS frequently exceed 20,000–100,000 U/L.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Ignoring tea-colored urine and failing to monitor CK and renal parameters leads directly to anuric acute tubular necrosis.',
        category: 'Assessment & Communication'
      },
      {
        id: 'st3-c7',
        stepNumber: 7,
        instruction: 'Administer specific pharmacologic antidotes: prepare IV Dantrolene (direct-acting muscle relaxant, 1–2.5 mg/kg IV) and/or Bromocriptine (dopamine agonist, 2.5–5 mg via NGT).',
        rationale: 'Dantrolene dissociates muscle excitation-contraction coupling; Bromocriptine restores central dopaminergic tone.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st3-c8',
        stepNumber: 8,
        instruction: 'Administer IV Lorazepam (1–2 mg) for agitation, skeletal muscle relaxation, and autonomic stabilization.',
        rationale: 'Benzodiazepines enhance GABAergic inhibition, decreasing autonomic hyperactivity and muscular thermogenesis.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st3-c9',
        stepNumber: 9,
        instruction: 'Continuous hemodynamic monitoring: track blood pressure fluctuations, ECG for QTc prolongation and arrhythmias, and urine output targeting > 100 mL/hr.',
        rationale: 'Autonomic storming causes labile hypertension, ventricular arrhythmias, and circulatory collapse.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      },
      {
        id: 'st3-c10',
        stepNumber: 10,
        instruction: 'Coordinate immediate transfer to Intensive Care Unit (ICU) and establish documentation of medication allergy/adverse drug reaction warning in the permanent medical record.',
        rationale: 'Patients with severe NMS require advanced mechanical ventilation and continuous hemodynamic ICU management.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      }
    ],
    mcqs: [
      {
        id: 'st3-q1',
        questionNumber: 1,
        questionText: 'Under the Hunter Serotonin Toxicity Criteria, which physical finding is the most specific and decisive diagnostic indicator of Serotonin Syndrome over NMS?',
        options: [
          { id: 'A', text: 'Lead-pipe muscular rigidity' },
          { id: 'B', text: 'Spontaneous clonus (ocular or ankle) and hyperreflexia' },
          { id: 'C', text: 'Elevated serum alkaline phosphatase' },
          { id: 'D', text: 'Persistent hypothermia below 35 °C' }
        ],
        correctAnswer: 'B',
        explanation: 'Spontaneous, inducible, or ocular clonus combined with tremor and hyperreflexia is the cardinal diagnostic hallmark of Serotonin Toxicity (Hunter Criteria). NMS is characterized by hyporeflexia and severe generalized lead-pipe rigidity.',
        learningDomain: 'Differential Diagnosis'
      },
      {
        id: 'st3-q2',
        questionNumber: 2,
        questionText: 'What is the primary pharmacological mechanism of action of Dantrolene Sodium in treating severe Neuroleptic Malignant Syndrome?',
        options: [
          { id: 'A', text: 'It stimulates postsynaptic dopamine D2 receptors in the striatum' },
          { id: 'B', text: 'It acts directly on skeletal muscle by inhibiting calcium release from the sarcoplasmic reticulum' },
          { id: 'C', text: 'It blocks 5-HT2A serotonin receptors in the gastrointestinal tract' },
          { id: 'D', text: 'It competitively inhibits acetylcholinesterase at the neuromuscular junction' }
        ],
        correctAnswer: 'B',
        explanation: 'Dantrolene acts directly on the ryanodine receptor channels of the sarcoplasmic reticulum, blocking calcium release, which halts hypermetabolic muscle contractions and reduces body temperature.',
        learningDomain: 'Clinical Pharmacology'
      },
      {
        id: 'st3-q3',
        questionNumber: 3,
        questionText: 'Which laboratory biomarker is elevated to extreme levels (frequently > 10,000–50,000 U/L) in Neuroleptic Malignant Syndrome as a direct consequence of severe rhabdomyolysis?',
        options: [
          { id: 'A', text: 'Creatine Kinase (CK / CPK)' },
          { id: 'B', text: 'Serum Amylase' },
          { id: 'C', text: 'Thyroid Stimulating Hormone (TSH)' },
          { id: 'D', text: 'Serum Ferritin' }
        ],
        correctAnswer: 'A',
        explanation: 'Intense, sustained muscular rigidity causes muscle necrosis and breakdown (rhabdomyolysis), releasing massive quantities of Creatine Kinase (CK) and myoglobin into the circulation.',
        learningDomain: 'Laboratory Diagnostics'
      },
      {
        id: 'st3-q4',
        questionNumber: 4,
        questionText: 'In a patient with suspected Serotonin Syndrome caused by polypharmacy (SSRI + MAOI / Tramadol), which specific serotonin antagonist medication is administered as an antidote?',
        options: [
          { id: 'A', text: 'Bromocriptine' },
          { id: 'B', text: 'Cyproheptadine' },
          { id: 'C', text: 'Flumazenil' },
          { id: 'D', text: 'Haloperidol' }
        ],
        correctAnswer: 'B',
        explanation: 'Cyproheptadine is a first-generation antihistamine with potent 5-HT1A and 5-HT2A serotonin receptor antagonist properties, utilized as a specific antidote in moderate-to-severe serotonin toxicity.',
        learningDomain: 'Antidote Pharmacology'
      },
      {
        id: 'st3-q5',
        questionNumber: 5,
        questionText: 'Why is aggressive IV hydration with Normal Saline critical when managing a patient with NMS and tea-colored urine?',
        options: [
          { id: 'A', text: 'To flush dopamine out of the central nervous system' },
          { id: 'B', text: 'To maintain high renal tubular flow and prevent myoglobin precipitation, tubular casts, and acute renal failure' },
          { id: 'C', text: 'To decrease intracranial pressure caused by cerebral edema' },
          { id: 'D', text: 'To dilute serum potassium and prevent hypokalemia' }
        ],
        correctAnswer: 'B',
        explanation: 'Myoglobin is filtered by the glomeruli and precipitates in acidic, concentrated renal tubules, forming toxic casts that cause acute tubular necrosis (ATN). Aggressive crystalloid hydration prevents renal failure.',
        learningDomain: 'Renal Protection'
      },
      {
        id: 'st3-q6',
        questionNumber: 6,
        questionText: 'What is the recommended dopamine agonist of choice administered enterally (via nasogastric tube) to reverse central dopamine depletion in NMS?',
        options: [
          { id: 'A', text: 'Bromocriptine' },
          { id: 'B', text: 'Metoclopramide' },
          { id: 'C', text: 'Chlorpromazine' },
          { id: 'D', text: 'Propranolol' }
        ],
        correctAnswer: 'A',
        explanation: 'Bromocriptine is a central dopamine D2 receptor agonist that overcomes neuroleptic receptor blockade in the nigrostriatal and hypothalamic pathways, reducing rigidity and fever.',
        learningDomain: 'Pharmacotherapy'
      },
      {
        id: 'st3-q7',
        questionNumber: 7,
        questionText: 'Which of the following clinical features represents autonomic nervous system instability commonly witnessed in NMS?',
        options: [
          { id: 'A', text: 'Flat, stable blood pressure and bradycardia' },
          { id: 'B', text: 'Labile blood pressure fluctuations, profuse diaphoresis, tachycardia, and cardiac arrhythmias' },
          { id: 'C', text: 'Dry mucous membranes with complete absence of sweat' },
          { id: 'D', text: 'Persistent hypoventilation without tachycardia' }
        ],
        correctAnswer: 'B',
        explanation: 'Autonomic dysregulation in NMS manifests with erratic fluctuations in blood pressure, sinus tachycardia, tachypnea, profuse diaphoresis (sweating), and cardiac dysrhythmias.',
        learningDomain: 'Pathophysiology'
      },
      {
        id: 'st3-q8',
        questionNumber: 8,
        questionText: 'How long must a psychiatric patient who has completely recovered from an episode of NMS be maintained off antipsychotic medications before carefully considering a cautious rechallenge with a different, low-potency atypical agent?',
        options: [
          { id: 'A', text: 'At least 24 to 48 hours' },
          { id: 'B', text: 'A minimum of 2 weeks (preferably 4 weeks) following complete clinical and laboratory resolution' },
          { id: 'C', text: 'Antipsychotics can never be prescribed again under any circumstances' },
          { id: 'D', text: 'Rechallenge can occur on the day body temperature normalizes' }
        ],
        correctAnswer: 'B',
        explanation: 'Re-introducing antipsychotics too early carries a high risk of NMS recurrence. Guidelines recommend waiting at least 2 weeks (and up to 4 weeks if depot neuroleptics were involved) with completely normal CK levels and vitals before titrating a novel atypical agent.',
        learningDomain: 'Clinical Rechallenge Guidelines'
      },
      {
        id: 'st3-q9',
        questionNumber: 9,
        questionText: 'What is the cardinal difference between Malignant Catatonia and Neuroleptic Malignant Syndrome regarding the timing of antipsychotic exposure?',
        options: [
          { id: 'A', text: 'Malignant catatonia occurs only in geriatric patients over 80 years' },
          { id: 'B', text: 'Malignant catatonia is preceded by classic psychiatric catatonic symptoms (waxy flexibility, posturing) and may develop in the total absence of antipsychotic exposure' },
          { id: 'C', text: 'NMS does not produce fever while malignant catatonia produces extreme fever' },
          { id: 'D', text: 'CK is always zero in malignant catatonia' }
        ],
        correctAnswer: 'B',
        explanation: 'Malignant catatonia and NMS share identical hyperthermic and rigid endpoints, but malignant catatonia is an idiopathic manifestation of severe mood or psychotic disorders and can arise without any neuroleptic exposure, responding rapidly to ECT or high-dose Lorazepam.',
        learningDomain: 'Neuropsychiatric Syndromes'
      },
      {
        id: 'st3-q10',
        questionNumber: 10,
        questionText: 'Which class of antiparkinsonian medications can paradoxically precipitate NMS when abruptly withdrawn in psychiatric or neurological patients?',
        options: [
          { id: 'A', text: 'Dopaminergic agents (such as Levodopa/Carbidopa or Amantadine)' },
          { id: 'B', text: 'SSRIs' },
          { id: 'C', text: 'Benzodiazepines' },
          { id: 'D', text: 'Beta blockers' }
        ],
        correctAnswer: 'A',
        explanation: 'Abrupt cessation of dopaminergic agonists (Levodopa, Amantadine) mimics the acute dopamine receptor blockade produced by high-potency neuroleptics, triggering acute "NMS-like" withdrawal hyperthermia and rigidity.',
        learningDomain: 'Etiology & Risk Factors'
      }
    ]
  },
  {
    id: 'station-4-ciwa-delirium-tremens',
    stationNumber: 4,
    title: 'Dual Diagnosis: Complex Substance Withdrawal & Delirium Tremens',
    subTitle: 'CIWA-Ar Protocol, High-Dose Parenteral Thiamine, Seizure Precautions & Hallucinosis',
    specialtyDomain: 'Addiction Psychiatry & Dual Diagnosis',
    clinicalScenario:
      'A 46-year-old male construction engineer with a 15-year history of heavy alcohol dependence (consuming 750 mL of dry gin daily) was admitted to the surgical ward 48 hours ago for an emergency open reduction and internal fixation (ORIF) of a compound tibia fracture. His family withheld his alcohol history from the surgical team. Six hours ago, he became acutely tremulous, agitated, and disoriented to time and place. He is currently hallucinating, clawing frantically at his bedsheets to "pull off venomous army ants crawling up my legs," and shouting in terror. His skin is soaked with perspiration, his hands exhibit gross coarse tremors, and he is unable to hold a cup of water.',
    doorBriefing:
      'Candidate Door Brief: You are the Postgraduate Mental Health Liaison Specialist called urgently to the orthopedic surgical ward. A 46-year-old post-op patient has developed acute Delirium Tremens (DTs) on Post-Op Day 2. You have 10 minutes to execute the Clinical Institute Withdrawal Assessment for Alcohol (CIWA-Ar), institute emergency seizure precautions, administer high-dose parenteral thiamine (Pabrinex) BEFORE intravenous dextrose, initiate symptom-triggered benzodiazepines, and secure patient safety. You will then have 10 minutes to complete 10 scenario-linked clinical MCQs.',
    candidateInstructions: [
      'Rapidly assess airway, breathing, circulation, and vital signs.',
      'Systematically score the 10 domains of the CIWA-Ar instrument.',
      'Enforce seizure precautions (padded bed rails, suction, oral airway on standby).',
      'Verify the non-negotiable administration of IV/IM Thiamine (Pabrinex) prior to any glucose infusion.',
      'Calculate and administer symptom-triggered Diazepam/Lorazepam according to CIWA-Ar score.',
      'Differentiate alcoholic hallucinosis from full Delirium Tremens.'
    ],
    patientProfile: {
      name: 'Babatunde Alabi',
      age: 46,
      gender: 'Male',
      setting: 'Orthopedic Post-Surgical Ward (Bed 14)',
      chiefComplaint: 'Severe tremors, tactile/visual hallucinations (insects crawling), confusion, and extreme autonomic storming.',
      historyOfPresentIllness: 'Sustained compound tibia fracture 48 hours ago in a motor vehicle accident. ORIF performed under general anesthesia. Last alcohol consumed 54 hours ago.',
      pastPsychiatricHistory: 'Three previous attempts at unassisted home detoxification resulting in alcohol withdrawal seizures.',
      medicalAndSubstanceHistory: 'Chronic alcohol dependence (25–30 units daily); early alcoholic liver cirrhosis; heavy smoker (20 cigarettes/day).',
      currentMedications: ['Cefuroxime 750 mg IV TDS', 'Tramadol 50 mg IV PRN (withheld)', 'Paracetamol 1g IV QDS'],
      allergies: ['NKDA']
    },
    entryVitals: {
      bloodPressure: '186/112 mmHg (Severe Autonomic Storm)',
      heartRate: '138 bpm (Sinus Tachycardia)',
      respiratoryRate: '26 cpm',
      temperature: '38.4 °C',
      oxygenSaturation: '96% on room air',
      painOrDistressScore: 'CIWA-Ar Score: 32/67 (Severe Withdrawal / Imminent Delirium Tremens)'
    },
    equipmentTray: [
      'Clinical Institute Withdrawal Assessment for Alcohol revised (CIWA-Ar) scoring tool',
      'Parenteral Thiamine / Vitamin B-complex (Pabrinex IV ampoules 1 & 2)',
      'Intravenous Diazepam 10mg/2mL and Lorazepam 4mg/mL ampoules',
      'Padded bed rails, suction apparatus, yankauer suction tip, and nasal cannula',
      'Blood glucose glucometer, liver function and magnesium/phosphate blood tubes'
    ],
    fatalErrorNotice:
      'CRITICAL RED FLAG / FATAL ERROR: Administering intravenous 5% Dextrose before administering high-dose parenteral Thiamine (risking acute precipitation of irreversible Wernicke-Korsakoff Encephalopathy) or managing severe withdrawal (CIWA-Ar > 25) with oral placebo/withholding benzodiazepines triggers an automatic Station Referral (Score capped at 49%).',
    checklist: [
      {
        id: 'st4-c1',
        stepNumber: 1,
        instruction: 'Assess immediate physical and surgical safety: check operative limb dressing/splint, calm the patient with orientation cues, and ensure a safe, well-lit, quiet environment.',
        rationale: 'Delirium tremens patients can dislodge surgical implants, pull out IV lines, or fall out of bed due to visual/tactile terrors.',
        points: 10,
        isCriticalFail: false,
        category: 'Preparation & Safety'
      },
      {
        id: 'st4-c2',
        stepNumber: 2,
        instruction: 'Implement comprehensive seizure precautions: pad side rails, ensure functioning wall suction, oxygen, and emergency bag-valve-mask at bedside.',
        rationale: 'Alcohol withdrawal seizures occur in up to 15-20% of severe untreated cases, often preceding or accompanying delirium tremens.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Leaving an acutely withdrawing patient without seizure precautions exposes the candidate to aspiration, head trauma, and status epilepticus.',
        category: 'Preparation & Safety'
      },
      {
        id: 'st4-c3',
        stepNumber: 3,
        instruction: 'Check capillary blood glucose stat with a glucometer to rule out profound alcoholic hypoglycemia.',
        rationale: 'Chronic alcoholics have depleted hepatic glycogen stores and impaired gluconeogenesis, causing severe neuroglycopenia.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st4-c4',
        stepNumber: 4,
        instruction: 'Administer high-dose parenteral Thiamine (Pabrinex IV 2 pairs of ampoules in 100 mL 0.9% Saline over 30 mins) strictly BEFORE any intravenous glucose infusion.',
        rationale: 'Administering glucose without thiamine consumes remaining thiamine pyrophosphate as a cofactor in carbohydrate metabolism, precipitating acute Wernicke-Korsakoff encephalopathy and death.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Infusing dextrose before parenteral thiamine causes acute, irreversible hemorrhagic necrosis of the mammillary bodies (Wernicke Encephalopathy).',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st4-c5',
        stepNumber: 5,
        instruction: 'Administer the CIWA-Ar instrument systematically across all 10 clinical domains: nausea/vomiting, tremor, paroxysmal sweats, anxiety, agitation, tactile/auditory/visual disturbances, headache, and orientation.',
        rationale: 'Validated scoring guides titration of symptom-triggered benzodiazepines and avoids under- or over-sedation.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st4-c6',
        stepNumber: 6,
        instruction: 'Calculate CIWA-Ar score (> 30 indicates severe withdrawal) and immediately administer symptom-triggered IV Diazepam (10–20 mg slow IV) or Lorazepam (2–4 mg IV if liver impairment suspected).',
        rationale: 'Benzodiazepines substitute for ethanol at GABA-A receptors, calming neuroexcitation and aborting delirium tremens.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Withholding benzodiazepines in severe delirium tremens (CIWA-Ar > 25) results in hyperpyrexia, status epilepticus, and cardiovascular collapse.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st4-c7',
        stepNumber: 7,
        instruction: 'Check and correct serum electrolytes, particularly potassium, magnesium, and phosphate.',
        rationale: 'Hypomagnesemia lowers the seizure threshold and impairs thiamine phosphorylation, perpetuating refractoriness to benzodiazepines.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st4-c8',
        stepNumber: 8,
        instruction: 'Provide re-orientation cues, reassurance, minimize sensory overload, and maintain constant nursing observation (Level 3 line-of-sight) to prevent injury.',
        rationale: 'Tactile and visual hallucinations in DTs cause catastrophic panic and unintentional self-harm.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st4-c9',
        stepNumber: 9,
        instruction: 'Repeat CIWA-Ar assessment and vital sign measurements every 15–30 minutes until clinical score drops below 10, then hourly.',
        rationale: 'Rapid reassessment prevents cumulative benzodiazepine toxicity while ensuring breakthrough withdrawal is captured immediately.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      },
      {
        id: 'st4-c10',
        stepNumber: 10,
        instruction: 'Formulate post-acute dual diagnosis management plan: plan oral thiamine maintenance, liaison psychiatry consultation, motivational interviewing, and community rehabilitation.',
        rationale: 'Detoxification without structured addiction and dual diagnosis rehabilitation leads to 90%+ rapid relapse.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      }
    ],
    mcqs: [
      {
        id: 'st4-q1',
        questionNumber: 1,
        questionText: 'What is the biochemical reason why intravenous thiamine (Vitamin B1) MUST be administered prior to any intravenous dextrose infusion in a malnourished or alcohol-dependent patient?',
        options: [
          { id: 'A', text: 'Dextrose binds directly to thiamine and neutralizes its vitamins' },
          { id: 'B', text: 'Glucose metabolism consumes thiamine pyrophosphate as a co-enzyme in pyruvate dehydrogenase, depleting marginal stores and precipitating acute Wernicke-Korsakoff syndrome' },
          { id: 'C', text: 'Thiamine prevents severe osmotic diuresis caused by dextrose' },
          { id: 'D', text: 'Dextrose causes acute cardiac arrest if not preceded by thiamine' }
        ],
        correctAnswer: 'B',
        explanation: 'Thiamine pyrophosphate is an indispensable cofactor in cerebral glucose metabolism (pyruvate decarboxylation and transketolase). Providing glucose without thiamine drives metabolic pathways that exhaust remaining thiamine, precipitating acute hemorrhagic thalamic necrosis.',
        learningDomain: 'Neurochemistry & Nutritional Neuroscience'
      },
      {
        id: 'st4-q2',
        questionNumber: 2,
        questionText: 'Which clinical triad classically characterizes acute Wernicke’s Encephalopathy?',
        options: [
          { id: 'A', text: 'Ophthalmoplegia (nystagmus/abducens palsy), ataxia, and acute confusion / global memory impairment' },
          { id: 'B', text: 'Hypertension, bradycardia, and irregular respirations (Cushing triad)' },
          { id: 'C', text: 'Lead-pipe rigidity, hyperthermia, and diaphoresis' },
          { id: 'D', text: 'Flapping tremor, jaundice, and ascites' }
        ],
        correctAnswer: 'A',
        explanation: 'Wernicke’s encephalopathy is defined by the classic triad of oculomotor abnormalities (nystagmus, 6th nerve palsy), cerebellar ataxia, and acute global encephalopathy/confusion.',
        learningDomain: 'Neuropsychiatric Syndromes'
      },
      {
        id: 'st4-q3',
        questionNumber: 3,
        questionText: 'When managing alcohol withdrawal in a patient with documented end-stage liver cirrhosis, which benzodiazepine is preferred due to its lack of active hepatic metabolites and direct glucuronidation?',
        options: [
          { id: 'A', text: 'Diazepam' },
          { id: 'B', text: 'Chlordiazepoxide' },
          { id: 'C', text: 'Lorazepam (or Oxazepam)' },
          { id: 'D', text: 'Clorazepate' }
        ],
        correctAnswer: 'C',
        explanation: 'Lorazepam and Oxazepam (the "LOT" drugs) bypass hepatic phase I CYP450 oxidation and undergo direct phase II glucuronidation, avoiding prolonged accumulation and hepatic encephalopathy in liver disease.',
        learningDomain: 'Hepatic Pharmacokinetics'
      },
      {
        id: 'st4-q4',
        questionNumber: 4,
        questionText: 'What is the defining clinical difference between Alcoholic Hallucinosis and Delirium Tremens?',
        options: [
          { id: 'A', text: 'Alcoholic hallucinosis occurs only in children' },
          { id: 'B', text: 'In alcoholic hallucinosis, sensorium is clear (intact orientation) with vivid auditory/visual hallucinations, whereas Delirium Tremens features global disorientation, clouding of consciousness, and intense autonomic instability' },
          { id: 'C', text: 'Delirium tremens never produces hallucinations' },
          { id: 'D', text: 'Alcoholic hallucinosis has a 50% mortality rate' }
        ],
        correctAnswer: 'B',
        explanation: 'Alcoholic hallucinosis presents with prominent hallucinations in a clear sensorium (patient is fully oriented to time, place, and person), whereas Delirium Tremens involves severe delirium (clouded consciousness, confusion) and profound autonomic storming.',
        learningDomain: 'Diagnostic Psychopathology'
      },
      {
        id: 'st4-q5',
        questionNumber: 5,
        questionText: 'What is the typical time window following the cessation or significant reduction of heavy alcohol intake during which Delirium Tremens most commonly emerges?',
        options: [
          { id: 'A', text: 'Within 2 to 4 hours' },
          { id: 'B', text: '48 to 96 hours post-cessation' },
          { id: 'C', text: '14 to 21 days post-cessation' },
          { id: 'D', text: 'Immediately after the first drink' }
        ],
        correctAnswer: 'B',
        explanation: 'While minor withdrawal tremors begin at 6–12 hours and seizures peak at 24–48 hours, Delirium Tremens typically manifests between 48 and 96 hours following the last alcoholic drink.',
        learningDomain: 'Withdrawal Chronobiology'
      },
      {
        id: 'st4-q6',
        questionNumber: 6,
        questionText: 'Which electrolyte abnormality is extremely prevalent in chronic alcohol dependence and directly impairs cerebral responsiveness to thiamine and benzodiazepines while lowering the seizure threshold?',
        options: [
          { id: 'A', text: 'Hypercalcemia' },
          { id: 'B', text: 'Hypomagnesemia' },
          { id: 'C', text: 'Hyperkalemia' },
          { id: 'D', text: 'Hypernatremia' }
        ],
        correctAnswer: 'B',
        explanation: 'Magnesium is a critical cofactor for thiamine pyrophosphokinase. Severe hypomagnesemia in alcoholics exacerbates neuronal excitability, causes refractory hypokalemia, and impairs response to thiamine.',
        learningDomain: 'Clinical Biochemistry'
      },
      {
        id: 'st4-q7',
        questionNumber: 7,
        questionText: 'Under the CIWA-Ar instrument, what score threshold indicates severe alcohol withdrawal requiring immediate aggressive pharmacotherapy?',
        options: [
          { id: 'A', text: 'Score < 5' },
          { id: 'B', text: 'Score between 5 and 9' },
          { id: 'C', text: 'Score of 20 or greater' },
          { id: 'D', text: 'Score of exactly 0' }
        ],
        correctAnswer: 'C',
        explanation: 'Scores < 10 reflect mild withdrawal; 10–19 indicate moderate withdrawal; scores $\ge 20$ signify severe withdrawal with imminent risk of delirium tremens, demanding aggressive intravenous/oral benzodiazepine loading.',
        learningDomain: 'Psychometric Instruments'
      },
      {
        id: 'st4-q8',
        questionNumber: 8,
        questionText: 'Why is antipsychotic monotherapy (e.g. Haloperidol alone) contraindicated as the primary treatment for alcohol withdrawal delirium?',
        options: [
          { id: 'A', text: 'Antipsychotics lower the seizure threshold and have zero protective effect against alcohol withdrawal seizures or autonomic storming' },
          { id: 'B', text: 'Antipsychotics cause rapid alcohol intoxication' },
          { id: 'C', text: 'Antipsychotics prevent thiamine absorption in the stomach' },
          { id: 'D', text: 'Antipsychotics accelerate liver cirrhosis within hours' }
        ],
        correctAnswer: 'A',
        explanation: 'Antipsychotics lower the seizure threshold and fail to treat the underlying GABA underactivity and glutamate/NMDA overactivity. Benzodiazepines are the gold-standard foundation of treatment.',
        learningDomain: 'Clinical Pharmacology'
      },
      {
        id: 'st4-q9',
        questionNumber: 9,
        questionText: 'What neurological consequence results when acute Wernicke’s Encephalopathy is misdiagnosed, untreated, or inadequately treated with low-dose oral vitamins?',
        options: [
          { id: 'A', text: 'Korsakoff’s Syndrome (severe irreversible anterograde amnesia and confabulation)' },
          { id: 'B', text: 'Multiple Sclerosis' },
          { id: 'C', text: 'Amyotrophic Lateral Sclerosis' },
          { id: 'D', text: 'Parkinson’s Disease' }
        ],
        correctAnswer: 'A',
        explanation: 'Untreated Wernicke’s encephalopathy progresses in 80%+ of survivors to Korsakoff’s amnestic syndrome, characterised by profound anterograde and retrograde amnesia and compensatory confabulation.',
        learningDomain: 'Neuropsychiatric Sequelae'
      },
      {
        id: 'st4-q10',
        questionNumber: 10,
        questionText: 'In dual diagnosis care, which FDA/NICE-approved anticraving medication acts as a mu-opioid receptor antagonist to diminish the rewarding euphoric effects of alcohol consumption?',
        options: [
          { id: 'A', text: 'Disulfiram' },
          { id: 'B', text: 'Naltrexone' },
          { id: 'C', text: 'Acamprosate' },
          { id: 'D', text: 'Methadone' }
        ],
        correctAnswer: 'B',
        explanation: 'Naltrexone blocks endogenous opioid release triggered by alcohol, blunting dopamine release in the nucleus accumbens and reducing alcohol cravings and consumption.',
        learningDomain: 'Relapse Prevention Pharmacology'
      }
    ]
  },
  {
    id: 'station-5-forensic-mental-health-act',
    stationNumber: 5,
    title: 'Forensic Psychiatric Assessment & Mental Health Legislation',
    subTitle: 'Statutory Involuntary Committal, Decision-Making Capacity, Human Rights & Seclusion Ethics',
    specialtyDomain: 'Forensic Mental Health & Jurisprudence',
    clinicalScenario:
      'A 39-year-old male former military officer with a diagnosed chronic Paranoid Schizophrenia defaulted on his depot antipsychotics 6 months ago. He was arrested by state police after brandishing a machete outside an embassy compound, declaring that foreign spies have compromised the national electrical grid and are beaming ultrasonic waves into his skull. The magistrate court has remanded him to the Maximum Security Forensic Psychiatric Hospital under statutory mental health legislation for competency assessment and clinical stabilization. Upon arrival on the forensic admission ward, the patient furiously claims illegal detention, threatens to execute nursing personnel, and demands immediate unconditional discharge.',
    doorBriefing:
      'Candidate Door Brief: You are the Senior Forensic Psychiatric Nurse. A 39-year-old remanded forensic patient with Paranoid Schizophrenia and potential violence has arrived under a statutory court order. You have 10 minutes to execute a formal admission risk assessment, evaluate mental capacity, explain legal rights under the Mental Health Act, handle hostile institutional defiance safely, and establish seclusion/containment protocols conforming to statutory human rights charters. You will then have 10 minutes to complete 10 scenario-linked clinical MCQs.',
    candidateInstructions: [
      'Verify statutory legal remand documentation (Form / Warrant / Court Remand Order).',
      'Conduct a focused assessment of decision-making capacity regarding hospitalization and treatment.',
      'Explain statutory rights under mental health legislation (tribunal appeal, legal representation, independent second opinion).',
      'Execute forensic violence risk screening (HCR-20 / DASA).',
      'Apply human rights principles (least restrictive alternative, proportionality, necessity) in containment and seclusion.',
      'Document findings in official statutory forensic mental health ledgers.'
    ],
    patientProfile: {
      name: 'Major Bello Haruna (Rtd)',
      age: 39,
      gender: 'Male',
      setting: 'Forensic Admissions & High-Security Evaluation Suite',
      chiefComplaint: 'Arrested outside embassy with machete; remanded under Mental Health Act for fitness assessment and psychiatric stabilization.',
      historyOfPresentIllness: 'Defaulted Paliperidone Palmitate depot 6 months ago. Developed intense persecutory and somatic passivity delusions. Believes embassy is coordinating micro-wave attacks on his body.',
      pastPsychiatricHistory: 'Diagnosed with Schizophrenia 10 years ago during military service; discharged medically. Two prior forensic hospitalizations for armed threats.',
      medicalAndSubstanceHistory: 'History of blast injury concussions; no active medical disease; denies current alcohol/substance use.',
      currentMedications: ['Defaulted all medications for 6 months'],
      allergies: ['NKDA']
    },
    entryVitals: {
      bloodPressure: '142/88 mmHg',
      heartRate: '98 bpm',
      respiratoryRate: '20 cpm',
      temperature: '36.9 °C',
      oxygenSaturation: '98% on ambient air',
      painOrDistressScore: 'Dynamic Appraisal of Situational Aggression (DASA Score: 5/7 - High Impending Violence)'
    },
    equipmentTray: [
      'Statutory Court Remand Order & Mental Health Act Involuntary Admission Certificate',
      'Historical Clinical Risk-20 (HCR-20) violence risk assessment protocol',
      'Dynamic Appraisal of Situational Aggression (DASA) inpatient instrument',
      'Mental Health Review Tribunal Rights Information Leaflet & Legal Aid Contact Dossier',
      'Seclusion & Mechanical Restraint Institutional Register & Continuous Observation Ledger'
    ],
    fatalErrorNotice:
      'CRITICAL RED FLAG / FATAL ERROR: Releasing a remanded forensic patient detained under a statutory court order without magistrate/senate authority, using seclusion/restraint as a punitive measure or staff convenience, or failing to inform an involuntarily detained patient of statutory rights of appeal triggers an automatic Station Referral (Score capped at 49%).',
    checklist: [
      {
        id: 'st5-c1',
        stepNumber: 1,
        instruction: 'Verify validity of statutory legal remand documents: verify magistrate court seal, patient identity, statutory section, and expiry timeline.',
        rationale: 'Involuntary detention without valid statutory legal instruments constitutes false imprisonment under constitutional law.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Detaining a citizen without verifying valid legal remand orders or releasing a court-remanded forensic patient is a gross legal and safety breach.',
        category: 'Preparation & Safety'
      },
      {
        id: 'st5-c2',
        stepNumber: 2,
        instruction: 'Conduct a thorough search for contraband and weapons adhering to forensic nursing dignity protocols with witness present.',
        rationale: 'Weapons, illicit substances, or prohibited items inside forensic psychiatric units endanger patients and clinicians.',
        points: 10,
        isCriticalFail: false,
        category: 'Preparation & Safety'
      },
      {
        id: 'st5-c3',
        stepNumber: 3,
        instruction: 'Assess decision-making capacity: evaluate ability to understand, retain, weigh treatment information, and communicate a reasoned choice.',
        rationale: 'Mental illness does not automatically equate to incapacity; capacity must be formally assessed on a decision-specific basis.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st5-c4',
        stepNumber: 4,
        instruction: 'Communicate clearly and respectfully to the patient their legal status under the Mental Health Act and provide written explanation of rights.',
        rationale: 'Statutory mental health codes mandate that detained patients be informed of their rights, including right to an independent legal advocate.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Failing to inform an involuntarily detained psychiatric patient of their statutory rights of appeal breaches national and international human rights charters.',
        category: 'Assessment & Communication'
      },
      {
        id: 'st5-c5',
        stepNumber: 5,
        instruction: 'Explain the legal avenues of appeal: Mental Health Review Tribunal, legal representation, and right to an independent second psychiatric opinion.',
        rationale: 'Due process safeguards protect against arbitrary or prolonged institutionalization.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st5-c6',
        stepNumber: 6,
        instruction: 'Administer the Dynamic Appraisal of Situational Aggression (DASA) and evaluate historical risk factors (HCR-20 framework).',
        rationale: 'Structured professional judgment (SPJ) instruments are superior to unstructured clinical intuition in predicting inpatient violence.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st5-c7',
        stepNumber: 7,
        instruction: 'Enforce the principle of the "Least Restrictive Alternative": attempt de-escalation, sensory modulation, and voluntary oral medication before seclusion.',
        rationale: 'Coercive containment measures must strictly be measures of last resort when all less restrictive options have failed.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st5-c8',
        stepNumber: 8,
        instruction: 'If seclusion is necessitated by imminent danger of catastrophic violence, ensure it is never applied as punishment, retribution, or staff convenience.',
        rationale: 'Punitive use of seclusion constitutes cruel, inhuman, and degrading treatment under international law and NMCN ethical codes.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Using seclusion, mechanical restraint, or sedation as a punitive measure or for staff disciplinary convenience is gross human rights abuse.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st5-c9',
        stepNumber: 9,
        instruction: 'Initiate continuous seclusion observation: maintain continuous visual monitoring, document vitals and mental state every 15 minutes, and provide nutrition, hydration, and toilet access.',
        rationale: 'Seclusion carries risks of self-harm, suffocation, hypothermia, and sensory deprivation trauma.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      },
      {
        id: 'st5-c10',
        stepNumber: 10,
        instruction: 'Conduct formal termination of seclusion review with consultant psychiatrist as soon as behavioral indicators demonstrate the emergency has resolved.',
        rationale: 'Seclusion must end immediately once the risk of acute physical harm subsides.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      }
    ],
    mcqs: [
      {
        id: 'st5-q1',
        questionNumber: 1,
        questionText: 'Under modern mental health legislation and human rights conventions, which four functional criteria must be evaluated to determine a patient’s legal decision-making capacity regarding medical treatment?',
        options: [
          { id: 'A', text: 'Intelligence quotient (IQ), educational attainment, fluency in English, and physical stamina' },
          { id: 'B', text: 'Ability to understand the relevant information, retain that information, weigh the information as part of decision-making, and communicate the decision' },
          { id: 'C', text: 'Presence or absence of any psychotic symptoms and family agreement' },
          { id: 'D', text: 'Willingness to comply with the senior psychiatrist’s recommendations' }
        ],
        correctAnswer: 'B',
        explanation: 'Capacity is functional and decision-specific: the patient must (1) understand relevant information, (2) retain it long enough, (3) weigh risks/benefits, and (4) communicate a clear choice.',
        learningDomain: 'Legal Capacity & Jurisprudence'
      },
      {
        id: 'st5-q2',
        questionNumber: 2,
        questionText: 'Which ethical and legal doctrine dictates that psychiatric interventions must impose the minimum necessary limitation on a patient’s liberty, autonomy, and freedom of movement?',
        options: [
          { id: 'A', text: 'The Doctrine of Parens Patriae' },
          { id: 'B', text: 'The Least Restrictive Alternative (or Least Restrictive Environment)' },
          { id: 'C', text: 'The Rule of Double Effect' },
          { id: 'D', text: 'The Therapeutic Privilege Mandate' }
        ],
        correctAnswer: 'B',
        explanation: 'The principle of the Least Restrictive Alternative mandates that clinicians choose interventions that infringe least upon the candidate’s personal autonomy and bodily freedom while achieving clinical safety.',
        learningDomain: 'Mental Health Ethics'
      },
      {
        id: 'st5-q3',
        questionNumber: 3,
        questionText: 'In forensic psychiatric risk assessment, what is the fundamental structural advantage of using Structured Professional Judgment (SPJ) tools (e.g., HCR-20, DASA) over unstructured clinical intuition?',
        options: [
          { id: 'A', text: 'SPJ tools completely eliminate the need for clinical judgment' },
          { id: 'B', text: 'SPJ integrates empirical static and dynamic risk factors, enhances predictive validity, and provides a transparent, defensible audit trail' },
          { id: 'C', text: 'SPJ tools are solely computerized and require zero patient interaction' },
          { id: 'D', text: 'SPJ tools automatically discharge low-risk patients without physician review' }
        ],
        correctAnswer: 'B',
        explanation: 'Structured Professional Judgment (SPJ) combines evidence-based static historical items with dynamic situational factors, minimizing personal clinician bias and maximizing inter-rater reliability.',
        learningDomain: 'Forensic Risk Assessment'
      },
      {
        id: 'st5-q4',
        questionNumber: 4,
        questionText: 'Under what specific circumstance does the legal exception of "Breach of Confidentiality in the Public Interest" (Tarasoff rule / statutory duty to protect) legally obligate the mental health nurse to disclose confidential patient information?',
        options: [
          { id: 'A', text: 'Whenever a patient admits to adultery during therapy' },
          { id: 'B', text: 'When a patient expresses an explicit, credible, and imminent threat to inflict severe physical harm or death upon an identifiable third party' },
          { id: 'C', text: 'Whenever an employer calls the ward asking about an employee’s mental diagnosis' },
          { id: 'D', text: 'When a patient defaults on payment of hospital admission fees' }
        ],
        correctAnswer: 'B',
        explanation: 'The common law Tarasoff doctrine and professional nursing ethics dictate that patient confidentiality ceases when there is a clear, imminent, and identifiable threat of death or serious physical harm to another person.',
        learningDomain: 'Forensic Nursing Ethics'
      },
      {
        id: 'st5-q5',
        questionNumber: 5,
        questionText: 'Which independent statutory legal body is responsible under mental health legislation for reviewing the legality of involuntary psychiatric detentions and hearing candidate appeals against hospitalization?',
        options: [
          { id: 'A', text: 'The Hospital Disciplinary Committee' },
          { id: 'B', text: 'The Mental Health Review Tribunal (or Mental Health Review Board)' },
          { id: 'C', text: 'The Medical and Dental Council Complaints Panel' },
          { id: 'D', text: 'The National Union of Nurses' }
        ],
        correctAnswer: 'B',
        explanation: 'The Mental Health Review Tribunal is an independent judicial body (typically comprising a judge/magistrate, independent psychiatrist, and lay member) statutorily authorized to review and terminate involuntary detentions.',
        learningDomain: 'Statutory Institutions'
      },
      {
        id: 'st5-q6',
        questionNumber: 6,
        questionText: 'Which of the following constitutes an absolute prohibition regarding the clinical deployment of Seclusion in mental health facilities?',
        options: [
          { id: 'A', text: 'Seclusion must not be initiated for an agitated patient with violent behavior' },
          { id: 'B', text: 'Seclusion must never be used as a punishment, disciplinary retaliation, or due to staffing shortages' },
          { id: 'C', text: 'Seclusion must never be documented in the patient chart' },
          { id: 'D', text: 'Seclusion cannot be terminated during night shift hours' }
        ],
        correctAnswer: 'B',
        explanation: 'International human rights conventions (WHO Mental Health Gap Action, UN Convention on the Rights of Persons with Disabilities) and national standards strictly ban seclusion as punishment or staff convenience.',
        learningDomain: 'Human Rights & Safety'
      },
      {
        id: 'st5-q7',
        questionNumber: 7,
        questionText: 'What is the mandatory maximum interval between documented visual checks of a patient confined in psychiatric seclusion?',
        options: [
          { id: 'A', text: 'Every 15 minutes (with continuous or direct visual observation)' },
          { id: 'B', text: 'Once every 2 hours' },
          { id: 'C', text: 'Once at the end of each nursing shift' },
          { id: 'D', text: 'Checks are unnecessary because the room is locked' }
        ],
        correctAnswer: 'A',
        explanation: 'Professional standards require continuous observation or visual checks documented at least every 15 minutes to assess airway, physical safety, hydration, and psychological distress during seclusion.',
        learningDomain: 'Inpatient Forensic Standards'
      },
      {
        id: 'st5-q8',
        questionNumber: 8,
        questionText: 'In legal jurisprudence, what is the meaning of the concept "Unfitness to Stand Trial" (or Incompetency to Stand Trial)?',
        options: [
          { id: 'A', text: 'The patient refuses to wear civilian clothing in court' },
          { id: 'B', text: 'The patient, due to a severe mental disorder, is unable to understand the nature of court proceedings, comprehend the charges, or instruct legal counsel rationally' },
          { id: 'C', text: 'The patient was psychotic at the exact moment the crime was committed 2 years ago' },
          { id: 'D', text: 'The patient has an IQ score below 90' }
        ],
        correctAnswer: 'B',
        explanation: 'Fitness to stand trial pertains to the candidate’s present mental capacity at the time of legal proceedings—specifically understanding charges, understanding the role of judge/jury, and cooperating rationally with defense counsel.',
        learningDomain: 'Forensic Competency'
      },
      {
        id: 'st5-q9',
        questionNumber: 9,
        questionText: 'How does "Unfitness to Stand Trial" differ fundamentally from the "Defense of Insanity" (e.g. M’Naghten Rules)?',
        options: [
          { id: 'A', text: 'They are identical legal concepts with different names' },
          { id: 'B', text: 'Fitness to stand trial assesses current mental state during trial, while the insanity defense assesses criminal responsibility at the precise time the offense was committed' },
          { id: 'C', text: 'Insanity defense applies only to minor traffic offenses' },
          { id: 'D', text: 'Fitness is determined by nurses, while insanity is determined by hospital porters' }
        ],
        correctAnswer: 'B',
        explanation: 'Fitness to stand trial is present-tense competency to participate in a trial. Criminal responsibility (insanity defense) is retrospective evaluation of whether a disease of the mind rendered the accused incapable of knowing the nature or wrongfulness of the act at the time of the offense.',
        learningDomain: 'Legal Distinctions'
      },
      {
        id: 'st5-q10',
        questionNumber: 10,
        questionText: 'When a court-remanded forensic patient demands to be released immediately on the grounds of constitutional freedom of movement, what is the correct legal position for the forensic nurse to articulate?',
        options: [
          { id: 'A', text: 'Open the gate and discharge the patient to avoid lawsuits' },
          { id: 'B', text: 'Calmly explain that detention is executed under a statutory court order issued by a judicial magistrate, which can only be vacated by the court or statutory review board' },
          { id: 'C', text: 'Administer an involuntary sedative injection to stop the patient from talking' },
          { id: 'D', text: 'Instruct the police to remove the patient back to prison without medical records' }
        ],
        correctAnswer: 'B',
        explanation: 'Forensic mental health remands derive from statutory judicial authority. The clinician must professionally explain the legal mandate while actively assisting the patient in accessing legal counsel and court appeal avenues.',
        learningDomain: 'Forensic Communication & Rights'
      }
    ]
  },
  {
    id: 'station-6-perinatal-geriatric-psychiatry',
    stationNumber: 6,
    title: 'Perinatal & Geriatric Neuropsychiatry: Postpartum Psychosis & Dementia',
    subTitle: 'Postpartum Psychosis with Infanticide Risk, Mother-Infant Safety, & Lewy Body Dementia Sensitivity',
    specialtyDomain: 'Specialty Populations & Neuropsychiatry',
    clinicalScenario:
      'A 29-year-old primiparous mother, 10 days post-caesarean delivery of a healthy term baby, is brought to the emergency psychiatric department by her mother and husband. The patient has had zero sleep for 5 days, exhibits pressured speech and flight of ideas, and expresses severe mood lability, fluctuating between euphoria and weeping. She holds the infant rigidly, declaring: "The archangels revealed that this child is possessed by an ancient demon and must be immersed in boiling river water at midnight to save our ancestral lineage." The infant appears dehydrated and crying incessantly.',
    doorBriefing:
      'Candidate Door Brief: You are the Postgraduate Mental Health Clinical Specialist. A 29-year-old mother Postpartum Day 10 presents with acute Postpartum Psychosis and imminent infanticide ideation. You have 10 minutes to execute immediate maternal-infant safety separation, conduct a perinatal psychiatric assessment, formulate an emergency medical and psychiatric treatment plan (admissions, lactation safety, antipsychotics, ECT evaluation), and organize supportive family interventions. You will then have 10 minutes to complete 10 scenario-linked clinical MCQs.',
    candidateInstructions: [
      'Prioritize immediate infant protection without triggering maternal panic or violent resistance.',
      'Conduct a focused assessment of postpartum psychosis versus postpartum depression and "baby blues".',
      'Assess infanticide ideation and command auditory hallucinations.',
      'Formulate an emergency psychiatric treatment plan including joint mother-baby unit (MBU) admission or supervised contact.',
      'Select lactation-compatible psychotropics and assess indications for emergency Electroconvulsive Therapy (ECT).',
      'Document immediate child protection and statutory safeguarding alerts.'
    ],
    patientProfile: {
      name: 'Amina Danjuma',
      age: 29,
      gender: 'Female',
      setting: 'Perinatal Mental Health Assessment Suite',
      chiefComplaint: 'Postpartum insomnia, religious delusions, lability, and delusional infanticide plan (immersion in boiling water).',
      historyOfPresentIllness: 'Elective Caesarean section 10 days ago. Developed progressive insomnia starting Day 3. Severe flight of ideas, hyperactivity, auditory hallucinations of archangels.',
      pastPsychiatricHistory: 'History of Bipolar I Disorder diagnosed at age 22; well maintained on Lithium pre-pregnancy, discontinued Lithium in 1st trimester against medical advice.',
      medicalAndSubstanceHistory: 'Uncomplicated pregnancy; surgical wound healing well; no substance use.',
      currentMedications: ['None currently; oral iron and calcium supplements'],
      allergies: ['NKDA']
    },
    entryVitals: {
      bloodPressure: '136/84 mmHg',
      heartRate: '108 bpm',
      respiratoryRate: '22 cpm',
      temperature: '37.3 °C',
      oxygenSaturation: '99% on ambient air',
      painOrDistressScore: 'Severe Perinatal Psychiatric Emergency (EPDS: 28/30; YMRS: 34/60; Imminent Infant Risk)'
    },
    equipmentTray: [
      'Infant safe bassinet and neonatal triage observation station',
      'Edinburgh Postnatal Depression Scale (EPDS) & Young Mania Rating Scale (YMRS)',
      'Statutory Child Protection & Safeguarding Referral Dossier',
      'Perinatal psychopharmacology lactation safety formulary (LactMed guidelines)'
    ],
    fatalErrorNotice:
      'CRITICAL RED FLAG / FATAL ERROR: Leaving the infant unsupervised with a psychotic mother expressing active infanticidal delusions, dismissing postpartum psychosis as normal "baby blues", or discharging the mother home without 24-hour continuous supervision triggers an automatic Station Referral (Score capped at 49%).',
    checklist: [
      {
        id: 'st6-c1',
        stepNumber: 1,
        instruction: 'Execute immediate, gentle physical safeguarding of the infant: gently transfer the baby to the grandmother/nurse without confrontational struggle, ensuring the baby is placed in a safe bassinet.',
        rationale: 'Infant life and safety take absolute precedence in acute postpartum psychosis with infanticidal delusions.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Leaving an infant in the physical custody of a mother with active delusions of demonic possession and boiling water immersion is fatal negligence.',
        category: 'Preparation & Safety'
      },
      {
        id: 'st6-c2',
        stepNumber: 2,
        instruction: 'Perform rapid pediatric assessment of the infant: check hydration, temperature, skin integrity, and alert pediatric team for feeding support.',
        rationale: 'Maternal psychosis frequently leads to unintentional severe neonatal dehydration, hypothermia, or unnoticed birth trauma.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st6-c3',
        stepNumber: 3,
        instruction: 'Recognize Postpartum Psychosis as a medical and psychiatric emergency distinct from self-limiting "maternity blues" or non-psychotic postpartum depression.',
        rationale: 'Postpartum psychosis has an acute onset (days 3–14 post-delivery) and carries a 5% infanticide and 5% suicide rate if untreated.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Dismissing postpartum psychosis with infanticide ideation as transient "baby blues" results in catastrophic infanticide and maternal suicide.',
        category: 'Assessment & Communication'
      },
      {
        id: 'st6-c4',
        stepNumber: 4,
        instruction: 'Conduct a focused mental state examination: evaluate mood lability, flight of ideas, cognitive delirium-like fluctuations, and command hallucinations.',
        rationale: 'Postpartum psychosis is frequently a manifestation of Bipolar I Disorder presenting with mixed affective and delirium-like cognitive features.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st6-c5',
        stepNumber: 5,
        instruction: 'Exclude medical and organic causes of postpartum delirium: order stat full blood count, CRP, renal/liver panels, thyroid function (TSH), and screen for puerperal sepsis or autoimmune encephalitis.',
        rationale: 'Puerperal sepsis, Sheehan syndrome, and anti-NMDA receptor encephalitis can mimic or precipitate acute postpartum psychosis.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st6-c6',
        stepNumber: 6,
        instruction: 'Initiate immediate emergency psychiatric admission: arrange admission to a specialized Mother and Baby Unit (MBU) or inpatient acute psychiatric unit with strict supervised infant contact.',
        rationale: 'MBUs allow ongoing mother-infant attachment and breastfeeding under 24-hour professional supervision, mitigating trauma.',
        points: 10,
        isCriticalFail: true,
        criticalFailReason: 'Discharging a mother with active postpartum psychosis home or allowing unmonitored infant contact violates clinical safety and child protection laws.',
        category: 'Intervention & Procedure'
      },
      {
        id: 'st6-c7',
        stepNumber: 7,
        instruction: 'Formulate acute pharmacotherapy: prescribe an atypical antipsychotic (Olanzapine 10–20 mg or Quetiapine) combined with a mood stabilizer and short-term benzodiazepine for sleep.',
        rationale: 'Antipsychotics rapidly control manic psychosis, while restoring restorative sleep is the single most critical biological intervention.',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st6-c8',
        stepNumber: 8,
        instruction: 'Assess lactation safety and discuss feeding plan: review antipsychotic excretion in breast milk (LactMed), discuss temporary bottle feeding, and manage breast engorgement.',
        rationale: 'Balancing psychotropic lactation compatibility with maternal sleep recovery is critical (sleep deprivation triggers psychosis relapse).',
        points: 10,
        isCriticalFail: false,
        category: 'Intervention & Procedure'
      },
      {
        id: 'st6-c9',
        stepNumber: 9,
        instruction: 'Evaluate indications for Electroconvulsive Therapy (ECT): identify ECT as the rapid, gold-standard, life-saving treatment for refractory postpartum psychosis.',
        rationale: 'Bilateral ECT produces rapid remission in postpartum psychosis, enabling rapid maternal-infant reunification.',
        points: 10,
        isCriticalFail: false,
        category: 'Assessment & Communication'
      },
      {
        id: 'st6-c10',
        stepNumber: 10,
        instruction: 'Provide structured psychoeducation to the husband and family regarding postpartum psychosis biology, relapse prevention, and submit statutory safeguarding notifications.',
        rationale: 'Family guilt and confusion are intense; clear psychoeducation ensures compliance and provides long-term protective surveillance.',
        points: 10,
        isCriticalFail: false,
        category: 'Evaluation & Documentation'
      }
    ],
    mcqs: [
      {
        id: 'st6-q1',
        questionNumber: 1,
        questionText: 'What is the estimated prevalence and typical onset timeline of Postpartum Psychosis following childbirth?',
        options: [
          { id: 'A', text: '50% of all births, starting within 2 hours of delivery' },
          { id: 'B', text: '1 to 2 per 1,000 deliveries (0.1–0.2%), typically presenting within the first 3 to 14 days postpartum' },
          { id: 'C', text: '10% of all births, presenting exclusively between 9 and 12 months' },
          { id: 'D', text: '1 per 100,000 deliveries, presenting only during labor' }
        ],
        correctAnswer: 'B',
        explanation: 'Postpartum psychosis affects approximately 1–2 per 1,000 women (0.1–0.2%) and has an acute onset usually within the first 1–2 weeks postpartum, representing an acute psychiatric emergency.',
        learningDomain: 'Perinatal Epidemiology'
      },
      {
        id: 'st6-q2',
        questionNumber: 2,
        questionText: 'Which pre-existing psychiatric diagnosis confers the single highest statistical risk (up to 25–50%) for the development of Postpartum Psychosis?',
        options: [
          { id: 'A', text: 'Generalized Anxiety Disorder' },
          { id: 'B', text: 'Bipolar I Disorder' },
          { id: 'C', text: 'Specific Phobia (dental)' },
          { id: 'D', text: 'Mild Bulimia Nervosa' }
        ],
        correctAnswer: 'B',
        explanation: 'Women with Bipolar I Disorder have up to a 50% risk of postpartum relapse/psychosis due to precipitate neuroendocrine fluctuations and severe perinatal sleep deprivation.',
        learningDomain: 'Risk Stratification'
      },
      {
        id: 'st6-q3',
        questionNumber: 3,
        questionText: 'What is the most crucial clinical distinction between Postpartum Blues ("Baby Blues") and Postpartum Psychosis?',
        options: [
          { id: 'A', text: 'Baby blues requires immediate ECT while psychosis does not' },
          { id: 'B', text: 'Baby blues is transient emotional lability peaking on Day 4–5 and resolving by Day 10–14 without psychotic delusions, whereas Postpartum Psychosis features frank delusions, hallucinations, disorganization, and high infanticide/suicide risk' },
          { id: 'C', text: 'Baby blues occurs only in fathers' },
          { id: 'D', text: 'Postpartum psychosis never features sleep disturbance' }
        ],
        correctAnswer: 'B',
        explanation: 'Baby blues affects up to 80% of mothers, peaks around day 4-5, and resolves spontaneously without affecting reality testing. Postpartum psychosis involves severe delusions, delirium-like fluctuations, and imminent risk to life.',
        learningDomain: 'Differential Diagnosis'
      },
      {
        id: 'st6-q4',
        questionNumber: 4,
        questionText: 'Why is an inpatient Mother and Baby Unit (MBU) the internationally recommended gold-standard environment for managing severe postpartum psychosis rather than a standard general psychiatric ward?',
        options: [
          { id: 'A', text: 'It allows the father to be admitted as the primary patient' },
          { id: 'B', text: 'It prevents traumatic mother-infant separation, supports emotional bonding and breastfeeding under 24/7 specialized nursing supervision, and reduces infant neglect' },
          { id: 'C', text: 'It eliminates the need for any psychotropic medications' },
          { id: 'D', text: 'It is significantly cheaper than outpatient clinics' }
        ],
        correctAnswer: 'B',
        explanation: 'Joint admission in an MBU preserves the critical early mother-infant bond, enables supervised parenting skill building, and protects infant safety without the traumatic psychological sequelae of sudden maternal separation.',
        learningDomain: 'Perinatal Healthcare Systems'
      },
      {
        id: 'st6-q5',
        questionNumber: 5,
        questionText: 'Which physical and laboratory examination is mandatory upon admission of any patient presenting with suspected postpartum psychosis to exclude organic encephalopathies?',
        options: [
          { id: 'A', text: 'Only a routine dental X-ray' },
          { id: 'B', text: 'Full blood count, inflammatory markers (CRP), renal and liver function, thyroid panel (TSH), and screening for puerperal sepsis or anti-NMDA receptor encephalitis' },
          { id: 'C', text: 'Serum amylase and lipid profile only' },
          { id: 'D', text: 'Urine pregnancy test only' }
        ],
        correctAnswer: 'B',
        explanation: 'Puerperal sepsis, cerebral venous sinus thrombosis, autoimmune (anti-NMDA receptor) encephalitis, and thyroiditis frequently present in the immediate puerperium with acute psychosis and must be ruled out.',
        learningDomain: 'Organic Differential'
      },
      {
        id: 'st6-q6',
        questionNumber: 6,
        questionText: 'When managing a geriatric psychiatric patient with Dementia with Lewy Bodies (DLB) who presents with distressing visual hallucinations, why must high-potency typical antipsychotics (e.g., Haloperidol) be strictly avoided?',
        options: [
          { id: 'A', text: 'They cause severe diarrhea' },
          { id: 'B', text: 'DLB patients have severe neuroleptic sensitivity; typical antipsychotics can precipitate catastrophic irreversible parkinsonism, acute rigidity, autonomic collapse, and death' },
          { id: 'C', text: 'They make visual hallucinations permanent' },
          { id: 'D', text: 'They induce acute hypercalcemia' }
        ],
        correctAnswer: 'B',
        explanation: 'Up to 50% of Lewy Body Dementia patients exhibit life-threatening antipsychotic sensitivity. Dopamine D2 antagonists trigger abrupt severe parkinsonism, immobility, and mortality.',
        learningDomain: 'Geriatric Neuropsychiatry'
      },
      {
        id: 'st6-q7',
        questionNumber: 7,
        questionText: 'If an atypical antipsychotic is unavoidable for distressing visual hallucinations and agitation in Lewy Body Dementia or Parkinson’s Disease Dementia, which agent is preferred due to minimal D2 blockade?',
        options: [
          { id: 'A', text: 'Haloperidol' },
          { id: 'B', text: 'Quetiapine (or Pimavanserin)' },
          { id: 'C', text: 'Fluphenazine' },
          { id: 'D', text: 'Chlorpromazine' }
        ],
        correctAnswer: 'B',
        explanation: 'Quetiapine has rapid D2 dissociation and low dopamine receptor affinity, making it least likely to worsen motor parkinsonism. Pimavanserin (a selective 5-HT2A inverse agonist with zero D2 affinity) is specifically indicated.',
        learningDomain: 'Geriatric Psychopharmacology'
      },
      {
        id: 'st6-q8',
        questionNumber: 8,
        questionText: 'What is the cornerstone biological sleep intervention in the acute management of postpartum psychosis?',
        options: [
          { id: 'A', text: 'Keeping the mother awake for 72 hours' },
          { id: 'B', text: 'Restoring uninterrupted sleep (minimum 6–8 hours) using sedation while night-time infant feeds are managed by nurses or family' },
          { id: 'C', text: 'Continuous bright light exposure throughout the night' },
          { id: 'D', text: 'High doses of caffeine throughout the evening' }
        ],
        correctAnswer: 'B',
        explanation: 'Severe sleep loss is both a primary trigger and a fuel for postpartum psychosis. Ensuring protected, uninterrupted nocturnal sleep by taking over night feeds is a primary therapeutic priority.',
        learningDomain: 'Perinatal Interventions'
      },
      {
        id: 'st6-q9',
        questionNumber: 9,
        questionText: 'What is the clinical role of Electroconvulsive Therapy (ECT) in acute postpartum psychosis?',
        options: [
          { id: 'A', text: 'It is contraindicated in all postpartum women due to pelvic floor risks' },
          { id: 'B', text: 'It is a rapid, highly effective, life-saving treatment of choice, particularly in severe catatonia, food refusal, or unremitting infanticidal/suicidal ideation' },
          { id: 'C', text: 'It is only used as a form of legal punishment' },
          { id: 'D', text: 'It requires permanently removing the infant for legal adoption' }
        ],
        correctAnswer: 'B',
        explanation: 'ECT produces rapid resolution of postpartum affective psychosis, often in 4–6 treatments, minimizing hospitalization duration and enabling safe reunification with the infant.',
        learningDomain: 'Somatic Therapies'
      },
      {
        id: 'st6-q10',
        questionNumber: 10,
        questionText: 'In planning future pregnancies for a woman with a documented history of Bipolar Disorder and previous Postpartum Psychosis, what is the mandatory perinatal psychiatric recommendation?',
        options: [
          { id: 'A', text: 'Mandatory tubal ligation' },
          { id: 'B', text: 'Pre-conception counseling, close multidisciplinary monitoring throughout pregnancy, and prophylactic mood stabilizer initiation immediately post-delivery' },
          { id: 'C', text: 'Avoiding all psychiatric appointments during pregnancy' },
          { id: 'D', text: 'Restricting the mother from holding any newborn' }
        ],
        correctAnswer: 'B',
        explanation: 'Prophylactic initiation of mood stabilizers (e.g., Lithium) immediately post-delivery, combined with pre-conception planning and sleep protection protocols, reduces postpartum psychosis recurrence from 50% to under 10%.',
        learningDomain: 'Relapse Prevention & Pre-conception Care'
      }
    ]
  }
];
