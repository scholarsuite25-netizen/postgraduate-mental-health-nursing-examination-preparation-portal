# -*- coding: utf-8 -*-
"""
Module 13: Substance Use Disorders and Dual Diagnosis
Questions MHN-Q1215 to MHN-Q1264 (Topics 1 to 5, 50 questions)
"""

QUESTIONS_T1_T5 = [
    # ---------------------------------------------------------
    # Topic 1: Alcohol Use Disorder (MHN-Q1215 to MHN-Q1224)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1215",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Foundation",
        "questionText": "A 42-year-old client completes the Alcohol Use Disorders Identification Test (AUDIT) during an outpatient health screening and receives a total score of 18. According to World Health Organization (WHO) clinical guidelines, how should the psychiatric nurse interpret this score and what is the recommended clinical action?",
        "options": [
            {"id": "A", "text": "Harmful alcohol use (score 16–19); provide brief intervention, motivational counseling, and close clinical monitoring with consideration for referral."},
            {"id": "B", "text": "Low-risk drinking (score 0–7); provide general alcohol education and encourage continuation of current lifestyle habits."},
            {"id": "C", "text": "Hazardous drinking (score 8–15); provide simple brief advice regarding standard units without further follow-up."},
            {"id": "D", "text": "Definitive alcohol dependence (score 20+); refer immediately for urgent inpatient medical detoxification and intensive residential rehabilitation."}
        ],
        "correctAnswer": "A",
        "explanation": "On the WHO AUDIT tool, scores 0–7 indicate low-risk consumption, 8–15 indicate hazardous alcohol use, 16–19 represent harmful alcohol use (warranting brief intervention, motivational counseling, and close monitoring), and 20–40 suggest alcohol dependence requiring diagnostic evaluation and specialized referral.",
        "incorrectExplanations": {
            "B": "Low-risk drinking corresponds to an AUDIT score of 0 to 7.",
            "C": "Hazardous drinking corresponds to an AUDIT score of 8 to 15.",
            "D": "Alcohol dependence requiring specialized referral is indicated by an AUDIT score of 20 or higher."
        },
        "learningObjective": "Interpret AUDIT screening scores accurately to determine evidence-based clinical interventions.",
        "reference": "Babor, T. F., et al. (2001). AUDIT: The Alcohol Use Disorders Identification Test: Guidelines for Use in Primary Care (2nd ed.). World Health Organization.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1216",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Foundation",
        "questionText": "During a comprehensive psychiatric assessment, a 36-year-old client reports experiencing 5 of the 11 DSM-5 diagnostic criteria for Alcohol Use Disorder over the preceding 12 months, including tolerance, withdrawal symptoms, persistent desire to cut down, cravings, and giving up important social activities. How should the mental health nurse categorize the severity of this client's condition?",
        "options": [
            {"id": "A", "text": "Mild Alcohol Use Disorder"},
            {"id": "B", "text": "Moderate Alcohol Use Disorder"},
            {"id": "C", "text": "Severe Alcohol Use Disorder"},
            {"id": "D", "text": "Subclinical Alcohol Misuse"}
        ],
        "correctAnswer": "B",
        "explanation": "According to DSM-5 criteria, Alcohol Use Disorder severity is based on the number of symptom criteria met within a 12-month period: 2–3 criteria indicate Mild, 4–5 criteria indicate Moderate, and 6 or more criteria indicate Severe Alcohol Use Disorder. Meeting 5 criteria classifies the condition as Moderate.",
        "incorrectExplanations": {
            "A": "Mild AUD is defined by the presence of 2 to 3 diagnostic criteria.",
            "C": "Severe AUD is defined by the presence of 6 or more diagnostic criteria.",
            "D": "Subclinical misuse refers to individuals meeting 0 or 1 criterion, which does not satisfy the diagnostic threshold."
        },
        "learningObjective": "Apply DSM-5 diagnostic severity thresholds for Alcohol Use Disorder.",
        "reference": "American Psychiatric Association. (2022). Diagnostic and Statistical Manual of Mental Disorders (5th ed., text rev.; DSM-5-TR).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1217",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Foundation",
        "questionText": "A mental health nurse is implementing a brief motivational intervention for alcohol reduction using the evidence-based FRAMES model. Which of the following components correctly matches the 'M' in this acronym?",
        "options": [
            {"id": "A", "text": "Mandatory abstinence guidelines"},
            {"id": "B", "text": "Medical detoxification protocol"},
            {"id": "C", "text": "Menu of alternative options and strategies for change"},
            {"id": "D", "text": "Monitoring of biological liver function markers"}
        ],
        "correctAnswer": "C",
        "explanation": "The FRAMES model stands for Feedback on personal risk, Responsibility of the individual for change, Advice to change, Menu of alternative options and strategies, Empathy in therapeutic style, and Self-efficacy enhancement. Providing a menu of options supports client autonomy in selecting feasible change strategies.",
        "incorrectExplanations": {
            "A": "Mandatory abstinence contradicts the person-centered, collaborative nature of FRAMES.",
            "B": "Medical detoxification is a clinical treatment phase, not an element of the FRAMES brief intervention acronym.",
            "D": "Biological monitoring may be clinical practice, but it is not what 'M' represents in the FRAMES model."
        },
        "learningObjective": "Identify the key components of the FRAMES model for brief alcohol interventions.",
        "reference": "Bien, T. H., Miller, W. R., & Tonigan, J. S. (1993). Brief interventions for alcohol problems: a review. Addiction, 88(3), 315-335.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1218",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A 48-year-old client with chronic alcohol dependence has achieved initial detoxification and is prescribed acamprosate (Campral) 666 mg three times daily to support abstinence maintenance. Which baseline laboratory assessment is essential before initiating acamprosate, and why?",
        "options": [
            {"id": "A", "text": "Serum amylase and lipase, because acamprosate carries a high risk of acute necrotizing pancreatitis."},
            {"id": "B", "text": "Thyroid-stimulating hormone (TSH), because acamprosate causes direct suppression of thyroxine synthesis."},
            {"id": "C", "text": "Electrocardiogram (ECG) for QTc prolongation, because acamprosate inhibits cardiac potassium ion channels."},
            {"id": "D", "text": "Serum creatinine and estimated glomerular filtration rate (eGFR), because acamprosate is excreted unchanged by the kidneys and is contraindicated in severe renal impairment."}
        ],
        "correctAnswer": "D",
        "explanation": "Acamprosate modulates glutamatergic NMDA transmission and is eliminated almost exclusively unchanged by the kidneys. It does not undergo hepatic metabolism. Therefore, renal function (creatinine and eGFR) must be evaluated: dosage adjustment is required in moderate renal impairment (eGFR 30–50 mL/min), and it is contraindicated in severe renal impairment (eGFR < 30 mL/min).",
        "incorrectExplanations": {
            "A": "Acamprosate does not carry a prominent risk of acute pancreatitis; pancreatitis is more commonly related to chronic alcohol use itself.",
            "B": "Acamprosate has no known mechanism of thyroid suppression.",
            "C": "Acamprosate does not prolong cardiac QTc intervals, unlike methadone or certain psychotropics."
        },
        "learningObjective": "Formulate safe prescribing and monitoring practices for acamprosate in relapse prevention.",
        "reference": "NICE. (2011). Alcohol-use disorders: diagnosis, assessment and management of harmful drinking and alcohol dependence (CG115). National Institute for Health and Care Excellence.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1219",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A 50-year-old client enrolled in an alcohol relapse prevention program is taking naltrexone 50 mg daily. The client is scheduled for an elective laparoscopic cholecystectomy in 5 days. What crucial clinical instruction must the psychiatric liaison nurse communicate to the surgical team and client?",
        "options": [
            {"id": "A", "text": "Discontinue naltrexone at least 48 to 72 hours before surgery, because as an opioid receptor antagonist, it will block the analgesic efficacy of opioid medications administered perioperatively."},
            {"id": "B", "text": "Double the dose of naltrexone prior to surgery to prevent stress-induced alcohol cravings in the hospital."},
            {"id": "C", "text": "Switch immediately to disulfiram 250 mg daily to ensure alcohol abstinence remains covered throughout hospitalization."},
            {"id": "D", "text": "Administer high-dose naloxone alongside general anesthesia to prevent severe naltrexone withdrawal."}
        ],
        "correctAnswer": "A",
        "explanation": "Naltrexone is a competitive mu-opioid receptor antagonist that binds with high affinity to opioid receptors. If taken perioperatively, it blocks opioid analgesia, potentially leading to uncontrollable pain or dangerous opioid over-titration. It should be withheld for at least 48–72 hours prior to elective procedures requiring opioid analgesics.",
        "incorrectExplanations": {
            "B": "Doubling naltrexone would exacerbate opioid blockade and cause severe perioperative pain management failure.",
            "C": "Disulfiram before surgery risks hazardous interactions with surgical skin preps containing alcohol and offers no analgesic benefit.",
            "D": "Naloxone is an opioid antagonist, not an agonist, and would not treat naltrexone cessation; naltrexone cessation does not cause physical opioid withdrawal in the absence of opioids."
        },
        "learningObjective": "Demonstrate understanding of the pharmacological mechanism and perioperative precautions for naltrexone.",
        "reference": "Substance Abuse and Mental Health Services Administration (SAMHSA). (2020). Medication for the Treatment of Alcohol Use Disorder: A Review of the Evidence. Treatment Improvement Protocol (TIP) 49.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1220",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A client initiated on disulfiram (Antabuse) 200 mg daily for alcohol use disorder asks the nurse about dietary and over-the-counter restrictions. Which counseling statement provided by the psychiatric nurse reflects accurate pharmacological education?",
        "options": [
            {"id": "A", "text": "You can safely consume food cooked with wine or beer because boiling eliminates all alcohol chemical structures."},
            {"id": "B", "text": "You must strictly avoid hidden alcohol sources, including mouthwashes, cough elixirs, vinegar-based sauces, and alcohol-based rub-in hand sanitizers, as they can trigger a severe acetaldehyde reaction."},
            {"id": "C", "text": "If you inadvertently drink alcohol, you should immediately take an extra disulfiram tablet to neutralize the toxic byproduct."},
            {"id": "D", "text": "Disulfiram becomes completely inactive 12 hours after your last tablet, so social drinking may resume the following day."}
        ],
        "correctAnswer": "B",
        "explanation": "Disulfiram irreversibly inhibits aldehyde dehydrogenase, causing an accumulation of toxic acetaldehyde if even trace ethanol is absorbed. The resulting disulfiram-ethanol reaction causes flushing, throbbing headache, palpitations, nausea, vomiting, and potentially life-threatening hypotension. Hidden sources such as elixirs, mouthwashes, and cooking sauces must be avoided. The enzyme inhibition persists for up to 14 days after discontinuation.",
        "incorrectExplanations": {
            "A": "Cooking does not completely remove alcohol; residual ethanol can precipitate a severe disulfiram reaction.",
            "C": "Taking additional disulfiram during alcohol exposure will dramatically worsen the toxic acetaldehyde accumulation.",
            "D": "Disulfiram causes irreversible enzyme inhibition; resynthesis of aldehyde dehydrogenase takes up to 1 to 2 weeks after stopping the medication."
        },
        "learningObjective": "Educate clients on safety precautions and pharmacological interactions associated with disulfiram therapy.",
        "reference": "Kranzler, H. R., & Soyka, M. (2018). Diagnosis and pharmacotherapy of alcohol use disorder: a review. JAMA, 320(8), 815-824.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1221",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "In reviewing routine laboratory markers for a client suspected of undisclosed heavy, chronic alcohol consumption, which pattern of hematological and hepatic parameters is most characteristic of chronic alcohol misuse?",
        "options": [
            {"id": "A", "text": "Microcytic anemia, elevated ALT with an AST:ALT ratio < 0.5, and decreased serum ferritin."},
            {"id": "B", "text": "Normal mean corpuscular volume (MCV), isolated severe hyperbilirubinemia, and thrombocytopenia without enzyme elevation."},
            {"id": "C", "text": "Macrocytosis (elevated MCV), elevated gamma-glutamyl transferase (GGT), elevated carbohydrate-deficient transferrin (CDT), and an AST:ALT ratio greater than 2:1."},
            {"id": "D", "text": "Marked leukopenia, suppressed GGT, elevated alkaline phosphatase, and normal erythrocyte volume."}
        ],
        "correctAnswer": "C",
        "explanation": "Chronic heavy alcohol consumption induces hepatic microsomal GGT, alters erythrocyte membrane lipids causing non-megaloblastic macrocytosis (elevated MCV), increases carbohydrate-deficient transferrin (CDT, a highly specific biomarker of heavy intake), and typically displays an AST:ALT ratio greater than 2:1 due to pyridoxal-5'-phosphate deficiency and mitochondrial AST release.",
        "incorrectExplanations": {
            "A": "An AST:ALT ratio < 1 is typical of non-alcoholic fatty liver disease (NAFLD) or viral hepatitis, not alcoholic liver injury.",
            "B": "Chronic heavy alcohol intake typically elevates MCV and hepatic transaminases rather than presenting as isolated hyperbilirubinemia.",
            "D": "GGT is typically elevated, not suppressed, by chronic alcohol intake."
        },
        "learningObjective": "Analyze laboratory biomarkers to identify biological indicators of chronic alcohol misuse.",
        "reference": "Lieber, C. S. (2004). Relationships between nutrition, alcohol use, and liver disease. Alcohol Research & Health, 27(3), 220-231.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1222",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A client with a past history of severe alcohol use disorder has remained completely abstinent from alcohol for 14 consecutive months. However, the client reports experiencing occasional strong psychological cravings when passing a favorite tavern. Under DSM-5-TR diagnostic criteria, how should this client's current diagnostic status be specified?",
        "options": [
            {"id": "A", "text": "In partial remission, because persistent cravings disqualify the client from any formal remission status."},
            {"id": "B", "text": "In early remission, because the client has not yet reached the 24-month benchmark required for sustained recovery."},
            {"id": "C", "text": "Alcohol Use Disorder, fully resolved with complete cure."},
            {"id": "D", "text": "In sustained remission, because none of the criteria for Alcohol Use Disorder (with the explicit exception of craving) have been met for 12 months or longer."}
        ],
        "correctAnswer": "D",
        "explanation": "Under DSM-5-TR, 'In early remission' is specified when none of the criteria have been met for at least 3 months but less than 12 months. 'In sustained remission' is specified when none of the criteria have been met at any time for 12 months or longer (with the explicit exception of Criterion 4: craving, which may still be present).",
        "incorrectExplanations": {
            "A": "The DSM-5-TR diagnostic criteria explicitly allow Criterion 4 (craving or a strong desire or urge to use) to persist without negating sustained remission status.",
            "B": "Sustained remission requires 12 months, not 24 months, of meeting no criteria except craving.",
            "C": "Substance use disorders are classified as in remission rather than 'cured', reflecting chronic relapse risk."
        },
        "learningObjective": "Apply DSM-5-TR remission specifiers accurately in clinical substance use documentation.",
        "reference": "American Psychiatric Association. (2022). Diagnostic and Statistical Manual of Mental Disorders (5th ed., text rev.; DSM-5-TR).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1223",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A 58-year-old male with a 30-year history of alcohol dependence is admitted to the psychiatric rehabilitation unit. On mental status examination, he is alert and cooperative with intact immediate recall of 3 objects, but 5 minutes later he cannot recall any objects. When asked about his morning activities, he vividly describes attending a lavish wedding banquet that never occurred. Which neurocognitive condition and phenomenon are demonstrated?",
        "options": [
            {"id": "A", "text": "Korsakoff's syndrome demonstrating anterograde amnesia and confabulation."},
            {"id": "B", "text": "Alzheimer's disease demonstrating retrograde semantic aphasia and visual agnosia."},
            {"id": "C", "text": "Delirium tremens demonstrating acute fluctuating clouding of consciousness."},
            {"id": "D", "text": "Frontotemporal dementia demonstrating executive disinhibition and hyperorality."}
        ],
        "correctAnswer": "A",
        "explanation": "Korsakoff's syndrome (alcohol-induced major neurocognitive disorder, amnestic-confabulatory type) is caused by chronic thiamine deficiency resulting in damage to the mammillary bodies and dorsomedial thalamic nuclei. Its hallmark is severe anterograde amnesia (inability to form new declarative memories) accompanied by confabulation (fabricating plausible memories without conscious intent to deceive) with preserved immediate recall and general alertness.",
        "incorrectExplanations": {
            "B": "The clinical picture shows preserved immediate registration but profound anterograde retrieval failure and classic confabulation characteristic of Korsakoff's, not typical primary Alzheimer's presentation.",
            "C": "Delirium tremens is an acute medical emergency marked by fluctuating sensorium, marked autonomic instability, and hallucinations, which are absent here.",
            "D": "Frontotemporal dementia presents primarily with early personality deterioration, apathy, or primary progressive language disturbance rather than isolated amnestic-confabulatory syndrome."
        },
        "learningObjective": "Distinguish the clinical and neuropsychiatric features of Korsakoff's syndrome from other neurocognitive disorders.",
        "reference": "Victor, M., Adams, R. D., & Collins, G. H. (1989). The Wernicke-Korsakoff Syndrome and Related Neurologic Disorders Due to Alcoholism and Malnutrition (2nd ed.). F. A. Davis.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1224",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Expert",
        "questionText": "A 52-year-old executive is seen in the psychiatric liaison clinic following an acute alcohol-related admission. Her AUDIT score is 17. When applying the 'Feedback' stage of the FRAMES model, which therapeutic verbalization by the psychiatric nurse best exemplifies evidence-based brief motivational engagement?",
        "options": [
            {"id": "A", "text": "'Your AUDIT score of 17 proves you are an alcoholic, and unless you stop completely today, you will lose your executive job.'"},
            {"id": "B", "text": "'Based on the assessment tool you completed, your score of 17 places your drinking in the harmful category compared to general population benchmarks, which increases your risk for hypertension and liver inflammation. How do you feel about these results?'"},
            {"id": "C", "text": "'You are drinking far more than any responsible professional should, so I have booked you into an inpatient facility starting tonight.'"},
            {"id": "D", "text": "'Your score indicates you can continue drinking as you are, provided you switch from spirits to lower-strength wine.'"}
        ],
        "correctAnswer": "B",
        "explanation": "In the FRAMES approach, Feedback (F) must be delivered objectively, non-judgmentally, and personalized against normative data, followed by eliciting the client's perspective to foster intrinsic motivation. Option B provides factual feedback regarding the score (harmful category), connects it to biological health risks, and immediately invites the client's personal reflection without labeling or coercion.",
        "incorrectExplanations": {
            "A": "Confrontational labeling ('you are an alcoholic') and threats increase defensiveness and violate motivational interviewing principles.",
            "C": "Imposing mandatory admission without exploring readiness violates the principles of personal responsibility and autonomy.",
            "D": "Minimizing harmful drinking provides medically inaccurate reassurance and fails to address identified health risks."
        },
        "learningObjective": "Demonstrate the clinical application of non-confrontational Feedback delivery within the FRAMES brief intervention protocol.",
        "reference": "Miller, W. R., & Rollnick, S. (2012). Motivational Interviewing: Helping People Change (3rd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # ---------------------------------------------------------
    # Topic 2: Alcohol Withdrawal Syndrome (MHN-Q1225 to MHN-Q1234)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1225",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Withdrawal Syndrome",
        "difficulty": "Foundation",
        "questionText": "A 45-year-old male with chronic alcohol dependence is admitted to the acute psychiatric inpatient unit. His last alcoholic drink was approximately 12 hours ago. On physical examination, the psychiatric nurse notes coarse hand tremors, marked diaphoresis, nausea, mild psychomotor agitation, and a resting heart rate of 110 bpm. Based on the neurobiology and timeline of alcohol withdrawal, which stage is this client displaying?",
        "options": [
            {"id": "A", "text": "Post-acute protracted withdrawal syndrome"},
            {"id": "B", "text": "Late-stage delirium tremens"},
            {"id": "C", "text": "Early uncomplicated alcohol withdrawal (autonomic hyperactivity)"},
            {"id": "D", "text": "Alcohol-induced persisting amnestic syndrome"}
        ],
        "correctAnswer": "C",
        "explanation": "The early stage of alcohol withdrawal typically begins within 6 to 24 hours of alcohol cessation or significant reduction. It is characterized by autonomic hyperactivity: coarse tremors, tachycardia, diaphoresis, hypertension, nausea/vomiting, insomnia, and psychomotor agitation due to acute GABA-A hypoactivity and rebound NMDA/glutamate hyperarousal.",
        "incorrectExplanations": {
            "A": "Protracted withdrawal refers to subacute sleep and affective disturbances lasting months after acute withdrawal.",
            "B": "Delirium tremens typically peaks between 48 and 72 to 96 hours post-cessation and is marked by global disorientation and delirium.",
            "D": "Alcohol-induced persisting amnestic disorder (Korsakoff's) involves chronic memory loss, not acute autonomic instability."
        },
        "learningObjective": "Identify the characteristic timeline and clinical manifestations of early alcohol withdrawal syndrome.",
        "reference": "Schuckit, M. A. (2014). Recognition and management of withdrawal delirium (delirium tremens). New England Journal of Medicine, 371(22), 2109-2117.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1226",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Withdrawal Syndrome",
        "difficulty": "Foundation",
        "questionText": "Approximately 36 hours after his last drink, an inpatient client undergoing unmonitored alcohol detoxification experiences two consecutive generalized tonic-clonic seizures. What is the evidence-based emergency pharmacological intervention for alcohol withdrawal seizures?",
        "options": [
            {"id": "A", "text": "Initiating a maintenance infusion of intravenous phenytoin (Dilantin)."},
            {"id": "B", "text": "Oral levetiracetam (Keppra) 1000 mg twice daily."},
            {"id": "C", "text": "Immediate administration of intramuscular haloperidol 5 mg."},
            {"id": "D", "text": "Immediate administration of intravenous or intramuscular benzodiazepines (such as diazepam or lorazepam)."}
        ],
        "correctAnswer": "D",
        "explanation": "Alcohol withdrawal seizures are caused by abrupt loss of GABA-A receptor stimulation combined with severe glutamatergic rebound excitability. Benzodiazepines (e.g., diazepam, lorazepam) enhance GABA-A receptor opening frequency, directly treating the underlying neurochemical cause. Phenytoin is ineffective for the prevention or treatment of alcohol withdrawal seizures.",
        "incorrectExplanations": {
            "A": "Phenytoin has been proven ineffective in preventing or treating alcohol withdrawal seizures because it acts on sodium channels, not the GABA/glutamate imbalance.",
            "B": "Oral levetiracetam is not first-line emergency management for acute alcohol withdrawal seizures.",
            "C": "Haloperidol lowers the seizure threshold and is strictly contraindicated as monotherapy for alcohol withdrawal seizures."
        },
        "learningObjective": "Select the correct first-line pharmacological treatment for acute alcohol withdrawal seizures.",
        "reference": "NICE. (2010). Alcohol-use disorders: diagnosis and clinical management of alcohol-related physical complications (CG100).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1227",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Withdrawal Syndrome",
        "difficulty": "Foundation",
        "questionText": "A 54-year-old client admitted to the psychiatric ward 68 hours ago becomes acutely disoriented to time and place, picks imaginary insects off the bedsheets, and exhibits severe pyrexia (temperature 38.9°C), marked hypertension (175/105 mmHg), and diaphoresis. Which life-threatening condition is this client manifesting?",
        "options": [
            {"id": "A", "text": "Delirium Tremens (DTs)"},
            {"id": "B", "text": "Wernicke's Encephalopathy"},
            {"id": "C", "text": "Neuroleptic Malignant Syndrome"},
            {"id": "D", "text": "Alcoholic Hallucinosis with clear sensorium"}
        ],
        "correctAnswer": "A",
        "explanation": "Delirium tremens (DTs) is a severe, life-threatening manifestation of alcohol withdrawal that characteristically emerges 48 to 72–96 hours after cessation. It is defined by clouding of consciousness (delirium), fluctuating disorientation, vivid visual/tactile hallucinations (zoopsia), profound autonomic instability (hyperthermia, severe tachycardia, hypertension), and carries significant mortality if untreated.",
        "incorrectExplanations": {
            "B": "Wernicke's encephalopathy presents with the classic triad of ataxia, ophthalmoplegia/nystagmus, and confusion, without florid autonomic hyperactivity.",
            "C": "Neuroleptic malignant syndrome is triggered by dopamine antagonists and is characterized by 'lead-pipe' rigidity, high CK, and hyperthermia.",
            "D": "Alcoholic hallucinosis occurs earlier (12–48 hours) and is distinguished by vivid hallucinations in the presence of a completely clear, oriented sensorium and normal vital signs."
        },
        "learningObjective": "Differentiate Delirium Tremens from other neuropsychiatric emergencies based on clinical timeline and features.",
        "reference": "Schuckit, M. A. (2014). Recognition and management of withdrawal delirium (delirium tremens). New England Journal of Medicine, 371(22), 2109-2117.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1228",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Withdrawal Syndrome",
        "difficulty": "Intermediate",
        "questionText": "A psychiatric nurse assesses an acute alcohol withdrawal client using the Clinical Institute Withdrawal Assessment for Alcohol, revised (CIWA-Ar) scale and calculates a score of 18. What clinical protocol action is indicated based on this score?",
        "options": [
            {"id": "A", "text": "Withhold all benzodiazepines and continue supportive monitoring only, as medical treatment is only indicated for scores > 30."},
            {"id": "B", "text": "Administer symptom-triggered benzodiazepines promptly according to medical protocol, provide supportive nursing care, and repeat CIWA-Ar assessment in 1 to 2 hours."},
            {"id": "C", "text": "Discharge the client to outpatient care because a score of 18 indicates that withdrawal has successfully resolved."},
            {"id": "D", "text": "Immediately administer flumazenil intravenously to reverse benzodiazepine receptor sensitivity."}
        ],
        "correctAnswer": "B",
        "explanation": "On the CIWA-Ar scale (maximum score 67), scores < 10 indicate mild withdrawal not requiring pharmacological intervention; scores 10 to 15 reflect moderate withdrawal requiring oral benzodiazepines; scores > 15 indicate severe withdrawal requiring prompt symptom-triggered benzodiazepines and intensive monitoring to avert seizures and delirium tremens.",
        "incorrectExplanations": {
            "A": "Scores >= 10 warrant pharmacological intervention; withholding medication at a score of 18 exposes the client to seizure and DT risk.",
            "C": "A score of 18 reflects severe withdrawal, which is unsafe for outpatient discharge.",
            "D": "Flumazenil is a benzodiazepine antagonist that precipitates acute seizures and is contraindicated."
        },
        "learningObjective": "Apply CIWA-Ar score cutoffs to guide safe benzodiazepine administration in alcohol withdrawal.",
        "reference": "Sullivan, J. T., et al. (1989). Assessment of alcohol withdrawal: the revised Clinical Institute Withdrawal Assessment for Alcohol scale (CIWA-Ar). British Journal of Addiction, 84(11), 1353-1357.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1229",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Withdrawal Syndrome",
        "difficulty": "Intermediate",
        "questionText": "When comparing symptom-triggered benzodiazepine dosing protocols to traditional fixed-schedule regimens for inpatient alcohol detoxification, which clinical advantage is consistently supported by psychiatric nursing evidence?",
        "options": [
            {"id": "A", "text": "Symptom-triggered protocols eliminate the need for objective nursing clinical assessment."},
            {"id": "B", "text": "Fixed-schedule regimens completely prevent the development of tolerance to benzodiazepines."},
            {"id": "C", "text": "Symptom-triggered protocols significantly reduce the total duration of treatment and total cumulative benzodiazepine dosage while achieving equivalent efficacy and safety."},
            {"id": "D", "text": "Fixed-schedule protocols eliminate any requirement for vital signs monitoring."}
        ],
        "correctAnswer": "C",
        "explanation": "Evidence-based trials demonstrate that symptom-triggered benzodiazepine administration (dosing only when CIWA-Ar >= 10 or >= 12) results in significantly shorter detoxification duration (e.g., median 9 hours vs 68 hours) and lower cumulative benzodiazepine consumption compared to rigid fixed-dose tapering schedules, while maintaining equivalent prevention of seizures and delirium.",
        "incorrectExplanations": {
            "A": "Symptom-triggered regimens require frequent, meticulous clinical assessments using standardized tools like CIWA-Ar.",
            "B": "Fixed-schedule regimens often over-medicate clients, increasing over-sedation and dependence risks.",
            "D": "Regular vital signs and clinical monitoring remain mandatory in all withdrawal management protocols."
        },
        "learningObjective": "Compare symptom-triggered and fixed-dose benzodiazepine regimens in alcohol withdrawal management.",
        "reference": "Daeppen, J. B., et al. (2002). Symptom-triggered vs fixed-schedule doses of benzodiazepine for alcohol withdrawal: a randomized treatment trial. Archives of Internal Medicine, 162(10), 1117-1121.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1230",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Withdrawal Syndrome",
        "difficulty": "Intermediate",
        "questionText": "A 61-year-old client with decompensated alcoholic cirrhosis (Child-Pugh Class B) and jaundice is admitted for alcohol withdrawal. Why does the multi-disciplinary team select oral lorazepam rather than chlordiazepoxide or diazepam for withdrawal management?",
        "options": [
            {"id": "A", "text": "Lorazepam is excreted entirely by alveolar exhalation, bypassing internal organs."},
            {"id": "B", "text": "Chlordiazepoxide is an opioid agonist that causes acute hepatic encephalopathy."},
            {"id": "C", "text": "Diazepam cannot cross the blood-brain barrier in patients with elevated bilirubin."},
            {"id": "D", "text": "Lorazepam undergoes direct glucuronidation without active hepatic oxidative metabolites, preventing drug accumulation and hepatic encephalopathy in severe liver impairment."}
        ],
        "correctAnswer": "D",
        "explanation": "Chlordiazepoxide and diazepam undergo extensive Phase I hepatic oxidation (cytochrome P450) and produce long-acting active metabolites (such as desmethyldiazepam) that accumulate in cirrhotic liver disease, precipitating prolonged sedation and hepatic coma. Lorazepam and oxazepam undergo direct Phase II glucuronidation without active metabolites, making them the preferred benzodiazepines in hepatic impairment.",
        "incorrectExplanations": {
            "A": "Lorazepam is not eliminated via exhalation; it is glucuronidated in the liver and excreted by the kidneys.",
            "B": "Chlordiazepoxide is a benzodiazepine, not an opioid agonist.",
            "C": "Diazepam crosses the blood-brain barrier readily regardless of bilirubin levels."
        },
        "learningObjective": "Select appropriate benzodiazepines based on hepatic metabolic pathways in clients with liver disease.",
        "reference": "NICE. (2010). Alcohol-use disorders: diagnosis and clinical management of alcohol-related physical complications (CG100).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1231",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Withdrawal Syndrome",
        "difficulty": "Advanced",
        "questionText": "An emaciated client with chronic alcohol dependence arrives at the emergency department in a state of acute withdrawal. The junior doctor orders an immediate intravenous infusion of 5% Dextrose in water (D5W) for hypoglycemia and dehydration, alongside intramuscular thiamine (Pabrinex). Which clinical action must the psychiatric nurse enforce prior to starting the dextrose infusion?",
        "options": [
            {"id": "A", "text": "Administer high-potency parenteral thiamine before or simultaneously with the intravenous dextrose, because glucose infusion alone can rapidly exhaust marginal thiamine stores and precipitate acute Wernicke's encephalopathy."},
            {"id": "B", "text": "Withhold all thiamine until the blood glucose level reaches exactly 15 mmol/L."},
            {"id": "C", "text": "Infuse the dextrose over 2 minutes as a rapid bolus before checking vital signs."},
            {"id": "D", "text": "Administer oral disulfiram immediately to block glucose metabolism."}
        ],
        "correctAnswer": "A",
        "explanation": "Thiamine (vitamin B1) is an essential cofactor for the pyruvate dehydrogenase complex and alpha-ketoglutarate dehydrogenase in the Krebs cycle and transketolase in the pentose phosphate pathway. Infusing glucose without adequate thiamine increases carbohydrate metabolic load, rapidly consuming depleted thiamine reserves and precipitating acute, potentially irreversible Wernicke's encephalopathy or fatal central pontine myelinolysis.",
        "incorrectExplanations": {
            "B": "Withholding thiamine until glucose rises exacerbates neurotoxic cellular energy failure.",
            "C": "Rapid bolus of D5W without thiamine increases brain swelling and acute encephalopathy risk.",
            "D": "Disulfiram plays no role in glucose metabolism and is contraindicated in acute withdrawal."
        },
        "learningObjective": "Explain the biological imperative for administering parenteral thiamine prior to carbohydrate infusions in chronic alcohol misuse.",
        "reference": "Thomson, A. D., et al. (2002). The Royal College of Physicians report on alcohol: guidelines for managing Wernicke's encephalopathy in the accident and Emergency Department. Alcohol and Alcoholism, 37(6), 513-521.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1232",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Withdrawal Syndrome",
        "difficulty": "Advanced",
        "questionText": "During a physical assessment of a client admitted for acute alcohol withdrawal, the psychiatric nurse observes horizontal nystagmus, bilateral lateral rectus palsy (sixth cranial nerve impairment), wide-based ataxic gait, and an acute confusional state. What clinical syndrome does this constellation of signs indicate?",
        "options": [
            {"id": "A", "text": "Parkinson's disease tremor crisis"},
            {"id": "B", "text": "Acute Wernicke's Encephalopathy"},
            {"id": "C", "text": "Normal pressure hydrocephalus"},
            {"id": "D", "text": "Guillain-Barré syndrome"}
        ],
        "correctAnswer": "B",
        "explanation": "The classic clinical triad of acute Wernicke's encephalopathy consists of: (1) encephalopathy/acute confusional state, (2) oculomotor dysfunction (most commonly bilateral horizontal nystagmus and abducens nerve/lateral rectus palsy), and (3) gait ataxia resulting from vestibular and cerebellar vermis dysfunction. Prompt high-dose parenteral thiamine is required to reverse ophthalmoplegia and prevent death or chronic Korsakoff's syndrome.",
        "incorrectExplanations": {
            "A": "Parkinson's disease presents with resting pill-rolling tremor, cogwheel rigidity, and bradykinesia, not acute ophthalmoplegia.",
            "C": "Normal pressure hydrocephalus presents with insidious gait disturbance, urinary incontinence, and progressive cognitive decline.",
            "D": "Guillain-Barré syndrome is an ascending post-infectious demyelinating polyneuropathy without acute encephalopathy and cranial nerve VI palsy as the primary presentation."
        },
        "learningObjective": "Recognize the classic clinical diagnostic triad of acute Wernicke's encephalopathy.",
        "reference": "Galvin, R., et al. (2010). EFNS guidelines for diagnosis, prevention and treatment of Wernicke's encephalopathy. European Journal of Neurology, 17(12), 1408-1418.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1233",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Use Disorder",
        "difficulty": "Advanced",
        "questionText": "A 56-year-old client with chronic alcohol-related neurocognitive impairment consistently confabulates when answering questions regarding his personal history. When asked what he had for lunch, he insists he dined at a five-star restaurant with the Prime Minister, despite remaining in the hospital ward all day. What is the neuropsychological basis of confabulation in Korsakoff's syndrome?",
        "options": [
            {"id": "A", "text": "Deliberate and conscious fabrication designed to deceive healthcare professionals for secondary financial gain."},
            {"id": "B", "text": "Auditory command hallucinations telling the client to recite false memories."},
            {"id": "C", "text": "Unconscious generation of fabricated or misremembered memories to fill in severe gaps in recall, occurring without intent to deceive due to frontal-diencephalic memory retrieval dysfunction."},
            {"id": "D", "text": "Transient ischemic attacks in the left temporal language cortex."}
        ],
        "correctAnswer": "C",
        "explanation": "Confabulation in Korsakoff's syndrome is an involuntary, non-deliberate production of fabricated, distorted, or misinterpreted memories about oneself or the world. It occurs because the patient has dense anterograde and patchy retrograde amnesia combined with frontal executive dysfunction, leading to failure of reality monitoring and temporal sequencing without any conscious intent to lie.",
        "incorrectExplanations": {
            "A": "Confabulation is distinct from malingering; the patient genuinely believes the fabricated memories are authentic.",
            "B": "Confabulation is a memory retrieval and monitoring deficit, not an auditory hallucination.",
            "D": "Korsakoff's syndrome involves bilateral mammillary body and thalamic lesions from thiamine deficiency, not transient ischemic attacks."
        },
        "learningObjective": "Analyze the neuropsychological mechanisms distinguishing confabulation from intentional deceit or psychotic symptoms.",
        "reference": "Kopelman, M. D. (1987). Two types of confabulation. Journal of the Royal Society of Medicine, 80(7), 430-433.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1234",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Alcohol Withdrawal Syndrome",
        "difficulty": "Expert",
        "questionText": "In managing a client experiencing severe alcohol withdrawal with perceptual distortions and extreme autonomic instability in an inpatient psychiatric setting, which environmental and nursing milieu intervention is most effective in minimizing delirium progression and preventing sensory misperceptions?",
        "options": [
            {"id": "A", "text": "Complete sensory deprivation: place the client in a pitch-black, silent seclusion room with no personal interaction."},
            {"id": "B", "text": "Expose the client to continuous loud radio broadcasts to maintain active cognitive orientation."},
            {"id": "C", "text": "Keep all window blinds open at night so street headlights can stimulate retinal pathways."},
            {"id": "D", "text": "Provide a well-lit, quiet, low-stimulus room, maintain regular orientation cues and 1-to-1 calm nursing presence, avoid dark shadows, and correct electrolyte abnormalities (particularly magnesium and potassium)."}
        ],
        "correctAnswer": "D",
        "explanation": "Sensory misperceptions (illusions) in alcohol withdrawal are exacerbated by ambiguous sensory stimuli, dim lighting, and shadows, which the brain misinterprets as frightening objects or animals. A well-lit, quiet room minimizes illusions, while consistent 1-to-1 reassurance promotes psychological grounding. Correcting hypomagnesemia and hypokalemia is crucial because magnesium is a necessary cofactor for thiamine utilization and prevents cardiac arrhythmias.",
        "incorrectExplanations": {
            "A": "Total darkness and sensory deprivation increase visual hallucinations, disorientation, and panic in delirium.",
            "B": "Loud, erratic audio stimulation causes cognitive sensory overload and worsens autonomic agitation.",
            "C": "Flickering lights and moving street shadows create visual illusions (e.g., seeing intruders or insects)."
        },
        "learningObjective": "Design a therapeutic physical and psychological environment to mitigate sensory illusions in severe alcohol withdrawal.",
        "reference": "Inouye, S. K., et al. (2014). Delirium in elderly people. The Lancet, 383(9920), 911-922.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # ---------------------------------------------------------
    # Topic 3: Opioid Use Disorder (MHN-Q1235 to MHN-Q1244)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1235",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Foundation",
        "questionText": "A 29-year-old client seeking treatment for heroin dependence is evaluated in the community addiction clinic using the Clinical Opiate Withdrawal Scale (COWS). The nurse documents resting pulse 108 bpm, intense piloerection ('gooseflesh'), rhinorrhea, lacrimation, dilated pupils (mydriasis), severe joint aches, and restlessness. Which physiological sign evaluated on COWS definitively differentiates opioid withdrawal from sedative-hypnotic or alcohol withdrawal?",
        "options": [
            {"id": "A", "text": "Pupillary dilation (mydriasis) and piloerection, which are classic signs of opioid withdrawal rather than sedative withdrawal."},
            {"id": "B", "text": "Tachycardia, which is uniquely exclusive to opioid withdrawal."},
            {"id": "C", "text": "Tremulousness, which never occurs in opioid withdrawal."},
            {"id": "D", "text": "Diaphoresis, which only occurs in opioid withdrawal."}
        ],
        "correctAnswer": "A",
        "explanation": "Pupillary dilation (mydriasis), piloerection ('cold turkey' gooseflesh), rhinorrhea, lacrimation, and yawning are classic sympathetic rebound signs characteristic of opioid withdrawal. In contrast, alcohol and sedative withdrawal do not feature mydriasis, rhinorrhea, or piloerection, but are characterized by tremor, hyperreflexia, and risk of status epilepticus.",
        "incorrectExplanations": {
            "B": "Tachycardia is common to alcohol, stimulant, and opioid withdrawal.",
            "C": "Mild tremors can occur in opioid withdrawal, though they are much more prominent in alcohol withdrawal.",
            "D": "Diaphoresis is a general sign of autonomic arousal present in alcohol, stimulant, and opioid withdrawal syndromes."
        },
        "learningObjective": "Differentiate objective physical assessment signs of opioid withdrawal from sedative-hypnotic withdrawal using the COWS instrument.",
        "reference": "Wesson, D. R., & Ling, W. (2003). The Clinical Opiate Withdrawal Scale (COWS). Journal of Psychoactive Drugs, 35(2), 253-259.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1236",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Foundation",
        "questionText": "A client with severe opioid use disorder is initiated on methadone maintenance therapy. Why must the starting dose of methadone be conservative (typically 20 to 30 mg daily) during the first week of induction, regardless of the client's self-reported high street heroin tolerance?",
        "options": [
            {"id": "A", "text": "Methadone is an antagonist at mu-opioid receptors and will trigger immediate withdrawal at high doses."},
            {"id": "B", "text": "Methadone has a long, highly variable elimination half-life (24 to 36 hours) leading to slow tissue accumulation, meaning fatal respiratory depression can occur on days 3 to 5 if the initial dose is too high."},
            {"id": "C", "text": "Methadone undergoes complete first-pass hepatic destruction if more than 30 mg is swallowed."},
            {"id": "D", "text": "Higher initial doses of methadone cause irreversible renal tubular calcification."}
        ],
        "correctAnswer": "B",
        "explanation": "Methadone is a lipid-soluble, full mu-opioid agonist with an elimination half-life ranging from 15 to 60 hours (average 24–36 hours). Its analgesic effects last 4–8 hours, but its respiratory depressant effects accumulate slowly across successive daily doses. An initial dose that appears tolerable on Day 1 can lead to toxic accumulation and fatal respiratory arrest by Day 3–5 as steady-state plasma concentrations are approached.",
        "incorrectExplanations": {
            "A": "Methadone is a full agonist, not an antagonist.",
            "C": "Methadone has high oral bioavailability (approximately 70–80%) and is well absorbed.",
            "D": "Methadone does not cause renal tubular calcification; its primary life-threatening risk is respiratory depression."
        },
        "learningObjective": "Explain the pharmacokinetic profile of methadone and the rationale for conservative dose induction.",
        "reference": "World Health Organization. (2009). Guidelines for the Psychosocially Assisted Pharmacological Treatment of Opioid Dependence. WHO Guidelines Approved by the Guidelines Review Committee.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1237",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A 46-year-old client on high-dose methadone maintenance (120 mg daily) is prescribed oral fluconazole for a fungal infection. Why is this pharmacological combination hazardous, and what cardiac assessment must the psychiatric nurse prioritize?",
        "options": [
            {"id": "A", "text": "Fluconazole accelerates methadone excretion, causing acute opiate withdrawal and hypertensive crisis."},
            {"id": "B", "text": "Fluconazole induces CYP3A4 enzymes, reducing methadone levels to near zero within 4 hours."},
            {"id": "C", "text": "Methadone causes dose-dependent QTc prolongation, and fluconazole is a potent CYP3A4 inhibitor that increases methadone plasma levels, substantially elevating the risk of Torsades de Pointes; obtain a 12-lead ECG."},
            {"id": "D", "text": "Fluconazole binds irreversibly to opioid receptors, displacing methadone and precipitating pulmonary edema."}
        ],
        "correctAnswer": "C",
        "explanation": "Methadone blocks cardiac hERG potassium channels, prolonging the cardiac QTc interval. At doses > 100 mg daily, the risk of QTc prolongation and polymorphic ventricular tachycardia (Torsades de Pointes) is heightened. Fluconazole inhibits CYP3A4 and CYP2C19 (the enzymes metabolizing methadone), markedly increasing serum methadone concentrations and compounding ventricular arrhythmogenic risk.",
        "incorrectExplanations": {
            "A": "Fluconazole inhibits methadone breakdown, increasing drug levels rather than accelerating clearance.",
            "B": "Fluconazole is a CYP inhibitor, not an inducer.",
            "D": "Fluconazole does not bind opioid receptors."
        },
        "learningObjective": "Identify drug interactions and cardiac safety monitoring requirements associated with methadone maintenance.",
        "reference": "Krantz, M. J., et al. (2009). QTc interval screening in methadone treatment. Annals of Internal Medicine, 150(6), 387-395.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1238",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A client with opioid dependence last used street fentanyl 4 hours ago and demands an immediate initial dose of sublingual buprenorphine. The client's COWS score is currently 4 (minimal withdrawal). If the psychiatric nurse administers buprenorphine at this juncture, what acute clinical complication will occur?",
        "options": [
            {"id": "A", "text": "Immediate severe respiratory arrest due to synergistic full-agonist receptor hyperactivation."},
            {"id": "B", "text": "Acute toxic psychosis caused by excessive dopamine synthesis."},
            {"id": "C", "text": "Neuroleptic malignant syndrome resulting from severe central dopamine depletion."},
            {"id": "D", "text": "Severe precipitated opioid withdrawal, because buprenorphine has a very high receptor affinity and will rapidly displace full agonists while exhibiting lower intrinsic efficacy."}
        ],
        "correctAnswer": "D",
        "explanation": "Buprenorphine is a partial mu-opioid receptor agonist with exceptionally high receptor binding affinity and low intrinsic activity. If administered while full agonists (heroin, morphine, fentanyl) are occupying receptors and the client is not yet in moderate withdrawal, buprenorphine displaces the full agonists, causing a precipitous drop in receptor activation and triggering acute, severe precipitated withdrawal. Induction requires objective withdrawal (COWS >= 12–13).",
        "incorrectExplanations": {
            "A": "Buprenorphine partial agonism has a ceiling effect on respiratory depression and does not cause synergistic agonist depression.",
            "B": "Precipitated withdrawal causes severe autonomic and gastrointestinal distress, not primary toxic dopamine psychosis.",
            "C": "Neuroleptic malignant syndrome is caused by dopamine antagonists, not partial opioid agonists."
        },
        "learningObjective": "Explain the pharmacology of buprenorphine-precipitated withdrawal and verify timing criteria for safe induction.",
        "reference": "Ling, W., et al. (2012). Buprenorphine: an update on pharmacological aspects and clinical uses. Expert Opinion on Pharmacotherapy, 13(6), 807-823.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1239",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "Why is naloxone combined with buprenorphine in a 4:1 fixed ratio in the formulation known as Suboxone, and how does this combination function when taken as prescribed versus when misused?",
        "options": [
            {"id": "A", "text": "When taken sublingually as prescribed, naloxone has minimal bioavailability (<10%) due to extensive first-pass hepatic metabolism, allowing buprenorphine to work; but if crushed and injected intravenously, naloxone blocks mu receptors and precipitates acute withdrawal, deterring parenteral abuse."},
            {"id": "B", "text": "Naloxone enhances the sublingual absorption of buprenorphine by 500% through salivary alkalization."},
            {"id": "C", "text": "Naloxone acts as a gentle stimulant to prevent buprenorphine-induced morning somnolence."},
            {"id": "D", "text": "Naloxone converts buprenorphine from a partial agonist into an irreversible full agonist in the stomach."}
        ],
        "correctAnswer": "A",
        "explanation": "Suboxone combines buprenorphine and naloxone (4:1 ratio) as an abuse-deterrent formulation. Taken sublingually, naloxone has negligible bioavailability (<10%) due to nearly complete first-pass hepatic glucuronidation, so buprenorphine's partial agonist action is unimpeded. However, if crushed and injected parenterally, naloxone enters the systemic circulation directly, antagonizes mu-opioid receptors, and induces acute withdrawal in opioid-dependent individuals.",
        "incorrectExplanations": {
            "B": "Naloxone does not enhance the sublingual absorption of buprenorphine.",
            "C": "Naloxone is an opioid antagonist, not a central nervous system stimulant.",
            "D": "Naloxone does not convert buprenorphine into a full agonist; buprenorphine remains a partial agonist."
        },
        "learningObjective": "Articulate the pharmacology and clinical rationale for the buprenorphine/naloxone combination product.",
        "reference": "Mendelson, J., & Jones, R. T. (2003). Clinical issues in using buprenorphine/naloxone. In Buprenorphine Therapy of Opiate Addiction (pp. 51-66).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1240",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A mental health nurse conducts a Take-Home Naloxone training session for peer workers and families of individuals with opioid use disorder. Which vital pharmacological concept regarding naloxone's duration of action must the nurse emphasize to prevent fatal community overdose outcomes?",
        "options": [
            {"id": "A", "text": "Naloxone remains active in the brain for 72 hours, so emergency medical services are unnecessary once the person breathes."},
            {"id": "B", "text": "Naloxone has an elimination half-life of only 30 to 90 minutes, whereas many opioids (such as methadone or sustained-release oxycodone) have much longer durations of action; the victim may relapse into fatal respiratory arrest as naloxone wears off, making emergency services mandatory."},
            {"id": "C", "text": "Naloxone can only be administered by a registered medical practitioner via central venous catheter."},
            {"id": "D", "text": "Repeated doses of naloxone cause permanent pulmonary fibrosis within 2 hours of administration."}
        ],
        "correctAnswer": "B",
        "explanation": "Naloxone's plasma half-life is approximately 30 to 90 minutes. In contrast, street opioids, fentanyl analogs, and especially long-acting opioids like methadone retain active receptor occupancy for many hours. Once naloxone dissociates from the mu receptors, residual circulating opioids can rebind, precipitating recurrent life-threatening respiratory depression. Calling emergency medical services is critical even after successful revival.",
        "incorrectExplanations": {
            "A": "Naloxone's duration of action is short (30–90 minutes), not 72 hours.",
            "C": "Naloxone can be safely administered by laypersons via intranasal spray or intramuscular auto-injector.",
            "D": "Naloxone does not cause pulmonary fibrosis; it is a safe and specific pure opioid antagonist."
        },
        "learningObjective": "Educate community stakeholders on the critical pharmacokinetic parameters of naloxone to prevent rebound overdose.",
        "reference": "World Health Organization. (2014). Community Management of Opioid Overdose. World Health Organization.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1241",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A nurse discovers an inpatient client unconscious in the hospital bathroom with cyanotic lips, a respiratory rate of 4 breaths per minute, unresponsiveness to deep sternal rub, and bilateral pinpoint pupils (miosis < 2 mm). What is this clinical triad diagnostic of, and what is the immediate priority intervention?",
        "options": [
            {"id": "A", "text": "Lithium toxicity; administer intravenous normal saline bolus and arrange emergent hemodialysis."},
            {"id": "B", "text": "Benzodiazepine toxicity; administer intravenous flumazenil immediately."},
            {"id": "C", "text": "Acute opioid overdose toxidrome; call for emergency medical assistance, support airway/ventilation with high-flow oxygen, and administer naloxone immediately."},
            {"id": "D", "text": "Anticholinergic toxidrome; administer intravenous physostigmine and perform bladder catheterization."}
        ],
        "correctAnswer": "C",
        "explanation": "The classic opioid toxidrome triad comprises: (1) central nervous system depression (coma/unresponsiveness), (2) severe respiratory depression (bradypnea < 8–10 breaths/min or apnea), and (3) pinpoint pupils (miosis). Immediate management requires airway protection, bag-valve-mask assisted oxygenation, and prompt administration of naloxone (IV, IM, or intranasal) to reverse mu-opioid receptor-mediated respiratory depression.",
        "incorrectExplanations": {
            "A": "Lithium toxicity causes coarse tremors, hyperreflexia, ataxia, and confusion, not pinpoint pupils and bradypnea.",
            "B": "Benzodiazepine overdose typically produces normal or sluggish pupils, not pinpoint miosis, and flumazenil carries severe seizure risks.",
            "D": "Anticholinergic toxidrome presents with dilated pupils (mydriasis), dry skin, hyperthermia, and delirium ('blind as a bat, hot as a hare, dry as a bone')."
        },
        "learningObjective": "Identify the acute opioid overdose toxidrome and execute immediate life-saving resuscitation and naloxone protocols.",
        "reference": "Boyer, E. W. (2012). Management of opioid analgesic overdose. New England Journal of Medicine, 367(2), 146-155.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1242",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Advanced",
        "questionText": "A 34-year-old client on stable methadone maintenance (80 mg daily) for 8 months requests unobserved 'take-home' doses to accommodate a new job. Which clinical criteria must the addiction nurse evaluate in accordance with national opioid substitution treatment guidelines before granting take-home privileges?",
        "options": [
            {"id": "A", "text": "Whether the client can recite the entire history of methadone synthesis and has never missed an appointment for 3 years."},
            {"id": "B", "text": "Whether the client has achieved at least 5 years of verified continuous abstinence from caffeine and nicotine."},
            {"id": "C", "text": "Whether the client agrees to allow random weekly home search inspections by law enforcement officers."},
            {"id": "D", "text": "Demonstrated stability, absence of recent illicit drug misuse on random urine screens, regular clinic attendance, safe home storage capacity (e.g., lockable box), and absence of diversion or overdose risk."}
        ],
        "correctAnswer": "D",
        "explanation": "Clinical guidelines for granting take-home doses of opioid agonist therapy evaluate several criteria: stability of lifestyle, adherence to treatment, negative toxicology screens for unprescribed opioids and hazardous sedatives/alcohol, absence of diversion behaviors, and availability of secure medication storage (to prevent accidental child poisoning or diversion).",
        "incorrectExplanations": {
            "A": "Historical pharmacological knowledge is irrelevant to evaluating clinical stability.",
            "B": "Caffeine and nicotine abstinence are not prerequisites for methadone take-home dosing.",
            "C": "Law enforcement home searches violate client human rights and are not part of clinical healthcare standards."
        },
        "learningObjective": "Evaluate clinical criteria for safe take-home opioid agonist medication dispensing.",
        "reference": "Department of Health (England) and the devolved administrations. (2017). Drug misuse and dependence: UK guidelines on clinical management. London: Department of Health.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1243",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Advanced",
        "questionText": "A 40-year-old client enrolled in a buprenorphine maintenance program (16 mg sublingual daily) sustains multiple fractures in a motor vehicle collision. The surgical resident suggests completely discontinuing buprenorphine and withholding all opioids due to 'addiction liability.' What is the evidence-based psychiatric liaison nursing guidance regarding acute pain management for this client?",
        "options": [
            {"id": "A", "text": "Maintain the baseline buprenorphine dose to prevent acute withdrawal and preserve opioid tolerance, while co-administering titrated short-acting full mu-opioid agonists with higher receptor affinity or non-opioid multimodal analgesics under close cardiorespiratory monitoring."},
            {"id": "B", "text": "Agree with the resident, because administering any pain medications to an individual on buprenorphine is medically futile and triggers immediate relapse."},
            {"id": "C", "text": "Discontinue buprenorphine and treat severe bone fractures solely with oral paracetamol and relaxation exercises."},
            {"id": "D", "text": "Administer high-dose naloxone infusions to cleanse opioid receptors before giving morphine."}
        ],
        "correctAnswer": "A",
        "explanation": "Clients on opioid agonist maintenance have high opioid tolerance and hyperalgesia. Abruptly discontinuing buprenorphine causes acute withdrawal, destabilizes recovery, and increases stress. Current evidence supports either continuing the baseline buprenorphine dose (to prevent withdrawal) and adding titrated full-agonist opioids (which can overcome buprenorphine's partial blockade at adequate doses) or dividing the buprenorphine dose, alongside multimodal non-opioid analgesia.",
        "incorrectExplanations": {
            "B": "Withholding analgesia in acute trauma is unethical, clinically harmful, and counterproductive.",
            "C": "Paracetamol alone is inadequate for acute multiple traumatic fractures.",
            "D": "Naloxone will precipitate acute agonizing withdrawal and aggravate shock."
        },
        "learningObjective": "Formulate an evidence-based acute pain management plan for clients on maintenance opioid agonist treatment.",
        "reference": "Alford, D. P., et al. (2006). Collaborative care for opioid-dependent patients: acute pain management in patients on buprenorphine maintenance. Annals of Internal Medicine, 144(2), 127-134.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1244",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Opioid Use Disorder",
        "difficulty": "Expert",
        "questionText": "A harm reduction psychiatric nurse reviews safer injecting practices with a client who injects heroin and has lost peripheral arm vein access. The client mentions plans to begin injecting into the 'groin' (femoral vein). What specific anatomical hazards must the nurse educate the client about to prevent catastrophic morbidity?",
        "options": [
            {"id": "A", "text": "Femoral injection has no anatomical hazards and is the safest recommended route for intravenous administration."},
            {"id": "B", "text": "Accidental puncture of the adjacent femoral artery causes uncontrollable arterial hemorrhage or limb-threatening pseudoaneurysm; damage to the femoral nerve can cause permanent motor paralysis; and deep vein thrombosis (DVT) with pulmonary embolism carries high mortality."},
            {"id": "C", "text": "Femoral injections cause immediate loss of hearing due to cranial nerve VIII pressure."},
            {"id": "D", "text": "The femoral vein directly connects to the hepatic portal system, instantly destroying all liver cells."}
        ],
        "correctAnswer": "B",
        "explanation": "The femoral triangle contains the femoral nerve, femoral artery, femoral vein, and deep lymphatics in close anatomical proximity ('NAVEL' from lateral to medial: Nerve, Artery, Vein, Empty space, Lymphatics). Blind groin injecting carries severe risks: accidental puncture of the femoral artery (leading to arterial rupture, hematoma, pseudoaneurysm, limb ischemia), femoral nerve trauma (chronic neuropathic pain, foot drop), and deep vein thrombosis (DVT) leading to pulmonary embolism or chronic venous ulceration.",
        "incorrectExplanations": {
            "A": "Femoral injecting carries exceptionally high morbidity and is strongly discouraged in harm reduction counseling.",
            "C": "Femoral injection does not exert cranial nerve pressure.",
            "D": "The femoral vein drains into the external iliac vein and inferior vena cava, not the portal system."
        },
        "learningObjective": "Deliver targeted harm reduction education regarding the anatomical and vascular dangers of femoral vein injection.",
        "reference": "Hope, V. D., et al. (2015). Groin injecting in the context of increasing bacterial infections among people who inject drugs. Addiction, 110(8), 1288-1296.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # ---------------------------------------------------------
    # Topic 4: Stimulant and Cocaine Misuse (MHN-Q1245 to MHN-Q1254)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1245",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Foundation",
        "questionText": "What is the primary cellular neurochemical mechanism of action responsible for the intense euphoria, behavioral alertness, and reinforcing properties of cocaine?",
        "options": [
            {"id": "A", "text": "Direct agonist stimulation of post-synaptic GABA-B receptors."},
            {"id": "B", "text": "Irreversible inhibition of monoamine oxidase type A (MAO-A)."},
            {"id": "C", "text": "Competitive blockade of monoamine reuptake transporters—predominantly the dopamine transporter (DAT), norepinephrine transporter (NET), and serotonin transporter (SERT)—leading to marked accumulation of synaptic monoamines."},
            {"id": "D", "text": "Antagonism of central muscarinic acetylcholine M1 receptors."}
        ],
        "correctAnswer": "C",
        "explanation": "Cocaine acts by binding to and blocking the presynaptic monoamine reuptake transporters: the dopamine transporter (DAT), norepinephrine transporter (NET), and serotonin transporter (SERT). By preventing the clearance of dopamine from the synaptic cleft in the mesolimbic pathway (ventral tegmental area to nucleus accumbens), cocaine generates intense dopamine accumulation responsible for its euphoric and reinforcing properties.",
        "incorrectExplanations": {
            "A": "GABA-B agonists (such as baclofen) produce muscle relaxation and sedation, not cocaine-like stimulation.",
            "B": "Cocaine does not inhibit monoamine oxidase; it blocks transporter reuptake.",
            "D": "Muscarinic antagonism causes anticholinergic symptoms (dry mouth, urinary retention), not cocaine's primary mechanism."
        },
        "learningObjective": "Describe the cellular mechanism of action of cocaine on monoamine neurotransmitter transporters.",
        "reference": "Ritz, M. C., et al. (1987). Cocaine receptors on dopamine transporters are related to self-administration of cocaine. Science, 237(4819), 1219-1223.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1246",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Foundation",
        "questionText": "How does crack cocaine chemically and pharmacokinetically differ from powder cocaine (cocaine hydrochloride), and why does crack have a significantly higher dependence liability?",
        "options": [
            {"id": "A", "text": "Crack cocaine is a synthetic opiate that binds mu receptors with higher potency."},
            {"id": "B", "text": "Crack cocaine can only be absorbed rectally, resulting in delayed peak plasma levels over 6 hours."},
            {"id": "C", "text": "Crack cocaine contains no active cocaine molecules and acts entirely via placebo effect."},
            {"id": "D", "text": "Crack is the freebase form created by processing cocaine hydrochloride with sodium bicarbonate and water; it has a lower melting point, is smoked/inhaled, absorbs almost instantaneously across the pulmonary alveolar capillary bed, reaches the brain in 6 to 8 seconds, and produces an intense peak followed by an abrupt 'crash'."}
        ],
        "correctAnswer": "D",
        "explanation": "Cocaine hydrochloride (powder) is salt-based, degrades when heated, and is typically insufflated or dissolved for injection. Crack is the alkaloid freebase form made by heating cocaine hydrochloride with baking soda. Because it vaporizes at low temperatures without decomposing, it can be inhaled. Pulmonary absorption delivers cocaine to the brain within seconds, producing an immediate, intense euphoric rush followed by rapid elimination, driving compulsive repeated redosing.",
        "incorrectExplanations": {
            "A": "Crack is a stimulant form of cocaine, not an opiate.",
            "B": "Crack is volatilized and inhaled, resulting in nearly instantaneous pulmonary delivery, not delayed absorption.",
            "C": "Crack contains high concentrations of active freebase cocaine."
        },
        "learningObjective": "Contrast the pharmacokinetics and dependence potential of crack cocaine with cocaine hydrochloride.",
        "reference": "Hatsukami, D. K., & Fischman, M. W. (1996). Crack cocaine: risks and additions. JAMA, 276(19), 1580-1588.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1247",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Foundation",
        "questionText": "A 26-year-old male with no past medical history is brought to the emergency department following an acute cocaine binge. He is clutching his chest, complaining of crushing substernal chest pain, and is diaphoretic with a heart rate of 128 bpm and blood pressure of 190/110 mmHg. An ECG reveals ST-segment elevation. Which triple pathophysiological mechanism explains cocaine-induced acute myocardial infarction?",
        "options": [
            {"id": "A", "text": "Coronary artery vasospasm via alpha-1 adrenergic stimulation, accelerated platelet aggregation/thrombus formation, and marked increase in myocardial oxygen demand from elevated heart rate and contractility."},
            {"id": "B", "text": "Coronary artery dilation, hypotension, and sudden hyperkalemic bradycardia."},
            {"id": "C", "text": "Immune-mediated destruction of aortic valve leaflets and mitral stenosis."},
            {"id": "D", "text": "Direct inhibition of myocardial sodium channels leading to massive pericardial effusion."}
        ],
        "correctAnswer": "A",
        "explanation": "Cocaine causes myocardial infarction through a triad of mechanisms: (1) marked alpha-1 adrenergic coronary vasoconstriction leading to intense epicardial vasospasm; (2) enhanced platelet activation and thromboxane production promoting acute coronary thrombosis; and (3) pronounced beta-1 and beta-2 adrenergic stimulation causing tachycardia and hypertension, drastically elevating myocardial oxygen demand when supply is restricted.",
        "incorrectExplanations": {
            "B": "Cocaine causes vasoconstriction, hypertension, and tachycardia, not coronary vasodilation and bradycardia.",
            "C": "Cocaine chest pain is ischemic, not caused by acute valvular destruction.",
            "D": "Pericardial effusion is not the primary mechanism of acute cocaine-induced myocardial infarction."
        },
        "learningObjective": "Explain the multi-factorial cardiovascular pathophysiology of cocaine-induced myocardial ischemia and infarction.",
        "reference": "Lange, R. A., & Hillis, L. D. (2001). Cardiovascular complications of cocaine use. New England Journal of Medicine, 345(5), 351-358.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1248",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Intermediate",
        "questionText": "When managing acute cocaine-induced chest pain, tachycardia, and severe hypertension in the emergency department, which class of cardiovascular medications is traditionally contraindicated as monotherapy due to the phenomenon of 'unopposed alpha-adrenergic stimulation'?",
        "options": [
            {"id": "A", "text": "Intravenous benzodiazepines (e.g., lorazepam)"},
            {"id": "B", "text": "Pure, non-selective beta-adrenergic blockers (e.g., propranolol)"},
            {"id": "C", "text": "Sublingual nitroglycerin"},
            {"id": "D", "text": "Calcium channel blockers (e.g., diltiazem)"}
        ],
        "correctAnswer": "B",
        "explanation": "Administering pure, non-selective beta-blockers (like propranolol) in acute cocaine toxicity blocks beta-2 receptor-mediated vasodilation while leaving alpha-1 adrenergic receptors unopposed. This allows excessive circulating norepinephrine and epinephrine to bind unopposed alpha-1 receptors, causing paradoxical worsening of coronary vasoconstriction, malignant hypertension, and increased myocardial ischemia. Benzodiazepines are first-line therapy.",
        "incorrectExplanations": {
            "A": "Benzodiazepines are the first-line medication of choice to reduce central sympathetic outflow, heart rate, and blood pressure.",
            "C": "Nitroglycerin is indicated to relieve coronary vasospasm and reduce cardiac preload.",
            "D": "Calcium channel blockers can be used as second-line agents to treat cocaine-associated vasospasm and hypertension."
        },
        "learningObjective": "Identify pharmacological contraindications and first-line treatment principles in acute cocaine cardiovascular toxicity.",
        "reference": "McCord, J., et al. (2008). Management of cocaine-associated chest pain and myocardial infarction: a scientific statement from the American Heart Association. Circulation, 117(14), 1897-1907.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1249",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Intermediate",
        "questionText": "A 31-year-old client with chronic cocaine dependence presents to the psychiatric crisis unit with numerous open, excoriated skin lesions across both arms and legs. She is terrified, stating that thousands of tiny parasites are burrowing beneath her skin, and she has been using tweezers to dig them out. Which specific tactile hallucinatory phenomenon is this client exhibiting?",
        "options": [
            {"id": "A", "text": "Hypnagogic sleep-onset illusion"},
            {"id": "B", "text": "Lilliputian visual hallucination"},
            {"id": "C", "text": "Formication (also known as 'cocaine bugs' or Magnan's sign)"},
            {"id": "D", "text": "Gegenhalten paratonic motor rigidity"}
        ],
        "correctAnswer": "C",
        "explanation": "Formication (Magnan's sign, commonly referred to as 'cocaine bugs' or 'meth mites') is a specific tactile hallucination characterized by the false sensation of insects, parasites, or worms crawling on or under the skin. It frequently leads to compulsive scratching, skin picking (dermatillomania), and secondary excoriations or ulcerations in individuals with chronic heavy stimulant misuse.",
        "incorrectExplanations": {
            "A": "Hypnagogic hallucinations occur during the transition to sleep and are not chronic parasitic delusions.",
            "B": "Lilliputian hallucinations involve seeing tiny people or animals, which are visual rather than tactile.",
            "D": "Gegenhalten is involuntary resistance to passive limb movement seen in frontal lobe dysfunction, not a tactile perception."
        },
        "learningObjective": "Recognize and document formication and stimulant-induced tactile hallucinations.",
        "reference": "Ellinwood, E. H. (1971). Assault and homicide associated with amphetamine abuse. American Journal of Psychiatry, 127(9), 1170-1175.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1250",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Intermediate",
        "questionText": "A 24-year-old client abruptly stops a 4-day continuous binge of crack cocaine. Over the subsequent 48 hours, the client enters the acute withdrawal phase ('the crash'). Which constellation of psychological and physiological symptoms should the psychiatric nurse anticipate during this phase?",
        "options": [
            {"id": "A", "text": "Severe hypertension, dilated pupils, insomnia, and hypersexual euphoria."},
            {"id": "B", "text": "Generalized tonic-clonic seizures, hyperthermia, and auditory hallucinations."},
            {"id": "C", "text": "Profound muscular rigidity, elevated creatine kinase, and oculogyric crisis."},
            {"id": "D", "text": "Profound dysphoria, anhedonia, extreme psychomotor fatigue, hypersomnia, hyperphagia (increased appetite), intense craving, and elevated risk of suicide."}
        ],
        "correctAnswer": "D",
        "explanation": "Stimulant withdrawal ('the crash') follows cessation of prolonged high-dose cocaine or amphetamine use as central dopamine and norepinephrine stores become severely depleted. It is characterized by the polar opposite of intoxication: profound dysphoria, anhedonia, exhaustion, prolonged hypersomnia, increased appetite (hyperphagia), vivid unpleasant dreams, psychomotor retardation, and deep depressive affect with potential for acute suicidal ideation.",
        "incorrectExplanations": {
            "A": "Hypertension, insomnia, and euphoria characterize acute stimulant intoxication, not withdrawal.",
            "B": "Seizures and delirium are typical of severe alcohol or sedative withdrawal, not stimulant withdrawal.",
            "C": "Muscular rigidity and oculogyric crisis indicate neuroleptic-induced extrapyramidal reactions or NMS."
        },
        "learningObjective": "Identify the clinical manifestations of the stimulant withdrawal crash and assess suicide risk.",
        "reference": "Gawin, F. H., & Kleber, H. D. (1986). Abstinence symptomatology and psychiatric impairment in 100 cocaine abusers. Archives of General Psychiatry, 43(2), 107-113.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1251",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Advanced",
        "questionText": "A 28-year-old chronic crystal methamphetamine user is admitted to the psychiatric hospital with persistent persecutory delusions, auditory hallucinations, and psychomotor agitation lasting 4 weeks after cessation of drug use. Toxicological screens are negative. Why can methamphetamine-induced psychotic disorder persist for weeks or months after drug clearance?",
        "options": [
            {"id": "A", "text": "Methamphetamine causes profound terminal axonal degeneration of dopamine and serotonin transporters, leading to chronic neurotoxicity, altered gene expression, and persistent neurochemical sensitization in the limbic system."},
            {"id": "B", "text": "Methamphetamine permanently integrates into host neuronal DNA, turning neurons into viral factories."},
            {"id": "C", "text": "Methamphetamine completely calcifies the occipital lobes within 48 hours of first use."},
            {"id": "D", "text": "Methamphetamine is permanently stored in body fat and released continuously for 10 years."}
        ],
        "correctAnswer": "A",
        "explanation": "Methamphetamine is directly neurotoxic. It generates reactive oxygen and nitrogen species, damages presynaptic dopamine and serotonin nerve terminals, causes sustained downregulation of dopamine transporters (DAT), and induces lasting neuroplastic alterations (behavioral sensitization) in mesolimbic circuitry. In vulnerable individuals, this can manifest as persistent psychosis lasting weeks, months, or years after cessation.",
        "incorrectExplanations": {
            "B": "Methamphetamine is a small synthetic molecule; it does not contain genetic material or integrate into DNA.",
            "C": "Methamphetamine does not cause acute calcification of the occipital cortex.",
            "D": "While lipophilic, methamphetamine is eliminated by hepatic metabolism and renal excretion over days, not decades."
        },
        "learningObjective": "Explain the neurobiological mechanisms underlying persistent methamphetamine-induced psychosis.",
        "reference": "Volkow, N. D., et al. (2001). Loss of dopamine transporters in methamphetamine abusers recovers with protracted abstinence. Journal of Neuroscience, 21(23), 9414-9418.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1252",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Advanced",
        "questionText": "A 23-year-old brought to the emergency department after taking excessive 'ecstasy' (MDMA) and methamphetamine at an all-night rave has a core body temperature of 41.2°C, profuse sweating, violent psychomotor delirium, a heart rate of 165 bpm, and passes dark tea-colored urine. Laboratory analysis reveals serum creatine kinase (CK) of 45,000 IU/L. Which medical emergency has developed, and what is the immediate nursing priority?",
        "options": [
            {"id": "A", "text": "Severe diabetic ketoacidosis; administer subcutaneous long-acting insulin glargine."},
            {"id": "B", "text": "Severe stimulant-induced hyperthermia, rhabdomyolysis, and acute kidney injury; initiate aggressive external cooling, intravenous fluid resuscitation with normal saline, and intensive monitoring."},
            {"id": "C", "text": "Opioid withdrawal crisis; administer sublingual buprenorphine immediately."},
            {"id": "D", "text": "Catatonic stupor; administer oral lorazepam and avoid all physical cooling blankets."}
        ],
        "correctAnswer": "B",
        "explanation": "MDMA and methamphetamine toxicity can trigger life-threatening hyperpyrexia (temperature > 40°C) driven by continuous muscular hyperactivity, central serotonin/dopamine storm, and impaired thermoregulation. Severe hyperthermia leads to rhabdomyolysis (massive skeletal muscle breakdown releasing myoglobin, indicated by dark urine and extreme CK elevation) and acute tubular necrosis. Immediate management prioritizes aggressive cooling (evaporative mist, ice packs) and high-volume IV crystalloids to prevent renal failure.",
        "incorrectExplanations": {
            "A": "The clinical picture shows hyperthermia and rhabdomyolysis from amphetamine toxicity, not primary diabetic ketoacidosis.",
            "C": "Opioid withdrawal does not cause core temperatures > 41°C and CK of 45,000 IU/L.",
            "D": "Failing to cool a patient with a temperature of 41.2°C will lead to multi-organ failure and death."
        },
        "learningObjective": "Manage acute stimulant-induced hyperthermia, rhabdomyolysis, and associated systemic complications.",
        "reference": "Hall, A. P., & Henry, J. A. (2006). Acute toxic effects of ‘Ecstasy’ (MDMA) and related compounds: overview of pathophysiology and clinical management. British Journal of Anaesthesia, 96(6), 678-685.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1253",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Advanced",
        "questionText": "While pharmacotherapies for stimulant use disorders remain limited, which behavioral psychotherapeutic intervention has demonstrated the most robust empirical evidence base and highest effect size for promoting cocaine and methamphetamine abstinence in clinical trials?",
        "options": [
            {"id": "A", "text": "Long-term psychoanalytic dream analysis"},
            {"id": "B", "text": "Aversion therapy using electrical shock stimulation"},
            {"id": "C", "text": "Contingency Management (CM), utilizing voucher- or incentive-based tangible reinforcement for objective proof of drug-negative urine toxicology screens"},
            {"id": "D", "text": "Mandatory confrontational peer group interventions"}
        ],
        "correctAnswer": "C",
        "explanation": "Contingency Management (CM), rooted in operant conditioning, provides immediate, tangible rewards (vouchers exchangeable for goods, privileges, or prize draws) contingent on objective evidence of desired behavior (such as drug-free urine toxicology tests). Multiple Cochrane reviews and clinical trials show CM has the largest effect size of any psychosocial intervention for stimulant use disorders.",
        "incorrectExplanations": {
            "A": "Psychoanalysis has no robust empirical evidence for promoting abstinence in acute stimulant use disorder.",
            "B": "Aversion electrical shocks are obsolete, ethically concerning, and lack efficacy in stimulant rehabilitation.",
            "D": "Confrontational approaches increase resistance, defensiveness, and treatment drop-out."
        },
        "learningObjective": "Identify evidence-based psychosocial interventions, specifically Contingency Management, for stimulant use disorders.",
        "reference": "Prendergast, M., et al. (2006). Contingency management for treatment of substance use disorders: a meta-analysis. Addiction, 101(11), 1546-1560.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1254",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Stimulant and Cocaine Misuse",
        "difficulty": "Expert",
        "questionText": "A 30-year-old patient who used crack cocaine 2 hours ago is pacing rapidly in the psychiatric assessment room, clenching his fists, shouting paranoid accusations, and showing extreme vigilance toward the door. What is the evidence-based psychiatric nursing priority for de-escalating this acute stimulant-induced psychomotor agitation?",
        "options": [
            {"id": "A", "text": "Immediately corner the patient with six security officers and physically restrain him to demonstrate institutional authority."},
            {"id": "B", "text": "Stand within 6 inches of the patient, stare directly into his eyes, and order him to sit down immediately."},
            {"id": "C", "text": "Laugh at his paranoid concerns to show him there is nothing to worry about."},
            {"id": "D", "text": "Ensure a low-stimulus environment, maintain a safe physical distance (outside arm's reach), adopt an open, non-threatening posture, communicate in brief, calm, concrete sentences, offer oral hydration or oral benzodiazepines, and ensure an unblocked exit path for both patient and staff."}
        ],
        "correctAnswer": "D",
        "explanation": "In stimulant-induced agitation and paranoia, the client's amygdala is hyperreactive. De-escalation requires reducing sensory input, avoiding perceived threats (maintaining physical space, open posture, avoiding prolonged confrontational eye contact), using simple concrete speech, and providing options (oral fluids or oral medications like benzodiazepines). Cornering or aggressively restraining a paranoid stimulant user dramatically increases violence risk.",
        "incorrectExplanations": {
            "A": "Cornering an agitated stimulant user provokes acute fight-or-flight aggression and physical violence.",
            "B": "Intense eye contact and invading personal space are interpreted as aggressive challenges by a paranoid patient.",
            "C": "Dismissive laughter invalidates the client and increases paranoid distress and hostility."
        },
        "learningObjective": "Demonstrate verbal de-escalation and environmental management techniques for acute stimulant-induced agitation.",
        "reference": "Richmond, J. S., et al. (2012). Verbal de-escalation of the agitated patient: consensus statement of the American Association for Emergency Psychiatry Project BETA de-escalation workgroup. Western Journal of Emergency Medicine, 13(1), 17-25.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # ---------------------------------------------------------
    # Topic 5: Cannabis Use Disorder (MHN-Q1255 to MHN-Q1264)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1255",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Foundation",
        "questionText": "Under DSM-5-TR diagnostic criteria, which constellation of symptoms emerging within 24 to 72 hours of cessation in a heavy, daily cannabis user confirms the diagnosis of Cannabis Withdrawal Syndrome?",
        "options": [
            {"id": "A", "text": "Irritability, anger or aggression, nervousness or anxiety, sleep difficulty (insomnia, disturbing dreams), decreased appetite or weight loss, restlessness, depressed mood, and physical symptoms such as abdominal pain, shakiness, or sweating."},
            {"id": "B", "text": "Generalized tonic-clonic seizures, visual hallucinations, and extreme hyperpyrexia."},
            {"id": "C", "text": "Profound miosis, bradypnea, and severe constipation."},
            {"id": "D", "text": "Immediate manic grandiosity, flight of ideas, and decreased need for sleep without dysphoria."}
        ],
        "correctAnswer": "A",
        "explanation": "DSM-5-TR defines Cannabis Withdrawal Syndrome as the development of at least 3 symptoms within approximately 1 week following cessation of heavy and prolonged cannabis use: (1) irritability, anger, or aggression; (2) nervousness or anxiety; (3) sleep difficulty (insomnia, vivid dreams); (4) decreased appetite or weight loss; (5) restlessness; (6) depressed mood; and (7) at least one physical symptom causing significant discomfort (abdominal pain, shakiness/tremors, sweating, fever, chills, headache).",
        "incorrectExplanations": {
            "B": "Seizures and delirium tremens occur in alcohol and sedative withdrawal, not uncomplicated cannabis withdrawal.",
            "C": "Pinpoint pupils and bradypnea represent acute opioid toxidrome, not cannabis withdrawal.",
            "D": "Cannabis withdrawal produces dysphoric, irritable, and anxious symptoms rather than euphoric mania."
        },
        "learningObjective": "Identify DSM-5-TR diagnostic criteria and clinical features of Cannabis Withdrawal Syndrome.",
        "reference": "Budney, A. J., & Hughes, J. R. (2006). The cannabis withdrawal syndrome. Current Opinion in Psychiatry, 19(3), 233-238.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1256",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Foundation",
        "questionText": "A 27-year-old male presents to the emergency department for the fourth time in 6 months with recurrent, intractable morning nausea, profuse non-bloody vomiting, and severe crampy abdominal pain. Extensive gastroenterological investigations, including upper endoscopy and CT scans, are entirely normal. The client acknowledges smoking high-potency cannabis daily for 8 years. What clinical condition should the nurse suspect?",
        "options": [
            {"id": "A", "text": "Acute appendicitis"},
            {"id": "B", "text": "Cannabinoid Hyperemesis Syndrome (CHS)"},
            {"id": "C", "text": "Gastric adenocarcinoma"},
            {"id": "D", "text": "Ulcerative colitis"}
        ],
        "correctAnswer": "B",
        "explanation": "Cannabinoid Hyperemesis Syndrome (CHS) is characterized by cyclic episodes of intractable nausea, vomiting, and colicky abdominal pain occurring in the context of chronic, heavy, daily cannabis use (typically lasting years). Gastrointestinal workups are characteristically negative. CHS is often unrecognized, leading to repeated emergency department visits and extensive negative investigative procedures.",
        "incorrectExplanations": {
            "A": "Acute appendicitis presents with localized right lower quadrant pain, fever, and leukocytosis, not chronic cyclical vomiting over months with normal imaging.",
            "C": "Gastric cancer would typically show visible organic pathology on endoscopy.",
            "D": "Ulcerative colitis presents with bloody diarrhea and visible mucosal inflammation on colonoscopy."
        },
        "learningObjective": "Recognize the clinical presentation and diagnostic pattern of Cannabinoid Hyperemesis Syndrome.",
        "reference": "Allen, J. H., et al. (2004). Cannabinoid hyperemesis: cyclical hyperemesis in association with chronic cannabis abuse. Gut, 53(11), 1566-1570.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1257",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Foundation",
        "questionText": "Which pathognomonic behavioral characteristic is uniquely associated with Cannabinoid Hyperemesis Syndrome (CHS), often discovered during the nursing clinical history?",
        "options": [
            {"id": "A", "text": "Compulsive consumption of large volumes of ice water"},
            {"id": "B", "text": "Inability to swallow any solid food for exactly 30 days"},
            {"id": "C", "text": "Learned compulsive hot showering or bathing for hours each day, which provides temporary relief from severe nausea and abdominal pain"},
            {"id": "D", "text": "Compulsive vigorous aerobic exercise during vomiting bouts"}
        ],
        "correctAnswer": "C",
        "explanation": "A hallmark behavioral feature of Cannabinoid Hyperemesis Syndrome is learned compulsive hot showering or bathing (often for hours daily). Hot water temporarily alleviates the severe nausea and pain. Chronic cannabis use dysregulates hypothalamic thermoregulation and transient receptor potential vanilloid 1 (TRPV1) receptors; hot water acts on cutaneous TRPV1 receptors, promoting peripheral vasodilation and redistributing splanchnic blood flow.",
        "incorrectExplanations": {
            "A": "Compulsive ice water ingestion is not a recognized feature of CHS.",
            "B": "Food avoidance is secondary to nausea, but a specific 30-day fast is not a diagnostic hallmark.",
            "D": "Vigorous exercise during vomiting bouts does not relieve CHS and is not observed."
        },
        "learningObjective": "Identify compulsive hot bathing behavior as a pathognomonic clinical feature of Cannabinoid Hyperemesis Syndrome.",
        "reference": "Sorensen, C. J., et al. (2017). Cannabinoid hyperemesis syndrome: diagnosis, pathophysiology, and treatment—a systematic review. Journal of Medical Toxicology, 13(1), 71-87.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1258",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "A client in the emergency department with acute Cannabinoid Hyperemesis Syndrome continues to retch violently despite receiving intravenous ondansetron 8 mg and metoclopramide 10 mg. Which evidence-based topical pharmacological intervention and long-term recommendation should the psychiatric nurse anticipate?",
        "options": [
            {"id": "A", "text": "Oral activated charcoal and recommendation to switch to synthetic cannabinoids."},
            {"id": "B", "text": "Intramuscular adrenaline and advice to smoke cannabis only in the evenings."},
            {"id": "C", "text": "High-dose intravenous dexamethasone and lifelong clear liquid diet."},
            {"id": "D", "text": "Application of topical capsaicin cream (0.075%) to the abdomen/back, and education that complete, permanent cessation of all cannabis is the only definitive curative treatment."}
        ],
        "correctAnswer": "D",
        "explanation": "CHS is famously refractory to standard antiemetics like 5-HT3 antagonists (ondansetron) and dopamine blockers. Topical capsaicin cream binds to and activates TRPV1 receptors in the skin, mimicking the heat of hot showers and providing effective relief from nausea and abdominal cramping. Long-term, patients must be educated that complete cessation of all cannabinoid use is the only definitive cure; symptoms inevitably recur upon resumption.",
        "incorrectExplanations": {
            "A": "Synthetic cannabinoids aggravate CHS with greater toxicity.",
            "B": "Adrenaline is not indicated for CHS and cannabis smoking at any time maintains the syndrome.",
            "C": "Steroids do not resolve CHS and a liquid diet does not treat the underlying cannabinoid toxicity."
        },
        "learningObjective": "Formulate pharmacological and psychoeducational management plans for Cannabinoid Hyperemesis Syndrome.",
        "reference": "Richards, J. R., et al. (2017). Pharmacologic treatment of cannabinoid hyperemesis syndrome: a systematic review. Pharmacotherapy, 37(6), 725-734.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1259",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "How does contemporary 'high-potency' cannabis (e.g., skunk, concentrates, wax, containing 15% to over 30% delta-9-THC) chemically differ from traditional cannabis cultivated decades ago, and what is its specific impact on the risk of developing a psychotic disorder?",
        "options": [
            {"id": "A", "text": "High-potency cannabis has very high delta-9-tetrahydrocannabinol (THC) concentrations with virtually negligible cannabidiol (CBD); because CBD possesses natural antipsychotic and anxiolytic properties, this unbalanced ratio confers a 3- to 5-fold higher risk of developing a psychotic disorder compared to non-users."},
            {"id": "B", "text": "High-potency cannabis contains 90% CBD and 0% THC, which permanently eliminates psychosis risk."},
            {"id": "C", "text": "High-potency cannabis is completely identical in cannabinoid proportions to traditional cannabis."},
            {"id": "D", "text": "High-potency cannabis contains synthetic strychnine added by plants to repel insects."}
        ],
        "correctAnswer": "A",
        "explanation": "Modern intensive cannabis breeding has dramatically increased delta-9-THC levels (the primary psychoactive, psychotomimetic component) while breeding out cannabidiol (CBD). CBD is a negative allosteric modulator of CB1 receptors with intrinsic antipsychotic, anti-inflammatory, and anxiolytic properties. The absence of protective CBD combined with high THC concentrations is epidemiologically linked to a 3- to 5-fold increased risk of developing psychosis.",
        "incorrectExplanations": {
            "B": "High-potency strains have high THC and negligible CBD, not high CBD.",
            "C": "Traditional cannabis contained roughly equal or modest ratios of THC (2–4%) and CBD; modern strains contain up to 20–30% THC.",
            "D": "High-potency cannabis is selectively bred botanically, not laced with strychnine."
        },
        "learningObjective": "Explain how the THC:CBD ratio in high-potency cannabis influences psychosis risk.",
        "reference": "Di Forti, M., et al. (2019). The contribution of cannabis use to variation in the incidence of psychotic disorder across Europe (EU-GEI): a multicentre case-control study. The Lancet Psychiatry, 6(5), 427-436.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1260",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Intermediate",
        "questionText": "In genetic and psychiatric epidemiological research, which specific genetic polymorphisms have been identified that moderate the relationship between adolescent cannabis use and the subsequent risk of developing schizophrenia?",
        "options": [
            {"id": "A", "text": "Trisomy 21 and Fragile X mutations"},
            {"id": "B", "text": "Polymorphisms in the Catechol-O-methyltransferase (COMT Val158Met) gene and the AKT1 gene, where individuals carrying the Val/Val or AKT1 C/C genotypes exhibit significantly heightened vulnerability to cannabis-induced psychosis."},
            {"id": "C", "text": "Huntington gene CAG trinucleotide repeat expansions on chromosome 4"},
            {"id": "D", "text": "Apolipoprotein E epsilon-4 allele homozygosity"}
        ],
        "correctAnswer": "B",
        "explanation": "Gene-environment interaction studies (e.g., Caspi et al.) demonstrated that the COMT Val158Met polymorphism moderates the effect of adolescent cannabis use on psychosis risk: individuals homozygous for the Val allele (which degrades prefrontal dopamine rapidly) who use cannabis in adolescence have a substantially higher risk of developing schizophrenia. Similarly, polymorphisms in the AKT1 gene (involved in dopamine signaling) confer elevated sensitivity to cannabis-induced psychosis.",
        "incorrectExplanations": {
            "A": "Trisomy 21 causes Down syndrome; it is not the gene-environment moderator for cannabis psychosis.",
            "C": "CAG repeats in the HTT gene cause Huntington's disease.",
            "D": "ApoE4 is a major genetic risk factor for late-onset Alzheimer's disease."
        },
        "learningObjective": "Identify genetic moderating factors (COMT and AKT1) linking adolescent cannabis exposure to schizophrenia vulnerability.",
        "reference": "Caspi, A., et al. (2005). Moderation of the effect of adolescent-onset cannabis use on adult psychosis by a functional polymorphism in the catechol-O-methyltransferase gene: longitudinal evidence of a gene X environment interaction. Biological Psychiatry, 57(10), 1117-1127.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1261",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Advanced",
        "questionText": "A 19-year-old university student with no prior psychiatric history smokes high-potency synthetic cannabis ('Spice') and is brought to the emergency department experiencing severe persecutory paranoia, auditory hallucinations of voices laughing, and intense fear. After 5 days of inpatient nursing observation, hydration, and abstinence, all psychotic symptoms completely remit without ongoing antipsychotic medication. How should this episode be classified in contrast to primary schizophrenia?",
        "options": [
            {"id": "A", "text": "Schizophrenia, paranoid subtype, in spontaneous complete remission"},
            {"id": "B", "text": "Factitious disorder imposed on self"},
            {"id": "C", "text": "Substance/Medication-Induced Psychotic Disorder, characterized by rapid onset following substance exposure and prompt resolution within days to weeks of verified abstinence."},
            {"id": "D", "text": "Malingering to avoid university coursework"}
        ],
        "correctAnswer": "C",
        "explanation": "DSM-5-TR Substance-Induced Psychotic Disorder is diagnosed when delusions or hallucinations develop during or soon after substance intoxication or withdrawal, the substance is capable of producing the symptoms, and the disturbance does not persist for a substantial period (usually > 1 month) beyond the cessation of acute intoxication or withdrawal. Spontaneous full resolution within days of verified abstinence confirms a substance-induced etiology.",
        "incorrectExplanations": {
            "A": "Schizophrenia requires continuous signs of disturbance for at least 6 months, not 5 days.",
            "B": "Factitious disorder involves feigning symptoms for psychological internal secondary gains.",
            "D": "Malingering involves intentional fabrication for external gains (e.g., evading legal consequences), which is not the case in acute toxic spice delirium/psychosis."
        },
        "learningObjective": "Differentiate substance-induced psychotic disorder from primary schizophrenia based on clinical course and abstinence response.",
        "reference": "American Psychiatric Association. (2022). Diagnostic and Statistical Manual of Mental Disorders (5th ed., text rev.; DSM-5-TR).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1262",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Advanced",
        "questionText": "A mother brings her 21-year-old son to the community mental health clinic. She describes that over the past 3 years of daily heavy cannabis use, he has dropped out of college, shows total apathy, lacks emotional warmth, exhibits blunted affect, spends all day on the couch with no vocational ambition, and displays impaired executive functioning. Neurological examination and brain MRI are normal. What neuropsychological construct describes this clinical presentation?",
        "options": [
            {"id": "A", "text": "Kluver-Bucy syndrome"},
            {"id": "B", "text": "Primary progressive non-fluent aphasia"},
            {"id": "C", "text": "Bipolar I rapid-cycling mania"},
            {"id": "D", "text": "Amotivational syndrome associated with chronic, heavy cannabis consumption."}
        ],
        "correctAnswer": "D",
        "explanation": "Amotivational syndrome is a clinical pattern observed in chronic, heavy cannabis users characterized by apathy, loss of ambition, avolition, blunted affect, passivity, impaired concentration, and deterioration in educational and social functioning. While historically debated, neuroimaging reveals that chronic heavy THC exposure blunts dopamine synthesis capacity in the striatum, directly impairing reward processing and motivation.",
        "incorrectExplanations": {
            "A": "Kluver-Bucy syndrome involves bilateral temporal lobe lesions causing hyperorality, hypersexuality, and visual agnosia.",
            "B": "Primary progressive aphasia is a neurodegenerative disorder affecting expressive language.",
            "C": "Mania involves hyperactive energy, pressured speech, and grandiosity, which are the opposite of apathy and avolition."
        },
        "learningObjective": "Recognize the manifestations and neurobiological correlates of amotivational syndrome in chronic cannabis users.",
        "reference": "Bloomfield, M. A., et al. (2014). The effects of cannabis on reward processing and motivation: a systematic review. European Neuropsychopharmacology, 24(5), 785-797.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1263",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Advanced",
        "questionText": "Why are synthetic cannabinoid receptor agonists (SCRAs, such as 'Spice', 'K2', 'Black Mamba') associated with significantly greater clinical toxicity, violent agitation, seizures, acute kidney injury, and death compared to natural botanical cannabis?",
        "options": [
            {"id": "A", "text": "SCRAs are full agonists at CB1 and CB2 receptors with up to 100 times higher binding affinity than THC, possess no protective cannabidiol (CBD), and metabolize into active, toxic compounds."},
            {"id": "B", "text": "SCRAs contain no chemical compounds that interact with human cannabinoid receptors."},
            {"id": "C", "text": "SCRAs are pure opioids that cause immediate respiratory depression identical to fentanyl."},
            {"id": "D", "text": "SCRAs only cause mild sedation and have zero biological toxicity."}
        ],
        "correctAnswer": "A",
        "explanation": "Unlike delta-9-THC (which is a partial agonist at CB1 receptors), synthetic cannabinoids are manufactured full agonists with up to 50–100 times greater receptor affinity and efficacy. Furthermore, synthetic preparations contain zero cannabidiol (CBD) to temper the psychotomimetic effects, and their metabolic breakdown products retain potent biological activity. This causes massive CB1 receptor hyperstimulation, leading to severe delirium, seizures, arrhythmias, rhabdomyolysis, and acute renal failure.",
        "incorrectExplanations": {
            "B": "SCRAs bind human CB1 and CB2 receptors with high affinity.",
            "C": "SCRAs are synthetic cannabinoids, not opioids, though they can be adulterated.",
            "D": "SCRAs cause severe, life-threatening neuropsychiatric and systemic toxicity."
        },
        "learningObjective": "Contrast the pharmacology and clinical toxicity of synthetic cannabinoids with botanical cannabis.",
        "reference": "Castaneto, M. S., et al. (2014). Synthetic cannabinoids: new addicted drugs on the horizon. Frontiers in Psychiatry, 5, 23.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1264",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Cannabis Use Disorder",
        "difficulty": "Expert",
        "questionText": "A community psychiatric nurse delivers a harm reduction psychoeducation session to a young adult client with cannabis use disorder who is currently unwilling to pursue total abstinence. Which evidence-based harm reduction recommendation should the nurse offer to reduce physical and psychiatric morbidity?",
        "options": [
            {"id": "A", "text": "Advise the client to mix cannabis with high-dose synthetic stimulants to counteract fatigue."},
            {"id": "B", "text": "Encourage deep breath-holding for 30 seconds when smoking to maximize lung absorption."},
            {"id": "C", "text": "Recommend using dry herb vaporizers instead of smoking with tobacco (combustion), choosing strains with lower THC and higher CBD content, avoiding daily use, and never driving under the influence."},
            {"id": "D", "text": "Advise switching exclusively to unregulated synthetic cannabinoid vape pens."}
        ],
        "correctAnswer": "C",
        "explanation": "Harm reduction in cannabis use focuses on minimizing pulmonary and psychiatric risks: (1) using vaporizers avoids toxic pyrolysis products, carbon monoxide, and co-administration with tobacco; (2) selecting strains with lower THC and balanced CBD mitigates psychosis and anxiety risks; (3) avoiding deep breath-holding (which does not increase THC uptake but increases tar deposition); (4) avoiding daily binging; and (5) abstaining from driving while intoxicated.",
        "incorrectExplanations": {
            "A": "Mixing stimulants with cannabis compounds cardiovascular and psychiatric risks.",
            "B": "Holding breath increases pulmonary tar and hydrocarbon deposition without increasing intoxication.",
            "D": "Synthetic cannabinoid vape pens carry extreme risks of toxic delirium, seizures, and lung injury."
        },
        "learningObjective": "Deliver pragmatic, evidence-based harm reduction guidance for clients with cannabis use disorder.",
        "reference": "Fischer, B., et al. (2017). Lower-risk cannabis use guidelines: a comprehensive update of evidence and recommendations. American Journal of Public Health, 107(8), e1-e12.",
        "contentReviewStatus": "Peer Reviewed"
    }
]
