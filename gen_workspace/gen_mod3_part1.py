# gen_workspace/gen_mod3_part1.py
"""
Module 3 Part 1: Topics 1 to 5 (Q215 - Q264, 50 questions)
Module: "3. Psychopathology and Psychiatric Diagnosis"
"""

MOD3_P1 = [
    # -------------------------------------------------------------
    # Topic 1: Schizophrenia Spectrum and Other Psychotic Disorders (Q215 - Q224)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q215",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Foundation",
        "questionText": "A 23-year-old university student is admitted to an acute psychiatric unit presenting with persecutory delusions, auditory hallucinations of commenting voices, and derailment of thought. Which clinical category do these manifestations represent within the psychopathology of schizophrenia?",
        "options": [
            {"id": "A", "text": "Positive symptoms reflecting an excess or distortion of normal psychological functioning"},
            {"id": "B", "text": "Negative symptoms reflecting a diminution or loss of goal-directed motivation"},
            {"id": "C", "text": "Cognitive deficits reflecting impaired central executive working memory"},
            {"id": "D", "text": "Catatonic signs indicating psychomotor disturbance and autonomic lability"}
        ],
        "correctAnswer": "A",
        "explanation": "Positive symptoms of schizophrenia represent an excess, exaggeration, or distortion of normal cognitive, perceptual, and behavioural functioning. Key examples include hallucinations (sensory perceptions without external stimuli), delusions (fixed false beliefs resistant to counter-evidence), and disorganised thinking/speech (such as derailment or loose associations).",
        "incorrectExplanations": {
            "A": "Positive symptoms represent an excess or distortion of normal functions.",
            "B": "Negative symptoms represent the reduction or absence of normal emotional expression and goal-directed behavior (e.g., avolition, alogia, anhedonia).",
            "C": "Cognitive deficits involve impairments in working memory, processing speed, and executive function, rather than florid perceptual distortions.",
            "D": "Catatonic signs specifically involve motor abnormalities such as stupor, posturing, catalepsy, or waxy flexibility."
        },
        "learningObjective": "Differentiate between positive, negative, and cognitive symptom clusters in schizophrenia.",
        "reference": "American Psychiatric Association. (2022). Diagnostic and Statistical Manual of Mental Disorders (5th ed., text rev.; DSM-5-TR). Arlington, VA.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q216",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Foundation",
        "questionText": "During a key-worker interview, a patient diagnosed with chronic schizophrenia provides brief, monosyllabic responses with prolonged latencies, speaking only two or three words in response to open-ended questions despite showing willingness to engage. Which negative symptom is this patient displaying?",
        "options": [
            {"id": "A", "text": "Anhedonia"},
            {"id": "B", "text": "Alogia"},
            {"id": "C", "text": "Avolition"},
            {"id": "D", "text": "Asociality"}
        ],
        "correctAnswer": "B",
        "explanation": "Alogia, or poverty of speech, is a cardinal negative symptom characterized by a marked reduction in the quantity of speech and spontaneous elaboration. Thought processes appear diminished, resulting in brief, empty, concrete, or monosyllabic verbal output.",
        "incorrectExplanations": {
            "A": "Anhedonia refers to the reduced capacity to experience pleasure from previously rewarding activities.",
            "B": "Alogia is poverty of speech and diminished spontaneous elaboration.",
            "C": "Avolition is a deficit in the initiation and persistence of goal-directed activities.",
            "D": "Asociality refers to a lack of interest in social interactions and relationship building."
        },
        "learningObjective": "Accurately assess and document specific negative symptoms in psychotic disorders.",
        "reference": "Sadock, B. J., Sadock, V. A., & Ruiz, P. (2017). Kaplan & Sadock's Comprehensive Textbook of Psychiatry (10th ed.). Wolters Kluwer.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q217",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Intermediate",
        "questionText": "Under DSM-5-TR criteria, what is the minimum duration of continuous disturbance required for a formal diagnosis of schizophrenia, and how long must active-phase Criterion A symptoms persist within that period?",
        "options": [
            {"id": "A", "text": "At least 1 month of total disturbance, with at least 1 week of active-phase symptoms"},
            {"id": "B", "text": "At least 3 months of total disturbance, with at least 2 weeks of active-phase symptoms"},
            {"id": "C", "text": "At least 6 months of total disturbance, with at least 1 month of active-phase symptoms"},
            {"id": "D", "text": "At least 12 months of total disturbance, with at least 3 months of active-phase symptoms"}
        ],
        "correctAnswer": "C",
        "explanation": "DSM-5-TR Criterion C requires continuous signs of the disturbance to persist for at least 6 months. This 6-month period must include at least 1 month of symptoms that meet Criterion A (active-phase symptoms: delusions, hallucinations, disorganised speech, grossly disorganised/catatonic behaviour, negative symptoms), unless successfully treated.",
        "incorrectExplanations": {
            "A": "A duration of less than 1 month represents Brief Psychotic Disorder.",
            "B": "Disturbances persisting between 1 and 6 months are classified as Schizophreniform Disorder.",
            "C": "At least 6 months of total disturbance with 1 month of active symptoms is required for Schizophrenia.",
            "D": "12 months is not required for schizophrenia diagnosis; 6 months is the established threshold."
        },
        "learningObjective": "Identify DSM-5-TR timeline criteria differentiating schizophrenia from brief psychotic and schizophreniform disorders.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Schizophrenia Spectrum and Other Psychotic Disorders.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q218",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Intermediate",
        "questionText": "An occupational health liaison nurse is reviewing functional impairment in an outpatient recovering from a first episode of psychosis. The patient's hallucinations have remitted, but they struggle to plan daily routines, sustain working memory, and maintain processing speed. Which symptom domain best explains this enduring functional disability?",
        "options": [
            {"id": "A", "text": "Residual affective disturbance"},
            {"id": "B", "text": "Extrapyramidal motor rigidity"},
            {"id": "C", "text": "Attenuated positive psychotic symptoms"},
            {"id": "D", "text": "Neurocognitive impairment"}
        ],
        "correctAnswer": "D",
        "explanation": "Neurocognitive impairment is a core feature of schizophrenia that often predates the first psychotic episode and persists independently of positive symptom resolution. Deficits in executive functioning, working memory, attention, and processing speed are the strongest predictors of real-world community functional outcome and vocational disability.",
        "incorrectExplanations": {
            "A": "Affective disturbance may impact mood but does not explain systematic executive and working memory deficits.",
            "B": "Extrapyramidal motor signs affect physical movement rather than central cognitive architecture.",
            "C": "The scenario notes that positive symptoms have remitted; positive symptoms correlate poorly with long-term vocational functioning.",
            "D": "Neurocognitive impairment is the leading determinant of vocational and community disability."
        },
        "learningObjective": "Analyze the impact of cognitive deficits on functional rehabilitation in schizophrenia.",
        "reference": "Green, M. F., et al. (2019). Neurocognition and functional outcome in schizophrenia: Are we measuring the right things? Schizophrenia Bulletin, 45(4), 780-789.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q219",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Foundation",
        "questionText": "A 28-year-old inpatient with schizophrenia maintains an uncomfortable posture with their arm elevated against gravity for over 45 minutes without shifting, allowing the nurse to gently reposition the limb where it remains motionless like warm wax. What specific psychomotor phenomena are demonstrated?",
        "options": [
            {"id": "A", "text": "Catalepsy and waxy flexibility (flexibilitas cerea)"},
            {"id": "B", "text": "Akathisia and motor restlessness"},
            {"id": "C", "text": "Tardive dystonia and choreiform tremor"},
            {"id": "D", "text": "Gegenhalten and oppositional paratonia"}
        ],
        "correctAnswer": "A",
        "explanation": "Catalepsy is passive induction of a posture held against gravity. Waxy flexibility (flexibilitas cerea) is slight, even resistance to positioning by the examiner, with the limb remaining in the newly imposed position. Both are diagnostic signs of catatonia under DSM-5-TR.",
        "incorrectExplanations": {
            "A": "Catalepsy and waxy flexibility describe posture maintenance against gravity and mouldable resistance.",
            "B": "Akathisia is an intense subjective restlessness compelling continuous physical motion.",
            "C": "Tardive dystonia presents with involuntary muscle contractions and twisting, not static waxy resistance.",
            "D": "Gegenhalten (paratonia) is active resistance to passive movement proportional to the force applied, rather than waxy accommodation."
        },
        "learningObjective": "Recognize and document cardinal catatonic psychomotor signs in psychiatric patients.",
        "reference": "Bush, G., et al. (1996). Catatonia: I. Rating scale and standardized examination. Acta Psychiatrica Scandinavica, 93(2), 129-136.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q220",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 34-year-old woman experiences severe auditory hallucinations and persecutory delusions that persist continuously for 8 months. During this illness course, she experiences a 6-week major depressive episode and later a 4-week manic episode. For at least 3 months, she exhibited florid psychotic symptoms without any mood disturbance. Which diagnosis is most accurate?",
        "options": [
            {"id": "A", "text": "Major Depressive Disorder with Psychotic Features"},
            {"id": "B", "text": "Schizoaffective Disorder"},
            {"id": "C", "text": "Bipolar I Disorder with Mood-Incongruent Psychotic Features"},
            {"id": "D", "text": "Delusional Disorder, mixed type"}
        ],
        "correctAnswer": "B",
        "explanation": "DSM-5-TR diagnostic criteria for Schizoaffective Disorder require delusions or hallucinations for 2 or more weeks in the absence of a major mood episode (depressive or manic) during the lifetime duration of the illness, while major mood episodes are present for the majority of the total duration of the active and residual periods.",
        "incorrectExplanations": {
            "A": "In MDD with psychotic features, psychosis occurs exclusively during the mood episodes.",
            "B": "Schizoaffective disorder requires at least 2 weeks of psychotic symptoms in the absence of a major mood episode.",
            "C": "In Bipolar I with psychotic features, psychotic symptoms are confined to episodes of mania or depression.",
            "D": "Delusional disorder excludes prominent auditory hallucinations and prominent mood episodes."
        },
        "learningObjective": "Differentiate Schizoaffective Disorder from mood disorders with psychotic features.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Schizoaffective Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q221",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Advanced",
        "questionText": "A 45-year-old accountant has held a solitary fixed belief for 9 months that their spouse is unfaithful, hiring private detectives and installing hidden GPS trackers despite no supporting evidence. The individual shows no hallucinations, no thought disorganisation, dresses immaculately, maintains high professional employment, and exhibits intact social functioning outside this specific belief. What is the primary diagnosis?",
        "options": [
            {"id": "A", "text": "Paranoid Personality Disorder"},
            {"id": "B", "text": "Schizophrenia, paranoid subtype"},
            {"id": "C", "text": "Delusional Disorder, jealous type"},
            {"id": "D", "text": "Obsessive-Compulsive Disorder with poor insight"}
        ],
        "correctAnswer": "C",
        "explanation": "Delusional Disorder is characterized by the presence of one or more delusions persisting for at least 1 month. Criterion C specifies that functioning is not markedly impaired and behavior is not obviously bizarre or odd outside the specific impact of the delusion. The jealous type centers on the ungrounded conviction of partner infidelity.",
        "incorrectExplanations": {
            "A": "Paranoid Personality Disorder involves pervasive distrust and suspiciousness without a discrete, encapsulated, systematized delusion.",
            "B": "Schizophrenia involves functional decline, disorganized thought, or prominent hallucinations, which are absent here.",
            "C": "Delusional Disorder is defined by circumscribed non-bizarre delusions with preserved psychosocial functioning.",
            "D": "OCD involves ego-dystonic obsessions with compulsions recognized as excessive, unlike the unshakeable fixed conviction of delusional jealousy (Othello syndrome)."
        },
        "learningObjective": "Distinguish Delusional Disorder from Schizophrenia and personality disorders based on psychosocial functioning and symptom encapsulation.",
        "reference": "Manschreck, T. C. (2019). Delusional Disorder and Shared Psychotic Disorder. Comprehensive Textbook of Psychiatry.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q222",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Advanced",
        "questionText": "A 19-year-old student experiences sudden onset of persecutory delusions, visual illusions, and severe disorganisation 4 days after the sudden death of their parent. The symptoms resolve completely within 18 days, with full return to the premorbid level of functioning. How is this episode classified under DSM-5-TR?",
        "options": [
            {"id": "A", "text": "Schizophreniform Disorder with good prognostic features"},
            {"id": "B", "text": "Adjustment Disorder with disturbance of conduct"},
            {"id": "C", "text": "Acute Stress Disorder with dissociative symptoms"},
            {"id": "D", "text": "Brief Psychotic Disorder with marked stressor"}
        ],
        "correctAnswer": "D",
        "explanation": "Brief Psychotic Disorder involves the sudden onset of at least one positive psychotic symptom (delusions, hallucinations, disorganised speech, or grossly disorganised/catatonic behaviour) lasting at least 1 day but less than 1 month, followed by eventual full return to premorbid functioning. The presence of a severe bereavement justifies the specifier 'with marked stressor' (brief reactive psychosis).",
        "incorrectExplanations": {
            "A": "Schizophreniform disorder requires symptoms lasting at least 1 month and less than 6 months.",
            "B": "Adjustment disorder does not involve overt delusions or psychotic disorganization.",
            "C": "Acute stress disorder involves trauma-related intrusion, avoidance, and hyperarousal, not florid psychotic delusions.",
            "D": "Brief Psychotic Disorder lasts from 1 day to under 1 month with full premorbid return."
        },
        "learningObjective": "Apply diagnostic duration thresholds to identify Brief Psychotic Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Brief Psychotic Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q223",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Advanced",
        "questionText": "An Early Intervention in Psychosis (EIP) mental health nurse is evaluating a 17-year-old who reports noticing shadowy movements in peripheral vision, experiencing brief ideas that people on the bus are mocking them (which they can reality-test and dismiss), and declining academic performance over 4 months. Which clinical high-risk criteria are met?",
        "options": [
            {"id": "A", "text": "Attenuated Psychosis Syndrome / Ultra-High Risk (UHR) for psychosis"},
            {"id": "B", "text": "Brief Intermittent Psychotic Symptoms (BLIPS) meeting full psychotic threshold"},
            {"id": "C", "text": "Schizotypal Personality Disorder without risk of transition"},
            {"id": "D", "text": "Prodromal Catatonic State requiring emergency benzodiazepine titration"}
        ],
        "correctAnswer": "A",
        "explanation": "Attenuated Psychosis Syndrome (or the Ultra-High Risk / At-Risk Mental State paradigm) is characterized by subthreshold psychotic symptoms: perceptual abnormalities or persecutory ideation with preserved reality testing and insight, occurring with sufficient frequency in the past year, associated with distress or functional decline.",
        "incorrectExplanations": {
            "A": "Attenuated Psychosis Syndrome represents subthreshold symptoms with intact reality-testing.",
            "B": "BLIPS refers to full-blown psychotic symptoms that remit spontaneously within days, which is not the case here.",
            "C": "Schizotypal personality disorder represents enduring, lifelong traits rather than subacute functional decline.",
            "D": "There are no motor signs of catatonia present in this clinical presentation."
        },
        "learningObjective": "Identify Ultra-High Risk (UHR) and Attenuated Psychosis Syndrome criteria in early intervention nursing.",
        "reference": "Fusar-Poli, P., et al. (2020). The psychosis high-risk state: a comprehensive review. JAMA Psychiatry, 77(7), 755-765.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q224",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Schizophrenia Spectrum and Other Psychotic Disorders",
        "difficulty": "Expert",
        "questionText": "According to the contemporary neurochemical model of schizophrenia, which pathophysiological combination accurately links dopaminergic tract dysfunction with clinical psychopathology?",
        "options": [
            {"id": "A", "text": "Hypodopaminergic activity in the mesolimbic tract causing hallucinations, and hyperdopaminergic activity in the tuberoinfundibular tract causing avolition"},
            {"id": "B", "text": "Hyperdopaminergic activity in the mesolimbic tract mediating positive symptoms, and hypodopaminergic activity in the mesocortical tract mediating negative and cognitive symptoms"},
            {"id": "C", "text": "Hyperdopaminergic activity in the nigrostriatal tract causing paranoia, and hypodopaminergic activity in the ventral striatum causing catatonia"},
            {"id": "D", "text": "Complete shutdown of the frontostriatal dopamine loop with compensatory hyperglutamatergic NMDA overactivation across the neocortex"}
        ],
        "correctAnswer": "B",
        "explanation": "The modified dopamine hypothesis posits that positive symptoms (delusions, hallucinations) arise from hyperdopaminergic transmission in the mesolimbic pathway projecting to the ventral striatum and limbic structures. In contrast, negative and cognitive symptoms are linked to hypodopaminergic transmission in the mesocortical pathway projecting to the prefrontal cortex.",
        "incorrectExplanations": {
            "A": "Mesolimbic activity is hyperactive, not hypoactive, in positive symptoms; tuberoinfundibular dopamine controls prolactin secretion.",
            "B": "Hyperactivity in the mesolimbic tract causes positive symptoms, while hypodopaminergia in the mesocortical tract causes negative/cognitive symptoms.",
            "C": "Nigrostriatal dopamine regulates motor control, not paranoia; antagonism here produces extrapyramidal symptoms.",
            "D": "NMDA receptor hypofunction (not hyperactivation) is implicated in the glutamatergic model of schizophrenia."
        },
        "learningObjective": "Synthesize the neurochemical mechanisms and tract-specific dopaminergic abnormalities underlying schizophrenia psychopathology.",
        "reference": "Stahl, S. M. (2021). Stahl's Essential Psychopharmacology: Neuroscientific Basis and Practical Applications (5th ed.). Cambridge University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 2: Bipolar and Related Disorders (Q225 - Q234)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q225",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Foundation",
        "questionText": "According to DSM-5-TR, which criterion is strictly required to establish a definitive diagnosis of Bipolar I Disorder?",
        "options": [
            {"id": "A", "text": "At least one hypomanic episode and at least one major depressive episode"},
            {"id": "B", "text": "Persistent cyclothymic mood fluctuations spanning at least 2 consecutive years"},
            {"id": "C", "text": "At least one lifetime manic episode, regardless of whether a major depressive episode has occurred"},
            {"id": "D", "text": "At least two major depressive episodes accompanied by a family history of mania"}
        ],
        "correctAnswer": "C",
        "explanation": "For a diagnosis of Bipolar I Disorder, it is necessary to meet criteria for at least one lifetime manic episode. While major depressive episodes and hypomanic episodes are common in Bipolar I Disorder, they are not strictly required for the formal diagnosis.",
        "incorrectExplanations": {
            "A": "A hypomanic episode paired with a major depressive episode (without a manic episode) defines Bipolar II Disorder.",
            "B": "Persistent subthreshold fluctuations define Cyclothymic Disorder.",
            "C": "At least one lifetime manic episode is the sole mandatory requirement for Bipolar I Disorder.",
            "D": "Family history and depressive episodes alone cannot establish Bipolar I without an experienced manic episode."
        },
        "learningObjective": "Identify core DSM-5-TR diagnostic criteria for Bipolar I Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Bipolar and Related Disorders.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q226",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Foundation",
        "questionText": "The clinical mnemonic 'DIGFAST' is widely used by mental health nurses during assessment of acute mania. Which cluster of symptoms does this mnemonic correctly represent?",
        "options": [
            {"id": "A", "text": "Delusions, Insomnia, Guilt, Fatigue, Agitation, Suicidality, Tardive movements"},
            {"id": "B", "text": "Dissociation, Impulsivity, Grandiosity, Flat affect, Anhedonia, Somatisation, Tremor"},
            {"id": "C", "text": "Depression, Irritability, Grief, Fear, Anorexia, Stupor, Thought blocking"},
            {"id": "D", "text": "Distractibility, Indiscretion, Grandiosity, Flight of ideas, Activity increase, Sleep deficit, Talkativeness"}
        ],
        "correctAnswer": "D",
        "explanation": "DIGFAST is the validated mnemonic for DSM-5 manic episode symptoms: Distractibility, Indiscretion (excessive involvement in risky activities), Grandiosity (inflated self-esteem), Flight of ideas (racing thoughts), Activity increase (goal-directed or psychomotor agitation), Sleep deficit (decreased need for sleep), and Talkativeness (pressured speech).",
        "incorrectExplanations": {
            "A": "Guilt, fatigue, and suicidality are depressive criteria, not manic criteria.",
            "B": "Flat affect and anhedonia are negative/depressive symptoms.",
            "C": "Grief, anorexia, and stupor do not correspond to the DIGFAST manic criteria.",
            "D": "DIGFAST represents Distractibility, Indiscretion, Grandiosity, Flight of ideas, Activity increase, Sleep deficit, and Talkativeness."
        },
        "learningObjective": "Utilize the DIGFAST mnemonic to perform systematic clinical assessments of manic states.",
        "reference": "Carlat, D. J. (2017). The Psychiatric Interview (4th ed.). Wolters Kluwer.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q227",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Foundation",
        "questionText": "A 31-year-old graphic designer presents with 5 days of elevated mood, uncharacteristic energy, sleeping only 4 hours nightly while feeling fully refreshed, and increased creative productivity. Friends notice they are more sociable and talkative, but there are no delusions, no hallucinations, no marked impairment in social or occupational functioning, and no need for hospitalisation. How is this state categorized?",
        "options": [
            {"id": "A", "text": "Hypomanic episode"},
            {"id": "B", "text": "Full manic episode"},
            {"id": "C", "text": "Mixed manic episode"},
            {"id": "D", "text": "Euthymic baseline with hyperthymic personality traits"}
        ],
        "correctAnswer": "A",
        "explanation": "A hypomanic episode lasts at least 4 consecutive days and involves an observable change in functioning with elevated/irritable mood and increased energy. Crucially, hypomania is not severe enough to cause marked impairment in social or occupational functioning, does not necessitate hospitalisation, and lacks psychotic features.",
        "incorrectExplanations": {
            "A": "Hypomania involves elevated mood lasting >= 4 days without marked functional disruption, hospitalisation, or psychosis.",
            "B": "A full manic episode requires at least 7 days (or any duration if hospitalisation is required) and causes marked functional impairment.",
            "C": "Mixed manic episodes require concurrent depressive symptoms, which are not present here.",
            "D": "The distinct 5-day change from baseline with reduced sleep need distinguishes this from static personality traits."
        },
        "learningObjective": "Differentiate hypomanic from manic episodes based on duration, severity, and absence of psychosis.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Hypomanic Episode criteria.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q228",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 26-year-old law clerk describes a 3-year history of unpredictable mood instability. For several weeks at a time, they experience mild depressive symptoms (low energy, pessimism, hypersomnia), alternating with periods of mild hypomanic symptoms (hyperactivity, decreased sleep need, increased self-confidence). They have never met the full criteria for a Major Depressive Episode or a Manic Episode, and symptoms have not remitted for more than 2 months at a time. What is the diagnosis?",
        "options": [
            {"id": "A", "text": "Bipolar I Disorder, current episode depressed"},
            {"id": "B", "text": "Cyclothymic Disorder"},
            {"id": "C", "text": "Borderline Personality Disorder"},
            {"id": "D", "text": "Persistent Depressive Disorder with anxious distress"}
        ],
        "correctAnswer": "B",
        "explanation": "Cyclothymic Disorder requires at least 2 years (1 year in children/adolescents) of numerous periods with hypomanic symptoms that do not meet criteria for a hypomanic episode and numerous periods with depressive symptoms that do not meet criteria for a major depressive episode, without being symptom-free for more than 2 consecutive months.",
        "incorrectExplanations": {
            "A": "Bipolar I requires at least one full manic episode, which has never occurred here.",
            "B": "Cyclothymic Disorder is defined by chronic subthreshold mood fluctuations for at least 2 years.",
            "C": "Borderline Personality Disorder features rapid affective shifts over hours triggered by interpersonal stressors, rather than sustained episodic fluctuations over weeks.",
            "D": "Persistent Depressive Disorder does not account for the distinct hypomanic symptom phases."
        },
        "learningObjective": "Recognize the diagnostic parameters and longitudinal course of Cyclothymic Disorder.",
        "reference": "Vieta, E., et al. (2018). Bipolar disorders. Nature Reviews Disease Primers, 4, 18008.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q229",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Advanced",
        "questionText": "A 40-year-old patient admitted with acute mania exhibits racing thoughts, continuous pressured speech, and grandiose ideas of divine mission. Simultaneously, they weep uncontrollably, express intense feelings of worthlessness, and state that life is not worth living. Which diagnostic specifier applies, and what is the primary clinical safety implication?",
        "options": [
            {"id": "A", "text": "With rapid cycling; heightened risk of neuroleptic malignant syndrome"},
            {"id": "B", "text": "With melancholic features; heightened risk of catatonic stupor"},
            {"id": "C", "text": "With mixed features; markedly elevated risk of completed suicide"},
            {"id": "D", "text": "With atypical features; high risk of severe metabolic dysregulation"}
        ],
        "correctAnswer": "C",
        "explanation": "The 'with mixed features' specifier applies when a manic episode includes at least 3 depressive symptoms (such as dysphoria, worthlessness, suicidality) or vice versa. The combination of high psychomotor energy, impulsivity, and severe depressive despair makes mixed states the highest-risk phase for completed suicide in bipolar disorder.",
        "incorrectExplanations": {
            "A": "Rapid cycling refers to episode frequency over 12 months, not concurrent opposite-pole symptoms within an episode.",
            "B": "Melancholic features require loss of pleasure and lack of mood reactivity, not concurrent manic hyperactivity.",
            "C": "Mixed features combine manic psychomotor agitation with depressive hopelessness, creating an exceptionally high suicide risk.",
            "D": "Atypical features refer to hypersomnia and hyperphagia in depression, not mixed manic-depressive presentations."
        },
        "learningObjective": "Evaluate the clinical presentation and acute suicide risk associated with bipolar mixed features.",
        "reference": "McIntyre, R. S., et al. (2017). The DSM-5 mixed specifier in bipolar disorder. Journal of Affective Disorders, 219, 110-116.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q230",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Intermediate",
        "questionText": "A mental health nurse evaluates a 38-year-old female patient with Bipolar II Disorder who has experienced two hypomanic episodes and two major depressive episodes over the preceding 10 months, each demarcated by partial remission. Which clinical course specifier is indicated?",
        "options": [
            {"id": "A", "text": "Continuous cycling mood dysregulation"},
            {"id": "B", "text": "Ultradian cycling bipolar illness"},
            {"id": "C", "text": "Refractory affective cycling"},
            {"id": "D", "text": "Rapid cycling specifier"}
        ],
        "correctAnswer": "D",
        "explanation": "The DSM-5-TR 'rapid cycling' specifier requires at least 4 mood episodes (major depressive, manic, or hypomanic) within the previous 12 months. The episodes must be demarcated either by partial or full remission for at least 2 months or by a switch to an episode of opposite polarity.",
        "incorrectExplanations": {
            "A": "Continuous cycling is not a standard DSM-5-TR diagnostic specifier.",
            "B": "Ultradian cycling describes fluctuations within a 24-hour cycle and is not an official DSM specifier.",
            "C": "Refractory cycling is not a standardized DSM-5-TR terminology.",
            "D": "Rapid cycling is formally defined as 4 or more mood episodes within a 12-month timeframe."
        },
        "learningObjective": "Identify criteria for the rapid cycling specifier in bipolar disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Bipolar Disorder Specifiers.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q231",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Advanced",
        "questionText": "An acutely manic patient on an inpatient psychiatric unit paces the corridors continuously, intrudes into other patients' bedrooms, shouts loudly, and has not eaten or rested for 18 hours. What is the priority nursing intervention?",
        "options": [
            {"id": "A", "text": "Reduce environmental stimuli, provide portable high-calorie finger foods and fluids, and set calm, firm behavioral boundaries"},
            {"id": "B", "text": "Engage the patient in competitive unit games and large group therapy to channel their excess energy"},
            {"id": "C", "text": "Place the patient in mechanical restraints immediately to enforce complete physical bedrest"},
            {"id": "D", "text": "Confront the patient's grandiose delusions firmly in front of peers to break through their lack of insight"}
        ],
        "correctAnswer": "A",
        "explanation": "Priority nursing management for acute mania focuses on physical safety, meeting basic physiological needs (nutrition and hydration through high-calorie, portable finger foods and fluids), minimizing sensory stimulation (quiet room, low lighting), and establishing clear, consistent, non-punitive limits without confrontational power struggles.",
        "incorrectExplanations": {
            "A": "Providing finger foods, reducing stimuli, and calm limit-setting maintain physiological stability and safety.",
            "B": "Competitive group activities overstimulate manic patients and provoke severe agitation or verbal conflict.",
            "C": "Restraints are restrictive last-resort measures indicated only for imminent physical danger when all de-escalation fails.",
            "D": "Confronting grandiose beliefs provokes hostility, paranoia, and behavioral escalation."
        },
        "learningObjective": "Formulate evidence-based nursing care priorities for acute manic exhaustion and behavioral dysregulation.",
        "reference": "Townsend, M. C., & Morgan, K. I. (2020). Psychiatric Mental Health Nursing: Concepts of Care in Evidence-Based Practice (10th ed.). F.A. Davis.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q232",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Advanced",
        "questionText": "A 24-year-old patient presenting with a severe first episode of depression is prescribed citalopram monotherapy by a general practitioner. Ten days later, the community psychiatric nurse finds the patient euphoric, speaking at breakneck speed, engaging in reckless online shopping, and not sleeping. What clinical issue does this scenario highlight?",
        "options": [
            {"id": "A", "text": "Serotonin syndrome resulting from citalopram toxicity"},
            {"id": "B", "text": "Antidepressant-induced manic switch revealing an underlying bipolar disorder"},
            {"id": "C", "text": "Paradoxical citalopram akathisia with pseudomania"},
            {"id": "D", "text": "Acute anticholinergic delirium secondary to SSRI accumulation"}
        ],
        "correctAnswer": "B",
        "explanation": "Antidepressant monotherapy in patients with undetected bipolar diathesis can trigger a treatment-emergent manic switch or destabilize mood into rapid cycling. Under DSM-5-TR, if a full manic episode emerges during antidepressant treatment and persists at a syndromal level beyond the physiological effect of the drug, a diagnosis of Bipolar I Disorder is warranted.",
        "incorrectExplanations": {
            "A": "Serotonin syndrome presents with autonomic instability, hyperreflexia, clonus, and hyperthermia, not pure euphoric mania.",
            "B": "Antidepressant monotherapy can precipitate manic switches in unrecognized bipolar illness.",
            "C": "Akathisia causes motor restlessness and subjective distress, not grandiosity and euphoric mood.",
            "D": "SSRIs do not possess meaningful anticholinergic activity to cause anticholinergic delirium."
        },
        "learningObjective": "Recognize the risk of antidepressant-induced manic switching and the importance of screening for bipolar disorder prior to antidepressant monotherapy.",
        "reference": "Pacchiarotti, I., et al. (2013). The International Society for Bipolar Disorders (ISBD) task force report on antidepressant use in bipolar disorders. American Journal of Psychiatry, 170(11), 1249-1262.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q233",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Advanced",
        "questionText": "A 56-year-old patient with no prior personal or family psychiatric history develops sudden euphoria, flight of ideas, hyperactivity, and grandiosity 5 days after initiating high-dose oral prednisolone for an acute autoimmune flare. Which diagnostic category is most appropriate?",
        "options": [
            {"id": "A", "text": "Late-onset Bipolar I Disorder, manic episode"},
            {"id": "B", "text": "Schizoaffective Disorder, bipolar type"},
            {"id": "C", "text": "Substance/Medication-Induced Bipolar and Related Disorder"},
            {"id": "D", "text": "Delirium Tremens with euphoric affect"}
        ],
        "correctAnswer": "C",
        "explanation": "When manic symptoms develop during or soon after exposure to a medication known to cause mood alteration (such as corticosteroids, dopaminergic agonists, or stimulants) in an individual without prior mood history, the diagnosis is Substance/Medication-Induced Bipolar and Related Disorder.",
        "incorrectExplanations": {
            "A": "Primary Bipolar I rarely presents de novo at age 56 without previous affective episodes and in the presence of an obvious causative pharmacologic agent.",
            "B": "Schizoaffective disorder requires persistent psychotic symptoms independent of mood episodes and cannot be attributed to substance effects.",
            "C": "Substance/Medication-Induced Bipolar Disorder accounts for corticosteroid-induced manic presentations.",
            "D": "Delirium tremens occurs on alcohol withdrawal and presents with visual hallucinations, severe autonomic tremor, and clouding of consciousness."
        },
        "learningObjective": "Differentiate secondary substance/medication-induced mania from primary idiopathic bipolar disorder.",
        "reference": "Brown, E. S., & Chandler, P. A. (2001). Mood and cognitive changes during systemic corticosteroid therapy. Primary Care Companion JCP, 3(1), 17-21.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q234",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Bipolar and Related Disorders",
        "difficulty": "Expert",
        "questionText": "Which neurobiological model explains why untreated bipolar mood episodes tend to become more frequent, severe, and spontaneous over time, with progressive cognitive attrition and diminished responsiveness to mood-stabilising pharmacotherapy?",
        "options": [
            {"id": "A", "text": "The default mode network deactivation hypothesis"},
            {"id": "B", "text": "The hypothalamic-pituitary-adrenal exhaustion paradigm"},
            {"id": "C", "text": "The neurotrophin hypersecretion feedback cascade"},
            {"id": "D", "text": "The kindling and neuroprogression hypothesis"}
        ],
        "correctAnswer": "D",
        "explanation": "Post's kindling hypothesis posits that early affective episodes are typically triggered by psychosocial stressors; however, repeated untreated episodes induce neurobiological alterations (kindling) that lower the threshold for subsequent episodes, eventually causing episodes to occur autonomously and spontaneously. This neuroprogression correlates with prefrontal grey matter volume loss and treatment resistance.",
        "incorrectExplanations": {
            "A": "Default mode network alterations relate to rumination and resting connectivity, not longitudinal episode sensitization.",
            "B": "HPA axis hyperactivity occurs in stress and mood disorders, but does not formulate the progressive kindling cascade.",
            "C": "Neurotrophic factors like BDNF are decreased, not hypersecreted, during acute mood episodes.",
            "D": "The kindling and neuroprogression model explains episode acceleration and treatment resistance in recurrent affective disorders."
        },
        "learningObjective": "Analyze the neurobiological concept of kindling and clinical neuroprogression in recurrent bipolar illness.",
        "reference": "Post, R. M. (2007). Kindling and sensitization as models for affective episode recurrence, cyclicity, and progression. Progress in Neuro-Psychopharmacology and Biological Psychiatry, 31(4), 858-873.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 3: Depressive Disorders (Q235 - Q244)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q235",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Foundation",
        "questionText": "Under DSM-5-TR, how many symptom criteria must be present for at least what minimum time period to diagnose a Major Depressive Episode, and which specific symptom must be among them?",
        "options": [
            {"id": "A", "text": "At least 5 of 9 symptoms for at least 2 weeks; must include depressed mood or loss of interest/pleasure (anhedonia)"},
            {"id": "B", "text": "At least 4 of 8 symptoms for at least 4 weeks; must include insomnia or suicidal thoughts"},
            {"id": "C", "text": "At least 3 of 7 symptoms for at least 1 month; must include fatigue or feelings of worthlessness"},
            {"id": "D", "text": "At least 6 of 10 symptoms for at least 6 months; must include psychomotor agitation and poor concentration"}
        ],
        "correctAnswer": "A",
        "explanation": "DSM-5-TR Criterion A for Major Depressive Disorder requires at least 5 of 9 symptoms present during the same 2-week period representing a change from previous functioning. At least one of the symptoms must be either (1) depressed mood or (2) loss of interest or pleasure (anhedonia).",
        "incorrectExplanations": {
            "A": "At least 5 of 9 symptoms for >= 2 weeks, including depressed mood or anhedonia, is the DSM-5-TR requirement.",
            "B": "4 weeks is not the minimum duration; 2 weeks is the threshold, and insomnia/suicidality are not mandatory gateway criteria.",
            "C": "1 month is not required, and fatigue/worthlessness cannot serve as the sole mandatory gateway symptom.",
            "D": "6 months is the duration criterion for GAD or dysthymia/chronic courses, not acute major depressive episode."
        },
        "learningObjective": "Define the core diagnostic criteria and gateway requirements for Major Depressive Episode.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Major Depressive Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q236",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Foundation",
        "questionText": "The clinical mnemonic 'SIG E CAPS' is widely utilized in mental status evaluations to identify symptoms of major depression. What does the letter 'G' in this mnemonic represent?",
        "options": [
            {"id": "A", "text": "Gastrointestinal disturbances"},
            {"id": "B", "text": "Guilt and feelings of worthlessness"},
            {"id": "C", "text": "Grandiosity in thought content"},
            {"id": "D", "text": "Gait and motor unsteadiness"}
        ],
        "correctAnswer": "B",
        "explanation": "SIG E CAPS stands for Sleep disturbance, Interest loss (anhedonia), Guilt/worthlessness, Energy loss/fatigue, Concentration deficits, Appetite/weight changes, Psychomotor retardation/agitation, and Suicidal ideation. The letter 'G' specifically denotes Guilt.",
        "incorrectExplanations": {
            "A": "Gastrointestinal signs may occur somatically but are not the specific 'G' criterion in SIG E CAPS.",
            "B": "Guilt and excessive feelings of worthlessness represent the 'G' in SIG E CAPS.",
            "C": "Grandiosity is a manic criterion (part of DIGFAST), not depression.",
            "D": "Gait unsteadiness is a neurological/motor sign, not a depressive diagnostic criterion."
        },
        "learningObjective": "Apply the SIG E CAPS mnemonic accurately during clinical assessment of depressive psychopathology.",
        "reference": "Carlat, D. J. (2017). The Psychiatric Interview (4th ed.). Wolters Kluwer.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q237",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 29-year-old patient diagnosed with Major Depressive Disorder reports that their mood temporarily brightens in response to positive external events. They also describe sleeping 12 hours a day (hypersomnia), ravenous appetite with a 5 kg weight gain, heavy leaden sensations in their limbs, and long-standing severe sensitivity to perceived interpersonal rejection. Which specifier is indicated?",
        "options": [
            {"id": "A", "text": "With melancholic features"},
            {"id": "B", "text": "With catatonic features"},
            {"id": "C", "text": "With atypical features"},
            {"id": "D", "text": "With anxious distress"}
        ],
        "correctAnswer": "C",
        "explanation": "The 'with atypical features' specifier requires mood reactivity (mood brightens in response to positive events) plus at least two of the following: significant weight gain or increase in appetite, hypersomnia, leaden paralysis (heavy feeling in arms or legs), and long-standing interpersonal rejection sensitivity.",
        "incorrectExplanations": {
            "A": "Melancholic features involve complete lack of mood reactivity, early morning awakening, anorexia/weight loss, and excessive guilt.",
            "B": "Catatonic features involve stupor, mutism, posturing, or catalepsy.",
            "C": "Atypical features include mood reactivity, hyperphagia, hypersomnia, leaden paralysis, and rejection sensitivity.",
            "D": "Anxious distress involves tension, restlessness, worry, and fear of impending doom without the specific vegetative reversal signs."
        },
        "learningObjective": "Differentiate atypical depression from melancholic depression based on vegetative symptoms and mood reactivity.",
        "reference": "Stewart, J. W., et al. (2010). Atypical depression: a valid subtype? Dialogues in Clinical Neuroscience, 12(4), 499-514.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q238",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 68-year-old patient admitted with severe depression insists that their internal organs have completely rotted away, that they possess no blood, and that their family is destitute because of their moral failures. What specific psychopathological phenomenon is this patient exhibiting?",
        "options": [
            {"id": "A", "text": "Capgras syndrome with persecutory delusion"},
            {"id": "B", "text": "Erotomanic delusions with somatisation"},
            {"id": "C", "text": "Delusion of thought insertion"},
            {"id": "D", "text": "Mood-congruent nihilistic delusion (Cotard's syndrome)"}
        ],
        "correctAnswer": "D",
        "explanation": "Cotard's syndrome (delire de negation) is a severe nihilistic delusion often seen in psychotic depression where patients believe they have lost organs, blood, or body parts, or that they are dead or non-existent. These delusions are mood-congruent because their content aligns directly with depressive themes of decay, guilt, and destruction.",
        "incorrectExplanations": {
            "A": "Capgras delusion is the fixed belief that a familiar person has been replaced by an identical imposter.",
            "B": "Erotomanic delusions involve the false belief that another person, usually of higher status, is in love with the patient.",
            "C": "Thought insertion is the belief that thoughts are being placed directly into the mind from an external agency.",
            "D": "Cotard's syndrome is a classic mood-congruent nihilistic delusion characterized by beliefs of organ rot, non-existence, or putrefaction."
        },
        "learningObjective": "Identify and document Cotard's delusion and mood-congruent psychotic features in severe depression.",
        "reference": "Berrios, G. E., & Luque, R. (1995). Cotard's syndrome: analysis of 100 cases. Acta Psychiatrica Scandinavica, 91(3), 185-188.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q239",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Foundation",
        "questionText": "A 35-year-old patient reports feeling chronically down, unmotivated, and fatigued for the past 3 years. They state, 'I cannot remember the last time I felt truly happy; it has been like this constantly.' They have never been free of depressive symptoms for more than 6 weeks at a time, though they have managed to work. Which diagnosis best fits this clinical picture?",
        "options": [
            {"id": "A", "text": "Cyclothymic Disorder"},
            {"id": "B", "text": "Persistent Depressive Disorder (Dysthymia)"},
            {"id": "C", "text": "Bipolar II Disorder"},
            {"id": "D", "text": "Major Depressive Disorder, single episode, in partial remission"}
        ],
        "correctAnswer": "B",
        "explanation": "Persistent Depressive Disorder (Dysthymia) is characterized by a depressed mood for most of the day, for more days than not, for at least 2 years in adults (1 year in children/adolescents). During this 2-year period, the individual has never been symptom-free for more than 2 months at a time.",
        "incorrectExplanations": {
            "A": "Cyclothymic disorder requires alternating periods of hypomanic symptoms, which are absent here.",
            "B": "Persistent Depressive Disorder requires at least 2 years of chronic depressive symptoms without > 2 months remission.",
            "C": "Bipolar II requires at least one hypomanic episode and one major depressive episode.",
            "D": "Partial remission implies a resolved acute episode rather than continuous 3-year chronicity."
        },
        "learningObjective": "Differentiate Persistent Depressive Disorder (Dysthymia) from episodic Major Depressive Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Persistent Depressive Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q240",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Intermediate",
        "questionText": "A perinatal mental health nurse is evaluating a mother 8 days postpartum. The patient exhibits extreme sleeplessness, rapid mood shifts, confusion, auditory hallucinations instructing her to 'save the infant from demonic forces,' and delusional beliefs that the infant is possessed. What is the immediate diagnostic classification and clinical priority?",
        "options": [
            {"id": "A", "text": "Postpartum 'baby blues'; provide reassurance, psychoeducation, and routine discharge"},
            {"id": "B", "text": "Postpartum anxiety; initiate low-dose buspirone and schedule home visits next week"},
            {"id": "C", "text": "Postpartum Psychosis; treat as a psychiatric emergency requiring immediate mother-infant safety precautions and psychiatric admission"},
            {"id": "D", "text": "Generalised Infanticidal Obsessive-Compulsive Disorder; provide outpatient exposure therapy"}
        ],
        "correctAnswer": "C",
        "explanation": "Postpartum psychosis (typically with onset in the first 1-2 weeks after delivery) is a severe psychiatric emergency with high risks of suicide and infanticide (often driven by altruistic or command delusions). Immediate psychiatric hospitalisation (ideally in a specialised Mother and Baby Unit) and constant supervised safety monitoring are mandatory.",
        "incorrectExplanations": {
            "A": "Baby blues occurs in up to 80% of women, is mild, transient (resolves by day 10-14), and never involves hallucinations or delusions.",
            "B": "Postpartum anxiety involves worry without psychotic command hallucinations or infanticidal delusional beliefs.",
            "C": "Postpartum psychosis is an acute psychiatric emergency carrying imminent risk of infant harm and completed suicide.",
            "D": "Postpartum OCD obsessions are ego-dystonic and horrific to the patient without delusions or psychotic detachment from reality."
        },
        "learningObjective": "Differentiate postpartum psychosis from postpartum blues and establish urgent perinatal safety priorities.",
        "reference": "Jones, I., et al. (2014). Post-partum psychosis: clinical features, management and treatment. British Journal of Psychiatry, 204(4), 263-268.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q241",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Advanced",
        "questionText": "A 32-year-old woman presents with severe mood lability, marked irritability, interpersonal conflict, lethargy, breast tenderness, and bloating that emerge consistently during the final week before menses onset, improving within a few days after onset of menses, and becoming minimal or absent post-menses. This pattern is confirmed across prospective daily symptom ratings over 2 consecutive cycles. What is the diagnosis?",
        "options": [
            {"id": "A", "text": "Premenstrual Exacerbation of Bipolar Disorder"},
            {"id": "B", "text": "Rapid-cycling Cyclothymic Disorder"},
            {"id": "C", "text": "Premenstrual Syndrome (PMS) without psychiatric significance"},
            {"id": "D", "text": "Premenstrual Dysphoric Disorder (PMDD)"}
        ],
        "correctAnswer": "D",
        "explanation": "Premenstrual Dysphoric Disorder (PMDD) requires at least 5 symptoms in the final week before onset of menses that start to improve within a few days after onset and become minimal in the week post-menses. Symptoms must include marked affective lability, irritability, depressed mood, or anxiety, plus physical/cognitive symptoms, confirmed prospectively over at least 2 symptomatic cycles.",
        "incorrectExplanations": {
            "A": "Premenstrual exacerbation refers to pre-existing mood disorders worsening in the luteal phase without an asymptomatic follicular phase.",
            "B": "Cyclothymia is not cyclically tied to the endocrine menstrual cycle phases.",
            "C": "PMS involves mild somatic or emotional symptoms that do not meet the syndromal psychiatric severity or functional impairment of PMDD.",
            "D": "PMDD is diagnosed when prospective tracking confirms luteal-phase affective and physical symptoms that remit post-menses."
        },
        "learningObjective": "Apply DSM-5-TR diagnostic criteria and prospective tracking requirements for Premenstrual Dysphoric Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Premenstrual Dysphoric Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q242",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Advanced",
        "questionText": "During a suicide risk assessment using the Columbia-Suicide Severity Rating Scale (C-SSRS), a patient states: 'I wish I could fall asleep and never wake up, but I would never actually take pills or hurt myself because my children need me.' How should the nurse categorise this ideation on the C-SSRS hierarchy?",
        "options": [
            {"id": "A", "text": "Passive suicidal ideation (wish to be dead) without active suicidal thoughts, intent, or plan"},
            {"id": "B", "text": "Active suicidal ideation with specific plan and explicit intent"},
            {"id": "C", "text": "Preparatory acts and suicidal behaviour"},
            {"id": "D", "text": "Aborted suicide attempt with protective ambivalence"}
        ],
        "correctAnswer": "A",
        "explanation": "On the C-SSRS, wishing to fall asleep and not wake up, or wishing to be dead without active thoughts of killing oneself, represents Level 1: 'Wish to be dead' (passive suicidal ideation). Because the patient expressly denies active suicidal thoughts, intent, or methods and cites protective factors, it lacks active ideation.",
        "incorrectExplanations": {
            "A": "Level 1 on C-SSRS represents passive ideation ('wish to be dead') without active thoughts, method, intent, or plan.",
            "B": "Active ideation with intent and plan represents C-SSRS Level 4 or 5.",
            "C": "Preparatory acts involve concrete behaviors such as acquiring pills, writing a note, or giving away possessions.",
            "D": "An aborted attempt occurs when an individual begins the process of self-harm but stops before potential injury occurs."
        },
        "learningObjective": "Accurately categorize suicidal thoughts and behavior using the C-SSRS framework.",
        "reference": "Posner, K., et al. (2011). The Columbia-Suicide Severity Rating Scale: initial validity and internal consistency. American Journal of Psychiatry, 168(12), 1266-1277.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q243",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Advanced",
        "questionText": "A newly admitted inpatient with severe depression and active suicidal ideation is asked by a junior nurse to sign a 'no-suicide contract.' Why does contemporary psychiatric nursing evidence discourage relying on no-suicide contracts, and what is recommended instead?",
        "options": [
            {"id": "A", "text": "They carry legal liability that prevents rapid hospital discharge; verbal agreements should be used instead"},
            {"id": "B", "text": "They increase anxiety by forcing patients to think about death; suicide assessment should be avoided during the first 48 hours"},
            {"id": "C", "text": "They lack empirical evidence for preventing suicide and provide false clinical reassurance; a collaborative Stanley-Brown Safety Plan should be co-created instead"},
            {"id": "D", "text": "They are only valid for outpatient settings; inpatient settings require mandatory 24-hour solitary observation"}
        ],
        "correctAnswer": "C",
        "explanation": "Clinical evidence and international guidelines show that 'contracts for safety' / 'no-suicide contracts' do not reduce suicide rates, have no legal validity, and create a false sense of security. Modern evidence-based practice mandates the use of collaborative Safety Planning Interventions (such as the Stanley-Brown model) that identify personalized warning signs, internal coping strategies, social contacts, and lethal means restriction.",
        "incorrectExplanations": {
            "A": "Verbal agreements share the same fundamental clinical flaws as written contracts.",
            "B": "Thorough suicide risk assessment must never be avoided; assessing suicide does not induce suicidal behavior.",
            "C": "Contracts for safety lack efficacy; collaborative safety planning with means restriction is the gold standard.",
            "D": "Solitary confinement/isolation increases distress and suicide risk rather than providing therapeutic care."
        },
        "learningObjective": "Critique the use of no-suicide contracts and apply evidence-based collaborative safety planning.",
        "reference": "Stanley, B., & Brown, G. K. (2012). Safety planning intervention: a brief intervention to mitigate suicide risk. Cognitive and Behavioral Practice, 19(2), 256-264.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q244",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Depressive Disorders",
        "difficulty": "Expert",
        "questionText": "A 45-year-old patient with Treatment-Resistant Depression (TRD) has failed adequate trials of escitalopram, venlafaxine, and lithium augmentation. When evaluating advanced therapeutic options, which intervention demonstrates the most rapid onset of antidepressant efficacy (within 2 to 24 hours) via NMDA receptor antagonism?",
        "options": [
            {"id": "A", "text": "Repetitive Transcranial Magnetic Stimulation (rTMS)"},
            {"id": "B", "text": "Vagus Nerve Stimulation (VNS)"},
            {"id": "C", "text": "Tranylcypromine monotherapy"},
            {"id": "D", "text": "Intranasal esketamine / intravenous ketamine"}
        ],
        "correctAnswer": "D",
        "explanation": "Ketamine (intravenous) and its S-enantiomer esketamine (intranasal) act as non-competitive N-methyl-D-aspartate (NMDA) receptor antagonists, triggering a rapid release of glutamate, stimulating AMPA receptors, and upregulating brain-derived neurotrophic factor (BDNF). This leads to synaptogenesis and dramatic reductions in depressive symptoms and suicidal ideation within 2 to 24 hours.",
        "incorrectExplanations": {
            "A": "rTMS requires daily sessions across 4 to 6 weeks to achieve therapeutic antidepressant response.",
            "B": "Vagus Nerve Stimulation requires months of surgical implantation and gradual titration to show efficacy.",
            "C": "MAOIs require several weeks of dosing and strict dietary washout periods.",
            "D": "Ketamine/esketamine uniquely produces rapid-onset antidepressant effects within hours via NMDA receptor antagonism."
        },
        "learningObjective": "Evaluate the neurobiological mechanism and rapid onset of NMDA antagonists in treatment-resistant depression.",
        "reference": "Popova, V., et al. (2019). Efficacy and safety of flexibly dosed esketamine nasal spray combined with a newly initiated oral antidepressant in treatment-resistant depression: TRANSFORM-2. American Journal of Psychiatry, 176(6), 428-438.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 4: Anxiety Disorders (Q245 - Q254)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q245",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Foundation",
        "questionText": "To meet DSM-5-TR diagnostic criteria for Generalized Anxiety Disorder (GAD), an adult must exhibit excessive anxiety and worry occurring more days than not for at least what duration, accompanied by at least how many physical or cognitive symptoms?",
        "options": [
            {"id": "A", "text": "At least 6 months; accompanied by at least 3 of 6 physical/cognitive symptoms"},
            {"id": "B", "text": "At least 1 month; accompanied by at least 4 of 8 panic symptoms"},
            {"id": "C", "text": "At least 3 months; accompanied by at least 2 of 5 autonomic symptoms"},
            {"id": "D", "text": "At least 12 months; accompanied by at least 5 of 9 depressive symptoms"}
        ],
        "correctAnswer": "A",
        "explanation": "DSM-5-TR criteria for GAD require excessive anxiety and worry occurring more days than not for at least 6 months about a number of events or activities. The individual finds it difficult to control the worry, and in adults, it must be associated with at least 3 of the following 6 symptoms: restlessness, easily fatigued, difficulty concentrating, irritability, muscle tension, and sleep disturbance.",
        "incorrectExplanations": {
            "A": "GAD requires at least 6 months of uncontrollable worry accompanied by at least 3 of 6 specified symptoms in adults.",
            "B": "1 month with panic symptoms defines panic disorder or acute stress reactions.",
            "C": "3 months is insufficient for GAD; the DSM-5-TR standard is 6 months.",
            "D": "12 months is not required; the 6-month threshold is diagnostic."
        },
        "learningObjective": "Identify DSM-5-TR diagnostic criteria and symptom thresholds for Generalized Anxiety Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Generalized Anxiety Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q246",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Foundation",
        "questionText": "A 27-year-old accountant experiences sudden surges of overwhelming fear accompanied by palpitations, sweating, shortness of breath, and chest tightness that peak within minutes. What additional criterion must be present for at least 1 month following at least one of these attacks to establish a diagnosis of Panic Disorder?",
        "options": [
            {"id": "A", "text": "Development of prominent visual and command auditory hallucinations"},
            {"id": "B", "text": "Persistent concern about having additional panic attacks or significant maladaptive change in behaviour related to the attacks"},
            {"id": "C", "text": "Consistent daily elevations in morning salivary cortisol levels"},
            {"id": "D", "text": "Complete social withdrawal meeting criteria for Agoraphobia"}
        ],
        "correctAnswer": "B",
        "explanation": "Panic Disorder requires recurrent unexpected panic attacks where at least one attack has been followed by 1 month (or more) of one or both of: (1) persistent concern or worry about additional panic attacks or their consequences (e.g., losing control, heart attack), and/or (2) a significant maladaptive change in behavior related to the attacks (e.g., avoiding exercise or unfamiliar situations).",
        "incorrectExplanations": {
            "A": "Hallucinations are psychotic symptoms that exclude an uncomplicated anxiety disorder.",
            "B": "Persistent worry about future attacks or maladaptive behavioral avoidance for at least 1 month is mandatory.",
            "C": "Biochemical markers like cortisol are not part of DSM-5-TR diagnostic criteria.",
            "D": "Agoraphobia is a separate diagnosis in DSM-5-TR and is not required to diagnose Panic Disorder."
        },
        "learningObjective": "Define the cognitive and behavioral criteria required to diagnose Panic Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Panic Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q247",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 22-year-old university student avoids speaking in seminars, eating in cafeterias, and attending social gatherings because of an intense fear that they will humiliate themselves, sweat visibly, or be negatively judged as foolish. When forced into these situations, they endure them with extreme distress. This pattern has persisted for 8 months. What is the diagnosis?",
        "options": [
            {"id": "A", "text": "Agoraphobia without panic attacks"},
            {"id": "B", "text": "Schizoid Personality Disorder"},
            {"id": "C", "text": "Social Anxiety Disorder (Social Phobia)"},
            {"id": "D", "text": "Avoidant Personality Disorder with catatonia"}
        ],
        "correctAnswer": "C",
        "explanation": "Social Anxiety Disorder (Social Phobia) is characterized by marked fear or anxiety about one or more social situations in which the individual is exposed to possible scrutiny by others (e.g., social interactions, being observed, performing). The individual fears negative evaluation (humiliation, rejection), and the fear is out of proportion to actual threat, lasting 6 months or more.",
        "incorrectExplanations": {
            "A": "Agoraphobia centers on fear of being in places where escape might be difficult if incapacitating symptoms occur, not fear of negative social scrutiny.",
            "B": "Schizoid personality disorder involves genuine disinterest in social relationships without social anxiety or fear of scrutiny.",
            "C": "Social Anxiety Disorder is defined by intense fear of negative scrutiny and humiliation in social situations.",
            "D": "Avoidant PD is a pervasive personality construct; this scenario describes classic syndromal Social Anxiety Disorder."
        },
        "learningObjective": "Distinguish Social Anxiety Disorder from agoraphobia and personality disorders.",
        "reference": "Stein, M. B., & Stein, D. J. (2008). Social anxiety disorder. The Lancet, 371(9618), 1115-1125.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q248",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Intermediate",
        "questionText": "Under DSM-5-TR, a patient must fear or avoid situations because of thoughts that escape might be difficult or help unavailable if panic-like or incapacitating symptoms occur. To meet criteria for Agoraphobia, this marked fear or anxiety must occur in at least how many of the five specified situational environments?",
        "options": [
            {"id": "A", "text": "At least 1 of the 5 situations for at least 1 month"},
            {"id": "B", "text": "At least 4 of the 5 situations for at least 3 months"},
            {"id": "C", "text": "All 5 of the 5 situations for at least 12 months"},
            {"id": "D", "text": "At least 2 of the 5 situations for at least 6 months"}
        ],
        "correctAnswer": "D",
        "explanation": "DSM-5-TR requires marked fear or anxiety about at least 2 of the following 5 situations: (1) using public transportation, (2) being in open spaces, (3) being in enclosed spaces, (4) standing in line or being in a crowd, and (5) being outside of the home alone. The symptoms must typically last for 6 months or more.",
        "incorrectExplanations": {
            "A": "Fearing only 1 situation is classified as a Specific Phobia (situational type), not Agoraphobia.",
            "B": "4 situations are not required; meeting 2 situations is sufficient.",
            "C": "Requiring all 5 situations is overly restrictive and incorrect.",
            "D": "At least 2 of the 5 designated situations for >= 6 months is the diagnostic requirement for Agoraphobia."
        },
        "learningObjective": "Apply DSM-5-TR criteria for Agoraphobia and recognize its operational independence from Panic Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Agoraphobia.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q249",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Intermediate",
        "questionText": "During a routine blood collection clinic, a 20-year-old patient experiences an initial brief surge in blood pressure and heart rate, followed immediately by sudden profound bradycardia, hypotension, pallor, and vasovagal syncope. Which subtype of Specific Phobia demonstrates this unique biphasic autonomic response?",
        "options": [
            {"id": "A", "text": "Blood-injection-injury (BII) type"},
            {"id": "B", "text": "Situational type"},
            {"id": "C", "text": "Animal type"},
            {"id": "D", "text": "Natural environment type"}
        ],
        "correctAnswer": "A",
        "explanation": "Blood-injection-injury (BII) phobia is unique among anxiety disorders because it displays a biphasic autonomic response: an initial brief sympathetic acceleration (tachycardia) followed rapidly by a parasympathetic vasovagal surge leading to severe bradycardia, peripheral vasodilation, systemic hypotension, and fainting (syncope).",
        "incorrectExplanations": {
            "A": "Blood-injection-injury phobia uniquely features this biphasic vasovagal syncope response.",
            "B": "Situational phobias (elevators, flying) produce sustained sympathetic hyperarousal without bradycardic syncope.",
            "C": "Animal phobias provoke pure sympathetic fight-or-flight tachycardia.",
            "D": "Natural environment phobias (heights, storms) trigger typical sympathetic tachycardia without vasovagal collapse."
        },
        "learningObjective": "Analyze the distinct autonomic pathophysiology of blood-injection-injury specific phobia and its nursing management.",
        "reference": "Ritz, T., et al. (2010). Blood-injection-injury phobia: an autonomic physiological perspective. Biological Psychology, 84(2), 201-212.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q250",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 48-year-old patient is referred to a liaison psychiatric clinic for 'recurrent severe panic attacks' refractory to high-dose SSRI therapy. The nurse notes episodes of severe headache, profuse diaphoresis, sustained pallor, and paroxysmal hypertension with blood pressures spiking to 210/120 mmHg. Which endocrine medical condition must be ruled out immediately?",
        "options": [
            {"id": "A", "text": "Addisonian crisis"},
            {"id": "B", "text": "Pheochromocytoma"},
            {"id": "C", "text": "Primary hypoparathyroidism"},
            {"id": "D", "text": "Hashimoto's encephalopathy"}
        ],
        "correctAnswer": "B",
        "explanation": "Pheochromocytoma is a catecholamine-secreting neuroendocrine tumor (usually adrenal) that presents with the classic triad of episodic headaches, profuse sweating (diaphoresis), and tachycardia, accompanied by severe paroxysmal hypertension. It frequently mimics panic disorder and must be ruled out via plasma or urinary fractionated metanephrines.",
        "incorrectExplanations": {
            "A": "Addisonian crisis presents with severe hypotension, hyperkalemia, and shock, not hypertensive paroxysms.",
            "B": "Pheochromocytoma secretes surges of catecholamines causing the triad of headache, sweating, and severe hypertension.",
            "C": "Hypoparathyroidism causes hypocalcemia, tetany, and laryngeal spasm, not episodic catecholaminergic storms.",
            "D": "Hashimoto's encephalopathy presents with subacute cognitive decline, tremor, and myoclonus with antithyroid antibodies."
        },
        "learningObjective": "Differentiate medical mimics of panic attacks from primary anxiety disorders in liaison psychiatry.",
        "reference": "Lenders, J. W., et al. (2014). Pheochromocytoma and paraganglioma: an endocrine society clinical practice guideline. JCEM, 99(6), 1915-1942.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q251",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Advanced",
        "questionText": "A patient experiencing an acute panic attack hyperventilates rapidly, complaining of severe dizziness, perioral tingling, and bilateral carpopedal spasms in their hands. What acid-base physiological disruption is occurring, and what is the safest nursing response?",
        "options": [
            {"id": "A", "text": "Metabolic acidosis; administer IV sodium bicarbonate and encourage rapid shallow breaths"},
            {"id": "B", "text": "Respiratory acidosis; place a tight paper bag over the nose and mouth to force CO2 retention"},
            {"id": "C", "text": "Respiratory alkalosis; guide the patient through slow diaphragmatic breathing and do NOT use a paper bag"},
            {"id": "D", "text": "Metabolic alkalosis; initiate high-flow nasal oxygen at 15 L/min immediately"}
        ],
        "correctAnswer": "C",
        "explanation": "Hyperventilation expels excessive carbon dioxide (hypocapnia), shifting arterial blood pH upward to produce respiratory alkalosis. This causes acute reduction in ionized calcium, triggering neuromuscular excitability (paresthesia, carpopedal spasm / Trousseau sign). The nurse should calmly coach slow, diaphragmatic breathing. Rebreathing into a paper bag is obsolete and hazardous due to risks of fatal hypoxia.",
        "incorrectExplanations": {
            "A": "Hyperventilation causes acute respiratory alkalosis, not metabolic acidosis.",
            "B": "Hyperventilation causes alkalosis, not acidosis; paper bags carry serious risks of hypoxia and are medically contraindicated.",
            "C": "Respiratory alkalosis occurs from CO2 wash-out; slow diaphragmatic breathing restores normocapnia safely without paper bags.",
            "D": "The mechanism is respiratory, not metabolic; high-flow oxygen can worsen hyperventilation sensations."
        },
        "learningObjective": "Explain the pathophysiology of hyperventilation-induced respiratory alkalosis in panic attacks and implement safe nursing interventions.",
        "reference": "Callaham, M. (1989). Hypoxic hazards of paper bag rebreathing in hyperventilation syndrome. Annals of Emergency Medicine, 18(6), 622-625.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q252",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Advanced",
        "questionText": "In cognitive behavioural therapy for Panic Disorder, a mental health nurse practitioner instructs a patient to deliberately breathe rapidly through a thin straw, spin in a chair, and run in place to provoke tachycardia, dizziness, and shortness of breath in a controlled setting. What specific therapeutic technique is being implemented?",
        "options": [
            {"id": "A", "text": "In vivo situational exposure"},
            {"id": "B", "text": "Aversive autonomic counter-conditioning"},
            {"id": "C", "text": "Attentional diversion therapy"},
            {"id": "D", "text": "Interoceptive exposure"}
        ],
        "correctAnswer": "D",
        "explanation": "Interoceptive exposure involves the deliberate induction of feared somatic/visceral sensations (such as breathlessness, tachycardia, dizziness) using physical exercises (spinning, hyperventilation, straw breathing). This allows patients with Panic Disorder to habituate to somatic sensations, disconfirm catastrophic misinterpretations, and reduce fear of internal bodily sensations.",
        "incorrectExplanations": {
            "A": "In vivo exposure entails confronting external feared physical situations (e.g., entering an elevator or shopping center).",
            "B": "Aversive counter-conditioning pairs noxious stimuli to extinguish unwanted habits (e.g., emetics in alcoholism).",
            "C": "Attentional diversion therapy seeks to distract patients from symptoms, which maintains safety behaviors rather than extinguishing fear.",
            "D": "Interoceptive exposure systematically induces feared internal somatic sensations to promote extinction and new learning."
        },
        "learningObjective": "Differentiate interoceptive exposure from in vivo exposure in the treatment of Panic Disorder.",
        "reference": "Barlow, D. H., et al. (2000). Cognitive-behavioral therapy, imipramine, or their combination for panic disorder: a randomized controlled trial. JAMA, 283(19), 2529-2536.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q253",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Advanced",
        "questionText": "A 34-year-old married engineer experiences disabling anxiety, nightmares, and panic attacks whenever their spouse travels for business, calling them 20 times daily and insisting they return immediately due to an overwhelming conviction that the spouse will die in a crash. This adult presentation of severe distress upon detachment from primary attachment figures is diagnosed as:",
        "options": [
            {"id": "A", "text": "Adult Separation Anxiety Disorder"},
            {"id": "B", "text": "Dependent Personality Disorder"},
            {"id": "C", "text": "Borderline Personality Disorder with abandonment terror"},
            {"id": "D", "text": "Delusional Disorder, persecutory type"}
        ],
        "correctAnswer": "A",
        "explanation": "Under DSM-5-TR, Separation Anxiety Disorder is recognised across the lifespan, including adulthood. It features developmentally inappropriate and excessive fear or anxiety concerning separation from attachment figures, manifesting as persistent worry regarding harm to attachment figures, reluctance to be alone, and nightmares of separation.",
        "incorrectExplanations": {
            "A": "Adult Separation Anxiety Disorder features marked distress and catastrophic worry regarding separation from attachment figures.",
            "B": "Dependent Personality Disorder involves a pervasive, submissive need to be taken care of across all decisions, lacking the specific panic/catastrophic fear of harm upon physical absence.",
            "C": "Borderline PD involves pervasive instability, identity disturbance, and self-harm, not circumscribed anxiety regarding partner physical safety.",
            "D": "The belief is an anxious catastrophization rather than an encapsulated persecutory delusional framework."
        },
        "learningObjective": "Recognize the clinical presentation and diagnostic criteria for Adult Separation Anxiety Disorder.",
        "reference": "Shear, M. K., et al. (2006). Adult separation anxiety disorder. American Journal of Psychiatry, 163(6), 967-975.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q254",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Anxiety Disorders",
        "difficulty": "Expert",
        "questionText": "Which neuroanatomical circuit abnormality is most consistently identified in the pathophysiology of pathological anxiety and panic disorders?",
        "options": [
            {"id": "A", "text": "Hypoactivation of the amygdala accompanied by hyperactivation of the anterior cingulate cortex"},
            {"id": "B", "text": "Hyperactivation of the basolateral amygdala coupled with deficient top-down inhibitory control from the ventromedial prefrontal cortex (vmPFC)"},
            {"id": "C", "text": "Selective destruction of the locus coeruleus noradrenergic nuclei resulting in peripheral parasympathetic storm"},
            {"id": "D", "text": "Bilateral caudate nucleus hypertrophy with elevated striatal dopamine D2 density"}
        ],
        "correctAnswer": "B",
        "explanation": "Pathological anxiety involves hyperresponsiveness of the amygdala (the core fear circuit hub) combined with failure of top-down inhibitory regulation from the ventromedial prefrontal cortex (vmPFC) and anterior cingulate cortex. This results in exaggerated autonomic and behavioural fear responses to benign or ambiguous stimuli.",
        "incorrectExplanations": {
            "A": "The amygdala is hyperactive (not hypoactive) in anxiety disorders.",
            "B": "Hyperactivity of the amygdala coupled with impaired prefrontal (vmPFC) inhibitory gating is the hallmark fear-circuit deficit.",
            "C": "The locus coeruleus is hyperactive, increasing noradrenergic drive, not destroyed.",
            "D": "Caudate and striatal abnormalities are primarily implicated in OCD and movement disorders, not primary fear neurocircuitry."
        },
        "learningObjective": "Explain the fronto-amygdalar circuitry and inhibitory deficits in pathological anxiety.",
        "reference": "Rauch, S. L., et al. (2006). Neurocircuitry models of PTSD and anxiety disorders: insights from neuroimaging. Biological Psychiatry, 60(4), 376-382.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 5: Obsessive-Compulsive and Related Disorders (Q255 - Q264)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q255",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Foundation",
        "questionText": "In psychiatric psychopathology, how are obsessions fundamentally differentiated from compulsions in an individual diagnosed with Obsessive-Compulsive Disorder (OCD)?",
        "options": [
            {"id": "A", "text": "Obsessions are observable motor rituals, whereas compulsions are unexpressed delusional convictions"},
            {"id": "B", "text": "Obsessions are pleasant daydreaming fantasies, whereas compulsions are involuntary epileptic tics"},
            {"id": "C", "text": "Obsessions are recurrent, persistent, intrusive, and unwanted thoughts, urges, or images that cause marked distress, whereas compulsions are repetitive behaviors or mental acts performed to prevent or reduce anxiety"},
            {"id": "D", "text": "Obsessions are ego-syntonic traits, whereas compulsions are ego-dystonic hallucinations"}
        ],
        "correctAnswer": "C",
        "explanation": "Under DSM-5-TR, obsessions are defined as recurrent and persistent thoughts, urges, or images that are experienced as intrusive and unwanted (ego-dystonic) and cause marked anxiety or distress. Compulsions are repetitive behaviors (e.g., hand washing, checking) or mental acts (e.g., counting, praying) that an individual feels driven to perform in response to an obsession or according to rigid rules.",
        "incorrectExplanations": {
            "A": "Obsessions are internal cognitive/intrusive phenomena; compulsions are the rituals performed to alleviate distress.",
            "B": "Obsessions are distressing and ego-dystonic, never pleasant fantasies, and compulsions are purposeful acts rather than epileptic tics.",
            "C": "Obsessions are intrusive unwanted thoughts/urges, and compulsions are repetitive behaviors/mental acts aimed at anxiety reduction.",
            "D": "Obsessions are ego-dystonic, not ego-syntonic, and compulsions are purposeful rituals, not hallucinations."
        },
        "learningObjective": "Differentiate between obsessions and compulsions using standard psychopathological definitions.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Obsessive-Compulsive Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q256",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Foundation",
        "questionText": "The Yale-Brown Obsessive Compulsive Scale (Y-BOCS) is the clinician-administered gold standard for measuring OCD severity. What total score range on the 0 to 40 scale typically denotes 'severe' obsessive-compulsive illness?",
        "options": [
            {"id": "A", "text": "0 to 7"},
            {"id": "B", "text": "8 to 15"},
            {"id": "C", "text": "16 to 23"},
            {"id": "D", "text": "24 to 31"}
        ],
        "correctAnswer": "D",
        "explanation": "On the 10-item Y-BOCS (score range 0 to 40): 0-7 is subclinical; 8-15 is mild; 16-23 is moderate; 24-31 is severe; and 32-40 is extreme. A score of 24-31 reflects severe distress, significant time consumption (>3-8 hours daily), and major functional impairment.",
        "incorrectExplanations": {
            "A": "0 to 7 represents subclinical symptoms.",
            "B": "8 to 15 represents mild illness severity.",
            "C": "16 to 23 represents moderate illness severity.",
            "D": "24 to 31 denotes severe OCD on the standard Y-BOCS stratification."
        },
        "learningObjective": "Interpret severity thresholds on the Yale-Brown Obsessive Compulsive Scale (Y-BOCS).",
        "reference": "Goodman, W. K., et al. (1989). The Yale-Brown Obsessive Compulsive Scale: I. Development, use, and reliability. Archives of General Psychiatry, 46(11), 1006-1011.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q257",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Foundation",
        "questionText": "A 21-year-old bodybuilder spends 4 hours daily examining their physique in mirrors, measuring muscle circumference, and wearing heavy oversized sweatshirts in hot weather because they believe their body is 'grotesquely scrawny and deformed,' despite having exceptionally muscular morphology. They have undergone multiple aesthetic surgeries with no satisfaction. Which disorder and specifier are present?",
        "options": [
            {"id": "A", "text": "Body Dysmorphic Disorder with muscle dysphoria specifier"},
            {"id": "B", "text": "Anorexia Nervosa, restricting type"},
            {"id": "C", "text": "Somatic Symptom Disorder with hypochondriasis"},
            {"id": "D", "text": "Ego-syntonic Narcissistic Personality Disorder"}
        ],
        "correctAnswer": "A",
        "explanation": "Body Dysmorphic Disorder (BDD) is characterized by preoccupation with one or more perceived defects or flaws in physical appearance that are not observable or appear slight to others, accompanied by repetitive behaviors (mirror checking, camouflaging). The 'with muscle dysphoria' specifier is added when the preoccupation centers on the belief that one's body build is too small or insufficiently muscular.",
        "incorrectExplanations": {
            "A": "Preoccupation with perceived physical flaws/scrawniness despite objective muscularity is BDD with muscle dysphoria.",
            "B": "Anorexia nervosa focuses on fear of weight gain and drive for thinness, not obsession with being insufficiently muscular.",
            "C": "Somatic symptom disorder focuses on fear of illness or bodily pain, not perceived aesthetic deformity.",
            "D": "Narcissistic PD involves grandiosity and self-admiration, not distressing obsessions of physical deformity."
        },
        "learningObjective": "Identify diagnostic criteria and specifiers for Body Dysmorphic Disorder (BDD).",
        "reference": "Phillips, K. A. (2005). The Broken Mirror: Understanding and Treating Body Dysmorphic Disorder. Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q258",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Intermediate",
        "questionText": "A community mental health nurse visits a 62-year-old client whose residence is packed floor-to-ceiling with discarded newspapers, broken appliances, and expired packaging. The client cannot access their bed, kitchen stove, or shower. The client becomes intensely distressed when the nurse suggests recycling outdated papers, insisting they 'might need them someday.' How does Hoarding Disorder differ from normal collecting behavior?",
        "options": [
            {"id": "A", "text": "Hoarding involves organizing items systematically into categorized display cabinets"},
            {"id": "B", "text": "Hoarding involves persistent difficulty discarding possessions regardless of value, resulting in clutter that congests and compromises active living areas"},
            {"id": "C", "text": "Hoarding requires an underlying psychotic delusion of external command control"},
            {"id": "D", "text": "Hoarding is strictly limited to hoarding of domestic animals"}
        ],
        "correctAnswer": "B",
        "explanation": "DSM-5-TR Hoarding Disorder is defined by persistent difficulty discarding or parting with possessions regardless of their actual value, driven by perceived utility or emotional attachment, resulting in severe accumulation of clutter that congests and compromises the intended use of active living spaces (kitchens, beds, bathrooms), creating significant fire, fall, and health hazards.",
        "incorrectExplanations": {
            "A": "Collecting involves curated, organized, categorized items that do not disrupt living spaces.",
            "B": "Hoarding disorder involves disorganized accumulation and severe clutter that renders active living spaces unusable.",
            "C": "Hoarding is rarely psychotic; it is driven by distress over discarding, not command delusions.",
            "D": "Animal hoarding is a specific manifestation, but hoarding disorder encompasses all physical possessions."
        },
        "learningObjective": "Differentiate Hoarding Disorder from healthy collecting behaviors and evaluate living environment hazards.",
        "reference": "Frost, R. O., & Hartl, T. L. (1996). A cognitive-behavioral model of hoarding. Behaviour Research and Therapy, 34(4), 341-350.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q259",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 19-year-old student presents with irregular patches of hair loss on the scalp with hairs broken at varying lengths, but no scarring or erythema. The patient admits to recurrent urges to pull their hair when studying or feeling anxious, accompanied by mounting tension before pulling and a sense of relief immediately afterward, followed by intense shame. What is the diagnosis and evidence-based behavioral intervention?",
        "options": [
            {"id": "A", "text": "Alopecia areata; refer for corticosteroid scalp injections"},
            {"id": "B", "text": "Obsessive-Compulsive Disorder with contamination rituals; initiate ERP for washing"},
            {"id": "C", "text": "Trichotillomania (Hair-Pulling Disorder); initiate Habit Reversal Training (HRT)"},
            {"id": "D", "text": "Excoriation Disorder; initiate surgical wound debridement"}
        ],
        "correctAnswer": "C",
        "explanation": "Trichotillomania is characterized by recurrent pulling out of one's hair resulting in hair loss, repeated attempts to decrease or stop, and significant distress or impairment. The gold-standard evidence-based behavioral psychotherapeutic intervention is Habit Reversal Training (HRT), which incorporates awareness training, competing response training, and stimulus control.",
        "incorrectExplanations": {
            "A": "Alopecia areata is an autoimmune condition featuring smooth, round patches of complete hair loss with exclamation mark hairs, not manual pulling.",
            "B": "Contamination OCD involves washing rituals, not repetitive body-focused hair pulling.",
            "C": "Trichotillomania involves repetitive hair pulling driven by tension/relief cycles, treated with Habit Reversal Training.",
            "D": "Excoriation disorder involves skin picking, not scalp hair pulling."
        },
        "learningObjective": "Identify Trichotillomania psychopathology and select Habit Reversal Training as primary behavioral therapy.",
        "reference": "Woods, D. W., & Twohig, M. P. (2008). Trichotillomania: An ACT-enhanced Behavior Therapy Approach. Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q260",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Intermediate",
        "questionText": "A patient with OCD firmly believes that if they do not tap the doorframe 16 times before leaving home, their family will die in an explosion. When questioned by the nurse, the patient states: 'I know it sounds completely irrational, but I cannot shake the terror.' Which DSM-5-TR insight specifier applies?",
        "options": [
            {"id": "A", "text": "With absent insight / delusional beliefs"},
            {"id": "B", "text": "With poor insight"},
            {"id": "C", "text": "With dissociative fugue insight"},
            {"id": "D", "text": "With good or fair insight"}
        ],
        "correctAnswer": "D",
        "explanation": "DSM-5-TR classifies insight in OCD into three levels: (1) With good or fair insight (the individual recognizes that OCD beliefs are definitely or probably not true, or that they may or may not be true); (2) With poor insight (thinks OCD beliefs are probably true); and (3) With absent insight/delusional beliefs (completely convinced that OCD beliefs are true).",
        "incorrectExplanations": {
            "A": "Absent insight/delusional beliefs means the individual is 100% convinced the obsession is factually true.",
            "B": "Poor insight means the patient believes the obsession is probably true.",
            "C": "Dissociative fugue is not an insight specifier in OCD.",
            "D": "Acknowledging that the belief is irrational constitutes good or fair insight."
        },
        "learningObjective": "Differentiate between the three DSM-5-TR insight specifiers in OCD.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Obsessive-Compulsive Disorder Specifiers.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q261",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Advanced",
        "questionText": "A newly admitted inpatient with severe OCD performs 2-hour handwashing and decontamination rituals before breakfast, causing them to miss meals and morning unit meetings. How should the psychiatric nurse manage this ritualistic behavior during the initial inpatient stabilization phase?",
        "options": [
            {"id": "A", "text": "Initially allow scheduled time for rituals, gradually negotiating collaborative time limits while planning systematic exposure and response prevention"},
            {"id": "B", "text": "Lock the patient's bathroom immediately and physically block access to water basins to abruptly terminate all rituals on Day 1"},
            {"id": "C", "text": "Perform the washing rituals for the patient to save time and reduce their physical exhaustion"},
            {"id": "D", "text": "Ignore the rituals completely and allow the patient to wash undisturbed for as many hours as needed"}
        ],
        "correctAnswer": "A",
        "explanation": "In the initial phase of psychiatric inpatient admission for severe OCD, nurses should accommodate the patient's need to perform rituals to avoid precipitating panic or agitation. The nurse collaborates with the patient to build trust, scheduling extra time for routines while gradually and mutually negotiating progressive reductions in ritual time, paving the way for formal Exposure and Response Prevention (ERP).",
        "incorrectExplanations": {
            "A": "Initial accommodation with gradual, collaborative structured time reduction preserves rapport and prevents severe panic.",
            "B": "Abrupt, unilateral prohibition of rituals precipitates extreme panic, agitation, and potential aggression without fostering learning.",
            "C": "Performing rituals for the patient constitutes accommodation and reinforces the OCD cycle.",
            "D": "Ignoring rituals indefinitely enables chronic disability and prevents therapeutic recovery."
        },
        "learningObjective": "Formulate safe, staged nursing management plans for severe ritualistic behavior in acute psychiatric settings.",
        "reference": "Townsend, M. C., & Morgan, K. I. (2020). Psychiatric Mental Health Nursing (10th ed.). F.A. Davis.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q262",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Advanced",
        "questionText": "A mental health nurse conducts a family psychoeducation session for the parents of a 22-year-old with OCD. The parents report that to prevent their son from becoming distressed, they boil his clothes daily, purchase cases of bleach, and inspect his locks 10 times nightly. How should the nurse explain the effect of this family accommodation on the patient's illness course?",
        "options": [
            {"id": "A", "text": "Family accommodation accelerates recovery by reducing the patient's physiological cortisol load"},
            {"id": "B", "text": "Family accommodation reinforces and perpetuates the OCD symptoms by preventing the patient from experiencing anxiety habituation and disconfirming catastrophic fears"},
            {"id": "C", "text": "Family accommodation transforms ego-dystonic obsessions into healthy protective ego-syntonic routines"},
            {"id": "D", "text": "Family accommodation is harmless and should be maintained until SSRI blood levels reach steady state"}
        ],
        "correctAnswer": "B",
        "explanation": "Family accommodation (participating in rituals, modifying routines, facilitating avoidance) provides temporary relief but maintains the OCD cycle. By shielding the patient from distress, accommodation prevents natural inhibitory learning and habituation, confirming the patient's irrational belief that catastrophic consequences can only be averted through rituals.",
        "incorrectExplanations": {
            "A": "Accommodation maintains and worsens symptoms over time rather than accelerating recovery.",
            "B": "Family accommodation prevents habituation and reinforces the catastrophic OCD belief cycle.",
            "C": "Accommodation does not create healthy routines; it entrenches disabling psychopathology.",
            "D": "Family accommodation significantly correlates with poorer pharmacotherapeutic and psychotherapy outcomes."
        },
        "learningObjective": "Explain the role of family accommodation in maintaining obsessive-compulsive symptomatology and guide family interventions.",
        "reference": "Lebowitz, E. R., et al. (2016). Family accommodation in obsessive-compulsive disorder. Expert Review of Neurotherapeutics, 16(1), 45-53.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q263",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Advanced",
        "questionText": "An 8-year-old child with no personal or family psychiatric history experiences an overnight, dramatic, explosive onset of severe contamination obsessions, choreiform motor tics, separation anxiety, and emotional lability 2 weeks after an untreated pharyngitis infection. Which pediatric neuropsychiatric condition should be investigated?",
        "options": [
            {"id": "A", "text": "Early-onset Schizophrenia spectrum disorder"},
            {"id": "B", "text": "Childhood-onset Bipolar I Disorder with mixed mania"},
            {"id": "C", "text": "Pediatric Autoimmune Neuropsychiatric Disorders Associated with Streptococcal Infections (PANDAS)"},
            {"id": "D", "text": "Gilles de la Tourette syndrome, non-inflammatory variant"}
        ],
        "correctAnswer": "C",
        "explanation": "PANDAS (Pediatric Autoimmune Neuropsychiatric Disorders Associated with Streptococcal Infections) is characterized by an abrupt, dramatic 'overnight' onset or exacerbation of OCD and/or tics following a Group A streptococcal infection. It is mediated by autoimmune molecular mimicry, where anti-streptococcal antibodies cross-react with basal ganglia neuronal antigens.",
        "incorrectExplanations": {
            "A": "Early-onset schizophrenia develops insidiously and does not present with post-infectious explosive chorea/tics.",
            "B": "Bipolar disorder does not manifest overnight with post-streptococcal basal ganglia signs.",
            "C": "PANDAS is the classic post-streptococcal autoimmune presentation of sudden-onset OCD and tics.",
            "D": "Tourette syndrome develops gradually over months in early childhood, not explosively post-strep."
        },
        "learningObjective": "Recognize the clinical presentation and autoimmune pathophysiology of PANDAS in pediatric mental health.",
        "reference": "Swedo, S. E., et al. (1998). Pediatric autoimmune neuropsychiatric disorders associated with streptococcal infections: clinical description of the first 50 cases. American Journal of Psychiatry, 155(2), 264-271.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q264",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Obsessive-Compulsive and Related Disorders",
        "difficulty": "Expert",
        "questionText": "Functional neuroimaging and neurosurgical models of severe, intractable OCD demonstrate persistent hyperactivity within which specific central nervous system circuitry?",
        "options": [
            {"id": "A", "text": "The dentato-rubro-thalamic cerebellar motor circuit"},
            {"id": "B", "text": "The spinothalamic ascending tract and dorsal root sensory ganglia"},
            {"id": "C", "text": "The mesocorticolimbic reward deficiency tract"},
            {"id": "D", "text": "The cortico-striato-thalamo-cortical (CSTC) loop, involving the orbitofrontal cortex and anterior cingulate cortex"}
        ],
        "correctAnswer": "D",
        "explanation": "The neurobiology of OCD centers on hyperactivity and impaired inhibitory gating within the cortico-striato-thalamo-cortical (CSTC) loop. Specifically, hyperactivation of the orbitofrontal cortex (generating intrusive danger signals) and anterior cingulate cortex (mediating tension and error detection), combined with caudate nucleus dysregulation, drives obsessional intrusions and compulsive urges. Neurosurgical procedures (capsulotomy) and Deep Brain Stimulation (DBS) target this CSTC circuit.",
        "incorrectExplanations": {
            "A": "The dentato-rubro-thalamic pathway is involved in cerebellar tremor, not obsessive-compulsive circuits.",
            "B": "The spinothalamic tract conducts peripheral pain and temperature sensations.",
            "C": "The reward deficiency tract is implicated in addiction, not classic CSTC OCD looping.",
            "D": "The CSTC loop linking orbitofrontal cortex, striatum, and thalamus is the primary pathophysiological circuit in OCD."
        },
        "learningObjective": "Synthesize the neuroanatomical circuitry of the CSTC loop in the pathogenesis and neuromodulation of OCD.",
        "reference": "Saxena, S., & Rauch, S. L. (2000). Functional neuroimaging and the neuroanatomy of obsessive-compulsive disorder. Psychiatric Clinics of North America, 23(3), 563-586.",
        "contentReviewStatus": "Peer Reviewed"
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(MOD3_P1)} questions for Module 3 Part 1")
