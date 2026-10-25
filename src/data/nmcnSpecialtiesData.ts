/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { NMCNSpecialty } from '../types/nmcnSpecialties';

export const NMCN_SPECIALTIES: NMCNSpecialty[] = [
  {
    id: 'spec-mentalhealth',
    code: 'NMCN-PSYCH-01',
    title: 'Mental Health & Psychiatric Nursing (Post-Basic)',
    regulatoryTitle: 'Post-Basic Psychiatric & Mental Health Nursing Licensure',
    statutoryAuthority: 'Nursing and Midwifery Council of Nigeria (NMCN) Act, Cap N143 LFN 2004',
    description:
      'Advanced psychiatric assessment, psychomotor crisis de-escalation, rapid tranquilization safety surveillance, high-lethality suicide risk mitigation, psychopharmacologic toxicity management, and statutory patient rights under Nigerian mental health law.',
    competencyDomains: [
      'Comprehensive Mental State Examination (MSE) & Psychopathology',
      'Acute Psychomotor Agitation & Non-Violent Crisis De-escalation',
      'Rapid Tranquilization Protocol, Airway Safety & EPS/NMS Surveillance',
      'High-Lethality Suicide & Self-Harm Risk Assessment (Columbia C-SSRS)',
      'Statutory Patient Rights, Confidentiality & Involuntary Admission Law'
    ],
    passMarkPercentage: 50.0,
    distinctionPercentage: 75.0,
    station: {
      id: 'nmcn-st-mentalhealth',
      title: 'Acute Psychomotor Agitation, Verbal De-escalation & Safe Rapid Tranquilization Protocol',
      subTitle: 'Non-Violent Verbal De-escalation, Physical Safety, Vital Signs & Emergency Antipsychotic Monitoring',
      clinicalScenario:
        'A 32-year-old male with known paranoid schizophrenia is brought to the acute psychiatric emergency assessment unit by family and police escorts. He has discontinued his oral medications for 3 weeks. He is pacing rapidly, shouting incoherently about government surveillance implants, brandishing a heavy wooden pen as a perceived weapon, clenching his fists, and glaring threateningly at staff. He is refusing oral medications and screaming that the hospital is trying to poison him. Triage notes mark him at high imminent violence risk.',
      doorBriefing:
        'Candidate Door Brief: You are the Senior Registered Psychiatric Nurse in charge of the Psychiatric Emergency Assessment Unit. Enter the room, ensure environmental safety and personal distance, execute structured verbal de-escalation, safely manage the object, conduct emergency assessment, coordinate safe clinical rapid tranquilization adhering to statutory council guidelines, and continuously monitor vital signs. You will then answer 10 statutory licensure MCQs.',
      candidateInstructions: [
        'Maintain personal and environmental safety: position yourself near an unblocked exit and maintain 2 arms-lengths distance.',
        'Use open, non-threatening posture and calm, non-confrontational verbal communication.',
        'Acknowledge patient distress and paranoia without validating or disputing delusional content.',
        'Verbally negotiate the safe surrender/placement of the hand-held pen without physical wrestling.',
        'Offer oral calming medication in a respectful, transparent manner before initiating parenteral routes.',
        'Prepare and coordinate rapid tranquilization with team support, ensuring pre- and post-administration vital signs and airway patency monitoring.',
        'Document the incident objectively according to statutory NMCN mental health documentation standards.'
      ],
      patientProfile: {
        name: 'Emeka Okafor',
        age: 32,
        gender: 'Male',
        setting: 'Psychiatric Emergency Assessment Unit (Room 2)',
        chiefComplaint: 'Acute psychomotor agitation, paranoia, sleep deprivation for 4 days, and threats of violence.',
        historyOfPresentIllness: 'Diagnosed with paranoid schizophrenia 6 years ago. Defaulted on maintenance depot fluphenazine 3 weeks ago. Relapsed with command auditory hallucinations and persecutory delusions.',
        currentMedications: ['Prescribed Depot Fluphenazine Decanoate 25mg IM monthly (defaulted)', 'Oral Haloperidol 5mg BD (defaulted)'],
        allergies: ['No known drug allergies (NKDA)']
      },
      entryVitals: {
        bloodPressure: '146/92 mmHg (Hypertensive response to acute agitation)',
        heartRate: '112 bpm (Sinus Tachycardia)',
        respiratoryRate: '24 cpm',
        temperature: '37.1 °C',
        oxygenSaturation: '98% on room air',
        painOrDistressScore: 'Agitation/Distress: 9/10 (High Imminent Risk)'
      },
      equipmentTray: [
        'Personal Duress Alarm / Call Bell',
        'Automated Blood Pressure Monitor & Pulse Oximeter',
        'Prescription Chart with Rapid Tranquilization Protocol (Haloperidol / Olanzapine / Lorazepam)',
        'Oral Medication Cups with Clean Water',
        'IM Injection Tray: Sterile 21G/23G Needles, 3mL Syringes, Alcohol Swabs, Sharps Bin',
        'IM Procyclidine / Benztropine (available on standby for acute dystonic reactions)',
        'Full Resuscitation Kit: Bag-Valve-Mask (Ambu Bag), Suction, Oxygen Mask, and IV Flumazenil (standby for benzodiazepine-induced respiratory depression)',
        'Structured Physical Health & MSE Monitoring Chart'
      ],
      checklist: [
        {
          id: 'mh-c1',
          stepNumber: 1,
          instruction: 'Environmental Safety & Staff Positioning: Check room for potential weapons/hazards, position self between patient and unblocked exit, and maintain safe physical distance (minimum 2 arms lengths).',
          category: 'Preparation & Safety',
          isCriticalFail: false,
          points: 10,
          rationale: 'Psychiatric emergency safety begins with environmental risk reduction and preserving uninhibited egress for both candidate and patient.'
        },
        {
          id: 'mh-c2',
          stepNumber: 2,
          instruction: 'Establish Calm, Empathetic Verbal Rapport: Introduce self clearly, use low-pitched, calm voice, speak in short concrete sentences, and display open non-verbal posture without crossed arms.',
          category: 'Assessment & Communication',
          isCriticalFail: false,
          points: 10,
          rationale: 'Agitated and paranoid individuals misinterpret complex instructions and defensive non-verbals as hostility.'
        },
        {
          id: 'mh-c3',
          stepNumber: 3,
          instruction: 'De-escalate Paranoia Without Collusion or Confrontation: Validate the emotional experience of fear and anxiety while avoiding arguing against or validating the persecutory delusions.',
          category: 'Assessment & Communication',
          isCriticalFail: false,
          points: 10,
          rationale: 'Directly disputing delusions increases hostility, while agreeing with them reinforces delusional beliefs. Validating the emotional state de-escalates affective tension.'
        },
        {
          id: 'mh-c4',
          stepNumber: 4,
          instruction: 'Negotiate Weapon/Object Surrender: Calmly request the patient to place the pen on the table; acknowledge concern for safety without lunging or physically snatching the object.',
          category: 'Intervention & Procedure',
          isCriticalFail: false,
          points: 10,
          rationale: 'Physical snatching triggers immediate fight-or-flight aggression. Voluntary placement de-escalates confrontation.'
        },
        {
          id: 'mh-c5',
          stepNumber: 5,
          instruction: 'Offer Oral Calming Medication First (Least Restrictive Principle): Explain purpose of medication transparently (to help sleep and reduce severe distress) and offer oral liquid or tablet before considering parenteral injections.',
          category: 'Intervention & Procedure',
          isCriticalFail: false,
          points: 10,
          rationale: 'NMCN and international psychiatric nursing guidelines mandate using the least restrictive intervention before coercive parenteral medication.'
        },
        {
          id: 'mh-c6',
          stepNumber: 6,
          instruction: 'Safe Execution of Rapid Tranquilization with Sufficient Trained Team: When oral medication is refused and violence is imminent, mobilize at least 5 trained staff members with designated roles, explain procedure calmly, and administer prescribed IM medication safely into upper outer quadrant of gluteal or anterolateral thigh.',
          category: 'Intervention & Procedure',
          isCriticalFail: false,
          points: 10,
          rationale: 'Team coordination prevents injury to patient and staff; proper anatomical site avoids sciatic nerve damage and ensures rapid absorption.'
        },
        {
          id: 'mh-c7',
          stepNumber: 7,
          instruction: 'CRITICAL SAFETY: Post-Tranquilization Airway & Vital Signs Monitoring: Immediately verify patent airway, place patient in safe recovery/semi-recumbent position (NEVER prone), and initiate vital signs monitoring every 15 minutes (BP, HR, RR, SpO2, sedation level).',
          category: 'Evaluation & Documentation',
          isCriticalFail: true,
          criticalFailReason: 'Prone positioning or failure to monitor vitals during rapid tranquilization risks positional asphyxia, severe respiratory depression, and sudden cardiovascular collapse.',
          points: 10,
          rationale: 'Prone positioning or failure to monitor vitals during rapid tranquilization risks positional asphyxia, severe respiratory depression, and sudden cardiovascular collapse.'
        },
        {
          id: 'mh-c8',
          stepNumber: 8,
          instruction: 'CRITICAL SAFETY: Antipsychotic Toxicity & Adverse Effect Surveillance: Inspect for acute extrapyramidal symptoms (acute dystonia, laryngeal spasm, oculogyric crisis) and Neuroleptic Malignant Syndrome (severe muscle rigidity, hyperpyrexia, autonomic instability), having anticholinergic reversal (IM Procyclidine/Benztropine) immediately accessible.',
          category: 'Evaluation & Documentation',
          isCriticalFail: true,
          criticalFailReason: 'Acute laryngeal dystonia can rapidly cause fatal upper airway obstruction, while unrecognized NMS has up to 10-20% mortality.',
          points: 10,
          rationale: 'Acute laryngeal dystonia can rapidly cause fatal upper airway obstruction, while unrecognized NMS has up to 10-20% mortality.'
        },
        {
          id: 'mh-c9',
          stepNumber: 9,
          instruction: 'Post-Crisis Debriefing & Re-establishing Therapeutic Alliance: When the patient regains composure, offer reassurance, debrief the experience, explain reasons for interventions, and provide fluids and nourishment.',
          category: 'Assessment & Communication',
          isCriticalFail: false,
          points: 10,
          rationale: 'Post-incident debriefing reduces psychological trauma, clarifies misconceptions, and restores the therapeutic nurse-patient relationship.'
        },
        {
          id: 'mh-c10',
          stepNumber: 10,
          instruction: 'Statutory Documentation & Incident Notification: Document chronological sequence, exact triggers, de-escalation attempts, specific medications administered with batch numbers/sites, post-tranquilization vitals, and statutory involuntary assessment forms under NMCN standards.',
          category: 'Evaluation & Documentation',
          isCriticalFail: false,
          points: 10,
          rationale: 'Comprehensive, objective legal documentation protects patient statutory human rights and provides an uncompromised audit trail.'
        }
      ],
      fatalErrorNotice:
        'RED FLAG VIOLATIONS (AUTOMATIC CRITICAL FAILURE): Leaving an agitated, actively hallucinating patient unmonitored; positioning the patient prone during or following restraint (severe risk of positional asphyxia); administering parenteral rapid tranquilization without vital sign monitoring and resuscitation equipment on standby; or failing to recognize and treat acute laryngeal dystonia.',
      mcqs: [
        {
          id: 'mh-q1',
          questionNumber: 1,
          questionText: 'During the Mental State Examination (MSE) of an agitated psychiatric patient, the nurse notes that the patient continuously jumps from one idea to another rapidly, connected only by superficial associations and rhyming puns. What psychopathological phenomenon is this?',
          options: [
            { id: 'A', text: 'Perseveration' },
            { id: 'B', text: 'Flight of Ideas' },
            { id: 'C', text: 'Thought Insertion' },
            { id: 'D', text: 'Thought Blocking' }
          ],
          correctAnswer: 'B',
          explanation: 'Flight of ideas is characterized by continuous, rapid speech with abrupt changes from one topic to another, often based on understandable associations, distractions, or play on words (clang associations), classic in acute mania and severe agitation.',
          learningDomain: 'MSE & Psychopathology'
        },
        {
          id: 'mh-q2',
          questionNumber: 2,
          questionText: 'Under the Nursing and Midwifery Council of Nigeria (NMCN) and international psychiatric guidelines, what is the FIRST-LINE clinical strategy when managing an escalating, agitated psychiatric patient?',
          options: [
            { id: 'A', text: 'Immediate four-point mechanical restraint' },
            { id: 'B', text: 'Verbal de-escalation and environmental adaptation in the least restrictive setting' },
            { id: 'C', text: 'Immediate involuntary intramuscular rapid tranquilization' },
            { id: 'D', text: 'Isolation in an unlit seclusion room without communication' }
          ],
          correctAnswer: 'B',
          explanation: 'NMCN professional standards mandate the least restrictive principle: verbal de-escalation, establishing calm communication, reducing sensory stimulation, and offering choices must always precede restrictive physical or parenteral interventions.',
          learningDomain: 'Crisis De-escalation & Legal Principles'
        },
        {
          id: 'mh-q3',
          questionNumber: 3,
          questionText: 'Thirty minutes after receiving IM Haloperidol 5mg for acute agitation, a patient suddenly develops involuntary upward deviation of the eyes (oculogyric crisis), neck torsion (torticollis), and difficulty speaking. What is the emergency nursing diagnosis and immediate treatment?',
          options: [
            { id: 'A', text: 'Tardive dyskinesia; increase the haloperidol dose' },
            { id: 'B', text: 'Acute dystonic reaction; administer IM/IV Procyclidine (or Benztropine) 5-10mg immediately' },
            { id: 'C', text: 'Conversion disorder; isolate the patient and observe' },
            { id: 'D', text: 'Malingering; provide reassurance and oral fluids' }
          ],
          correctAnswer: 'B',
          explanation: 'Acute dystonia occurs within hours of first-generation antipsychotic administration due to acute D2 receptor blockade causing striatal cholinergic excess. It is an emergency (risk of laryngeal dystonia) treated with immediate anticholinergic agents like IM Procyclidine 5-10mg or Diphenhydramine.',
          learningDomain: 'Psychopharmacology & Adverse Effects'
        },
        {
          id: 'mh-q4',
          questionNumber: 4,
          questionText: 'Which clinical tetrad is pathognomonic for Neuroleptic Malignant Syndrome (NMS), a life-threatening idiosyncratic reaction to dopamine receptor antagonists?',
          options: [
            { id: 'A', text: 'Hypothermia, flaccid paralysis, diarrhea, and miosis' },
            { id: 'B', text: 'Hyperthermia (often >38.5°C), severe "lead-pipe" muscle rigidity, autonomic instability, and altered mental status' },
            { id: 'C', text: 'Hypertension, polyuria, polydipsia, and hyporeflexia' },
            { id: 'D', text: 'Maculopapular rash, wheezing, angioedema, and bradycardia' }
          ],
          correctAnswer: 'B',
          explanation: 'NMS is characterized by severe hyperthermia, generalized muscular rigidity (lead-pipe), altered sensorium, autonomic dysregulation (tachycardia, labile BP, diaphoresis), and markedly elevated serum creatine kinase (CK). Immediate cessation of antipsychotics and intensive supportive care (Dantrolene/Bromocriptine) are required.',
          learningDomain: 'Psychiatric Emergencies (NMS)'
        },
        {
          id: 'mh-q5',
          questionNumber: 5,
          questionText: 'When assessing a patient with high-lethality suicidal ideation, which question is most critical for establishing immediate imminent risk?',
          options: [
            { id: 'A', text: '"Have you ever thought about how your family would react to your funeral?"' },
            { id: 'B', text: '"Do you have a specific plan, access to the intended means (e.g., firearms, pills), and an intent to carry it out today?"' },
            { id: 'C', text: '"Why do you think life is not worth living when others have it worse?"' },
            { id: 'D', text: '"Will you promise me in writing that you will never feel sad again?"' }
          ],
          correctAnswer: 'B',
          explanation: 'Assessment of imminent lethality requires evaluating three specific components: explicit plan, available lethal means, and immediate intent. Asking directly does NOT plant ideas in the patient’s mind but is life-saving.',
          learningDomain: 'Suicide Risk Assessment (C-SSRS)'
        },
        {
          id: 'mh-q6',
          questionNumber: 6,
          questionText: 'A patient receiving maintenance Lithium carbonate for bipolar disorder presents with coarse hand tremors, ataxia, slurred speech, persistent nausea/vomiting, and confusion. What is the priority nursing intervention?',
          options: [
            { id: 'A', text: 'Administer the next scheduled lithium dose with milk' },
            { id: 'B', text: 'Withhold lithium immediately, notify the psychiatrist, and order urgent serum lithium and renal/electrolyte panels' },
            { id: 'C', text: 'Encourage strenuous aerobic exercise to sweat out the excess drug' },
            { id: 'D', text: 'Administer oral potassium supplements and discharge home' }
          ],
          correctAnswer: 'B',
          explanation: 'Coarse tremors, ataxia, slurred speech, gastrointestinal distress, and confusion indicate moderate-to-severe lithium toxicity (levels typically >1.5-2.0 mmol/L). The nurse must immediately withhold lithium, check serum level, and initiate intravenous fluid hydration.',
          learningDomain: 'Mood Stabilizers & Toxicities'
        },
        {
          id: 'mh-q7',
          questionNumber: 7,
          questionText: 'Under the Nigerian Mental Health Act 2021 and NMCN ethical standards, what fundamental right is legally guaranteed to voluntary mental health inpatients regarding their care?',
          options: [
            { id: 'A', text: 'Their property is automatically transferred to hospital management upon admission' },
            { id: 'B', text: 'The right to confidentiality, informed consent to treatments (unless legally certified emergency), and dignity free from cruel, inhuman, or degrading punishment' },
            { id: 'C', text: 'They lose the right to vote or communicate with legal representation permanently' },
            { id: 'D', text: 'Hospital staff may utilize indefinite physical seclusion as a disciplinary measure' }
          ],
          correctAnswer: 'B',
          explanation: 'The Mental Health Act 2021 guarantees the rights of persons with mental health conditions, protecting dignity, right to confidentiality, informed consent, legal representation, and strictly prohibiting punitive or degrading treatments.',
          learningDomain: 'Mental Health Legislation & Rights'
        },
        {
          id: 'mh-q8',
          questionNumber: 8,
          questionText: 'A psychiatric nurse is caring for a patient experiencing frightening visual and command auditory hallucinations telling him to harm himself. What is the most therapeutic communication response?',
          options: [
            { id: 'A', text: '"You know there is nobody in the corner; you are just imagining things."' },
            { id: 'B', text: '"I do not hear the voices, but I understand that they are very scary for you. You are in a safe place, and I am here with you."' },
            { id: 'C', text: '"Tell the voices that they have no right to speak to you and yell back at them."' },
            { id: 'D', text: '"I can see the figures too; let us both hide under the bed together."' }
          ],
          correctAnswer: 'B',
          explanation: 'The nurse should validate reality ("I do not hear the voices"), acknowledge the patient’s affective distress ("I understand they are very scary for you"), and provide reassurance of safety without reinforcing the hallucination or belittling the patient.',
          learningDomain: 'Therapeutic Communication'
        },
        {
          id: 'mh-q9',
          questionNumber: 9,
          questionText: 'In a patient receiving Clozapine for treatment-resistant schizophrenia, what mandatory laboratory parameter must the psychiatric nurse monitor continuously to detect fatal Agranulocytosis?',
          options: [
            { id: 'A', text: 'Serum amylase and lipase' },
            { id: 'B', text: 'Absolute Neutrophil Count (ANC) / Full Blood Count' },
            { id: 'C', text: 'Serum prostate-specific antigen (PSA)' },
            { id: 'D', text: 'Urinary protein and microalbumin' }
          ],
          correctAnswer: 'B',
          explanation: 'Clozapine carries a black-box warning for severe neutropenia/agranulocytosis (ANC < 500/μL). Mandatory national protocols require regular ANC monitoring (weekly for the first 18 weeks, then bi-weekly, then monthly) to prevent lethal opportunistic sepsis.',
          learningDomain: 'Specialized Psychopharmacology'
        },
        {
          id: 'mh-q10',
          questionNumber: 10,
          questionText: 'Why is the "prone" (face-down) position strictly contraindicated during physical restraint of an agitated psychiatric patient under NMCN patient safety directives?',
          options: [
            { id: 'A', text: 'It damages the patient’s clothing' },
            { id: 'B', text: 'It creates a severe risk of positional asphyxia and sudden cardiac arrest due to restricted thoracic wall excursion' },
            { id: 'C', text: 'It makes it too easy for the patient to escape' },
            { id: 'D', text: 'It prevents the patient from taking oral fluids' }
          ],
          correctAnswer: 'B',
          explanation: 'Prone restraint compresses the chest wall and diaphragm, severely inhibiting respiratory excursion and venous return. This is the primary mechanism of restraint-related sudden deaths in psychiatric settings (positional asphyxia). Restraint must always maintain open airway and supine/lateral positioning.',
          learningDomain: 'Patient Safety & Restraint Directives'
        }
      ]
    }
  },
  {
    id: 'spec-med-surg',
    code: 'NMCN-MEDSURG-01',
    title: 'Medical-Surgical Nursing (Adult Health)',
    regulatoryTitle: 'Post-Basic Medical-Surgical Nursing Licensure',
    statutoryAuthority: 'Nursing and Midwifery Council of Nigeria (NMCN) Act, Cap N143 LFN 2004',
    description:
      'Advanced clinical management of acute and chronic adult medical-surgical conditions, aseptic procedural technique, central line maintenance, fluid/electrolyte resuscitation, and surgical wound infection surveillance.',
    competencyDomains: [
      'Surgical Asepsis & Wound Microbiology',
      'Central Venous Access Device (CVAD) Management',
      'Infection Control & Biohazard Segregation',
      'Systemic Sepsis Screening (qSOFA / SIRS)',
      'Pharmacokinetics & Antimicrobial Stewardship'
    ],
    passMarkPercentage: 50.0,
    distinctionPercentage: 75.0,
    station: {
      id: 'nmcn-st-medsurg',
      title: 'Aseptic Surgical Wound Care, Debridement & Central Venous Line Site Management',
      subTitle: 'Sterile Field Maintenance, Levine Swab Technique & Antiseptic Air-Drying Protocol',
      clinicalScenario:
        'A 48-year-old male on Post-Operative Day 4 following an emergency exploratory laparotomy for perforated appendicitis with peritonitis. The surgical abdominal dressing is heavily saturated with foul-smelling purulent exudate. He has a triple-lumen subclavian central venous catheter in situ with an unocclusive dressing. The patient is febrile, tachycardic, and reports localized abdominal incision pain (7/10).',
      doorBriefing:
        'Candidate Door Brief: You are the Senior Medical-Surgical Nurse on the acute post-operative surgical ward. Enter the bedside room, perform an aseptic wound debridement and redressing, collect a microbiologically viable wound swab using the Levine technique, and perform antiseptic site care on the subclavian central line adhering strictly to surgical asepsis. You will then answer 10 statutory licensure MCQs.',
      candidateInstructions: [
        'Verify patient identity, confirm allergy history, and explain the procedure.',
        'Establish a sterile field maintaining strict aseptic non-touch technique (ANTT).',
        'Inspect exudate and remove soiled dressing safely into yellow biohazard waste.',
        'Cleanse surgical wound top-to-bottom without cross-contaminating clean tissue.',
        'Collect a wound specimen using the Levine technique over viable granulation tissue.',
        'Apply 2% Chlorhexidine in 70% alcohol to the central line site and allow full 30-120s air-drying.'
      ],
      patientProfile: {
        name: 'Musa Abdullahi',
        age: 48,
        gender: 'Male',
        setting: 'Post-Surgical Inpatient Ward (Bed 6)',
        chiefComplaint: 'Fever, saturated purulent abdominal dressing, and pain around surgical incision.',
        historyOfPresentIllness: 'Underwent emergency laparotomy 4 days ago for perforated appendix. Dressing saturated over the past 6 hours.',
        currentMedications: ['IV Ceftriaxone 1g daily', 'IV Metronidazole 500mg TDS', 'IV Tramadol 50mg PRN'],
        allergies: ['Penicillin (develops urticaria)']
      },
      entryVitals: {
        bloodPressure: '138/86 mmHg',
        heartRate: '104 bpm (Tachycardia)',
        respiratoryRate: '22 cpm',
        temperature: '38.6 °C (Pyrexia)',
        oxygenSaturation: '97% on room air',
        painOrDistressScore: 'Pain: 7/10 (Incisional)'
      },
      equipmentTray: [
        'Sterile dressing pack (forceps, gallipot, cotton balls, gauze swabs)',
        'Sterile surgical gloves (Size 7.5) and clean non-sterile examination gloves',
        'Sterile Normal Saline 0.9% irrigation solution',
        'Amies transport culture swab with charcoal',
        '2% Chlorhexidine gluconate in 70% isopropyl alcohol applicator',
        'Tegaderm transparent semi-permeable adhesive dressing',
        'Yellow clinical biohazard waste bag and sharps disposal container'
      ],
      fatalErrorNotice:
        'CRITICAL RED FLAG / FATAL ERROR: Breaching surgical asepsis (touching outer non-sterile surfaces with sterile gloves) or swabbing necrotic pus instead of viable granulation tissue without wound cleansing triggers an automatic Station Referral (Score capped at 49%).',
      checklist: [
        {
          id: 'ms-c1',
          stepNumber: 1,
          instruction: 'Verify candidate/patient identification using 2 identifiers, confirm penicillin allergy, explain procedure, and secure informed verbal consent.',
          rationale: 'Patient identification and allergy verification are fundamental statutory safety standards (NMCN).',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Performing invasive wound dressing on unverified patient or ignoring documented drug allergies violates statutory patient safety.',
          category: 'Preparation & Safety'
        },
        {
          id: 'ms-c2',
          stepNumber: 2,
          instruction: 'Perform hand hygiene (WHO 5 Moments, minimum 20s rub) and don clean non-sterile gloves and waterproof plastic apron.',
          rationale: 'Infection prevention begins with compliant hand hygiene before touching clinical surfaces.',
          points: 10,
          isCriticalFail: false,
          category: 'Preparation & Safety'
        },
        {
          id: 'ms-c3',
          stepNumber: 3,
          instruction: 'Gently remove the soiled dressing parallel to skin, inspect color, odor, and consistency of exudate, and discard in yellow biohazard bag.',
          rationale: 'Removing tape parallel to skin prevents epidermal stripping; visual inspection provides wound staging data.',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'ms-c4',
          stepNumber: 4,
          instruction: 'Doff soiled gloves, perform alcohol hand rub, and open sterile dressing pack maintaining a sterile 1-inch outer border.',
          rationale: 'Prevents transfer of purulent pathogens from soiled gloves to the sterile tray.',
          points: 10,
          isCriticalFail: false,
          category: 'Preparation & Safety'
        },
        {
          id: 'ms-c5',
          stepNumber: 5,
          instruction: 'Don sterile surgical gloves using strict closed or open aseptic glove technique without touching the external sterile glove surface.',
          rationale: 'Direct hand contact with outer sterile glove surfaces contaminates the field with skin flora (Staph epidermidis).',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Contaminating sterile gloves before touching an open laparotomy wound or central line introduces hospital-acquired pathogens.',
          category: 'Intervention & Procedure'
        },
        {
          id: 'ms-c6',
          stepNumber: 6,
          instruction: 'Cleanse the surgical incision top-to-bottom (least to most contaminated) using sterile 0.9% Normal Saline with a single stroke per swab.',
          rationale: 'Single-direction strokes prevent dragging exudate back across newly cleansed surgical tissue.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ms-c7',
          stepNumber: 7,
          instruction: 'Collect wound culture swab using the Levine Technique: rotate swab over 1 cm² of viable granulation tissue with sufficient pressure to express tissue fluid.',
          rationale: 'Levine technique captures true quantitative pathogens rather than colonizing superficial surface contaminants.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Swabbing uncleaned pooled pus or slough instead of viable granulation tissue yields inaccurate microbiologic cultures.',
          category: 'Intervention & Procedure'
        },
        {
          id: 'ms-c8',
          stepNumber: 8,
          instruction: 'Apply sterile non-adherent primary dressing and secure with hypoallergenic fixation tape.',
          rationale: 'Non-adherent dressing protects epithelial buds from trauma during future dressing changes.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ms-c9',
          stepNumber: 9,
          instruction: 'Disinfect subclavian central line exit site using 2% Chlorhexidine in 70% alcohol for 30s in a back-and-forth friction scrub, and allow full air-drying (minimum 30–60s) before applying Tegaderm.',
          rationale: 'Chlorhexidine requires complete evaporation to exert its sustained bactericidal action and avoid chemical burns under occlusive dressing.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ms-c10',
          stepNumber: 10,
          instruction: 'Dispose of sharps in yellow rigid bin, discard clinical waste in biohazard bag, perform terminal hand hygiene, document findings, and reassure patient.',
          rationale: 'Safe waste segregation complies with national healthcare waste management guidelines.',
          points: 10,
          isCriticalFail: false,
          category: 'Evaluation & Documentation'
        }
      ],
      mcqs: [
        {
          id: 'ms-q1',
          questionNumber: 1,
          questionText: 'Why is the Levine technique recognized internationally as the gold-standard method for wound swab collection over the Z-stroke technique?',
          options: [
            { id: 'A', text: 'It collects surface bacteria without causing patient discomfort' },
            { id: 'B', text: 'It recovers true pathogenic organisms from viable deep wound tissue fluid rather than superficial colonizers' },
            { id: 'C', text: 'It does not require any prior wound cleansing' },
            { id: 'D', text: 'It can be performed using non-sterile examination gloves' }
          ],
          correctAnswer: 'B',
          explanation: 'The Levine technique expresses wound tissue fluid from viable granulation tissue, yielding microbial counts that correlate significantly with true histological wound infection and quantitative biopsy.',
          learningDomain: 'Wound Microbiology'
        },
        {
          id: 'ms-q2',
          questionNumber: 2,
          questionText: 'When applying 2% Chlorhexidine gluconate in 70% isopropyl alcohol to a central venous catheter insertion site, why is allowing complete air-drying mandatory before applying an occlusive dressing?',
          options: [
            { id: 'A', text: 'To cool the skin and relieve insertion discomfort' },
            { id: 'B', text: 'Because its bactericidal antimicrobial mechanism occurs primarily during solvent evaporation, and trapping wet alcohol causes severe chemical dermatitis' },
            { id: 'C', text: 'To allow the catheter to bond permanently to the dermis' },
            { id: 'D', text: 'To dissolve any fibrin sheaths inside the subclavian vein' }
          ],
          correctAnswer: 'B',
          explanation: 'Chlorhexidine in alcohol destroys microbial cell membranes during contact and evaporation. Trapping wet disinfectant beneath an occlusive film causes chemical skin breakdown and diminishes antimicrobial efficacy.',
          learningDomain: 'Infection Control'
        },
        {
          id: 'ms-q3',
          questionNumber: 3,
          questionText: 'Under the quick Sepsis-related Organ Failure Assessment (qSOFA) criteria, which three bedside clinical parameters screen for high mortality risk in adult surgical patients?',
          options: [
            { id: 'A', text: 'Fever > 38.5°C, leukocytosis > 15,000, and nausea' },
            { id: 'B', text: 'Respiratory rate ≥ 22 cpm, altered mental status (GCS < 15), and systolic blood pressure ≤ 100 mmHg' },
            { id: 'C', text: 'Heart rate > 100 bpm, hyperglycemia, and localized wound erythema' },
            { id: 'D', text: 'Platelet count < 100,000, serum bilirubin > 2 mg/dL, and oliguria' }
          ],
          correctAnswer: 'B',
          explanation: 'qSOFA evaluates three bedside variables: altered mentation, tachypnea (RR ≥ 22), and hypotension (systolic BP ≤ 100). A score of 2 or more indicates high risk of sepsis and in-hospital mortality.',
          learningDomain: 'Surgical Sepsis Surveillance'
        },
        {
          id: 'ms-q4',
          questionNumber: 4,
          questionText: 'What is the mandatory clinical action if a surgical wound displays complete dehiscence with evisceration (protrusion of bowel loops through incision)?',
          options: [
            { id: 'A', text: 'Manually push the bowel loops back into the abdominal cavity using clean gloves' },
            { id: 'B', text: 'Cover protruding viscera immediately with sterile saline-soaked gauze, place patient in low Fowler position with knees flexed, and call the surgical team stat' },
            { id: 'C', text: 'Apply dry sterile compression bandage tightly over the wound' },
            { id: 'D', text: 'Instruct the patient to ambulate to the surgical theater immediately' }
          ],
          correctAnswer: 'B',
          explanation: 'Eviscerated viscera must remain moist to prevent tissue desiccation and necrosis. Low Fowler’s with knees bent relieves tension on the abdominal wall while emergency theater transfer is arranged.',
          learningDomain: 'Surgical Emergencies'
        },
        {
          id: 'ms-q5',
          questionNumber: 5,
          questionText: 'Which phase of surgical wound healing is characterized by capillary angiogenesis, fibroblast proliferation, and pink, friable granulation tissue formation?',
          options: [
            { id: 'A', text: 'Hemostasis phase' },
            { id: 'B', text: 'Proliferative phase' },
            { id: 'C', text: 'Maturation / Remodeling phase' },
            { id: 'D', text: 'Inflammatory phase' }
          ],
          correctAnswer: 'B',
          explanation: 'The proliferative phase (typically Day 4 to 21) is dominated by fibroblast activity, collagen deposition, neo-vascularization (angiogenesis), and granulation tissue formation.',
          learningDomain: 'Wound Physiology'
        },
        {
          id: 'ms-q6',
          questionNumber: 6,
          questionText: 'Why is therapeutic drug monitoring (peak and trough serum concentrations) mandatory during parenteral Aminoglycoside therapy (e.g. Gentamicin) in surgical patients?',
          options: [
            { id: 'A', text: 'To prevent severe nephrotoxicity (acute tubular necrosis) and permanent ototoxicity' },
            { id: 'B', text: 'To ensure the drug reaches effective concentrations in the cerebrospinal fluid' },
            { id: 'C', text: 'To prevent acute liver failure' },
            { id: 'D', text: 'To monitor for malignant hyperthermia' }
          ],
          correctAnswer: 'A',
          explanation: 'Aminoglycosides have a narrow therapeutic index. Elevated trough levels correlate directly with progressive renal tubular accumulation (nephrotoxicity) and vestibular/cochlear hair cell damage (ototoxicity).',
          learningDomain: 'Clinical Pharmacology'
        },
        {
          id: 'ms-q7',
          questionNumber: 7,
          questionText: 'Under CDC and NMCN guidelines, what is the maximum recommended interval for changing a transparent semi-permeable central venous catheter dressing in the absence of soiling or loosening?',
          options: [
            { id: 'A', text: 'Every 24 hours' },
            { id: 'B', text: 'Every 7 days (or immediately if damp, loosened, or soiled)' },
            { id: 'C', text: 'Every 30 days' },
            { id: 'D', text: 'Dressings should never be changed once placed' }
          ],
          correctAnswer: 'B',
          explanation: 'Transparent CVAD dressings should be changed at least every 7 days (every 2 days for gauze dressings) unless soiled or loose, minimizing catheter disruption and bloodstream infections.',
          learningDomain: 'Vascular Access Standards'
        },
        {
          id: 'ms-q8',
          questionNumber: 8,
          questionText: 'In healthcare waste management, which color-coded bin is statutorily designated for infectious dressings, swabs, and human tissue contaminated with body fluids?',
          options: [
            { id: 'A', text: 'Black bag' },
            { id: 'B', text: 'Yellow bag' },
            { id: 'C', text: 'Brown bag' },
            { id: 'D', text: 'Green bag' }
          ],
          correctAnswer: 'B',
          explanation: 'Yellow is the international and statutory Nigerian code for biohazardous, infectious clinical waste requiring high-temperature incineration.',
          learningDomain: 'Hospital Waste Governance'
        },
        {
          id: 'ms-q9',
          questionNumber: 9,
          questionText: 'Which laboratory biomarker is the most sensitive diagnostic indicator of tissue hypoperfusion, anaerobic metabolism, and septic shock progression in postoperative patients?',
          options: [
            { id: 'A', text: 'Serum Creatinine' },
            { id: 'B', text: 'Serum Lactate (> 2.0 mmol/L)' },
            { id: 'C', text: 'Serum Sodium' },
            { id: 'D', text: 'Serum Albumin' }
          ],
          correctAnswer: 'B',
          explanation: 'Serum lactate reflects cellular hypoxia and anaerobic glycolysis due to systemic hypoperfusion. Levels > 2.0 mmol/L demand aggressive hemodynamic fluid resuscitation.',
          learningDomain: 'Critical Care Biomarkers'
        },
        {
          id: 'ms-q10',
          questionNumber: 10,
          questionText: 'What is the correct cleansing stroke sequence when preparing an elliptical surgical midline incision with clean surrounding skin?',
          options: [
            { id: 'A', text: 'From the outer periphery towards the incision center' },
            { id: 'B', text: 'From the incision center directly outwards, moving from least to most contaminated' },
            { id: 'C', text: 'Circular vigorous scrubbing back and forth across the incision line' },
            { id: 'D', text: 'Cleansing the drainage bag before the incision' }
          ],
          correctAnswer: 'B',
          explanation: 'Surgical wounds are cleansed from the cleanest area (the surgical incision itself) outward to the periphery to prevent introducing skin bacteria into the healing incision.',
          learningDomain: 'Aseptic Technique'
        }
      ]
    }
  },
  {
    id: 'spec-maternal-midwifery',
    code: 'NMCN-MIDWIFERY-02',
    title: 'Maternal & Obstetric Nursing (Midwifery)',
    regulatoryTitle: 'Post-Basic Midwifery & Perinatal Healthcare Licensure',
    statutoryAuthority: 'NMCN Midwifery Examination & Regulatory Directives / WHO Standards',
    description:
      'Advanced obstetric intrapartum care, active management of the third stage of labour (AMTSL), postpartum hemorrhage (PPH) prevention, emergency neonatal resuscitation, and partograph interpretation.',
    competencyDomains: [
      'Active Management of Third Stage of Labour (AMTSL)',
      'Postpartum Hemorrhage Prevention & Management',
      'Fetal Well-being & Partograph Plotting',
      'Obstetric Pharmacotherapy (Oxytocics & Tocolytics)',
      'Neonatal Resuscitation & APGAR Scoring'
    ],
    passMarkPercentage: 50.0,
    distinctionPercentage: 75.0,
    station: {
      id: 'nmcn-st-midwifery',
      title: 'Active Management of Third Stage of Labour (AMTSL) & PPH Prevention',
      subTitle: 'Twin Exclusion, Uterotonic Administration, Controlled Cord Traction & Fundal Massage',
      clinicalScenario:
        'A 27-year-old Gravida 3 Para 2 mother has just given birth vaginally to a live, vigorous term male infant weighing 3.4 kg. The baby has been dried, clamped, cut, and placed in skin-to-skin contact on the mother’s chest. The placenta remains undelivered. The midwife must execute the Active Management of the Third Stage of Labour to prevent catastrophic postpartum hemorrhage.',
      doorBriefing:
        'Candidate Door Brief: You are the Midwifery Officer in the Labor Ward. Enter the delivery room, palpate the mother’s abdomen to definitively exclude an undiagnosed second twin, administer prophylactic uterotonic therapy, perform controlled cord traction upon signs of placental separation, inspect the placenta and membranes, and initiate fundal massage. You will then answer 10 statutory licensure MCQs.',
      candidateInstructions: [
        'Palpate the maternal abdomen immediately to confirm the absence of a second twin.',
        'Administer Oxytocin 10 IU IM within 1 minute of childbirth.',
        'Observe for signs of placental separation before applying traction.',
        'Execute Controlled Cord Traction (Brandt-Andrews technique) with counter-traction.',
        'Examine placenta and fetal membranes for completeness (cotyledons and vessels).',
        'Perform immediate fundal massage and assess postpartum blood loss.'
      ],
      patientProfile: {
        name: 'Fatima Garba',
        age: 27,
        gender: 'Female',
        setting: 'Maternity Labor & Delivery Suite (Bed 2)',
        chiefComplaint: 'Normal spontaneous vaginal delivery completed 1 minute ago; placenta in utero.',
        historyOfPresentIllness: 'Uncomplicated term labor lasting 7 hours. Delivered 3.4 kg healthy male infant with APGAR scores 9 and 10.',
        currentMedications: ['Prenatal iron and folic acid'],
        allergies: ['NKDA']
      },
      entryVitals: {
        bloodPressure: '116/74 mmHg',
        heartRate: '82 bpm',
        respiratoryRate: '18 cpm',
        temperature: '36.8 °C',
        oxygenSaturation: '99% on room air',
        painOrDistressScore: 'Moderate uterine cramping'
      },
      equipmentTray: [
        'Oxytocin 10 IU ampoule with 2 mL sterile syringe and 21G/23G needle',
        'Sterile delivery gloves and waterproof maternity apron',
        'Sterile cord clamp, Mayo scissors, and Spencer Wells artery forceps',
        'Placenta basin and calibrated postpartum blood collection drape',
        'Sterile gauze swabs and sanitary maternity pads'
      ],
      fatalErrorNotice:
        'CRITICAL RED FLAG / FATAL ERROR: Administering oxytocin or ergometrine BEFORE palpating the abdomen to exclude an undiagnosed second twin, or pulling vigorously on the umbilical cord without suprapubic counter-traction (causing uterine inversion) triggers an automatic Station Referral (Score capped at 49%).',
      checklist: [
        {
          id: 'mid-c1',
          stepNumber: 1,
          instruction: 'Palpate the maternal abdomen immediately after delivery of the infant to definitively rule out the presence of an undiagnosed second twin.',
          rationale: 'Administering uterotonics with an undiagnosed twin in utero causes severe tetanic contractions, fetal hypoxia, and uterine rupture.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Administering uterotonic drugs without palpating to exclude a second twin causes fetal asphyxiation and death.',
          category: 'Preparation & Safety'
        },
        {
          id: 'mid-c2',
          stepNumber: 2,
          instruction: 'Administer Oxytocin 10 IU Intramuscularly into the maternal anterolateral thigh (vastus lateralis) within 1 minute of birth.',
          rationale: 'Oxytocin within 1 minute is the cornerstone of AMTSL, reducing severe PPH incidence by up to 60%.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'mid-c3',
          stepNumber: 3,
          instruction: 'Observe for classical signs of placental separation: sudden lengthening of the umbilical cord, a gush of blood from the vagina, and uterus rising and becoming firm and globular.',
          rationale: 'Applying traction before separation risks avulsion of the cord and catastrophic uterine inversion.',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'mid-c4',
          stepNumber: 4,
          instruction: 'Place one hand on the lower abdomen above the symphysis pubis to apply gentle upward counter-traction, while the other hand applies steady downward Controlled Cord Traction (Brandt-Andrews technique).',
          rationale: 'Suprapubic counter-traction prevents the uterine fundus from being pulled down into the vaginal vault.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Pulling on the umbilical cord without suprapubic counter-traction precipitates acute uterine inversion and fatal neurogenic shock.',
          category: 'Intervention & Procedure'
        },
        {
          id: 'mid-c5',
          stepNumber: 5,
          instruction: 'As the placenta emerges at the introitus, support it with both hands and gently twist it in a slow clockwise motion to wind the membranes into a rope.',
          rationale: 'Twisting the membranes prevents ragged tearing and retention of succenturiate placental lobes.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'mid-c6',
          stepNumber: 6,
          instruction: 'Perform immediate, vigorous transabdominal fundal massage until the uterus is hard and contracted ("cricket ball" firmness).',
          rationale: 'Uterine contraction constricts the interlacing myometrial fibers, sealing bleeding maternal spiral arterioles.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'mid-c7',
          stepNumber: 7,
          instruction: 'Thoroughly examine the maternal surface of the placenta to ensure all cotyledons are intact and fit together without missing lobules.',
          rationale: 'Retained placental fragments are the leading cause of secondary postpartum hemorrhage and puerperal sepsis.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Failing to inspect the placenta and missing retained cotyledons causes life-threatening postpartum hemorrhage.',
          category: 'Assessment & Communication'
        },
        {
          id: 'mid-c8',
          stepNumber: 8,
          instruction: 'Examine the fetal surface and membranes: trace umbilical vessels to the margin to rule out vasa previa or a torn vessel indicating a retained succenturiate lobe.',
          rationale: 'Vessels extending across membranes that terminate abruptly indicate a retained extra lobe.',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'mid-c9',
          stepNumber: 9,
          instruction: 'Inspect the perineum, vagina, and cervix under good illumination to identify and stage any lacerations, tears, or active hematomas.',
          rationale: 'Trauma to the genital tract is the second most common cause of early postpartum hemorrhage (the "4 Ts").',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'mid-c10',
          stepNumber: 10,
          instruction: 'Teach the mother to self-palpate her uterine fundus, measure baseline postpartum vitals (BP, pulse), calculate cumulative blood loss, and document in statutory birth register.',
          rationale: 'Empowering the mother to recognize uterine atony enables immediate detection of secondary bleeding.',
          points: 10,
          isCriticalFail: false,
          category: 'Evaluation & Documentation'
        }
      ],
      mcqs: [
        {
          id: 'mid-q1',
          questionNumber: 1,
          questionText: 'Under WHO and NMCN clinical guidelines, what are the three mandatory components that constitute Active Management of the Third Stage of Labour (AMTSL)?',
          options: [
            { id: 'A', text: 'Fundal pressure, early cord clamping, and maternal bear-down efforts' },
            { id: 'B', text: 'Administration of a prophylactic uterotonic (Oxytocin), Controlled Cord Traction (CCT), and immediate uterine fundal massage' },
            { id: 'C', text: 'Intravenous ergometrine, manual removal of placenta, and cold abdominal packs' },
            { id: 'D', text: 'Waiting 60 minutes for spontaneous expulsion without medication' }
          ],
          correctAnswer: 'B',
          explanation: 'AMTSL comprises three evidence-based interventions: (1) administration of a uterotonic drug within 1 minute, (2) controlled cord traction with counter-traction, and (3) uterine massage.',
          learningDomain: 'Obstetric Protocols'
        },
        {
          id: 'mid-q2',
          questionNumber: 2,
          questionText: 'Why is Ergometrine (or Methylergonovine) strictly contraindicated in pregnant or intrapartum women with pre-eclampsia or chronic hypertension?',
          options: [
            { id: 'A', text: 'It causes severe fetal hypoglycemia' },
            { id: 'B', text: 'It induces systemic vasoconstriction, precipitating severe hypertensive crises, cerebrovascular hemorrhage (stroke), and convulsions' },
            { id: 'C', text: 'It causes acute placental abruption in future pregnancies' },
            { id: 'D', text: 'It permanently suppresses maternal breast milk production' }
          ],
          correctAnswer: 'B',
          explanation: 'Ergot alkaloids cause intense peripheral vasoconstriction. In hypertensive or pre-eclamptic women, ergometrine can trigger dangerous blood pressure spikes, intracranial hemorrhage, and maternal death. Oxytocin is the uterotonic of choice.',
          learningDomain: 'Obstetric Pharmacology'
        },
        {
          id: 'mid-q3',
          questionNumber: 3,
          questionText: 'What is the diagnostic threshold volume for primary Postpartum Hemorrhage (PPH) following a normal spontaneous vaginal delivery?',
          options: [
            { id: 'A', text: 'Loss of > 100 mL of blood' },
            { id: 'B', text: 'Cumulative blood loss of ≥ 500 mL within 24 hours of delivery (or ≥ 1,000 mL following Cesarean delivery)' },
            { id: 'C', text: 'Loss of > 2,000 mL exclusively' },
            { id: 'D', text: 'Any vaginal bleeding during labor' }
          ],
          correctAnswer: 'B',
          explanation: 'Primary PPH is defined as blood loss $\ge 500$ mL following vaginal delivery or $\ge 1,000$ mL following Cesarean section, or any blood loss causing hemodynamic compromise.',
          learningDomain: 'PPH Definitions'
        },
        {
          id: 'mid-q4',
          questionNumber: 4,
          questionText: 'Which mnemonic framework represents the four most common etiologies of primary Postpartum Hemorrhage?',
          options: [
            { id: 'A', text: 'The 4 As (Airway, Acidosis, Anemia, Atony)' },
            { id: 'B', text: 'The 4 Ts (Tone [uterine atony], Tissue [retained placenta], Trauma [lacerations], and Thrombin [coagulopathy])' },
            { id: 'C', text: 'The 4 Cs (Cord, Cervix, Contraction, Clamp)' },
            { id: 'D', text: 'The 4 Ps (Passage, Passenger, Powers, Psyche)' }
          ],
          correctAnswer: 'B',
          explanation: 'The 4 Ts summarize PPH etiologies: Tone (uterine atony, ~70%), Trauma (~20%), Tissue (retained products, ~10%), and Thrombin (coagulopathies, <1%).',
          learningDomain: 'Etiology & Staging'
        },
        {
          id: 'mid-q5',
          questionNumber: 5,
          questionText: 'When interpreting the WHO Modified Partograph, what is the mandatory clinical response when cervical dilatation crosses the "Action Line" (4 hours to the right of the Alert Line)?',
          options: [
            { id: 'A', text: 'Instruct the mother to sleep for 6 hours' },
            { id: 'B', text: 'Immediate decision-making by obstetrician/senior midwife: evaluate for cephalopelvic disproportion (CPD), augment with oxytocin if obstructed labor is ruled out, or prepare for emergency Cesarean section' },
            { id: 'C', text: 'Discharge the mother home immediately' },
            { id: 'D', text: 'Stop all fetal heart rate monitoring' }
          ],
          correctAnswer: 'B',
          explanation: 'Crossing the Action Line indicates prolonged/obstructed labor. Immediate intervention is mandatory to prevent uterine rupture, vesicovaginal fistula (VVF), and fetal asphyxia.',
          learningDomain: 'Partograph Interpretation'
        },
        {
          id: 'mid-q6',
          questionNumber: 6,
          questionText: 'What is the recommended first-line non-surgical physical intervention for unremitting uterine atony and severe hemorrhage while awaiting surgical assistance?',
          options: [
            { id: 'A', text: 'External aortic compression or Bimanual Uterine Compression' },
            { id: 'B', text: 'Applying warm heating pads to the maternal abdomen' },
            { id: 'C', text: 'Placing the mother in reverse Trendelenburg position' },
            { id: 'D', text: 'Inserting a Foley catheter into the rectum' }
          ],
          correctAnswer: 'A',
          explanation: 'Bimanual uterine compression (one gloved hand in anterior vaginal fornix, the other compressing the fundus through the abdominal wall) compresses spiral arteries directly, halting hemorrhage.',
          learningDomain: 'Emergency Obstetric Maneuvers'
        },
        {
          id: 'mid-q7',
          questionNumber: 7,
          questionText: 'What temperature must oxytocin ampoules be maintained at to guarantee potency in tropical healthcare settings?',
          options: [
            { id: 'A', text: 'Stored on the open delivery trolley in direct sunlight (+35°C to +40°C)' },
            { id: 'B', text: 'Continuous cold-chain refrigeration between +2 °C and +8 °C' },
            { id: 'C', text: 'Frozen solid at -20 °C' },
            { id: 'D', text: 'Boiled daily for sterilization' }
          ],
          correctAnswer: 'B',
          explanation: 'Oxytocin is heat-labile and degrades rapidly at ambient tropical temperatures. WHO guidelines mandate cold-chain storage (+2°C to +8°C) to prevent catastrophic drug failure during PPH.',
          learningDomain: 'Drug Stability & Storage'
        },
        {
          id: 'mid-q8',
          questionNumber: 8,
          questionText: 'Which prostaglandin E1 analogue tablet is recommended by the WHO for PPH prevention and treatment when injectable oxytocin is unavailable or cold chain is compromised?',
          options: [
            { id: 'A', text: 'Misoprostol' },
            { id: 'B', text: 'Metformin' },
            { id: 'C', text: 'Mifepristone' },
            { id: 'D', text: 'Methotrexate' }
          ],
          correctAnswer: 'A',
          explanation: 'Misoprostol (sublingual or rectal) is heat-stable and does not require refrigeration, making it the WHO-recommended alternative uterotonic in low-resource and community outreach settings.',
          learningDomain: 'Uterotonic Alternatives'
        },
        {
          id: 'mid-q9',
          questionNumber: 9,
          questionText: 'What is the defining clinical characteristic of acute Uterine Inversion occurring during third stage management?',
          options: [
            { id: 'A', text: 'A hard, contracted fundus located 2 cm below the umbilicus' },
            { id: 'B', text: 'Absence of the uterine fundus on abdominal palpation, sudden severe neurogenic shock, profound bradycardia/hypotension, and a bluish-red mass visible at the introitus' },
            { id: 'C', text: 'Sudden onset of polyuria without bleeding' },
            { id: 'D', text: 'Fetal tachycardia on auscultation' }
          ],
          correctAnswer: 'B',
          explanation: 'Uterine inversion occurs when the fundus collapses into the cavity and through the cervix. Traction on peritoneal nerves induces profound neurogenic shock and massive hemorrhage.',
          learningDomain: 'Obstetric Emergencies'
        },
        {
          id: 'mid-q10',
          questionNumber: 10,
          questionText: 'In APGAR scoring of a newborn at 1 and 5 minutes, what 5 clinical signs are evaluated, each scored from 0 to 2?',
          options: [
            { id: 'A', text: 'Weight, height, head circumference, gestational age, and blood group' },
            { id: 'B', text: 'Appearance (color), Pulse (heart rate), Grimace (reflex irritability), Activity (muscle tone), and Respiration' },
            { id: 'C', text: 'Temperature, blood pressure, urine output, stool color, and suck reflex' },
            { id: 'D', text: 'Maternal blood pressure, placental weight, cord length, crying volume, and eye color' }
          ],
          correctAnswer: 'B',
          explanation: 'APGAR evaluates: Appearance (0=blue/pale, 1=acrocyanotic, 2=pink), Pulse (0=absent, 1=<100, 2=>100), Grimace, Activity, and Respiration (0=absent, 1=slow/irregular, 2=vigorous cry).',
          learningDomain: 'Neonatal Resuscitation'
        }
      ]
    }
  },
  {
    id: 'spec-pediatric-child-health',
    code: 'NMCN-PEDIATRIC-03',
    title: 'Pediatric & Neonatal Nursing',
    regulatoryTitle: 'Post-Basic Paediatric Nursing Licensure',
    statutoryAuthority: 'NMCN Child Health Guidelines / WHO IMCI Protocols',
    description:
      'Pediatric emergency assessment, Integrated Management of Childhood Illness (IMCI), management of severe dehydration and hypovolemic shock (WHO Plan C), pediatric medication safety, and neonatal resuscitation.',
    competencyDomains: [
      'IMCI Clinical Staging & Triage',
      'Pediatric Fluid Resuscitation (WHO Plan C)',
      'Pediatric Pharmacokinetics & Micro-Dosing',
      'Neonatal Sepsis & Thermal Regulation',
      'Nutritional Rehabilitation in Severe Acute Malnutrition'
    ],
    passMarkPercentage: 50.0,
    distinctionPercentage: 75.0,
    station: {
      id: 'nmcn-st-pediatric',
      title: 'Severe Dehydrating Gastroenteritis & Hypovolemic Shock Resuscitation',
      subTitle: 'WHO Plan C Rapid Intravenous Rehydration, Potassium Safety & Zinc Supplementation',
      clinicalScenario:
        'A 14-month-old infant weighing 10 kg is rushed to the pediatric emergency unit by his mother. The child has had watery diarrhea (10–12 times per day) and frequent vomiting for 48 hours. On examination, the infant is lethargic and floppy, eyes are deeply sunken, the anterior fontanelle is markedly depressed, skin pinch on the abdomen retracts very slowly (> 2 seconds), and radial pulses are weak and thready with cold extremities.',
      doorBriefing:
        'Candidate Door Brief: You are the Senior Paediatric Nurse in the Pediatric Emergency Room. A 14-month-old infant in severe dehydration and hypovolemic shock requires immediate resuscitation. Enter the treatment bay, execute the WHO Plan C Intravenous Rehydration protocol, calculate and administer the correct fluid bolus volume and rate, monitor neurological status, and plan oral zinc and maintenance therapy. You will then answer 10 statutory licensure MCQs.',
      candidateInstructions: [
        'Rapidly stage dehydration according to WHO / IMCI criteria.',
        'Calculate total rehydration fluid volume for severe dehydration (100 mL/kg).',
        'Divide fluid administration across initial rapid phase (30 mL/kg in 30 mins) and maintenance phase (70 mL/kg in 2.5 hours).',
        'Select the appropriate crystalloid solution (Ringer’s Lactate or Normal Saline).',
        'Verify urine output before adding potassium chloride to prevent fatal hyperkalemic arrest.',
        'Prescribe oral zinc supplementation (20 mg/day for 14 days) and ORS upon clinical recovery.'
      ],
      patientProfile: {
        name: 'Tunde Adeleke',
        age: '14 Months',
        gender: 'Male',
        setting: 'Pediatric Emergency Resuscitation Unit (Cot 4)',
        chiefComplaint: 'Profuse watery diarrhea, vomiting, lethargy, and inability to drink fluids.',
        historyOfPresentIllness: 'Watery rotavirus diarrhea began 2 days ago; ceased tolerating breast milk this morning.',
        currentMedications: ['None; received home salt-sugar solution yesterday'],
        allergies: ['NKDA']
      },
      entryVitals: {
        bloodPressure: '68/42 mmHg (Pediatric Hypotension)',
        heartRate: '168 bpm (Marked Sinus Tachycardia)',
        respiratoryRate: '44 cpm (Tachypnea without retractions)',
        temperature: '38.2 °C',
        oxygenSaturation: '95% on room air',
        painOrDistressScore: 'AVPU: Responds only to Pain (P); CRT: 4 seconds'
      },
      equipmentTray: [
        'Ringer’s Lactate 500 mL IV infusion bags',
        'Pediatric 60 drops/mL micro-drip volumetric infusion set (Burette)',
        'Pediatric IV cannulas (24G yellow and 22G blue) and tourniquet',
        'Oral Rehydration Salts (ORS) packets and clean measuring jug',
        'Elemental Zinc sulphate dispersible tablets 20 mg',
        'Capillary blood glucose glucometer and lancets'
      ],
      fatalErrorNotice:
        'CRITICAL RED FLAG / FATAL ERROR: Adding potassium chloride (KCl) to intravenous fluids before the child has passed urine (triggering fatal hyperkalemic cardiac arrest in acute anuria) or infusing hypotonic plain dextrose (5% D/W) without electrolytes triggers an automatic Station Referral (Score capped at 49%).',
      checklist: [
        {
          id: 'ped-c1',
          stepNumber: 1,
          instruction: 'Assess Airway, Breathing, Circulation, and rapidly stage dehydration using WHO/IMCI criteria (lethargic, sunken eyes, skin pinch > 2s, absent radial pulse = Severe Dehydration).',
          rationale: 'Severe dehydration is a medical emergency requiring immediate intravenous access.',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'ped-c2',
          stepNumber: 2,
          instruction: 'Select WHO Plan C Intravenous Rehydration and calculate total fluid requirement: 100 mL/kg (for 10 kg infant = 1,000 mL total).',
          rationale: 'WHO Plan C provides 100 mL/kg of isotonic crystalloids to replace deficit and ongoing losses.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ped-c3',
          stepNumber: 3,
          instruction: 'Select appropriate IV solution: Ringer’s Lactate (preferred) or 0.9% Normal Saline; strictly avoid plain 5% Dextrose in Water (D5W).',
          rationale: 'Isotonic crystalloids expand intravascular volume; D5W is hypotonic and precipitates fatal cerebral edema.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Infusing plain 5% Dextrose in Water for hypovolemic shock causes acute hyponatremia and fatal cerebral herniation.',
          category: 'Intervention & Procedure'
        },
        {
          id: 'ped-c4',
          stepNumber: 4,
          instruction: 'Administer the initial rapid fluid bolus: for infants ≥ 1 year, infuse 30 mL/kg (300 mL) over 30 minutes (or 1 hour if under 12 months).',
          rationale: 'Rapid bolus administration restores central circulating volume, blood pressure, and renal perfusion.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ped-c5',
          stepNumber: 5,
          instruction: 'Perform capillary blood glucose test immediately to rule out secondary pediatric hypoglycemia.',
          rationale: 'Infants have minimal hepatic glycogen stores; severe gastroenteritis frequently produces life-threatening hypoglycemia.',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'ped-c6',
          stepNumber: 6,
          instruction: 'Re-evaluate child at 30 minutes: check radial pulse strength, capillary refill time, heart rate, and level of consciousness.',
          rationale: 'If radial pulse remains undetectable, repeat the 30 mL/kg bolus immediately.',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'ped-c7',
          stepNumber: 7,
          instruction: 'Infuse remainder of fluid: 70 mL/kg (700 mL) over 2.5 hours (or 5 hours if under 12 months) via pediatric burette.',
          rationale: 'Sustained replacement replenishes intracellular and interstitial fluid compartments.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ped-c8',
          stepNumber: 8,
          instruction: 'Enforce strict potassium safety: NEVER add potassium chloride (KCl) to IV infusion until the child has voided urine and established adequate renal function.',
          rationale: 'Administering KCl in anuric shock produces abrupt, lethal hyperkalemic asystole.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Adding potassium chloride to IV fluids in an oliguric/anuric child triggers lethal hyperkalemic cardiac arrest.',
          category: 'Intervention & Procedure'
        },
        {
          id: 'ped-c9',
          stepNumber: 9,
          instruction: 'As soon as the child can drink without vomiting, introduce Oral Rehydration Salts (ORS) solution (5 mL/kg/hour) while IV infusion continues.',
          rationale: 'Oral ORS supplies potassium and base while accelerating enterocyte sodium-glucose cotransport recovery.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ped-c10',
          stepNumber: 10,
          instruction: 'Prescribe dispersible Zinc Sulphate 20 mg daily for 14 days, educate mother on continued breastfeeding, hygiene, and danger signs.',
          rationale: 'Zinc reduces the duration and severity of diarrhea and prevents recurrence for 2-3 months (WHO/UNICEF).',
          points: 10,
          isCriticalFail: false,
          category: 'Evaluation & Documentation'
        }
      ],
      mcqs: [
        {
          id: 'ped-q1',
          questionNumber: 1,
          questionText: 'Under WHO IMCI guidelines, what are the four clinical signs of "Severe Dehydration", of which at least two must be present to mandate WHO Plan C?',
          options: [
            { id: 'A', text: 'Dry skin, hunger, active crying, and mild fever' },
            { id: 'B', text: 'Lethargy or unconsciousness, sunken eyes, inability to drink or drinking poorly, and skin pinch going back very slowly (> 2 seconds)' },
            { id: 'C', text: 'Profuse sweating, hypertension, polyuria, and hyperactive reflexes' },
            { id: 'D', text: 'Bulging fontanelle, cough, stridor, and peripheral edema' }
          ],
          correctAnswer: 'B',
          explanation: 'Severe dehydration is defined by at least two of: (1) lethargy/unconsciousness, (2) sunken eyes, (3) not able to drink/drinking poorly, and (4) skin pinch going back very slowly (>2s).',
          learningDomain: 'IMCI Dehydration Staging'
        },
        {
          id: 'ped-q2',
          questionNumber: 2,
          questionText: 'What is the total volume of intravenous fluid per kilogram allocated for rehydrating a child with severe dehydration under WHO Plan C?',
          options: [
            { id: 'A', text: '20 mL/kg' },
            { id: 'B', text: '50 mL/kg' },
            { id: 'C', text: '100 mL/kg' },
            { id: 'D', text: '200 mL/kg' }
          ],
          correctAnswer: 'C',
          explanation: 'WHO Plan C specifies 100 mL/kg of Ringer’s Lactate or Normal Saline, divided into a 30 mL/kg rapid bolus followed by a 70 mL/kg slower infusion.',
          learningDomain: 'Fluid Math'
        },
        {
          id: 'ped-q3',
          questionNumber: 3,
          questionText: 'Why is Ringer’s Lactate internationally preferred over 0.9% Normal Saline for large-volume pediatric fluid resuscitation in acute diarrhea?',
          options: [
            { id: 'A', text: 'Ringer’s lactate contains broad-spectrum antibiotics' },
            { id: 'B', text: 'Ringer’s lactate is a balanced physiological solution containing lactate (which is metabolized to bicarbonate) and prevents hyperchloremic metabolic acidosis' },
            { id: 'C', text: 'Ringer’s lactate tastes sweet and can be drunk orally' },
            { id: 'D', text: 'Normal saline causes immediate acute renal failure in all children' }
          ],
          correctAnswer: 'B',
          explanation: 'Massive infusions of 0.9% Saline (154 mEq/L chloride) cause hyperchloremic acidosis. Ringer’s Lactate has a lower chloride concentration and contains lactate, which converts to bicarbonate in the liver.',
          learningDomain: 'Fluid Physiology'
        },
        {
          id: 'ped-q4',
          questionNumber: 4,
          questionText: 'What is the statutory daily dose and duration of oral Zinc supplementation recommended by the WHO for children over 6 months with acute diarrhea?',
          options: [
            { id: 'A', text: '5 mg daily for 2 days' },
            { id: 'B', text: '20 mg daily for 10 to 14 days (10 mg daily for infants under 6 months)' },
            { id: 'C', text: '100 mg daily for 1 month' },
            { id: 'D', text: 'Zinc is strictly contraindicated in pediatric diarrhea' }
          ],
          correctAnswer: 'B',
          explanation: 'WHO/UNICEF recommend 20 mg elemental zinc daily for 10-14 days for children > 6 months (10 mg for infants < 6 months) to repair intestinal mucosa and boost immune defense.',
          learningDomain: 'Nutritional Pediatrics'
        },
        {
          id: 'ped-q5',
          questionNumber: 5,
          questionText: 'Why must potassium chloride (KCl) NEVER be added to intravenous fluids in a severely dehydrated child until after the child has urinated?',
          options: [
            { id: 'A', text: 'Potassium prevents the absorption of glucose' },
            { id: 'B', text: 'In acute dehydration, temporary renal shutdown (anuria) is common; infusing potassium into an anuric patient causes rapid lethal hyperkalemia and cardiac arrest' },
            { id: 'C', text: 'Potassium causes acute diarrhea' },
            { id: 'D', text: 'Potassium degrades intravenous plastic tubing' }
          ],
          correctAnswer: 'B',
          explanation: 'Potassium is excreted almost entirely by the kidneys. If an oliguric child is administered IV potassium, serum levels escalate rapidly, precipitating peaked T waves, ventricular fibrillation, and asystole.',
          learningDomain: 'Electrolyte Safety'
        },
        {
          id: 'ped-q6',
          questionNumber: 6,
          questionText: 'In a 9-month-old infant presenting with acute fever, poor feeding, lethargy, full fontanelle, and purpuric rash, what is the immediate priority diagnostic procedure?',
          options: [
            { id: 'A', text: 'Immediate lumbar puncture (unless signs of raised intracranial pressure / shock are present) and blood cultures before antibiotics' },
            { id: 'B', text: 'Waiting 48 hours for outpatient pediatric clinic' },
            { id: 'C', text: 'Stool microscopy for parasites only' },
            { id: 'D', text: 'Administering high-dose oral aspirin' }
          ],
          correctAnswer: 'A',
          explanation: 'Fever, full fontanelle, and purpura indicate acute bacterial (meningococcal) meningitis or septicemia. Blood cultures and CSF analysis guide life-saving antimicrobial therapy.',
          learningDomain: 'Pediatric Infections'
        },
        {
          id: 'ped-q7',
          questionNumber: 7,
          questionText: 'Which physical finding distinguishes Kwashiorkor from Marasmus in severe acute malnutrition (SAM)?',
          options: [
            { id: 'A', text: 'Extreme muscle wasting only' },
            { id: 'B', text: 'Bilateral pitting nutritional edema (starting in the feet), hepatomegaly, and "flaky paint" dermatosis' },
            { id: 'C', text: 'Excessive appetite and hyperactivity' },
            { id: 'D', text: 'Normal serum albumin levels' }
          ],
          correctAnswer: 'B',
          explanation: 'Kwashiorkor is characterized by bilateral pitting pedal edema, moon face, enlarged fatty liver, and cutaneous dyspigmentation, caused by protein deficiency relative to calories.',
          learningDomain: 'Malnutrition Staging'
        },
        {
          id: 'ped-q8',
          questionNumber: 8,
          questionText: 'In the initial stabilization phase of a child with Severe Acute Malnutrition (SAM), why are high-protein feeds and high-sodium IV fluids strictly avoided?',
          options: [
            { id: 'A', text: 'They cause severe diarrhea' },
            { id: 'B', text: 'Malnourished children have reduced renal capacity and impaired cellular sodium pumps; high sodium and protein trigger congestive heart failure and Refeeding Syndrome' },
            { id: 'C', text: 'They cause rapid tooth decay' },
            { id: 'D', text: 'Protein cannot be swallowed by infants' }
          ],
          correctAnswer: 'B',
          explanation: 'SAM children have depleted intracellular potassium/phosphate and compromised cardiac output. High sodium/protein loads trigger circulatory overload and fatal refeeding hypophosphatemia.',
          learningDomain: 'Refeeding Syndrome Safety'
        },
        {
          id: 'ped-q9',
          questionNumber: 9,
          questionText: 'What is the first and most critical action in the neonatal resuscitation algorithm for a non-breathing, limp newborn with heart rate < 100 bpm?',
          options: [
            { id: 'A', text: 'Immediate intravenous epinephrine' },
            { id: 'B', text: 'Position head in "sniffing" position, clear airway if obstructed, and initiate Positive Pressure Ventilation (PPV) with bag and mask within the first golden minute' },
            { id: 'C', text: 'Chest compressions at 120/min without ventilation' },
            { id: 'D', text: 'Submerging the newborn in cold water' }
          ],
          correctAnswer: 'B',
          explanation: 'Neonatal resuscitation is primarily respiratory. Effective bag-mask positive pressure ventilation (PPV) with room air within the first golden minute expands fluid-filled alveoli and restores cardiac rate.',
          learningDomain: 'Neonatal Resuscitation'
        },
        {
          id: 'ped-q10',
          questionNumber: 10,
          questionText: 'Which physiological factor makes infants and young children significantly more vulnerable to rapid hypovolemic shock than adults?',
          options: [
            { id: 'A', text: 'Infants have a much higher percentage of Total Body Water (75–80%) with a larger proportion in the extracellular fluid compartment, combined with higher metabolic rates' },
            { id: 'B', text: 'Infants have thicker skin that does not sweat' },
            { id: 'C', text: 'Infants cannot metabolize glucose' },
            { id: 'D', text: 'Infants have double the adult blood volume per kilogram' }
          ],
          correctAnswer: 'A',
          explanation: 'Infants have 75–80% body weight as water (mostly ECF) and high surface-area-to-mass ratios. Diarrheal fluid loss depletes intravascular volume much faster than in adults.',
          learningDomain: 'Pediatric Fluid Physiology'
        }
      ]
    }
  },
  {
    id: 'spec-community-public-health',
    code: 'NMCN-PUBHEALTH-04',
    title: 'Community & Public Health Nursing',
    regulatoryTitle: 'Post-Basic Public Health Nursing Licensure',
    statutoryAuthority: 'NMCN Public Health Directives / WHO EPI Guidelines',
    description:
      'Community health assessment, primary health care (PHC) management, vaccine cold-chain integrity, Expanded Programme on Immunization (EPI), outbreak surveillance, and maternal-child health outreaches.',
    competencyDomains: [
      'Vaccine Cold Chain Maintenance & VVM Audit',
      'EPI Immunization Scheduling & Technique',
      'Epidemiological Disease Surveillance (IDSR)',
      'Primary Health Care Management',
      'Outbreak Response & Infection Control'
    ],
    passMarkPercentage: 50.0,
    distinctionPercentage: 75.0,
    station: {
      id: 'nmcn-st-publichealth',
      title: 'Vaccine Cold-Chain Integrity, EPI Immunizations & Outreach Safety',
      subTitle: 'Vaccine Vial Monitor (VVM) Staging, Shake Test Protocol & Open-Vial Multi-Dose Policy',
      clinicalScenario:
        'You are the Community Health Nurse in charge of a primary health care immunization outreach post in a rural peri-urban settlement. The outreach ice-lined cold box was transported 4 hours ago under high ambient temperatures (34°C). A queue of mothers and infants has gathered for routine EPI immunizations (BCG, Pentavalent, OPV, Measles, and Yellow Fever). Before administering vaccines, you must perform a mandatory cold-chain audit and safe injection inspection.',
      doorBriefing:
        'Candidate Door Brief: Enter the Primary Healthcare outreach clinic. Audit the vaccine cold box, verify the digital thermometer reading, evaluate the Vaccine Vial Monitors (VVM) across all vaccine vials, identify heat-damaged or frozen vials, discard compromised stock, enforce the WHO Open-Vial Policy, and execute a safe intradermal BCG and intramuscular Pentavalent administration. You will then answer 10 statutory licensure MCQs.',
      candidateInstructions: [
        'Check and record the cold-box internal temperature log (+2 °C to +8 °C).',
        'Inspect and correctly stage the Vaccine Vial Monitors (VVM 1 to 4).',
        'Identify vials that MUST NOT be used (VVM Stage 3 and 4, or inner square same color or darker than circle).',
        'Perform the Shake Test on suspected frozen freeze-sensitive vaccines (Pentavalent / Td / Hep B).',
        'Enforce the WHO Open-Vial Multi-Dose Policy for reconstituted lyophilized vaccines (discard after 6 hours).',
        'Demonstrate correct anatomical sites, needle sizes, and routes for BCG and Pentavalent vaccines.'
      ],
      patientProfile: {
        name: 'Fatima & Baby Amina',
        age: '6 Weeks',
        gender: 'Female Infant',
        setting: 'Primary Healthcare Centre (PHC) Immunization Station',
        chiefComplaint: 'Scheduled 6-week routine immunization visit (Pentavalent 1, OPV 1, PCV 1, Rotavirus 1).',
        historyOfPresentIllness: 'Term infant, received BCG and OPV 0 at birth. Healthy, afebrile, feeding well.',
        currentMedications: ['None'],
        allergies: ['NKDA']
      },
      entryVitals: {
        bloodPressure: 'Normal for age',
        heartRate: '136 bpm',
        respiratoryRate: '34 cpm',
        temperature: '36.7 °C',
        oxygenSaturation: '99% on ambient air',
        painOrDistressScore: 'Calm, interactive infant'
      },
      equipmentTray: [
        'Vaccine cold box with 4 conditioned ice-packs and internal digital stem thermometer',
        'Vaccine vials with VVM indicators: Pentavalent (DTP-HepB-Hib), OPV, BCG, and Measles with diluents',
        'Auto-disable (AD) immunization syringes: 0.05 mL, 0.5 mL, and reconstitution syringes',
        'Yellow rigid cardboard safety box for immediate sharps disposal',
        'Cotton wool balls and clean tap water (no alcohol swabs for live vaccines)',
        'EPI Immunization Child Register and Child Health Card'
      ],
      fatalErrorNotice:
        'CRITICAL RED FLAG / FATAL ERROR: Administering a vaccine with a VVM at Stage 3 or 4 (heat damage), administering freeze-sensitive vaccines that failed the shake test, or using reconstituted BCG or Measles vaccine beyond 6 hours (toxic shock / fatal sepsis) triggers an automatic Station Referral (Score capped at 49%).',
      checklist: [
        {
          id: 'ph-c1',
          stepNumber: 1,
          instruction: 'Inspect the cold-box internal thermometer immediately upon opening and verify temperature is within the statutory safe range (+2 °C to +8 °C).',
          rationale: 'Vaccines lose potency when exposed to temperatures above +8°C or below +2°C.',
          points: 10,
          isCriticalFail: false,
          category: 'Preparation & Safety'
        },
        {
          id: 'ph-c2',
          stepNumber: 2,
          instruction: 'Examine the Vaccine Vial Monitor (VVM) on each vial: compare the color of the inner square with the outer reference circle.',
          rationale: 'VVMs provide visual cumulative heat exposure data directly on the vial label.',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'ph-c3',
          stepNumber: 3,
          instruction: 'Identify and immediately discard vials where the inner square is the same color as or darker than the outer circle (VVM Stage 3 and 4).',
          rationale: 'VVM 3 and 4 indicate irreversible heat denaturation and zero immunogenic potency.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Administering a vaccine with VVM Stage 3 or 4 provides zero immunity while exposing the infant to unsafe degraded biologicals.',
          category: 'Intervention & Procedure'
        },
        {
          id: 'ph-c4',
          stepNumber: 4,
          instruction: 'Perform the Shake Test on suspected frozen liquid vaccines (Pentavalent, Td, HepB): shake test vial alongside a deliberately frozen-thawed control vial and observe sedimentation rate.',
          rationale: 'Freeze-sensitive vaccines contain aluminum adjuvants that aggregate when frozen; frozen vials sediment much faster than undamaged vials.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Administering freeze-damaged aluminum-adjuvanted vaccines causes sterile abscesses and lack of protection.',
          category: 'Intervention & Procedure'
        },
        {
          id: 'ph-c5',
          stepNumber: 5,
          instruction: 'Reconstitute freeze-dried vaccines (BCG and Measles) strictly using the manufacturer-provided specific diluent kept at the same cold-chain temperature.',
          rationale: 'Using sterile water or unchilled diluents causes thermal shock and alters osmolarity.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ph-c6',
          stepNumber: 6,
          instruction: 'Enforce the WHO Open-Vial Policy: discard reconstituted vials of BCG and Measles strictly within 6 hours of reconstitution (or at end of session).',
          rationale: 'Reconstituted lyophilized vaccines have no preservative; bacterial contamination causes fatal Staphylococcal Toxic Shock Syndrome.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Administering reconstituted BCG or Measles vaccine after 6 hours has caused documented child fatalities from bacterial contamination.',
          category: 'Intervention & Procedure'
        },
        {
          id: 'ph-c7',
          stepNumber: 7,
          instruction: 'Administer Pentavalent vaccine: 0.5 mL Intramuscularly (IM) into the anterolateral aspect of the left thigh (vastus lateralis) using a 0.5 mL Auto-Disable (AD) syringe.',
          rationale: 'The anterolateral thigh is the safest muscle group in infants, avoiding the sciatic nerve in the buttocks.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ph-c8',
          stepNumber: 8,
          instruction: 'Administer Oral Polio Vaccine (OPV): 2 drops orally directly onto the tongue, avoiding touching the dropper to the oral mucosa.',
          rationale: 'Contact between dropper and saliva contaminates the multi-dose vial.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'ph-c9',
          stepNumber: 9,
          instruction: 'Discard all used needles and AD syringes immediately into the yellow rigid safety box without recapping or bending needles.',
          rationale: 'Never recapping needles eliminates needle-stick injuries and bloodborne pathogen transmission.',
          points: 10,
          isCriticalFail: false,
          category: 'Preparation & Safety'
        },
        {
          id: 'ph-c10',
          stepNumber: 10,
          instruction: 'Record vaccines administered in child health card and register, counsel mother on expected adverse events (mild fever, local swelling), and schedule next 10-week visit.',
          rationale: 'Accurate record keeping and tracking prevent dropouts and missed opportunities.',
          points: 10,
          isCriticalFail: false,
          category: 'Evaluation & Documentation'
        }
      ],
      mcqs: [
        {
          id: 'ph-q1',
          questionNumber: 1,
          questionText: 'What is the statutory temperature range for the storage of all EPI vaccines in refrigerators and cold boxes at the health facility level?',
          options: [
            { id: 'A', text: '-20 °C to -10 °C' },
            { id: 'B', text: '+2 °C to +8 °C' },
            { id: 'C', text: '+15 °C to +25 °C' },
            { id: 'D', text: 'Any temperature provided the vials are kept in darkness' }
          ],
          correctAnswer: 'B',
          explanation: 'The standard cold-chain storage temperature for all vaccines at service delivery level is +2°C to +8°C.',
          learningDomain: 'Cold Chain Standards'
        },
        {
          id: 'ph-q2',
          questionNumber: 2,
          questionText: 'Which class of vaccines is irreversibly destroyed by freezing (temperatures < 0°C) and must NEVER be placed in direct contact with frozen ice packs?',
          options: [
            { id: 'A', text: 'Oral Polio Vaccine (OPV)' },
            { id: 'B', text: 'Freeze-sensitive liquid vaccines containing aluminum adjuvants (Pentavalent [DTP-HepB-Hib], Td, Hepatitis B, PCV, and IPV)' },
            { id: 'C', text: 'Lyophilized BCG vaccine' },
            { id: 'D', text: 'Lyophilized Measles vaccine' }
          ],
          correctAnswer: 'B',
          explanation: 'Adsorbed vaccines contain aluminum salts. Freezing breaks the antigen-adjuvant lattice, forming gritty precipitates that cause sterile abscesses and zero immunogenicity.',
          learningDomain: 'Freeze Sensitivity'
        },
        {
          id: 'ph-q3',
          questionNumber: 3,
          questionText: 'In interpreting a Vaccine Vial Monitor (VVM), what visual appearance dictates that the vaccine has reached its discard point and MUST NOT be used?',
          options: [
            { id: 'A', text: 'The inner square is lighter in color than the outer reference circle' },
            { id: 'B', text: 'The inner square matches the color of the outer circle, or the inner square is darker than the outer circle' },
            { id: 'C', text: 'The circle is completely white and the square is blue' },
            { id: 'D', text: 'The vial label is missing a serial number' }
          ],
          correctAnswer: 'B',
          explanation: 'VVM Stages 1 and 2 (inner square lighter than circle) can be used. When the square matches or becomes darker than the circle (Stages 3 and 4), heat exposure has destroyed potency.',
          learningDomain: 'VVM Interpretation'
        },
        {
          id: 'ph-q4',
          questionNumber: 4,
          questionText: 'Under the WHO Open-Vial Multi-Dose Policy, what is the maximum duration for which reconstituted lyophilized vaccines (such as BCG and Measles-Rubella) can be safely kept before mandatory disposal?',
          options: [
            { id: 'A', text: 'Up to 28 days if kept refrigerated' },
            { id: 'B', text: 'A maximum of 6 hours (or at the end of the immunization session, whichever comes first)' },
            { id: 'C', text: 'Until the vial is empty, regardless of time' },
            { id: 'D', text: '48 hours' }
          ],
          correctAnswer: 'B',
          explanation: 'Reconstituted BCG and Measles contain no bacteriostatic preservatives. After 6 hours, bacterial growth can produce fatal toxic shock syndrome; vials must be discarded.',
          learningDomain: 'Open-Vial Policy'
        },
        {
          id: 'ph-q5',
          questionNumber: 5,
          questionText: 'Why is the gluteal muscle (buttocks) strictly contraindicated for intramuscular vaccine injections in infants and children under 2 years of age?',
          options: [
            { id: 'A', text: 'The muscle absorbs vaccines too quickly' },
            { id: 'B', text: 'High risk of irreversible injury to the sciatic nerve and deep thick subcutaneous fat layer preventing intramuscular deposition' },
            { id: 'C', text: 'It causes acute constipation' },
            { id: 'D', text: 'The skin in the gluteal region cannot be sterilized' }
          ],
          correctAnswer: 'B',
          explanation: 'In infants, the sciatic nerve has variable anatomy and runs near the surface. Injection into the buttock causes sciatic neuropathy and paralysis. The anterolateral thigh (vastus lateralis) is mandatory.',
          learningDomain: 'Injection Safety'
        },
        {
          id: 'ph-q6',
          questionNumber: 6,
          questionText: 'What is the correct anatomical site, route, and needle angle for the administration of the BCG (Bacille Calmette-Guérin) vaccine in a newborn?',
          options: [
            { id: 'A', text: 'Deep Intramuscular (90°) in the left gluteus' },
            { id: 'B', text: 'Strictly Intradermal (10° to 15° angle with bevel up) into the insertion of the left deltoid muscle' },
            { id: 'C', text: 'Subcutaneous (45°) in the anterior abdominal wall' },
            { id: 'D', text: 'Oral drops onto the tongue' }
          ],
          correctAnswer: 'B',
          explanation: 'BCG must be injected strictly intradermally at a 10-15° angle over the left deltoid to produce a discrete wheal (peau d’orange). Subcutaneous injection causes severe chronic ulceration and lymphadenitis.',
          learningDomain: 'Vaccine Administration'
        },
        {
          id: 'ph-q7',
          questionNumber: 7,
          questionText: 'What is the Shake Test used to determine in community immunization practice?',
          options: [
            { id: 'A', text: 'Whether a vaccine vial contains bacterial contamination' },
            { id: 'B', text: 'Whether a freeze-sensitive aluminum-adjuvanted vaccine has suffered irreversible freeze damage' },
            { id: 'C', text: 'The volume of vaccine remaining in an opaque vial' },
            { id: 'D', text: 'Whether the vaccine syringe needle is blocked' }
          ],
          correctAnswer: 'B',
          explanation: 'The Shake Test compares the sedimentation rate of a suspected frozen vial against a frozen control. Damaged vials sediment rapidly and form a clear supernatant; intact vials remain cloudy longer.',
          learningDomain: 'Cold Chain Quality Control'
        },
        {
          id: 'ph-q8',
          questionNumber: 8,
          questionText: 'Under the Integrated Disease Surveillance and Response (IDSR) framework, which category of diseases mandates immediate reporting within 24 hours to the LGA / State Epidemiologist?',
          options: [
            { id: 'A', text: 'Mild tension headaches and acne' },
            { id: 'B', text: 'Epidemic-prone diseases with high outbreak potential (e.g., Cholera, Yellow Fever, Lassa Fever, Measles, and Acute Flaccid Paralysis [Polio])' },
            { id: 'C', text: 'Chronic hypertension in geriatric patients' },
            { id: 'D', text: 'Uncomplicated dental caries' }
          ],
          correctAnswer: 'B',
          explanation: 'IDSR Class 1 epidemic-prone diseases demand immediate case-based notification within 24 hours to trigger epidemiological ring vaccination, contact tracing, and outbreak containment.',
          learningDomain: 'Disease Surveillance (IDSR)'
        },
        {
          id: 'ph-q9',
          questionNumber: 9,
          questionText: 'Why should alcohol swabs or chemical antiseptics NOT be used to cleanse the skin prior to administering live attenuated viral vaccines (such as BCG or Measles)?',
          options: [
            { id: 'A', text: 'Alcohol makes the injection completely painless' },
            { id: 'B', text: 'Residual chemical antiseptic can inactivate or kill the live attenuated organisms, destroying the vaccine’s ability to induce immune protection' },
            { id: 'C', text: 'Alcohol causes immediate permanent skin tattooing' },
            { id: 'D', text: 'Alcohol makes the child intoxicated' }
          ],
          correctAnswer: 'B',
          explanation: 'Live attenuated vaccines rely on live organism replication. Residual alcohol destroys the organisms. Skin should be cleaned with sterile water or allowed to dry completely if alcohol is used.',
          learningDomain: 'Vaccine Immunology'
        },
        {
          id: 'ph-q10',
          questionNumber: 10,
          questionText: 'What is the definition of "Herd Immunity" (Community Immunity) in public health epidemiology?',
          options: [
            { id: 'A', text: 'Immunity acquired by domestic livestock in rural communities' },
            { id: 'B', text: 'Indirect protection from an infectious disease that occurs when a high proportion of a population is immune, making person-to-person spread unlikely and shielding vulnerable non-immune individuals' },
            { id: 'C', text: 'Immunity obtained exclusively through contracting wild viral infection' },
            { id: 'D', text: 'A statutory ban on international travel' }
          ],
          correctAnswer: 'B',
          explanation: 'Herd immunity occurs when high immunization coverage breaks chains of transmission, protecting individuals who cannot be vaccinated (e.g. infants, immunocompromised children).',
          learningDomain: 'Epidemiology Principles'
        }
      ]
    }
  },
  {
    id: 'spec-emergency-critical-care',
    code: 'NMCN-EMERG-05',
    title: 'Emergency, Trauma & Critical Care Nursing',
    regulatoryTitle: 'Post-Basic Accident, Emergency & Critical Care Licensure',
    statutoryAuthority: 'NMCN Trauma Nursing Committee / ATLS & ABCDE Frameworks',
    description:
      'Advanced trauma life support (ATLS), primary and secondary survey execution, in-line cervical spine immobilization, hemorrhagic shock resuscitation, tension pneumothorax decompression, and emergency triage.',
    competencyDomains: [
      'Primary Survey (ABCDE) & Immediate Life-Saving Resuscitation',
      'In-Line Cervical Spine Protection & Log-Roll',
      'Thoracic Trauma & Needle Thoracostomy / Chest Tube Care',
      'Hemorrhagic Shock & Massive Transfusion Protocol',
      'Neurological Assessment (Glasgow Coma Scale - GCS)'
    ],
    passMarkPercentage: 50.0,
    distinctionPercentage: 75.0,
    station: {
      id: 'nmcn-st-emergency',
      title: 'Polytrauma Primary Survey, In-Line C-Spine Protection & Hemorrhagic Shock',
      subTitle: 'ATLS ABCDE Execution, Tension Pneumothorax Identification & Pelvic Stabilization',
      clinicalScenario:
        'A 32-year-old male driver was involved in a high-speed head-on motor vehicle collision. He was unrestrained and ejected through the windscreen. He arrives in the emergency resuscitation bay strapped to a spine board. He has severe facial lacerations, labored breathing, tracheal deviation to the left, absent breath sounds on the right hemithorax, distended neck veins, and an unstable pelvis with pelvic pain. He is pale, cool, and clammy with unpalpable radial pulses.',
      doorBriefing:
        'Candidate Door Brief: You are the Senior Emergency & Trauma Nurse leading the trauma resuscitation team. Enter the resuscitation bay, execute a systematic ATLS Primary Survey (ABCDE) while maintaining manual in-line cervical spine stabilization, identify life-threatening thoracic trauma (tension pneumothorax), apply pelvic stabilization, and initiate massive hemorrhage resuscitation. You will then answer 10 statutory licensure MCQs.',
      candidateInstructions: [
        'Maintain manual in-line cervical spine stabilization throughout airway assessment.',
        'Assess Airway: perform jaw thrust/chin lift without head extension; clear secretions.',
        'Assess Breathing: identify tension pneumothorax (tracheal deviation, absent right breath sounds, hyper-resonance) and prepare immediate needle chest decompression.',
        'Assess Circulation: identify class III/IV hemorrhagic shock, apply pelvic binder, and establish two wide-bore 14G/16G IV lines for rapid warmed crystalloid/blood infusion.',
        'Assess Disability: rapid Glasgow Coma Scale (GCS) and bilateral pupillary light reflex.',
        'Assess Exposure: log-roll patient maintaining spinal axis, inspect back, and prevent hypothermia.'
      ],
      patientProfile: {
        name: 'Oluwaseun Bakare',
        age: 32,
        gender: 'Male',
        setting: 'Level 1 Trauma Centre Emergency Resuscitation Bay',
        chiefComplaint: 'Blunt polytrauma following high-speed motor vehicle collision; dyspnea and shock.',
        historyOfPresentIllness: 'Ejected through windscreen 35 minutes ago; extricated by road safety team.',
        currentMedications: ['Unknown'],
        allergies: ['Unknown']
      },
      entryVitals: {
        bloodPressure: '76/48 mmHg (Severe Hemorrhagic Shock)',
        heartRate: '142 bpm (Severe Sinus Tachycardia)',
        respiratoryRate: '36 cpm (Severe Tachypnea)',
        temperature: '35.4 °C (Hypothermia Risk)',
        oxygenSaturation: '86% on room air',
        painOrDistressScore: 'GCS: 8/15 (E2 V2 M4) • Extremity CRT > 4s'
      },
      equipmentTray: [
        'Rigid cervical collar and manual in-line head immobilization blocks',
        'High-flow non-rebreather oxygen mask (15 L/min with reservoir bag)',
        '14G / 16G large-bore intravenous cannulas and blood transfusion sets',
        '14G 8cm needle decompression catheter (for 2nd intercostal space mid-clavicular line)',
        'Commercial pelvic circumferential compression binder (or folded draw-sheet)',
        'Warm forced-air warming blanket and trauma shears'
      ],
      fatalErrorNotice:
        'CRITICAL RED FLAG / FATAL ERROR: Tilting the head or hyperextending the neck to open the airway in suspected cervical spine trauma (risking transection of the spinal cord), or delaying decompression of a tension pneumothorax while waiting for a chest X-ray triggers an automatic Station Referral (Score capped at 49%).',
      checklist: [
        {
          id: 'em-c1',
          stepNumber: 1,
          instruction: 'Assign an assistant to maintain continuous manual in-line cervical spine stabilization, strictly avoiding any head tilt, flexion, or rotational movement.',
          rationale: 'Blunt polytrauma above the clavicle carries up to a 10% risk of unstable cervical spine fractures; movement risks spinal cord transection.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Tilting the head or hyperextending the neck in suspected spine trauma causes complete spinal cord transection and quadriplegia.',
          category: 'Preparation & Safety'
        },
        {
          id: 'em-c2',
          stepNumber: 2,
          instruction: 'Assess Airway (A): inspect for blood, broken teeth, or tongue obstruction, clear airway using rigid suction (Yankauer), and perform gentle jaw-thrust maneuver.',
          rationale: 'The jaw-thrust opens the pharynx without extending the cervical spine.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'em-c3',
          stepNumber: 3,
          instruction: 'Assess Breathing (B): apply high-flow oxygen (15 L/min via non-rebreather mask), inspect chest wall excursion, and auscultate bilateral breath sounds.',
          rationale: 'Hypoxia rapidly compounds traumatic brain injury and myocardial ischemia.',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'em-c4',
          stepNumber: 4,
          instruction: 'Diagnose Tension Pneumothorax: recognize tracheal shift to left, absent breath sounds on right, distended neck veins, and hypotension.',
          rationale: 'Tension pneumothorax is a clinical diagnosis; waiting for radiological imaging results in cardiac arrest.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Delaying decompression of a tension pneumothorax to await a chest X-ray causes total obstructive shock and death within minutes.',
          category: 'Assessment & Communication'
        },
        {
          id: 'em-c5',
          stepNumber: 5,
          instruction: 'Execute immediate Needle Decompression: insert a 14G cannula (minimum 7–8 cm) into the 2nd intercostal space mid-clavicular line (or 4th/5th ICS anterior axillary line) on the right.',
          rationale: 'Releases trapped pleural air, relieves mediastinal compression, and restores venous return to the heart.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'em-c6',
          stepNumber: 6,
          instruction: 'Assess Circulation (C): establish two large-bore (14G or 16G) IV cannulas in antecubital fossae, send blood for cross-match, and initiate warmed crystalloids/O-negative blood.',
          rationale: 'Wide-bore peripheral lines deliver higher flow rates (Poiseuille’s law) than central lines in acute exsanguination.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'em-c7',
          stepNumber: 7,
          instruction: 'Examine pelvis: recognize pelvic instability/crepitus and immediately apply a commercial Pelvic Binder (centered over greater trochanters) without repeated spring testing.',
          rationale: 'Repeated pelvic manipulation dislodges retroperitoneal clots and worsens catastrophic venous bleeding.',
          points: 10,
          isCriticalFail: true,
          criticalFailReason: 'Repeatedly springing an unstable fractured pelvis or failing to apply a pelvic binder causes fatal retroperitoneal exsanguination.',
          category: 'Intervention & Procedure'
        },
        {
          id: 'em-c8',
          stepNumber: 8,
          instruction: 'Assess Disability (D): calculate Glasgow Coma Scale (GCS = 8), check pupil symmetry and light reactivity, and test capillary blood glucose.',
          rationale: 'GCS ≤ 8 defines severe traumatic brain injury mandating endotracheal intubation for airway protection.',
          points: 10,
          isCriticalFail: false,
          category: 'Assessment & Communication'
        },
        {
          id: 'em-c9',
          stepNumber: 9,
          instruction: 'Assess Exposure (E) and Log-Roll: perform a coordinated 4-person log-roll maintaining anatomical spinal alignment, inspect spinal column and rectum, and remove wet clothing.',
          rationale: 'Detects occult penetrating trauma, step-offs, and spinal tenderness while preventing cord injury.',
          points: 10,
          isCriticalFail: false,
          category: 'Intervention & Procedure'
        },
        {
          id: 'em-c10',
          stepNumber: 10,
          instruction: 'Institute immediate aggressive hypothermia prevention: apply warm blankets, warmed IV fluids, cover patient, and alert the trauma theater for damage control surgery.',
          rationale: 'Hypothermia triggers the fatal trauma triad (Hypothermia, Coagulopathy, Acidosis).',
          points: 10,
          isCriticalFail: false,
          category: 'Evaluation & Documentation'
        }
      ],
      mcqs: [
        {
          id: 'em-q1',
          questionNumber: 1,
          questionText: 'In trauma resuscitation, why is the Jaw-Thrust maneuver preferred over the Head-Tilt/Chin-Lift maneuver for establishing airway patency in unconscious trauma patients?',
          options: [
            { id: 'A', text: 'It requires fewer clinicians to perform' },
            { id: 'B', text: 'It lifts the tongue away from the posterior pharyngeal wall without extending or flexing the potentially injured cervical spine' },
            { id: 'C', text: 'It automatically clears blood clots from the larynx' },
            { id: 'D', text: 'It stimulates spontaneous respiration by reflex' }
          ],
          correctAnswer: 'B',
          explanation: 'The head-tilt hyperextends the neck and can transect the cervical spinal cord if an unstable fracture is present. The jaw-thrust mobilizes the mandible forward with zero cervical spinal motion.',
          learningDomain: 'Airway Management'
        },
        {
          id: 'em-q2',
          questionNumber: 2,
          questionText: 'What is the physiological mechanism of cardiovascular collapse in an untreated Tension Pneumothorax?',
          options: [
            { id: 'A', text: 'Severe coronary vasospasm' },
            { id: 'B', text: 'Massive intra-pleural pressure shifts the mediastinum, kinking the inferior and superior vena cavae, completely blocking venous return and dropping cardiac output to zero' },
            { id: 'C', text: 'Acute hyperkalemia' },
            { id: 'D', text: 'Rapid rupture of the stomach' }
          ],
          correctAnswer: 'B',
          explanation: 'One-way valve air trapping builds massive intrathoracic pressure, collapsing the ipsilateral lung, shifting the mediastinum, compressing the vena cavae, and halting venous return, producing fatal obstructive shock.',
          learningDomain: 'Thoracic Pathophysiology'
        },
        {
          id: 'em-q3',
          questionNumber: 3,
          questionText: 'What three physiological derangements comprise the lethal "Trauma Triad of Death"?',
          options: [
            { id: 'A', text: 'Hypertension, tachycardia, and hyperglycemia' },
            { id: 'B', text: 'Hypothermia, Acidosis, and Coagulopathy' },
            { id: 'C', text: 'Hyperthermia, leukocytosis, and oliguria' },
            { id: 'D', text: 'Anemia, jaundice, and ascites' }
          ],
          correctAnswer: 'B',
          explanation: 'Hypothermia impairs enzyme coagulation; metabolic acidosis further halts thrombin generation; coagulopathy accelerates blood loss, establishing a fatal self-reinforcing downward spiral.',
          learningDomain: 'Trauma Triad of Death'
        },
        {
          id: 'em-q4',
          questionNumber: 4,
          questionText: 'What is the correct anatomical landmark for placing a commercial pelvic circumferential compression binder in an unstable open-book pelvic fracture?',
          options: [
            { id: 'A', text: 'Directly over the iliac crests' },
            { id: 'B', text: 'Centered directly over the greater trochanters of both femurs' },
            { id: 'C', text: 'Around the upper ribcage' },
            { id: 'D', text: 'Around the mid-thighs' }
          ],
          correctAnswer: 'B',
          explanation: 'The pelvic binder must be centered at the level of the greater trochanters (symphysis pubis level). Placing it too high over the iliac crests fails to close the pelvic ring and may worsen pelvic bleeding.',
          learningDomain: 'Pelvic Trauma Resuscitation'
        },
        {
          id: 'em-q5',
          questionNumber: 5,
          questionText: 'What is the recommended ratio of Packed Red Blood Cells (PRBCs), Fresh Frozen Plasma (FFP), and Platelets in modern Damage Control Massive Transfusion Protocols (MTP)?',
          options: [
            { id: 'A', text: '10 : 1 : 1' },
            { id: 'B', text: '1 : 1 : 1 (balanced hemostatic resuscitation)' },
            { id: 'C', text: '1 : 5 : 10' },
            { id: 'D', text: 'Crystalloids only with zero blood products' }
          ],
          correctAnswer: 'B',
          explanation: 'Modern 1:1:1 balanced resuscitation replicates whole blood, replenishing clotting factors and platelets simultaneously with red cells, dramatically cutting mortality from trauma coagulopathy.',
          learningDomain: 'Massive Transfusion Protocol'
        },
        {
          id: 'em-q6',
          questionNumber: 6,
          questionText: 'A trauma patient has a Glasgow Coma Scale (GCS) score of 7 (Eyes: 2, Verbal: 2, Motor: 3). What is the mandatory immediate airway management decision?',
          options: [
            { id: 'A', text: 'Provide 2 L/min oxygen via nasal prongs and monitor' },
            { id: 'B', text: 'Immediate definitive endotracheal intubation with rapid sequence induction (RSI) and cervical spine protection ("GCS ≤ 8 = Intubate")' },
            { id: 'C', text: 'Discharge to ward for observation' },
            { id: 'D', text: 'Administer oral glucose tablets' }
          ],
          correctAnswer: 'B',
          explanation: 'Patients with a GCS of 8 or less lose protective laryngeal and pharyngeal reflexes, facing catastrophic aspiration and hypoventilation. Immediate endotracheal intubation is the universal rule.',
          learningDomain: 'Neurotrauma & GCS'
        },
        {
          id: 'em-q7',
          questionNumber: 7,
          questionText: 'According to Poiseuille’s Law, which IV access device provides the fastest flow rate for rapid volume resuscitation in hemorrhagic shock?',
          options: [
            { id: 'A', text: 'A long, narrow 20G triple-lumen central venous catheter' },
            { id: 'B', text: 'A short, large-bore (14G or 16G) peripheral intravenous catheter placed in the antecubital fossa' },
            { id: 'C', text: 'A 24G pediatric scalp vein cannula' },
            { id: 'D', text: 'A radial artery cannula' }
          ],
          correctAnswer: 'B',
          explanation: 'Flow rate is inversely proportional to catheter length and directly proportional to the 4th power of radius. Short, wide peripheral lines deliver crystalloids and blood much faster than narrow central lines.',
          learningDomain: 'Vascular Access Physics'
        },
        {
          id: 'em-q8',
          questionNumber: 8,
          questionText: 'Which physical sign differentiates Cardiac Tamponade from Tension Pneumothorax in blunt chest trauma?',
          options: [
            { id: 'A', text: 'Presence of hypertension' },
            { id: 'B', text: 'In cardiac tamponade, breath sounds are equal bilaterally and the trachea is midline, whereas tension pneumothorax features absent unilateral breath sounds and deviated trachea' },
            { id: 'C', text: 'Cardiac tamponade causes instant leg paralysis' },
            { id: 'D', text: 'Tension pneumothorax never causes hypotension' }
          ],
          correctAnswer: 'B',
          explanation: 'Both cause obstructive shock and distended neck veins. However, cardiac tamponade displays bilateral breath sounds with midline trachea, while tension pneumothorax produces unilateral silent breath sounds and tracheal shift.',
          learningDomain: 'Thoracic Trauma Differential'
        },
        {
          id: 'em-q9',
          questionNumber: 9,
          questionText: 'What is Beck’s Triad, classically indicative of acute Cardiac Tamponade?',
          options: [
            { id: 'A', text: 'Fever, cough, and hemoptysis' },
            { id: 'B', text: 'Hypotension, Muffled/Distant heart sounds, and Jugular Venous Distension (JVD)' },
            { id: 'C', text: 'Bradycardia, hypertension, and bradypnea' },
            { id: 'D', text: 'Abdominal rigidity, vomiting, and jaundice' }
          ],
          correctAnswer: 'B',
          explanation: 'Beck’s triad consists of hypotension (low stroke volume), muffled heart sounds (fluid in pericardial sac insulating sound), and jugular venous distension (impaired right atrial filling).',
          learningDomain: 'Clinical Syndromes'
        },
        {
          id: 'em-q10',
          questionNumber: 10,
          questionText: 'In emergency triage under mass casualty incidents (e.g., START triage), what triage category is assigned to a victim who is unresponsive with absent respirations even after manually repositioning the airway?',
          options: [
            { id: 'A', text: 'Red (Immediate / Priority 1)' },
            { id: 'B', text: 'Yellow (Delayed / Priority 2)' },
            { id: 'C', text: 'Green (Minor / Walking Wounded)' },
            { id: 'D', text: 'Black (Expectant / Deceased)' }
          ],
          correctAnswer: 'D',
          explanation: 'In mass casualty triage, resources are directed to salvageable patients. If a victim has no spontaneous respirations after opening the airway, they are triaged as Black (Deceased/Expectant).',
          learningDomain: 'Disaster Triage (START)'
        }
      ]
    }
  }
];
