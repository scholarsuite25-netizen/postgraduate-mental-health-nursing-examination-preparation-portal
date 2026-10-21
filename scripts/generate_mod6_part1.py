# generate_mod6_part1.py
# Questions MHN-Q515 to MHN-Q564 (Module 6, Topics 1 to 5)

mod6_part1 = [
    # -------------------------------------------------------------
    # TOPIC 1: Suicide Risk Assessment and Safety Planning (MHN-Q515 to MHN-Q524)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q515",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Foundation",
        "questionText": "When utilizing the Columbia-Suicide Severity Rating Scale (C-SSRS) during an emergency department triage assessment, which question specifically differentiates 'active suicidal ideation with some intent to act, without specific plan' from 'active suicidal ideation with specific plan and intent'?",
        "options": [
            { "id": "A", "text": "'Have you thought about how you would do this, and do you have some intention of carrying out these thoughts?' versus 'Have you worked out or started to work out the details of how to kill yourself, and do you intend to carry out this plan?'" },
            { "id": "B", "text": "'Do you wish you were dead?' versus 'Have you taken an overdose?'" },
            { "id": "C", "text": "'Are your family members supportive?' versus 'Do you own any firearms?'" },
            { "id": "D", "text": "'Have you ever felt sad in the past month?' versus 'Do you have medical insurance?'" }
        ],
        "correctAnswer": "A",
        "explanation": "In the C-SSRS 5-level ideation hierarchy, Item 4 assesses 'Active Suicidal Ideation with Some Intent to Act, without Specific Plan' (asking if the patient has any intention to act on suicidal thoughts), while Item 5 assesses 'Active Suicidal Ideation with Specific Plan and Intent' (asking if concrete details of how, when, and where have been formulated alongside intent).",
        "incorrectExplanations": {
            "B": "Item 1 assesses passive wish to be dead ('Wish to be Dead'); taking an overdose is actual suicidal behavior, not ideation grading.",
            "C": "Family support and firearm ownership are contextual risk/protective assessments, not the specific C-SSRS ideation differential items.",
            "D": "These are general demographic/mood questions outside the C-SSRS standardized screening algorithm."
        },
        "learningObjective": "Differentiate between levels of suicidal ideation and intent using the Columbia-Suicide Severity Rating Scale (C-SSRS).",
        "reference": "Posner, K., et al. (2011). The Columbia-Suicide Severity Rating Scale: Initial validity and internal consistency findings. American Journal of Psychiatry, 168(12), 1266-1277.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q516",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Intermediate",
        "questionText": "In psychiatric risk stratification, a critical distinction is drawn between static and dynamic suicide risk factors. Which grouping correctly pairs a static risk factor with a dynamic risk factor?",
        "options": [
            { "id": "A", "text": "Static: History of a near-lethal hanging attempt three years ago; Dynamic: Severe acute insomnia, severe psychic agitation, and current alcohol intoxication" },
            { "id": "B", "text": "Static: Acute command auditory hallucinations; Dynamic: Biological male sex" },
            { "id": "C", "text": "Static: Severe marital separation that occurred yesterday; Dynamic: Family history of completed suicide" },
            { "id": "D", "text": "Static: Current severe depressive episode; Dynamic: Genetic polymorphism in the serotonin transporter gene" }
        ],
        "correctAnswer": "A",
        "explanation": "Static risk factors are historical, unchangeable baseline markers (prior suicide attempts, biological sex, family history). Dynamic risk factors are modifiable, fluctuating clinical states (acute insomnia, severe anxiety/agitation, intoxication, active suicidal intent) that serve as immediate targets for emergency clinical intervention.",
        "incorrectExplanations": {
            "B": "Biological sex is static; command hallucinations are dynamic.",
            "C": "Yesterday's marital breakup is dynamic/acute; family suicide history is static.",
            "D": "Depressive episode is dynamic/treatable; genetic polymorphisms are immutable/static."
        },
        "learningObjective": "Distinguish between static and dynamic suicide risk factors to guide immediate crisis intervention.",
        "reference": "Simon, R. I. (2012). Preventing Patient Suicide: Clinical Assessment and Management. American Psychiatric Publishing.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q517",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Foundation",
        "questionText": "During a comprehensive suicide risk evaluation, which patient characteristic represents an internal protective factor against suicide rather than an external protective factor?",
        "options": [
            { "id": "A", "text": "Strong problem-solving ability, positive coping beliefs, and moral/spiritual objections to suicide" },
            { "id": "B", "text": "Having custody of two dependent young children" },
            { "id": "C", "text": "Caring for a beloved golden retriever that requires daily feeding" },
            { "id": "D", "text": "A strong, ongoing therapeutic relationship with an outpatient psychiatric nurse" }
        ],
        "correctAnswer": "A",
        "explanation": "Internal protective factors are psychological strengths, cognitive abilities, and personal belief systems residing within the patient (e.g., adaptive problem-solving skills, emotional resilience, hope for the future, religious/moral beliefs against suicide). Dependent children, pets, and therapeutic relationships are external protective factors.",
        "incorrectExplanations": {
            "B": "Dependent children are external social responsibilities.",
            "C": "Caring for pets is an external responsibility.",
            "D": "A therapeutic relationship is an external interpersonal and clinical support."
        },
        "learningObjective": "Differentiate between internal and external protective factors in comprehensive suicide risk assessment.",
        "reference": "American Association of Suicidology. (2019). Recognizing and Responding to Suicide Risk: Clinical Practice Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q518",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Intermediate",
        "questionText": "The SAD PERSONS scale has historically been used in emergency settings to screen for suicide risk. However, contemporary psychiatric nursing guidelines caution against relying on this scale as a definitive triage tool. What is the primary clinical limitation of the SAD PERSONS scale?",
        "options": [
            { "id": "A", "text": "It has unacceptably low sensitivity and poor predictive validity for prospective suicidal behavior, weighting static demographic factors over acute, fluctuating dynamic mental states" },
            { "id": "B", "text": "It cannot be administered to individuals younger than 65 years of age" },
            { "id": "C", "text": "It requires an invasive cerebrospinal fluid tap to measure 5-HIAA levels" },
            { "id": "D", "text": "It is copyrighted exclusively for use by forensic criminal investigators" }
        ],
        "correctAnswer": "A",
        "explanation": "Multiple large-scale prospective clinical studies have demonstrated that the SAD PERSONS scale has very poor sensitivity and low positive predictive value. It heavily weights static historical/demographic variables (e.g., male sex, single status) while overlooking acute dynamic crisis drivers (e.g., severe agitation, command hallucinations, acute trauma), creating false reassurances.",
        "incorrectExplanations": {
            "B": "The scale was designed for adult populations of all ages, not solely older adults.",
            "C": "The scale is a 10-item clinical mnemonic checklist, requiring no laboratory tests.",
            "D": "The scale has always been in the public domain for medical/nursing use."
        },
        "learningObjective": "Evaluate the clinical limitations and poor predictive validity of the SAD PERSONS scale.",
        "reference": "Bolton, J. M., et al. (2012). A systematic review of suicide risk assessment tools in primary care and emergency departments. Journal of Clinical Psychiatry, 73(6), 844-850.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q519",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Advanced",
        "questionText": "In the evidence-based Stanley-Brown Safety Planning Intervention (SPI), what is the correct hierarchical sequence of the six collaborative steps?",
        "options": [
            { "id": "A", "text": "Step 1: Warning signs; Step 2: Internal coping strategies; Step 3: Social contacts/places for distraction; Step 4: Family/friends who can help resolve crisis; Step 5: Professionals and agencies; Step 6: Making the environment safe (lethal means restriction)" },
            { "id": "B", "text": "Step 1: Involuntary commitment; Step 2: Oral psychotropics; Step 3: ECT; Step 4: Family therapy; Step 5: Seclusion; Step 6: Discharge" },
            { "id": "C", "text": "Step 1: Means restriction; Step 2: Professional contacts; Step 3: Calling emergency services; Step 4: Distraction; Step 5: Warning signs; Step 6: Reflection" },
            { "id": "D", "text": "Step 1: No-suicide contract; Step 2: Medication review; Step 3: Bed check; Step 4: Urine toxicology; Step 5: Social work; Step 6: Close observation" }
        ],
        "correctAnswer": "A",
        "explanation": "The Stanley-Brown Safety Planning Intervention follows a strict hierarchical 6-step escalation: (1) Recognizing warning signs, (2) Using internal coping strategies without contacting others, (3) Socializing with people/places for distraction, (4) Contacting trusted family/friends for crisis help, (5) Contacting mental health professionals and agencies, and (6) Restricting access to lethal means.",
        "incorrectExplanations": {
            "B": "This represents an institutional restraint cascade, not a collaborative patient safety plan.",
            "C": "This inverts the hierarchical steps; internal coping and distraction precede professional contact.",
            "D": "'No-suicide contracts' are clinically discredited, non-protective, and have been replaced by collaborative safety plans.",
        },
        "learningObjective": "Sequence the six standardized hierarchical steps of the Stanley-Brown Safety Planning Intervention.",
        "reference": "Stanley, B., & Brown, G. K. (2012). Safety planning intervention: A collaborative approach to helping patients deal with suicidal ideation and urges. Cognitive and Behavioral Practice, 19(2), 256-264.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q520",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Intermediate",
        "questionText": "What does systemic suicide prevention research identify as the single most effective, evidence-based environmental intervention for immediately reducing suicide mortality rates across clinical and community populations?",
        "options": [
            { "id": "A", "text": "Lethal means restriction (safely securing firearms, limiting quantities of toxic prescription medications, and erecting barriers at high jumping sites)" },
            { "id": "B", "text": "Signing mandatory written 'no-harm' and 'no-suicide' contracts" },
            { "id": "C", "text": "Administering high-dose sedating antihistamines to all distressed patients" },
            { "id": "D", "text": "Mandatory 30-day inpatient psychiatric hospitalizations for any expression of death ideation" }
        ],
        "correctAnswer": "A",
        "explanation": "Lethal means restriction is the most robust, evidence-based suicide prevention intervention known. Because suicidal crises are often acute and time-limited, restricting rapid access to high-fatality means (firearms, lethal medication packs, bridge barriers) saves lives through means substitution with less lethal methods or allowing time for ambivalence to emerge.",
        "incorrectExplanations": {
            "B": "'No-suicide contracts' provide zero legal or clinical protection and have no empirical evidence of reducing mortality.",
            "C": "Sedating antihistamines do not address underlying suicidal drivers and carry anticholinergic risks.",
            "D": "Blanket hospitalizations are restrictive, erode patient trust, and show no evidence of reducing long-term suicide rates."
        },
        "learningObjective": "Explain the evidence base supporting lethal means restriction as a paramount suicide prevention strategy.",
        "reference": "Zalsman, G., et al. (2016). Suicide prevention strategies revisited: 10-year systematic review. The Lancet Psychiatry, 3(7), 646-659.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q521",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Advanced",
        "questionText": "A 54-year-old patient hospitalized for severe melancholic depression who has been profoundly withdrawn, weeping, and psychomotor retarded for two weeks suddenly appears radiant, energetic, and unusually cheerful during morning rounds. He smiles warmly at the nurse, gives away his favorite gold watch to a fellow patient, and states, 'Everything is finally sorted out; I feel total peace today.' How should the psychiatric nurse interpret and respond to this clinical presentation?",
        "options": [
            { "id": "A", "text": "Recognize this sudden, unprompted brightening as a high-risk warning sign of imminent suicide following finalization of a lethal plan; immediately institute continuous 1:1 observation and conduct an urgent reassessment" },
            { "id": "B", "text": "Celebrate the rapid therapeutic efficacy of his antidepressant medication and initiate discharge paperwork" },
            { "id": "C", "text": "Congratulate the patient on his altruistic generosity in giving away his watch" },
            { "id": "D", "text": "Interpret the behavior as a healthy defense mechanism of sublimation and grant unsupervised grounds privileges" }
        ],
        "correctAnswer": "A",
        "explanation": "A sudden, unexpected shift from deep depression to calm cheerfulness, accompanied by giving away prized possessions, is a classic high-risk indicator of finalized suicide intent. The patient experiences relief because the ambivalence of living is resolved by deciding to end their life, and gained physical energy enables action.",
        "incorrectExplanations": {
            "B": "True antidepressant response occurs gradually over weeks; sudden complete cheerfulness overnight with gift-giving is ominous.",
            "C": "Giving away valued belongings ('parting gifts') is a recognized preparatory suicide behavior.",
            "D": "Granting unsupervised privileges under these conditions creates a catastrophic opportunity for suicide."
        },
        "learningObjective": "Identify sudden, unexpected elevation of mood in severe depression as a herald of imminent suicide.",
        "reference": "Sadock, B. J., Sadock, V. A., & Ruiz, P. (2017). Kaplan and Sadock's Comprehensive Textbook of Psychiatry (10th ed.). Wolters Kluwer.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q522",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Advanced",
        "questionText": "When assessing a patient with schizophrenia who is experiencing auditory command hallucinations instructing him to jump off a bridge, which assessment parameter is most predictive of immediate compliance with the command?",
        "options": [
            { "id": "A", "text": "The patient perceives the voice as having high authority, omnipotence, and a recognized personal identity, and admits he feels powerless to resist" },
            { "id": "B", "text": "The voices speak in a foreign language" },
            { "id": "C", "text": "The voices occur only during phase 4 non-REM sleep" },
            { "id": "D", "text": "The patient has a diagnosis of schizophrenia rather than schizoaffective disorder" }
        ],
        "correctAnswer": "A",
        "explanation": "Research on command hallucinations (e.g., Birchwood and colleagues) demonstrates that compliance is strongly predicted by the patient's cognitive beliefs about the voices: perceived omnipotence, high authority, personal familiarity/identity of the voice, and the patient's perceived inability to resist or appease the voice.",
        "incorrectExplanations": {
            "B": "Foreign language hallucinations do not correlate with increased compliance.",
            "C": "True psychiatric hallucinations occur while awake; hypnagogic/hypnopompic events occur at sleep transitions.",
            "D": "Diagnostic subtyping between schizophrenia and schizoaffective disorder does not predict command compliance."
        },
        "learningObjective": "Assess cognitive and phenomenological risk variables predictive of compliance with suicidal command hallucinations.",
        "reference": "Birchwood, M., et al. (2000). The power and omnipotence of voices: Subordinating beliefs in command hallucinations. Psychological Medicine, 30(2), 337-344.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q523",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Foundation",
        "questionText": "A psychiatric inpatient on Level 2 observation (intermittent 15-minute visual checks) suddenly reveals to the nurse, 'I have hidden broken razor blades in my room and I will cut my throat the moment staff walk away.' What immediate observation change must the psychiatric nurse initiate?",
        "options": [
            { "id": "A", "text": "Immediately place the patient on continuous, unbroken 1:1 line-of-sight observation (within arm's reach) and search the environment for the sharp objects" },
            { "id": "B", "text": "Increase observation checks to every 5 minutes while allowing the patient to remain in their closed room" },
            { "id": "C", "text": "Request a routine psychological evaluation for the following morning" },
            { "id": "D", "text": "Administer an oral multivitamin and document the statement in the nursing shift handover" }
        ],
        "correctAnswer": "A",
        "explanation": "Active suicidal ideation with immediate lethal intent, stated access to means (razor blades), and explicit plan requires immediate initiation of continuous 1:1 line-of-sight observation (within arm's length) to prevent fatal harm, along with an immediate safety room search.",
        "incorrectExplanations": {
            "B": "Five-minute intermittent checks leave unmonitored windows sufficient to inflict a fatal laceration.",
            "C": "Delaying assessment until the next morning risks patient death within minutes.",
            "D": "Handover documentation without immediate physical safety containment is severe clinical negligence."
        },
        "learningObjective": "Determine the clinical criteria requiring immediate escalation to continuous 1:1 suicide observation.",
        "reference": "National Institute for Health and Care Excellence (NICE). (2022). Self-harm: Assessment, management and preventing recurrence (NG225).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q524",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Suicide Risk Assessment and Safety Planning",
        "difficulty": "Expert",
        "questionText": "What is the primary clinical difference between Non-Suicidal Self-Injury (NSSI) and a Suicidal Attempt regarding intent, cognitive motivation, and repetitive frequency?",
        "options": [
            { "id": "A", "text": "NSSI is performed without intent to die, serving primarily to regulate intolerable negative affect, end dissociation, or punish oneself, and typically occurs with high chronic frequency; whereas a suicide attempt carries intent to terminate one's life" },
            { "id": "B", "text": "NSSI uses only sharp objects, whereas suicide attempts involve only pharmaceutical overdoses" },
            { "id": "C", "text": "NSSI is exclusively practiced by adolescents, whereas suicide attempts occur exclusively in older adults" },
            { "id": "D", "text": "NSSI carries zero risk of ever resulting in accidental death or future suicide attempts" }
        ],
        "correctAnswer": "A",
        "explanation": "NSSI is distinguished by the explicit absence of suicidal intent. Its primary psychological function is emotional regulation, distress tolerance, relief from numbness/dissociation, or self-directed anger. However, chronic NSSI remains a strong independent risk factor for future suicide attempts due to habituation to physical pain.",
        "incorrectExplanations": {
            "B": "Both NSSI and suicide attempts can utilize overlapping physical modalities (cutting, burning, overdose).",
            "C": "Both NSSI and suicidal behaviors can manifest across the entire lifespan.",
            "D": "NSSI carries significant risk of accidental lethality and is a potent predictor of future suicide attempts."
        },
        "learningObjective": "Differentiate Non-Suicidal Self-Injury from suicidal behavior while recognizing shared clinical vulnerabilities.",
        "reference": "Nock, M. K. (2010). Self-Injury. Annual Review of Clinical Psychology, 6, 339-363.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # TOPIC 2: Acute Agitation Management and De-escalation (MHN-Q525 to MHN-Q534)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q525",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Foundation",
        "questionText": "In Project BETA (Best practices in Evaluation and Treatment of Agitation), which of the following is designated as one of the fundamental 10 domains of verbal de-escalation?",
        "options": [
            { "id": "A", "text": "Respecting personal space, maintaining an open non-threatening posture, speaking concisely with simple language, and establishing what the patient wants" },
            { "id": "B", "text": "Surrounding the patient with security guards to demonstrate overwhelming institutional physical force" },
            { "id": "C", "text": "Arguing logically against the patient's persecutory delusions until they admit error" },
            { "id": "D", "text": "Locking the patient in an empty seclusion room before initiating any verbal dialogue" }
        ],
        "correctAnswer": "A",
        "explanation": "Project BETA's 10 domains of verbal de-escalation include: (1) Respect personal space, (2) Do not provoke, (3) Establish verbal contact, (4) Be concise, (5) Identify wants and feelings, (6) Listen closely, (7) Agree or agree to disagree, (8) Lay down the law and set clear limits, (9) Offer choices and optimism, and (10) Debrief the patient and staff.",
        "incorrectExplanations": {
            "B": "Surrounding a patient with physical force provokes fight-or-flight panic and accelerates violent escalation.",
            "C": "Directly arguing with delusions damages trust and intensifies paranoid agitation.",
            "D": "Seclusion prior to verbal engagement breaches the least restrictive care doctrine."
        },
        "learningObjective": "Identify the core verbal de-escalation principles established by Project BETA.",
        "reference": "Richmond, J. S., et al. (2012). Verbal De-escalation of the Agitated Patient: Consensus Statement of the American Association for Emergency Psychiatry Project BETA De-escalation Workgroup. Western Journal of Emergency Medicine, 13(1), 17-25.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q526",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Intermediate",
        "questionText": "Under the ethical and legal doctrine of the 'Least Restrictive Approach' in psychiatric nursing, what is the mandatory sequence of clinical escalation when managing acute escalating agitation?",
        "options": [
            { "id": "A", "text": "Verbal de-escalation and environmental adaptation -> Voluntary oral medication -> Involuntary rapid tranquilisation (parenteral) -> Mechanical restraint or seclusion as an absolute last resort" },
            { "id": "B", "text": "Mechanical restraint -> Rapid tranquilisation -> Verbal de-escalation -> Voluntary oral medication" },
            { "id": "C", "text": "Immediate seclusion -> Intramuscular neuroleptics -> Environmental adaptation -> Discharge" },
            { "id": "D", "text": "Electroconvulsive therapy -> Intramuscular haloperidol -> Physical restraint -> Psychotherapy" }
        ],
        "correctAnswer": "A",
        "explanation": "The least restrictive principle requires beginning with the lowest level of intrusion: verbal de-escalation and calming the environment. If insufficient, voluntary oral medications are offered. Involuntary parenteral medication is used only when oral measures fail and safety is compromised. Restraint/seclusion is the absolute last resort.",
        "incorrectExplanations": {
            "B": "Starting with mechanical restraint is an ethical and legal violation of human rights.",
            "C": "Seclusion prior to verbal and voluntary measures violates the least restrictive mandate.",
            "D": "ECT is not an emergency de-escalation technique for acute agitation."
        },
        "learningObjective": "Demonstrate understanding of the stepped-care escalation hierarchy in the least restrictive management of agitation.",
        "reference": "NICE. (2015). Violence and aggression: Short-term management in mental health, health and community settings (NG10).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q527",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Intermediate",
        "questionText": "When entering an interview room to conduct verbal de-escalation with an increasingly hostile, pacing patient, what environmental and spatial positioning guidelines should the psychiatric nurse adhere to?",
        "options": [
            { "id": "A", "text": "Maintain at least two arm-lengths of physical distance, ensure an unobstructed exit path to the door for both the nurse and patient, and avoid standing directly between the patient and their exit" },
            { "id": "B", "text": "Close and deadlock the door behind the nurse to ensure total interview privacy" },
            { "id": "C", "text": "Stand within 12 inches of the patient while maintaining unbroken, intense direct eye contact" },
            { "id": "D", "text": "Sit behind a heavy locked desk with arms tightly crossed across the chest" }
        ],
        "correctAnswer": "A",
        "explanation": "Safety guidelines dictate maintaining at least two arm-lengths of personal space (outside kicking/punching range), keeping the doorway unobstructed for both nurse and patient (preventing the patient from feeling trapped/cornered, which triggers violent flight-or-fight reactions), and facilitating rapid exit.",
        "incorrectExplanations": {
            "B": "Deadlocking the door traps the clinician in a room with an agitated individual without an escape route.",
            "C": "Invading personal space and prolonged glaring are perceived as aggressive challenges.",
            "D": "Sitting behind barriers with crossed arms communicates hostile defensiveness and impairs communication."
        },
        "learningObjective": "Apply environmental safety and spatial positioning principles during acute de-escalation.",
        "reference": "Richmond, J. S., et al. (2012). Verbal De-escalation of the Agitated Patient. Western Journal of Emergency Medicine, 13(1), 17-25.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q528",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Foundation",
        "questionText": "When pharmacological intervention is required to treat acute behavioral agitation, why do international guidelines (such as NICE and Project BETA) strongly emphasize offering oral medications (e.g., oral liquid or disintegrating tablets) over intramuscular injections whenever possible?",
        "options": [
            { "id": "A", "text": "Oral administration respects patient autonomy, preserves the therapeutic alliance, causes significantly less trauma, and is perceived as collaborative rather than coercive" },
            { "id": "B", "text": "Oral medications produce instantaneous peak plasma concentrations within 30 seconds" },
            { "id": "C", "text": "Intramuscular injections are legally prohibited in all psychiatric facilities" },
            { "id": "D", "text": "Oral psychotropics have zero risk of causing extrapyramidal symptoms or sedation" }
        ],
        "correctAnswer": "A",
        "explanation": "Oral formulations (tablets, liquids, orally disintegrating tablets) allow the patient to maintain dignity and agency. Involuntary intramuscular injections are physically painful, perceived as punitive assault, damage therapeutic rapport, and can cause injection-site complications.",
        "incorrectExplanations": {
            "B": "Oral medications take 20-45 minutes to absorb, whereas IV/IM routes are faster; however, speed does not justify unnecessary trauma.",
            "C": "IM injections are legally permitted when emergency criteria and least restrictive alternatives are exhausted.",
            "D": "Oral antipsychotics can still cause extrapyramidal symptoms and sedation."
        },
        "learningObjective": "Justify the clinical preference for oral over parenteral psychotropic routes in acute agitation.",
        "reference": "Wilson, M. P., et al. (2012). Behavioral Emergencies for Healthcare Providers. Springer.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q529",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Advanced",
        "questionText": "According to the Maudsley Prescribing Guidelines and NICE guidelines (NG10), which pharmacological combination is considered an evidence-based first-line parenteral regimen for rapid tranquilisation in severe acute psychotic agitation when monotherapy lorazepam is ineffective or inappropriate?",
        "options": [
            { "id": "A", "text": "Intramuscular Haloperidol combined with Intramuscular Promethazine" },
            { "id": "B", "text": "Intravenous Clozapine combined with Intravenous Lithium" },
            { "id": "C", "text": "Intramuscular Chlorpromazine combined with Subcutaneous Morphine" },
            { "id": "D", "text": "Intramuscular Ketamine combined with Oral Buspirone" }
        ],
        "correctAnswer": "A",
        "explanation": "IM Haloperidol combined with IM Promethazine (or monotherapy IM Lorazepam) is an established first-line evidence-based rapid tranquilisation protocol (supported by the TREC trials). Promethazine provides sedative and anticholinergic protection, significantly reducing haloperidol-induced acute dystonia and akathisia.",
        "incorrectExplanations": {
            "B": "Clozapine does not exist in IV form and cannot be initiated in acute agitation; lithium is never a rapid tranquiliser.",
            "C": "Chlorpromazine IM causes severe hypotension and tissue necrosis; morphine is an opioid contraindicated in behavioral agitation.",
            "D": "Ketamine is an anesthetic reserved for extreme delirium with excited exhaustion; buspirone takes weeks to work."
        },
        "learningObjective": "Identify evidence-based parenteral rapid tranquilisation regimens and rationale for combining haloperidol with promethazine.",
        "reference": "Taylor, D. M., Barnes, T. R., & Young, A. H. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q530",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Advanced",
        "questionText": "A 28-year-old agitated patient is administered intramuscular Olanzapine 10 mg for acute psychotic aggression. Which critical pharmacological warning must the psychiatric nurse heed regarding co-administration of parenteral benzodiazepines?",
        "options": [
            { "id": "A", "text": "Parenteral olanzapine and parenteral benzodiazepines (e.g., IM lorazepam) should not be administered simultaneously or within 1 to 2 hours of each other due to documented risks of severe hypotension, respiratory depression, and death" },
            { "id": "B", "text": "Co-administration triggers immediate acute hypertensive stroke" },
            { "id": "C", "text": "Parenteral benzodiazepines completely neutralize the antipsychotic efficacy of olanzapine" },
            { "id": "D", "text": "Olanzapine cannot be administered if the patient has consumed water in the preceding 6 hours" }
        ],
        "correctAnswer": "A",
        "explanation": "The FDA, EMA, and clinical guidelines explicitly warn against the concurrent parenteral administration of IM olanzapine and parenteral benzodiazepines. Co-administration has been linked to fatal cases of severe cardiorespiratory depression, extreme bradycardia, and profound hypotension. An interval of at least 1-2 hours is required.",
        "incorrectExplanations": {
            "B": "The danger is profound hypotension and respiratory arrest, not hypertensive stroke.",
            "C": "Benzodiazepines do not chemically neutralize olanzapine; they synergize with dangerous depressive respiratory outcomes.",
            "D": "Water intake has no bearing on intramuscular absorption."
        },
        "learningObjective": "Recognize the life-threatening drug interaction between parenteral olanzapine and parenteral benzodiazepines.",
        "reference": "Taylor, D. M., Barnes, T. R., & Young, A. H. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q531",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Advanced",
        "questionText": "Following the administration of intramuscular rapid tranquilisation medications to an agitated patient, what physical health monitoring schedule is mandated by psychiatric clinical governance standards (e.g., NICE NG10)?",
        "options": [
            { "id": "A", "text": "Vital signs (temperature, pulse, blood pressure, respiratory rate, and oxygen saturation) and level of consciousness monitored every 15 minutes for the first hour, and every 30 minutes for the second hour until fully stable" },
            { "id": "B", "text": "A single visual check from the hallway window at the end of the 12-hour shift" },
            { "id": "C", "text": "Monitoring vital signs only if the patient verbally complains of chest pain" },
            { "id": "D", "text": "Continuous invasive arterial line blood pressure monitoring in an intensive care isolation unit" }
        ],
        "correctAnswer": "A",
        "explanation": "Post-rapid tranquilisation protocols require rigorous physical health observations (pulse, BP, respiratory rate, SpO2, temperature, and Glasgow Coma Scale / sedation score) every 15 minutes for the first hour, then every 30 minutes for the second hour until the patient is awake, alert, and ambulatory, to detect drug-induced respiratory depression, arrhythmia, or collapse.",
        "incorrectExplanations": {
            "B": "Visual hallway checks are utterly negligent and fail to detect hypoxemia or respiratory arrest.",
            "C": "Sedated patients cannot complain of symptoms; proactive monitoring is essential.",
            "D": "Invasive arterial lines are inappropriate and disproportionate for psychiatric rapid tranquilisation."
        },
        "learningObjective": "Specify the standard physical monitoring protocol and vital sign intervals following rapid tranquilisation.",
        "reference": "NICE. (2015). Violence and aggression: Short-term management in mental health, health and community settings (NG10).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q532",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Intermediate",
        "questionText": "In psychiatric emergency and crisis settings, what is the primary clinical advantage of utilizing a standardized sedation assessment instrument such as the Richmond Agitation-Sedation Scale (RASS)?",
        "options": [
            { "id": "A", "text": "It provides an objective, reliable, 10-point ordinal rating ranging from combative (+4) to unarousable (-5), allowing precise titration of medication to achieve calm without dangerous oversedation" },
            { "id": "B", "text": "It accurately diagnoses the underlying DSM-5 personality disorder" },
            { "id": "C", "text": "It automatically generates a legal warrant for involuntary detention" },
            { "id": "D", "text": "It calculates the exact milligram dose of antipsychotics based on genetic liver enzyme phenotyping" }
        ],
        "correctAnswer": "A",
        "explanation": "The Richmond Agitation-Sedation Scale (RASS) scores arousal from +4 (combative) to -5 (unarousable), with 0 being alert and calm. Utilizing RASS enables clear communication between clinicians, prevents toxic oversedation (targeting a score of 0 to -1), and monitors post-tranquilisation recovery.",
        "incorrectExplanations": {
            "B": "RASS measures acute behavioral arousal and level of consciousness, not personality structure.",
            "C": "RASS is a clinical physiological scale with no legal detention warrant powers.",
            "D": "RASS does not calculate pharmacological pharmacokinetics."
        },
        "learningObjective": "Apply the Richmond Agitation-Sedation Scale (RASS) in monitoring acute agitation and sedation levels.",
        "reference": "Sessler, C. N., et al. (2002). The Richmond Agitation-Sedation Scale: Validity and reliability in adult intensive care unit patients. American Journal of Respiratory and Critical Care Medicine, 166(10), 1338-1344.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q533",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Expert",
        "questionText": "A 62-year-old patient with no prior psychiatric history is brought to the psychiatric emergency service by police due to sudden violent agitation, confusion, sweating, and combative behavior. Before administering sedating psychotropic medications, which rapid medical assessments must the triage nurse prioritize to exclude life-threatening medical mimics?",
        "options": [
            { "id": "A", "text": "Capillary blood glucose (ruling out severe hypoglycemia), pulse oximetry (hypoxia), vital signs (ruling out sepsis/hypertensive crisis), and pupil examination/neurological screen" },
            { "id": "B", "text": "A full 24-hour computerized psychiatric personality inventory" },
            { "id": "C", "text": "Psychoanalytic assessment of repressed childhood rage" },
            { "id": "D", "text": "A complete dental radiography survey" }
        ],
        "correctAnswer": "A",
        "explanation": "Sudden new-onset agitation in an older adult without psychiatric history is organic delirium until proven otherwise. Immediate bedside checks for hypoglycemia, hypoxia, intracranial hemorrhage, sepsis, or acute intoxication/withdrawal are life-saving medical imperatives before administering central nervous system depressants.",
        "incorrectExplanations": {
            "B": "Psychological personality testing is impossible and contraindicated in acute organic delirium.",
            "C": "Acute organic agitation is not caused by psychodynamic repressed anger.",
            "D": "Dental x-rays have no relevance to acute emergency delirium triage."
        },
        "learningObjective": "Formulate rapid triage medical screening protocols to identify medical mimics of acute psychiatric agitation.",
        "reference": "American College of Emergency Physicians (ACEP). (2014). Clinical Policy: Critical issues in the diagnosis and management of the adult psychiatric patient in the emergency department.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q534",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Agitation Management and De-escalation",
        "difficulty": "Expert",
        "questionText": "Following a severe crisis incident involving acute violent aggression and emergency physical containment on an inpatient unit, comprehensive trauma-informed practice requires two distinct debriefing processes. What are these two processes, and what are their respective goals?",
        "options": [
            { "id": "A", "text": "A staff operational and emotional debrief (to review safety protocols, support staff emotional well-being, and learn), and a patient therapeutic debrief (to restore safety, understand triggers, and repair therapeutic alliance)" },
            { "id": "B", "text": "A police interrogation session and a mandatory staff drug screening test" },
            { "id": "C", "text": "A public patient trial in the day room and an administrative disciplinary hearing" },
            { "id": "D", "text": "A formal financial audit and an institutional public relations press briefing" }
        ],
        "correctAnswer": "A",
        "explanation": "Post-incident debriefing comprises: (1) Immediate staff debrief/defusing to process emotional trauma, identify operational improvements, and evaluate safety; and (2) Patient therapeutic debriefing (once calm) to explore what triggered the escalation, how staff could have intervened earlier, and repair therapeutic trust.",
        "incorrectExplanations": {
            "B": "Police interrogation and punitive drug testing contradict trauma-informed clinical care.",
            "C": "Public shaming violates patient dignity, rights, and ethical clinical practice.",
            "D": "Financial audits do not serve immediate clinical or therapeutic recovery needs."
        },
        "learningObjective": "Differentiate between staff and patient post-incident debriefing in trauma-informed crisis intervention.",
        "reference": "Huckshorn, K. A. (2004). Reducing seclusion & restraint in mental health settings: A core strategies approach. Journal of Psychosocial Nursing and Mental Health Services, 42(9), 22-33.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # TOPIC 3: Physical Restraint and Seclusion (MHN-Q535 to MHN-Q544)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q535",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Foundation",
        "questionText": "Under international human rights standards and mental health legislation, under what specific, exclusive clinical circumstance is the initiation of physical restraint or seclusion legally and ethically justified?",
        "options": [
            { "id": "A", "text": "Only as an exceptional emergency measure of absolute last resort to prevent imminent, serious physical harm to the patient or others, when all less restrictive interventions have failed" },
            { "id": "B", "text": "Whenever a patient refuses to swallow prescribed oral psychotropic medications" },
            { "id": "C", "text": "As a behavioral punishment for verbal rudeness or swearing at nursing staff" },
            { "id": "D", "text": "To compensate for inadequate ward staffing levels during night shifts" }
        ],
        "correctAnswer": "A",
        "explanation": "Physical restraint and seclusion are never permissible for punishment, convenience, discipline, or staffing shortages. They are strictly emergency safety interventions of last resort indicated exclusively to avert imminent, serious physical injury when all de-escalation alternatives have been exhausted.",
        "incorrectExplanations": {
            "B": "Medication refusal alone does not justify physical restraint; competency and legal treatment protocols must be followed.",
            "C": "Using containment as punishment is an illegal violation of human rights and constitutes assault.",
            "D": "Using restraint for institutional convenience or short staffing is an egregious violation of professional nursing ethics."
        },
        "learningObjective": "State the strict legal and ethical criteria governing the initiation of physical restraint and seclusion.",
        "reference": "World Health Organization (WHO). (2019). Strategies to end seclusion and restraint: WHO QualityRights specialized training.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q536",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Advanced",
        "questionText": "During a manual physical takedown and containment of an acutely violent patient, what biomechanical hazard makes the 'Prone Position' (face-down on the floor with staff applying downward pressure on the back) life-threatening?",
        "options": [
            { "id": "A", "text": "Positional asphyxia: downward weight on the torso severely impairs diaphragmatic excursion and chest wall expansion, rapidly precipitating fatal metabolic acidosis and cardiac arrest" },
            { "id": "B", "text": "Immediate rupture of the spleen due to gravity alone" },
            { "id": "C", "text": "Sudden complete intracranial arterial calcification" },
            { "id": "D", "text": "Spontaneous bilateral pneumothorax caused by emotional terror" }
        ],
        "correctAnswer": "A",
        "explanation": "Prone restraint with weight applied to the torso is a leading cause of restraint-related death. Positional asphyxia occurs because the patient's diaphragm and intercostal muscles cannot expand against abdominal compression and body weight, resulting in rapid hypoxia, hypercapnia, severe metabolic/lactic acidosis, and fatal arrhythmias.",
        "incorrectExplanations": {
            "B": "Splenic rupture requires blunt abdominal trauma, not gravitational pull.",
            "C": "Arterial calcification is a chronic metabolic disease, not an acute mechanical event.",
            "D": "Terror does not mechanically rupture pleural membranes to cause pneumothorax."
        },
        "learningObjective": "Explain the lethal pathophysiology of positional asphyxia associated with prone physical restraint.",
        "reference": "Paterson, B., et al. (2003). Deaths in custody in the UK: An analysis of violent deaths involving restraint. Journal of Psychiatric and Mental Health Nursing, 10(6), 677-684.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q537",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Foundation",
        "questionText": "When a psychiatric patient is placed into 4-point mechanical bed restraints, what level of nursing monitoring is strictly mandated by clinical safety protocols?",
        "options": [
            { "id": "A", "text": "Continuous, uninterrupted 1:1 face-to-face visual observation by a dedicated nurse, with neurovascular checks and vital signs recorded every 15 minutes" },
            { "id": "B", "text": "Checking on the patient once every 2 hours through a closed wooden door" },
            { "id": "C", "text": "Monitoring the patient solely via an overhead grainy closed-circuit television camera" },
            { "id": "D", "text": "Checking on the patient only when their restraint time limit expires" }
        ],
        "correctAnswer": "A",
        "explanation": "Patients in mechanical restraint are completely helpless and at immediate risk of aspiration, positional asphyxia, nerve injury, circulatory compromise, and lethal cardiac collapse. Continuous, direct 1:1 face-to-face visual observation is mandatory, accompanied by 15-minute neurovascular, respiratory, and circulatory assessments.",
        "incorrectExplanations": {
            "B": "Two-hour intervals leave patients at extreme risk of suffocation or aspiration without staff awareness.",
            "C": "CCTV camera monitoring cannot assess pulse, respiratory excursion, airway patency, or capillary refill.",
            "D": "Waiting until the legal authorization expires is gross negligence."
        },
        "learningObjective": "Detail the continuous 1:1 monitoring and 15-minute assessment requirements for restrained psychiatric patients.",
        "reference": "The Joint Commission. (2020). Comprehensive Accreditation Manual for Hospitals: Restraint and Seclusion Standards.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q538",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Intermediate",
        "questionText": "What clinical criteria must the psychiatric nurse use to determine when a patient should be released from mechanical restraints?",
        "options": [
            { "id": "A", "text": "As soon as the patient demonstrates sustained behavioral calm, absence of imminent violence, ability to follow verbal instructions, and agrees to safety planning, with limbs released sequentially" },
            { "id": "B", "text": "Only when the full four hours of the physician's maximum time order have completely elapsed" },
            { "id": "C", "text": "Only when the patient signs a legally binding waiver agreeing never to file a lawsuit" },
            { "id": "D", "text": "When the patient is asleep and deeply sedated so they cannot react" }
        ],
        "correctAnswer": "A",
        "explanation": "Restraint must be terminated at the earliest possible moment the emergency safety risk abates. The decision is based on objective clinical indicators of calm and cooperation, not arbitrary clock times. Re-release should occur sequentially (e.g., one limb at a time) to ensure ongoing stability.",
        "incorrectExplanations": {
            "B": "Orders specify maximum durations; keeping a calm patient in restraints to 'fill the time' is illegal false imprisonment.",
            "C": "Coercing legal waivers under restraint is illegal and unethical.",
            "D": "Sedated sleeping patients in mechanical restraints face elevated aspiration/asphyxia risks and must be released when safe."
        },
        "learningObjective": "Identify objective clinical criteria for terminating physical restraint safely and promptly.",
        "reference": "American Psychiatric Nurses Association (APNA). (2018). APNA Position Statement: The Use of Seclusion and Restraint.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q539",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Intermediate",
        "questionText": "What is the clinical definition of 'Seclusion' in psychiatric emergency care, and what physical environment is required?",
        "options": [
            { "id": "A", "text": "The involuntary solitary confinement of a patient in a specially designated room from which free exit is denied, featuring safety padding, shatterproof observation glass, and no ligature points" },
            { "id": "B", "text": "Allowing a patient to voluntarily rest in their unlocked personal bedroom" },
            { "id": "C", "text": "Placing a disruptive patient in a bathroom with a locked door" },
            { "id": "D", "text": "Restricting a patient to the communal ward day room during television hours" }
        ],
        "correctAnswer": "A",
        "explanation": "Seclusion is the involuntary solitary confinement of a patient in a designated safety room where exit is physically prevented. The seclusion room must be specifically constructed for safety: impact-resistant walls/padding, shatterproof viewing panels, ligature-free fixtures, external ventilation, and clear visual monitoring.",
        "incorrectExplanations": {
            "B": "Voluntary time-out in an unlocked bedroom is an open de-escalation technique, not seclusion.",
            "C": "Locking a patient in a standard bathroom is extremely dangerous due to hard surfaces, water fixtures, and ligature points.",
            "D": "Dayroom restriction is an administrative rule, not solitary seclusion."
        },
        "learningObjective": "Define seclusion and specify the mandatory architectural safety requirements of a seclusion suite.",
        "reference": "NICE. (2015). Violence and aggression: Short-term management in mental health, health and community settings (NG10).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q540",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Advanced",
        "questionText": "A 30-year-old muscular male patient with excited delirium struggles violently against 4-point leather restraints for three continuous hours despite repeated sedation attempts. His urine in the collection bag turns dark reddish-brown ('tea-colored'). Which life-threatening physiological complication has occurred, and what laboratory parameter must be checked immediately?",
        "options": [
            { "id": "A", "text": "Rhabdomyolysis resulting from intense isometric muscle exertion against restraints; immediately check serum Creatine Kinase (CK) and renal function (BUN/creatinine)" },
            { "id": "B", "text": "Acute urinary tract infection; immediately check urine culture" },
            { "id": "C", "text": "Renal amyloidosis; check 24-hour urine protein" },
            { "id": "D", "text": "Spontaneous bladder rupture; check abdominal ultrasound" }
        ],
        "correctAnswer": "A",
        "explanation": "Violent continuous struggling against mechanical restraints leads to massive skeletal muscle breakdown (rhabdomyolysis). Myoglobin is released into the systemic circulation, filtering into the urine and causing myoglobinuria (tea-colored urine), which precipitates acute tubular necrosis and renal failure. Serum CK is profoundly elevated.",
        "incorrectExplanations": {
            "B": "Tea-colored urine after violent struggling is classic myoglobinuria, not a routine bacterial UTI.",
            "C": "Amyloidosis is a chronic protein-folding systemic disease, not an acute traumatic complication.",
            "D": "Bladder rupture presents with peritonitis and anuria, not dark tea-colored urine filled with myoglobin."
        },
        "learningObjective": "Recognize rhabdomyolysis and acute kidney injury as critical physiological complications of prolonged restraint.",
        "reference": "Mohr, W. K., et al. (2003). Adverse physiological effects of physical restraint: A review for pediatric and adult nurses. Journal of Psychosocial Nursing, 41(9), 16-24.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q541",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Intermediate",
        "questionText": "What psychological sequela is most frequently documented among psychiatric patients who have undergone involuntary physical restraint and seclusion, particularly those with pre-existing trauma and abuse histories?",
        "options": [
            { "id": "A", "text": "Severe retraumatization, exacerbation of post-traumatic stress symptoms, feelings of profound humiliation, and enduring betrayal trauma that destroys therapeutic trust" },
            { "id": "B", "text": "Development of a healthy, mature gratitude toward psychiatric nursing staff" },
            { "id": "C", "text": "Immediate permanent elimination of all borderline personality pathology" },
            { "id": "D", "text": "Spontaneous increase in prefrontal dopamine D2 receptor density" }
        ],
        "correctAnswer": "A",
        "explanation": "Physical restraint and seclusion are perceived by patients as terrifying, punitive, and coercive assaults. For patients with histories of physical or sexual trauma, being pinned down or locked in an isolation cell replicates past abuse, causing severe retraumatization, profound shame, and destruction of therapeutic rapport.",
        "incorrectExplanations": {
            "B": "Restraint uniformly generates anger, fear, and betrayal, not gratitude.",
            "C": "Traumatic containment exacerbates personality dysfunction and emotional dysregulation.",
            "D": "Restraint induces severe stress axis (cortisol/adrenaline) surges, not therapeutic receptor proliferation."
        },
        "learningObjective": "Analyze the profound psychological harm and retraumatization caused by physical containment.",
        "reference": "Strout, T. D. (2010). Perspectives on the experience of unwanted restraint: An integrative review. Journal of Psychiatric and Mental Health Nursing, 17(5), 416-427.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q542",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Advanced",
        "questionText": "Following an episode of physical restraint, what elements must be meticulously detailed in the clinical nursing documentation to withstand forensic, legal, and accreditation scrutiny?",
        "options": [
            { "id": "A", "text": "Exact precipitating dangerous behaviors, specific de-escalation techniques attempted and reasons for their failure, emergency medical justification, time initiated, staff involved, continuous 15-minute observations (vital signs, circulation, mental state), fluids/nutrition offered, and sequential de-restraint criteria" },
            { "id": "B", "text": "A brief note stating: 'Patient became unruly and was locked in seclusion per standard ward routine'" },
            { "id": "C", "text": "Only the billing code for physical restraint supplies" },
            { "id": "D", "text": "A photocopy of the nurse's state registration certificate" }
        ],
        "correctAnswer": "A",
        "explanation": "Legal and clinical governance mandates rigorous documentation for every restraint event: explicit antecedent behaviors proving imminent danger, less restrictive alternatives tried, medical orders, exact start/stop times, physical checks every 15 minutes, fluids/toileting offered, and detailed release criteria.",
        "incorrectExplanations": {
            "B": "Vague, boilerplate notes ('patient unruly') are legally indefensible and fail to prove emergency necessity.",
            "C": "Billing codes provide no clinical or legal justification for deprivation of liberty.",
            "D": "Staff credentials do not document patient care or clinical monitoring."
        },
        "learningObjective": "Formulate comprehensive, legally defensible nursing documentation for physical restraint and seclusion.",
        "reference": "The Joint Commission. (2020). Restraint and Seclusion Standards. Comprehensive Accreditation Manual for Hospitals.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q543",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Expert",
        "questionText": "When a patient must be physically restrained on a bed to prevent imminent severe violence, which anatomical position is universally recognized as the safest to minimize mortality risk?",
        "options": [
            { "id": "A", "text": "Supine position with the head of the bed elevated 30 to 45 degrees, ensuring free cervical movement and continuous open airway monitoring" },
            { "id": "B", "text": "Prone position with arms pulled backward behind the spine" },
            { "id": "C", "text": "Trendelenburg position with feet elevated above the head" },
            { "id": "D", "text": "Lateral decubitus position with legs tightly strapped together" }
        ],
        "correctAnswer": "A",
        "explanation": "The supine position (face-up) with the head of the bed elevated at 30 to 45 degrees is the safest biomechanical posture. It eliminates torso compression, optimizes lung expansion and diaphragmatic movement, minimizes aspiration risk, and allows unobstructed continuous visualization of the face, airway, and pupils.",
        "incorrectExplanations": {
            "B": "Prone position with arms pulled back severely compresses the chest wall and causes fatal positional asphyxia.",
            "C": "Trendelenburg increases intracranial pressure and restricts diaphragmatic excursion due to abdominal contents pushing up.",
            "D": "Tightly strapping legs in lateral decubitus risks nerve compression and deep vein thrombosis without securing the airway."
        },
        "learningObjective": "Identify the supine position with head elevation as the standard of care for physical bed restraint.",
        "reference": "APNA. (2018). APNA Position Statement: The Use of Seclusion and Restraint.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q544",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Physical Restraint and Seclusion",
        "difficulty": "Expert",
        "questionText": "In Kevin Ann Huckshorn's 'Six Core Strategies for Reducing Seclusion and Restraint' (a widely adopted evidence-based administrative and clinical model), which of the following is designated as Core Strategy #1?",
        "options": [
            { "id": "A", "text": "Leadership Toward Organizational Change (defining restraint reduction as an executive priority with administrative oversight and philosophy)" },
            { "id": "B", "text": "Purchasing stronger, titanium-reinforced mechanical restraint cuffs" },
            { "id": "C", "text": "Mandatory administration of rapid-acting neuroleptics upon every patient admission" },
            { "id": "D", "text": "Banning all family visits to eliminate external emotional triggers" }
        ],
        "correctAnswer": "A",
        "explanation": "Huckshorn's Six Core Strategies are: (1) Leadership Toward Organizational Change, (2) Use of Data to Inform Practice, (3) Workforce Development, (4) Use of S/R Prevention Tools, (5) Full Inclusion of Consumers and Advocates, and (6) Debriefing Techniques. Executive leadership commitment is the foundational prerequisite.",
        "incorrectExplanations": {
            "B": "Purchasing stronger hardware contradicts the goal of restraint elimination.",
            "C": "Mandatory chemical sedation upon admission is unconstitutional and clinically abusive.",
            "D": "Banning family isolates patients and increases distress and aggression."
        },
        "learningObjective": "Identify the leadership and systemic components of Huckshorn's Six Core Strategies for reducing restraint.",
        "reference": "Huckshorn, K. A. (2004). Reducing seclusion & restraint in mental health settings: A core strategies approach. Journal of Psychosocial Nursing and Mental Health Services, 42(9), 22-33.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # TOPIC 4: Catatonia Assessment and Management (MHN-Q545 to MHN-Q554)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q545",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Foundation",
        "questionText": "According to DSM-5 diagnostic criteria, catatonia can be diagnosed when the clinical picture is dominated by at least three of how many classic psychomotor signs?",
        "options": [
            { "id": "A", "text": "Three or more of 12 distinct psychomotor symptoms (including stupor, catalepsy, waxy flexibility, mutism, negativism, posturing, mannerisms, stereotypy, agitation, grimacing, echolalia, and echopraxia)" },
            { "id": "B", "text": "Three or more of 4 symptoms (fever, rigidity, tremor, and rash)" },
            { "id": "C", "text": "Three or more of 6 somatic delusions" },
            { "id": "D", "text": "Three or more laboratory elevations in serum bilirubin" }
        ],
        "correctAnswer": "A",
        "explanation": "Under DSM-5, catatonia (associated with another mental disorder, a medical condition, or unspecified) requires the presence of 3 or more of 12 characteristic psychomotor features: stupor, catalepsy, waxy flexibility, mutism, negativism, posturing, mannerisms, stereotypy, agitation, grimacing, echolalia, and echopraxia.",
        "incorrectExplanations": {
            "B": "Fever, rigidity, and tremor are classic signs of NMS, not the 12 DSM-5 catatonia diagnostic criteria.",
            "C": "Somatic delusions are psychotic thought abnormalities, not catatonic motor criteria.",
            "D": "Catatonia is a clinical psychomotor diagnosis, not a bilirubin laboratory profile."
        },
        "learningObjective": "State the DSM-5 diagnostic criteria and recognize the 12 cardinal psychomotor features of catatonia.",
        "reference": "American Psychiatric Association (APA). (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed.). APA Publishing.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q546",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Intermediate",
        "questionText": "What standardized clinical rating instrument is recognized as the gold standard for screening, diagnosing, and tracking severity of catatonia in psychiatric nursing practice?",
        "options": [
            { "id": "A", "text": "The Bush-Francis Catatonia Rating Scale (BFCRS)" },
            { "id": "B", "text": "The Abnormal Involuntary Movement Scale (AIMS)" },
            { "id": "C", "text": "The Mini-Mental State Examination (MMSE)" },
            { "id": "D", "text": "The Young Mania Rating Scale (YMRS)" }
        ],
        "correctAnswer": "A",
        "explanation": "The Bush-Francis Catatonia Rating Scale (BFCRS) is the gold standard clinical scale. It includes a 14-item screening version (where presence of 2 or more items suggests catatonia) and a full 23-item severity instrument scored from 0 to 3 to quantify baseline severity and treatment response.",
        "incorrectExplanations": {
            "B": "The AIMS specifically assesses tardive dyskinesia, not acute catatonia.",
            "C": "The MMSE screens for cognitive impairment and dementia, not catatonic motor signs.",
            "D": "The YMRS quantifies the severity of manic episodes, not catatonia."
        },
        "learningObjective": "Identify the Bush-Francis Catatonia Rating Scale (BFCRS) as the primary assessment instrument for catatonia.",
        "reference": "Bush, G., et al. (1996). Catatonia. I. Rating scale and standardized examination. Acta Psychiatrica Scandinavica, 93(2), 129-136.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q547",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Intermediate",
        "questionText": "During a physical examination of a catatonic patient, the psychiatric nurse gently raises the patient's arm into an awkward, uncomfortable overhead position. The patient offers slight, uniform resistance during positioning, like bending a warm candle, and then maintains this awkward posture indefinitely without fatigue. Which specific catatonic sign does this demonstrate?",
        "options": [
            { "id": "A", "text": "Waxy Flexibility (cerea flexibilitas)" },
            { "id": "B", "text": "Gegenhalten (oppositional paratonia)" },
            { "id": "C", "text": "Echopraxia" },
            { "id": "D", "text": "Mitgehen" }
        ],
        "correctAnswer": "A",
        "explanation": "Waxy flexibility (cerea flexibilitas) is characterized by slight, even resistance to positioning by the examiner (resembling the bending of a wax candle or soft lead), followed by the patient maintaining the newly imposed uncomfortable position (catalepsy).",
        "incorrectExplanations": {
            "B": "Gegenhalten is active resistance to passive movement that increases in proportion to the force applied by the examiner.",
            "C": "Echopraxia is the involuntary, repetitive copying or mirroring of another person's movements.",
            "D": "Mitgehen ('anglepoise lamp' sign) is an exaggerated cooperation where the patient moves a limb in response to light fingertip pressure, even when instructed to resist."
        },
        "learningObjective": "Differentiate Waxy Flexibility from Gegenhalten, Mitgehen, and other catatonic motor phenomena.",
        "reference": "Fink, M., & Taylor, M. A. (2003). Catatonia: A Clinician's Guide to Diagnosis and Treatment. Cambridge University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q548",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Advanced",
        "questionText": "A psychiatric nurse evaluates a patient with severe catatonia. When the nurse extends a hand and asks the patient to shake hands, the patient moves her hand forward, stops abruptly, pulls it back, moves it forward again, and hesitates in motor deadlock. Later, when asked to sit down, the patient stands rigidly upright. Which two catatonic phenomena are represented?",
        "options": [
            { "id": "A", "text": "Ambitendency and Negativism" },
            { "id": "B", "text": "Echolalia and Stereotypy" },
            { "id": "C", "text": "Waxy flexibility and Automatic obedience" },
            { "id": "D", "text": "Catalepsy and Verbigeration" }
        ],
        "correctAnswer": "A",
        "explanation": "Ambitendency is a motor indecision where the patient is caught between opposing motor impulses (hesitating back and forth, unable to complete an action like shaking hands). Negativism is the motiveless resistance to instructions or attempts to move the patient, or doing the exact opposite (active negativism).",
        "incorrectExplanations": {
            "B": "Echolalia is repeating words; stereotypy is repetitive, non-goal-directed movement.",
            "C": "Automatic obedience is blind compliance with requests; here the patient showed motor conflict and opposition.",
            "D": "Verbigeration is repetitive meaningless vocalizations; catalepsy is posture maintenance."
        },
        "learningObjective": "Recognize ambitendency and negativism during the clinical evaluation of catatonia.",
        "reference": "Bush, G., et al. (1996). Catatonia. I. Rating scale and standardized examination. Acta Psychiatrica Scandinavica, 93(2), 129-136.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q549",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Foundation",
        "questionText": "What constitutes the standard diagnostic and initial therapeutic trial for suspected acute catatonia?",
        "options": [
            { "id": "A", "text": "The Lorazepam Challenge Test (administering 1 to 2 mg of Lorazepam IV or IM, followed by reassessment of BFCRS motor signs within 30 to 60 minutes)" },
            { "id": "B", "text": "Administering Haloperidol 10 mg IM stat" },
            { "id": "C", "text": "A 14-day trial of oral Fluoxetine 20 mg daily" },
            { "id": "D", "text": "Intravenous Naloxone 0.4 mg infusion" }
        ],
        "correctAnswer": "A",
        "explanation": "The Lorazepam Challenge Test is the diagnostic gold standard. Administering 1-2 mg lorazepam IV (or IM/sublingual) typically results in a marked (often dramatic >50%) reduction in catatonic signs (mutism, stupor, rigidity) within 30 to 60 minutes, confirming the diagnosis and establishing initial pharmacotherapy.",
        "incorrectExplanations": {
            "B": "Haloperidol is an antipsychotic that is contraindicated in acute catatonia, risking severe exacerbation or precipitating NMS.",
            "C": "SSRIs have no role in acute emergency catatonia and take weeks to achieve therapeutic levels.",
            "D": "Naloxone is an opioid receptor antagonist for opioid overdose, having no efficacy in catatonia."
        },
        "learningObjective": "Describe the administration protocol and clinical interpretation of the Lorazepam Challenge Test.",
        "reference": "Fink, M., & Taylor, M. A. (2003). Catatonia: A Clinician's Guide to Diagnosis and Treatment. Cambridge University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q550",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Advanced",
        "questionText": "What clinical constellation distinguishes 'Malignant Catatonia' (also termed lethal catatonia) from non-malignant catatonia, converting it into an immediate medical emergency?",
        "options": [
            { "id": "A", "text": "The acute emergence of severe Hyperthermia (>38.0°C / 100.4°F), marked Autonomic Instability (labile blood pressure, tachycardia, diaphoresis), extreme exhaustion, and cardiovascular collapse" },
            { "id": "B", "text": "The presence of visual hallucinations and mild insomnia" },
            { "id": "C", "text": "Refusal to take oral vitamins in the presence of normal vital signs" },
            { "id": "D", "text": "Slow handwriting and mild blunting of facial affect" }
        ],
        "correctAnswer": "A",
        "explanation": "Malignant catatonia is a life-threatening subtype sharing clinical and pathophysiological features with NMS. It is characterized by severe motor signs (stupor or frenzy) complicated by acute hyperthermia, autonomic lability (tachycardia, diaphoresis, fluctuating BP), rhabdomyolysis, and high risk of cardiovascular collapse.",
        "incorrectExplanations": {
            "B": "Visual hallucinations and mild insomnia do not indicate malignant catatonia.",
            "C": "Refusal of vitamins without systemic autonomic compromise is non-malignant.",
            "D": "Blunted affect and micrographia are parkinsonian signs, not malignant catatonia."
        },
        "learningObjective": "Differentiate life-threatening Malignant Catatonia from standard catatonia based on autonomic and thermal signs.",
        "reference": "Sienaert, P., et al. (2014). A clinical review of the treatment of catatonia. Frontiers in Psychiatry, 5, 181.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q551",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Advanced",
        "questionText": "A 38-year-old patient with severe stuporous catatonia has been mute, motionless, and bedbound for 48 hours. Aside from administering prescribed lorazepam, which comprehensive nursing care interventions are critical to prevent life-threatening somatic complications?",
        "options": [
            { "id": "A", "text": "Venous thromboembolism prophylaxis (low-molecular-weight heparin and compression stockings), scheduled 2-hourly pressure repositioning to prevent decubitus ulcers, strict fluid balance monitoring, IV hydration, nutritional support, and bladder scanning/catheterization for urinary retention" },
            { "id": "B", "text": "Encouraging the patient to independently jog around the hospital grounds" },
            { "id": "C", "text": "Administering high-potency oral haloperidol drops every 2 hours" },
            { "id": "D", "text": "Restricting all fluid and food intake until the patient agrees to speak" }
        ],
        "correctAnswer": "A",
        "explanation": "Immobile catatonic patients face high risks of fatal pulmonary embolism (from DVT), decubitus pressure ulcers, acute renal failure (from dehydration/rhabdomyolysis), urinary retention, and severe malnutrition. Prophylactic anticoagulation, pressure injury prevention, and hydration/nutrition are essential nursing priorities.",
        "incorrectExplanations": {
            "B": "A stuporous catatonic patient is paralyzed by motor inhibition and cannot jog.",
            "C": "Antipsychotics are contraindicated in acute catatonia due to severe NMS precipitation risks.",
            "D": "Withholding hydration/food is clinical negligence that guarantees fatal dehydration."
        },
        "learningObjective": "Formulate a comprehensive nursing care plan to prevent somatic complications in stuporous catatonia.",
        "reference": "Boyd, M. A. (2022). Psychiatric Nursing: Contemporary Practice (7th ed.). Wolters Kluwer.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q552",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Intermediate",
        "questionText": "When a patient with malignant catatonia fails to respond to high-dose IV lorazepam (up to 16-24 mg daily) within 48 to 72 hours, or exhibits rapidly escalating hyperthermia and circulatory collapse, what is the definitive, life-saving intervention of choice?",
        "options": [
            { "id": "A", "text": "Emergency Electroconvulsive Therapy (ECT)" },
            { "id": "B", "text": "Immediate initiation of Clozapine monotherapy" },
            { "id": "C", "text": "High-dose intravenous Haloperidol" },
            { "id": "D", "text": "Transcutaneous electrical nerve stimulation (TENS) applied to the calves" }
        ],
        "correctAnswer": "A",
        "explanation": "Electroconvulsive Therapy (ECT) is the definitive, life-saving treatment of choice for malignant catatonia, catatonia refractory to benzodiazepines, and excited catatonia. Bilateral ECT typically induces dramatic reversal of catatonic symptoms and normalizes autonomic physiology.",
        "incorrectExplanations": {
            "B": "Clozapine requires slow titration and cannot treat emergent hyperthermic malignant catatonia.",
            "C": "Haloperidol blocks dopamine receptors and is lethal in malignant catatonia, precipitating fatal NMS.",
            "D": "TENS has zero efficacy for central catatonic neurocircuitry."
        },
        "learningObjective": "Identify Electroconvulsive Therapy (ECT) as the definitive emergency intervention for refractory or malignant catatonia.",
        "reference": "Luchini, F., et al. (2015). Electroconvulsive therapy in catatonia: Modern treatment and clinical considerations. Psychiatric Annals, 45(1), 35-40.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q553",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Advanced",
        "questionText": "Why are high-potency dopamine D2-receptor antagonist antipsychotics (such as Haloperidol or Fluphenazine) strongly contraindicated in the acute management of un-medicated catatonia?",
        "options": [
            { "id": "A", "text": "D2 antagonism drastically worsens catatonic motor immobility, increases skeletal rigidity, and carries an exceptionally high risk of triggering full-blown Neuroleptic Malignant Syndrome (NMS)" },
            { "id": "B", "text": "They cause instantaneous aplastic anemia in catatonic patients" },
            { "id": "C", "text": "They metabolize lorazepam into toxic cyanide metabolites" },
            { "id": "D", "text": "They induce excessive motor hyperactivity and uncontrollable laughter" }
        ],
        "correctAnswer": "A",
        "explanation": "Catatonia involves profound dysfunction in striatal dopaminergic, GABAergic, and glutamatergic pathways. Administering potent D2 receptor blockers shuts down residual striatal dopamine signaling, severely worsening motor stupor and triggering the hyperthermia, extreme rigidity, and autonomic storm of NMS.",
        "incorrectExplanations": {
            "B": "Antipsychotics do not cause instantaneous aplastic anemia in catatonia.",
            "C": "There is no metabolic conversion of lorazepam into cyanide.",
            "D": "D2 blockers worsen akinesia and rigidity, not uncontrollable laughter."
        },
        "learningObjective": "Explain why high-potency typical antipsychotics are contraindicated in acute catatonia.",
        "reference": "van der Heijden, F. M., et al. (2005). The dilemma of treating catatonia with antipsychotics. European Psychiatry, 20(7), 523-524.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q554",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Catatonia Assessment and Management",
        "difficulty": "Expert",
        "questionText": "A 26-year-old patient presents with 'Excited Catatonia' (catatonic excitement). How does this syndrome present clinically, and why does it represent an acute psychiatric emergency?",
        "options": [
            { "id": "A", "text": "Continuous, frenzied, purposeless, non-goal-directed motor agitation with shouting, stereotypy, autonomic instability, and lack of response to external stimuli, which can rapidly result in fatal exhaustion, dehydration, and cardiovascular collapse" },
            { "id": "B", "text": "A calm, euphoric state where the patient composes classical symphonies without needing sleep" },
            { "id": "C", "text": "Mild restless legs syndrome occurring exclusively while seated in evening group therapy" },
            { "id": "D", "text": "Intermittent verbal bragging regarding personal wealth in a patient with stable vital signs" }
        ],
        "correctAnswer": "A",
        "explanation": "Excited catatonia presents with extreme, purposeless, frenzied motor agitation and hyperactivity, uninfluenced by external cues. Patients scream, exhibit stereotypic movements, and neither eat nor sleep. Without emergency benzodiazepines or ECT, it rapidly progresses to hyperthermia, rhabdomyolysis, and fatal circulatory exhaustion.",
        "incorrectExplanations": {
            "B": "This describes creative hypomania, not frenzied excited catatonia.",
            "C": "Restless legs is akathisia or RLS, not life-threatening excited catatonia.",
            "D": "Verbal grandiosity is a feature of mania, lacking catatonic frenzy or fatal exhaustion risk."
        },
        "learningObjective": "Recognize the clinical presentation and life-threatening nature of excited catatonia.",
        "reference": "Fink, M., & Taylor, M. A. (2003). Catatonia: A Clinician's Guide to Diagnosis and Treatment. Cambridge University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # TOPIC 5: Acute Dystonia and Extrapyramidal Emergencies (MHN-Q555 to MHN-Q564)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q555",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Foundation",
        "questionText": "What neurochemical mechanism in the nigrostriatal pathway triggers an acute dystonic reaction following the administration of a high-potency typical antipsychotic (such as haloperidol)?",
        "options": [
            { "id": "A", "text": "Acute, potent dopamine D2 receptor blockade, causing an abrupt loss of dopamine-mediated inhibition of cholinergic interneurons and resulting in relative acetylcholine hyperactivity" },
            { "id": "B", "text": "Massive hyper-stimulation of serotonin 5-HT2A receptors" },
            { "id": "C", "text": "Immediate depletion of gamma-aminobutyric acid (GABA) stores in the spinal cord" },
            { "id": "D", "text": "Excessive noradrenergic receptor synthesis in the locus coeruleus" }
        ],
        "correctAnswer": "A",
        "explanation": "In the nigrostriatal pathway, dopamine exerts a tonic inhibitory brake on acetylcholine release. Potent D2 receptor blockade by neuroleptics abruptly removes this inhibition, creating an acute surge in cholinergic output and an extreme dopamine-acetylcholine imbalance, manifesting as severe muscle spasms.",
        "incorrectExplanations": {
            "B": "5-HT2A stimulation triggers psychedelic experiences or serotonin toxicity, not nigrostriatal acute dystonia.",
            "C": "GABA depletion is involved in stiff-person syndrome or seizures, not standard neuroleptic dystonia.",
            "D": "Noradrenergic hyperactivity in the locus coeruleus produces panic or hyperarousal, not basal ganglia dystonia."
        },
        "learningObjective": "Explain the neurochemical imbalance (dopamine-acetylcholine ratio) underlying acute dystonic reactions.",
        "reference": "Stahl, S. M. (2021). Stahl's Essential Psychopharmacology (5th ed.). Cambridge University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q556",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Intermediate",
        "questionText": "Thirty-six hours after receiving his first dose of intramuscular haloperidol, a 22-year-old male patient suddenly develops sustained, involuntary, spastic upward and lateral deviation of his eyes, unable to look forward. He is in extreme panic and experiencing severe anxiety. What clinical condition is this patient experiencing?",
        "options": [
            { "id": "A", "text": "Oculogyric Crisis" },
            { "id": "B", "text": "Tardive Dyskinesia" },
            { "id": "C", "text": "Nystagmus secondary to cerebellar stroke" },
            { "id": "D", "text": "Horner's syndrome" }
        ],
        "correctAnswer": "A",
        "explanation": "An oculogyric crisis is an acute focal dystonic reaction of the extraocular muscles, characterized by prolonged, painful, involuntary upward and lateral gaze deviation. It is accompanied by severe psychic terror and anxiety and is an acute psychiatric emergency.",
        "incorrectExplanations": {
            "B": "Tardive dyskinesia consists of involuntary choreiform or athetoid movements occurring after months or years of neuroleptic exposure, not hours.",
            "C": "Nystagmus is rhythmic oscillatory eye movement, not fixed sustained spastic upward gaze.",
            "D": "Horner's syndrome features ptosis, miosis, and anhidrosis from sympathetic chain interruption."
        },
        "learningObjective": "Recognize an oculogyric crisis as a classic manifestation of acute neuroleptic-induced dystonia.",
        "reference": "Sadock, B. J., Sadock, V. A., & Ruiz, P. (2017). Kaplan and Sadock's Comprehensive Textbook of Psychiatry (10th ed.). Wolters Kluwer.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q557",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Intermediate",
        "questionText": "A 25-year-old male receiving oral fluphenazine presents with his head violently twisted to the right shoulder, severe pain in the left sternocleidomastoid muscle, and inability to turn his neck to the midline. Which type of acute dystonia is present?",
        "options": [
            { "id": "A", "text": "Acute Torticollis" },
            { "id": "B", "text": "Retrocollis" },
            { "id": "C", "text": "Opisthotonus" },
            { "id": "D", "text": "Trismus" }
        ],
        "correctAnswer": "A",
        "explanation": "Acute torticollis (wry neck) is an acute dystonic spasm of the neck musculature (primarily the sternocleidomastoid, trapezius, and scalene muscles) causing painful twisting and tilting of the head to one side.",
        "incorrectExplanations": {
            "B": "Retrocollis is the severe spastic hyperextension of the neck pulling the head backward.",
            "C": "Opisthotonus is extreme axial arching of the entire spine and back.",
            "D": "Trismus is severe spastic contraction of the masseter muscles causing locked jaw."
        },
        "learningObjective": "Identify acute torticollis and differentiate it from other regional dystonic presentations.",
        "reference": "Taylor, D. M., Barnes, T. R., & Young, A. H. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q558",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Advanced",
        "questionText": "A patient receiving high-dose typical antipsychotics suddenly develops difficulty breathing, high-pitched inspiratory stridor, tachypnea, intercostal retractions, and facial cyanosis. The nurse recognizes this as an acute laryngeal dystonic reaction. What immediate action is required?",
        "options": [
            { "id": "A", "text": "Immediately call a medical emergency crash team, support airway/ventilation with high-flow oxygen, and administer immediate IV or IM Procyclidine or Benztropine" },
            { "id": "B", "text": "Have the patient breathe into a paper bag for hyperventilation syndrome" },
            { "id": "C", "text": "Offer an oral antacid for suspected esophageal reflux" },
            { "id": "D", "text": "Administer an oral tablet of propranolol and re-check in 2 hours" }
        ],
        "correctAnswer": "A",
        "explanation": "Acute laryngeal dystonia is a rare, life-threatening psychiatric emergency where spastic contraction of the laryngeal musculature and vocal cords occludes the upper airway, presenting with inspiratory stridor, cyanosis, and imminent asphyxiation. Emergency airway management and immediate parenteral anticholinergic antidote are required.",
        "incorrectExplanations": {
            "B": "Paper bag breathing causes lethal asphyxiation in anatomical upper airway occlusion.",
            "C": "Antacids do not treat vocal cord spasm and delay life-saving antidote administration.",
            "D": "Oral propranolol treats akathisia or tremors, but is useless and dangerous during acute laryngeal asphyxia."
        },
        "learningObjective": "Recognize and execute immediate emergency resuscitation for life-threatening acute laryngeal dystonia.",
        "reference": "Christodoulou, C., & Kalaitzi, C. (2005). Antipsychotic drug-induced acute laryngeal dystonia: Two case reports and a mini-review. Journal of Psychopharmacology, 19(5), 559-563.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q559",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Advanced",
        "questionText": "A psychiatric nurse evaluates a patient who, following an antipsychotic dose increase, exhibits severe locked jaw with clenched masseter muscles preventing speech or eating, accompanied by dramatic backward arching of the spine where only the back of his head and heels touch the mattress. Which two clinical terms accurately document these dystonic spasms?",
        "options": [
            { "id": "A", "text": "Trismus and Opisthotonus" },
            { "id": "B", "text": "Catalepsy and Mutism" },
            { "id": "C", "text": "Akathisia and Ataxia" },
            { "id": "D", "text": "Chorea and Athetosis" }
        ],
        "correctAnswer": "A",
        "explanation": "Trismus is severe spastic contraction of the masseter and temporalis jaw muscles ('lockjaw'). Opisthotonus is severe, dramatic hyperextension and spastic arching of the entire spinal axis, commonly seen in severe acute dystonic reactions or tetanus.",
        "incorrectExplanations": {
            "B": "Catalepsy is passive posture maintenance without spastic arching; mutism is lack of speech.",
            "C": "Akathisia is subjective inner restlessness; ataxia is cerebellar lack of voluntary muscle coordination.",
            "D": "Chorea consists of rapid, jerky movements; athetosis consists of slow, writhing movements."
        },
        "learningObjective": "Accurately document trismus and opisthotonus during severe extrapyramidal emergencies.",
        "reference": "Sadock, B. J., Sadock, V. A., & Ruiz, P. (2017). Kaplan and Sadock's Comprehensive Textbook of Psychiatry (10th ed.). Wolters Kluwer.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q560",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Foundation",
        "questionText": "What is the primary pharmacological antidote for the rapid reversal of acute neuroleptic-induced dystonic reactions?",
        "options": [
            { "id": "A", "text": "An anticholinergic agent administered IM or IV (such as Procyclidine 5 to 10 mg or Benztropine 1 to 2 mg, or Diphenhydramine 25 to 50 mg)" },
            { "id": "B", "text": "Flumazenil 0.5 mg IV" },
            { "id": "C", "text": "Naloxone 2 mg intranasally" },
            { "id": "D", "text": "Sodium Bicarbonate 100 mEq IV infusion" }
        ],
        "correctAnswer": "A",
        "explanation": "Centrally acting anticholinergic agents (such as Procyclidine 5-10 mg IM/IV, Benztropine 1-2 mg IM/IV, or the anticholinergic antihistamine Diphenhydramine 25-50 mg IM/IV) block excess muscarinic cholinergic activity in the striatum, restoring the dopamine-acetylcholine balance and providing dramatic relief within 5-15 minutes.",
        "incorrectExplanations": {
            "B": "Flumazenil is a benzodiazepine antagonist that induces seizures and has zero efficacy against dystonia.",
            "C": "Naloxone reverses opioid toxicity and has no effect on striatal extrapyramidal mechanisms.",
            "D": "Sodium bicarbonate treats tricyclic antidepressant cardiotoxicity, not acute dystonia."
        },
        "learningObjective": "Identify anticholinergic agents (procyclidine, benztropine, diphenhydramine) as the definitive antidotes for acute dystonia.",
        "reference": "Taylor, D. M., Barnes, T. R., & Young, A. H. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q561",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Foundation",
        "questionText": "What is the typical time frame of onset for acute dystonic reactions following the initiation or significant dose escalation of a high-potency typical antipsychotic?",
        "options": [
            { "id": "A", "text": "Within the first 24 to 96 hours (with over 50% occurring within 48 hours and up to 90% within 5 days)" },
            { "id": "B", "text": "After 6 to 12 months of continuous uninterrupted treatment" },
            { "id": "C", "text": "Within the first 30 seconds of swallowing an oral tablet" },
            { "id": "D", "text": "Only upon abrupt discontinuation after decades of use" }
        ],
        "correctAnswer": "A",
        "explanation": "Acute dystonic reactions occur acutely at the beginning of treatment or immediately following dose increases. Greater than 50% occur within the first 48 hours, and approximately 90% occur within 5 days of initiation or titration.",
        "incorrectExplanations": {
            "B": "Onset after 6-12 months is characteristic of tardive dyskinesia, not acute dystonia.",
            "C": "Oral tablets require gastrointestinal absorption (20-45 minutes); 30 seconds is physiologically impossible.",
            "D": "Withdrawal dyskinesias emerge upon discontinuation, whereas acute dystonia occurs upon drug introduction."
        },
        "learningObjective": "Specify the typical clinical time course and latency of acute dystonic reactions.",
        "reference": "Stahl, S. M. (2021). Stahl's Essential Psychopharmacology (5th ed.). Cambridge University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q562",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Intermediate",
        "questionText": "Which demographic and clinical profile carries the highest epidemiological risk for developing acute neuroleptic-induced dystonic reactions?",
        "options": [
            { "id": "A", "text": "Young age (adolescents and young adults), biological male sex, history of prior dystonic reactions, and high-dose high-potency first-generation antipsychotic use" },
            { "id": "B", "text": "Elderly female patients with osteoporosis" },
            { "id": "C", "text": "Patients receiving low-dose second-generation atypical antipsychotics" },
            { "id": "D", "text": "Infants receiving prophylactic infant vitamins" }
        ],
        "correctAnswer": "A",
        "explanation": "Young males have the highest density and sensitivity of striatal dopamine receptors, making young men receiving high-potency first-generation antipsychotics (e.g., haloperidol, fluphenazine) at least twice as likely to experience acute dystonia compared to other cohorts.",
        "incorrectExplanations": {
            "B": "Elderly females are at high risk for tardive dyskinesia and parkinsonism, but have lower risk for acute dystonia.",
            "C": "Atypical antipsychotics have much lower D2 affinity and 5-HT2A antagonism, carrying significantly lower dystonia risk.",
            "D": "Infants do not receive dopamine-blocking neuroleptics in vitamin preparations."
        },
        "learningObjective": "Identify demographic and pharmacological risk factors predisposing patients to acute dystonia.",
        "reference": "Keepers, G. A., et al. (1983). The risk of early adverse reactions to high-potency antipsychotics. Psychiatric Annals, 13(4), 312-321.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q563",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Advanced",
        "questionText": "Following the successful emergency reversal of an acute oculogyric crisis with intramuscular procyclidine, what ongoing post-acute management is essential to prevent a secondary rebound dystonic reaction?",
        "options": [
            { "id": "A", "text": "Prescribing an oral anticholinergic agent (e.g., oral procyclidine or benztropine) for 2 to 3 days, accompanied by reassurance and a multidisciplinary review of the antipsychotic regimen" },
            { "id": "B", "text": "Immediately doubling the offending antipsychotic dose to overcome receptor sensitivity" },
            { "id": "C", "text": "Discharging the patient immediately with instructions to attend the emergency room if spasms recur" },
            { "id": "D", "text": "Placing the patient on permanent bed rest in mechanical restraints" }
        ],
        "correctAnswer": "A",
        "explanation": "Parenteral anticholinergics have a shorter elimination half-life than long-acting neuroleptics (like haloperidol). As the anticholinergic wears off after a few hours, the patient remains at high risk for recurrent dystonia. Continuation of oral anticholinergics for 48-72 hours, alongside reassurance and psychiatric regimen review (switching to an atypical agent), is required.",
        "incorrectExplanations": {
            "B": "Doubling the neuroleptic dose increases D2 blockade and triggers catastrophic, severe dystonia or NMS.",
            "C": "Discharging without oral anticholinergic coverage guarantees a terrifying rebound dystonia at home.",
            "D": "Mechanical restraint is medically contraindicated and does nothing to prevent pharmacological spasms."
        },
        "learningObjective": "Formulate a post-acute management plan to prevent rebound dystonic reactions.",
        "reference": "Taylor, D. M., Barnes, T. R., & Young, A. H. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q564",
        "module": "6. Psychiatric Emergencies and Crisis Intervention",
        "topic": "Acute Dystonia and Extrapyramidal Emergencies",
        "difficulty": "Expert",
        "questionText": "A psychiatric nurse working on an acute ward observes a patient gasping with acute torticollis and panic. The ward protocol includes a pre-approved nurse-initiated emergency Medical Standing Order for acute dystonia. What is the nurse's priority sequence of actions?",
        "options": [
            { "id": "A", "text": "Ensure airway patency, provide calm verbal reassurance to reduce panic, verify vital signs and contraindications, administer the standing order dose of parenteral procyclidine or benztropine, and document the event and response" },
            { "id": "B", "text": "Refuse to intervene until an on-call physician arrives from across the city two hours later" },
            { "id": "C", "text": "Forcefully twist the patient's neck back to the center using manual traction" },
            { "id": "D", "text": "Administer an extra dose of the offending antipsychotic medication" }
        ],
        "correctAnswer": "A",
        "explanation": "Under standing emergency orders, the psychiatric nurse acts promptly: assesses and maintains airway, reassures the terrified patient, confirms dosage and contraindications (e.g. angle-closure glaucoma, myasthenia gravis), delivers the IM/IV anticholinergic, monitors response, and informs the medical team.",
        "incorrectExplanations": {
            "B": "Delaying treatment for hours when an emergency protocol exists causes unnecessary agony and risks airway compromise.",
            "C": "Manual neck manipulation against severe muscle spasm risks cervical spine fracture or spinal cord damage.",
            "D": "Administering more antipsychotic worsens the acute neurochemical crisis."
        },
        "learningObjective": "Execute nurse-initiated emergency standing orders for acute extrapyramidal dystonic crises safely and effectively.",
        "reference": "Boyd, M. A. (2022). Psychiatric Nursing: Contemporary Practice (7th ed.). Wolters Kluwer.",
        "contentReviewStatus": "Peer Reviewed"
    }
]
