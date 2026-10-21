# -*- coding: utf-8 -*-
"""
Module 13: Substance Use Disorders and Dual Diagnosis
Questions MHN-Q1265 to MHN-Q1314 (Topics 6 to 10, 50 questions)
"""

QUESTIONS_T6_T10 = [
    # ---------------------------------------------------------
    # Topic 6: Benzodiazepine Dependence (MHN-Q1265 to MHN-Q1274)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1265",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Foundation",
        "questionText": "What is the primary neurobiological mechanism responsible for the development of tolerance and physical dependence during prolonged, continuous benzodiazepine administration?",
        "options": [
            {"id": "A", "text": "Continuous upregulation and hypersensitization of dopamine D2 receptors in the prefrontal cortex."},
            {"id": "B", "text": "Conformational uncoupling and downregulation of GABA-A receptor subunits, coupled with compensatory upregulation of excitatory glutamatergic NMDA neurotransmission."},
            {"id": "C", "text": "Irreversible depletion of central acetylcholine stores in the hippocampus."},
            {"id": "D", "text": "Direct destruction of postsynaptic serotonin 5-HT1A receptors in the raphe nuclei."}
        ],
        "correctAnswer": "B",
        "explanation": "Benzodiazepines act as positive allosteric modulators at GABA-A receptors, enhancing chloride conductance. Prolonged exposure causes neuroadaptation: GABA-A receptors undergo conformational uncoupling (reduced sensitivity between benzodiazepine and GABA binding sites) and internalization/downregulation. Simultaneously, the brain mounts a compensatory upregulation of excitatory glutamatergic pathways (NMDA receptors). Abrupt withdrawal leaves unopposed glutamatergic excitotoxicity.",
        "incorrectExplanations": {
            "A": "Dopamine D2 upregulation is not the primary mechanism of benzodiazepine physical dependence.",
            "C": "Benzodiazepines do not deplete acetylcholine stores.",
            "D": "Serotonin 5-HT1A destruction does not drive benzodiazepine tolerance and physical dependence."
        },
        "learningObjective": "Explain the neurobiological alterations in GABA-A and NMDA receptors underlying benzodiazepine tolerance and dependence.",
        "reference": "Ashton, H. (2005). The diagnosis and management of benzodiazepine dependence. Current Opinion in Psychiatry, 18(3), 249-255.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1266",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Foundation",
        "questionText": "How does the elimination half-life of different benzodiazepines dictate the onset and timeline of the acute withdrawal syndrome following abrupt discontinuation?",
        "options": [
            {"id": "A", "text": "All benzodiazepines produce acute withdrawal symptoms exactly 14 days after cessation regardless of half-life."},
            {"id": "B", "text": "Long-acting benzodiazepines produce withdrawal within 2 hours, whereas short-acting agents take 3 weeks."},
            {"id": "C", "text": "Short-acting benzodiazepines never produce physical withdrawal symptoms."},
            {"id": "D", "text": "Short-acting benzodiazepines (e.g., alprazolam, lorazepam) produce acute withdrawal within 24 to 48 hours of cessation, whereas long-acting benzodiazepines (e.g., diazepam, clonazepam) produce an onset delayed for 5 to 10 days due to lingering active metabolites."}
        ],
        "correctAnswer": "D",
        "explanation": "The onset of benzodiazepine withdrawal is directly governed by pharmacokinetics. Short-acting agents with short elimination half-lives and no active metabolites (e.g., alprazolam, lorazepam, oxazepam) produce rapid, intense withdrawal symptoms within 24 to 48 hours of cessation. Conversely, long-acting agents (e.g., diazepam, chlordiazepoxide) have prolonged half-lives and active metabolites, delaying the onset of withdrawal symptoms until 5 to 10 days post-cessation.",
        "incorrectExplanations": {
            "A": "Withdrawal onset varies significantly depending on whether the agent is short-, intermediate-, or long-acting.",
            "B": "This reverses the pharmacological reality; short-acting agents trigger rapid withdrawal, not long-acting ones.",
            "C": "Short-acting benzodiazepines carry a severe, rapid-onset physical withdrawal risk."
        },
        "learningObjective": "Correlate benzodiazepine pharmacokinetic half-lives with the expected clinical timeline of withdrawal emergence.",
        "reference": "Lader, M. (2011). Benzodiazepine harm: how can it be reduced? British Journal of Clinical Pharmacology, 77(2), 295-301.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1267",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Intermediate",
        "questionText": "What are the most severe, life-threatening clinical complications that can occur following abrupt, unmonitored cessation of long-term high-dose benzodiazepines?",
        "options": [
            {"id": "A", "text": "Generalized tonic-clonic status epilepticus, hyperthermic delirium, and severe autonomic instability resembling delirium tremens."},
            {"id": "B", "text": "Fatal respiratory depression and sudden bilateral pinpoint miosis."},
            {"id": "C", "text": "Acute thyroid storm and widespread urticaria."},
            {"id": "D", "text": "Aplastic anemia and sudden massive gastrointestinal hemorrhage."}
        ],
        "correctAnswer": "A",
        "explanation": "Abrupt cessation of chronic benzodiazepines causes loss of GABAergic inhibition and severe glutamatergic excess, which can precipitate generalized tonic-clonic seizures, status epilepticus, and severe delirium accompanied by visual/auditory hallucinations, marked autonomic instability (hypertension, tachycardia, hyperthermia), and potential cardiovascular collapse.",
        "incorrectExplanations": {
            "B": "Respiratory depression and pinpoint miosis characterize opioid intoxication, not benzodiazepine withdrawal.",
            "C": "Benzodiazepine withdrawal does not cause primary thyroid storm or urticaria.",
            "D": "Aplastic anemia is a bone marrow failure syndrome unrelated to acute benzodiazepine cessation."
        },
        "learningObjective": "Recognize status epilepticus and hyperthermic delirium as life-threatening complications of abrupt benzodiazepine cessation.",
        "reference": "Pétursson, H. (1994). The benzodiazepine withdrawal syndrome. Addiction, 89(11), 1455-1459.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1268",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Intermediate",
        "questionText": "A 38-year-old client undergoing outpatient benzodiazepine reduction complains of distressing sensations: room lights seem blindingly bright, everyday sounds like dishes clattering cause excruciating ear pain, she notices a persistent metallic taste in her mouth, and feels her skin is crawling. Which symptom cluster does this describe?",
        "options": [
            {"id": "A", "text": "Primary somatic symptom disorder without physiological basis"},
            {"id": "B", "text": "Sensory perceptual distortions and hyperacusis characteristic of benzodiazepine withdrawal syndrome"},
            {"id": "C", "text": "Ménière's disease and vestibular neuritis"},
            {"id": "D", "text": "Trigeminal neuralgia and Bell's palsy"}
        ],
        "correctAnswer": "B",
        "explanation": "Sensory hypersensitivity (hyperacusis, photophobia, hyperosmia), metallic taste in the mouth, muscle fasciculations, paresthesias, and depersonalization/derealization are characteristic perceptual distortions of the benzodiazepine withdrawal syndrome. They result from the sudden unmasking and hyperexcitability of central sensory processing circuits following withdrawal of GABAergic inhibition.",
        "incorrectExplanations": {
            "A": "These are classic neurochemical sensory rebound symptoms, not somatization.",
            "C": "Ménière's disease presents with episodic vertigo, low-frequency sensorineural hearing loss, and aural fullness.",
            "D": "Trigeminal neuralgia causes unilateral, stabbing electric facial pain along trigeminal branches."
        },
        "learningObjective": "Identify sensory perceptual disturbances, hyperacusis, and dysgeusia as specific indicators of benzodiazepine withdrawal.",
        "reference": "Ashton, H. (1984). Benzodiazepine withdrawal: an unfinished story. British Medical Journal, 288(6424), 1135-1140.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1269",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Intermediate",
        "questionText": "According to the internationally recognized Ashton Manual protocol for discontinuing high-potency, short-acting benzodiazepines (such as alprazolam or lorazepam), what is the essential initial pharmacological step before commencing dose tapering?",
        "options": [
            {"id": "A", "text": "Abruptly stop all benzodiazepines and substitute with high-dose intravenous propofol."},
            {"id": "B", "text": "Switch the client to an equivalent dose of a short-acting barbiturate."},
            {"id": "C", "text": "Gradually convert the short-acting benzodiazepine to an approximate equivalent daily dose of a long-acting benzodiazepine (diazepam) in divided doses to achieve stable plasma concentrations."},
            {"id": "D", "text": "Double the dose of alprazolam and maintain it indefinitely."}
        ],
        "correctAnswer": "C",
        "explanation": "The Ashton protocol recommends substituting high-potency, short-acting benzodiazepines (e.g., alprazolam, lorazepam) with equivalent doses of diazepam, a long-acting agent with a smooth plasma elimination profile (half-life up to 100–200 hours including active metabolites). This eliminates inter-dose withdrawal peaks and troughs and allows subsequent fine, gradual dose reductions.",
        "incorrectExplanations": {
            "A": "Abrupt cessation exposes the patient to life-threatening seizures and status epilepticus.",
            "B": "Barbiturates have a much narrower therapeutic index and carry high toxicity.",
            "D": "Doubling the alprazolam dose escalates physical dependence and compounds withdrawal severity."
        },
        "learningObjective": "Apply the principles of the Ashton Manual for converting short-acting benzodiazepines to long-acting diazepam equivalents.",
        "reference": "Ashton, C. H. (2002). Benzodiazepines: How They Work and How to Withdraw (The Ashton Manual). Newcastle University.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1270",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Advanced",
        "questionText": "A client has been successfully converted to diazepam 30 mg daily following the Ashton protocol. What is the evidence-based recommendation regarding the rate of subsequent dose reduction to minimize withdrawal distress and avoid rebound seizures?",
        "options": [
            {"id": "A", "text": "Reduce by 10 mg every 2 days to complete withdrawal in under 1 week."},
            {"id": "B", "text": "Stop the entire 30 mg dose on the second week and provide relaxation recordings."},
            {"id": "C", "text": "Reduce the dose by 50% every 24 hours while checking blood pressure."},
            {"id": "D", "text": "Taper gradually by approximately 5% to 10% of the current dose (or 1 to 2 mg diazepam) every 1 to 2 weeks, with flexibility based on patient tolerance, slowing down further during the final stages."}
        ],
        "correctAnswer": "D",
        "explanation": "Safe benzodiazepine discontinuation requires slow, flexible, patient-led tapering. The Ashton Manual and clinical guidelines advise reducing by roughly 1 to 2 mg diazepam (or 5–10% of the current dose) every 1 to 2 weeks. As the total dose diminishes (especially below 10 mg diazepam), the rate of reduction should often be slowed to 0.5–1 mg decrements every 2 to 4 weeks to manage persistent receptor recalibration.",
        "incorrectExplanations": {
            "A": "A reduction of 10 mg every 2 days is dangerously rapid and will trigger severe rebound anxiety and seizures.",
            "B": "Abrupt cessation of 30 mg diazepam will cause acute severe withdrawal and seizure risk.",
            "C": "Halving the dose daily is an unsafe rapid detox that invariably leads to clinical failure and emergency readmission."
        },
        "learningObjective": "Calculate and evaluate safe gradual dose reduction schedules for benzodiazepine discontinuation.",
        "reference": "British National Formulary (BNF). (2023). Benzodiazepine dependence and withdrawal guidelines. BMJ Group and Pharmaceutical Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1271",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Foundation",
        "questionText": "A client undertaking a diazepam taper struggles with severe rebound insomnia. The junior doctor suggests prescribing zopiclone 7.5 mg nightly as a 'non-benzodiazepine' sleep aid. Why should the psychiatric nurse question and advise against this prescription?",
        "options": [
            {"id": "A", "text": "Z-drugs (such as zopiclone and zolpidem) act as agonists at the benzodiazepine site of the GABA-A receptor (specifically alpha-1 subunits), exhibiting cross-tolerance and cross-dependence, thereby perpetuating the dependence cycle."},
            {"id": "B", "text": "Zopiclone is a pure opioid that causes fatal respiratory depression when combined with diazepam."},
            {"id": "C", "text": "Zopiclone permanently destroys renal nephrons within 48 hours."},
            {"id": "D", "text": "Zopiclone is an MAOI that causes fatal serotonin toxicity with benzodiazepines."}
        ],
        "correctAnswer": "A",
        "explanation": "Although chemically distinct from benzodiazepines (cyclopyrrolones and imidazopyridines), 'Z-drugs' (zopiclone, zolpidem, zaleplon) bind directly to the same GABA-A receptor complex at the alpha-1 subunit benzodiazepine binding site. Consequently, they share complete cross-tolerance and cross-dependence with benzodiazepines. Prescribing a Z-drug during a benzodiazepine taper maintains neurochemical dependence and sabotages the discontinuation process.",
        "incorrectExplanations": {
            "B": "Z-drugs are positive allosteric GABA-A modulators, not opioids.",
            "C": "Zopiclone does not cause acute renal nephron destruction.",
            "D": "Zopiclone is not a monoamine oxidase inhibitor (MAOI)."
        },
        "learningObjective": "Explain why non-benzodiazepine hypnotics (Z-drugs) are contraindicated as substitute agents during benzodiazepine withdrawal.",
        "reference": "National Institute for Health and Care Excellence (NICE). (2004). Guidance on the use of zaleplon, zolpidem and zopiclone for the short-term management of insomnia (TA77).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1272",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Advanced",
        "questionText": "In clients with a history of benzodiazepine withdrawal seizures or those who experience severe withdrawal symptoms despite gradual tapering, which adjunctive non-benzodiazepine anticonvulsant medication has evidence supporting its off-label use to raise seizure threshold and ease withdrawal discomfort?",
        "options": [
            {"id": "A", "text": "Intravenous phenytoin bolus"},
            {"id": "B", "text": "Carbamazepine, gabapentin, or pregabalin, which can attenuate withdrawal symptoms and elevate seizure thresholds under careful clinical oversight."},
            {"id": "C", "text": "Oral haloperidol monotherapy"},
            {"id": "D", "text": "Lithium carbonate at supratherapeutic levels"}
        ],
        "correctAnswer": "B",
        "explanation": "Carbamazepine (by blocking voltage-gated sodium channels and dampening neuronal excitability) and gabapentinoids (gabapentin or pregabalin, by binding alpha-2-delta calcium channel subunits and decreasing excitatory glutamate release) have demonstrated efficacy in clinical trials for reducing withdrawal severity and preventing seizures during benzodiazepine tapers.",
        "incorrectExplanations": {
            "A": "Phenytoin is ineffective in preventing withdrawal-related seizures resulting from GABAergic deficiency.",
            "C": "Haloperidol lowers the seizure threshold and worsens withdrawal neurotoxicity.",
            "D": "Supratherapeutic lithium produces severe neurotoxicity and renal damage."
        },
        "learningObjective": "Evaluate the clinical evidence for adjunctive anticonvulsant pharmacotherapy during complex benzodiazepine withdrawal.",
        "reference": "Schweizer, E., et al. (1991). Carbamazepine treatment in patients with severe benzodiazepine withdrawal. American Journal of Psychiatry, 148(4), 515-517.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1273",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Advanced",
        "questionText": "A 45-year-old client who successfully completed a diazepam taper 4 months ago returns to the clinic reporting periodic 'waves' of anxiety, tinnitus, gastrointestinal upset, muscle twitches, and sleep disruption lasting several days, alternating with symptom-free 'windows.' What phenomenon is this client experiencing, and what is the nurse's therapeutic response?",
        "options": [
            {"id": "A", "text": "Schizophrenia prodrome; advise immediate long-term fluphenazine depot injections."},
            {"id": "B", "text": "Malingering to obtain a new benzodiazepine prescription; discharge the client immediately."},
            {"id": "C", "text": "Protracted benzodiazepine withdrawal syndrome (Post-Acute Withdrawal Syndrome - PAWS); provide psychoeducation reassuring the client that waxing-and-waning symptom waves are common, benign, and gradually subside over months as receptor homeostasis recalibrates."},
            {"id": "D", "text": "Acute bacterial meningitis; order immediate lumbar puncture and isolation."}
        ],
        "correctAnswer": "C",
        "explanation": "Protracted withdrawal syndrome (or Post-Acute Withdrawal Syndrome - PAWS) can persist for months or even 1 to 2 years following benzodiazepine discontinuation. It is characterized by fluctuating 'waves' of sensory hypersensitivity, tinnitus, gastrointestinal disturbances, insomnia, and autonomic anxiety alternating with symptom-free 'windows.' The nurse should provide validation and reassurance that this reflects slow, ongoing neuroplastic receptor recovery.",
        "incorrectExplanations": {
            "A": "PAWS symptoms are typical of benzodiazepine receptor recovery, not schizophrenia.",
            "B": "Dismissing PAWS as malingering damages the therapeutic alliance and increases relapse risk.",
            "D": "The absence of high fever, nuchal rigidity, and photophobia distinguishes chronic PAWS from acute meningitis."
        },
        "learningObjective": "Distinguish protracted benzodiazepine withdrawal syndrome from psychiatric relapse and provide supportive psychoeducation.",
        "reference": "Ashton, H. (1991). Protracted withdrawal syndromes from benzodiazepines. Journal of Substance Abuse Treatment, 8(1-2), 19-28.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1274",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Benzodiazepine Dependence",
        "difficulty": "Expert",
        "questionText": "An 82-year-old female living independently is prescribed temazepam 20 mg nightly for insomnia. Her daughter notes progressive memory problems, daytime confusion, and two recent falls resulting in hip bruising. Why are elderly patients uniquely vulnerable to severe adverse drug events from benzodiazepines, according to the Beers Criteria?",
        "options": [
            {"id": "A", "text": "Elderly patients absorb benzodiazepines through the skin rather than the gut, bypassing all biological controls."},
            {"id": "B", "text": "Elderly patients have 10-fold higher renal filtration rates that convert benzodiazepines into neurotoxic metabolites."},
            {"id": "C", "text": "Elderly individuals develop immediate permanent blindness after 3 doses of any hypnotic."},
            {"id": "D", "text": "Age-related reductions in hepatic oxidative metabolism and renal clearance prolong drug half-lives, combined with increased central nervous system pharmacodynamic sensitivity and decreased physiological reserve, significantly elevating risks of cognitive impairment, delirium, falls, hip fractures, and motor vehicle accidents."}
        ],
        "correctAnswer": "D",
        "explanation": "Aging is accompanied by decreased hepatic cytochrome P450 enzyme activity, decreased renal excretion, increased proportion of body fat (expanding the volume of distribution of lipophilic drugs), and increased pharmacodynamic sensitivity of cerebral GABA-A receptors. Consequently, benzodiazepine clearance is markedly delayed, leading to cumulative drug toxicity, psychomotor incoordination, delirium, falls, and fractures, as highlighted in the American Geriatrics Society Beers Criteria.",
        "incorrectExplanations": {
            "A": "Temazepam is administered orally and absorbed in the GI tract, not transdermally.",
            "B": "Aging decreases, rather than increases, glomerular filtration and hepatic clearance.",
            "C": "Benzodiazepines do not cause immediate permanent blindness."
        },
        "learningObjective": "Analyze the geriatric pharmacokinetic and pharmacodynamic vulnerabilities to benzodiazepines and apply the Beers Criteria.",
        "reference": "American Geriatrics Society. (2019). 2019 Updated AGS Beers Criteria for potentially inappropriate medication use in older adults. Journal of the American Geriatrics Society, 67(4), 674-694.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # ---------------------------------------------------------
    # Topic 7: Dual Diagnosis (Co-occurring Disorders) (MHN-Q1275 to MHN-Q1284)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1275",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Foundation",
        "questionText": "Epidemiological studies, including the landmark Epidemiologic Catchment Area (ECA) study and the National Comorbidity Survey (NCS), indicate approximately what percentage of individuals diagnosed with severe and persistent mental illness (SPMI, such as schizophrenia or bipolar disorder) experience a co-occurring substance use disorder during their lifetime?",
        "options": [
            {"id": "A", "text": "Approximately 50%"},
            {"id": "B", "text": "Less than 2%"},
            {"id": "C", "text": "Exactly 100%"},
            {"id": "D", "text": "Approximately 12%"}
        ],
        "correctAnswer": "A",
        "explanation": "Major psychiatric epidemiological surveys (including the ECA and NCS studies) consistently demonstrate that roughly 50% of individuals with severe and persistent mental illness (schizophrenia, bipolar I disorder) meet lifetime diagnostic criteria for a co-occurring substance use disorder. This exceptionally high comorbidity underscores that dual diagnosis is an expectation rather than an exception in psychiatric nursing practice.",
        "incorrectExplanations": {
            "B": "Less than 2% dramatically understates the prevalence of dual diagnosis in severe mental illness.",
            "C": "While highly prevalent, not all individuals with SPMI experience substance use disorders.",
            "D": "Twelve percent reflects general population substance use rates, not the concentrated comorbidity observed in severe psychiatric illness."
        },
        "learningObjective": "Identify epidemiological prevalence rates of co-occurring substance use disorders in severe mental illness.",
        "reference": "Regier, D. A., et al. (1990). Comorbidity of mental disorders with alcohol and other drug abuse: results from the Epidemiologic Catchment Area (ECA) study. JAMA, 264(19), 2511-2518.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1276",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Foundation",
        "questionText": "Which theoretical formulation, originally proposed by Edward Khantzian, posits that individuals do not choose substances of abuse randomly, but rather select specific classes of drugs whose distinct psychopharmacological actions alleviate specific, intolerable subjective affective states and psychological distress?",
        "options": [
            {"id": "A", "text": "The Moral Model of Addiction"},
            {"id": "B", "text": "The Self-Medication Hypothesis"},
            {"id": "C", "text": "The Social Learning Theory of Deviance"},
            {"id": "D", "text": "The Genetic Inevitability Model"}
        ],
        "correctAnswer": "B",
        "explanation": "Edward Khantzian's Self-Medication Hypothesis posits that individuals select specific addictive substances based on their pharmacological capacity to relieve specific painful affective states: e.g., individuals with rage/aggression may use opioids to soothe dysphoria; individuals with depression/apathy may use stimulants to boost energy; and individuals with panic/social anxiety may use alcohol or sedatives to blunt hyperarousal.",
        "incorrectExplanations": {
            "A": "The Moral Model views addiction as a willful character defect, not a coping strategy for psychological pain.",
            "C": "Social Learning Theory focuses on observational modeling and environmental contingencies.",
            "D": "Genetic models focus on inherited biological vulnerabilities rather than conscious/unconscious drug selection for affect regulation."
        },
        "learningObjective": "Explain the core tenets of the Self-Medication Hypothesis in dual diagnosis formulation.",
        "reference": "Khantzian, E. J. (1997). The self-medication hypothesis of substance use disorders: a reconsideration and recent applications. Harvard Review of Psychiatry, 4(5), 231-244.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1277",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Intermediate",
        "questionText": "In contemporary dual diagnosis neurobiology, what is the 'common liability' or 'shared neurobiological vulnerability' model explaining the co-occurrence of psychosis and substance use disorders?",
        "options": [
            {"id": "A", "text": "Both conditions are caused exclusively by a shared bacterial infection of the parietal cortex."},
            {"id": "B", "text": "Substance use and psychosis share no common biological pathways whatsoever."},
            {"id": "C", "text": "Intrinsic dysregulation within the mesocorticolimbic dopamine reward circuitry (ventral tegmental area to nucleus accumbens) underlies both the aberrant salience and cognitive deficits of psychosis and the heightened susceptibility to substance reinforcement."},
            {"id": "D", "text": "Psychiatric medications directly synthesize illegal street drugs inside the gut microbiome."}
        ],
        "correctAnswer": "C",
        "explanation": "The shared vulnerability model proposes that pre-existing abnormalities in the mesocorticolimbic dopamine reward system underlie both disorders: dysregulated striatal dopamine firing produces aberrant salience (generating delusions and hallucinations in psychosis) while simultaneously impairing reward processing, predisposing the individual to enhanced reward sensitivity and compulsive substance seeking.",
        "incorrectExplanations": {
            "A": "Psychosis and substance use disorders are not caused by bacterial infections of the parietal cortex.",
            "B": "Extensive neuroimaging demonstrates substantial shared neural circuitry, particularly in dopamine pathways.",
            "D": "Psychotropic drugs do not transform into illicit drugs within the gut."
        },
        "learningObjective": "Describe the shared neurobiological mechanisms linking mesolimbic dopamine dysregulation to psychosis and addiction.",
        "reference": "Chambers, R. A., et al. (2001). A neurobiological basis for substance abuse comorbidity in schizophrenia. Biological Psychiatry, 50(2), 71-83.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1278",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Intermediate",
        "questionText": "Historically, healthcare systems treated co-occurring mental illness and substance use either sequentially (one disorder treated before the other) or in parallel (treated simultaneously by separate agencies). Why has Integrated Dual Diagnosis Treatment (IDDT) replaced these fragmented approaches as the gold standard of care?",
        "options": [
            {"id": "A", "text": "IDDT is cheaper because it eliminates all clinical nurses and relies entirely on volunteers."},
            {"id": "B", "text": "Sequential treatment worked perfectly, but parallel treatment was banned by international law."},
            {"id": "C", "text": "IDDT forces all patients to sign mandatory 5-year abstinence contracts before receiving mental healthcare."},
            {"id": "D", "text": "IDDT treats both psychiatric and substance use disorders concurrently within a single unified multidisciplinary team, using a shared formulation, staged interventions, and assertive outreach, preventing patients from falling between fragmented service gaps."}
        ],
        "correctAnswer": "D",
        "explanation": "Sequential models historically excluded patients from mental health care until they achieved abstinence (which they could not do untreated), while parallel models led to conflicting advice, incompatible treatment philosophies, and high dropout. Integrated Dual Diagnosis Treatment (IDDT) provides coordinated, synchronized mental health and addiction care by a single team using stage-wise interventions and harm reduction.",
        "incorrectExplanations": {
            "A": "IDDT relies on specialized, highly trained multidisciplinary clinicians, not unpaid volunteers.",
            "B": "Sequential treatment failed because substance use exacerbated psychiatric symptoms and vice versa.",
            "C": "IDDT embraces harm reduction and does not mandate pre-treatment abstinence contracts."
        },
        "learningObjective": "Contrast Integrated Dual Diagnosis Treatment (IDDT) with obsolete sequential and parallel treatment models.",
        "reference": "Drake, R. E., et al. (2001). Implementing dual diagnosis services for clients with severe mental illness. Psychiatric Services, 52(4), 469-476.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1279",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Intermediate",
        "questionText": "Which clinical and service outcomes are consistently demonstrated in high-quality randomized controlled trials evaluating Integrated Dual Diagnosis Treatment (IDDT) compared to standard fragmented care?",
        "options": [
            {"id": "A", "text": "Substantial reductions in psychiatric hospitalization rates, improved treatment retention, decreased substance misuse, and enhanced overall functional recovery."},
            {"id": "B", "text": "Immediate 100% cure of schizophrenia within 14 days of enrollment."},
            {"id": "C", "text": "Increased emergency department presentations and higher arrest rates."},
            {"id": "D", "text": "Total elimination of all required psychotropic pharmacotherapy."}
        ],
        "correctAnswer": "A",
        "explanation": "Robust clinical trials evaluate IDDT and demonstrate significant clinical benefits: reduced psychiatric inpatient days, fewer relapses, lower substance consumption, higher treatment retention, improved psychosocial functioning, and reduced criminal justice contacts.",
        "incorrectExplanations": {
            "B": "Schizophrenia is a chronic condition; IDDT promotes long-term recovery and symptom stability, not a 14-day cure.",
            "C": "IDDT decreases emergency visits and legal entanglements.",
            "D": "Psychotropic pharmacotherapy remains an essential component of integrated care."
        },
        "learningObjective": "Identify evidence-based clinical outcomes associated with integrated dual diagnosis service delivery.",
        "reference": "Mueser, K. T., et al. (2003). Integrated Treatment for Dual Disorders: A Guide to Effective Practice. Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1280",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Advanced",
        "questionText": "The COMPASS Programme (Combined Psychosis and Substance Use) is an evidence-based clinical model tailored specifically for clients with dual diagnosis. What are the core therapeutic pillars of this intervention?",
        "options": [
            {"id": "A", "text": "Involuntary seclusion and daily urine drug screening under police observation."},
            {"id": "B", "text": "An integrated cognitive-behavioral and motivational framework combining motivational enhancement, psychoeducation on the interaction between psychosis and drugs, cognitive restructuring, relapse prevention, and family/carer involvement."},
            {"id": "C", "text": "High-dose antipsychotic monotherapy without any psychological interventions."},
            {"id": "D", "text": "Exclusively spiritual conversion and wilderness survival training."}
        ],
        "correctAnswer": "B",
        "explanation": "The COMPASS model (Barrowclough et al.) integrates Motivational Interviewing (MI) and Cognitive Behavioural Therapy (CBT) with family intervention specifically designed for psychosis and substance use. It addresses the bi-directional interaction between mental health symptoms and substance use, coping strategies, cognitive appraisal of psychotic experiences, and social network reinforcement.",
        "incorrectExplanations": {
            "A": "Involuntary seclusion and coercive policing destroy therapeutic engagement.",
            "C": "COMPASS is fundamentally a psychosocial and cognitive-behavioral model.",
            "D": "Wilderness survival and spiritual conversion are not clinical components of COMPASS."
        },
        "learningObjective": "Describe the therapeutic components of the COMPASS model for co-occurring psychosis and substance misuse.",
        "reference": "Barrowclough, C., et al. (2001). Randomized controlled trial of motivational interviewing, cognitive behavior therapy, and family intervention for patients with comorbid schizophrenia and substance use disorders. American Journal of Psychiatry, 158(10), 1706-1713.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1281",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Advanced",
        "questionText": "During a routine admission to an acute mental health unit, a nurse administers the Drug Abuse Screening Test (DAST-10) to a client with bipolar disorder. The client scores 7. How should the nurse interpret this clinical finding and what is the corresponding clinical recommendation?",
        "options": [
            {"id": "A", "text": "Score 0: No problem; no action required."},
            {"id": "B", "text": "Score 1–2: Low level problem; provide brief educational leaflet."},
            {"id": "C", "text": "Score 6–8: Substantial level problem; warrants comprehensive specialized assessment and intensive integrated dual diagnosis intervention."},
            {"id": "D", "text": "Score 7: Inconclusive; the DAST-10 is invalid for individuals with mood disorders."}
        ],
        "correctAnswer": "C",
        "explanation": "On the DAST-10: a score of 0 indicates no problem; 1–2 indicates low problem level (monitoring/brief advice); 3–5 indicates moderate problem level (brief intervention); 6–8 indicates a substantial problem level; and 9–10 reflects a severe problem level. A score of 7 falls into the 'substantial' category, requiring in-depth assessment and intensive integrated treatment.",
        "incorrectExplanations": {
            "A": "A score of 7 indicates substantial substance-related problems.",
            "B": "Low level corresponds to scores 1–2.",
            "D": "The DAST-10 is a validated, reliable screening instrument for populations with co-occurring psychiatric disorders."
        },
        "learningObjective": "Interpret DAST-10 screening scores accurately in dual diagnosis psychiatric triage.",
        "reference": "Skinner, H. A. (1982). The drug abuse screening test. Addictive Behaviors, 7(4), 363-371.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1282",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Advanced",
        "questionText": "Why is the risk of completed suicide and severe deliberate self-harm synergistically multiplied in clients with dual diagnosis (e.g., severe depression or bipolar disorder combined with alcohol or substance use disorder) compared to clients with a single diagnosis?",
        "options": [
            {"id": "A", "text": "Because substances alter blood hemoglobin levels to prevent oxygen binding."},
            {"id": "B", "text": "Substance use actually protects against suicide by providing chemical contentment."},
            {"id": "C", "text": "Because genetic testing shows dual diagnosis patients have an absent serotonin transporter gene."},
            {"id": "D", "text": "Substance intoxication increases impulsivity, diminishes prefrontal cognitive restraint, intensifies depressive dysphoria, disrupts social and familial support systems, and facilitates lethal means acquisition."}
        ],
        "correctAnswer": "D",
        "explanation": "Substance misuse exerts a synergistic, multiplying effect on suicidality in psychiatric illness. Acute intoxication impairs frontal inhibitory control, escalates impulsivity, and turns passive suicidal ideation into active lethal attempts. Furthermore, chronic substance dependence exacerbates depressive despair, causes financial/social ruin, and accelerates therapeutic non-adherence.",
        "incorrectExplanations": {
            "A": "Hemoglobin oxygen binding alterations are not the mechanism of increased suicidal behavior.",
            "B": "Substance use substantially escalates, rather than protects against, suicide risk.",
            "C": "Dual diagnosis suicidality is multi-factorial, not driven by an absent gene."
        },
        "learningObjective": "Analyze the synergistic mechanisms through which substance use elevates suicide risk in psychiatric disorders.",
        "reference": "Hawton, K., et al. (2013). Risk factors for suicide in individuals with depression: a systematic review. Journal of Affective Disorders, 147(1-3), 17-28.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1283",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Advanced",
        "questionText": "What clinical diagnostic error is exemplified by 'diagnostic overshadowing' when a mental health team evaluates a client with known substance use disorder presenting with acute psychiatric symptoms?",
        "options": [
            {"id": "A", "text": "Attributing all physical illnesses to an underlying brain tumor."},
            {"id": "B", "text": "The tendency for clinicians to misattribute all acute emotional distress, affective instability, or psychotic symptoms entirely to substance intoxication or withdrawal, thereby overlooking and failing to treat an underlying primary psychiatric disorder (or vice versa)."},
            {"id": "C", "text": "Failing to document the client's preferred pronouns on hospital charts."},
            {"id": "D", "text": "Ordering an excessive number of neuroimaging scans for a minor headache."}
        ],
        "correctAnswer": "B",
        "explanation": "Diagnostic overshadowing occurs when clinicians allow the presence of one condition (such as substance use or intellectual disability) to 'overshadow' and blind them to symptoms of another condition. In dual diagnosis, clinicians frequently dismiss hallucinations, severe depression, or suicidality as 'merely drug-induced' or 'drug-seeking behavior,' neglecting serious primary psychiatric disorders and denying timely treatment.",
        "incorrectExplanations": {
            "A": "Over-diagnosing brain tumors is not diagnostic overshadowing.",
            "C": "Documenting pronouns is culturally affirming practice, not diagnostic overshadowing.",
            "D": "Excessive imaging represents defensive or low-value medicine, not diagnostic overshadowing."
        },
        "learningObjective": "Define and prevent diagnostic overshadowing during psychiatric assessment of individuals who use substances.",
        "reference": "Jones, S., et al. (2008). Dual diagnosis in the mental health inpatient setting: a review of the literature. Journal of Psychiatric and Mental Health Nursing, 15(6), 496-504.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1284",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Dual Diagnosis (Co-occurring Disorders)",
        "difficulty": "Expert",
        "questionText": "In Osher and Kofoed's seminal 4-stage model of treatment for individuals with dual diagnosis, what is the correct sequential order of stages, and which primary nursing task characterizes the 'Persuasion' stage?",
        "options": [
            {"id": "A", "text": "Active Treatment -> Relapse Prevention -> Engagement -> Persuasion; task is prescribing Antabuse."},
            {"id": "B", "text": "Relapse Prevention -> Action -> Precontemplation -> Discharge; task is signing an abstinence pledge."},
            {"id": "C", "text": "Engagement -> Persuasion -> Active Treatment -> Relapse Prevention; during Persuasion, the nurse works with an engaged client who does not yet acknowledge the need for substance reduction to help them recognize the negative impact of substance use on their personal goals and mental health."},
            {"id": "D", "text": "Detoxification -> Confinement -> Confrontation -> Maintenance; task is aggressive confrontation."}
        ],
        "correctAnswer": "C",
        "explanation": "Osher and Kofoed's stages of treatment are: (1) Engagement (establishing trust and alliance without requiring discussion of substance change); (2) Persuasion (motivational enhancement to help the client recognize how substance use impairs their own valued goals and mental stability); (3) Active Treatment (developing explicit skills and strategies to reduce/stop use); and (4) Relapse Prevention (maintaining gains and developing resilience).",
        "incorrectExplanations": {
            "A": "This sequence reverses the treatment trajectory.",
            "B": "This confuses Osher and Kofoed's model with the Transtheoretical Model.",
            "D": "Coercive confrontation is countertherapeutic and directly contradicts dual diagnosis practice standards."
        },
        "learningObjective": "Structure dual diagnosis nursing care using Osher and Kofoed's four stages of treatment.",
        "reference": "Osher, F. C., & Kofoed, L. L. (1989). Treatment of patients with psychiatric and psychoactive substance abuse disorders. Hospital & Community Psychiatry, 40(10), 1025-1030.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # ---------------------------------------------------------
    # Topic 8: Motivational Interviewing in Substance Use (MHN-Q1285 to MHN-Q1294)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1285",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Foundation",
        "questionText": "The underlying 'Spirit' of Motivational Interviewing (MI), as formulated by Miller and Rollnick, is encapsulated by the acronym PACE (Partnership, Acceptance, Compassion, and Evocation). Which clinical practice represents the principle of 'Evocation'?",
        "options": [
            {"id": "A", "text": "The nurse lectures the client on the medical dangers of liver cirrhosis for 45 minutes."},
            {"id": "B", "text": "The nurse orders the client to memorize a standardized set of hospital rules."},
            {"id": "C", "text": "The nurse gives the client a pre-written list of reasons why they must stop using substances."},
            {"id": "D", "text": "The nurse draws out and elicits the client's own internal ideas, values, motivations, and arguments for change, operating from the premise that the wisdom and motivation reside within the client."}
        ],
        "correctAnswer": "D",
        "explanation": "In MI, Evocation is the opposite of an educational or deficit model where the clinician 'instills' knowledge or motivation into an empty recipient. Instead, Evocation assumes the client already possesses the intrinsic motivations, strengths, and personal reasons for change; the nurse's role is to elicit and evoke these internal motivations through open exploration.",
        "incorrectExplanations": {
            "A": "Lecturing is the 'expert trap' and provokes sustain talk and discord.",
            "B": "Ordering compliance violates autonomy and is the opposite of evocation.",
            "C": "Imposing reasons from the outside fails to elicit the client's internal value system."
        },
        "learningObjective": "Differentiate Evocation from didactic advice-giving within the Spirit of Motivational Interviewing.",
        "reference": "Miller, W. R., & Rollnick, S. (2012). Motivational Interviewing: Helping People Change (3rd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1286",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Foundation",
        "questionText": "Within the core communication skills of Motivational Interviewing (OARS: Open-ended questions, Affirmations, Reflective listening, Summarizing), which nursing question best exemplifies an effective 'Open-ended Question' during an initial substance use exploration?",
        "options": [
            {"id": "A", "text": "'What role does alcohol play in your life right now, and what are some of the things you might like to be different?'"},
            {"id": "B", "text": "'Do you drink every single day?'"},
            {"id": "C", "text": "'Are you going to take your Antabuse tablet this morning, yes or no?'"},
            {"id": "D", "text": "'Have you ever attended an Alcoholics Anonymous meeting before?'"}
        ],
        "correctAnswer": "A",
        "explanation": "Open-ended questions invite broad exploration, cannot be answered with a simple 'yes' or 'no', and encourage the client to tell their story and reflect on their values. Option A invites the client to describe their subjective experience and open the door to change talk.",
        "incorrectExplanations": {
            "B": "This is a closed question eliciting a brief factual answer ('yes' or 'no').",
            "C": "This is a closed, confrontational binary choice.",
            "D": "This is a closed inquiry eliciting a single historical fact."
        },
        "learningObjective": "Formulate open-ended questions that elicit reflection and client exploration in motivational interviewing.",
        "reference": "Miller, W. R., & Rollnick, S. (2012). Motivational Interviewing: Helping People Change (3rd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1287",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Intermediate",
        "questionText": "A client with alcohol dependence remarks with a heavy sigh: 'My wife says she's going to pack up the children and leave if I have one more drink. But coming home from work is so stressful that drinking is the only way I know how to unwind.' Which nurse response represents an effective 'Complex Reflection'?",
        "options": [
            {"id": "A", "text": "'Your wife is packing her bags to leave.'"},
            {"id": "B", "text": "'You're feeling caught in a painful bind: alcohol feels like your only buffer against overwhelming work stress, yet you desperately fear losing your family, whom you cherish deeply.'"},
            {"id": "C", "text": "'Why don't you simply find a new job that isn't so stressful?'"},
            {"id": "D", "text": "'You really shouldn't let work get to you like that.'"}
        ],
        "correctAnswer": "B",
        "explanation": "A complex reflection goes beyond repeating the client's spoken words (simple reflection) by capturing the deeper meaning, unstated emotions, and underlying ambivalence. Option B reflects both sides of the decisional conflict—the coping function of alcohol and the deep terror of losing his beloved family—fostering cognitive resolution of ambivalence.",
        "incorrectExplanations": {
            "A": "This is a simple reflection that merely parrots the client's words without adding emotional depth.",
            "C": "This offers unsolicited advice and falls into the 'fixing reflex.'",
            "D": "This is dismissive and invalidating of the client's emotional experience."
        },
        "learningObjective": "Construct complex reflections that illuminate client ambivalence and deepen the therapeutic alliance.",
        "reference": "Rollnick, S., Miller, W. R., & Butler, C. C. (2008). Motivational Interviewing in Health Care: Helping Patients Change Behavior. Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1288",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Intermediate",
        "questionText": "In Motivational Interviewing, client speech is categorized into 'Sustain Talk' and 'Change Talk.' Change talk is further divided into Preparatory change talk (DARN) and Mobilizing change talk (CAT). Which acronym components comprise Preparatory Change Talk?",
        "options": [
            {"id": "A", "text": "Depression, Anxiety, Rage, Neurosis"},
            {"id": "B", "text": "Detoxification, Abstinence, Relapse, Nutrition"},
            {"id": "C", "text": "Desire, Ability, Reasons, and Need"},
            {"id": "D", "text": "Denial, Anger, Resistance, Negotiation"}
        ],
        "correctAnswer": "C",
        "explanation": "Preparatory Change Talk reflects the client's consideration of change and is categorized by the DARN acronym: Desire ('I want to stop drinking'), Ability ('I could cut down on weekends'), Reasons ('If I quit, I'd save money and sleep better'), and Need ('I must do something because my health is failing'). Mobilizing change talk (CAT) consists of Commitment, Activation, and Taking steps.",
        "incorrectExplanations": {
            "A": "These are psychiatric symptom states, not MI change talk categories.",
            "B": "These are addiction treatment phases, not the DARN acronym.",
            "D": "These represent Kubler-Ross grief stages, not motivational change talk."
        },
        "learningObjective": "Differentiate Preparatory Change Talk (DARN) from Mobilizing Change Talk (CAT) in motivational discourse.",
        "reference": "Amrhein, P. C., et al. (2003). Client commitment language during motivational interviewing predicts drug use outcomes. Journal of Consulting and Clinical Psychology, 71(5), 862-878.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1289",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Intermediate",
        "questionText": "During a motivational conversation, which of the following client verbalizations represents Mobilizing Change Talk specifically indicating 'Commitment' (the 'C' in CAT)?",
        "options": [
            {"id": "A", "text": "'I wish I didn't spend so much money on cocaine every weekend.'"},
            {"id": "B", "text": "'I suppose I might be able to stop if my friends supported me.'"},
            {"id": "C", "text": "'My doctor tells me my blood pressure will improve if I cut down.'"},
            {"id": "D", "text": "'I promise you that starting tomorrow morning, I will attend the 10:00 AM outpatient dual diagnosis group session.'"}
        ],
        "correctAnswer": "D",
        "explanation": "Commitment language (the 'C' in Mobilizing Change Talk CAT) represents an explicit pledge, promise, or agreement to take concrete action. 'I promise you that starting tomorrow morning, I will attend the group' is unambiguous commitment language, which strongly predicts actual behavioral change.",
        "incorrectExplanations": {
            "A": "This expresses Desire ('I wish'), which is preparatory change talk.",
            "B": "This expresses Ability ('I might be able to'), which is preparatory change talk.",
            "C": "This expresses a Reason, which is preparatory change talk."
        },
        "learningObjective": "Identify Mobilizing Commitment language as a key predictor of behavioral change in Motivational Interviewing.",
        "reference": "Amrhein, P. C. (2004). How does motivational interviewing work? What client talk reveals. Journal of Cognitive Psychotherapy, 18(4), 323-336.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1290",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Advanced",
        "questionText": "A 22-year-old client with cannabis misuse crosses his arms, glares at the nurse, and angrily states: 'You nurses are all the same! You think you know everything and have the right to tell me how to live my life. Nobody can force me to quit weed!' What is the most skillful response consistent with 'Rolling with Resistance' (dancing rather than wrestling)?",
        "options": [
            {"id": "A", "text": "'You're absolutely right; nobody can force you to change. Whether you choose to stop using cannabis, cut back, or continue exactly as you are is entirely your personal decision. I'm just here to support you in exploring what you want for your future.'"},
            {"id": "B", "text": "'Under hospital policy and the law, I am a registered nurse and you are required to listen to my medical advice.'"},
            {"id": "C", "text": "'If you keep that hostile attitude, I will have security escort you out and discharge you immediately.'"},
            {"id": "D", "text": "'Why are you being so defensive when I'm only trying to help you?'"}
        ],
        "correctAnswer": "A",
        "explanation": "In Motivational Interviewing, client discord or defensiveness is viewed as a signal of interpersonal dissonance, often triggered when the clinician pushes for change faster than the client is ready. 'Rolling with resistance' involves avoiding arguing, defusing the power struggle, explicitly honoring the client's ultimate autonomy and personal control, and redirecting the conversation collaboratively.",
        "incorrectExplanations": {
            "B": "Asserting professional authority and hierarchy invites defiance and escalates conflict.",
            "C": "Threatening punitive discharge destroys the therapeutic alliance.",
            "D": "Challenging the client's defensiveness provokes further sustain talk and hostility."
        },
        "learningObjective": "Demonstrate the clinical skill of rolling with resistance to defuse therapeutic discord.",
        "reference": "Miller, W. R., & Rollnick, S. (2012). Motivational Interviewing: Helping People Change (3rd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1291",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Advanced",
        "questionText": "In Motivational Interviewing, the clinical strategy of 'Developing Discrepancy' is designed to motivate behavioral change. How does the psychiatric nurse operationalize this technique?",
        "options": [
            {"id": "A", "text": "By pointing out discrepancies between the client's statements and what their family secretly reported to the nurse."},
            {"id": "B", "text": "By helping the client identify and examine the profound gap between their deeply held personal core values, life goals, and self-image versus their current substance-using behaviors and consequences."},
            {"id": "C", "text": "By calculating the mathematical difference between the client's urine toxicology results and standard hospital ranges."},
            {"id": "D", "text": "By confronting the client with criminal statistics regarding individuals with substance misuse."}
        ],
        "correctAnswer": "B",
        "explanation": "Developing discrepancy creates an internal psychological motivation for change. The nurse explores what the client values most (e.g., being a loving parent, financial independence, career achievement) and gently contrasts this with where their current substance use is leading them. When clients perceive a substantial gap between who they want to be and what their behavior produces, intrinsic motivation to resolve the discrepancy surges.",
        "incorrectExplanations": {
            "A": "Using family collateral to trap the client generates feelings of betrayal and defensiveness.",
            "C": "Mathematical toxicology reporting does not evoke internal emotional values.",
            "D": "Impersonal crime statistics produce detachment rather than personal reflection."
        },
        "learningObjective": "Apply the technique of Developing Discrepancy between client core values and substance use behaviors.",
        "reference": "Miller, W. R., & Rollnick, S. (2012). Motivational Interviewing: Helping People Change (3rd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1292",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Advanced",
        "questionText": "Under Prochaska and DiClemente's Transtheoretical Model (Stages of Change), a client arrives at the dual diagnosis service stating: 'I don't have an alcohol problem. My boss and my wife are just paranoid and overreacting. I can handle my liquor better than anyone.' Which stage of change is this client in, and what is the appropriate primary nursing objective?",
        "options": [
            {"id": "A", "text": "Action stage; goal is teaching behavioral refusal skills in bars."},
            {"id": "B", "text": "Preparation stage; goal is setting a concrete quit date within 7 days."},
            {"id": "C", "text": "Precontemplation stage; goal is to raise awareness of personal risks, build trust, and gently explore the client's own perceptions without demanding immediate change."},
            {"id": "D", "text": "Maintenance stage; goal is preventing long-term relapse."}
        ],
        "correctAnswer": "C",
        "explanation": "Clients in the Precontemplation stage do not intend to take action in the foreseeable future (usually defined as within the next 6 months) and are often unaware or in denial of the adverse consequences of their behavior. The nurse's objective is not to force action (which causes fierce resistance), but to establish rapport, raise awareness, explore how substance use impacts their life, and plant seeds for reflection.",
        "incorrectExplanations": {
            "A": "Action stage interventions assume the client has already decided to modify behavior, which is clearly not the case here.",
            "B": "Preparation stage interventions (setting quit dates) will fail because the client does not acknowledge a problem.",
            "D": "Maintenance applies to individuals who have maintained sustained change for at least 6 months."
        },
        "learningObjective": "Match psychiatric nursing interventions to the client's specific stage of change within the Transtheoretical Model.",
        "reference": "Prochaska, J. O., & DiClemente, C. C. (1983). Stages and processes of self-change of smoking: toward an integrative model of change. Journal of Consulting and Clinical Psychology, 51(3), 390-395.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1293",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Advanced",
        "questionText": "A client in the Contemplation stage of change for opioid use disorder states: 'I love the warm relief heroin gives me from my emotional trauma, but I hate living in fear of overdosing and spending every cent I have.' What is the clinical hallmark of the Contemplation stage, and how should the psychiatric nurse intervene?",
        "options": [
            {"id": "A", "text": "Total denial of any negative consequences; enforce immediate locked seclusion."},
            {"id": "B", "text": "Active implementation of lifestyle change; provide an AA 90-day chip."},
            {"id": "C", "text": "Permanent resolution of all psychiatric trauma; discharge from case management."},
            {"id": "D", "text": "Acute ambivalence (simultaneously experiencing compelling reasons to continue and powerful reasons to quit); the nurse should explore the pros and cons (decisional balance) and elicit change talk to tip the scale toward change."}
        ],
        "correctAnswer": "D",
        "explanation": "The defining hallmark of the Contemplation stage is ambivalence: the client recognizes they have a problem and considers change, but feels caught between the perceived benefits of substance use and the mounting costs. The nurse's task is to explore this ambivalence (decisional balance), validate both perspectives, and selectively evoke and amplify change talk to help tip the scales toward preparation and action.",
        "incorrectExplanations": {
            "A": "Denial characterizes precontemplation, not contemplation where consequences are recognized.",
            "B": "Active behavioral implementation occurs in the Action stage.",
            "C": "Contemplation does not imply trauma resolution."
        },
        "learningObjective": "Facilitate resolution of ambivalence for clients in the Contemplation stage of change.",
        "reference": "Prochaska, J. O., Norcross, J. C., & DiClemente, C. C. (1995). Changing for Good. Avon Books.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1294",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Motivational Interviewing in Substance Use",
        "difficulty": "Expert",
        "questionText": "A client with stimulant use disorder has purchased a calendar, circled a quit date 10 days away, researched local SMART Recovery meetings, and disposed of their drug paraphernalia. When the client attends their nursing review, how should the nurse classify this stage of change, and what is the priority clinical nursing task?",
        "options": [
            {"id": "A", "text": "Preparation stage; the priority task is to collaborate on developing a realistic, concrete Action Plan, identify potential obstacles, and bolster self-efficacy."},
            {"id": "B", "text": "Precontemplation stage; the priority task is to confront the client with urine toxicology screens."},
            {"id": "C", "text": "Action stage; the priority task is to declare the client fully recovered and close the clinical case."},
            {"id": "D", "text": "Relapse stage; the priority task is to admit the client to an acute locked psychiatric ward."}
        ],
        "correctAnswer": "A",
        "explanation": "In the Preparation stage, the client intends to take action in the immediate future (typically within the next 30 days) and has begun taking small behavioral steps (e.g., choosing a quit date, obtaining resources, getting rid of paraphernalia). The nurse's role is to help formulate a specific, viable action plan, identify triggers, rehearse coping strategies, and reinforce self-efficacy.",
        "incorrectExplanations": {
            "B": "The client has moved far beyond precontemplation and is actively preparing for change.",
            "C": "The Action stage begins when the behavioral change actually starts (e.g., abstinence commences); declaring recovery and closing the case is premature and hazardous.",
            "D": "Taking preparation steps is positive recovery progress, not a relapse warranting locked admission."
        },
        "learningObjective": "Formulate a personalized Action Plan for clients transitioning from Preparation to Action in the Transtheoretical Model.",
        "reference": "Connors, G. J., et al. (2013). Substance Abuse Treatment and the Stages of Change: Selecting and Planning Interventions (2nd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # ---------------------------------------------------------
    # Topic 9: Harm Reduction Principles (MHN-Q1295 to MHN-Q1304)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1295",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Foundation",
        "questionText": "What is the foundational philosophical and ethical tenet of Harm Reduction in substance use and mental health nursing practice?",
        "options": [
            {"id": "A", "text": "Substance use must be totally eradicated from society through strict criminalization and incarceration."},
            {"id": "B", "text": "Prioritizing the immediate reduction of drug-related health, social, and legal harms (e.g., fatal overdose, viral infections) without requiring immediate cessation of drug use as a prerequisite for receiving respectful healthcare."},
            {"id": "C", "text": "Encouraging individuals who do not use substances to begin experimenting with drugs under nursing supervision."},
            {"id": "D", "text": "Conditioning healthcare access on 100% verified continuous drug abstinence."}
        ],
        "correctAnswer": "B",
        "explanation": "Harm reduction is a pragmatic, compassionate, and evidence-based public health approach. It recognizes that complete abstinence may not be an immediate or realistic goal for everyone. By prioritizing the prevention of fatal overdoses, transmission of bloodborne viruses (HIV, HCV), and injection-related injuries, harm reduction preserves life and health while meeting people 'where they are at' with dignity.",
        "incorrectExplanations": {
            "A": "Criminalization and zero-tolerance approaches are opposite to the public health principles of harm reduction.",
            "C": "Harm reduction seeks to minimize harm among people who currently use substances, never to encourage drug initiation.",
            "D": "Mandatory abstinence as a precondition for healthcare is a barrier to care that violates harm reduction ethics."
        },
        "learningObjective": "Define the foundational ethical and philosophical principles of harm reduction in psychiatric nursing.",
        "reference": "Marlatt, G. A., et al. (2011). Harm Reduction: Pragmatic Strategies for Managing High-Risk Behaviors (2nd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1296",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Foundation",
        "questionText": "Extensive international public health evaluations by the World Health Organization (WHO) and the Centers for Disease Control and Prevention (CDC) have proven that Needle and Syringe Programmes (NSPs) achieve which primary epidemiological outcome?",
        "options": [
            {"id": "A", "text": "They cause a 400% increase in neighborhood crime and illicit drug use."},
            {"id": "B", "text": "They completely cure hepatitis C within 24 hours of needle exchange."},
            {"id": "C", "text": "They dramatically reduce the transmission of bloodborne pathogens (HIV, Hepatitis B, and Hepatitis C) without increasing illicit drug injection rates or community syringe litter."},
            {"id": "D", "text": "They have no effect on viral transmission rates."}
        ],
        "correctAnswer": "C",
        "explanation": "Decades of robust global surveillance demonstrate that Needle and Syringe Programmes (NSPs) are highly cost-effective public health interventions that substantially reduce HIV and Hepatitis C incidence among people who inject drugs. Crucially, evidence demonstrates NSPs do NOT increase drug use, do not encourage injection initiation, and facilitate entry into drug treatment programs through therapeutic contact.",
        "incorrectExplanations": {
            "A": "Decades of evidence show NSPs do not increase local crime or drug injection rates.",
            "B": "NSPs prevent viral transmission; they do not treat or cure established infections.",
            "D": "NSPs demonstrate marked, statistically significant reductions in viral transmission."
        },
        "learningObjective": "Summarize the epidemiological evidence base supporting Needle and Syringe Programmes in preventing bloodborne viral transmission.",
        "reference": "World Health Organization. (2004). Effectiveness of sterile needle and syringe programming in reducing HIV/AIDS among injecting drug users. WHO Evidence for Action Technical Papers.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1297",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Intermediate",
        "questionText": "What does clinical evidence demonstrate regarding the impact of Supervised Consumption Facilities (SCFs / Overdose Prevention Centers) on public health and community safety?",
        "options": [
            {"id": "A", "text": "SCFs result in frequent fatal overdoses inside the facilities and higher rates of neighborhood syringe waste."},
            {"id": "B", "text": "SCFs are strictly prohibited by the United Nations because they encourage adolescent drug experimentation."},
            {"id": "C", "text": "SCFs require clients to be admitted for mandatory long-term psychiatric hospitalization."},
            {"id": "D", "text": "SCFs have achieved zero fatal overdoses within their facilities worldwide, reduce public drug consumption and discarded syringes, provide immediate life-saving overdose intervention, and increase client enrollment in detoxification and addiction treatment."}
        ],
        "correctAnswer": "D",
        "explanation": "Supervised Consumption Facilities (SCFs) provide a sterile, medically monitored environment for individuals to consume pre-obtained substances under nursing oversight. Globally, millions of injections have occurred across hundreds of SCFs with zero recorded overdose fatalities. Research demonstrates they reduce public injecting, lower ambulance callouts, reduce emergency department burdens, and serve as vital gateways into primary care and addiction treatment.",
        "incorrectExplanations": {
            "A": "There have been zero fatal overdoses inside sanctioned SCFs globally, and neighborhood discarded syringes decrease significantly.",
            "B": "SCFs are endorsed by international harm reduction bodies and operating successfully across Europe, Canada, Australia, and the US.",
            "C": "SCFs operate on voluntary engagement and low-threshold access, not mandatory detention."
        },
        "learningObjective": "Evaluate the clinical and community outcomes of Supervised Consumption Facilities (SCFs).",
        "reference": "Potier, C., et al. (2014). Supervised injection services: what does the literature tell us? A systematic review. Drug and Alcohol Dependence, 145, 48-68.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1298",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Intermediate",
        "questionText": "What is the primary objective of 'Good Samaritan' overdose legislation, and how does it support community naloxone distribution programs?",
        "options": [
            {"id": "A", "text": "It grants legal immunity from arrest or prosecution for minor drug possession to individuals who call emergency services or administer naloxone during an overdose emergency, removing the fear of police arrest that historically delayed 911 calls."},
            {"id": "B", "text": "It requires all citizens to carry naloxone under penalty of monetary fines."},
            {"id": "C", "text": "It allows police officers to search any person's home without a warrant if an overdose occurs."},
            {"id": "D", "text": "It provides free housing to anyone who witnesses an overdose."}
        ],
        "correctAnswer": "A",
        "explanation": "The primary barrier to calling emergency medical services during an overdose is fear of police arrival, arrest, and criminal prosecution for drug possession or probation violations. Good Samaritan laws provide statutory immunity from arrest or prosecution for minor possession charges to the caller and the overdose victim, encouraging timely emergency activation and saving lives.",
        "incorrectExplanations": {
            "B": "Good Samaritan laws provide legal protection, not mandatory possession penalties.",
            "C": "These laws restrict police prosecution to encourage emergency calls, rather than expanding warrantless searches.",
            "D": "The legislation provides legal immunity from drug charges, not housing entitlements."
        },
        "learningObjective": "Explain how Good Samaritan legislation facilitates timely emergency response and naloxone administration.",
        "reference": "Banta-Green, C. J., et al. (2013). Police officers’ and paramedics’ experiences with and perceptions of Washington State’s 911 Good Samaritan Drug Overdose Law. Drug and Alcohol Dependence, 132(3), 625-628.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1299",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Intermediate",
        "questionText": "Community drug checking services (such as spectrometer testing and fentanyl test strips) allow people who use drugs to analyze their substances before consumption. Which behavioral outcome has been documented when clients discover unexpected toxic adulterants (such as fentanyl or synthetic cathinones) in their drug supply?",
        "options": [
            {"id": "A", "text": "Clients immediately inject twice the amount to test their tolerance."},
            {"id": "B", "text": "Clients frequently discard the batch, use a smaller test dose ('tester shot'), use in the presence of a peer with naloxone, or choose not to consume the substance alone, significantly reducing overdose risk."},
            {"id": "C", "text": "Drug checking has zero impact on client consumption behavior."},
            {"id": "D", "text": "Clients become violent toward the healthcare testing personnel."}
        ],
        "correctAnswer": "B",
        "explanation": "Empirical studies on drug checking (e.g., using fentanyl test strips or FTIR spectroscopy) show that when individuals receive objective evidence of lethal adulteration (like unanticipated fentanyl in cocaine or ketamine), a substantial majority modify their behavior: they discard the substance, use smaller test quantities, snort rather than inject, or ensure a peer is present with naloxone.",
        "incorrectExplanations": {
            "A": "Clients do not intentionally double their dose when warned of lethal contamination.",
            "C": "Multiple peer-reviewed studies show significant positive behavioral risk modification following drug checking.",
            "D": "Drug checking programs build trust and collaboration between clinicians and people who use drugs."
        },
        "learningObjective": "Describe the behavioral and harm reduction impact of community drug checking and fentanyl test strip programs.",
        "reference": "Karamouzian, M., et al. (2018). Evaluation of a rapid drug checking service in a supervised injection facility. The Lancet Public Health, 3(10), e469-e470.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1300",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Advanced",
        "questionText": "In recent years, the veterinary non-opioid sedative xylazine ('tranq') has increasingly contaminated illicit fentanyl supplies. What distinct clinical manifestation and management challenge does xylazine toxicity present to psychiatric and emergency nurses?",
        "options": [
            {"id": "A", "text": "Severe hypertension and high fever that resolves completely with oral aspirin."},
            {"id": "B", "text": "Immediate manic psychosis that requires high-dose electroconvulsive therapy."},
            {"id": "C", "text": "Severe, deep necrotic skin ulcerations (often occurring away from injection sites), profound bradycardia, hypotension, and central nervous system sedation that does NOT directly reverse with naloxone (though naloxone must still be administered for the co-ingested opioid)."},
            {"id": "D", "text": "Sudden growth of hair and rapid weight gain without vital sign changes."}
        ],
        "correctAnswer": "C",
        "explanation": "Xylazine is a non-opioid alpha-2 adrenergic agonist used in veterinary medicine. When co-mingled with illicit fentanyl, it causes profound bradycardia, hypotension, hypothermia, and prolonged sedation. Because it is not an opioid, its sedative effects are refractory to naloxone (although naloxone must still be given to reverse fentanyl-induced respiratory arrest). Additionally, xylazine causes severe peripheral vasoconstriction resulting in extensive necrotic skin ulcerations.",
        "incorrectExplanations": {
            "A": "Xylazine causes profound hypotension and bradycardia, not hypertension, and does not respond to aspirin.",
            "B": "Xylazine causes heavy sedation and coma, not manic psychosis.",
            "D": "These are fictitious somatic complaints unrelated to xylazine toxicity."
        },
        "learningObjective": "Recognize the clinical presentation and nursing management of xylazine-adulterated opioid toxicity.",
        "reference": "Friedman, J., et al. (2022). Xylazine spreads across the US: a growing component of the increasingly synthetic and polysubstance overdose crisis. Drug and Alcohol Dependence, 233, 109380.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1301",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Advanced",
        "questionText": "Why is integrating sexual and reproductive health services—including Pre-Exposure Prophylaxis (PrEP) for HIV, barrier contraception, and routine STI screening—an indispensable component of harm reduction within psychiatric and addiction nursing?",
        "options": [
            {"id": "A", "text": "Because all clients who use substances are legally required to undergo fertility testing."},
            {"id": "B", "text": "Because psychotropic medications only work if the client is taking daily antiviral drugs."},
            {"id": "C", "text": "Because people who use drugs never engage in sexual activity."},
            {"id": "D", "text": "Because substance use (especially stimulants like methamphetamine and crack) is frequently linked with disinhibited sexual activity, sex work for survival, and shared biological transmission vectors, placing this population at elevated risk for HIV, syphilis, and unintended pregnancy."}
        ],
        "correctAnswer": "D",
        "explanation": "Substance use (particularly 'chemsex' or stimulant misuse with methamphetamine, cocaine, and alcohol) can lower inhibitions and increase high-risk sexual practices. Furthermore, economic marginalization may lead individuals to engage in transactional sex for survival or substances. Integrating sexual health (PrEP, condoms, STI screening, hepatitis vaccines, reproductive counseling) into addiction care addresses overlapping transmission vectors.",
        "incorrectExplanations": {
            "A": "Mandatory fertility testing is unethical and unconstitutional.",
            "B": "Psychotropics do not require concurrent antiviral medications to exert their pharmacological effects.",
            "C": "Assuming people who use substances are asexual ignores clinical reality and leaves sexual health unaddressed."
        },
        "learningObjective": "Explain the epidemiological rationale for embedding sexual and reproductive health interventions into harm reduction nursing care.",
        "reference": "Centers for Disease Control and Prevention (CDC). (2021). US Public Health Service: Preexposure prophylaxis for the prevention of HIV infection in the United States—2021 Update: A clinical practice guideline.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1302",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Advanced",
        "questionText": "Harm reduction programs distribute 'safer smoking kits' (containing Pyrex glass stems, heat-resistant silicone mouthpieces, and brass screens) to individuals who smoke crack cocaine or crystal methamphetamine. What is the evidence-based clinical rationale for this public health intervention?",
        "options": [
            {"id": "A", "text": "Preventing severe lip burns, cuts, and oral sores that serve as mucous membrane entry points and transmission vectors for Hepatitis C virus (HCV) and other bloodborne pathogens when sharing makeshift pipes (e.g., broken glass or aluminum cans)."},
            {"id": "B", "text": "Enhancing the euphoric potency of street stimulants by 300% to save money."},
            {"id": "C", "text": "Encouraging clients to switch from oral medications to smoking illicit stimulants."},
            {"id": "D", "text": "Eliminating all cardiovascular risks associated with cocaine misuse."}
        ],
        "correctAnswer": "A",
        "explanation": "Makeshift crack pipes (broken antennas, cans, jagged glass) cause severe lacerations, thermal burns, and bleeding blisters on the lips and oral mucosa. When individuals share pipes, blood from oral lesions transfers viral pathogens—most notably Hepatitis C virus (HCV), which remains viable in dried blood. Distributing heat-resistant Pyrex stems and personal mouthpieces prevents burns, cuts, and viral cross-transmission.",
        "incorrectExplanations": {
            "B": "Harm reduction kits minimize physical injury and infection, not enhance drug potency.",
            "C": "Kits aim to make existing smoking behaviors safer, not encourage new consumption routes.",
            "D": "Safer smoking kits prevent local mucosal injury and viral spread; they do not alter systemic adrenergic cardiovascular toxicity."
        },
        "learningObjective": "Explain how safer smoking kits prevent mucosal injury and Hepatitis C transmission among stimulant users.",
        "reference": "Malchy, L. A., et al. (2008). Do crack smoking materials promote safer behavior? A systematic review of safer crack kits. Harm Reduction Journal, 5(1), 1-8.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1303",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Advanced",
        "questionText": "In modern psychiatric nursing documentation and therapeutic communication, which linguistic adjustment exemplifies person-first, non-stigmatizing clinical language?",
        "options": [
            {"id": "A", "text": "Referring to the client as an 'addict' and recording that their urine test was 'dirty.'"},
            {"id": "B", "text": "Documenting that the client is 'a frequent flyer who is non-compliant and drug-seeking.'"},
            {"id": "C", "text": "Documenting that the client is a 'person with an opioid use disorder' and that their toxicology screen was 'positive for opioids.'"},
            {"id": "D", "text": "Referring to the client as an 'abuser' and noting that they are 'unmotivated.'"}
        ],
        "correctAnswer": "C",
        "explanation": "Language shapes clinical attitudes and perpetuates healthcare stigma. Person-first language (e.g., 'person with a substance use disorder' rather than 'addict' or 'abuser') emphasizes human dignity. Describing toxicology results factually (e.g., 'positive for opioid metabolites' rather than 'dirty', and 'negative' rather than 'clean') avoids framing medical tests in moralistic terms of purity versus contamination.",
        "incorrectExplanations": {
            "A": "Terms like 'addict' and 'dirty urine' are stigmatizing, moralistic, and dehumanizing.",
            "B": "'Frequent flyer' and 'drug-seeking' represent derogatory labeling that impairs care quality.",
            "D": "'Abuser' evokes punitive rather than medical responses and worsens provider bias."
        },
        "learningObjective": "Demonstrate the use of non-stigmatizing, person-first language in psychiatric nursing documentation and communication.",
        "reference": "Kelly, J. F., & Westerhoff, C. M. (2010). Does it hurt to refer to a person with a substance use disorder as a 'substance abuser'? A randomized trial. International Journal of Drug Policy, 21(3), 202-207.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1304",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Harm Reduction Principles",
        "difficulty": "Expert",
        "questionText": "A 54-year-old male with end-stage alcohol dependence and chronic homelessness has had 38 emergency department presentations in the past year for severe alcohol withdrawal, falls, and hypothermia. He has repeatedly consumed non-beverage alcohol (mouthwash and surgical spirits). Which innovative harm reduction program is specifically designed to stabilize such clients by providing scheduled, regulated administration of beverage alcohol in a supportive housing setting?",
        "options": [
            {"id": "A", "text": "Mandatory locked civil commitment detoxification"},
            {"id": "B", "text": "Aversion conditioning with emetic medications"},
            {"id": "C", "text": "Total isolation in solitary confinement"},
            {"id": "D", "text": "Managed Alcohol Programs (MAPs)"}
        ],
        "correctAnswer": "D",
        "explanation": "Managed Alcohol Programs (MAPs) are low-threshold harm reduction interventions for individuals with severe, chronic alcohol dependence and homelessness for whom abstinence-based treatments have repeatedly failed. In a MAP, measured doses of beverage alcohol (e.g., wine or beer) are administered at scheduled hourly intervals alongside meals, housing, and nursing care. MAPs dramatically reduce non-beverage alcohol ingestion, emergency visits, police contacts, and head trauma.",
        "incorrectExplanations": {
            "A": "Involuntary locked commitment does not solve chronic addiction and leads to immediate post-discharge relapse.",
            "B": "Aversive emetics are outdated, dangerous, and lack long-term efficacy in end-stage dependence.",
            "C": "Solitary confinement is punitive, unethical, and medically unsafe for severe alcohol dependence."
        },
        "learningObjective": "Evaluate the clinical evidence and harm reduction rationale for Managed Alcohol Programs (MAPs).",
        "reference": "Stockwell, T., et al. (2018). Impact of managed alcohol programs on alcohol-related harm: a prospective cohort study. Canadian Medical Association Journal (CMAJ), 190(6), E157-E163.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # ---------------------------------------------------------
    # Topic 10: Relapse Prevention (MHN-Q1305 to MHN-Q1314)
    # ---------------------------------------------------------
    {
        "id": "MHN-Q1305",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Foundation",
        "questionText": "In G. Alan Marlatt's Cognitive-Behavioral Model of Relapse Prevention, what is the crucial conceptual distinction between a 'lapse' (or 'slip') and a 'relapse'?",
        "options": [
            {"id": "A", "text": "A 'lapse' is an initial, single violation of a self-imposed abstinence rule, whereas a 'relapse' is a complete return to the continuous, compulsive pre-treatment baseline pattern of substance misuse."},
            {"id": "B", "text": "A 'lapse' only occurs with illicit drugs, while a 'relapse' only occurs with alcohol."},
            {"id": "C", "text": "A 'lapse' means the client is cured, while a 'relapse' means they require permanent institutionalization."},
            {"id": "D", "text": "There is no distinction; any single sip or puff constitutes an immediate total clinical relapse."}
        ],
        "correctAnswer": "A",
        "explanation": "Marlatt and Gordon's model makes an essential clinical distinction between a lapse and a relapse. A 'lapse' (slip) is an initial, discrete event involving substance use after a period of abstinence. A 'relapse' is an escalating, progressive reinstatement of the previous addictive baseline pattern. Distinguishing between the two allows the nurse and client to intervene immediately after a lapse to prevent it from snowballing into a full relapse.",
        "incorrectExplanations": {
            "B": "Lapses and relapses occur across all substances (alcohol, nicotine, opioids, stimulants).",
            "C": "A lapse is not a cure, nor does a relapse imply permanent institutionalization.",
            "D": "Equating a single slip with total failure triggers the Abstinence Violation Effect, worsening outcomes."
        },
        "learningObjective": "Differentiate a 'lapse' from a 'relapse' in cognitive-behavioral relapse prevention theory.",
        "reference": "Marlatt, G. A., & Gordon, J. R. (Eds.). (1985). Relapse Prevention: Maintenance Strategies in the Treatment of Addictive Behaviors. Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1306",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Foundation",
        "questionText": "According to Marlatt's empirical research on High-Risk Situations (HRS) triggering substance use lapses, which category of triggers accounts for the highest proportion of initial relapse episodes across clinical populations?",
        "options": [
            {"id": "A", "text": "Sudden genetic mutations occurring overnight"},
            {"id": "B", "text": "Negative emotional states (e.g., anger, anxiety, depression, boredom, or loneliness)"},
            {"id": "C", "text": "Accidental ingestion of contaminated drinking water"},
            {"id": "D", "text": "Winning large amounts of money in lotteries"}
        ],
        "correctAnswer": "B",
        "explanation": "In Marlatt's taxonomy of relapse determinants, intrapersonal factors account for over half of all initial lapses, with 'Negative Emotional States' (frustration, anger, anxiety, depression, loneliness, boredom) being the single most common category (accounting for approximately 35–40% of lapses). Interpersonal conflict and social pressure constitute the other major high-risk categories.",
        "incorrectExplanations": {
            "A": "Relapse triggers are psychological, neurobehavioral, and environmental, not overnight genetic mutations.",
            "C": "Drinking water contamination is not an established substance relapse trigger.",
            "D": "Positive emotional states can trigger lapses, but negative emotional states account for far more episodes."
        },
        "learningObjective": "Identify negative emotional states as the primary intrapersonal high-risk determinant of substance relapse.",
        "reference": "Witkiewitz, K., & Marlatt, G. A. (2004). Relapse prevention for alcohol and drug problems: that was Zen, this is Tao. American Psychologist, 59(4), 224-235.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1307",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Intermediate",
        "questionText": "A client who had been abstinent from alcohol for 6 months drinks a single glass of beer at an anniversary dinner. Immediately afterward, he thinks: 'I've completely ruined my recovery. I'm a hopeless addict with zero willpower. I might as well finish the entire bottle and get smashed.' He then binges heavily. Which cognitive-behavioral phenomenon has this client experienced?",
        "options": [
            {"id": "A", "text": "Malingering for secondary gain"},
            {"id": "B", "text": "Substance-induced korsakoff confabulation"},
            {"id": "C", "text": "The Abstinence Violation Effect (AVE)"},
            {"id": "D", "text": "Retrograde psychogenic fugue"}
        ],
        "correctAnswer": "C",
        "explanation": "The Abstinence Violation Effect (AVE) consists of two interrelated components that occur following a lapse: (1) cognitive dissonance (conflict between the self-concept of being an abstinent person and the reality of having consumed the substance) and (2) internal, stable, global attributions of personal failure ('I have no willpower, I am a failure, I cannot succeed'). The resulting shame, guilt, and hopelessness propel the individual to escalate the lapse into a full relapse.",
        "incorrectExplanations": {
            "A": "The AVE is an internal cognitive-affective distress reaction, not deliberate deceit for secondary gain.",
            "B": "Confabulation involves memory retrieval deficits, not catastrophic cognitive distortion after a lapse.",
            "D": "Psychogenic fugue is a dissociative amnesia characterized by unexpected travel, unrelated to this scenario."
        },
        "learningObjective": "Explain the psychological mechanisms comprising the Abstinence Violation Effect (AVE).",
        "reference": "Marlatt, G. A., & Donovan, D. M. (Eds.). (2005). Relapse Prevention: Maintenance Strategies in the Treatment of Addictive Behaviors (2nd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1308",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Intermediate",
        "questionText": "When working with a client who has just experienced an initial substance lapse, how should the psychiatric nurse apply cognitive restructuring to neutralize the Abstinence Violation Effect?",
        "options": [
            {"id": "A", "text": "Agree with the client that they have failed completely and suggest they start treatment again from scratch next year."},
            {"id": "B", "text": "Require the client to wear a sign around their neck stating they violated their abstinence rule."},
            {"id": "C", "text": "Report the lapse to the client's employer immediately."},
            {"id": "D", "text": "Re-frame the lapse not as a catastrophic moral failure or evidence of hopelessness, but as a temporary, valuable learning event and feedback error that highlights specific trigger situations and coping skill deficits to be addressed."}
        ],
        "correctAnswer": "D",
        "explanation": "To defuse the Abstinence Violation Effect, the nurse helps the client attribute the lapse to external, unstable, and controllable factors (e.g., 'I was exhausted, in a high-risk environment, and didn't use my assertive refusal skills') rather than internal, unchangeable flaws ('I am a defective addict'). Re-framing the slip as a learning experience preserves self-efficacy and stops escalation into full relapse.",
        "incorrectExplanations": {
            "A": "Validating catastrophizing reinforces hopelessness and guarantees progression to a full relapse.",
            "B": "Shaming and punitive humiliation increase guilt and drive further substance use.",
            "C": "Breaching confidentiality damages the therapeutic relationship and violates ethics."
        },
        "learningObjective": "Apply cognitive restructuring to mitigate the Abstinence Violation Effect and restore client self-efficacy.",
        "reference": "Larimer, M. E., Palmer, R. S., & Marlatt, G. A. (1999). Relapse prevention: an overview of Marlatt's cognitive-behavioral model. Alcohol Research & Health, 23(2), 151-160.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1309",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Intermediate",
        "questionText": "In Marlatt's cognitive-behavioral model, what are 'Apparently Irrelevant Decisions' (AIDs)?",
        "options": [
            {"id": "A", "text": "Subtle, seemingly innocuous micro-decisions and choices that seem unrelated to substance use on the surface, but cumulatively and covertly position the individual directly into a high-risk situation where resistance is nearly impossible."},
            {"id": "B", "text": "Court rulings made by judges regarding patient custody."},
            {"id": "C", "text": "Decisions regarding which brand of toothpaste to purchase."},
            {"id": "D", "text": "Formal written contracts signed between a nurse and physician."}
        ],
        "correctAnswer": "A",
        "explanation": "Apparently Irrelevant Decisions (AIDs) are covert, subconscious behavioral choices that appear harmless or rationalized (e.g., deciding to take a scenic walk that happens to pass one's former dealer's house, or keeping a bottle of spirits at home 'in case unexpected dinner guests drop by'). By making a chain of AIDs, the individual constructs a high-risk trap while maintaining the illusion of having no intention to use.",
        "incorrectExplanations": {
            "B": "AIDs are client psychological behavioral micro-decisions, not legal court judgments.",
            "C": "Toothpaste choices are trivial daily decisions, not the clinical concept of AIDs in addiction.",
            "D": "AIDs are behavioral choices, not administrative nursing contracts."
        },
        "learningObjective": "Identify and analyze Apparently Irrelevant Decisions (AIDs) that lead to high-risk relapse environments.",
        "reference": "Marlatt, G. A., & Gordon, J. R. (Eds.). (1985). Relapse Prevention: Maintenance Strategies in the Treatment of Addictive Behaviors. Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1310",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Advanced",
        "questionText": "The mindfulness-based relapse prevention technique known as 'Urge Surfing' (developed by Alan Marlatt) teaches clients to manage intense cravings by conceptualizing urges in what way?",
        "options": [
            {"id": "A", "text": "As permanent tsunamis that can only be survived by consuming the substance immediately."},
            {"id": "B", "text": "As ocean waves that gradually build up, crest, peak in intensity over 15 to 30 minutes, and naturally subside, which the client can mindfully 'ride out' using breath awareness without fighting or giving in to them."},
            {"id": "C", "text": "As physical sports activities requiring immediate purchase of a surfboard."},
            {"id": "D", "text": "As signs of demonic possession that require exorcism rituals."}
        ],
        "correctAnswer": "B",
        "explanation": "Urge Surfing is a mindfulness technique where clients observe their craving sensations with detached curiosity, like a surfer riding an ocean wave. Clients learn that cravings do not escalate indefinitely; rather, like waves, they rise, peak in intensity (usually lasting 15–30 minutes), and naturally subside. Fighting the craving causes distress, while surfing it with somatic awareness allows it to wash over without relapsing.",
        "incorrectExplanations": {
            "A": "Believing cravings are permanent tsunamis increases helplessness and promotes immediate giving in.",
            "C": "Urge surfing is a psychological mindfulness metaphor, not athletic surfing.",
            "D": "Urge surfing is an evidence-based cognitive-behavioral practice, not a supernatural concept."
        },
        "learningObjective": "Instruct clients in the mindfulness-based relapse prevention technique of Urge Surfing.",
        "reference": "Bowen, S., Chawla, N., & Marlatt, G. A. (2010). Mindfulness-Based Relapse Prevention for Addictive Behaviors: A Clinician's Guide. Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1311",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Advanced",
        "questionText": "In behavioral coping skills training for relapse prevention, what are the key non-verbal and verbal components of an effective 'Assertive Drug Refusal' skill when offered substances in a social pressure situation?",
        "options": [
            {"id": "A", "text": "Looking down at the floor, apologizing profusely, and giving a 10-minute elaborate excuse about why one's liver enzymes are elevated."},
            {"id": "B", "text": "Aggressively punching the person who offered the drink in the jaw."},
            {"id": "C", "text": "Maintaining direct eye contact, standing with upright confident posture, delivering a clear and unambiguous 'No' (e.g., 'No, thanks, I don't drink anymore'), suggesting an alternative activity or non-alcoholic beverage, and changing the subject without over-apologizing."},
            {"id": "D", "text": "Accepting the drink and secretly pouring it into a nearby potted plant."}
        ],
        "correctAnswer": "C",
        "explanation": "Effective assertive refusal involves both verbal and non-verbal assertiveness: clear eye contact, erect posture, a firm calm voice, an immediate concise refusal ('No, thank you, I've quit drinking'), and changing the topic or suggesting an alternative. Hesitation, looking away, over-apologizing, or giving lengthy excuses signals ambivalence to peers, inviting continued pressure.",
        "incorrectExplanations": {
            "A": "Looking away and over-apologizing conveys weakness and ambivalence, encouraging peers to insist.",
            "B": "Physical violence is maladaptive, illegal, and causes legal and personal harm.",
            "D": "Holding the beverage creates proximity to temptation and invites discovery or accidental drinking."
        },
        "learningObjective": "Demonstrate behavioral role-play and coaching of assertive substance refusal skills.",
        "reference": "Monti, P. M., et al. (2002). Coping and Social Skills Training for Alcohol-Dependent Patients (2nd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1312",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Advanced",
        "questionText": "Which elements are essential in a client's written Relapse Prevention Action Plan (Emergency Crisis Card) to maximize its utility during an acute craving crisis or immediately following a lapse?",
        "options": [
            {"id": "A", "text": "A list of the client's past crimes and a signed agreement to pay the hospital 1,000 dollars if they drink."},
            {"id": "B", "text": "The phone numbers of three local bars and liquor stores."},
            {"id": "C", "text": "An essay on the chemistry of fermentation written in Latin."},
            {"id": "D", "text": "Personalized early idiosyncratic warning signs, specific high-risk triggers, concrete distraction techniques, contact numbers of three trusted recovery supports/peers, and explicit emergency steps to take within 60 minutes of a slip."}
        ],
        "correctAnswer": "D",
        "explanation": "A high-quality Relapse Prevention Plan is concise, actionable, and personalized. It identifies idiosyncratic early warning signs (subtle changes in thinking, sleep, or mood), explicit triggers, instant coping mechanisms (e.g., leaving the premises, 15-minute delay), contact details for immediate sober support (peer sponsor, recovery coach, crisis line), and emergency steps to take if a slip occurs to stop escalation.",
        "incorrectExplanations": {
            "A": "Past crime listings and monetary penalties induce shame, compounding relapse risk.",
            "B": "Listing bars provides cues that facilitate substance access.",
            "C": "Theoretical essays in Latin are useless in an acute behavioral crisis."
        },
        "learningObjective": "Construct a comprehensive, actionable Relapse Prevention Action Plan for clinical practice.",
        "reference": "Daley, D. C., & Marlatt, G. A. (2006). Overcoming Your Alcohol or Drug Problem: Effective Recovery Strategies (Client Workbook). Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1313",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Advanced",
        "questionText": "When comparing mutual-aid recovery support groups, how does the underlying philosophy of SMART Recovery (Self-Management and Recovery Training) fundamentally differ from traditional 12-Step programs like Alcoholics Anonymous (AA)?",
        "options": [
            {"id": "A", "text": "SMART Recovery is a secular, science-based program utilizing Cognitive Behavioural Therapy (CBT) and Rational Emotive Behaviour Therapy (REBT) principles that emphasize self-empowerment and personal choice, whereas 12-Step programs utilize a spiritual framework emphasizing surrender to a Higher Power and accepting powerlessness over addiction."},
            {"id": "B", "text": "SMART Recovery requires members to consume alcohol at every meeting, whereas AA strictly forbids it."},
            {"id": "C", "text": "AA is only for individuals with university degrees, whereas SMART Recovery is for adolescents only."},
            {"id": "D", "text": "SMART Recovery is led exclusively by police officers and probation departments."}
        ],
        "correctAnswer": "A",
        "explanation": "12-Step groups (AA/NA) are rooted in a spiritual framework where individuals admit powerlessness over their addiction and rely on a Higher Power and peer fellowship for recovery. In contrast, SMART Recovery is a secular, evidence-based mutual-aid group based on REBT and CBT (focusing on building motivation, coping with urges, problem-solving, and lifestyle balance), emphasizing personal self-empowerment and internal locus of control.",
        "incorrectExplanations": {
            "B": "Neither program involves consuming alcohol; both support recovery.",
            "C": "Both AA and SMART Recovery are open to all individuals struggling with addictive behaviors regardless of education.",
            "D": "SMART Recovery is a peer-led community group, not a law enforcement program."
        },
        "learningObjective": "Contrast the theoretical frameworks of 12-Step mutual-aid groups with SMART Recovery.",
        "reference": "Horvath, A. T., & Yeterian, J. (2012). SMART Recovery: self-management and recovery training. In Mutual Aid for Addictive Behaviors (pp. 87-104).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1314",
        "module": "13. Substance Use Disorders and Dual Diagnosis",
        "topic": "Relapse Prevention",
        "difficulty": "Expert",
        "questionText": "In contemporary recovery research (Granfield and Cloud), what is 'Recovery Capital,' and why is its systematic nursing assessment essential in long-term relapse prevention planning?",
        "options": [
            {"id": "A", "text": "The monetary value of real estate owned by private rehabilitation clinics."},
            {"id": "B", "text": "The cumulative sum of internal and external resources (personal, social, physical, human, and community capital) that an individual can mobilize to initiate and sustain recovery from substance use disorders."},
            {"id": "C", "text": "The amount of gold bullion held in national bank reserves to fund psychiatric hospitals."},
            {"id": "D", "text": "The total number of milligrams of psychotropic medication a client has ingested in their lifetime."}
        ],
        "correctAnswer": "B",
        "explanation": "Recovery Capital (Cloud & Granfield) encompasses the breadth of resources required to maintain long-term recovery: Human Capital (skills, health, coping strategies, education), Social Capital (supportive family, sober social networks), Physical Capital (financial assets, secure housing, food security), and Community Capital (accessible healthcare, recovery community organizations, peer groups). Relapse risk is strongly dictated by the depth of an individual's recovery capital.",
        "incorrectExplanations": {
            "A": "Recovery capital refers to client resources, not commercial real estate.",
            "C": "National gold reserves have no bearing on individual recovery capital.",
            "D": "Cumulative medication exposure is not the definition of recovery capital."
        },
        "learningObjective": "Assess and build multi-dimensional Recovery Capital to promote sustained substance use recovery.",
        "reference": "Granfield, R., & Cloud, W. (2001). Social context and natural recovery: the role of social capital in the resolution of drug-associated problems. Substance Use & Misuse, 36(11), 1543-1570.",
        "contentReviewStatus": "Peer Reviewed"
    }
]
