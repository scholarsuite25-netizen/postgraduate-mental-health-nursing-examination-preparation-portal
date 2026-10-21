"""
Module 8 Part 2: Questions MHN-Q765 to MHN-Q814 (50 questions)
Topics 6 to 10:
6. Delirium in older adults (MHN-Q765 to MHN-Q774)
7. Dementia types and management (MHN-Q775 to MHN-Q784)
8. Late-life depression (MHN-Q785 to MHN-Q794)
9. Elder abuse and safeguarding (MHN-Q795 to MHN-Q804)
10. Geriatric psychopharmacology (MHN-Q805 to MHN-Q814)
"""

QUESTIONS_MOD8_PART2 = [
    # -------------------------------------------------------------------------
    # Topic 6: Delirium in older adults (MHN-Q765 - MHN-Q774)
    # Target Answers: B, D, B, D, A, C, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q765",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Foundation",
        "questionText": "The Confusion Assessment Method (CAM) is the most widely validated diagnostic algorithm for delirium. To confirm a clinical diagnosis of delirium using the CAM, which specific combination of features must be demonstrated?",
        "options": [
            {"id": "A", "text": "Feature 1 (Memory loss) and Feature 2 (Depressed mood) only"},
            {"id": "B", "text": "Feature 1 (Acute onset and fluctuating course) AND Feature 2 (Inattention), PLUS EITHER Feature 3 (Disorganized thinking) OR Feature 4 (Altered level of consciousness)"},
            {"id": "C", "text": "Feature 3 (Disorganized thinking) and Feature 4 (Altered consciousness) without inattention"},
            {"id": "D", "text": "Presence of auditory hallucinations persisting for at least 6 months"}
        ],
        "correctAnswer": "B",
        "explanation": "The CAM diagnostic algorithm requires the presence of both Feature 1 (Acute onset and fluctuating course) AND Feature 2 (Inattention: difficulty focusing or sustaining attention), PLUS either Feature 3 (Disorganized thinking) OR Feature 4 (Altered level of consciousness: hyperalert, lethargic, stuporous).",
        "incorrectExplanations": {
            "A": "Memory loss and depression do not meet criteria for delirium; they suggest dementia or affective illness.",
            "C": "Inattention (Feature 2) is the cardinal neurocognitive hallmark of delirium and is mandatory for CAM diagnosis.",
            "D": "Six months of hallucinations indicates a chronic psychotic disorder, not acute delirium."
        },
        "learningObjective": "Apply the Confusion Assessment Method (CAM) diagnostic criteria to identify delirium in older adults.",
        "reference": "Inouye, S. K., et al. (1990). Clarifying confusion: the confusion assessment method. A new method for detection of delirium. Annals of Internal Medicine, 113(12), 941-948.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q766",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Foundation",
        "questionText": "In the multifactorial model of delirium, clinicians distinguish between 'Predisposing Factors' (baseline vulnerabilities) and 'Precipitating Factors' (acute triggers). Which of the following represents a classic acute PRECIPITATING factor?",
        "options": [
            {"id": "A", "text": "Age 88 years"},
            {"id": "B", "text": "Pre-existing severe Alzheimer's disease"},
            {"id": "C", "text": "Severe chronic bilateral visual impairment"},
            {"id": "D", "text": "An acute untreated Escherichia coli urinary tract infection with acute urinary retention"}
        ],
        "correctAnswer": "D",
        "explanation": "Predisposing factors are baseline vulnerability traits (advanced age, pre-existing dementia, sensory impairment, multimorbidity). Precipitating factors are acute insults, triggers, or noxious physiological events (e.g., acute infection/sepsis, urinary retention, electrolyte disturbance, new anticholinergic drugs, surgery) that trigger delirium.",
        "incorrectExplanations": {
            "A": "Advanced age is a predisposing vulnerability factor.",
            "B": "Pre-existing dementia is the single strongest predisposing factor for delirium.",
            "C": "Chronic visual impairment is a predisposing sensory vulnerability."
        },
        "learningObjective": "Differentiate predisposing baseline risk factors from acute precipitating triggers in delirium pathophysiology.",
        "reference": "Inouye, S. K., et al. (2014). Delirium in elderly people. The Lancet, 383(9920), 911-922.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q767",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Intermediate",
        "questionText": "An 82-year-old hospitalized patient is quiet, lying motionless in bed, staring blankly, speaking very slowly when addressed, and exhibiting apathy and reduced motor tone. The surgical team believes the patient is 'just pleasantly depressed'. What delirium subtype does this patient exhibit, and why does it carry higher mortality?",
        "options": [
            {"id": "A", "text": "Hyperactive delirium; carries high mortality due to cardiac exhaustion"},
            {"id": "B", "text": "Hypoactive delirium; it is frequently overlooked, under-recognized, or misdiagnosed as depression, leading to delays in identifying and treating life-threatening underlying medical causes"},
            {"id": "C", "text": "Malingering catatonia; carries high mortality from intentional fasting"},
            {"id": "D", "text": "Dissociative fugue state"}
        ],
        "correctAnswer": "B",
        "explanation": "Hypoactive delirium accounts for roughly 50% of delirium cases, characterized by lethargy, psychomotor slowing, apathy, and withdrawal. Because patients are quiet and not disruptive, hypoactive delirium is frequently missed or misdiagnosed as depression or dementia, resulting in untreated underlying medical pathology and higher mortality than hyperactive delirium.",
        "incorrectExplanations": {
            "A": "Hyperactive delirium features agitation, restlessness, and delusions; this patient is lethargic and slow.",
            "C": "Hypoactive delirium is an involuntary organic encephalopathy, not intentional malingering.",
            "D": "Dissociative fugue involves wandering and identity loss, not medical psychomotor lethargy."
        },
        "learningObjective": "Recognize the clinical presentation and heightened mortality risks associated with hypoactive delirium.",
        "reference": "Meagher, D. J., et al. (2012). Motor subtypes of delirium: past, present and future. International Review of Psychiatry, 24(6), 557-565.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q768",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Intermediate",
        "questionText": "The 4AT (Rapid Clinical Test for Delirium) is widely recommended across acute hospital and mental health trusts. What four items are assessed in the 4AT, and what score threshold indicates probable delirium?",
        "options": [
            {"id": "A", "text": "Blood pressure, pulse, glucose, and oxygen saturation; score >=10"},
            {"id": "B", "text": "Memory, language, calculation, and motor apraxia; score >=20"},
            {"id": "C", "text": "Reflexes, cranial nerves, sensation, and gait; score >=2"},
            {"id": "D", "text": "[1] Alertness, [2] AMT4 (Age, Date of birth, Place, Current year), [3] Attention (Months of the year backwards), and [4] Acute change or fluctuating course; a score of 4 or more indicates probable delirium"}
        ],
        "correctAnswer": "D",
        "explanation": "The 4AT evaluates four specific clinical domains: 1) Alertness (normal vs altered), 2) AMT4 cognitive items, 3) Attention tested via reciting the months of the year backwards, and 4) Acute change or fluctuating course. A total score of 4 or more indicates probable delirium (with or without dementia).",
        "incorrectExplanations": {
            "A": "These are routine physiological vital signs, not the 4AT delirium tool.",
            "B": "These reflect detailed neuropsychological testing similar to the MMSE.",
            "C": "These are standard components of a physical neurological examination."
        },
        "learningObjective": "Administer and interpret the 4AT rapid screening instrument for delirium.",
        "reference": "Bellelli, G., et al. (2014). Validation of the 4AT, a new tool for delirium detection in older patients. Age and Ageing, 43(4), 496-502.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q769",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Intermediate",
        "questionText": "In accordance with NICE Guideline NG103 and international gerontological nursing standards, what constitutes the mandatory FIRST-LINE management strategy for an older adult experiencing delirium?",
        "options": [
            {"id": "A", "text": "Non-pharmacological multicomponent interventions: frequent verbal reorientation by consistent staff, ensuring sensory aids (clean glasses and working hearing aids) are in place, maintaining hydration, promoting mobilization, optimizing sleep hygiene, treating pain, and avoiding physical restraints"},
            {"id": "B", "text": "Immediate intravenous injection of high-dose haloperidol and physical wrist restraints"},
            {"id": "C", "text": "Placing the patient in total sensory deprivation in a dark, silent room for 48 hours"},
            {"id": "D", "text": "Continuous intravenous midazolam infusion until the patient is completely unarousable"}
        ],
        "correctAnswer": "A",
        "explanation": "NICE NG103 emphasizes that non-pharmacological multicomponent interventions are first-line for delirium: reorienting the patient, ensuring hearing aids and eyeglasses are fitted, optimizing fluid balance, promoting early mobilization, minimizing room changes, ensuring quiet sleep environments, managing pain, and avoiding physical restraints.",
        "incorrectExplanations": {
            "B": "Chemical and physical restraints worsen delirium, increase falls, and risk cardiac arrest; they are never first-line.",
            "C": "Sensory deprivation exacerbates disorientation and triggers visual hallucinations.",
            "D": "Benzodiazepines worsen delirium and precipitate respiratory arrest; they are contraindicated unless delirium tremens."
        },
        "learningObjective": "Implement evidence-based non-pharmacological multicomponent nursing interventions for delirium.",
        "reference": "NICE. (2019). Delirium: prevention, diagnosis and management (NICE Guideline NG103).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q770",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Intermediate",
        "questionText": "When systematically investigating the underlying physical causes of acute delirium in an older adult, what does the clinical nursing mnemonic 'PINCH ME' represent?",
        "options": [
            {"id": "A", "text": "Paranoia, Insanity, Neurosis, Catatonia, Hallucinations, Mania, and Euphoria"},
            {"id": "B", "text": "Pulse, Intubation, Nasogastric tube, Catheter, Hemoglobin, Magnesium, and ECG"},
            {"id": "C", "text": "Pain, Infection (UTI, chest), Nutrition, Constipation, Hydration/Hypoxia, Medication, and Environmental changes"},
            {"id": "D", "text": "Platelets, Insulin, Nitrogen, Creatinine, Hepatic enzymes, Monocytes, and Electrolytes"}
        ],
        "correctAnswer": "C",
        "explanation": "'PINCH ME' is an evidence-based clinical mnemonic summarizing common reversible organic triggers of delirium in older adults: Pain, Infection, Nutrition/constipation, Constipation, Hydration/hypoxia, Medication (anticholinergics, sedatives), and Environmental disruption.",
        "incorrectExplanations": {
            "A": "These are psychiatric symptom labels that fail to identify reversible medical pathology.",
            "B": "These are invasive medical devices and basic vital signs.",
            "D": "These are laboratory haematology and biochemistry parameters."
        },
        "learningObjective": "Utilize the 'PINCH ME' clinical mnemonic to systematically investigate reversible organic triggers of delirium.",
        "reference": "British Geriatrics Society (BGS). (2018). Delirium in older people: Diagnosis, prevention and management.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q771",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Advanced",
        "questionText": "Under NICE guidance, when is it clinically justifiable to administer low-dose, short-term psychopharmacotherapy (e.g. Haloperidol 0.5 mg or Quetiapine) to an older patient experiencing acute delirium, and in which neurological condition is antipsychotic use absolutely contraindicated?",
        "options": [
            {"id": "A", "text": "Whenever the patient asks repetitive questions; contraindicated in hypertension"},
            {"id": "B", "text": "Strictly when non-pharmacological methods have failed AND the patient's symptoms present severe intractable distress or immediate danger of physical harm to self or others; absolutely contraindicated in Dementia with Lewy Bodies or Parkinson's disease due to life-threatening neuroleptic sensitivity"},
            {"id": "C", "text": "As routine prophylaxis for all surgical admissions; contraindicated in diabetes"},
            {"id": "D", "text": "To keep the ward quiet so night staff can complete paperwork; contraindicated in asthma"}
        ],
        "correctAnswer": "B",
        "explanation": "Antipsychotics in delirium are strictly restricted to cases where non-pharmacological interventions fail and the patient's agitation causes extreme distress or direct safety risks. They must be prescribed at the lowest effective dose for the shortest possible duration (1-7 days). They are absolutely contraindicated in Lewy body dementia and Parkinson's disease due to severe, potentially fatal neuroleptic sensitivity.",
        "incorrectExplanations": {
            "A": "Repetitive questions require reassurance, not chemical restraint.",
            "C": "Antipsychotics are never indicated as routine prophylaxis for surgical patients.",
            "D": "Using psychotropics for staff convenience is illegal chemical restraint and institutional abuse."
        },
        "learningObjective": "Delineate strict clinical indications, dosing principles, and neurodegenerative contraindications for pharmacological intervention in delirium.",
        "reference": "NICE. (2019). Delirium: prevention, diagnosis and management (NICE Guideline NG103).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q772",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Advanced",
        "questionText": "An advanced practice psychiatric nurse is called to evaluate an 85-year-old patient admitted to an acute medical ward. What clinical diagnostic triad most reliably differentiates acute delirium from chronic dementia?",
        "options": [
            {"id": "A", "text": "Delirium has an insidious multi-year onset, stable alertness, and is irreversible; dementia has sudden onset, fluctuating alertness, and is fully curable"},
            {"id": "B", "text": "Delirium occurs exclusively in young athletes; dementia occurs exclusively in newborn infants"},
            {"id": "C", "text": "Both conditions have identical sudden onsets and identical neurochemical mechanisms"},
            {"id": "D", "text": "Delirium features rapid acute onset (hours to days), fluctuating course with marked inattention and impaired alertness, and potential reversibility; dementia features insidious progressive onset (months to years), relatively preserved alertness in early stages, and gradual irreversible decline"}
        ],
        "correctAnswer": "D",
        "explanation": "Delirium has an acute/subacute onset (hours to days), a fluctuating course throughout the 24-hour cycle, prominent inattention, altered level of consciousness, and is potentially reversible upon treating the precipitant. Dementia develops insidiously over months to years, alertness is typically preserved until late stages, and the course is chronically progressive.",
        "incorrectExplanations": {
            "A": "This option completely reverses the definitions of delirium and dementia.",
            "B": "Delirium and dementia are disorders predominantly affecting older adults, not athletes or neonates.",
            "C": "Delirium and dementia have distinct clinical courses, etiologies, and prognoses."
        },
        "learningObjective": "Differentiate the clinical features, onset, course, and reversibility of delirium versus dementia.",
        "reference": "Inouye, S. K., et al. (2014). Delirium in elderly people. The Lancet, 383(9920), 911-922.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q773",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Advanced",
        "questionText": "What does longitudinal epidemiological research demonstrate regarding the long-term neurocognitive trajectory of older adults who experience an episode of delirium during a general hospital admission?",
        "options": [
            {"id": "A", "text": "Delirium is associated with an accelerated trajectory of permanent long-term cognitive decline, an estimated three-fold increased risk of developing incident dementia, higher rates of permanent institutional care placement, and elevated 1-year mortality"},
            {"id": "B", "text": "Delirium permanently enhances neurogenesis and increases cognitive IQ by 20 points"},
            {"id": "C", "text": "Delirium has zero long-term sequelae; all patients return permanently to 100% baseline with no risks"},
            {"id": "D", "text": "Delirium provides lifelong biological protection against future strokes"}
        ],
        "correctAnswer": "A",
        "explanation": "Longitudinal cohort studies demonstrate that delirium is not merely a transient benign state. It reflects significant neuro-inflammatory stress and neuronal injury, leading to accelerated cognitive decline, a three-fold higher risk of incident dementia, increased long-term nursing home placement, and substantially increased 6- to 12-month mortality.",
        "incorrectExplanations": {
            "B": "Delirium induces neuroinflammation and neurotoxicity, never cognitive enhancement.",
            "C": "The assumption that delirium leaves no long-term damage has been disproven by longitudinal research.",
            "D": "Delirium is associated with heightened cerebrovascular morbidity, not stroke protection."
        },
        "learningObjective": "Analyze longitudinal prognostic outcomes and secondary dementia risks following hospital delirium episodes.",
        "reference": "Witlox, J., et al. (2010). Delirium in elderly patients and the risk of postdischarge mortality, institutionalization, and dementia: A meta-analysis. JAMA, 304(4), 443-451.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q774",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Delirium in older adults",
        "difficulty": "Expert",
        "questionText": "The Hospital Elder Life Program (HELP), formulated by Sharon Inouye, is an established multidisciplinary model for hospital-wide delirium prevention. When implementing HELP across an acute geriatric admissions unit, what protocolized interventions reduce delirium incidence by approximately 40%?",
        "options": [
            {"id": "A", "text": "Routine administration of prophylactic high-dose benzodiazepines to all patients over 70"},
            {"id": "B", "text": "Keeping all patients strictly immobilized in bed with continuous bladder catheters"},
            {"id": "C", "text": "Protocolized cognitive stimulation/reorientation, early daily mobilization, non-pharmacological sleep enhancement (warm drinks, back rubs, white noise, eliminating nocturnal vital checks), visual and hearing aid optimization, and systematic oral hydration assistance"},
            {"id": "D", "text": "Performing daily routine lumbar punctures and arterial blood gas sampling on all admitted elders"}
        ],
        "correctAnswer": "C",
        "explanation": "The HELP program targets six primary delirium risk factors through protocolized nursing/volunteer interventions: cognitive impairment (daily cognitively stimulating activities), sleep deprivation (sleep protocol avoiding nocturnal noise/vitals), immobility (daily ambulation), visual/hearing deficits (ensuring clean aids), and dehydration (oral fluid protocols), reducing delirium incidence by ~40%.",
        "incorrectExplanations": {
            "A": "Prophylactic benzodiazepines double the incidence of delirium and increase falls.",
            "B": "Bed rest and indwelling catheters are major precipitating causes of delirium.",
            "D": "Invasive painful testing causes distress and sleep fragmentation, precipitating delirium."
        },
        "learningObjective": "Design and evaluate systemic delirium prevention systems utilizing the Hospital Elder Life Program (HELP) framework.",
        "reference": "Inouye, S. K., et al. (1999). A multicomponent intervention to prevent delirium in hospitalized older patients. New England Journal of Medicine, 340(9), 669-676.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 7: Dementia types and management (MHN-Q775 - MHN-Q784)
    # Target Answers: A, C, B, D, A, C, B, A, D, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q775",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Foundation",
        "questionText": "What are the cardinal clinical presentation and hallmark neuropathological lesions that characterize Alzheimer's Disease (AD)?",
        "options": [
            {"id": "A", "text": "Insidious onset with progressive impairment of episodic memory (difficulty learning and retaining new information), followed by executive dysfunction and aphasia; characterized pathologically by extracellular amyloid-beta plaques and intracellular hyperphosphorylated tau neurofibrillary tangles"},
            {"id": "B", "text": "Sudden onset of acute hemiparesis with complete preservation of memory; characterized pathologically by brain abscesses"},
            {"id": "C", "text": "Early disinhibition and gluttony with normal neuropathology"},
            {"id": "D", "text": "Visual hallucinations occurring strictly in the dark with no histological brain changes"}
        ],
        "correctAnswer": "A",
        "explanation": "Alzheimer's Disease typically begins insidiously with failure of episodic memory (hippocampal and entorhinal cortex degeneration), progressing to executive dysfunction, word-finding deficits (aphasia), and visuospatial impairment. Its hallmark neuropathology consists of extracellular amyloid-beta neuritic plaques and intracellular hyperphosphorylated tau neurofibrillary tangles.",
        "incorrectExplanations": {
            "B": "Sudden hemiparesis describes acute stroke, not typical Alzheimer's dementia.",
            "C": "Early disinhibition and hyperorality characterize frontotemporal dementia, not classic Alzheimer's.",
            "D": "Visual hallucinations suggest Lewy body dementia, which exhibits alpha-synuclein inclusions."
        },
        "learningObjective": "Identify the clinical manifestations and hallmark neuropathology of Alzheimer's Disease.",
        "reference": "McKhann, G. M., et al. (2011). The diagnosis of dementia due to Alzheimer's disease: Recommendations from the National Institute on Aging-Alzheimer's Association workgroups. Alzheimer's & Dementia, 7(3), 263-269.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q776",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Foundation",
        "questionText": "A 74-year-old man with a history of hypertension, type 2 diabetes, and two past minor strokes presents with cognitive decline. His family notes his decline occurs in distinct 'step-wise' drops following transient episodes of confusion, with early impairment in executive processing and psychomotor speed. What dementia type is most likely?",
        "options": [
            {"id": "A", "text": "Prion-induced Creutzfeldt-Jakob disease"},
            {"id": "B", "text": "Frontotemporal lobar degeneration"},
            {"id": "C", "text": "Vascular Dementia (VaD)"},
            {"id": "D", "text": "Wernicke-Korsakoff syndrome"}
        ],
        "correctAnswer": "C",
        "explanation": "Vascular Dementia (VaD) is characterized by a stepwise or fluctuating progression of cognitive deficits linked to cerebrovascular injury (multi-infarcts, lacunar strokes, subcortical small vessel ischemia). Executive dysfunction, slowed information processing, gait unsteadiness, and focal neurological signs typically precede severe memory loss.",
        "incorrectExplanations": {
            "A": "Creutzfeldt-Jakob disease presents with rapidly progressive dementia (weeks to months) with severe myoclonus.",
            "B": "Frontotemporal dementia presents primarily with prominent personality changes, not stepwise post-stroke deficits.",
            "D": "Wernicke-Korsakoff syndrome involves severe anterograde amnesia and confabulation secondary to thiamine deficiency in chronic alcoholism."
        },
        "learningObjective": "Differentiate Vascular Dementia from Alzheimer's Disease based on clinical course and cerebrovascular risk factors.",
        "reference": "O'Brien, J. T., & Thomas, A. (2015). Vascular dementia. The Lancet, 386(10004), 1698-1706.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q777",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Foundation",
        "questionText": "Which clinical diagnostic triad constitutes the core clinical features of Dementia with Lewy Bodies (DLB)?",
        "options": [
            {"id": "A", "text": "Grandiosity, flight of ideas, and decreased need for sleep"},
            {"id": "B", "text": "1) Fluctuating cognition with pronounced variations in attention and alertness, 2) Recurrent, well-formed, detailed visual hallucinations, and 3) Spontaneous motor parkinsonism (rigidity, bradykinesia, tremor)"},
            {"id": "C", "text": "Sudden amnesia, severe polyphagia, and peripheral neuropathy"},
            {"id": "D", "text": "Pure motor paralysis without any cognitive or perceptual symptoms"}
        ],
        "correctAnswer": "B",
        "explanation": "According to the consensus criteria for Dementia with Lewy Bodies (DLB), the core clinical triad comprises: 1) Fluctuating cognition and alertness, 2) Recurrent, complex, well-formed visual hallucinations (often people or animals), and 3) Spontaneous features of parkinsonism. REM sleep behavior disorder is also a major indicative biomarker.",
        "incorrectExplanations": {
            "A": "These are the diagnostic symptoms of bipolar mania.",
            "C": "This presentation suggests Korsakoff syndrome or metabolic neuropathy, not DLB.",
            "D": "Pure motor paralysis without cognitive deficit describes lower motor neuron or stroke syndromes."
        },
        "learningObjective": "Recall the core diagnostic triad and clinical features of Dementia with Lewy Bodies (DLB).",
        "reference": "McKeith, I. G., et al. (2017). Diagnosis and management of dementia with Lewy bodies: Fourth consensus report of the DLB Consortium. Neurology, 89(1), 88-100.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q778",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Intermediate",
        "questionText": "A patient with suspected Dementia with Lewy Bodies (DLB) is admitted to an acute ward and given Haloperidol 2 mg for nocturnal visual hallucinations. Within 24 hours, the patient develops profound rigidity, mutism, severe extrapyramidal freezing, autonomic collapse, and acute cognitive deterioration. What clinical catastrophe has occurred?",
        "options": [
            {"id": "A", "text": "A standard therapeutic response indicating the haloperidol dose should be increased"},
            {"id": "B", "text": "Spontaneous cure of the underlying Lewy bodies"},
            {"id": "C", "text": "Acute bacterial meningitis acquired during admission"},
            {"id": "D", "text": "Severe neuroleptic sensitivity reaction; up to 50% of patients with DLB exhibit extreme, life-threatening sensitivity to antipsychotics, making their use contraindicated"}
        ],
        "correctAnswer": "D",
        "explanation": "Severe neuroleptic sensitivity is a cardinal feature of Dementia with Lewy Bodies (occurring in up to 50% of patients). Exposure to antipsychotics (especially typical D2 antagonists like haloperidol) can trigger acute life-threatening parkinsonian crisis, profound rigidity, autonomic instability, irreversible cognitive decline, and increased mortality. Typical antipsychotics are absolutely contraindicated in DLB.",
        "incorrectExplanations": {
            "A": "Increasing the dose in severe neuroleptic sensitivity is potentially fatal.",
            "B": "Neuroleptic sensitivity indicates severe pharmacological harm, not a cure.",
            "C": "Acute onset of rigidity and mutism immediately post-antipsychotic reflects drug toxicity, not meningitis."
        },
        "learningObjective": "Evaluate severe neuroleptic sensitivity in Dementia with Lewy Bodies and identify strict prescribing contraindications.",
        "reference": "McKeith, I., et al. (1992). Neuroleptic sensitivity in patients with senile dementia of Lewy body type. BMJ, 305(6855), 673-678.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q779",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Intermediate",
        "questionText": "A 58-year-old corporate executive begins making crude sexual remarks in meetings, stealing candy from children's hands, stuffing his mouth with excessive amounts of food (hyperorality), and exhibiting profound apathy and complete lack of empathy toward his grieving wife. Neuropsychological testing shows impaired executive function but intact episodic memory. What neurodegenerative disorder is indicated?",
        "options": [
            {"id": "A", "text": "Behavioural Variant Frontotemporal Dementia (bvFTD)"},
            {"id": "B", "text": "Typical late-onset Alzheimer's disease"},
            {"id": "C", "text": "Huntington's disease with chorea"},
            {"id": "D", "text": "Normal pressure hydrocephalus"}
        ],
        "correctAnswer": "A",
        "explanation": "Behavioural variant Frontotemporal Dementia (bvFTD) is characterized by early and progressive changes in personality and social conduct: loss of inhibition (socially inappropriate behavior), apathy, loss of sympathy/empathy, perseverative/compulsive behaviors, and hyperorality/dietary changes, with relative preservation of episodic memory and visuospatial functions early on.",
        "incorrectExplanations": {
            "B": "Alzheimer's disease typically begins with prominent episodic memory deficits, not early social disinhibition.",
            "C": "Huntington's disease is marked by choreiform involuntary motor movements and autosomal dominant family history.",
            "D": "Normal pressure hydrocephalus presents with the classic triad of wet, wacky, and wobbly (incontinence, cognitive decline, gait apraxia)."
        },
        "learningObjective": "Identify the clinical diagnostic criteria and neurobehavioural signs of Behavioural Variant Frontotemporal Dementia (bvFTD).",
        "reference": "Rascovsky, K., et al. (2011). Sensitivity of revised diagnostic criteria for the behavioural variant of frontotemporal dementia. Brain, 134(9), 2456-2477.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q780",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Intermediate",
        "questionText": "In Tom Kitwood's pioneering framework of Person-Centred Care for dementia, how should Behavioural and Psychological Symptoms of Dementia (BPSD—such as shouting, pacing, and resisting personal care) be understood by psychiatric nurses?",
        "options": [
            {"id": "A", "text": "As intentional hostility and malice designed to manipulate ward staff"},
            {"id": "B", "text": "As random, meaningless biological electrical discharges requiring immediate sedation"},
            {"id": "C", "text": "As meaningful expressions of unmet physical, psychological, or emotional needs (such as unmanaged pain, fear, boredom, loneliness, sensory overload, or loss of dignity) communicating distress when verbal faculties have failed"},
            {"id": "D", "text": "As proof that the person has lost all human consciousness"}
        ],
        "correctAnswer": "C",
        "explanation": "Tom Kitwood's person-centred dementia care model conceptualizes BPSD not as random brain pathology, but as communication of unmet human needs. When cognitive decline impairs verbal articulation, behavioral disturbances (agitation, wandering, shouting, resistance) become the individual's language expressing pain, cold, hunger, fear, boredom, or loss of identity.",
        "incorrectExplanations": {
            "A": "Kitwood rejected pathologizing or blaming the individual; behaviors are not malicious manipulations.",
            "B": "Viewing behavior as meaningless biological noise justifies chemical restraint, which Kitwood strongly opposed.",
            "D": "Person-centred care asserts that personhood remains intact throughout the dementia journey."
        },
        "learningObjective": "Apply Tom Kitwood's Person-Centred Care framework to interpret BPSD as communication of unmet human needs.",
        "reference": "Kitwood, T. (1997). Dementia Reconsidered: The Person Comes First. Open University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q781",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Advanced",
        "questionText": "An 81-year-old resident with moderate Alzheimer's dementia becomes intensely agitated, screaming and striking out at care staff, every afternoon at 15:00 when staff attempt to assist her with showering. When applying the evidence-based DICE (Describe, Investigate, Create, Evaluate) framework, what non-pharmacological nursing intervention should be tested?",
        "options": [
            {"id": "A", "text": "Administer intramuscular haloperidol 5 mg 30 minutes before every shower"},
            {"id": "B", "text": "Investigate underlying precipitants (e.g., cold bathroom temperature, fear of water spray, undressed vulnerability, arthritis pain); modify the routine by warming the room, playing preferred relaxing music, using a towel bath or gentle sponge bath, and scheduling pre-wash analgesia"},
            {"id": "C", "text": "Restrain the resident's wrists with leather restraints during all washing procedures"},
            {"id": "D", "text": "Cease all washing permanently and ignore the resident's hygiene for the rest of her life"}
        ],
        "correctAnswer": "B",
        "explanation": "The DICE approach (Kales et al.) systematically investigates behavioral triggers. In shower-related agitation, common triggers include cold bathrooms, arthritis pain when moving, and terror from water spraying directly in the face. Interventions such as warming towels, playing soothing music, providing pre-emptive analgesia, and adapting to sponge/towel baths successfully reduce distress without psychotropic medications.",
        "incorrectExplanations": {
            "A": "Chemical restraint carries high stroke and mortality risks and fails to address the underlying sensory fear.",
            "C": "Physical restraint induces terror, trauma, physical injuries, and breaches human rights.",
            "D": "Abandoning hygiene leads to skin breakdown, pressure sores, and severe infection."
        },
        "learningObjective": "Formulate non-pharmacological behavioral interventions for BPSD utilizing the DICE assessment approach.",
        "reference": "Kales, H. C., et al. (2014). Management of neuropsychiatric symptoms of dementia in clinical settings: recommendations from a multidisciplinary expert panel. Journal of the American Geriatrics Society, 62(4), 762-769.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q782",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Advanced",
        "questionText": "A psychiatric nurse is reviewing the pharmacological profile of Acetylcholinesterase Inhibitors (Donepezil, Rivastigmine, Galantamine) prescribed for mild to moderate Alzheimer's disease. What core mechanism of action and common cholinergic adverse effects must the nurse monitor?",
        "options": [
            {"id": "A", "text": "They reversibly inhibit acetylcholinesterase, increasing synaptic acetylcholine; common adverse effects include nausea, diarrhea, anorexia, bradycardia, syncope, and vivid dreams/insomnia"},
            {"id": "B", "text": "They block dopamine D2 receptors; common adverse effects include tardive dyskinesia and agranulocytosis"},
            {"id": "C", "text": "They stimulate GABA-A receptors; common adverse effects include respiratory arrest and rapid addiction"},
            {"id": "D", "text": "They deplete brain serotonin; common adverse effects include severe hypertensive crisis"}
        ],
        "correctAnswer": "A",
        "explanation": "Cholinesterase inhibitors (Donepezil, Rivastigmine, Galantamine) enhance central cholinergic neurotransmission by preventing the enzymatic breakdown of acetylcholine. Systemic cholinergic stimulation commonly causes gastrointestinal side effects (nausea, vomiting, diarrhea, weight loss) and cardiovascular effects, notably vagal-mediated bradycardia, heart block, and syncope.",
        "incorrectExplanations": {
            "B": "D2 receptor blockade characterizes antipsychotics, not cholinesterase inhibitors.",
            "C": "GABA-A stimulation is the mechanism of benzodiazepines and barbiturates.",
            "D": "Serotonin depletion is not the mechanism of cholinesterase inhibitors."
        },
        "learningObjective": "Explain the pharmacodynamics, clinical indications, and cholinergic adverse effects of cholinesterase inhibitors.",
        "reference": "Birks, J. S. (2006). Cholinesterase inhibitors for Alzheimer's disease. Cochrane Database of Systematic Reviews, (1), CD005593.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q783",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Advanced",
        "questionText": "What is the unique pharmacological mechanism of action and primary clinical indication for Memantine in the management of Alzheimer's disease?",
        "options": [
            {"id": "A", "text": "Irreversible monoamine oxidase B inhibition; indicated for acute ischemic stroke"},
            {"id": "B", "text": "Serotonin-norepinephrine reuptake inhibition; indicated for mild insomnia"},
            {"id": "C", "text": "High-affinity dopamine receptor agonism; indicated for early frontotemporal dementia"},
            {"id": "D", "text": "Low-to-moderate affinity, uncompetitive N-methyl-D-aspartate (NMDA) receptor antagonist that protects cholinergic neurons from pathological glutamate excitotoxicity; approved for moderate to severe Alzheimer's disease"}
        ],
        "correctAnswer": "D",
        "explanation": "Memantine is an uncompetitive NMDA receptor antagonist. By blocking pathological tonic influx of calcium through NMDA receptor channels while allowing physiological transmission required for learning, Memantine protects neurons from chronic glutamate-mediated excitotoxicity. It is approved for moderate to severe Alzheimer's disease (either alone or combined with a cholinesterase inhibitor).",
        "incorrectExplanations": {
            "A": "MAO-B inhibitors (e.g. selegiline) are used in Parkinson's disease, not Memantine's mechanism.",
            "B": "Memantine does not inhibit serotonin or norepinephrine reuptake.",
            "C": "Memantine is an NMDA antagonist, not a dopamine agonist."
        },
        "learningObjective": "Differentiate the neurobiological mechanism, glutamatergic pathways, and clinical indications of Memantine in moderate-to-severe Alzheimer's disease.",
        "reference": "Reisberg, B., et al. (2003). Memantine in moderate-to-severe Alzheimer's disease. New England Journal of Medicine, 348(14), 1333-1341.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q784",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Dementia types and management",
        "difficulty": "Expert",
        "questionText": "Regulatory agencies (such as the UK MHRA and US FDA) issued stringent safety warnings regarding the off-label prescription of typical and atypical antipsychotics for Behavioural and Psychological Symptoms of Dementia (BPSD). What specific clinical risks prompted these warnings, and what governance rules apply?",
        "options": [
            {"id": "A", "text": "Antipsychotics cause rapid hair loss; treatment must be stopped if alopecia occurs"},
            {"id": "B", "text": "Antipsychotics are 100% curable but cause severe tooth discoloration"},
            {"id": "C", "text": "A clear, statistically significant increased risk of cerebrovascular adverse events (stroke, transient ischemic attack) and an approximate 1.6- to 1.7-fold increase in all-cause mortality; prescribing must be restricted to severe distress/danger, used at the lowest dose, and time-limited to a maximum of 6-12 weeks with mandatory regular review"},
            {"id": "D", "text": "Antipsychotics are completely safe and should be added to drinking water across care homes"}
        ],
        "correctAnswer": "C",
        "explanation": "Meta-analyses of randomized trials revealed that elderly patients with dementia treated with antipsychotics have a significantly elevated risk of stroke (3-fold increase) and all-cause mortality (approx. 1.6-1.7x higher, primarily from cardiovascular events and aspiration pneumonia). Antipsychotics should be prescribed only for severe distress/danger, at minimal doses, and time-limited to 6-12 weeks with regular multidisciplinary review.",
        "incorrectExplanations": {
            "A": "The black box warnings focus on fatal stroke and death, not cosmetic hair loss.",
            "B": "Antipsychotics do not cure dementia and warnings are not based on dental coloration.",
            "D": "Antipsychotics carry profound mortality risks in dementia and require rigorous prescription auditing."
        },
        "learningObjective": "Critique regulatory black-box warnings, stroke risks, and time-limited prescribing governance for antipsychotic use in dementia.",
        "reference": "Banerjee, S. (2009). The use of antipsychotic medication for people with dementia: Time for action. UK Department of Health.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 8: Late-life depression (MHN-Q785 - MHN-Q794)
    # Target Answers: B, D, A, C, B, D, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q785",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Foundation",
        "questionText": "In geriatric psychiatric nursing, what is 'Masked Depression' (or 'Depression without Sadness') in older adults?",
        "options": [
            {"id": "A", "text": "A clinical trial where patients wear carnival masks during psychotherapy"},
            {"id": "B", "text": "A common presentation in older adults where overt sadness or depressed mood is denied, and the illness presents predominantly with multiple vague somatic complaints, hypochondriasis, severe apathy, psychomotor retardation, and cognitive slowing"},
            {"id": "C", "text": "A severe allergic dermatological rash covering the facial bones"},
            {"id": "D", "text": "Malingering designed to obtain unnecessary orthopaedic walking sticks"}
        ],
        "correctAnswer": "B",
        "explanation": "Older adults with major depression frequently minimize or completely deny feelings of sadness or dysphoria (depression without sadness). Instead, they present with prominent somatic complaints (unexplained gastrointestinal pain, musculoskeletal aches, fatigue), preoccupation with bodily functions (hypochondriasis), psychomotor retardation, and apathy.",
        "incorrectExplanations": {
            "A": "Masked depression is a clinical psychiatric concept, not a literal mask ceremony.",
            "C": "It is a neuropsychiatric affective disorder, not a dermatological condition.",
            "D": "Somatic distress in geriatric depression is genuine suffering, not malingering."
        },
        "learningObjective": "Identify atypical presentations of late-life depression, including masked depression and somatic focus.",
        "reference": "Alexopoulos, G. S. (2005). Depression in the elderly. The Lancet, 365(9475), 1961-1970.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q786",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Foundation",
        "questionText": "A 78-year-old retired schoolteacher presents with sudden-onset cognitive impairment, scoring poorly on MMSE orientation and recall. During testing, she frequently responds 'I don't know' or 'I can't do this,' appears tearful and distressed about her memory loss, and her family notes the memory problems began abruptly after her sister died two months ago. What condition is most likely?",
        "options": [
            {"id": "A", "text": "End-stage Huntington's disease"},
            {"id": "B", "text": "Creutzfeldt-Jakob prion encephalopathy"},
            {"id": "C", "text": "Korsakoff confabulatory psychosis"},
            {"id": "D", "text": "Depressive Pseudodementia (Depressive Cognitive Impairment)"}
        ],
        "correctAnswer": "D",
        "explanation": "Depressive Pseudodementia refers to cognitive impairment secondary to severe major depression. Key distinguishing features include abrupt onset following an emotional trigger, prominent distress/complaints about cognitive deficits, 'I don't know' answers indicating poor effort/motivation, and complete reversal of cognitive deficits once the underlying depression is treated.",
        "incorrectExplanations": {
            "A": "Huntington's involves prominent choreiform movements and chronic genetic decline.",
            "B": "Creutzfeldt-Jakob involves myoclonus, ataxia, and rapid death within months.",
            "C": "Korsakoff patients confabulate to cover memory gaps and are unconcerned; pseudodementia patients say 'I don't know' and are distressed."
        },
        "learningObjective": "Differentiate depressive pseudodementia from primary neurodegenerative dementia.",
        "reference": "Wells, C. E. (1979). Pseudodementia. American Journal of Psychiatry, 136(7), 895-900.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q787",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Intermediate",
        "questionText": "Why is the Geriatric Depression Scale (GDS, such as the GDS-15) preferred over general depression instruments (like the Beck Depression Inventory or Hamilton-D) when screening for depression in medically ill older adults?",
        "options": [
            {"id": "A", "text": "The GDS deliberately omits or minimizes somatic and vegetative symptom items (such as fatigue, insomnia, and appetite changes) that are frequently confounded by physical co-morbidities and normal ageing"},
            {"id": "B", "text": "The GDS requires patients to run on a treadmill for 20 minutes to measure heart rate"},
            {"id": "C", "text": "The GDS is the only test that can be administered legally by law enforcement officers"},
            {"id": "D", "text": "The GDS measures electrical brain waves through skin electrodes"}
        ],
        "correctAnswer": "A",
        "explanation": "Standard adult depression inventories heavily weigh somatic/vegetative symptoms (weight loss, sleep changes, fatigue, bodily aches). In older adults, these symptoms frequently stem from physical illnesses (arthritis, heart failure) or normal physiological ageing, yielding false-positive scores. The GDS focuses on cognitive and affective symptoms (hopelessness, boredom, satisfaction).",
        "incorrectExplanations": {
            "B": "The GDS is a brief 15-item questionnaire, not an athletic exercise test.",
            "C": "The GDS is a validated clinical psychometric instrument used by healthcare professionals.",
            "D": "The GDS is a questionnaire, not an electroencephalogram."
        },
        "learningObjective": "Explain the diagnostic rationale and structural advantages of the Geriatric Depression Scale (GDS-15).",
        "reference": "Yesavage, J. A., et al. (1982). Development and validation of a geriatric depression screening scale: a preliminary report. Journal of Psychiatric Research, 17(1), 37-49.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q788",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Intermediate",
        "questionText": "What does the 'Vascular Depression Hypothesis' (Alexopoulos et al.) propose regarding the pathophysiology and clinical characteristics of late-onset depression in older adults?",
        "options": [
            {"id": "A", "text": "Depression is caused entirely by low blood pressure in the pedal extremities"},
            {"id": "B", "text": "Depression is an acute allergic reaction to cholesterol-lowering statin drugs"},
            {"id": "C", "text": "Cerebrovascular pathology (subcortical ischemic white matter hyperintensities) disrupts frontostriatal neural circuits, producing a distinct clinical syndrome characterized by executive dysfunction, psychomotor slowing, apathy, and poorer response to conventional monoaminergic antidepressants"},
            {"id": "D", "text": "Vascular depression occurs exclusively in healthy young endurance swimmers"}
        ],
        "correctAnswer": "C",
        "explanation": "The Vascular Depression Hypothesis posits that cerebrovascular disease (microvascular ischemia, white matter hyperintensities) damages subcortical and frontostriatal pathways governing mood and executive function. Patients present with late-onset depression, prominent executive dysfunction (depressive-dysexecutive syndrome), apathy, psychomotor slowing, and treatment resistance to standard SSRIs.",
        "incorrectExplanations": {
            "A": "Vascular depression involves cerebral microvascular ischemia, not pedal blood pressure.",
            "B": "Statins do not cause vascular depression; controlling vascular risk factors is preventive.",
            "D": "Vascular depression affects older adults with cerebrovascular risk factors (hypertension, diabetes)."
        },
        "learningObjective": "Analyze the Vascular Depression Hypothesis and its implications for frontostriatal disruption and antidepressant response.",
        "reference": "Alexopoulos, G. S., et al. (1997). 'Vascular depression' hypothesis. Archives of General Psychiatry, 54(10), 915-922.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q789",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Intermediate",
        "questionText": "An 83-year-old woman with severe late-life psychotic depression is bedbound, refusing all oral food and hydration, expresses severe nihilistic delusions ('my organs are dead and rotting'), and has failed two trials of antidepressants. Why is Electroconvulsive Therapy (ECT) considered a first-line treatment in this clinical emergency?",
        "options": [
            {"id": "A", "text": "ECT is a punitive behavioral measure used to force patients to eat"},
            {"id": "B", "text": "ECT has exceptional efficacy (~80%) and rapid therapeutic response in severe, psychotic, and life-threatening depression; it is safe and well-tolerated in older adults, rapidly restoring oral intake and reversing life-threatening dehydration"},
            {"id": "C", "text": "ECT is mandatory by law whenever a patient reaches age 80"},
            {"id": "D", "text": "ECT permanently cures all neurodegenerative diseases within 24 hours"}
        ],
        "correctAnswer": "B",
        "explanation": "ECT is one of the most effective, rapid, and life-saving psychiatric interventions available for severe late-life depression—especially with psychotic features (Cotard's syndrome / nihilistic delusions) or life-threatening refusal of food/fluids. It has an 80% response rate in older adults and is physiologically well-tolerated under modern anesthesia.",
        "incorrectExplanations": {
            "A": "ECT is a safe biological medical treatment, never a punitive disciplinary tool.",
            "C": "Age is never a mandatory criterion for ECT; indications are clinical severity and urgency.",
            "D": "ECT treats affective and psychotic episodes; it does not cure underlying neurodegeneration."
        },
        "learningObjective": "Evaluate the clinical indications, efficacy, and emergency safety profile of Electroconvulsive Therapy (ECT) in geriatric depression.",
        "reference": "Kellner, C. H., et al. (2016). ECT in treatment-resistant depression. American Journal of Psychiatry, 173(9), 856-862.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q790",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Intermediate",
        "questionText": "When prescribing Citalopram for late-life depression in older adults (aged 60 years and older), what maximum daily dosage is mandated by regulatory safety alerts (FDA/MHRA), and what cardiac hazard dictates this limit?",
        "options": [
            {"id": "A", "text": "Maximum 80 mg/day due to acute renal failure"},
            {"id": "B", "text": "Maximum 5 mg/day due to acute gastric perforation"},
            {"id": "C", "text": "Maximum 100 mg/day due to retinal detachment"},
            {"id": "D", "text": "Maximum 20 mg/day due to dose-dependent QTc prolongation on the electrocardiogram, which carries a risk of fatal Torsades de Pointes ventricular arrhythmias"}
        ],
        "correctAnswer": "D",
        "explanation": "Regulatory agencies capped the maximum daily dose of Citalopram at 20 mg/day in adults aged 60 years and older (and 10 mg/day for escitalopram). At higher doses, these agents cause dose-dependent prolongation of the cardiac QTc interval, predisposing frail older adults to fatal Torsades de Pointes ventricular arrhythmias.",
        "incorrectExplanations": {
            "A": "80 mg/day is a toxic overdose that severely prolongs the QTc interval.",
            "B": "5 mg is a subtherapeutic dose, and SSRIs do not cause acute gastric perforation.",
            "C": "100 mg is a lethal dose for citalopram; retinal detachment is not the primary mechanism."
        },
        "learningObjective": "Identify geriatric dosage ceilings and QTc prolongation risks associated with citalopram in older adults.",
        "reference": "FDA. (2012). FDA Drug Safety Communication: Revised recommendations for Celexa (citalopram hydrobromide) related to a potential risk of abnormal heart rhythms.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q791",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Advanced",
        "questionText": "An 82-year-old woman taking a thiazide diuretic for hypertension is initiated on Sertraline 50 mg/day for late-life depression. Two weeks later, she presents to the clinic with profound lethargy, confusion, nausea, unsteady gait, and muscle weakness. What metabolic complication must the psychiatric nurse investigate immediately?",
        "options": [
            {"id": "A", "text": "Severe hypercalcemia from parathyroid adenoma"},
            {"id": "B", "text": "Antidepressant-induced Syndrome of Inappropriate Antidiuretic Hormone Secretion (SIADH) resulting in severe hyponatremia (serum sodium <125 mmol/L)"},
            {"id": "C", "text": "Acute diabetic ketoacidosis"},
            {"id": "D", "text": "Acute gouty arthritis of the metatarsophalangeal joint"}
        ],
        "correctAnswer": "B",
        "explanation": "Antidepressant-induced SIADH and hyponatremia are common and potentially life-threatening adverse reactions in older adults taking SSRIs or SNRIs. The risk is multiplied when combined with other sodium-depleting agents such as thiazide diuretics. Symptoms include lethargy, confusion, gait instability (causing falls), nausea, and seizures.",
        "incorrectExplanations": {
            "A": "SSRIs do not induce hypercalcemic parathyroid crises.",
            "C": "DKA features profound hyperglycemia, tachypnea, and ketosis, not thiazide-SSRI hyponatremia.",
            "D": "Gout causes intense localized joint erythema and pain, not generalized confusion and lethargy."
        },
        "learningObjective": "Manage antidepressant-induced SIADH and severe hyponatremia in geriatric psychopharmacology.",
        "reference": "Fabian, T. J., et al. (2004). Paroxetine-induced hyponatremia in the elderly: A randomized controlled trial. Archives of Internal Medicine, 164(3), 327-332.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q792",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Advanced",
        "questionText": "Epidemiological data reveals that older men (aged 75-85+ years) consistently display among the highest completed suicide rates of any demographic group globally. What clinical and psychological characteristics distinguish suicide in late life from suicide in younger populations?",
        "options": [
            {"id": "A", "text": "Older adults make dozens of non-lethal, impulsive suicidal gestures to seek social attention"},
            {"id": "B", "text": "Late-life suicide is almost exclusively driven by illicit recreational ecstasy use"},
            {"id": "C", "text": "Suicide attempts in older adults have a very low lethality ratio (1 death per 200 attempts)"},
            {"id": "D", "text": "Older adults exhibit higher suicidal intent, utilize more violent and lethal means (firearms, hanging), make fewer communicative warnings or threats, have lower attempt-to-completion ratios (1 death per 2-4 attempts), and are physically less resilient to survive tissue trauma"}
        ],
        "correctAnswer": "D",
        "explanation": "Late-life suicide is characterized by high lethal intent. While younger people have an attempt-to-completion ratio of roughly 25:1, in older adults the ratio is roughly 4:1 (or 2:1 in frail men). Older adults plan suicides meticulously, express fewer overt cries for help, use highly lethal means, and have less physiological reserve to survive attempts.",
        "incorrectExplanations": {
            "A": "Older adults rarely make non-lethal ambivalent gestures; intent is typically determined and lethal.",
            "B": "Late-life suicide is driven by depression, physical multimorbidity, chronic pain, and bereavement, not club drugs.",
            "C": "Older adults have an exceptionally high lethality ratio, not a low one."
        },
        "learningObjective": "Analyze epidemiological risk profiles and lethal intent dynamics in late-life suicide.",
        "reference": "Conwell, Y., et al. (2011). Suicide in older adults. Psychiatric Clinics of North America, 34(2), 451-468.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q793",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Advanced",
        "questionText": "A mental health nurse conducts a structured psychosocial group in an assisted living facility utilizing 'Reminiscence and Life Review Therapy' (Butler). How does this evidence-based intervention operate to alleviate late-life depressive symptoms?",
        "options": [
            {"id": "A", "text": "By facilitating structured, progressive recall and re-evaluation of past life events, unresolved conflicts, and achievements, fostering ego integrity versus despair (Erikson) and restoring meaning and self-worth"},
            {"id": "B", "text": "By forcing participants to forget all past memories through intensive hypnosis"},
            {"id": "C", "text": "By requiring residents to engage in silent meditation without speaking for 6 weeks"},
            {"id": "D", "text": "By assigning competitive written exams regarding historical facts"}
        ],
        "correctAnswer": "A",
        "explanation": "Robert Butler's Life Review and Reminiscence Therapy is an evidence-based psychotherapy for older adults. Based on Erik Erikson's developmental stage of 'Ego Integrity vs Despair,' it guides individuals to recall, evaluate, and integrate positive and painful life experiences, resolve past conflicts, find meaning, and enhance self-worth.",
        "incorrectExplanations": {
            "B": "Life review encourages rich, intentional biographical recall, the exact opposite of memory suppression.",
            "C": "Life review is a rich conversational narrative group, not silent isolation.",
            "D": "It explores personal subjective life meanings, not academic historical exams."
        },
        "learningObjective": "Apply Reminiscence and Life Review therapy principles within geriatric mental health nursing practice.",
        "reference": "Bohlmeijer, E., et al. (2003). The effects of reminiscence on psychological well-being in older adults: A meta-analysis. International Journal of Aging and Human Development, 57(1), 69-94.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q794",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Late-life depression",
        "difficulty": "Expert",
        "questionText": "An advanced practice psychiatric nurse is managing a 79-year-old patient with severe, treatment-resistant major depression who has not responded to an optimized trial of Venlafaxine. The team considers lithium augmentation. What specific pharmacokinetic considerations and therapeutic serum level targets apply to lithium therapy in older adults?",
        "options": [
            {"id": "A", "text": "Older adults clear lithium faster than young adults; target serum level should be 1.2 to 1.5 mmol/L"},
            {"id": "B", "text": "Lithium is entirely metabolized by the liver, so renal function is irrelevant"},
            {"id": "C", "text": "Due to age-related reductions in glomerular filtration rate (GFR) and heightened central nervous system sensitivity, older adults require lower daily doses, and the therapeutic serum concentration target is lower (typically 0.4 to 0.6 mmol/L) to prevent severe neurotoxicity"},
            {"id": "D", "text": "Lithium is strictly contraindicated in all individuals over age 65 under international law"}
        ],
        "correctAnswer": "C",
        "explanation": "In older adults, renal GFR decreases substantially, prolonging lithium elimination half-life and predisposing them to rapid accumulation. Furthermore, ageing brains exhibit increased sensitivity to neurotoxicity (tremor, ataxia, confusion, delirium). Target therapeutic serum levels for late-life depression augmentation are lower (0.4-0.6 mmol/L) than in young adults (0.6-0.8+ mmol/L).",
        "incorrectExplanations": {
            "A": "Older adults have reduced renal clearance, and levels of 1.2-1.5 mmol/L produce life-threatening toxicity.",
            "B": "Lithium is excreted 100% unchanged through the kidneys; hepatic metabolism is zero.",
            "D": "Lithium is widely and safely used in older adults with careful dosing and therapeutic drug monitoring."
        },
        "learningObjective": "Formulate safe lithium augmentation strategies, renal clearance adaptations, and therapeutic level targets for geriatric depression.",
        "reference": "Young, R. C., et al. (2017). Geriatric bipolar disorder: a review of treatment options. Drugs & Aging, 34(12), 895-906.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 9: Elder abuse and safeguarding (MHN-Q795 - MHN-Q804)
    # Target Answers: A, C, B, D, A, C, B, A, D, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q795",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Foundation",
        "questionText": "Under statutory adult safeguarding frameworks (e.g. UK Care Act 2014) and WHO guidelines, what are the primary recognized categories of elder abuse and mistreatment?",
        "options": [
            {"id": "A", "text": "Physical abuse, Psychological/Emotional abuse, Financial/Material abuse, Sexual abuse, Neglect (and acts of omission), and Organisational/Institutional abuse"},
            {"id": "B", "text": "Late retirement, Choosing not to exercise, Eating sweets, and Watching television"},
            {"id": "C", "text": "Moving to a warmer climate and selling a vehicle"},
            {"id": "D", "text": "Attending bingo games and forgetting an anniversary"}
        ],
        "correctAnswer": "A",
        "explanation": "Statutory adult safeguarding frameworks recognize six core domains of adult abuse: 1) Physical abuse, 2) Domestic abuse / emotional abuse, 3) Sexual abuse, 4) Financial or material abuse, 5) Neglect and acts of omission, and 6) Organisational or institutional abuse (plus modern categories of self-neglect and modern slavery).",
        "incorrectExplanations": {
            "B": "Lifestyle choices and leisure activities are personal liberties, not safeguarding abuse categories.",
            "C": "Relocation and asset sales are standard life events when conducted autonomously.",
            "D": "Minor social memory lapses are normal cognitive occurrences, not maltreatment."
        },
        "learningObjective": "Recall the statutory categories of elder abuse and adult safeguarding under the Care Act 2014.",
        "reference": "Department of Health and Social Care. (2014). Care and Support Statutory Guidance (Care Act 2014). UK Government.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q796",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Foundation",
        "questionText": "A community psychiatric nurse is visiting an 84-year-old woman with moderate vascular dementia. The nurse discovers that the patient's heating has been shut off for non-payment, there is no food in the cupboards, and bank statements reveal sudden recent ATM cash withdrawals of £500 every three days by a distant nephew who recently moved into the home. What category of elder abuse is suspected?",
        "options": [
            {"id": "A", "text": "Physical abuse"},
            {"id": "B", "text": "Medical malpractice"},
            {"id": "C", "text": "Financial or material abuse (exploitation)"},
            {"id": "D", "text": "Discriminatory religious abuse"}
        ],
        "correctAnswer": "C",
        "explanation": "Financial or material abuse involves the unauthorized, improper, or illegal use of an older person's funds, property, pension, or assets. Key indicators include unexplained ATM withdrawals, sudden alterations in bank accounts, missing valuables, and failure to pay essential utility or food bills despite adequate personal funds.",
        "incorrectExplanations": {
            "A": "While neglect is co-occurring, the active misappropriation of funds defines financial abuse.",
            "B": "Medical malpractice involves professional clinical negligence, not theft by family relatives.",
            "D": "There is no indication of religious discrimination in this financial exploitation."
        },
        "learningObjective": "Recognize behavioral and financial indicators of elder financial abuse and exploitation.",
        "reference": "National Center on Elder Abuse (NCEA). (2020). Research, Practice, Policy: Financial Exploitation of Older Adults.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q797",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Foundation",
        "questionText": "An 80-year-old man who resides with his son is brought to an outpatient clinic. Physical assessment reveals bilateral, symmetrical fingertip-sized oval bruises on the medial aspects of both upper arms, as well as bruising along his posterior neck. How should the nurse interpret these physical findings?",
        "options": [
            {"id": "A", "text": "Normal senile purpura resulting from minor bumping against furniture"},
            {"id": "B", "text": "Suspicious indicators of physical abuse, specifically 'grip marks' consistent with forceful grabbing, shaking, or restraint by another person"},
            {"id": "C", "text": "Cutaneous manifestations of acute dietary vitamin D deficiency"},
            {"id": "D", "text": "Insect bites sustained in the garden"}
        ],
        "correctAnswer": "B",
        "explanation": "Bilateral bruising on the inner (medial) aspects of the upper arms typically represents 'grip marks'—injuries caused when a caregiver or perpetrator forcefully grabs, holds, shakes, or restrains an older adult. Senile purpura occurs on the extensor surfaces (backs of hands, forearms) over bony areas, not medial protected arm surfaces.",
        "incorrectExplanations": {
            "A": "Senile purpura occurs on extensor surfaces of hands and forearms, not bilateral inner arms.",
            "C": "Vitamin D deficiency causes osteomalacia, not bilateral grip-pattern hematomas.",
            "D": "Large bilateral grip hematomas bear no resemblance to insect stings."
        },
        "learningObjective": "Differentiate suspicious physical abuse injury patterns (such as grip marks) from benign age-related skin changes (senile purpura).",
        "reference": "Wiglesworth, A., et al. (2009). Bruising as a marker of physical elder abuse. Journal of the American Geriatrics Society, 57(7), 1191-1196.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q798",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Intermediate",
        "questionText": "In the epidemiological literature on elder abuse etiology, which caregiver characteristics are most strongly associated with an increased risk of perpetrating abuse against a dependent older adult?",
        "options": [
            {"id": "A", "text": "Caregiver attending regular weekly peer support groups and using respite services"},
            {"id": "B", "text": "Caregiver having a high personal income and living in a separate home"},
            {"id": "C", "text": "Caregiver having a professional qualification in clinical gerontology"},
            {"id": "D", "text": "Caregiver substance use disorder, untreated caregiver psychiatric illness, high caregiver burden/burnout, financial dependency on the older adult, and a personal history of family violence"}
        ],
        "correctAnswer": "D",
        "explanation": "Caregiver risk factors for elder abuse include substance misuse, mental illness, high levels of stress/burnout, co-residence, financial dependence on the older person (which breeds resentment), and historical domestic violence. When severe caregiver stress meets cognitive impairment in the elder, abuse risk rises significantly.",
        "incorrectExplanations": {
            "A": "Attending support groups and using respite care are protective factors that prevent burnout.",
            "B": "Living independently and financial independence reduce domestic friction and dependency.",
            "C": "Professional gerontological training improves understanding and provides coping skills."
        },
        "learningObjective": "Identify caregiver risk factors that contribute to elder abuse and mistreatment.",
        "reference": "Burnes, D., et al. (2015). Prevalence of and risk factors for elder abuse: A systematic review. American Journal of Public Health, 105(8), e56-e64.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q799",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Intermediate",
        "questionText": "An advanced practice psychiatric nurse assesses an 86-year-old widow living with severe cognitive impairment and osteoarthritis. What specific vulnerability factors make this patient particularly susceptible to domestic elder abuse?",
        "options": [
            {"id": "A", "text": "Cognitive impairment (inability to comprehend or report abuse), physical functional dependency for basic ADLs, social isolation, and fear of being abandoned or institutionalized if she complains"},
            {"id": "B", "text": "Holding a valid passport and driver's license"},
            {"id": "C", "text": "Having a high pension and living in an urban apartment"},
            {"id": "D", "text": "Regular daily visits from multiple community healthcare workers"}
        ],
        "correctAnswer": "A",
        "explanation": "Older adult vulnerability factors include cognitive deficits (dementia compromises memory, judgment, and ability to communicate abuse), physical dependency (relying on the abuser for food, toileting, medications), social isolation (lack of outside observers), and fear that reporting abuse will result in placement in a nursing home.",
        "incorrectExplanations": {
            "B": "Passports and licenses are civil documents that do not increase elder vulnerability.",
            "C": "Financial resources alone do not constitute functional vulnerability.",
            "D": "Frequent visits from professional healthcare workers provide oversight and serve as protective factors."
        },
        "learningObjective": "Assess vulnerable adult risk factors predisposing older individuals to exploitation and abuse.",
        "reference": "Dong, X. Q. (2015). Elder abuse: Systematic review and implications for practice. Journal of the American Geriatrics Society, 63(6), 1214-1238.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q800",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Intermediate",
        "questionText": "A community psychiatric nurse is referred to visit an 82-year-old man living alone in severe domestic squalor (Diogenes Syndrome). The home is filled to the ceiling with rotting rubbish, human waste, and vermin; the man is emaciated, unwashed, with maggot-infested leg ulcers, but adamantly refuses all medical care and cleaning assistance, shouting 'Leave me alone in my house!' What clinical priority must the nurse address first?",
        "options": [
            {"id": "A", "text": "Accept his refusal immediately and close the file because adults have the right to live in squalor"},
            {"id": "B", "text": "Arrest the man for municipal code littering violations"},
            {"id": "C", "text": "Conduct an urgent, comprehensive assessment of mental capacity regarding his health, self-care, and living conditions; assess physical acuity, and initiate an adult safeguarding alert for severe self-neglect"},
            {"id": "D", "text": "Set fire to the rubbish piles to eradicate the vermin"}
        ],
        "correctAnswer": "C",
        "explanation": "Severe self-neglect (Diogenes syndrome) presents acute health and mortality risks. The nurse's immediate duty is to evaluate mental capacity: does the patient understand the immediate risks to life, retain information, and weigh the consequences? An urgent adult safeguarding alert for self-neglect and multi-agency environmental triage must be enacted.",
        "incorrectExplanations": {
            "A": "Closing the file when life-threatening neglect and infected ulcers are present breaches duty of care.",
            "B": "Self-neglect is a clinical and social crisis, not a criminal matter.",
            "D": "Setting fires is a criminal act and would kill the resident."
        },
        "learningObjective": "Manage severe self-neglect (Diogenes Syndrome) and execute mental capacity and safeguarding assessments.",
        "reference": "Braye, S., Orr, D., & Preston-Shoot, M. (2014). Self-Neglect Policy and Practice: Building an Evidence Base for Adult Social Care. SCIE Report 46.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q801",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Advanced",
        "questionText": "Under the Mental Capacity Act (MCA) 2005, what are the five statutory core principles that must guide clinical decision-making when safeguarding an older adult?",
        "options": [
            {"id": "A", "text": "1) Immediate detention, 2) Chemical restraint, 3) Asset seizure, 4) Paternalism, and 5) Permanent institutionalization"},
            {"id": "B", "text": "1) Presumption of capacity, 2) All practicable steps to support decision-making, 3) The right to make unwise decisions, 4) Best interests determinations (when capacity is lacking), and 5) Least restrictive intervention"},
            {"id": "C", "text": "1) Presumption of incapacity, 2) Doctor knows best, 3) Family votes determine care, 4) Mandatory hospitalization, and 5) Cost minimization"},
            {"id": "D", "text": "1) Criminal trial, 2) Police escort, 3) Prison placement, 4) Solitary confinement, and 5) Parole"}
        ],
        "correctAnswer": "B",
        "explanation": "The five statutory principles of the UK Mental Capacity Act 2005 are: 1) A person must be assumed to have capacity unless proven otherwise; 2) A person cannot be treated as unable to make a decision unless all practicable steps to help them have failed; 3) A person is not to be treated as lacking capacity merely because they make an unwise decision; 4) Acts done for a person lacking capacity must be in their 'best interests'; 5) The decision must be the least restrictive of basic rights and freedoms.",
        "incorrectExplanations": {
            "A": "These reflect coercive asylum-era practices contrary to the human rights foundation of the MCA.",
            "C": "Presuming incapacity and 'doctor knows best' directly violate the MCA's statutory principles.",
            "D": "These are criminal justice penal concepts irrelevant to mental capacity law."
        },
        "learningObjective": "Apply the five statutory core principles of the Mental Capacity Act 2005 in adult safeguarding.",
        "reference": "Ministry of Justice. (2007). Mental Capacity Act 2005: Code of Practice. TSO.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q802",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Advanced",
        "questionText": "A psychiatric liaison nurse visiting a commercial residential care home observes that residents are locked in their bedrooms from 18:00 to 08:00 to accommodate reduced night staffing, call bells are placed out of reach, and incontinent residents are left in soiled garments for hours. What category of abuse does this represent?",
        "options": [
            {"id": "A", "text": "Organisational (institutional) abuse"},
            {"id": "B", "text": "Normative geriatric care routines"},
            {"id": "C", "text": "Acceptable cost-effective administrative streamlining"},
            {"id": "D", "text": "Individual financial exploitation"}
        ],
        "correctAnswer": "A",
        "explanation": "Organisational (or institutional) abuse occurs when routines, systems, and practices within a care facility prioritize institutional or staff convenience over the human dignity, safety, and rights of residents. Indicators include rigid locked schedules, call bells withheld, deprivation of basic hygiene, and systemic neglect due to intentional under-staffing.",
        "incorrectExplanations": {
            "B": "Neglect, confinement, and deprivation of call bells are abusive, never acceptable nursing care.",
            "C": "Cost-cutting that inflicts dehumanizing neglect is illegal under healthcare regulatory standards.",
            "D": "This scenario involves systemic operational abuse, not individual financial theft."
        },
        "learningObjective": "Identify institutional and organizational abuse indicators in residential and nursing care facilities.",
        "reference": "Care Quality Commission (CQC). (2018). Safeguarding people: Guidance for providers of health and social care services.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q803",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Advanced",
        "questionText": "During a memory clinic appointment, an 80-year-old woman discloses in tears that her adult son regularly slaps her across the face and threatens to shoot her pet dog whenever she refuses to give him money. When the nurse attempts to initiate a local authority adult safeguarding referral, the clinic manager tells the nurse: 'Don't get involved; it will damage our clinic's reputation.' What is the nurse's professional and legal duty?",
        "options": [
            {"id": "A", "text": "Obey the manager and shred the clinical notes to protect the clinic's reputation"},
            {"id": "B", "text": "Tell the patient to buy a gun to defend herself"},
            {"id": "C", "text": "Wait for 12 months to see if the son's behavior improves spontaneously"},
            {"id": "D", "text": "Uphold the mandatory professional duty of care: override the manager's improper directive, document the disclosure factually, submit an urgent adult safeguarding alert to the statutory local authority adult social care safeguarding team, and utilize institutional whistleblowing policies if obstruction persists"}
        ],
        "correctAnswer": "D",
        "explanation": "Professional regulatory codes (NMC The Code / ANA Code of Ethics) mandate that nurses act without delay if they believe someone is at risk of harm or abuse. Prioritizing institutional reputation over patient safety is gross misconduct. The nurse must raise an adult safeguarding alert and utilize whistleblowing channels if leadership obstructs safeguarding duties.",
        "incorrectExplanations": {
            "A": "Shredding records and colluding with an abusive cover-up violates law and professional registration.",
            "B": "Recommending weapons escalates lethal domestic homicide risks.",
            "C": "Delaying safeguarding intervention leaves a vulnerable elder in imminent danger of severe violence."
        },
        "learningObjective": "Demonstrate professional accountability, mandatory reporting duties, and whistleblowing in elder safeguarding.",
        "reference": "Nursing and Midwifery Council (NMC). (2018). The Code: Professional standards of practice and behaviour for nurses, midwives and nursing associates.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q804",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Elder abuse and safeguarding",
        "difficulty": "Expert",
        "questionText": "A 76-year-old woman with intact mental capacity is living with her daughter, who verbally abuses her and controls her movements. During a private assessment, the woman admits the abuse but firmly refuses any safeguarding intervention or police involvement, explaining: 'She is my only child; if you take her away or arrest her, I will be completely alone and die of heartbreak.' How must the advanced practice nurse navigate the ethical and legal dilemma between adult autonomy and protection?",
        "options": [
            {"id": "A", "text": "Immediately obtain a court order to commit the mother to a locked psychiatric asylum against her will"},
            {"id": "B", "text": "Discharge the patient from the service and refuse ever to see her again"},
            {"id": "C", "text": "Respect her autonomous decision as a mentally competent adult while evaluating for undue influence and coercive control; maintain an open, non-abandoning therapeutic alliance, provide discrete emergency safety numbers, explore low-barrier community supports, and establish a scheduled safeguarding review plan"},
            {"id": "D", "text": "Arrest the daughter immediately without evidence or complainant testimony"}
        ],
        "correctAnswer": "C",
        "explanation": "Under the Mental Capacity Act and adult safeguarding law, a competent adult has the legal right to make unwise decisions, including remaining in an abusive relationship. The nurse must assess whether 'undue influence' or coercive control impairs decision-making, respect her autonomy while maintaining an active safety net, avoid abandonment, offer confidential resources, and monitor ongoing risk collaboratively.",
        "incorrectExplanations": {
            "A": "Involuntary asylum commitment of a competent victim breaches human rights and the Mental Health Act.",
            "B": "Abandoning the patient isolates her further and increases danger.",
            "D": "Nurses lack legal powers of arrest; action must follow statutory adult protection frameworks."
        },
        "learningObjective": "Resolve complex ethical and legal tensions between respecting competent adult autonomy and mitigating coercive control in elder abuse.",
        "reference": "Social Care Institute for Excellence (SCIE). (2020). Adult safeguarding: Sharing information and managing risk.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 10: Geriatric psychopharmacology (MHN-Q805 - MHN-Q814)
    # Target Answers: B, D, A, C, B, D, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q805",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Foundation",
        "questionText": "Age-related physiological changes significantly alter psychotropic drug pharmacokinetics. Which of the following changes represents a characteristic pharmacokinetic alteration in older adults?",
        "options": [
            {"id": "A", "text": "Massive increase in total body water and decrease in body fat percentage"},
            {"id": "B", "text": "Decreased glomerular filtration rate (GFR), reduced hepatic Phase I cytochrome P450 enzyme metabolism, increased relative body fat percentage (prolonging the half-life of lipophilic drugs like diazepam), and decreased serum albumin"},
            {"id": "C", "text": "Permanent elimination of all blood-brain barrier permeability"},
            {"id": "D", "text": "A ten-fold increase in renal clearance of psychotropic compounds"}
        ],
        "correctAnswer": "B",
        "explanation": "Ageing is associated with reduced renal drug clearance (GFR declines ~1% per year after age 40), reduced Phase I hepatic oxidation, increased proportional body fat (which dramatically expands the volume of distribution and prolongs elimination half-lives of lipophilic drugs such as long-acting benzodiazepines), and reduced serum albumin (increasing free active drug fractions).",
        "incorrectExplanations": {
            "A": "Total body water decreases and body fat percentage increases in ageing.",
            "C": "The blood-brain barrier becomes more permeable, not completely impermeable.",
            "D": "Renal clearance decreases with age, never increases ten-fold."
        },
        "learningObjective": "Recall pharmacokinetic alterations (absorption, distribution, metabolism, excretion) in geriatric psychopharmacology.",
        "reference": "Hilmer, S. N. (2008). Practical guide to prescribing in the elderly. Australian Prescriber, 31(1), 20-23.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q806",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Foundation",
        "questionText": "The Beers Criteria (American Geriatrics Society) is a globally recognized evidence-based guideline in geriatric medicine. What is the primary purpose of the Beers Criteria?",
        "options": [
            {"id": "A", "text": "To calculate the retail commercial price of generic psychotropic tablets"},
            {"id": "B", "text": "To rank psychiatric nurses on clinical charting speed"},
            {"id": "C", "text": "To prescribe mandatory alcohol intake for hospitalized geriatric patients"},
            {"id": "D", "text": "To identify Potentially Inappropriate Medications (PIMs) whose risks of adverse events generally outweigh their clinical benefits in older adults (e.g. tertiary TCAs, long-acting benzodiazepines, first-generation antihistamines)"}
        ],
        "correctAnswer": "D",
        "explanation": "The AGS Beers Criteria identifies Potentially Inappropriate Medications (PIMs) that should generally be avoided in older adults due to high risks of adverse drug events (falls, delirium, fractures, gastrointestinal bleeds) compared to limited benefits. Notable psychiatric PIMs include tertiary tricyclics (amitriptyline), long-acting benzodiazepines, and first-generation antihistamines.",
        "incorrectExplanations": {
            "A": "The Beers criteria evaluates clinical safety, not commercial retail drug pricing.",
            "B": "It is an evidence-based pharmacological safety guide, not a nurse speed ranking.",
            "C": "It is named after Dr. Mark Beers; it has nothing to do with alcoholic beverages."
        },
        "learningObjective": "Define the purpose, structure, and clinical application of the AGS Beers Criteria for Potentially Inappropriate Medications.",
        "reference": "American Geriatrics Society. (2019). Updated AGS Beers Criteria for potentially inappropriate medication use in older adults. Journal of the American Geriatrics Society, 67(4), 674-694.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q807",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Intermediate",
        "questionText": "In geriatric clinical pharmacology, how do the STOPP (Screening Tool of Older Persons' Prescriptions) and START (Screening Tool to Alert to Right Treatment) criteria differ from each other?",
        "options": [
            {"id": "A", "text": "STOPP identifies potentially inappropriate medications that should be discontinued to prevent adverse drug events; START identifies evidence-based, clinically indicated medications that have been erroneously omitted"},
            {"id": "B", "text": "STOPP is used exclusively for pediatric patients; START is used exclusively for deceased patients"},
            {"id": "C", "text": "STOPP requires hospital admission; START requires outpatient discharge"},
            {"id": "D", "text": "There are no differences; both terms are interchangeable legal trademarks"}
        ],
        "correctAnswer": "A",
        "explanation": "STOPP/START criteria are physiological system-based medication review tools. STOPP identifies potentially inappropriate prescribing (drugs to deprescribe or discontinue), while START identifies potential prescribing omissions (evidence-based therapies that are clinically indicated for chronic conditions but have been inadvertently omitted).",
        "incorrectExplanations": {
            "B": "Both tools are specifically designed for older adult geriatric pharmacotherapy.",
            "C": "STOPP and START are applied across both inpatient and community ambulatory settings.",
            "D": "STOPP and START address opposing prescribing errors (inappropriate commission vs omitted indication)."
        },
        "learningObjective": "Differentiate between the STOPP and START criteria in geriatric medication optimization and deprescribing.",
        "reference": "O'Mahony, D., et al. (2015). STOPP/START criteria for potentially inappropriate prescribing in older people: version 2. Age and Ageing, 44(2), 213-218.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q808",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Intermediate",
        "questionText": "An 80-year-old patient with mild cognitive impairment is concurrently prescribed Amitriptyline 50 mg (for neuropathy), Oxybutynin 10 mg (for overactive bladder), Chlorpheniramine (for allergies), and Haloperidol 1 mg (for agitation). When calculating the Anticholinergic Cognitive Burden (ACB score), what severe clinical risks must the nurse highlight?",
        "options": [
            {"id": "A", "text": "Excessive salivation and uncontrolled diarrhea"},
            {"id": "B", "text": "Immediate permanent blindness from retinal detachment"},
            {"id": "C", "text": "Cumulative high anticholinergic burden producing acute delirium, accelerated cognitive decline, dry mouth, severe constipation/bowel impaction, urinary retention, blurred vision, and heightened fall risk"},
            {"id": "D", "text": "Profound hypothermia and skeletal muscle hypertrophy"}
        ],
        "correctAnswer": "C",
        "explanation": "The Anticholinergic Cognitive Burden (ACB) scale quantifies cumulative central and peripheral anticholinergic exposure. A high cumulative score (>=3) significantly increases the risk of acute delirium, cognitive decline, falls, dry mouth, visual blurring, paralytic ileus/severe constipation, and acute urinary retention in older adults.",
        "incorrectExplanations": {
            "A": "Anticholinergics cause severe dry mouth and constipation, the exact opposite of salivation and diarrhea.",
            "B": "Retinal detachment is not caused by anticholinergic medications.",
            "D": "Anticholinergics impair sweating, leading to hyperthermia rather than hypothermia."
        },
        "learningObjective": "Calculate Anticholinergic Cognitive Burden (ACB) scores and evaluate clinical complications of cumulative anticholinergic toxicity.",
        "reference": "Boustani, M., et al. (2008). Impact of anticholinergics on cognition. Aging Health, 4(3), 311-320.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q809",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Intermediate",
        "questionText": "An older adult admitted to an acute psychogeriatric ward falls on night three, sustaining a fractured neck of femur. The medication chart reveals the patient takes Trazodone 100 mg, Quetiapine 50 mg, and Lorazepam 1 mg at bedtime. What primary pharmacological mechanisms contributed to this patient's fall risk?",
        "options": [
            {"id": "A", "text": "Excessive dopamine stimulation causing involuntary choreiform running"},
            {"id": "B", "text": "Alpha-1 adrenergic receptor antagonism causing severe orthostatic (postural) hypotension, combined with sedation and motor ataxia from benzodiazepine GABA-A receptor modulation"},
            {"id": "C", "text": "Selective serotonin reuptake inhibition causing brittle bone disease"},
            {"id": "D", "text": "Severe hypokalemia from excessive intravenous fluid administration"}
        ],
        "correctAnswer": "B",
        "explanation": "Psychotropic-induced fall risk is driven by potent pharmacodynamic mechanisms: 1) Alpha-1 adrenergic blockade (prominent in trazodone, quetiapine, low-potency antipsychotics) causes acute postural/orthostatic hypotension, producing syncope or lightheadedness upon standing; 2) Benzodiazepines (lorazepam) impair vestibular balance, cause motor ataxia, and induce sedation.",
        "incorrectExplanations": {
            "A": "These medications block dopamine and alpha receptors; they do not stimulate dopamine.",
            "C": "While SSRIs affect bone density chronically, acute bedtime falls are hemodynamic and sedative.",
            "D": "The scenario describes sedating oral psychotropics, not IV fluid-induced hypokalemia."
        },
        "learningObjective": "Identify pharmacological mechanisms driving falls in geriatric psychopharmacology, particularly alpha-1 adrenergic blockade and sedation.",
        "reference": "Seppala, L. J., et al. (2018). STOPPFall (Screening Tool of Older Persons Prescriptions in older adults with high fall risk): Delphi study by the EuGMS Task and Finish Group on Fall-Risk-Increasing Drugs. Age and Ageing, 50(4), 1189-1199.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q810",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Intermediate",
        "questionText": "When adjusting the dosages of renally eliminated psychotropic medications (such as Lithium, Gabapentin, Pregabalin, or Paliperidone) in frail older adults with sarcopenia (reduced muscle mass), why must the nurse verify the Cockcroft-Gault estimated Creatinine Clearance (CrCl) rather than relying solely on automated laboratory eGFR (CKD-EPI)?",
        "options": [
            {"id": "A", "text": "Cockcroft-Gault is legally required for financial insurance reimbursement"},
            {"id": "B", "text": "Automated eGFR is 100% accurate in all body types regardless of muscle mass"},
            {"id": "C", "text": "Cockcroft-Gault measures hepatic Phase II glucuronidation exclusively"},
            {"id": "D", "text": "In frail older adults with diminished muscle mass, baseline serum creatinine is deceptively low, causing automated eGFR to substantially overestimate renal function; Cockcroft-Gault incorporates actual body weight and age, preventing dangerous drug overdoses"}
        ],
        "correctAnswer": "D",
        "explanation": "Serum creatinine is a byproduct of skeletal muscle breakdown. In sarcopenic, frail elderly patients, low muscle mass produces deceptively low serum creatinine levels. Automated eGFR equations (CKD-EPI/MDRD) often falsely overestimate true kidney function, leading to toxic overdoses. Drug licensing and dosing guidelines mandate using Cockcroft-Gault CrCl.",
        "incorrectExplanations": {
            "A": "The reason is patient safety and toxicity prevention, not billing.",
            "B": "Automated eGFR is notoriously inaccurate in frail older adults with extreme body composition.",
            "C": "Cockcroft-Gault calculates renal creatinine clearance, not liver metabolism."
        },
        "learningObjective": "Evaluate renal function assessment methods (Cockcroft-Gault CrCl vs automated eGFR) for safe geriatric psychotropic dosing.",
        "reference": "Nyman, H. A., et al. (2011). Comparative evaluation of the Cockcroft-Gault equation and the Modification of Diet in Renal Disease (MDRD) study equation for drug dosing: An opinion of the Nephrology Practice and Research Network of the American College of Clinical Pharmacy. Pharmacotherapy, 31(11), 1130-1144.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q811",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Advanced",
        "questionText": "An advanced practice psychiatric nurse is leading a 'Deprescribing' initiative in an older adult psychiatric day unit. What core clinical principles should guide the systematic deprescribing of unnecessary psychotropic medications in older adults with polypharmacy?",
        "options": [
            {"id": "A", "text": "Abruptly stop all ten medications simultaneously on day one without informing the patient"},
            {"id": "B", "text": "Conduct a comprehensive review of all medications and indications, prioritize medications with high risk/benefit ratios (or lacking current indication), taper one drug slowly at a time with close monitoring for withdrawal or symptom recurrence, and engage the patient/family in shared decision-making"},
            {"id": "C", "text": "Replace all prescription drugs with unverified herbal teas"},
            {"id": "D", "text": "Deprescribing is unethical; once a psychotropic is started, it must be continued until death"}
        ],
        "correctAnswer": "B",
        "explanation": "Deprescribing is the planned, supervised process of dose reduction or discontinuation of medications that may be causing harm or no longer provide benefit. Best practice requires systematic review, identifying high-risk agents (Beers/STOPP), tapering one drug at a time slowly, monitoring for discontinuation emergent symptoms or illness recurrence, and shared decision-making.",
        "incorrectExplanations": {
            "A": "Abruptly stopping multiple medications triggers catastrophic withdrawal syndromes (rebound psychosis, cholinergic rebound, seizures).",
            "C": "Replacing evidence-based medicine with unverified herbal products exposes patients to uncontrolled toxicities.",
            "D": "Deprescribing is an essential clinical competency; continuing futile medications violates the principle of non-maleficence."
        },
        "learningObjective": "Formulate evidence-based clinical protocols for systematic psychotropic deprescribing in older adults.",
        "reference": "Reeve, E., et al. (2014). Review of approaches to deprescribing for people with dementia and cognitive impairment. International Journal of Clinical Pharmacy, 36(6), 1146-1153.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q812",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Advanced",
        "questionText": "An 84-year-old hospitalized patient with mild dementia is given Diazepam 5 mg at 22:00 for acute insomnia. By midnight, instead of sleeping, the patient becomes extremely disinhibited, shouting, highly agitated, attempting to climb over the bed rails, and experiencing visual illusions. What clinical phenomenon has occurred?",
        "options": [
            {"id": "A", "text": "Malingering designed to obtain hot chocolate from the night nurse"},
            {"id": "B", "text": "Immediate therapeutic cure of the dementia"},
            {"id": "C", "text": "Acute bacterial septic shock"},
            {"id": "D", "text": "Paradoxical excitation (disinhibition) from benzodiazepines, a well-documented adverse reaction in older adults and individuals with pre-existing cognitive impairment"}
        ],
        "correctAnswer": "D",
        "explanation": "Paradoxical excitation / disinhibition is a recognized adverse reaction to benzodiazepines, especially in older adults and individuals with neurocognitive impairment. Instead of sedation, the drug produces severe worsening of agitation, motor restlessness, disinhibition, confusion, and delirium. Benzodiazepines should be avoided for BPSD and insomnia in older adults.",
        "incorrectExplanations": {
            "A": "Paradoxical disinhibition is an involuntary neurochemical reaction, not willful malingering.",
            "B": "Benzodiazepines exacerbate cognitive deficits; they never cure dementia.",
            "C": "Acute onset within two hours of benzodiazepine ingestion indicates drug toxicity, not septic shock."
        },
        "learningObjective": "Recognize and manage paradoxical excitation and disinhibition reactions from benzodiazepines in older adults.",
        "reference": "Mancuso, C. E., et al. (2004). Paradoxical reactions to benzodiazepines: literature review and mechanisms. Pharmacotherapy, 24(9), 1177-1185.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q813",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Advanced",
        "questionText": "An 76-year-old patient taking high-dose Naproxen for severe knee osteoarthritis is prescribed Sertraline 100 mg/day for major depression. What serious pharmacodynamic drug-drug interaction must the psychiatric nurse recognize, and what gastroprotective intervention is recommended?",
        "options": [
            {"id": "A", "text": "A substantially increased risk of upper gastrointestinal bleeding (due to combined platelet serotonin depletion from the SSRI and gastric mucosal injury from the NSAID); co-prescribing a Proton Pump Inhibitor (PPI) or switching to an alternative antidepressant/analgesic is strongly recommended"},
            {"id": "B", "text": "Immediate permanent deafness; requiring hearing aids"},
            {"id": "C", "text": "Severe hypertension requiring intravenous nitroprusside"},
            {"id": "D", "text": "Instantaneous dissolution of all dental fillings"}
        ],
        "correctAnswer": "A",
        "explanation": "SSRIs deplete serotonin within blood platelets, impairing platelet aggregation and hemostasis. When combined with NSAIDs (which cause gastric mucosal erosion and inhibit cyclooxygenase), the risk of severe upper gastrointestinal bleeding increases synergistically (up to a 6- to 12-fold increase in older adults). Co-prescription of a gastroprotective PPI (e.g. omeprazole) is standard practice.",
        "incorrectExplanations": {
            "B": "SSRI-NSAID interactions cause gastrointestinal hemorrhage, not ototoxicity.",
            "C": "NSAIDs can elevate blood pressure slightly, but the acute synergistic danger is catastrophic GI bleeding.",
            "D": "Dental fillings are completely unaffected by this drug interaction."
        },
        "learningObjective": "Analyze pharmacodynamic drug-drug interactions between SSRIs and NSAIDs regarding gastrointestinal hemorrhage.",
        "reference": "de Abajo, F. J., et al. (2008). Risk of upper gastrointestinal tract bleeding associated with selective serotonin reuptake inhibitors and venlafaxine therapy: Interaction with nonsteroidal anti-inflammatory drugs. Archives of General Psychiatry, 65(7), 795-803.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q814",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Geriatric psychopharmacology",
        "difficulty": "Expert",
        "questionText": "A 79-year-old woman with chronic insomnia requests a prescription for Zolpidem or Zopiclone ('Z-drugs'), stating her friend takes them every night. What evidence-based guidance must the advanced practice psychiatric nurse provide regarding first-line therapy and the risks of non-benzodiazepine hypnotics in older adults?",
        "options": [
            {"id": "A", "text": "Prescribe double-strength zolpidem because Z-drugs have zero side effects in older adults"},
            {"id": "B", "text": "Instruct the patient that insomnia in late life is incurable and should be ignored"},
            {"id": "C", "text": "Recommend Cognitive Behavioural Therapy for Insomnia (CBT-I) as the evidence-based first-line treatment; explain that Z-drugs act on the same GABA-A benzodiazepine receptor complex, carrying risks of nocturnal falls, hip fractures, motor vehicle accidents, and next-day cognitive impairment comparable to traditional benzodiazepines"},
            {"id": "D", "text": "Advise consuming two glasses of brandy at bedtime instead of medication"}
        ],
        "correctAnswer": "C",
        "explanation": "Cognitive Behavioural Therapy for Insomnia (CBT-I) is the recommended first-line treatment for chronic insomnia across all age groups, producing sustained improvements without pharmacological risk. While marketed as safer, 'Z-drugs' (zolpidem, zopiclone, zaleplon) act on the GABA-A receptor and carry risk profiles nearly identical to benzodiazepines in older adults: doubled risk of nocturnal falls, hip fractures, daytime somnolence, and memory impairment.",
        "incorrectExplanations": {
            "A": "Z-drugs carry severe fall, fracture, and confusion risks in older adults; the AGS Beers criteria recommends avoiding them.",
            "B": "Late-life insomnia is highly treatable with CBT-I.",
            "D": "Alcohol disrupts sleep architecture, causes nocturnal awakenings, and increases fall risks."
        },
        "learningObjective": "Appraise the comparative efficacy and adverse event profiles of Cognitive Behavioural Therapy for Insomnia (CBT-I) versus Z-drug hypnotics in geriatric populations.",
        "reference": "Glass, J., et al. (2005). Sedative hypnotics in older people with insomnia: meta-analysis of risks and benefits. BMJ, 331(7526), 1169.",
        "contentReviewStatus": "Peer Reviewed"
    }
]
