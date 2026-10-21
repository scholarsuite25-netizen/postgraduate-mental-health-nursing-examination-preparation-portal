import { Question } from '../types';
import { MOD1_2_QUESTIONS } from './questions_mod1_2';
import { MOD3_4_QUESTIONS } from './questions_mod3_4';
import { MOD5_6_QUESTIONS } from './questions_mod5_6';
import { MOD7_8_QUESTIONS } from './questions_mod7_8';
import { MOD9_10_QUESTIONS } from './questions_mod9_10';
import { MOD11_12_QUESTIONS } from './questions_mod11_12';
import { MOD13_14_QUESTIONS } from './questions_mod13_14';

export const PROVISIONAL_MODULES = [
  "1. Foundations of Mental Health Nursing",
  "2. Psychiatric Assessment and Mental Status Examination",
  "3. Psychopathology and Psychiatric Diagnosis",
  "4. Psychopharmacology and Medication Management",
  "5. Psychotherapy and Therapeutic Communication",
  "6. Psychiatric Emergencies and Crisis Intervention",
  "7. Community Mental Health and Psychiatric Rehabilitation",
  "8. Child, Adolescent, and Older Adult Mental Health",
  "9. Psychiatric Nursing Ethics, Law, and Human Rights",
  "10. Research Methods and Evidence-Based Practice",
  "11. Advanced Clinical Scenarios",
  "12. Leadership and Professional Practice",
  "13. Substance Use Disorders and Dual Diagnosis",
  "14. Special Populations and Culturally Relevant Practice"
];

