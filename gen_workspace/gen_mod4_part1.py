# gen_workspace/gen_mod4_part1.py
"""
Module 4 Part 1: Topics 1 to 5 (Q315 - Q364, 50 questions)
Module: "4. Psychopharmacology and Medication Management"
"""

MOD4_P1 = [
    # -------------------------------------------------------------
    # Topic 1: First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms (Q315 - Q324)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q315",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Foundation",
        "questionText": "What is the primary neuropharmacological mechanism of action by which first-generation (typical) antipsychotics, such as haloperidol, exert their therapeutic antipsychotic effects?",
        "options": [
            {"id": "A", "text": "Competitive antagonism of post-synaptic dopamine D2 receptors in the mesolimbic pathway"},
            {"id": "B", "text": "Selective inhibition of the presynaptic serotonin transporter (SERT) in the dorsal raphe nucleus"},
            {"id": "C", "text": "Positive allosteric modulation of GABA-A receptor chloride channels in the cerebellum"},
            {"id": "D", "text": "Direct stimulation of postsynaptic alpha-1 adrenergic receptors in the locus coeruleus"}
        ],
        "correctAnswer": "A",
        "explanation": "First-generation antipsychotics (FGAs) exert their therapeutic antipsychotic efficacy predominantly by competitive antagonism (blockade) of dopamine D2 receptors in the mesolimbic pathway, thereby dampening hyperactive dopaminergic signaling responsible for positive psychotic symptoms.",
        "incorrectExplanations": {
            "A": "D2 receptor blockade in the mesolimbic pathway mediates the therapeutic reduction of positive psychotic symptoms.",
            "B": "Inhibition of SERT is the mechanism of SSRI antidepressants, not typical antipsychotics.",
            "C": "Positive allosteric modulation of GABA-A is the mechanism of benzodiazepines and barbiturates.",
            "D": "Typical antipsychotics block (antagonize) alpha-1 receptors, causing orthostatic hypotension, rather than stimulating them."
        },
        "learningObjective": "Explain the therapeutic mechanism of action of first-generation antipsychotics in the mesolimbic pathway.",
        "reference": "Taylor, D. M., Barnes, T. R., & Young, A. H. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q316",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Foundation",
        "questionText": "Thirty-six hours after receiving a second dose of intramuscular haloperidol 5 mg, a 22-year-old male develops sudden, painful spastic contraction of the neck muscles forcing the head sideways (acute torticollis) and sustained upward deviation of the eyes. What acute extrapyramidal emergency is this, and what is the immediate first-line nursing intervention?",
        "options": [
            {"id": "A", "text": "Akathisia; administer oral propranolol 10 mg"},
            {"id": "B", "text": "Acute Dystonic Reaction (torticollis and oculogyric crisis); administer parenteral anticholinergic medication (e.g., IM/IV benztropine or procyclidine) immediately"},
            {"id": "C", "text": "Tardive Dyskinesia; stop all medications and start oral levodopa"},
            {"id": "D", "text": "Neuroleptic Malignant Syndrome; apply ice packs and prepare dantrolene infusion"}
        ],
        "correctAnswer": "B",
        "explanation": "An acute dystonic reaction involves sudden, involuntary, painful sustained contractions of muscle groups (such as torticollis, retrocollis, trismus, or oculogyric crisis). It typically occurs within 24 to 72 hours of initiating or increasing high-potency FGAs, particularly in young males. It constitutes a medical emergency (risk of laryngeal dystonia) and is treated rapidly with parenteral anticholinergics (IM/IV benztropine 1-2 mg or procyclidine 5-10 mg).",
        "incorrectExplanations": {
            "A": "Akathisia causes motor restlessness and inner urge to move, not sustained spastic muscle contractions.",
            "B": "Acute dystonia requires immediate administration of parenteral anticholinergics to reverse muscle spasm.",
            "C": "Tardive dyskinesia develops after months/years of exposure, and levodopa can trigger florid psychosis.",
            "D": "NMS presents with hyperthermia, lead-pipe rigidity, autonomic instability, and altered mental status, not isolated focal dystonia."
        },
        "learningObjective": "Recognize and promptly manage acute dystonic reactions secondary to high-potency FGAs.",
        "reference": "Taylor, D. M., et al. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q317",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Intermediate",
        "questionText": "A patient commenced on fluphenazine describes an unbearable internal sense of tension and a compelling drive to keep moving, continuously pacing the corridor, shifting weight from foot to foot when standing, and unable to remain seated for more than 30 seconds. The nurse recognizes this symptom as akathisia. Which intervention represents first-line evidence-based pharmacologic management?",
        "options": [
            {"id": "A", "text": "Increase the fluphenazine dose to suppress psychotic restlessness"},
            {"id": "B", "text": "Administer high-dose oral vitamin C and restrict caffeine"},
            {"id": "C", "text": "Reduce the antipsychotic dose if clinically feasible and initiate a beta-blocker (e.g., propranolol) or a low-dose benzodiazepine"},
            {"id": "D", "text": "Commence immediate dopamine depletion therapy with tetrabenazine"}
        ],
        "correctAnswer": "C",
        "explanation": "Akathisia is characterized by subjective inner restlessness and objective motor agitation (pacing, rocking, foot tapping). It is often misdiagnosed as psychotic worsening. First-line management includes reducing the antipsychotic dosage if feasible, switching to an antipsychotic with lower EPS propensity, or initiating a centrally active beta-blocker such as propranolol (30-80 mg/day) or a short-term low-dose benzodiazepine (e.g., lorazepam/clonazepam).",
        "incorrectExplanations": {
            "A": "Increasing the antipsychotic dose will dramatically worsen akathisia and can provoke suicidal agitation.",
            "B": "Vitamin C has no demonstrated efficacy in treating antipsychotic-induced akathisia.",
            "C": "Beta-blockers (propranolol) and dosage reduction are the established first-line treatments for akathisia.",
            "D": "Tetrabenazine depletes dopamine and can precipitate or worsen akathisia and depression."
        },
        "learningObjective": "Differentiate akathisia from psychotic agitation and implement first-line management strategies.",
        "reference": "Barnes, T. R. (2003). The Barnes Akathisia Rating Scale—revisited. Journal of Psychopharmacology, 17(4), 365-370.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q318",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Intermediate",
        "questionText": "A 58-year-old inpatient with chronic schizophrenia receiving haloperidol 10 mg daily exhibits marked bradykinesia, generalized cogwheel rigidity, masked facial expression (hypomimia), excessive drooling, and a short, shuffling, festinating gait. What is the pharmacological basis of this pseudoparkinsonism, and how should it be managed?",
        "options": [
            {"id": "A", "text": "Serotonin excess in the locus coeruleus; treat with cyproheptadine"},
            {"id": "B", "text": "GABA deficiency in the substantia nigra; treat with sodium valproate"},
            {"id": "C", "text": "Glutamate excitotoxicity in the hippocampus; treat with memantine"},
            {"id": "D", "text": "D2 receptor blockade in the nigrostriatal pathway creating a relative excess of acetylcholine; treat by lowering the dose or adding an anticholinergic agent (e.g., procyclidine)"}
        ],
        "correctAnswer": "D",
        "explanation": "Antipsychotic-induced pseudoparkinsonism results from blockade of dopamine D2 receptors in the nigrostriatal pathway. In the basal ganglia, dopamine normally exerts an inhibitory tone on cholinergic interneurons; D2 antagonism removes this inhibition, resulting in cholinergic hyperactivation. Management involves reducing the antipsychotic dose, switching to an SGA, or adding an anticholinergic antiparkinsonian drug (e.g., procyclidine, trihexyphenidyl).",
        "incorrectExplanations": {
            "A": "Serotonin excess causes serotonin syndrome, not extrapyramidal pseudoparkinsonism.",
            "B": "GABA deficiency is not the underlying pathophysiological mechanism of parkinsonian rigidity.",
            "C": "Glutamate excitotoxicity does not account for acute/subacute nigrostriatal D2 motor blockade.",
            "D": "D2 blockade in the nigrostriatal tract leads to relative cholinergic overactivity, reversible by anticholinergics or dose reduction."
        },
        "learningObjective": "Explain the nigrostriatal dopamine-acetylcholine imbalance in pseudoparkinsonism and outline appropriate nursing and pharmacological interventions.",
        "reference": "Stahl, S. M. (2021). Stahl's Essential Psychopharmacology (5th ed.). Cambridge University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q319",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Foundation",
        "questionText": "How do low-potency first-generation antipsychotics (e.g., chlorpromazine) differ in their side-effect profile from high-potency first-generation antipsychotics (e.g., haloperidol)?",
        "options": [
            {"id": "A", "text": "Low-potency FGAs have lower affinity for D2 receptors, resulting in lower EPS risk, but have higher affinity for H1, alpha-1, and M1 receptors, causing greater sedation, orthostatic hypotension, and anticholinergic effects"},
            {"id": "B", "text": "Low-potency FGAs cause significantly higher rates of acute dystonia and oculogyric crises than high-potency FGAs"},
            {"id": "C", "text": "Low-potency FGAs produce zero sedation and stimulate appetite without affecting blood pressure"},
            {"id": "D", "text": "High-potency FGAs cause profound orthostatic hypotension and anticholinergic dry mouth, with negligible motor rigidity"}
        ],
        "correctAnswer": "A",
        "explanation": "High-potency FGAs (haloperidol, fluphenazine) bind selectively and strongly to D2 receptors, causing high rates of extrapyramidal side effects (EPS) but minimal sedation, anticholinergic effects, or hypotension. Low-potency FGAs (chlorpromazine, thioridazine) require higher milligram doses and broadly block histaminergic H1 (heavy sedation), alpha-1 adrenergic (orthostatic hypotension), and muscarinic M1 (anticholinergic) receptors, with lower EPS rates.",
        "incorrectExplanations": {
            "A": "Low-potency FGAs produce lower EPS but greater sedation, orthostasis, and anticholinergic burden.",
            "B": "Acute dystonias are far more common with high-potency FGAs like haloperidol.",
            "C": "Low-potency FGAs are profoundly sedating due to potent H1 receptor blockade.",
            "D": "High-potency FGAs have low anticholinergic and alpha-1 affinity, meaning they cause minimal hypotension but high motor rigidity."
        },
        "learningObjective": "Compare and contrast the adverse effect profiles of high-potency versus low-potency first-generation antipsychotics.",
        "reference": "Haddad, P. M., & Dursun, S. M. (2008). Neurological complications of psychiatric drugs: clinical features and management. Human Psychopharmacology: Clinical and Experimental, 23(S1), 15-26.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q320",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Intermediate",
        "questionText": "An elderly patient who has received depot fluphenazine decanoate for 15 years presents with involuntary, choreoathetoid movements of the tongue, lip smacking, puckering, and grimacing. The movements persist during sleep and worsen when the patient is distracted. What condition is this, and what is its proposed pathophysiological mechanism?",
        "options": [
            {"id": "A", "text": "Huntington's disease; autosomal dominant CAG triplet repeat expansion"},
            {"id": "B", "text": "Tardive Dyskinesia; postsynaptic dopamine D2 receptor upregulation and supersensitivity in the nigrostriatal pathway following prolonged receptor blockade"},
            {"id": "C", "text": "Acute akathisia; peripheral adrenergic hyperstimulation of striated skeletal motor units"},
            {"id": "D", "text": "Sydenham's chorea; autoimmune cross-reactivity following Group A streptococcal infection"}
        ],
        "correctAnswer": "B",
        "explanation": "Tardive Dyskinesia (TD) is a potentially irreversible movement disorder developing after prolonged exposure (typically months or years) to dopamine receptor blocking agents. The leading pathophysiological hypothesis is that chronic continuous D2 antagonism induces compensatory proliferation (upregulation) and neurochemical supersensitivity of postsynaptic D2 receptors in the nigrostriatal pathway.",
        "incorrectExplanations": {
            "A": "Huntington's chorea is a genetic neurodegenerative disorder, whereas this is medication-induced tardive movement.",
            "B": "Tardive dyskinesia results from chronic D2 blockade causing dopamine receptor supersensitivity and upregulation.",
            "C": "Akathisia presents as a subjective urge to move, not involuntary choreiform orofacial movements.",
            "D": "Sydenham's chorea is a pediatric post-streptococcal autoimmune condition, not a chronic iatrogenic complication in older adults."
        },
        "learningObjective": "Explain the clinical features and dopamine supersensitivity hypothesis of Tardive Dyskinesia.",
        "reference": "Correll, C. U., et al. (2017). Recognizing and treating tardive dyskinesia. Journal of Clinical Psychiatry, 78(1), e03.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q321",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Advanced",
        "questionText": "A mental health nurse conducts a routine quarterly screening using the Abnormal Involuntary Movement Scale (AIMS). During the physical examination protocol, why is the patient instructed to tap their thumb to each finger rapidly or walk across the room?",
        "options": [
            {"id": "A", "text": "To test for peripheral diabetic neuropathy and vibratory sense loss"},
            {"id": "B", "text": "To measure cerebellar balance and exclude alcohol intoxication"},
            {"id": "C", "text": "As an activation maneuver to unmask or accentuate subtle orofacial and extremity movements that may not be apparent at rest"},
            {"id": "D", "text": "To exhaust striated muscle fibers and determine fatigability in myasthenia gravis"}
        ],
        "correctAnswer": "C",
        "explanation": "In the standardized AIMS examination protocol, activation procedures (such as rapidly tapping the thumb with each finger, counting backwards, or walking across the room) are deliberate stress/distraction tasks. Activating one motor circuit unmasks or accentuates latent, subtle choreoathetoid involuntary movements in other muscle groups (such as the tongue, jaw, or trunk).",
        "incorrectExplanations": {
            "A": "AIMS screens for extrapyramidal involuntary movements, not diabetic peripheral sensory neuropathy.",
            "B": "AIMS is not a test for acute alcohol intoxication.",
            "C": "Activation maneuvers in AIMS bring out hidden or subtle dyskinetic movements through motor distraction.",
            "D": "AIMS does not measure fatigability for myasthenia gravis."
        },
        "learningObjective": "Demonstrate understanding of the administration protocol and activation maneuvers of the Abnormal Involuntary Movement Scale (AIMS).",
        "reference": "Guy, W. (1976). ECDEU Assessment Manual for Psychopharmacology (DHEW Publication No. ADM 76-338). National Institute of Mental Health.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q322",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Advanced",
        "questionText": "When managing confirmed, distressing Tardive Dyskinesia in a patient stabilized on antipsychotic therapy, what is the current evidence-based pharmacological guideline recommendation, and why are anticholinergic medications contraindicated?",
        "options": [
            {"id": "A", "text": "Prescribe high-dose procyclidine; anticholinergics directly regenerate damaged striatal GABA interneurons"},
            {"id": "B", "text": "Administer intramuscular fluphenazine boluses; higher D2 occupancy stops dyskinetic movements permanently"},
            {"id": "C", "text": "Initiate high-dose haloperidol to mask the movements indefinitely"},
            {"id": "D", "text": "Initiate an approved Vesicular Monoamine Transporter 2 (VMAT2) inhibitor (e.g., valbenazine or deutetrabenazine); anticholinergics must be avoided or withdrawn because they worsen TD movements"}
        ],
        "correctAnswer": "D",
        "explanation": "VMAT2 inhibitors (valbenazine, deutetrabenazine) selectively inhibit vesicular monoamine transporter 2, reducing presynaptic packaging and release of dopamine, and are the first-line FDA-approved treatments for TD. Crucially, anticholinergic medications (e.g., benztropine, procyclidine), while useful in acute dystonia and parkinsonism, worsen tardive dyskinesia by further tilting the striatal dopamine-acetylcholine balance toward dopaminergic excess.",
        "incorrectExplanations": {
            "A": "Anticholinergics consistently exacerbate and worsen tardive dyskinesia movements.",
            "B": "Escalating FGA doses provides temporary masking but accelerates the underlying striatal neurotoxicity and receptor supersensitivity.",
            "C": "Masking TD with haloperidol leads to severe, irreversible rebound dyskinesia upon any future dose change.",
            "D": "VMAT2 inhibitors are the established first-line evidence-based pharmacotherapy; anticholinergics exacerbate TD."
        },
        "learningObjective": "Evaluate modern therapeutic management of Tardive Dyskinesia, including VMAT2 inhibitors and the hazard of anticholinergic exacerbation.",
        "reference": "Bhidayasiri, R., et al. (2018). Update on tardive dyskinesia: recommendations from the American Academy of Neurology. Neurology, 81(5), 463-473.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q323",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Advanced",
        "questionText": "A 26-year-old female receiving haloperidol for 6 months presents with galactorrhea, secondary amenorrhea, loss of libido, and acne. Serum prolactin is elevated at 2,400 mIU/L (normal < 500 mIU/L). Which dopaminergic tract is responsible for this endocrine adverse effect, and what long-term health risk does chronic hyperprolactinemia pose?",
        "options": [
            {"id": "A", "text": "Tuberoinfundibular pathway; chronic hypogonadism leads to accelerated bone mineral density loss and osteoporosis"},
            {"id": "B", "text": "Mesocortical pathway; causes severe hepatic encephalopathy"},
            {"id": "C", "text": "Nigrostriatal pathway; causes severe vascular calcification and stroke"},
            {"id": "D", "text": "Mesolimbic pathway; causes secondary adrenal insufficiency and Addison's disease"}
        ],
        "correctAnswer": "A",
        "explanation": "Dopamine released from the hypothalamus travels through the tuberoinfundibular pathway to anterior pituitary lactotrophs, where it tonic-inhibits prolactin release. Antipsychotic D2 blockade in this pathway disinhibits prolactin secretion, leading to hyperprolactinemia (galactorrhea, amenorrhea, sexual dysfunction). Long-term hypogonadism (suppressed estrogen/testosterone) significantly accelerates bone mineral demineralization, causing osteopenia and osteoporosis.",
        "incorrectExplanations": {
            "A": "The tuberoinfundibular pathway regulates prolactin; chronic suppression of sex hormones causes osteoporosis.",
            "B": "The mesocortical pathway projects to prefrontal cortex and mediates cognition, not pituitary prolactin.",
            "C": "The nigrostriatal pathway mediates motor control (EPS), not pituitary hormone regulation.",
            "D": "The mesolimbic pathway mediates reward and psychosis, not prolactin secretion or adrenal function."
        },
        "learningObjective": "Explain the physiology of tuberoinfundibular dopamine blockade and the long-term skeletal risks of hyperprolactinemia.",
        "reference": "Haddad, P. M., & Wieck, A. (2004). Antipsychotic-induced hyperprolactinaemia: mechanisms, clinical features and management. Drugs, 64(20), 2291-2314.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q324",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "First-Generation Antipsychotics (FGA) and Extrapyramidal Symptoms",
        "difficulty": "Expert",
        "questionText": "Positron Emission Tomography (PET) neuroimaging studies have established a critical 'therapeutic window' for striatal dopamine D2 receptor occupancy by antipsychotic agents. What are the established lower and upper percentage thresholds for antipsychotic efficacy versus extrapyramidal toxicity?",
        "options": [
            {"id": "A", "text": "10% occupancy for efficacy; 30% occupancy triggers hyperprolactinemia"},
            {"id": "B", "text": "Approximately 60% to 65% D2 occupancy is required for clinical antipsychotic response, whereas occupancy exceeding 78% to 80% dramatically increases the incidence of extrapyramidal symptoms"},
            {"id": "C", "text": "95% occupancy is required for antipsychotic efficacy; toxicity occurs only at 100% saturation"},
            {"id": "D", "text": "Occupancy has no mathematical correlation with clinical effects due to second messenger buffering"}
        ],
        "correctAnswer": "B",
        "explanation": "Pioneering PET studies (Farde, Kapur, et al.) demonstrated that clinical antipsychotic efficacy requires approximately 60% to 65% striatal D2 receptor occupancy. When occupancy reaches 72%, hyperprolactinemia typically emerges; and once occupancy exceeds 78% to 80%, the risk of extrapyramidal symptoms (EPS) rises exponentially, defining the narrow therapeutic window of high-potency FGAs.",
        "incorrectExplanations": {
            "A": "10-30% occupancy produces no meaningful therapeutic antipsychotic effect.",
            "B": "60-65% occupancy provides clinical response, while exceeding 78-80% triggers high rates of EPS.",
            "C": "95% occupancy is well into the toxic range, causing severe parkinsonism or catatonia.",
            "D": "PET research clearly confirms a robust, reproducible sigmoidal relationship between D2 occupancy and clinical outcomes."
        },
        "learningObjective": "Synthesize PET imaging evidence regarding D2 receptor occupancy thresholds for antipsychotic efficacy and EPS liability.",
        "reference": "Kapur, S., et al. (2000). Relationship between dopamine D(2) occupancy, clinical response, and side effects: a double-blind PET study of first-episode schizophrenia. American Journal of Psychiatry, 157(4), 514-520.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 2: Second-Generation Antipsychotics (SGA) and Metabolic Monitoring (Q325 - Q334)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q325",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Foundation",
        "questionText": "What pharmacodynamic receptor binding property fundamentally distinguishes atypical (second-generation) antipsychotics from classical first-generation antipsychotics, explaining their lower risk of extrapyramidal side effects?",
        "options": [
            {"id": "A", "text": "Irreversible blockade of presynaptic monoamine oxidase enzymes"},
            {"id": "B", "text": "Selective agonism of peripheral beta-2 adrenergic receptors"},
            {"id": "C", "text": "Potent antagonism of serotonin 5-HT2A receptors combined with weaker or more transient dopamine D2 receptor antagonism"},
            {"id": "D", "text": "Pure antagonism of voltage-gated cardiac sodium channels"}
        ],
        "correctAnswer": "C",
        "explanation": "Second-generation (atypical) antipsychotics are characterized by a high ratio of serotonin 5-HT2A receptor antagonism relative to dopamine D2 receptor antagonism. 5-HT2A receptor blockade in the nigrostriatal pathway stimulates local dopamine release, which competes with the antipsychotic at D2 receptors, mitigating extrapyramidal symptoms and reducing prolactin elevation.",
        "incorrectExplanations": {
            "A": "MAO inhibition is the mechanism of MAOI antidepressants, not SGAs.",
            "B": "Beta-2 agonism is the mechanism of bronchodilators like salbutamol.",
            "C": "Potent 5-HT2A antagonism relative to D2 antagonism defines atypicality and reduces EPS liability.",
            "D": "Cardiac sodium channel blockade causes quinidine-like cardiotoxicity (seen in TCA overdose), not atypical antipsychotic action."
        },
        "learningObjective": "Explain the pharmacodynamic basis of atypicality involving 5-HT2A and D2 receptor interaction.",
        "reference": "Meltzer, H. Y. (1989). Clinical studies on the mechanism of action of clozapine: the dopamine-serotonin hypothesis of schizophrenia. Psychopharmacology, 99(Suppl 1), S18-S27.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q326",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Foundation",
        "questionText": "When considering the risk of significant weight gain, hyperlipidemia, and new-onset type 2 diabetes mellitus, which two second-generation antipsychotics carry the highest metabolic liability?",
        "options": [
            {"id": "A", "text": "Aripiprazole and lurasidone"},
            {"id": "B", "text": "Ziprasidone and haloperidol"},
            {"id": "C", "text": "Amisulpride and cariprazine"},
            {"id": "D", "text": "Clozapine and olanzapine"}
        ],
        "correctAnswer": "D",
        "explanation": "Clozapine and olanzapine possess the greatest propensity among all antipsychotics for causing marked weight gain, dyslipidemia, insulin resistance, and new-onset Type 2 diabetes. Their potent antagonism of histaminergic H1 and serotonergic 5-HT2C receptors in the hypothalamus strongly stimulates appetite and impairs peripheral glucose disposal.",
        "incorrectExplanations": {
            "A": "Aripiprazole and lurasidone are among the most metabolically neutral second-generation antipsychotics.",
            "B": "Ziprasidone has minimal weight gain risk, and haloperidol is an FGA with low metabolic impact.",
            "C": "Amisulpride and cariprazine have low-to-intermediate metabolic risk profiles.",
            "D": "Clozapine and olanzapine rank highest in metabolic syndrome liability across all guidelines."
        },
        "learningObjective": "Stratify second-generation antipsychotics according to their metabolic risk profile.",
        "reference": "De Hert, M., et al. (2011). Physical illness in patients with severe mental disorders. II. Barriers to care, monitoring and treatment guidelines, plus recommendations at the system and individual level. World Psychiatry, 10(2), 138-151.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q327",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Intermediate",
        "questionText": "According to established international guidelines (e.g., NICE, ADA/APA), which monitoring schedule represents the standard metabolic screening protocol for a patient newly commenced on an atypical antipsychotic?",
        "options": [
            {"id": "A", "text": "Baseline measurement of weight/BMI, waist circumference, blood pressure, fasting glucose/HbA1c, and fasting lipid profile; repeat weight at 4, 8, and 12 weeks; repeat BP, fasting glucose, and lipids at 12 weeks; and annually thereafter"},
            {"id": "B", "text": "Single baseline weight measurement with no further physical health checks required unless symptoms emerge"},
            {"id": "C", "text": "Weekly oral glucose tolerance tests and daily 24-hour urine collection for 2 years"},
            {"id": "D", "text": "Bi-weekly echocardiograms and brain MRI scans every 6 months"}
        ],
        "correctAnswer": "A",
        "explanation": "Standard physical health monitoring protocols for antipsychotics mandate comprehensive baseline parameters (BMI, waist circumference, BP, HbA1c/fasting glucose, fasting lipids). Weight is re-checked at 4, 8, and 12 weeks post-initiation. At 12 weeks, BP, fasting glucose/HbA1c, and lipid panel are repeated, followed by comprehensive annual monitoring thereafter.",
        "incorrectExplanations": {
            "A": "Baseline, 12-week, and annual metabolic screening with early weight checks at 4, 8, and 12 weeks is the international standard.",
            "B": "Failing to re-check metabolic labs after baseline represents substandard care that misses early diabetic ketoacidosis.",
            "C": "Weekly oral glucose tolerance tests are excessively burdensome and not clinically indicated.",
            "D": "Echocardiograms and MRI scans are not part of routine metabolic screening protocols."
        },
        "learningObjective": "Apply clinical guideline protocols for baseline and ongoing metabolic monitoring of patients on antipsychotics.",
        "reference": "American Diabetes Association & American Psychiatric Association. (2004). Consensus development conference on antipsychotic drugs and obesity and diabetes. Diabetes Care, 27(2), 596-601.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q328",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Intermediate",
        "questionText": "Aripiprazole is recognized as a 'dopamine system stabilizer' due to its unique receptor pharmacology. How does its mechanism of action differ fundamentally from traditional D2 receptor antagonists?",
        "options": [
            {"id": "A", "text": "It completely destroys dopamine D2 receptors in the anterior pituitary gland"},
            {"id": "B", "text": "It acts as a partial agonist at dopamine D2 and 5-HT1A receptors, and an antagonist at 5-HT2A receptors, providing functional dopamine antagonism in hyperdopaminergic states and functional agonism in hypodopaminergic states"},
            {"id": "C", "text": "It is a pure dopamine reuptake transporter inhibitor with zero receptor affinity"},
            {"id": "D", "text": "It acts exclusively on cannabinoid CB1 receptors to suppress dopamine synthesis"}
        ],
        "correctAnswer": "B",
        "explanation": "Aripiprazole is a dopamine D2 receptor partial agonist (intrinsic activity ~25-30%). In areas of dopamine excess (mesolimbic pathway in psychosis), it competes with endogenous dopamine and lowers signaling, acting as a functional antagonist. In areas of dopamine deficit (mesocortical pathway), it stimulates D2 receptors, acting as a functional agonist. It is also a 5-HT1A partial agonist and 5-HT2A antagonist.",
        "incorrectExplanations": {
            "A": "Aripiprazole binds reversibly to receptors and does not cause cytotoxic destruction.",
            "B": "D2 partial agonism provides homeostatic modulation: functional antagonism during hyperdopaminergia and functional agonism during hypodopaminergia.",
            "C": "Aripiprazole does not act primarily as a dopamine reuptake inhibitor (that is the mechanism of bupropion/methylphenidate).",
            "D": "Aripiprazole's primary actions are on monoamine receptors, not cannabinoid receptors."
        },
        "learningObjective": "Explain the pharmacodynamics of dopamine D2 partial agonism demonstrated by aripiprazole.",
        "reference": "Burris, K. D., et al. (2002). Aripiprazole, a novel atypical antipsychotic drug with a unique pharmacology. Journal of Pharmacology and Experimental Therapeutics, 302(1), 381-389.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q329",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Intermediate",
        "questionText": "A patient commenced on clozapine must undergo mandatory haematological monitoring to prevent fatal agranulocytosis. According to national monitoring protocols, what is the mandatory blood testing frequency during the first 18 weeks, and what is the 'red alert' threshold for Absolute Neutrophil Count (ANC) mandating immediate cessation?",
        "options": [
            {"id": "A", "text": "Monthly FBC for 18 weeks; stop if ANC < 3.0 x 10^9/L"},
            {"id": "B", "text": "Daily FBC for 18 weeks; stop if platelets < 100 x 10^9/L"},
            {"id": "C", "text": "Weekly FBC for the first 18 weeks; immediate cessation of clozapine if ANC falls below 1.0 x 10^9/L (or WBC < 2.0 x 10^9/L) / 'Red Alert'"},
            {"id": "D", "text": "FBC every 6 months; stop only if eosinophils exceed 20%"}
        ],
        "correctAnswer": "C",
        "explanation": "Clozapine monitoring mandates a Full Blood Count (FBC) weekly for the first 18 weeks, then fortnightly from weeks 19 to 52, and monthly thereafter. A 'Red Alert' occurs if the Absolute Neutrophil Count (ANC) falls below 1.0 x 10^9/L (or WBC < 2.0 x 10^9/L; or ANC < 1.5 in benign ethnic neutropenia protocols). A Red Alert requires immediate cessation of clozapine, patient isolation, urgent medical review, and a permanent ban on rechallenge.",
        "incorrectExplanations": {
            "A": "Monthly testing during the first 18 weeks is unsafe; weekly testing is legally mandated.",
            "B": "Daily venepuncture is clinically excessive and impractical.",
            "C": "Weekly testing for 18 weeks and an ANC cutoff < 1.0 x 10^9/L is the universal haematological safety standard.",
            "D": "Six-monthly testing during the first year is dangerous, as agranulocytosis risk peaks within the first 18 weeks."
        },
        "learningObjective": "Identify mandatory haematological monitoring schedules and critical red-alert thresholds for clozapine.",
        "reference": "Taylor, D. M., et al. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Clozapine monitoring.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q330",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Intermediate",
        "questionText": "During the third week of clozapine titration, a 28-year-old patient develops a resting tachycardia of 118 bpm, low-grade fever of 38.1 C, shortness of breath on exertion, and chest discomfort. Which life-threatening cardiovascular complication must be investigated immediately?",
        "options": [
            {"id": "A", "text": "Aortic dissection"},
            {"id": "B", "text": "Mitral valve prolapse"},
            {"id": "C", "text": "Subacute bacterial endocarditis"},
            {"id": "D", "text": "Clozapine-induced acute myocarditis"}
        ],
        "correctAnswer": "D",
        "explanation": "Clozapine-induced myocarditis is an idiosyncratic inflammatory reaction of the myocardium with a mortality rate of up to 10-20%. Over 80% of cases occur within the first 4 to 8 weeks of initiation. Clinical signs include unexplained persistent tachycardia, fever, chest pain, dyspnea, and elevated troponin and C-reactive protein (CRP). Immediate cessation and emergency cardiology admission are mandatory.",
        "incorrectExplanations": {
            "A": "Aortic dissection presents with sudden, tearing chest pain radiating to the back, not subacute fever and tachycardia during clozapine titration.",
            "B": "Mitral valve prolapse is a chronic structural valvular leaflet issue, not an acute drug-induced inflammatory response.",
            "C": "Endocarditis is caused by bacterial colonization of valves, typically presenting with murmurs and positive blood cultures.",
            "D": "Clozapine-induced myocarditis peaks in weeks 2 to 4, presenting with tachycardia, fever, and chest discomfort."
        },
        "learningObjective": "Recognize the clinical presentation and emergency management of clozapine-induced myocarditis.",
        "reference": "Ronaldson, K. J., et al. (2011). Clinical course and analysis of ten fatal cases of clozapine-induced myocarditis and comparison with 43 surviving cases. Schizophrenia Research, 128(1-3), 161-165.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q331",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Advanced",
        "questionText": "A patient established on clozapine reports severe abdominal pain, abdominal distension, vomiting, and not having passed a bowel movement for 5 days. Examination reveals absent bowel sounds and tympanic percussion. Why is clozapine-induced gastrointestinal hypomotility clinically critical, and what is the underlying mechanism?",
        "options": [
            {"id": "A", "text": "It results from potent muscarinic (M3) and serotonergic (5-HT3) antagonism causing intestinal hypomotility, leading to paralytic ileus, bowel necrosis, and septic shock, which kills more patients than agranulocytosis"},
            {"id": "B", "text": "It is caused by excessive hypergastrinemia stimulating duodenal hyperperistalsis"},
            {"id": "C", "text": "It reflects acute clozapine-induced pancreatitis cured with high-fat meals"},
            {"id": "D", "text": "It is a benign psychosomatic conversion symptom that requires only reassurance"}
        ],
        "correctAnswer": "A",
        "explanation": "Clozapine-induced gastrointestinal hypomotility (CIGH) is mediated by potent anticholinergic (muscarinic M3) and antiserotonergic actions slowing bowel peristalsis. It affects up to 50% of patients and can progress to severe fecal impaction, paralytic ileus, toxic megacolon, bowel ischemia, perforation, and death. Epidemiological data show that CIGH carries a higher mortality rate than clozapine-induced agranulocytosis.",
        "incorrectExplanations": {
            "A": "Clozapine anticholinergic/antiserotonergic blockade causes severe bowel hypomotility and fatal paralytic ileus.",
            "B": "Clozapine causes profound hypomotility (paralysis of the bowel), not hyperperistalsis.",
            "C": "Paralytic ileus is not acute pancreatitis, and high-fat meals worsen gastrointestinal distress.",
            "D": "Dismissing severe constipation on clozapine as psychosomatic can lead to preventable fatal bowel necrosis."
        },
        "learningObjective": "Evaluate the clinical risks of clozapine-induced gastrointestinal hypomotility and implement proactive bowel management.",
        "reference": "Every-Palmer, S., & Ellis, P. M. (2017). Clozapine-induced gastrointestinal hypomotility: a potentially fatal adverse event. CNS Drugs, 31(7), 543-558.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q332",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Advanced",
        "questionText": "A patient on clozapine complains of waking up every morning with pillows soaked with saliva and experiencing distressing daytime drooling (sialorrhea). What is the paradoxical pharmacological mechanism, and which evidenced intervention is appropriate?",
        "options": [
            {"id": "A", "text": "Pure beta-adrenergic blockade; treated with high-dose propranolol"},
            {"id": "B", "text": "Paradoxical agonism at muscarinic M4 receptors combined with impaired laryngeal swallowing reflexes; treated with sublingual ipratropium spray or oral glycopyrrolate"},
            {"id": "C", "text": "Direct stimulation of parotid salivary duct calcification; treated with surgical gland excision"},
            {"id": "D", "text": "Histaminergic H2 stimulation; treated with oral ranitidine"}
        ],
        "correctAnswer": "B",
        "explanation": "Although clozapine is a potent anticholinergic antagonist at most muscarinic receptors, it acts as a selective partial agonist at muscarinic M4 receptors, stimulating saliva production. Concurrently, clozapine sedates the patient and reduces the pharyngeal swallowing reflex during sleep. First-line treatments include topical anticholinergic drops (e.g., sublingual ipratropium bromide spray) or peripheral oral antimuscarinic agents like glycopyrrolate.",
        "incorrectExplanations": {
            "A": "Beta-blockade does not treat clozapine-induced hypersalivation.",
            "B": "M4 agonism combined with impaired swallowing causes sialorrhea, managed by local/peripheral antimuscarinics (ipratropium, glycopyrrolate).",
            "C": "Parotid gland excision is an invasive, inappropriate surgical mutilation for a pharmacological side effect.",
            "D": "H2 stimulation is not the mechanism of clozapine-induced sialorrhea."
        },
        "learningObjective": "Explain the mechanism of clozapine-induced sialorrhea and select targeted evidence-based treatments.",
        "reference": "Syed, R., et al. (2008). Pharmacological interventions for clozapine-induced hypersalivation. Cochrane Database of Systematic Reviews, (3), CD005579.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q333",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Advanced",
        "questionText": "A patient with schizophrenia is prescribed risperidone 8 mg daily. The psychiatric liaison nurse notes that the patient has developed prominent parkinsonian rigidity and tremors, and blood tests reveal marked hyperprolactinemia. How is risperidone unique among second-generation antipsychotics regarding its dose-dependent binding profile?",
        "options": [
            {"id": "A", "text": "Risperidone cannot cross the blood-brain barrier and acts only on intestinal enteric neurons"},
            {"id": "B", "text": "Risperidone has no affinity for dopamine D2 receptors at any dose"},
            {"id": "C", "text": "Risperidone behaves like a typical FGA at doses above 6 mg/day due to potent striatal D2 occupancy exceeding 80%, and causes significant prolactin elevation even at low doses due to poor blood-brain barrier penetration retention in the pituitary"},
            {"id": "D", "text": "Risperidone causes immediate destruction of the locus coeruleus noradrenergic tract"}
        ],
        "correctAnswer": "C",
        "explanation": "Risperidone has the highest D2 receptor binding affinity among the common SGAs. At low doses (2-4 mg/day), it maintains atypicality; however, at doses exceeding 6 mg/day, striatal D2 occupancy crosses 80%, causing it to behave clinically like a high-potency FGA with significant EPS. Furthermore, because the pituitary gland lies outside the blood-brain barrier, risperidone potently blocks tuberoinfundibular D2 receptors even at low doses, causing marked hyperprolactinemia.",
        "incorrectExplanations": {
            "A": "Risperidone crosses the blood-brain barrier effectively to treat central psychotic symptoms.",
            "B": "Risperidone has exceptionally high affinity for dopamine D2 receptors.",
            "C": "At doses > 6 mg/day, risperidone acts like a typical FGA, and its pituitary exposure produces prominent hyperprolactinemia.",
            "D": "Risperidone does not cause structural destruction of the locus coeruleus."
        },
        "learningObjective": "Explain the dose-dependent pharmacodynamic shift of risperidone from atypicality to typical-like EPS and hyperprolactinemia.",
        "reference": "Kapur, S., et al. (1999). Clinical and theoretical implications of 5-HT2 and D2 receptor occupancy of clozapine, risperidone, and olanzapine in schizophrenia. American Journal of Psychiatry, 156(2), 286-293.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q334",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Second-Generation Antipsychotics (SGA) and Metabolic Monitoring",
        "difficulty": "Expert",
        "questionText": "A patient established on clozapine 400 mg daily with a stable therapeutic plasma level of 450 ng/mL is admitted to a smoke-free psychiatric inpatient unit. Over the next 10 days, the patient stops smoking tobacco completely. Two weeks later, the patient becomes severely drowsy, ataxic, experiences myoclonic jerks, and develops clozapine toxicity. What pharmacokinetic mechanism explains this occurrence?",
        "options": [
            {"id": "A", "text": "Nicotine in tobacco smoke inhibits renal tubular secretion of clozapine"},
            {"id": "B", "text": "Tobacco smoke activates gastric parietal cells, blocking oral clozapine absorption"},
            {"id": "C", "text": "Tobacco smoke contains carbon monoxide that directly destroys clozapine molecules in systemic circulation"},
            {"id": "D", "text": "Polycyclic aromatic hydrocarbons in tobacco smoke induce hepatic CYP1A2 enzymes; smoking cessation removes this induction, causing clozapine metabolism to drop and serum levels to double or triple"}
        ],
        "correctAnswer": "D",
        "explanation": "Polycyclic aromatic hydrocarbons (tar) in tobacco smoke—NOT nicotine—are potent inducers of the hepatic cytochrome P450 enzyme CYP1A2, which is the primary metabolic clearance pathway for clozapine and olanzapine. When a patient abruptly stops smoking (e.g., during hospital admission), CYP1A2 induction ceases over 1 to 2 weeks, causing clozapine clearance to plunge and serum clozapine levels to surge by 50% to 100% or more, precipitating severe toxicity and seizures.",
        "incorrectExplanations": {
            "A": "Nicotine is not the inducer and does not affect renal tubular secretion; hydrocarbons induce hepatic CYP1A2.",
            "B": "Tobacco smoke does not impair gastric absorption of clozapine.",
            "C": "Carbon monoxide does not destroy clozapine molecules in blood.",
            "D": "Removal of CYP1A2 enzyme induction following smoking cessation causes clozapine clearance to drop and blood levels to spike dangerously."
        },
        "learningObjective": "Analyze the pharmacokinetic interaction between tobacco smoke hydrocarbons, CYP1A2 induction, and clozapine toxicity upon smoking cessation.",
        "reference": "de Leon, J., et al. (2005). The effects of smoking on clozapine and olanzapine metabolism: a review. Psychopharmacology, 180(3), 390-398.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 3: Antidepressants and Neurochemical Mechanisms (Q335 - Q344)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q335",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Foundation",
        "questionText": "What is the primary cellular mechanism of action common to all Selective Serotonin Reuptake Inhibitors (SSRIs), such as fluoxetine, sertraline, and citalopram?",
        "options": [
            {"id": "A", "text": "Selective inhibition of the presynaptic serotonin reuptake transporter (SERT), increasing serotonin availability in the synaptic cleft"},
            {"id": "B", "text": "Direct postsynaptic activation of nicotinic acetylcholine receptors"},
            {"id": "C", "text": "Selective blockade of postsynaptic dopamine D2 receptors in the striatum"},
            {"id": "D", "text": "Inhibition of peripheral catechol-O-methyltransferase (COMT)"}
        ],
        "correctAnswer": "A",
        "explanation": "SSRIs selectively bind to and inhibit the presynaptic serotonin transporter protein (SERT), blocking the reuptake of 5-hydroxytryptamine (serotonin) into the presynaptic neuron. This increases the concentration and residence time of serotonin in the synaptic cleft, triggering downstream adaptive changes including 5-HT1A autoreceptor desensitization and neurogenesis.",
        "incorrectExplanations": {
            "A": "Selective inhibition of SERT increases synaptic serotonin levels, mediating SSRI antidepressant efficacy.",
            "B": "Nicotinic acetylcholine receptors are not the primary target of SSRIs.",
            "C": "D2 receptor blockade is the mechanism of antipsychotics, not SSRIs.",
            "D": "COMT inhibition is utilized in Parkinson's disease (e.g., entacapone), not the mechanism of SSRIs."
        },
        "learningObjective": "State the primary cellular and molecular mechanism of action of SSRIs.",
        "reference": "Stahl, S. M. (2021). Stahl's Essential Psychopharmacology (5th ed.). Cambridge University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q336",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Foundation",
        "questionText": "A 62-year-old patient who suffered an acute myocardial infarction 6 weeks ago develops major depressive disorder. According to the landmark SADHART trial and international cardiology/psychiatry guidelines, which SSRI is the first-line choice due to its proven cardiovascular safety and antiplatelet stability?",
        "options": [
            {"id": "A", "text": "Amitriptyline"},
            {"id": "B", "text": "Sertraline"},
            {"id": "C", "text": "Tranylcypromine"},
            {"id": "D", "text": "Venlafaxine high-dose"}
        ],
        "correctAnswer": "B",
        "explanation": "Sertraline is the established first-line antidepressant of choice in patients with unstable angina or recent myocardial infarction, validated by the SADHART (Sertraline Antidepressant Heart Attack Randomized Trial). It has negligible cardiotoxicity, does not prolong QTc at standard therapeutic doses, and possesses mild antiplatelet effects that do not increase cardiovascular mortality.",
        "incorrectExplanations": {
            "A": "Amitriptyline (TCA) is strictly contraindicated post-MI due to cardiotoxicity, orthostasis, and dysrhythmias.",
            "B": "Sertraline is the evidence-based first-line antidepressant in cardiovascular disease post-MI.",
            "C": "Tranylcypromine (MAOI) carries severe risks of hypertensive crisis and drug interactions.",
            "D": "High-dose venlafaxine causes dose-dependent hypertension and tachycardia, undesirable post-MI."
        },
        "learningObjective": "Select the safest evidence-based antidepressant for patients with ischemic cardiac disease.",
        "reference": "Glassman, A. H., et al. (2002). Sertraline treatment of major depression in patients with acute MI or unstable angina (SADHART trial). JAMA, 288(6), 701-709.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q337",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Intermediate",
        "questionText": "Regulatory agencies (FDA and MHRA) issued safety warnings restricting the maximum daily dose of citalopram to 40 mg in general adults and 20 mg in adults over 65 years or those with hepatic impairment. What specific cardiac risk prompted this dosage restriction?",
        "options": [
            {"id": "A", "text": "Severe coronary artery vasospasm (Prinzmetal angina)"},
            {"id": "B", "text": "Acute bacterial pericarditis"},
            {"id": "C", "text": "Dose-dependent prolongation of the electrocardiographic QTc interval, risking Torsades de Pointes and fatal ventricular dysrhythmias"},
            {"id": "D", "text": "Aortic valve calcification"}
        ],
        "correctAnswer": "C",
        "explanation": "Citalopram (and to a lesser degree escitalopram) causes concentration-dependent prolongation of the electrocardiographic QT interval by blocking the cardiac hERG potassium channel. Excessive QTc prolongation (>500 ms) substantially increases the risk of Torsades de Pointes, a polymorphic ventricular tachycardia that can degenerate into fatal ventricular fibrillation. Hence, maximum doses were capped at 40 mg/day (20 mg in the elderly).",
        "incorrectExplanations": {
            "A": "Citalopram does not cause coronary artery vasospasm.",
            "B": "Pericarditis is an inflammatory condition unrelated to SSRI pharmacology.",
            "C": "Concentration-dependent QTc prolongation risking Torsades de Pointes prompted regulatory dosage restrictions.",
            "D": "Aortic valve calcification is a degenerative structural condition, not an SSRI-induced channelopathy."
        },
        "learningObjective": "Identify cardiac safety warnings and maximum dosing limits for citalopram related to QTc prolongation.",
        "reference": "Medicines and Healthcare products Regulatory Agency. (2011). Citalopram and escitalopram: QT interval prolongation. Drug Safety Update, 5(5), A1.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q338",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Intermediate",
        "questionText": "A patient with refractory depression is commenced on venlafaxine and titrated up to 225 mg daily. In addition to monitoring depressive symptoms, which vital sign parameter must the psychiatric nurse monitor regularly due to venlafaxine's dual reuptake inhibition at higher doses?",
        "options": [
            {"id": "A", "text": "Peak expiratory flow rate"},
            {"id": "B", "text": "Intraocular pressure"},
            {"id": "C", "text": "Capillary blood glucose"},
            {"id": "D", "text": "Blood pressure (specifically looking for sustained diastolic hypertension)"}
        ],
        "correctAnswer": "D",
        "explanation": "Venlafaxine functions primarily as a serotonergic reuptake inhibitor (SRI) at lower doses (<150 mg/day). At moderate-to-high doses (>=150-225 mg/day), it additionally exerts potent norepinephrine reuptake inhibition (NRI). This elevated noradrenergic tone can induce dose-dependent increases in blood pressure and resting heart rate, occasionally causing sustained diastolic hypertension.",
        "incorrectExplanations": {
            "A": "Peak expiratory flow rate is monitored in asthma, not routine SNRI titration.",
            "B": "Intraocular pressure monitoring is for acute closed-angle glaucoma, not routine venlafaxine surveillance.",
            "C": "Venlafaxine does not cause primary acute glycemic dysregulation requiring routine fingerstick glucose checks.",
            "D": "Blood pressure monitoring is mandatory because high-dose noradrenergic reuptake inhibition can cause sustained hypertension."
        },
        "learningObjective": "Explain the dose-dependent dual mechanism of venlafaxine and the clinical necessity of blood pressure monitoring.",
        "reference": "Taylor, D. M., et al. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Venlafaxine.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q339",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Foundation",
        "questionText": "A 74-year-old patient with severe depression experiences profound insomnia and has lost 8 kg due to marked anorexia. The psychiatrist prescribes mirtazapine 15 mg at bedtime. What unique pharmacodynamic profile makes mirtazapine advantageous in this specific clinical presentation?",
        "options": [
            {"id": "A", "text": "Potent stimulant properties via dopamine reuptake inhibition causing weight loss"},
            {"id": "B", "text": "Antagonism of presynaptic alpha-2 adrenergic receptors enhancing noradrenaline and 5-HT transmission, combined with potent histaminergic H1 receptor antagonism that promotes marked sedation and increased appetite/weight gain"},
            {"id": "C", "text": "Irreversible inhibition of monoamine oxidase A and B enzymes"},
            {"id": "D", "text": "Direct cholinergic agonism that prevents memory decline and accelerates gastrointestinal transit"}
        ],
        "correctAnswer": "B",
        "explanation": "Mirtazapine is a Noradrenergic and Specific Serotonergic Antidepressant (NaSSA). It blocks presynaptic alpha-2 autoreceptors and heteroreceptors, increasing noradrenaline and serotonin release. Concurrently, its potent blockade of postsynaptic 5-HT2 and 5-HT3 receptors prevents serotonin-mediated nausea, anxiety, and sexual dysfunction, while potent H1 histamine blockade induces marked drowsiness/sedation and stimulates appetite, making 15 mg highly therapeutic for depressed patients with insomnia and cachexia.",
        "incorrectExplanations": {
            "A": "Mirtazapine is sedating and stimulates appetite, rather than acting as a dopamine stimulant causing weight loss.",
            "B": "Alpha-2 antagonism coupled with potent H1 blockade provides rapid sedation and appetite stimulation.",
            "C": "Mirtazapine does not inhibit MAO enzymes.",
            "D": "Mirtazapine has no meaningful direct cholinergic agonist activity."
        },
        "learningObjective": "Explain the unique receptor profile of mirtazapine and its clinical utility for depressed patients with insomnia and weight loss.",
        "reference": "Fawcett, J., & Barkin, R. L. (1998). Review of the results of clinical studies on the efficacy, safety and tolerability of mirtazapine for depression. International Clinical Psychopharmacology, 13(6), 289-296.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q340",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Intermediate",
        "questionText": "A 28-year-old patient being treated for depression wishes to switch antidepressants because their current SSRI causes severe sexual dysfunction (anorgasmia and loss of libido). The clinician considers bupropion. Which medical history finding represents an absolute contraindication to initiating bupropion?",
        "options": [
            {"id": "A", "text": "Co-occurring tobacco dependence"},
            {"id": "B", "text": "Premature ejaculation"},
            {"id": "C", "text": "A history of epilepsy / seizure disorder, or a current/prior diagnosis of Anorexia Nervosa or Bulimia Nervosa"},
            {"id": "D", "text": "History of mild seasonal allergic rhinitis"}
        ],
        "correctAnswer": "C",
        "explanation": "Bupropion (a norepinephrine-dopamine reuptake inhibitor, NDRI) does not cause sexual dysfunction. However, it lowers the epileptic seizure threshold in a dose-dependent manner. It is strictly contraindicated in patients with a history of seizure disorders and in patients with eating disorders (anorexia or bulimia), in whom the incidence of grand mal seizures during bupropion treatment was found to be unacceptably high due to electrolyte instability.",
        "incorrectExplanations": {
            "A": "Tobacco dependence is an indication for bupropion (marketed as Zyban for smoking cessation).",
            "B": "Bupropion lacks serotonergic sexual dampening and does not carry a contraindication for premature ejaculation.",
            "C": "Seizure disorders and eating disorders are absolute contraindications due to significantly heightened seizure risks.",
            "D": "Allergic rhinitis does not affect bupropion clearance or seizure liability."
        },
        "learningObjective": "Identify absolute contraindications to bupropion therapy, particularly seizure disorder and eating disorders.",
        "reference": "Fava, M., et al. (2005). 15 years of clinical experience with bupropion HCl: from bupropion to bupropion SR to bupropion XL. Primary Care Companion JCP, 7(3), 106-113.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q341",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Advanced",
        "questionText": "A 42-year-old patient is admitted to the intensive care unit following an intentional overdose of amitriptyline. The ECG reveals sinus tachycardia with a QRS duration of 148 ms and prolonged QTc. What is the primary molecular mechanism of Tricyclic Antidepressant (TCA) cardiac lethality in overdose, and what is the emergency pharmacological antidote?",
        "options": [
            {"id": "A", "text": "Coronary thrombosis; emergency streptokinase thrombolysis"},
            {"id": "B", "text": "Hypercalcemic crisis; intravenous pamidronate infusion"},
            {"id": "C", "text": "Beta-1 adrenergic blockade; intravenous glucagon infusion"},
            {"id": "D", "text": "Blockade of cardiac fast voltage-gated sodium channels (phase 0 depolarization), causing intraventricular conduction delay and lethal arrhythmias; treat with intravenous sodium bicarbonate boluses"}
        ],
        "correctAnswer": "D",
        "explanation": "In overdose, TCAs (e.g., amitriptyline) cause severe cardiotoxicity primarily by blocking cardiac fast voltage-gated sodium channels (Nav1.5), slowing Phase 0 depolarization. This manifests on ECG as QRS prolongation (>100 ms predicts seizures; >160 ms predicts ventricular arrhythmias). Intravenous sodium bicarbonate (1-2 mmol/kg) is the specific emergency antidote: it raises extracellular sodium (overcoming the competitive block) and alkalinizes blood pH (neutralizing the drug's active ionized form).",
        "incorrectExplanations": {
            "A": "TCA overdose does not involve coronary thrombosis.",
            "B": "Hypercalcemia is not the mechanism of TCA QRS widening.",
            "C": "Glucagon is the antidote for beta-blocker overdose, not TCA sodium channel blockade.",
            "D": "Nav1.5 sodium channel blockade causes QRS widening and fatal arrhythmias, reversed by IV sodium bicarbonate."
        },
        "learningObjective": "Explain the cardiac pathophysiology of TCA toxicity and the mechanism of intravenous sodium bicarbonate rescue.",
        "reference": "Body, R., et al. (2011). Guidelines in Emergency Medicine Network (GEMNet): guideline for the management of tricyclic antidepressant overdose. Emergency Medicine Journal, 28(4), 347-368.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q342",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Advanced",
        "questionText": "A patient prescribed the irreversible Monoamine Oxidase Inhibitor (MAOI) phenelzine attends a dinner party where they consume aged stilton cheese, cured salami, and two glasses of draught chianti. Within 45 minutes, they develop an explosive occipital headache, palpitations, dilated pupils, and a blood pressure of 230/130 mmHg. What dangerous clinical reaction has occurred?",
        "options": [
            {"id": "A", "text": "Hypertensive crisis ('cheese reaction') caused by dietary tyramine escaping gut MAO-A degradation and displacing stored norepinephrine into systemic circulation"},
            {"id": "B", "text": "Acute cyanide poisoning from fermented wine yeasts"},
            {"id": "C", "text": "Histamine intolerance with anaphylactoid angioedema"},
            {"id": "D", "text": "Acute neuroleptic malignant syndrome"}
        ],
        "correctAnswer": "A",
        "explanation": "Irreversible MAOIs inhibit both MAO-A and MAO-B in the gastrointestinal tract and liver. Ingested dietary tyramine (present in aged cheeses, cured meats, yeast extracts, draught beer) cannot be broken down and enters systemic circulation. Tyramine enters noradrenergic nerve terminals via the NET transporter and forces massive displacement of stored norepinephrine into the synaptic cleft, stimulating vascular alpha-1 receptors and triggering a catastrophic hypertensive crisis.",
        "incorrectExplanations": {
            "A": "Dietary tyramine displacement of norepinephrine causes severe hypertensive crisis when MAO-A is irreversibly inhibited.",
            "B": "Fermented wine contains tyramine, not cyanide.",
            "C": "Histamine intolerance does not produce hypertensive emergencies with blood pressures of 230/130 mmHg.",
            "D": "NMS is caused by dopamine D2 antagonism, not MAOI dietary tyramine ingestion."
        },
        "learningObjective": "Detail the mechanism of the MAOI-tyramine 'cheese reaction' and guide essential dietary precautions.",
        "reference": "Gillman, P. K. (2018). Much ado about tyramine: dietary tyramine and monoamine oxidase inhibitors. Journal of Neural Transmission, 125(11), 1707-1717.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q343",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Advanced",
        "questionText": "When switching an outpatient from fluoxetine to a monoamine oxidase inhibitor (MAOI) like tranylcypromine, what is the mandatory washout period required between stopping fluoxetine and starting the MAOI, and why?",
        "options": [
            {"id": "A", "text": "24 hours; fluoxetine is cleared completely by renal glomerular filtration within one day"},
            {"id": "B", "text": "3 days; to prevent histamine withdrawal urticaria"},
            {"id": "C", "text": "At least 5 weeks; because fluoxetine and its active metabolite norfluoxetine have an exceptionally long elimination half-life (up to 16 days), posing a lethal risk of serotonin toxicity if an MAOI is initiated too early"},
            {"id": "D", "text": "Zero days; cross-tapering should occur simultaneously to prevent depressive relapse"}
        ],
        "correctAnswer": "C",
        "explanation": "Fluoxetine has an elimination half-life of 2 to 4 days, but its active desmethyl metabolite, norfluoxetine, has an elimination half-life of 7 to 16 days. Complete elimination takes approximately 5 half-lives (about 5 weeks). Initiating an MAOI while norfluoxetine is still circulating will cause massive intrasynaptic serotonin accumulation and fatal serotonin syndrome. Therefore, a mandatory 5-week washout is required (compared to 1-2 weeks for other SSRIs).",
        "incorrectExplanations": {
            "A": "24 hours is completely insufficient and will precipitate fatal serotonin toxicity.",
            "B": "3 days does not account for the prolonged half-life of norfluoxetine.",
            "C": "A 5-week washout is legally and clinically mandated due to norfluoxetine's 16-day elimination half-life.",
            "D": "Simultaneous cross-tapering of fluoxetine and MAOIs is an absolute medical contraindication carrying high mortality."
        },
        "learningObjective": "Apply safe antidepressant switching protocols and calculate appropriate pharmacokinetic washout intervals.",
        "reference": "Taylor, D. M., et al. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Switching and stopping antidepressants.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q344",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Antidepressants and Neurochemical Mechanisms",
        "difficulty": "Expert",
        "questionText": "Two days after abruptly stopping paroxetine 40 mg daily, a patient experiences dizziness, electric-shock sensations in their head ('brain zaps'), nausea, insomnia, vivid nightmares, and crying spells. What clinical syndrome is this, which mnemonic summarizes its presentation, and what pharmacological factor determines its high risk with paroxetine and venlafaxine?",
        "options": [
            {"id": "A", "text": "Acute tardive dystonia; mnemonic 'CRAMPS'; caused by irreversible striatal D2 up-regulation"},
            {"id": "B", "text": "Subacute thyroid storm; mnemonic 'HOT-STORM'; caused by sudden thyroid hormone surge"},
            {"id": "C", "text": "Serotonin syndrome; mnemonic 'HUNTER'; caused by excessive serotonergic transmission"},
            {"id": "D", "text": "Antidepressant Discontinuation Syndrome; summarized by the 'FINISH' mnemonic; driven by a short elimination half-life and absence of active metabolites"}
        ],
        "correctAnswer": "D",
        "explanation": "Antidepressant Discontinuation Syndrome occurs upon abrupt cessation or rapid tapering of antidepressants, particularly agents with short elimination half-lives and no active metabolites (paroxetine t1/2 ~24 hrs; venlafaxine t1/2 ~5-11 hrs). Symptoms are captured by the FINISH mnemonic: Flu-like symptoms, Insomnia, Nausea, Imbalance/dizziness, Sensory disturbances (electric shock sensations / brain zaps), and Hyperarousal (anxiety, agitation).",
        "incorrectExplanations": {
            "A": "Tardive dystonia involves involuntary motor muscle contractions from antipsychotics, not SSRI withdrawal.",
            "B": "Thyroid storm is an endocrine hyperthyroid crisis presenting with hyperthermia and thyrotoxicosis.",
            "C": "Serotonin syndrome occurs upon initiation or overdose of serotonergic agents, not upon abrupt cessation.",
            "D": "Antidepressant Discontinuation Syndrome (FINISH) is driven by the rapid clearance of short-acting agents like paroxetine and venlafaxine."
        },
        "learningObjective": "Identify Antidepressant Discontinuation Syndrome using the FINISH mnemonic and explain the role of pharmacokinetic half-life.",
        "reference": "Berigan, T. R. (2002). The many faces of the antidepressant discontinuation syndrome. Primary Care Companion JCP, 4(1), 31-32.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 4: Mood Stabilisers and Therapeutic Drug Monitoring (Q345 - Q354)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q345",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Foundation",
        "questionText": "According to international clinical standards, what is the established therapeutic serum concentration range for lithium in maintenance treatment of Bipolar Disorder, and how many hours after the last dose should the blood sample be drawn?",
        "options": [
            {"id": "A", "text": "0.1 to 0.4 mmol/L; drawn 2 hours post-dose"},
            {"id": "B", "text": "1.5 to 2.5 mmol/L; drawn 24 hours post-dose"},
            {"id": "C", "text": "0.6 to 0.8 mmol/L (up to 1.0 mmol/L in acute mania/relapse); drawn exactly 12 hours post-dose (12-hour trough level)"},
            {"id": "D", "text": "2.0 to 3.5 mmol/L; drawn randomly during peak absorption"}
        ],
        "correctAnswer": "C",
        "explanation": "Standard maintenance lithium therapy requires a 12-hour post-dose serum trough concentration between 0.6 and 0.8 mmol/L (often targeted higher, 0.8 to 1.0 mmol/L, during acute mania or in patients with frequent relapses). Blood sampling must occur exactly 12 hours after the previous evening dose to ensure standardized, comparable trough measurements.",
        "incorrectExplanations": {
            "A": "0.1 to 0.4 mmol/L is subtherapeutic and provides no prophylaxis against manic or depressive relapse.",
            "B": "1.5 to 2.5 mmol/L represents significant clinical lithium toxicity.",
            "C": "0.6 to 0.8 mmol/L drawn exactly 12 hours post-dose is the standard international therapeutic trough target.",
            "D": "2.0 to 3.5 mmol/L causes severe neurotoxicity and renal damage."
        },
        "learningObjective": "Define the therapeutic serum reference range for lithium and execute correct 12-hour trough blood sampling protocols.",
        "reference": "National Institute for Health and Care Excellence. (2014). Bipolar disorder: assessment and management (NICE Guideline CG185). London: NICE.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q346",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Foundation",
        "questionText": "A patient stabilized on lithium for 4 years presents with coarse hand tremors, persistent nausea, profuse watery diarrhea, slurred speech (dysarthria), and unsteadiness on their feet (ataxia). Serum lithium is reported at 2.1 mmol/L. How is this clinical state categorized, and what is the primary risk?",
        "options": [
            {"id": "A", "text": "Mild therapeutic adaptation; encourage the patient to drink salty broth"},
            {"id": "B", "text": "Subtherapeutic pseudotremor; increase the lithium dose immediately"},
            {"id": "C", "text": "Conversion reaction; provide psychoanalytic psychotherapy"},
            {"id": "D", "text": "Moderate-to-severe lithium toxicity; risk of permanent cerebellar damage, seizures, coma, and acute renal failure mandating emergency hospitalisation"}
        ],
        "correctAnswer": "D",
        "explanation": "A serum lithium level of 2.1 mmol/L represents moderate-to-severe lithium toxicity. Coarse tremor, ataxia, dysarthria, nausea, and diarrhea are hallmark neurotoxic and gastrointestinal warning signs. Severe toxicity (>2.0 mmol/L) carries risks of permanent neurological damage (Syndrome of Irreversible Lithium-Effectuated Neurotoxicity - SILENT), grand mal seizures, renal shutdown, coma, and death, requiring urgent medical admission and IV hydration.",
        "incorrectExplanations": {
            "A": "A level of 2.1 mmol/L is a medical emergency, not a mild therapeutic adaptation.",
            "B": "The patient is toxic; increasing the dose could prove fatal.",
            "C": "Dismissing toxic motor ataxia as conversion reaction delays life-saving interventions.",
            "D": "Moderate-to-severe toxicity (>2.0 mmol/L) requires urgent hospitalization to prevent permanent neurological and renal injury."
        },
        "learningObjective": "Recognize the signs and symptoms of lithium toxicity and implement emergency clinical interventions.",
        "reference": "Baird-Gunning, J., et al. (2016). Lithium poisoning. Journal of Medical Toxicology, 12(3), 249-263.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q347",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Intermediate",
        "questionText": "Because lithium is cleared almost exclusively by the kidneys and concentrates in glandular tissues, which two organ systems require mandatory baseline and 6-monthly biochemical monitoring throughout long-term therapy?",
        "options": [
            {"id": "A", "text": "Renal function (eGFR and serum creatinine) and Thyroid function (TSH and free T4)"},
            {"id": "B", "text": "Pulmonary function (FEV1) and ocular fundoscopy"},
            {"id": "C", "text": "Hepatic transaminases (ALT/AST) and serum amylase"},
            {"id": "D", "text": "Bone marrow biopsy and synovial fluid cytology"}
        ],
        "correctAnswer": "A",
        "explanation": "Lithium undergoes 100% renal elimination and can cause nephrogenic diabetes insipidus (impaired urinary concentrating ability via vasopressin V2 receptor resistance) and chronic tubulointerstitial nephropathy. Furthermore, lithium inhibits thyroid hormone release and iodine coupling, causing hypothyroidism and goitre in up to 20-30% of patients. Renal function (eGFR/creatinine) and thyroid function (TSH) must be monitored baseline and at least every 6 months.",
        "incorrectExplanations": {
            "A": "Renal function and thyroid function require mandatory surveillance every 6 months.",
            "B": "Lithium does not cause pulmonary or ocular toxicity requiring routine spirometry.",
            "C": "Lithium is not metabolized by the liver; hepatic transaminases are relevant for valproate, not lithium.",
            "D": "Lithium does not cause bone marrow aplasia or joint effusions requiring biopsies."
        },
        "learningObjective": "Formulate a systematic clinical monitoring protocol for renal and thyroid function during maintenance lithium therapy.",
        "reference": "McKnight, R. F., et al. (2012). Lithium toxicity profile: a systematic review and meta-analysis. The Lancet, 379(9817), 721-728.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q348",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Intermediate",
        "questionText": "A patient maintained on lithium for bipolar disorder develops acute osteoarthritis and self-medicates with over-the-counter ibuprofen 400 mg three times daily. A week later, they present with tremors, confusion, and a lithium level of 2.2 mmol/L. What pharmacokinetic interaction caused this toxicity?",
        "options": [
            {"id": "A", "text": "Ibuprofen displaces lithium from plasma albumin binding sites"},
            {"id": "B", "text": "NSAIDs inhibit renal prostaglandin synthesis, reducing renal blood flow and glomerular filtration, which diminishes renal lithium clearance and increases serum levels by up to 30-50%"},
            {"id": "C", "text": "Ibuprofen stimulates hepatic CYP2D6 enzymes, producing active lithium metabolites"},
            {"id": "D", "text": "Ibuprofen binds to gastric lithium receptors and triples oral bioabsorption"}
        ],
        "correctAnswer": "B",
        "explanation": "Lithium is filtered freely by the glomerulus and 80% is reabsorbed in the proximal renal tubules. Non-steroidal anti-inflammatory drugs (NSAIDs, e.g., ibuprofen, naproxen, celecoxib) inhibit renal synthesis of vasodilatory prostaglandins, decreasing renal blood flow and glomerular filtration. This leads to increased proximal tubular reabsorption of lithium, decreasing lithium clearance and raising serum lithium concentrations by 30% to 50%, precipitating toxicity.",
        "incorrectExplanations": {
            "A": "Lithium does not bind to plasma proteins at all (0% protein binding); it is an inorganic ion.",
            "B": "NSAID-mediated inhibition of renal prostaglandin synthesis reduces renal lithium clearance, spiking serum levels.",
            "C": "Lithium is not metabolized by CYP enzymes and has no metabolites.",
            "D": "The interaction is entirely renal, not gastric absorption."
        },
        "learningObjective": "Explain the pharmacokinetic interaction between lithium and NSAIDs and educate patients on over-the-counter analgesic avoidance.",
        "reference": "Finley, P. R. (2016). Drug interactions with lithium: an update. Clinical Pharmacokinetics, 55(8), 925-941.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q349",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Intermediate",
        "questionText": "Why have regulatory authorities (such as the MHRA and EMA) implemented strict Pregnancy Prevention Programmes ('Prevent') prohibiting the prescription of sodium valproate to female patients of childbearing potential unless exceptional conditions are met?",
        "options": [
            {"id": "A", "text": "Valproate causes maternal irreversible retinal blindness"},
            {"id": "B", "text": "Valproate triggers sudden fatal cardiac rupture in postpartum mothers"},
            {"id": "C", "text": "Valproate is a potent teratogen carrying a ~10% risk of major congenital malformations (neural tube defects like spina bifida) and up to a 30% to 40% risk of neurodevelopmental disorders and autism in exposed children"},
            {"id": "D", "text": "Valproate passes into maternal bones and prevents breastmilk production permanently"}
        ],
        "correctAnswer": "C",
        "explanation": "Sodium valproate in pregnancy is associated with catastrophic teratogenicity: approximately a 10% risk of major congenital physical malformations (neural tube defects like spina bifida, craniofacial clefts, cardiac defects) and a 30% to 40% risk of long-term neurodevelopmental delay, cognitive impairment, and Autism Spectrum Disorders. The 'Prevent' programme mandates that valproate must not be used in women of childbearing potential unless fully informed, enrolled in a prevention programme, and using highly effective contraception.",
        "incorrectExplanations": {
            "A": "Valproate does not cause maternal retinal blindness.",
            "B": "Valproate does not cause postpartum cardiac rupture.",
            "C": "A 10% risk of major congenital malformations and 30-40% risk of neurodevelopmental disorders makes valproate strictly contraindicated in childbearing potential.",
            "D": "Valproate does not permanently destroy maternal breastmilk production."
        },
        "learningObjective": "Outline the teratogenic risks of sodium valproate and adhere to the guidelines of the Valproate Pregnancy Prevention Programme.",
        "reference": "Medicines and Healthcare products Regulatory Agency. (2018). Valproate medicines: contraindication in women of childbearing potential unless a Pregnancy Prevention Programme is in place. Drug Safety Update, 11(9), 1.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q350",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Intermediate",
        "questionText": "A 22-year-old male established on sodium valproate for Bipolar I Disorder presents with severe, persistent epigastric pain radiating to the back, nausea, and repeated vomiting. Blood tests show serum lipase and amylase elevated to 5 times the upper limit of normal. Which idiosyncratic adverse reaction has occurred?",
        "options": [
            {"id": "A", "text": "Duodenal peptic ulcer perforation"},
            {"id": "B", "text": "Acute cholecystitis with gallstone impaction"},
            {"id": "C", "text": "Valproate-induced acute pancreatitis"},
            {"id": "D", "text": "Mesenteric arterial thrombosis"}
        ],
        "correctAnswer": "C",
        "explanation": "Acute pancreatitis is an idiosyncratic, potentially life-threatening complication of sodium valproate that can occur at any time during treatment, independent of dose or serum concentration. Patients presenting with severe abdominal pain, nausea, and vomiting must be evaluated urgently with serum amylase and lipase. If pancreatitis is confirmed, valproate must be discontinued immediately.",
        "incorrectExplanations": {
            "A": "Peptic ulcer perforation presents with a rigid, board-like abdomen and free air under the diaphragm on X-ray, not massive lipase spikes.",
            "B": "Acute cholecystitis causes right upper quadrant pain and fever, without marked isolated lipase elevation.",
            "C": "Valproate-induced acute pancreatitis is a recognized black-box complication presenting with radiating epigastric pain and elevated lipase/amylase.",
            "D": "Mesenteric thrombosis presents with severe pain out of proportion to exam in elderly patients with vascular disease."
        },
        "learningObjective": "Recognize the clinical presentation and laboratory diagnosis of valproate-induced acute pancreatitis.",
        "reference": "Grauso-Eby, N. L., et al. (2003). Acute pancreatitis in children from valproic acid. Pediatric Neurology, 28(2), 145-147.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q351",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Advanced",
        "questionText": "A patient with Bipolar II depression is commenced on lamotrigine. Why is lamotrigine strictly titrated using an initial low dose (25 mg daily) with slow bi-weekly dose increments over 6 weeks?",
        "options": [
            {"id": "A", "text": "To reduce the risk of life-threatening severe cutaneous adverse reactions, specifically Stevens-Johnson Syndrome (SJS) and Toxic Epidermal Necrolysis (TEN)"},
            {"id": "B", "text": "To prevent sudden fatal aplastic anemia occurring on Day 1"},
            {"id": "C", "text": "To allow the kidneys time to grow additional tubular glomeruli"},
            {"id": "D", "text": "To avoid immediate precipitation of severe manic exhaustion"}
        ],
        "correctAnswer": "A",
        "explanation": "The incidence of severe, potentially fatal cutaneous adverse reactions—including Stevens-Johnson Syndrome (SJS) and Toxic Epidermal Necrolysis (TEN)—is strongly correlated with the initial starting dose and the speed of dose escalation of lamotrigine. Standard slow titration (25 mg daily for weeks 1-2, 50 mg daily for weeks 3-4, then 100 mg daily) significantly reduces this risk. Any emerging rash, especially with fever or mucosal involvement, requires immediate cessation.",
        "incorrectExplanations": {
            "A": "Slow titration is specifically designed to minimize the incidence of life-threatening Stevens-Johnson Syndrome and TEN.",
            "B": "Aplastic anemia is an idiosyncratic risk associated with carbamazepine, not the driver of lamotrigine titration.",
            "C": "Kidneys do not generate new glomeruli in response to medication.",
            "D": "Lamotrigine has minimal risk of precipitating acute mania; the slow titration is purely dermatological safety."
        },
        "learningObjective": "Explain the pharmacological rationale for the slow titration schedule of lamotrigine to prevent Stevens-Johnson Syndrome.",
        "reference": "Messina, N., et al. (2000). Lamotrigine-induced Stevens-Johnson syndrome: a case report and review of the literature. Pharmacotherapy, 20(8), 987-991.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q352",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Advanced",
        "questionText": "A patient with bipolar disorder maintained on sodium valproate 1,000 mg daily requires the addition of lamotrigine for treatment-resistant depressive symptoms. What crucial pharmacokinetic interaction occurs between valproate and lamotrigine, and how must the lamotrigine titration be adjusted?",
        "options": [
            {"id": "A", "text": "Valproate doubles the renal clearance of lamotrigine, requiring the lamotrigine starting dose to be quadrupled to 100 mg daily"},
            {"id": "B", "text": "Valproate potently inhibits hepatic UDP-glucuronosyltransferase (UGT2B7), doubling lamotrigine's elimination half-life; therefore, the lamotrigine starting dose and titration rate must be reduced by more than 50% (starting at 25 mg every other day)"},
            {"id": "C", "text": "Lamotrigine destroys valproate in the stomach, requiring valproate to be switched to intravenous injections"},
            {"id": "D", "text": "There is zero pharmacokinetic interaction; standard adult dosing applies"}
        ],
        "correctAnswer": "B",
        "explanation": "Lamotrigine is eliminated almost exclusively by hepatic glucuronidation (via UGT enzymes). Sodium valproate is a potent inhibitor of glucuronidation, more than doubling the elimination half-life of lamotrigine (from ~25-30 hours up to ~60-70 hours). This dramatically spikes lamotrigine blood levels and escalates SJS risk unless the lamotrigine dose is reduced by at least half (starting at 25 mg every alternate day). Conversely, carbamazepine (a UGT inducer) halves lamotrigine levels.",
        "incorrectExplanations": {
            "A": "Valproate inhibits metabolism, it does not accelerate renal clearance; quadrupling the dose would provoke fatal SJS.",
            "B": "Valproate inhibits glucuronidation and doubles lamotrigine's half-life, mandating that the lamotrigine titration dose be halved.",
            "C": "Lamotrigine does not destroy valproate in the gastrointestinal tract.",
            "D": "Failing to account for the valproate-lamotrigine interaction is a major prescribing error that precipitates toxic epidermal necrolysis."
        },
        "learningObjective": "Calculate adjusted lamotrigine titration regimens in the presence of enzyme-inhibiting co-medications like sodium valproate.",
        "reference": "Garnett, W. R. (1997). Lamotrigine: pharmacokinetics. Journal of Child Neurology, 12(Suppl 1), S10-S15.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q353",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Advanced",
        "questionText": "A patient commenced on carbamazepine develops a sore throat, persistent fever of 38.8 C, mouth ulcers, and petechiae 6 weeks into treatment. An urgent full blood count demonstrates profound leukopenia (WBC 1.4 x 10^9/L) and absolute neutropenia. Which severe adverse haematological reaction has occurred?",
        "options": [
            {"id": "A", "text": "Transient physiological stress lymphopenia"},
            {"id": "B", "text": "Carbamazepine-induced agranulocytosis / aplastic anemia"},
            {"id": "C", "text": "Iron-deficiency microcytic anemia"},
            {"id": "D", "text": "Polycythemia vera"}
        ],
        "correctAnswer": "B",
        "explanation": "Carbamazepine carries a black-box warning for serious haematological toxicity, including agranulocytosis and aplastic anemia, which occurs at a rate roughly 5 to 8 times higher than in the general population. Clinical signs include sudden fever, sore throat, mucosal ulcerations, and bruising. Patients require immediate cessation of carbamazepine, protective isolation, and urgent medical/hematological evaluation.",
        "incorrectExplanations": {
            "A": "A WBC of 1.4 with absolute neutropenia represents life-threatening agranulocytosis, not benign stress lymphopenia.",
            "B": "Carbamazepine-induced agranulocytosis/aplastic anemia is a life-threatening complication requiring immediate drug cessation.",
            "C": "Iron-deficiency anemia affects red blood cell indices (MCV, ferritin), not acute catastrophic white cell collapse.",
            "D": "Polycythemia vera is an overproduction of red blood cells, the opposite of marrow suppression."
        },
        "learningObjective": "Recognize the signs of carbamazepine-induced agranulocytosis and implement emergency hematological safety protocols.",
        "reference": "Pellock, J. M. (1987). Carbamazepine side effects in children and adults. Epilepsia, 28(Suppl 3), S64-S70.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q354",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Mood Stabilisers and Therapeutic Drug Monitoring",
        "difficulty": "Expert",
        "questionText": "Beyond simple mood stabilization, lithium possesses unique, robust anti-suicidal properties independent of its antidepressant or antimanic efficacy. Which intracellular enzyme inhibition pathway is heavily implicated in lithium's neuroprotective, anti-suicidal, and grey-matter preservation actions?",
        "options": [
            {"id": "A", "text": "Inhibition of cardiac acetylcholinesterase"},
            {"id": "B", "text": "Selective activation of peripheral monoamine oxidase B"},
            {"id": "C", "text": "Stimulation of gastric histamine H2 receptors"},
            {"id": "D", "text": "Inhibition of Glycogen Synthase Kinase-3 beta (GSK-3b) and inositol monophosphatase (IMPase), leading to upregulation of Brain-Derived Neurotrophic Factor (BDNF) and anti-apoptotic protein Bcl-2"}
        ],
        "correctAnswer": "D",
        "explanation": "Lithium directly inhibits Glycogen Synthase Kinase-3 beta (GSK-3b) and inositol monophosphatase (IMPase) within the phosphoinositol secondary messenger cascade. This inhibition suppresses pro-apoptotic signaling, upregulates anti-apoptotic Bcl-2, stimulates Brain-Derived Neurotrophic Factor (BDNF) synthesis, and promotes hippocampal neurogenesis and synaptic plasticity, explaining its unique long-term neuroprotective and anti-suicidal properties.",
        "incorrectExplanations": {
            "A": "Lithium does not target cardiac acetylcholinesterase.",
            "B": "Lithium does not activate peripheral monoamine oxidase enzymes.",
            "C": "Gastric H2 receptors mediate acid secretion and have no role in central anti-suicidal mechanisms.",
            "D": "Inhibition of GSK-3b and IMPase upregulates BDNF and Bcl-2, providing neuroprotection and anti-suicidal efficacy."
        },
        "learningObjective": "Synthesize the intracellular neuroprotective mechanisms of lithium involving GSK-3b inhibition and BDNF upregulation.",
        "reference": "Malhi, G. S., et al. (2013). Lithium: a neuroprotective drug? Australian & New Zealand Journal of Psychiatry, 47(3), 205-208.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 5: Anxiolytics, Hypnotics, and Sedatives (Q355 - Q364)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q355",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Foundation",
        "questionText": "What is the primary neurochemical mechanism of action of benzodiazepines (such as diazepam and lorazepam) in reducing anxiety and inducing sedation?",
        "options": [
            {"id": "A", "text": "Direct agonism of serotonin 5-HT2C receptors in the spinal cord"},
            {"id": "B", "text": "Competitive blockade of histamine H1 receptors in the cerebellum"},
            {"id": "C", "text": "Positive allosteric modulation of the GABA-A receptor, increasing the frequency of chloride channel opening in response to GABA"},
            {"id": "D", "text": "Inhibition of presynaptic dopamine transporter (DAT) proteins"}
        ],
        "correctAnswer": "C",
        "explanation": "Benzodiazepines act as positive allosteric modulators at the gamma-aminobutyric acid type A (GABA-A) receptor complex. By binding to a specific pocket between the alpha and gamma subunits, they enhance the receptor's affinity for endogenous GABA, increasing the frequency of chloride ion channel opening. The resulting chloride influx hyperpolarizes the neuronal membrane, producing widespread CNS inhibitory effects (anxiolysis, sedation, muscle relaxation, anticonvulsant action).",
        "incorrectExplanations": {
            "A": "Benzodiazepines do not act via serotonin 5-HT2C agonism.",
            "B": "Histamine H1 blockade mediates antihistaminic sedation, not benzodiazepine action.",
            "C": "Positive allosteric modulation of GABA-A increasing chloride channel opening frequency is the exact mechanism.",
            "D": "Dopamine transporter inhibition is the mechanism of psychostimulants, not GABAergic sedatives."
        },
        "learningObjective": "Explain the molecular mechanism of positive allosteric modulation of GABA-A receptors by benzodiazepines.",
        "reference": "Olsen, R. W., & Sieghart, W. (2009). International Union of Pharmacology. LXX. Subtypes of gamma-aminobutyric acid(A) receptors: classification on the basis of subunit composition, pharmacology, and function. Pharmacological Reviews, 60(3), 243-260.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q356",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Foundation",
        "questionText": "According to NICE and international clinical guidelines, what is the maximum recommended duration for prescribing benzodiazepines in the acute management of severe anxiety or insomnia?",
        "options": [
            {"id": "A", "text": "6 to 12 months with automatic repeat prescriptions"},
            {"id": "B", "text": "Indefinitely, provided the patient does not consume alcohol"},
            {"id": "C", "text": "Single dose only; never repeated under any circumstance"},
            {"id": "D", "text": "2 to 4 weeks (including tapering period) to prevent tolerance, physiological dependence, and rebound anxiety"}
        ],
        "correctAnswer": "D",
        "explanation": "Clinical guidelines universally recommend that benzodiazepine use for anxiety and insomnia be restricted to short-term crisis management (maximum 2 to 4 weeks, including the tapering-off phase). Prolonged use beyond 4 weeks inevitably produces neuroadaptation, pharmacodynamic tolerance, physical and psychological dependence, cognitive deficits, and rebound withdrawal symptoms upon cessation.",
        "incorrectExplanations": {
            "A": "Prescribing benzodiazepines for 6-12 months causes severe physiological dependence and is contrary to clinical guidelines.",
            "B": "Indefinite open-ended prescribing leads to chronic addiction and cognitive impairment.",
            "C": "Restricting strictly to a single dose is untrue; a brief course of several days up to 2-4 weeks is clinically indicated in acute crises.",
            "D": "A maximum duration of 2 to 4 weeks is the universally established guideline threshold to avoid dependence."
        },
        "learningObjective": "Identify evidence-based duration limits for benzodiazepine therapy to prevent physiological dependence.",
        "reference": "National Institute for Health and Care Excellence. (2011). Generalised anxiety disorder and panic disorder in adults (NICE Guideline CG113). London: NICE.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q357",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Intermediate",
        "questionText": "A 45-year-old patient who has taken lorazepam 2 mg three times daily for 3 years abruptly runs out of medication 48 hours ago. They present to the emergency department with severe tremor, tachycardia (130 bpm), profuse sweating, extreme agitation, hypersensitivity to light and sound, and brief visual illusions. What severe clinical condition is emerging, and what is the primary medical risk?",
        "options": [
            {"id": "A", "text": "Acute Benzodiazepine Withdrawal Syndrome; carrying imminent risk of grand mal seizures, delirium tremens, and cardiovascular collapse"},
            {"id": "B", "text": "Opiate withdrawal; risk of mild piloerection and yawning"},
            {"id": "C", "text": "Emergence of untreated Bipolar I mania"},
            {"id": "D", "text": "Catatonic excitement secondary to acute schizophrenia"}
        ],
        "correctAnswer": "A",
        "explanation": "Abrupt cessation of chronic high-dose benzodiazepines causes acute Benzodiazepine Withdrawal Syndrome due to severe unmasking of down-regulated GABA-A receptors and compensatory uninhibited glutamatergic storm. Symptoms include autonomic hyperactivity (tachycardia, diaphoresis, tremor), sensory distortions (photophobia, hyperacusis), psychosis, and a high risk of life-threatening generalized tonic-clonic seizures and delirium tremens. Immediate reinstatement with a long-acting agent (diazepam) and gradual tapering is required.",
        "incorrectExplanations": {
            "A": "Acute benzodiazepine withdrawal is a life-threatening medical emergency with imminent risk of fatal seizures and delirium.",
            "B": "Opiate withdrawal causes lacrimation, rhinorrhea, and muscle aches, but is rarely directly fatal compared to sedative-hypnotic withdrawal.",
            "C": "This is an acute neurochemical withdrawal state, not a primary manic episode.",
            "D": "Sensory hypersensitivity, severe autonomic tachycardia, and tremulousness following abrupt sedative stoppage define withdrawal, not catatonia."
        },
        "learningObjective": "Recognize the clinical features and life-threatening seizure risk of acute benzodiazepine withdrawal.",
        "reference": "Lader, M. (2011). Benzodiazepine harm: how can it be reduced? British Journal of Clinical Pharmacology, 77(2), 295-301.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q358",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Intermediate",
        "questionText": "Flumazenil is a specific competitive antagonist at the benzodiazepine binding site on the GABA-A receptor, capable of rapidly reversing benzodiazepine sedation. Why is the routine administration of flumazenil contraindicated in patients with suspected mixed overdoses or chronic benzodiazepine dependence?",
        "options": [
            {"id": "A", "text": "It can precipitate immediate intractable status epilepticus and fatal cardiac arrhythmias (especially if co-ingested with proconvulsant tricyclic antidepressants)"},
            {"id": "B", "text": "It permanently binds to red blood cells and prevents oxygen delivery"},
            {"id": "C", "text": "It causes acute renal cortical necrosis within 10 minutes"},
            {"id": "D", "text": "It induces immediate deep anaesthesia lasting over 48 hours"}
        ],
        "correctAnswer": "A",
        "explanation": "Flumazenil competitively displaces benzodiazepines from GABA-A receptors. In individuals with chronic benzodiazepine tolerance or dependence, sudden receptor clearance precipitates acute, severe withdrawal seizures that cannot be controlled with standard benzodiazepines. Furthermore, in mixed overdoses involving tricyclic antidepressants (TCAs), flumazenil removes the anticonvulsant buffering of the benzodiazepine, unleashing fatal TCA-induced cardiac arrhythmias and refractory status epilepticus.",
        "incorrectExplanations": {
            "A": "Flumazenil can trigger refractory status epilepticus and fatal arrhythmias, particularly in dependent patients or mixed TCA overdoses.",
            "B": "Flumazenil does not bind irreversibly to erythrocytes or block oxygen transport.",
            "C": "Flumazenil is not directly nephrotoxic and does not cause renal cortical necrosis.",
            "D": "Flumazenil is a receptor antagonist that reverses anesthesia, not an anesthetic agent."
        },
        "learningObjective": "Explain the risks and clinical contraindications of using flumazenil in acute overdose management.",
        "reference": "Veiraiah, A., et al. (2012). Flumazenil: a review of its role in acute benzodiazepine overdose. Emergency Medicine Journal, 29(4), 263-268.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q359",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Intermediate",
        "questionText": "Buspirone is a non-benzodiazepine anxiolytic indicated for Generalized Anxiety Disorder (GAD). What is its primary pharmacodynamic mechanism, and how does its clinical profile differ from traditional benzodiazepines?",
        "options": [
            {"id": "A", "text": "It is a potent GABA-A positive modulator that causes rapid addiction and amnesia"},
            {"id": "B", "text": "It is an irreversible inhibitor of acetylcholinesterase with instant sedative onset"},
            {"id": "C", "text": "It is a 5-HT1A receptor partial agonist; it lacks sedation, cognitive impairment, anticonvulsant effects, tolerance, or abuse potential, but requires 2 to 4 weeks for therapeutic anxiolytic onset"},
            {"id": "D", "text": "It blocks histamine H1 and alpha-1 receptors to produce immediate profound hypnosis within 15 minutes"}
        ],
        "correctAnswer": "C",
        "explanation": "Buspirone is an azapirone that acts as a partial agonist at presynaptic somatodendritic 5-HT1A autoreceptors and postsynaptic 5-HT1A receptors. Unlike benzodiazepines, buspirone does not interact with GABA receptors, causes no sedation or motor impairment, has zero potential for physical dependence or abuse, and does not exhibit cross-tolerance with benzodiazepines. Its primary limitation is a delayed onset of therapeutic efficacy (2 to 4 weeks).",
        "incorrectExplanations": {
            "A": "Buspirone does not bind to GABA-A receptors and has zero addictive or amnestic potential.",
            "B": "Buspirone is not an acetylcholinesterase inhibitor.",
            "C": "As a 5-HT1A partial agonist, buspirone lacks sedation and abuse potential but requires 2-4 weeks to work.",
            "D": "Buspirone is non-sedating and does not produce acute hypnotic effects."
        },
        "learningObjective": "Compare the pharmacodynamic mechanism and clinical characteristics of buspirone with benzodiazepines.",
        "reference": "Howland, R. H. (2015). Buspirone for the treatment of generalized anxiety disorder. Journal of Psychosocial Nursing and Mental Health Services, 53(11), 21-24.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q360",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Intermediate",
        "questionText": "The 'Z-drugs' (zopiclone, zolpidem, zaleplon) were originally developed as safer alternatives to benzodiazepines for insomnia. What is their molecular selectivity, and which significant adverse behaviors have emerged in post-marketing surveillance?",
        "options": [
            {"id": "A", "text": "They bind to dopamine D1 receptors; cause acute dystonic tongue protrusions"},
            {"id": "B", "text": "They block melatonin MT1 receptors; cause permanent daytime blindness"},
            {"id": "C", "text": "They act as pure opiate agonists; cause severe pupillary miosis and pulmonary edema"},
            {"id": "D", "text": "They selectively target the alpha-1 subunit of the GABA-A receptor; while less anxiolytic, they still cause dependence, tolerance, next-day ataxia/falls, and complex sleep behaviors (sleep-walking, sleep-driving, and nocturnal binge eating with complete amnesia)"}
        ],
        "correctAnswer": "D",
        "explanation": "Z-drugs selectively bind to the alpha-1 subunit of the GABA-A receptor, which preferentially mediates sedation and hypnotic effects rather than muscle relaxation or anxiolysis. However, post-marketing surveillance confirms that Z-drugs still induce tolerance, physical dependence, and rebound insomnia. Furthermore, they carry severe warnings for complex sleep-related behaviors (parasomnias like sleep-walking, sleep-driving, preparing food) performed while not fully awake with complete retrograde amnesia.",
        "incorrectExplanations": {
            "A": "Z-drugs act on GABA-A receptors, not dopamine D1 receptors.",
            "B": "Z-drugs do not block melatonin receptors and do not cause blindness.",
            "C": "Z-drugs are not opioids and do not act on mu-opioid receptors.",
            "D": "Alpha-1 GABA-A subunit selectivity mediates sedation, but carries risks of dependence, falls, and complex sleep behaviors (sleep-driving)."
        },
        "learningObjective": "Identify the receptor selectivity, adverse effects, and parasomnia risks associated with Z-drug hypnotics.",
        "reference": "Food and Drug Administration. (2019). FDA adds Boxed Warning for risk of serious injuries caused by sleepwalking and other complex sleep behaviors with certain insomnia medicines. FDA Drug Safety Communication.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q361",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Advanced",
        "questionText": "Promethazine is a first-generation phenothiazine antihistamine frequently utilized off-label in psychiatric units as a PRN sedative and for rapid tranquilization. Which pharmacological property contributes to its sedative action, and what major safety caution applies in elderly delirious patients?",
        "options": [
            {"id": "A", "text": "Central H1 receptor antagonism provides sedation, but its potent antimuscarinic (anticholinergic) properties can worsen delirium, cause urinary retention, and significantly increase fall risks in older adults"},
            {"id": "B", "text": "Pure GABA-B agonism causes rapid bone remineralization in dementia"},
            {"id": "C", "text": "Selective serotonin reuptake inhibition increases cortical clarity"},
            {"id": "D", "text": "Dopamine D2 agonism stimulates cognitive alertness, reversing confusion"}
        ],
        "correctAnswer": "A",
        "explanation": "Promethazine crosses the blood-brain barrier and blocks histamine H1 receptors in the tuberomammillary arousal pathways, inducing sedation. However, it also possesses potent central and peripheral antimuscarinic (anticholinergic) properties. In older adults or patients with existing neurocognitive impairment, this anticholinergic burden exacerbates delirium, provokes acute urinary retention, causes blurred vision, and substantially increases the risk of severe falls.",
        "incorrectExplanations": {
            "A": "H1 blockade produces sedation, but antimuscarinic action worsens delirium, causes urinary retention, and increases falls.",
            "B": "Promethazine is not a GABA-B agonist.",
            "C": "Promethazine does not inhibit serotonin reuptake.",
            "D": "Promethazine does not stimulate dopamine D2 receptors; as a phenothiazine, it possesses mild D2 antagonist properties."
        },
        "learningObjective": "Evaluate the clinical utility and anticholinergic hazards of promethazine in elderly and delirious psychiatric patients.",
        "reference": "Taylor, D. M., et al. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Promethazine.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q362",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Advanced",
        "questionText": "When prescribing an anxiolytic benzodiazepine for an elderly patient with mild hepatic impairment, why are lorazepam, oxazepam, or temazepam (the 'LOT' mnemonic) pharmacokinetically preferred over diazepam or chlordiazepoxide?",
        "options": [
            {"id": "A", "text": "The 'LOT' drugs are cleared entirely by pulmonary exhalation, completely bypassing the liver"},
            {"id": "B", "text": "The 'LOT' drugs undergo direct Phase II glucuronide conjugation without requiring hepatic cytochrome P450 Phase I microsomal oxidation, and do not form long-acting active metabolites that accumulate in hepatic impairment"},
            {"id": "C", "text": "The 'LOT' drugs are prodrugs that only activate when contacting bone marrow stem cells"},
            {"id": "D", "text": "Diazepam undergoes instantaneous biliary excretion, causing severe pancreatitis in the elderly"}
        ],
        "correctAnswer": "B",
        "explanation": "Most benzodiazepines (e.g., diazepam, chlordiazepoxide) undergo Phase I hepatic microsomal oxidation via CYP enzymes, generating active metabolites with long half-lives (e.g., desmethyldiazepam, t1/2 > 100 hours) that accumulate in older adults or liver dysfunction, causing prolonged sedation and ataxia. In contrast, Lorazepam, Oxazepam, and Temazepam ('LOT') bypass Phase I oxidation and undergo direct Phase II glucuronidation to inactive glucuronides, minimizing accumulation risk.",
        "incorrectExplanations": {
            "A": "Benzodiazepines are not cleared by pulmonary exhalation.",
            "B": "Lorazepam, Oxazepam, and Temazepam undergo direct Phase II glucuronidation without active metabolites, preventing accumulation in elderly/hepatic impairment.",
            "C": "These are active sedatives, not bone marrow prodrugs.",
            "D": "Diazepam has an extremely long half-life due to active hepatic metabolites, not rapid biliary excretion."
        },
        "learningObjective": "Apply the 'LOT' pharmacokinetic mnemonic to select safe benzodiazepines in geriatric and hepatically impaired populations.",
        "reference": "Greenblatt, D. J., et al. (1991). Benzodiazepines: history, pharmacokinetics, and pharmacodynamics. Journal of Clinical Pharmacology, 31(S1), 4-13.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q363",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Advanced",
        "questionText": "Melatonin receptor agonists (such as prolonged-release melatonin and ramelteon) are increasingly utilized for circadian rhythm sleep-wake disorders and primary insomnia in older adults. What major physiological advantage do they possess over traditional GABAergic hypnotics (benzodiazepines and Z-drugs)?",
        "options": [
            {"id": "A", "text": "They produce permanent wakefulness by destroying adenosine receptors"},
            {"id": "B", "text": "They induce profound neuromuscular paralysis to prevent nocturnal movement"},
            {"id": "C", "text": "They mimic endogenous pineal signaling at MT1 and MT2 receptors in the suprachiasmatic nucleus to synchronize circadian rhythms, without depressing respiration, impairing cognition, altering sleep architecture, or causing tolerance, dependence, or rebound insomnia"},
            {"id": "D", "text": "They double REM sleep duration and prevent nocturnal dreaming entirely"}
        ],
        "correctAnswer": "C",
        "explanation": "Melatonin agonists act specifically on MT1 (inducing sleepiness) and MT2 (synchronizing circadian phase) G-protein coupled receptors located in the suprachiasmatic nucleus (SCN) of the hypothalamus. Unlike GABA-A receptor modulators, melatonin agonists do not alter physiological sleep architecture (they preserve normal REM/NREM ratios), do not depress respiratory drive, do not cause next-day hangover or cognitive deficits, and have no abuse liability or withdrawal rebound.",
        "incorrectExplanations": {
            "A": "Melatonin agonists promote sleep induction and circadian synchronization, not permanent wakefulness.",
            "B": "They do not cause neuromuscular paralysis.",
            "C": "MT1/MT2 agonism synchronizes circadian rhythms without respiratory depression, tolerance, or dependence liability.",
            "D": "They preserve physiological sleep architecture rather than suppressing dreaming or unnaturally doubling REM."
        },
        "learningObjective": "Explain the advantages of melatonin receptor agonists over GABAergic hypnotics in older adults.",
        "reference": "Wade, A. G., et al. (2014). Prolonged-release melatonin in the treatment of insomnia in patients aged 55-80: quality of sleep and next-day alertness outcomes. Clinical Interventions in Aging, 9, 947-956.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q364",
        "module": "4. Psychopharmacology and Medication Management",
        "topic": "Anxiolytics, Hypnotics, and Sedatives",
        "difficulty": "Expert",
        "questionText": "What neuroadaptive molecular mechanism explains the development of profound pharmacodynamic tolerance and severe physical dependence following chronic continuous exposure to benzodiazepines?",
        "options": [
            {"id": "A", "text": "Complete necrosis of the raphe nuclei accompanied by upregulation of spinal reflex arcs"},
            {"id": "B", "text": "Irreversible destruction of brainstem chloride ion channels"},
            {"id": "C", "text": "Downregulation of the beta-1 adrenergic receptors in cardiac myocytes"},
            {"id": "D", "text": "Conformational uncoupling of benzodiazepine and GABA binding sites, internalization and endocytosis of surface GABA-A receptors, and compensatory upregulation of excitatory glutamatergic NMDA and AMPA receptor expression"}
        ],
        "correctAnswer": "D",
        "explanation": "Chronic continuous stimulation of GABA-A receptors by benzodiazepines triggers homeostatic counter-adaptation: (1) Conformational uncoupling between the GABA and benzodiazepine recognition sites; (2) Phosphorylation, clathrin-mediated internalization, and endocytosis (downregulation) of surface GABA-A receptors; and (3) Compensatory upregulation and hypersensitivity of excitatory glutamatergic transmission (NMDA/AMPA receptors and voltage-gated calcium channels). When the benzodiazepine is withdrawn, the loss of GABA inhibition combined with excess glutamate excitation precipitates severe withdrawal neurotoxicity.",
        "incorrectExplanations": {
            "A": "Benzodiazepines do not cause tissue necrosis of the raphe nuclei.",
            "B": "Chloride channels are not destroyed; receptor complexes are internalized and endocytosed.",
            "C": "Tolerance is a central neuroreceptor adaptation, not cardiac beta-1 downregulation.",
            "D": "GABA-A receptor uncoupling/internalization coupled with compensatory glutamatergic NMDA/AMPA upregulation drives tolerance and dependence."
        },
        "learningObjective": "Synthesize the neuroadaptive molecular mechanisms of benzodiazepine tolerance, receptor downregulation, and withdrawal hyperexcitability.",
        "reference": "Allison, C., & Pratt, J. A. (2003). Neuroadaptive processes in GABAergic and glutamatergic systems in benzodiazepine dependence. Pharmacology & Therapeutics, 98(2), 171-195.",
        "contentReviewStatus": "Peer Reviewed"
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(MOD4_P1)} questions for Module 4 Part 1")