// ─── Seed questions (14 verified hand-crafted questions) ─────────────────────
export const INITIAL_QUESTION_BANK: Question[] = [
  {
    id: "MHN-Q001",
    module: "1. Foundations of Mental Health Nursing",
    topic: "Historical Evolution of Psychiatric Nursing",
    difficulty: "Foundation",
    questionText: "Who is widely recognized as the first American psychiatric nurse who laid the foundation for psychiatric nursing theory and education through her pioneering work in the late 19th century?",
    options: [
      { id: "A", text: "Hildegard Peplau" },
      { id: "B", text: "Linda Richards" },
      { id: "C", text: "Dorothea Dix" },
      { id: "D", text: "Clifford Beers" }
    ],
    correctAnswer: "B",
    explanation: "Linda Richards is recognized as America's first trained nurse, having graduated from the New England Hospital for Women and Children in 1873. She went on to specialize in psychiatric nursing and developed the first nursing care program in psychiatric hospitals.",
    incorrectExplanations: {
      A: "Hildegard Peplau formulated interpersonal nursing theory decades later.",
      C: "Dorothea Dix was a social reformer, not a trained nurse.",
      D: "Clifford Beers sparked the mental hygiene movement after personal hospitalization."
    },
    learningObjective: "Identify key historical figures who shaped the evolution of psychiatric and mental health nursing.",
    reference: "Boyd, M. A. (2020). Psychiatric Nursing: Contemporary Practice.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q002",
    module: "2. Psychiatric Assessment and Mental Status Examination",
    topic: "Mental Status Examination (MSE)",
    difficulty: "Intermediate",
    questionText: "During a mental status examination, a patient states that the television news anchor is speaking directly to them and broadcasting their private thoughts to the public. How is this perceptual or thought abnormality correctly documented?",
    options: [
      { id: "A", text: "Idea of reference" },
      { id: "B", text: "Delusion of control" },
      { id: "C", text: "Delusion of reference" },
      { id: "D", text: "Auditory hallucination" }
    ],
    correctAnswer: "C",
    explanation: "A delusion of reference is a fixed, false belief that innocuous events, objects, or communications (such as television broadcasts) carry a special, personal meaning specifically directed at the individual with absolute conviction.",
    incorrectExplanations: {
      A: "Ideas of reference lack absolute delusional conviction.",
      B: "Delusions of control involve belief that actions are controlled by external forces.",
      D: "Auditory hallucinations involve hearing voices without external stimuli."
    },
    learningObjective: "Accurately categorize and document thought content abnormalities during psychiatric assessment.",
    reference: "Sadock, B. J., & Sadock, V. A. (2018). Kaplan and Sadock's Synopsis of Psychiatry.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q003",
    module: "3. Psychopathology and Psychiatric Diagnosis",
    topic: "Mood Disorders and Major Depressive Episode",
    difficulty: "Foundation",
    questionText: "According to standard diagnostic criteria (such as DSM-5-TR), what is the minimum duration of continuous symptoms required for a diagnosis of Major Depressive Episode?",
    options: [
      { id: "A", text: "1 week" },
      { id: "B", text: "2 weeks" },
      { id: "C", text: "1 month" },
      { id: "D", text: "6 months" }
    ],
    correctAnswer: "B",
    explanation: "To meet diagnostic criteria for a Major Depressive Episode, a patient must exhibit five or more specific depressive symptoms during the same 2-week period representing a noticeable change from previous functioning.",
    incorrectExplanations: {
      A: "1 week aligns with manic or hypomanic episode durations.",
      C: "1 month applies to brief psychotic or acute stress disorders.",
      D: "6 months applies to generalized anxiety or schizophrenia duration criteria."
    },
    learningObjective: "Recall diagnostic criteria and timeframes for major depressive episodes in clinical practice.",
    reference: "American Psychiatric Association. (2022). DSM-5-TR.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q004",
    module: "4. Psychopharmacology and Medication Management",
    topic: "Antipsychotic Medications and Extrapyramidal Symptoms",
    difficulty: "Advanced",
    questionText: "A patient taking haloperidol for schizophrenia presents with severe muscular rigidity, a 'lead-pipe' muscle tone, hyperpyrexia (temperature 39.8°C), autonomic instability, and altered mental status. Which nursing intervention is most urgent?",
    options: [
      { id: "A", text: "Administer prescribed PRN benztropine and continue antipsychotic monitoring." },
      { id: "B", text: "Immediately withhold the antipsychotic medication and notify the medical team for emergency management." },
      { id: "C", text: "Apply cooling blankets and encourage oral fluid intake." },
      { id: "D", text: "Prepare the patient for immediate electroconvulsive therapy (ECT)." }
    ],
    correctAnswer: "B",
    explanation: "The presentation describes Neuroleptic Malignant Syndrome (NMS), a life-threatening neurological emergency. The absolute first priority is immediate discontinuation of the offending antipsychotic agent and emergency medical intervention.",
    incorrectExplanations: {
      A: "Benztropine is insufficient for NMS which requires immediate drug cessation.",
      C: "Cooling measures are supportive, but withholding the drug takes precedence.",
      D: "ECT is reserved for refractory cases after resuscitation and discontinuation."
    },
    learningObjective: "Recognize life-threatening psychopharmacological emergencies such as Neuroleptic Malignant Syndrome.",
    reference: "Stahl, S. M. (2021). Stahl's Essential Psychopharmacology.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q005",
    module: "5. Psychotherapy and Therapeutic Communication",
    topic: "Therapeutic Communication Techniques",
    difficulty: "Foundation",
    questionText: "A patient expresses intense grief and anxiety about starting new psychiatric medications, saying, 'I don't think I can ever feel normal again.' Which nursing response demonstrates the therapeutic communication technique of 'restating'?",
    options: [
      { id: "A", text: "'Why do you feel that way when your doctor is helping you?'" },
      { id: "B", text: "'You are going to feel much better once the medication reaches therapeutic levels.'" },
      { id: "C", text: "'You feel that regaining your normal life is out of reach right now?'" },
      { id: "D", text: "'Everything will work out fine; try not to worry so much.'" }
    ],
    correctAnswer: "C",
    explanation: "Restating involves repeating the core content of the patient's message using similar words to confirm understanding and encourage further exploration.",
    incorrectExplanations: {
      A: "Asking 'why' puts the patient on the defensive.",
      B: "Premature reassurance invalidates genuine patient distress.",
      D: "False reassurance shuts down open communication."
    },
    learningObjective: "Apply effective therapeutic communication techniques in clinical nurse-patient interactions.",
    reference: "Videbeck, S. L. (2019). Psychiatric-Mental Health Nursing.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q006",
    module: "6. Psychiatric Emergencies and Crisis Intervention",
    topic: "Suicide Risk Assessment and Safety Planning",
    difficulty: "Intermediate",
    questionText: "During an initial mental health assessment, a client admits to having passive suicidal ideation ('I wish I wouldn't wake up') but denies any active plan or intent. What is the most appropriate initial nursing action?",
    options: [
      { id: "A", text: "Place the client in continuous 1:1 constant visual observation immediately." },
      { id: "B", text: "Conduct a comprehensive suicide risk evaluation including lethality, access to means, and collaborative safety planning." },
      { id: "C", text: "Document the statement as minor depressive talk and proceed with routine outpatient education." },
      { id: "D", text: "Reassure the client that everyone has gloomy thoughts sometimes and advise them to sleep." }
    ],
    correctAnswer: "B",
    explanation: "Even passive suicidal ideation warrants a thorough risk assessment to evaluate specific intent, plan, means, history, and protective factors, followed by collaborative safety planning.",
    incorrectExplanations: {
      A: "Continuous 1:1 observation is indicated for active, imminent self-harm risk.",
      C: "Ignoring or minimizing passive ideation compromises patient safety.",
      D: "Minimizing patient distress is unprofessional and dangerous."
    },
    learningObjective: "Perform rigorous suicide risk evaluation and initiate appropriate safety interventions.",
    reference: "Townsend, M. C., & Morgan, K. I. (2022). Psychiatric Mental Health Nursing.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q007",
    module: "7. Community Mental Health and Psychiatric Rehabilitation",
    topic: "Community-Based Care and Assertive Community Treatment (ACT)",
    difficulty: "Intermediate",
    questionText: "Which patient population is the primary target for Assertive Community Treatment (ACT) multidisciplinary teams?",
    options: [
      { id: "A", text: "Clients with mild adjustment disorders experiencing temporary work stress" },
      { id: "B", text: "Older adults experiencing age-related mild cognitive impairment" },
      { id: "C", text: "Individuals with severe and persistent mental illness (SPMI) who experience frequent hospitalizations and difficulty engaging with traditional outpatient care" },
      { id: "D", text: "Children and adolescents with attention deficit hyperactivity disorder (ADHD)" }
    ],
    correctAnswer: "C",
    explanation: "ACT is an intensive, evidence-based community model specifically designed for individuals with severe and persistent mental illnesses who have high psychiatric hospitalization rates and struggle with conventional clinic settings.",
    incorrectExplanations: {
      A: "Mild adjustment disorders are managed via outpatient counseling.",
      B: "Mild cognitive impairment is managed in geriatric memory clinics.",
      D: "Youth ADHD is managed in pediatric and specialty youth clinics."
    },
    learningObjective: "Understand community mental health delivery models and the scope of Assertive Community Treatment.",
    reference: "Stuart, G. W. (2016). Principles and Practice of Psychiatric Nursing.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q008",
    module: "8. Child, Adolescent, and Older Adult Mental Health",
    topic: "Neurocognitive Disorders in Older Adults (Delirium vs. Dementia)",
    difficulty: "Intermediate",
    questionText: "A family brings their 78-year-old grandfather to the clinic because over the past 48 hours he has become fluctuatingly confused, highly agitated at night, and unable to sustain attention. What key feature distinguishes this presentation from major neurocognitive disorder (dementia)?",
    options: [
      { id: "A", text: "Insidious onset and slow, steady progression over several years" },
      { id: "B", text: "Acute onset, fluctuating course, and prominent disturbance in attention and consciousness" },
      { id: "C", text: "Intact alertness with selective memory deficits" },
      { id: "D", text: "Permanent, irreversible structural brain deterioration" }
    ],
    correctAnswer: "B",
    explanation: "Delirium is characterized by an acute onset, fluctuating course over hours to days, and hallmark impairments in attention and consciousness, distinguishing it from dementia's insidious progression.",
    incorrectExplanations: {
      A: "Insidious onset characterizes dementia.",
      C: "Alertness is compromised in delirium.",
      D: "Delirium is often acute and reversible when underlying causes are treated."
    },
    learningObjective: "Differentiate between delirium and neurocognitive disorders in older adult psychiatric nursing assessments.",
    reference: "Videbeck, S. L. (2019). Psychiatric-Mental Health Nursing.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q009",
    module: "9. Psychiatric Nursing Ethics, Law, and Human Rights",
    topic: "Involuntary Commitment and Patient Rights",
    difficulty: "Advanced",
    questionText: "A competent adult patient admitted voluntarily to an inpatient psychiatric unit demands immediate discharge against medical advice (AMA). The psychiatric nurse reviews the admission status and notes no legal holds or emergency detention orders. What is the nurse's correct legal and professional action?",
    options: [
      { id: "A", text: "Refuse discharge until the attending psychiatrist completes a 72-hour review." },
      { id: "B", text: "Facilitate the voluntary discharge process while ensuring safe transition planning and discharge education." },
      { id: "C", text: "Notify hospital security to detain the patient in their room." },
      { id: "D", text: "Contact the local court to convert the status to involuntary commitment immediately." }
    ],
    correctAnswer: "B",
    explanation: "Voluntary patients retain the right to request discharge at any time unless an evaluation indicates they meet criteria for involuntary emergency detention. Staff must process discharge safely.",
    incorrectExplanations: {
      A: "Voluntary patients cannot be arbitrarily held without legal justification.",
      C: "Detention without legal basis constitutes unlawful imprisonment.",
      D: "Involuntary conversion requires strict clinical criteria and formal legal documentation."
    },
    learningObjective: "Understand legal boundaries, voluntary admission rights, and ethical principles in psychiatric nursing.",
    reference: "Barker, P. J. (2009). Psychiatric and Mental Health Nursing: The Craft of Caring.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q010",
    module: "10. Research Methods and Evidence-Based Practice",
    topic: "Evidence-Based Practice in Mental Health Nursing",
    difficulty: "Advanced",
    questionText: "When formulating an evidence-based clinical question regarding the effectiveness of psychoeducation versus standard care on relapse rates in schizophrenia, which clinical inquiry framework is most appropriate?",
    options: [
      { id: "A", text: "PICO (Population, Intervention, Comparison, Outcome)" },
      { id: "B", text: "SOAP (Subjective, Objective, Assessment, Plan)" },
      { id: "C", text: "ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation)" },
      { id: "D", text: "SBAR (Situation, Background, Assessment, Recommendation)" }
    ],
    correctAnswer: "A",
    explanation: "The PICO framework is the gold-standard methodology for framing clinical foreground questions in evidence-based practice to structure literature searches.",
    incorrectExplanations: {
      B: "SOAP is a documentation format.",
      C: "ADPIE represents nursing process steps.",
      D: "SBAR is a clinical communication handover tool."
    },
    learningObjective: "Apply the PICO framework to formulate evidence-based clinical questions in mental health nursing.",
    reference: "Polit, D. F., & Beck, C. T. (2021). Nursing Research: Generating and Assessing Evidence.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q011",
    module: "11. Advanced Clinical Scenarios",
    topic: "Managing Acute Agitation and De-escalation",
    difficulty: "Advanced",
    questionText: "A patient in the psychiatric emergency unit becomes increasingly agitated, pacing rapidly, and shouting threats at staff. According to evidence-based guidelines for managing acute agitation, what should be the nurse's first-line intervention?",
    options: [
      { id: "A", text: "Immediately administer emergency intramuscular antipsychotics and physical restraints." },
      { id: "B", text: "Initiate verbal de-escalation with a calm, non-threatening demeanor, respectful space, and clear communication." },
      { id: "C", text: "Ignore the behavior so the patient self-soothes in isolation." },
      { id: "D", text: "Challenge the patient's threats assertively to establish immediate staff dominance." }
    ],
    correctAnswer: "B",
    explanation: "Verbal de-escalation is always the first-line, least restrictive intervention for acute agitation before resorting to restraints or chemical sedation.",
    incorrectExplanations: {
      A: "Immediate physical or chemical restraint violates least-restrictive principles.",
      C: "Ignoring acute escalation risks violence.",
      D: "Challenging an agitated patient precipitates aggression."
    },
    learningObjective: "Demonstrate least-restrictive principles in managing acute agitation and crisis de-escalation.",
    reference: "Richmond, J. S., et al. (2012). Verbal De-escalation of the Agitated Patient.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q012",
    module: "12. Leadership and Professional Practice",
    topic: "Clinical Supervision and Reflective Practice",
    difficulty: "Advanced",
    questionText: "What is the primary professional benefit of structured clinical supervision and reflective practice for psychiatric nurses working in high-acuity environments?",
    options: [
      { id: "A", text: "Replacing formal nursing administrative performance appraisals" },
      { id: "B", text: "Enhancing clinical competence, mitigating compassion fatigue, and processing emotional responses to complex patient trauma" },
      { id: "C", text: "Ensuring hospital financial compliance and billing accuracy" },
      { id: "D", text: "Eliminating all legal liability during adverse incident investigations" }
    ],
    correctAnswer: "B",
    explanation: "Clinical supervision provides a safe, reflective space for psychiatric nurses to examine clinical decisions, manage emotional countertransference, and prevent burnout.",
    incorrectExplanations: {
      A: "Supervision is distinct from administrative appraisals.",
      C: "Financial billing is an informatics function.",
      D: "Supervision aids quality improvement but does not absolve professional liability."
    },
    learningObjective: "Value the role of clinical supervision and reflective practice in psychiatric nursing leadership.",
    reference: "Butterworth, T., & Faugier, J. (1992). Clinical Supervision and Mentorship in Nursing.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q013",
    module: "13. Substance Use Disorders and Dual Diagnosis",
    topic: "Alcohol Withdrawal Management and CIWA-Ar",
    difficulty: "Intermediate",
    questionText: "A client admitted for alcohol detoxification begins exhibiting tremors, diaphoresis, tachycardia, and auditory hallucinations on hospital day two. Which nursing action is most appropriate?",
    options: [
      { id: "A", text: "Reassure the client that symptoms are psychological and will resolve without intervention." },
      { id: "B", text: "Administer scheduled or symptom-triggered benzodiazepines per protocol and monitor vital signs closely." },
      { id: "C", text: "Restrict all fluid intake to prevent cerebral edema." },
      { id: "D", text: "Initiate immediate physical seclusion." }
    ],
    correctAnswer: "B",
    explanation: "Alcohol withdrawal can progress rapidly to delirium tremens and seizures. Symptom-triggered or scheduled benzodiazepine protocols combined with close monitoring are standard care.",
    incorrectExplanations: {
      A: "Alcohol withdrawal is a medical emergency.",
      C: "Hydration and electrolyte management are vital.",
      D: "Seclusion is unnecessary unless acute violence occurs."
    },
    learningObjective: "Manage alcohol withdrawal syndromes safely using validated clinical protocols.",
    reference: "Sullivan, J. T., et al. (1989). Assessment of alcohol withdrawal: the CIWA-Ar.",
    contentReviewStatus: "Verified Demo"
  },
  {
    id: "MHN-Q014",
    module: "14. Special Populations and Culturally Relevant Practice",
    topic: "Cultural Formulation and Idioms of Distress",
    difficulty: "Advanced",
    questionText: "A West African patient presents complaining of 'brain fog,' heat rising in the head, and crawling sensations under the skin during periods of intense academic stress. How should the psychiatric nurse culturally contextualize this presentation?",
    options: [
      { id: "A", text: "Dismiss the symptoms as somatic delusions indicative of paranoid schizophrenia." },
      { id: "B", text: "Recognize the expressions as culturally recognized idioms of distress reflecting somatic manifestations of anxiety and stress." },
      { id: "C", text: "Immediately administer high-dose depot antipsychotics." },
      { id: "D", text: "Conclude that the patient is feigning illness to avoid responsibilities." }
    ],
    correctAnswer: "B",
    explanation: "Idioms of distress are culturally specific ways that communities communicate emotional and psychological suffering through physical symptoms. Understanding them prevents misdiagnosis.",
    incorrectExplanations: {
      A: "Labeling cultural idioms as psychotic delusions is a cross-cultural diagnostic error.",
      C: "Antipsychotics are not indicated for cultural somatic stress expressions.",
      D: "Dismissing patient suffering undermines therapeutic trust."
    },
    learningObjective: "Integrate cultural formulations and idioms of distress into psychiatric nursing assessments.",
    reference: "Kleinman, A. (1988). Rethinking Psychiatry.",
    contentReviewStatus: "Verified Demo"
  }
];

// ─── Lazy imports from modular question files (generated per module pair) ────
// These are loaded only once via getAllQuestions().
let _cachedBank: Question[] | null = null;

/**
 * Returns the complete, deduplicated question bank.
 * Combines the 14 seed questions with all generated module question files.
 * Results are cached after the first call.
 */
export function getAllQuestions(): Question[] {
  if (_cachedBank) return _cachedBank;

  // Start with the 14 verified seed questions
  const bank: Question[] = [...INITIAL_QUESTION_BANK];
  const seenIds = new Set(bank.map(q => q.id));
  const seenTexts = new Set(bank.map(q => q.questionText.trim().toLowerCase()));

  /**
   * Safely merge questions from a module file, skipping any duplicates.
   * This guard ensures zero duplication even if module files overlap.
   */
  function mergeQuestions(incoming: Question[]): void {
    for (const q of incoming) {
      const textKey = q.questionText.trim().toLowerCase();
      if (!seenIds.has(q.id) && !seenTexts.has(textKey)) {
        seenIds.add(q.id);
        seenTexts.add(textKey);
        bank.push(q);
      }
    }
  }

  // Merge all modular question banks
  if (Array.isArray(MOD1_2_QUESTIONS)) mergeQuestions(MOD1_2_QUESTIONS);
  if (Array.isArray(MOD3_4_QUESTIONS)) mergeQuestions(MOD3_4_QUESTIONS);
  if (Array.isArray(MOD5_6_QUESTIONS)) mergeQuestions(MOD5_6_QUESTIONS);
  if (Array.isArray(MOD7_8_QUESTIONS)) mergeQuestions(MOD7_8_QUESTIONS);
  if (Array.isArray(MOD9_10_QUESTIONS)) mergeQuestions(MOD9_10_QUESTIONS);
  if (Array.isArray(MOD11_12_QUESTIONS)) mergeQuestions(MOD11_12_QUESTIONS);
  if (Array.isArray(MOD13_14_QUESTIONS)) mergeQuestions(MOD13_14_QUESTIONS);

  _cachedBank = bank;
  return bank;
}

/**
 * Clears the in-memory question cache (call this after adding custom questions
 * so getAllQuestions() returns a fresh list on next invocation).
 */
export function invalidateQuestionCache(): void {
  _cachedBank = null;
}

