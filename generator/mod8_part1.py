"""
Module 8 Part 1: Questions MHN-Q715 to MHN-Q764 (50 questions)
Topics 1 to 5:
1. ADHD in children and adolescents (MHN-Q715 to MHN-Q724)
2. Autism Spectrum Disorder (ASD) (MHN-Q725 to MHN-Q734)
3. Childhood anxiety and depression (MHN-Q735 to MHN-Q744)
4. Adolescent risk-taking and self-harm (MHN-Q745 to MHN-Q754)
5. Child safeguarding (MHN-Q755 to MHN-Q764)
"""

QUESTIONS_MOD8_PART1 = [
    # -------------------------------------------------------------------------
    # Topic 1: ADHD in children and adolescents (MHN-Q715 - MHN-Q724)
    # Target Answers: A, C, B, D, A, C, B, A, D, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q715",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Foundation",
        "questionText": "According to the DSM-5 diagnostic criteria for Attention-Deficit/Hyperactivity Disorder (ADHD) in children up to age 16, what is the minimum number of symptoms required in either the inattention or hyperactivity-impulsivity domain, and across what minimum number of settings must impairment be demonstrated?",
        "options": [
            {"id": "A", "text": "At least 6 symptoms in either domain persisting for >=6 months, present across 2 or more distinct settings (such as home and school)"},
            {"id": "B", "text": "At least 2 symptoms persisting for 2 weeks, present in only 1 setting"},
            {"id": "C", "text": "Exactly 10 symptoms present for 1 month, observed exclusively in a clinical laboratory"},
            {"id": "D", "text": "At least 4 symptoms persisting for 12 months, observed strictly during sports activities"}
        ],
        "correctAnswer": "A",
        "explanation": "DSM-5 requires at least 6 symptoms of inattention and/or 6 symptoms of hyperactivity-impulsivity (persisting for at least 6 months to a degree that is inconsistent with developmental level) for children up to 16 years. Symptoms must be present across two or more settings (e.g., home, school, social activities) and several must have been present before age 12.",
        "incorrectExplanations": {
            "B": "Two symptoms for two weeks is insufficient for a neurodevelopmental disorder and reflects acute transient situational distress.",
            "C": "Ten symptoms is an arbitrary, non-DSM threshold, and evaluation cannot be restricted to artificial laboratory settings.",
            "D": "Four symptoms does not meet the diagnostic threshold of six for children."
        },
        "learningObjective": "Identify DSM-5 diagnostic thresholds, symptom duration, and cross-situational criteria for paediatric ADHD.",
        "reference": "American Psychiatric Association. (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed., DSM-5). APA.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q716",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Foundation",
        "questionText": "A 10-year-old girl is referred for assessment due to falling behind academically. Her teacher reports she is quiet, daydreaming, frequently loses her schoolbooks, and fails to complete assignments, but displays zero disruptive motor hyperactivity or impulsivity. Which ADHD presentation does this profile illustrate, and why are girls frequently diagnosed later than boys?",
        "options": [
            {"id": "A", "text": "Hyperactive-impulsive presentation; girls are diagnosed later because of physical growth rates"},
            {"id": "B", "text": "Conduct disorder; daydreaming is an intentional oppositional tactic"},
            {"id": "C", "text": "Predominantly inattentive presentation; girls frequently display internalizing and inattentive symptoms without disruptive externalizing behaviors, causing their difficulties to be overlooked"},
            {"id": "D", "text": "Childhood bipolar disorder with rapid cycling mania"}
        ],
        "correctAnswer": "C",
        "explanation": "ADHD has three presentations: Predominantly Inattentive, Predominantly Hyperactive-Impulsive, and Combined. Girls are significantly more likely to present with predominantly inattentive symptoms (daydreaming, disorganization, internal distractibility) without overt disruptive or aggressive hyperactivity, leading to substantial diagnostic delays compared to boys.",
        "incorrectExplanations": {
            "A": "This child shows zero hyperactivity or impulsivity, ruling out the hyperactive-impulsive subtype.",
            "B": "Daydreaming and losing books are executive function deficits, not deliberate conduct disorder violations.",
            "D": "Inattention without mood elevation, grandiosity, or decreased need for sleep does not indicate bipolar disorder."
        },
        "learningObjective": "Differentiate ADHD presentations and explain the gender differences contributing to under-identification of ADHD in females.",
        "reference": "NICE. (2018). Attention deficit hyperactivity disorder: diagnosis and management (NICE Guideline NG87).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q717",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Foundation",
        "questionText": "Prior to initiating psychostimulant pharmacotherapy (e.g., Methylphenidate) in a child diagnosed with ADHD, what essential baseline physical health and cardiovascular assessment must the psychiatric nurse perform?",
        "options": [
            {"id": "A", "text": "Lumbar puncture and 24-hour video electroencephalogram"},
            {"id": "B", "text": "Baseline blood pressure, pulse, height, weight, and a thorough personal and family cardiovascular history (including sudden unexplained cardiac death in young relatives)"},
            {"id": "C", "text": "Routine cranial magnetic resonance imaging (MRI) and serum prolactin"},
            {"id": "D", "text": "Serum lithium level and full rheumatology autoantibody panel"}
        ],
        "correctAnswer": "B",
        "explanation": "Clinical guidelines (NICE NG87 and AAP) mandate that prior to initiating stimulants, clinicians must measure baseline blood pressure, pulse, height, and weight (plotted on growth charts), and take a comprehensive cardiovascular history. A family history of sudden premature cardiac death or personal cardiac symptoms warrants a cardiology referral and baseline ECG.",
        "incorrectExplanations": {
            "A": "Invasive lumbar punctures and video EEGs are not indicated for routine ADHD stimulant initiation.",
            "C": "Neuroimaging and prolactin levels are unnecessary for initiating methylphenidate.",
            "D": "Lithium monitoring is specific to mood stabilizer therapy, not psychostimulants."
        },
        "learningObjective": "Execute required pre-treatment physical health and cardiovascular screening protocols prior to stimulant initiation.",
        "reference": "NICE. (2018). Attention deficit hyperactivity disorder: diagnosis and management (NICE Guideline NG87).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q718",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Intermediate",
        "questionText": "An 8-year-old boy taking extended-release methylphenidate presents for a 6-month follow-up. His parents report that he has lost his appetite at lunchtime, has trouble falling asleep, and his growth chart reveals his weight has dropped from the 50th percentile to the 25th percentile. How should the mental health nurse advise the family?",
        "options": [
            {"id": "A", "text": "Immediately double the dose of methylphenidate to stimulate metabolic appetite"},
            {"id": "B", "text": "Recommend immediate permanent hospitalization for anorexia nervosa"},
            {"id": "C", "text": "Tell the parents that weight loss is purely psychosomatic and requires no dietary adjustments"},
            {"id": "D", "text": "Advise high-calorie, nutrient-dense meals at breakfast before medication takes effect and in the late evening when medication wears off, monitor growth velocity closely, and discuss dose adjustment or drug holidays with the prescriber"}
        ],
        "correctAnswer": "D",
        "explanation": "Appetite suppression and insomnia are common, dose-dependent side effects of psychostimulants. Practical nursing management involves nutritional strategies: providing large, calorie-dense breakfasts before the morning stimulant dose takes effect, nutrient-dense evening snacks as the drug clears, monitoring growth velocity, and collaborating with the prescriber regarding dose timing or weekend drug holidays if growth falters.",
        "incorrectExplanations": {
            "A": "Increasing the stimulant dose would worsen anorexia and growth deceleration.",
            "B": "Stimulant-induced appetite loss is a known pharmacological side effect, not anorexia nervosa.",
            "C": "Ignoring growth failure leads to permanent stature impairment."
        },
        "learningObjective": "Formulate clinical nursing interventions to mitigate stimulant-induced appetite suppression and growth deceleration.",
        "reference": "Cortese, S., et al. (2018). Comparative efficacy and tolerability of medications for ADHD in children, adolescents, and adults: A systematic review and network meta-analysis. The Lancet Psychiatry, 5(9), 727-738.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q719",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Intermediate",
        "questionText": "A 12-year-old adolescent with ADHD and a personal history of severe motor tics cannot tolerate psychostimulants. The prescriber initiates Atomoxetine. What primary mechanism of action and black-box safety monitoring parameter must the nurse teach the patient and caregivers?",
        "options": [
            {"id": "A", "text": "Atomoxetine is a selective norepinephrine reuptake inhibitor (SNRI); caregivers must monitor for rare signs of suicidal ideation, agitation, and hepatic dysfunction"},
            {"id": "B", "text": "Atomoxetine is a high-potency dopamine D2 receptor blocker that causes irreversible agranulocytosis"},
            {"id": "C", "text": "Atomoxetine is an irreversible monoamine oxidase inhibitor requiring a strict tyramine-free diet"},
            {"id": "D", "text": "Atomoxetine is an immediate-acting narcotic sedative that produces profound dependence within 24 hours"}
        ],
        "correctAnswer": "A",
        "explanation": "Atomoxetine is a non-stimulant selective norepinephrine reuptake inhibitor (NRI). Because it affects monoamine transmission, regulatory authorities (FDA/MHRA) mandate a black-box warning regarding a small increased risk of suicidal thoughts in children and adolescents during early treatment. Additionally, patients and families must be alerted to symptoms of rare liver injury (jaundice, pruritus).",
        "incorrectExplanations": {
            "B": "Atomoxetine is not an antipsychotic D2 blocker and does not cause agranulocytosis.",
            "C": "Atomoxetine is not an MAOI and requires no tyramine dietary restrictions.",
            "D": "Atomoxetine has no abuse liability and is not a controlled narcotic substance."
        },
        "learningObjective": "Explain the pharmacodynamics, non-stimulant indications, and safety monitoring requirements of atomoxetine in paediatric ADHD.",
        "reference": "Taylor, D., et al. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q720",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Intermediate",
        "questionText": "The seminal Multimodal Treatment Study of Children with ADHD (MTA study) conducted by the NIMH compared four distinct treatment strategies: systematic medication management, intensive behavioural therapy, combined treatment, and routine community care. What was the critical clinical finding regarding core ADHD symptoms?",
        "options": [
            {"id": "A", "text": "Behavioural therapy alone was vastly superior to medication management for core inattention and hyperactivity"},
            {"id": "B", "text": "Routine community care outperformed all specialized treatment protocols"},
            {"id": "C", "text": "Carefully titrated medication management (and combined treatment) was significantly superior to behavioural therapy alone for reducing core ADHD symptoms, while combined treatment allowed lower medication doses and produced superior non-ADHD outcomes (social skills, parent satisfaction)"},
            {"id": "D", "text": "No intervention demonstrated any clinical efficacy over untreated observation"}
        ],
        "correctAnswer": "C",
        "explanation": "The landmark 14-month MTA study demonstrated that carefully titrated medication management (alone or combined) was superior to intensive behavioural therapy alone for core ADHD symptoms (hyperactivity, impulsivity, inattention). However, combined treatment offered significant advantages in functional domains (anxiety, academic performance, parent-child relations, social skills) and allowed slightly lower stimulant doses.",
        "incorrectExplanations": {
            "A": "The study conclusively proved medication was superior to behavioural therapy alone for core symptoms.",
            "B": "Routine community care yielded significantly poorer outcomes than algorithmic research care.",
            "D": "Active interventions showed robust efficacy compared to natural history."
        },
        "learningObjective": "Appraise empirical findings from the Multimodal Treatment Study of Children with ADHD (MTA study).",
        "reference": "MTA Cooperative Group. (1999). A 14-month randomized clinical trial of treatment strategies for attention-deficit/hyperactivity disorder. Archives of General Psychiatry, 56(12), 1073-1086.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q721",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Advanced",
        "questionText": "A community child and adolescent mental health nurse is delivering evidence-based Behavioural Parent Training (such as Incredible Years or Triple P) for parents of a 6-year-old child with combined ADHD. What core behavioural principle should the nurse train parents to prioritize?",
        "options": [
            {"id": "A", "text": "Delivering lengthy verbal lectures and executing severe physical corporal punishment for mistakes"},
            {"id": "B", "text": "Immediate, specific positive reinforcement and praise for desired behaviors ('catching the child being good'), paired with clear concise commands, structured routines, and planned ignoring of minor attention-seeking disruptions"},
            {"id": "C", "text": "Total permissiveness with zero boundaries or rules in the home environment"},
            {"id": "D", "text": "Locking the child in their bedroom in total darkness whenever they fidget"}
        ],
        "correctAnswer": "B",
        "explanation": "Evidence-based behavioural parent training focuses on positive reinforcement: providing immediate, labelled praise when the child displays desired behaviors, using brief direct one-step commands, establishing predictable daily routines, implementing token economies, and utilizing planned ignoring for minor irritating behaviors while setting consistent consequences for aggression.",
        "incorrectExplanations": {
            "A": "Lengthy verbal lectures overwhelm executive working memory, and corporal punishment increases aggression and trauma.",
            "C": "Permissiveness exacerbates ADHD-related disorganization and behavioral chaos.",
            "D": "Dark isolation is abusive, traumatizing, and clinically counterproductive."
        },
        "learningObjective": "Design evidence-based behavioural parent training interventions for young children diagnosed with ADHD.",
        "reference": "Webster-Stratton, C. (2011). The Incredible Years: A Troubleshooting Guide for Parents of Children Aged 2–8 Years. Incredible Years Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q722",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Advanced",
        "questionText": "A psychiatric nurse is consulting with a school team to establish classroom accommodations for a 9-year-old student with ADHD who struggles with working memory deficits and motor restlessness. Which individualized educational plan (IEP) modification is most evidence-supported?",
        "options": [
            {"id": "A", "text": "Preferential seating near the teacher away from windows and doors, chunking assignments into small sequential steps, using visual timers, and providing scheduled motor movement breaks"},
            {"id": "B", "text": "Placing the student's desk in a broom closet facing a blank wall with no teacher interaction"},
            {"id": "C", "text": "Requiring the student to complete four times as much written homework as peers to train mental discipline"},
            {"id": "D", "text": "Banning the student from all school recess and outdoor physical activity permanently"}
        ],
        "correctAnswer": "A",
        "explanation": "Evidence-based classroom accommodations for ADHD include environmental adjustments: preferential seating close to instructional delivery away from extraneous distractions, dividing complex assignments into small digestible chunks, utilizing visual checklists and timers to support temporal processing, and permitting planned movement breaks (e.g. running errands, standing desks).",
        "incorrectExplanations": {
            "B": "Isolating children in closets is abusive and punitive.",
            "C": "Excessive homework overwhelms depleted working memory and triggers behavioral meltdowns.",
            "D": "Depriving children with ADHD of recess eliminates physical activity, exacerbating restlessness."
        },
        "learningObjective": "Formulate evidence-based classroom and educational accommodations for students with ADHD.",
        "reference": "DuPaul, G. J., & Stoner, G. (2014). ADHD in the Schools: Assessment and Intervention Strategies (3rd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q723",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Advanced",
        "questionText": "An 11-year-old child with severe ADHD exhibits persistent vindictiveness, actively defies adult rules, deliberately annoys others, blames others for their mistakes, and has intense temper outbursts when given instructions. What comorbid psychiatric condition should the nurse assess for?",
        "options": [
            {"id": "A", "text": "Childhood-onset schizophrenia"},
            {"id": "B", "text": "Rheumatoid arthritis"},
            {"id": "C", "text": "Selective mutism"},
            {"id": "D", "text": "Oppositional Defiant Disorder (ODD)"}
        ],
        "correctAnswer": "D",
        "explanation": "Oppositional Defiant Disorder (ODD) is highly comorbid with paediatric ADHD, occurring in approximately 40% to 50% of children with ADHD. It is characterized by an enduring pattern of angry/irritable mood, argumentative/defiant behavior, and vindictiveness persisting for at least 6 months.",
        "incorrectExplanations": {
            "A": "Schizophrenia is characterized by hallucinations, delusions, and thought disorder, not behavioral defiance.",
            "B": "Rheumatoid arthritis is an autoimmune joint disorder.",
            "C": "Selective mutism is failure to speak in specific social situations due to anxiety."
        },
        "learningObjective": "Identify psychiatric comorbidities in paediatric ADHD, specifically Oppositional Defiant Disorder (ODD).",
        "reference": "American Psychiatric Association. (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed., DSM-5). APA.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q724",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "ADHD in children and adolescents",
        "difficulty": "Expert",
        "questionText": "A 17-year-old adolescent with ADHD who has been maintained on lisdexamfetamine is preparing to obtain their driver's license and transition to university. When planning this transition, which clinical risk and psychopharmacological guidance must the advanced practice nurse highlight?",
        "options": [
            {"id": "A", "text": "Advise the adolescent that driving without medication is safer because stimulants impair peripheral vision"},
            {"id": "B", "text": "Instruct the patient to abruptly stop all medication upon their 18th birthday because ADHD spontaneously cures at adulthood"},
            {"id": "C", "text": "Highlight epidemiological evidence that untreated ADHD substantially increases motor vehicle accident rates; ensure medication coverage extends to evening driving hours, discuss safe storage to prevent peer diversion, and execute a transition plan to adult mental health services"},
            {"id": "D", "text": "Recommend consuming energy drinks and alcohol simultaneously to enhance concentration"}
        ],
        "correctAnswer": "C",
        "explanation": "Adolescents with untreated ADHD have a 2- to 4-fold higher risk of serious vehicular collisions due to inattention and impulsivity. Studies show psychostimulant treatment significantly reduces motor vehicle crashes. Advanced nursing care involves ensuring medication coverage during peak driving hours (after school/evening), educating on diversion risks, and planning seamless CAMHS-to-adult transition.",
        "incorrectExplanations": {
            "A": "Stimulants improve reaction time and attention, dramatically lowering crash risk.",
            "B": "ADHD persists into adulthood in approximately 60-70% of cases; abrupt cessation causes functional relapse.",
            "D": "Combining alcohol and stimulants is hazardous and impairs driving judgment."
        },
        "learningObjective": "Evaluate adolescent transition risks in ADHD, including vehicular safety, stimulant diversion, and CAMHS-to-adult service continuity.",
        "reference": "Chang, Z., et al. (2014). Serious transport accidents in adults with attention-deficit/hyperactivity disorder and the effect of medication: A population-based study. JAMA Psychiatry, 71(3), 319-325.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 2: Autism Spectrum Disorder (ASD) (MHN-Q725 - MHN-Q734)
    # Target Answers: B, D, A, C, B, D, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q725",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Foundation",
        "questionText": "What are the two core diagnostic symptom domains that constitute the diagnostic dyad of Autism Spectrum Disorder (ASD) under the DSM-5 framework?",
        "options": [
            {"id": "A", "text": "Visual hallucinations and auditory hallucinations"},
            {"id": "B", "text": "1) Persistent deficits in social communication and social interaction across multiple contexts, and 2) Restricted, repetitive patterns of behavior, interests, or activities"},
            {"id": "C", "text": "Severe depressive mood swings and grandiosity"},
            {"id": "D", "text": "Severe short-term anterograde amnesia and motor apraxia"}
        ],
        "correctAnswer": "B",
        "explanation": "DSM-5 established a two-domain diagnostic framework for ASD: 1) Persistent deficits in social communication and social interaction (social-emotional reciprocity, nonverbal communication, developing relationships), and 2) Restricted, repetitive patterns of behavior, interests, or activities (stereotyped movements, insistence on sameness, fixated interests, sensory hyper/hyporeactivity).",
        "incorrectExplanations": {
            "A": "Hallucinations are psychotic phenomena, not core diagnostic features of ASD.",
            "C": "Mood swings and grandiosity describe bipolar disorder, not autism.",
            "D": "Amnesia and apraxia describe neurological dementia syndromes."
        },
        "learningObjective": "Recall the core diagnostic dyad of Autism Spectrum Disorder under DSM-5 criteria.",
        "reference": "American Psychiatric Association. (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed., DSM-5). APA.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q726",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Foundation",
        "questionText": "DSM-5 categorizes Autism Spectrum Disorder into three severity levels for clinical coding and service planning. What are these three severity levels based on the required level of assistance?",
        "options": [
            {"id": "A", "text": "Stage I (Curable), Stage II (Chronic), and Stage III (Terminal)"},
            {"id": "B", "text": "Grade A (Mild), Grade B (Moderate), and Grade C (Surgical)"},
            {"id": "C", "text": "Phase 1 (Inpatient), Phase 2 (Residential), and Phase 3 (Outpatient)"},
            {"id": "D", "text": "Level 1 ('Requiring support'), Level 2 ('Requiring substantial support'), and Level 3 ('Requiring very substantial support')"}
        ],
        "correctAnswer": "D",
        "explanation": "DSM-5 rates ASD severity across both social communication and restricted/repetitive behavior domains into three standardized tiers: Level 1: 'Requiring support', Level 2: 'Requiring substantial support', and Level 3: 'Requiring very substantial support.'",
        "incorrectExplanations": {
            "A": "Autism is a lifelong neurodevelopmental condition, not a staged terminal disease.",
            "B": "Surgical grading does not exist in neurodevelopmental psychiatric diagnosis.",
            "C": "Severity levels reflect functional support needs, not institutional placement phases."
        },
        "learningObjective": "Classify the DSM-5 severity levels of Autism Spectrum Disorder based on required support.",
        "reference": "American Psychiatric Association. (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed., DSM-5). APA.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q727",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Intermediate",
        "questionText": "A 7-year-old autistic boy becomes intensely distressed, screaming and covering his ears, whenever the school cafeteria fluorescent lights flicker or when the hand dryer is activated in the restroom. How should the mental health nurse explain this sensory phenomenon to the teaching staff?",
        "options": [
            {"id": "A", "text": "Sensory hyper-reactivity (hypersensitivity), where normal auditory and visual sensory inputs are perceived with painful, overwhelming neurological intensity"},
            {"id": "B", "text": "Intentional malingering to gain extra playtime outdoors"},
            {"id": "C", "text": "A severe conduct disorder requiring corporal discipline"},
            {"id": "D", "text": "An auditory hallucination originating from temporal lobe epilepsy"}
        ],
        "correctAnswer": "A",
        "explanation": "Sensory processing differences are explicitly codified in DSM-5 criterion B4 of ASD. Sensory hyper-reactivity involves atypical neurological processing where ordinary environmental stimuli (fluorescent light humming/flickering, hand dryers, clothing tags) register as excruciatingly loud, bright, or painful, triggering fight-or-flight panic.",
        "incorrectExplanations": {
            "B": "Sensory distress is an involuntary neurological response, not deceptive malingering.",
            "C": "Punishing a child for sensory pain causes severe psychological trauma and escalates distress.",
            "D": "Physical auditory stimuli trigger the response, not internal epileptic hallucinations."
        },
        "learningObjective": "Analyze sensory processing sensitivities (hyper- and hypo-reactivity) in individuals with ASD.",
        "reference": "Bogdashina, O. (2016). Sensory Perceptual Issues in Autism and Asperger Syndrome (2nd ed.). Jessica Kingsley Publishers.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q728",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Intermediate",
        "questionText": "A 14-year-old autistic adolescent is admitted to an acute adolescent mental health ward. What environmental and procedural adaptations should the nursing team implement to provide an autism-friendly clinical encounter?",
        "options": [
            {"id": "A", "text": "Place the patient in the center of the loudest day room and enforce direct prolonged eye contact"},
            {"id": "B", "text": "Conduct surprise unannounced physical examinations at random intervals during the night"},
            {"id": "C", "text": "Provide a low-stimulus environment (dimmable lighting, low noise), use visual schedules and social stories explaining routines, avoid unexpected physical touch, and allow familiar comfort objects"},
            {"id": "D", "text": "Deprive the adolescent of their comfort items until they converse fluently in complex metaphors"}
        ],
        "correctAnswer": "C",
        "explanation": "Reasonable clinical adjustments for autistic patients include reducing sensory overload (dimming lights, minimizing noise, quiet rooms), establishing predictability through written or visual schedules, preparing them for transitions with social stories, asking permission before touching, and welcoming sensory soothing items.",
        "incorrectExplanations": {
            "A": "Forcing eye contact and loud environments induces intense sensory stress and autonomic exhaustion.",
            "B": "Surprise procedures violate need for sameness and induce severe panic.",
            "D": "Withholding comfort items is punitive and exacerbates sensory dysregulation."
        },
        "learningObjective": "Implement environmental and communication adaptations to optimize healthcare encounters for autistic service users.",
        "reference": "NICE. (2012). Autism spectrum disorder in under 19s: recognition, referral and diagnosis (NICE Guideline CG128).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q729",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Intermediate",
        "questionText": "When communicating verbally with an autistic child or young person during a psychiatric evaluation, which linguistic approach is most clinically effective?",
        "options": [
            {"id": "A", "text": "Using sarcasm, rhetorical irony, and abstract metaphors to test their imagination"},
            {"id": "B", "text": "Using clear, concrete, literal language, allowing extra processing time (e.g. 10-15 seconds) before repeating questions, and avoiding idioms like 'pull your socks up' or 'it's raining cats and dogs'"},
            {"id": "C", "text": "Speaking at maximum volume while making rapid, complex gestures"},
            {"id": "D", "text": "Asking five multi-part questions simultaneously without pausing"}
        ],
        "correctAnswer": "B",
        "explanation": "Autistic individuals process communication literally and may misinterpret metaphors, idioms, irony, or sarcasm. Effective clinical communication requires concise, unambiguous, literal wording, breaking instructions into single steps, avoiding abstract colloquialisms, and providing ample cognitive processing time.",
        "incorrectExplanations": {
            "A": "Sarcasm and metaphors induce confusion and anxiety due to literal interpretation styles.",
            "C": "Shouting and rapid gesturing cause sensory overload and alarm.",
            "D": "Multi-part questions exceed receptive processing capacity."
        },
        "learningObjective": "Demonstrate effective verbal and linguistic communication strategies tailored to autistic cognitive processing.",
        "reference": "Attwood, T. (2007). The Complete Guide to Asperger's Syndrome. Jessica Kingsley Publishers.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q730",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Intermediate",
        "questionText": "An 8-year-old non-speaking autistic child suddenly begins banging his head against the wall, grimacing, refusing solid foods, and weeping. The child cannot verbally articulate what is wrong. What must the nurse prioritize during the clinical assessment?",
        "options": [
            {"id": "A", "text": "Prescribe high-dose oral neuroleptics assuming this is purely psychological psychosis"},
            {"id": "B", "text": "Assume the child is throwing a deliberate tantrum and leave him in isolation"},
            {"id": "C", "text": "Physically restrain the child for 24 hours without medical examination"},
            {"id": "D", "text": "Conduct a thorough physical examination to identify acute occult somatic pain (such as a severe dental abscess, otitis media, or gastroesophageal reflux) using behavioural pain assessment tools"}
        ],
        "correctAnswer": "D",
        "explanation": "In non-speaking or minimally verbal individuals with ASD, acute somatic pain (dental caries, ear infections, constipation, appendicitis, bone fractures) frequently manifests as sudden behavioral change: self-injury (head-banging), aggression, food refusal, or crying. Clinicians must rule out acute physical pain before considering psychiatric etiologies.",
        "incorrectExplanations": {
            "A": "Sedating a child with antipsychotics masks physical illness and risks fatal sepsis or bowel perforation.",
            "B": "Dismissing acute distress as a tantrum neglects potentially serious physical disease.",
            "C": "Restraint without medical assessment is dangerous and abusive."
        },
        "learningObjective": "Identify behavioral indicators of acute somatic pain in non-verbal individuals with Autism Spectrum Disorder.",
        "reference": "Courtemanche, A. B., et al. (2012). Gastrointestinal symptoms and self-injurious behaviour in autism: A systematic review. Journal of Autism and Developmental Disorders, 42(6), 1182-1193.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q731",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Advanced",
        "questionText": "How does an 'Autistic Sensory Meltdown' differ clinically and neurobiologically from a typical childhood behavioural temper tantrum?",
        "options": [
            {"id": "A", "text": "A meltdown is an intentional manipulation used to win arguments, whereas a tantrum is purely biological"},
            {"id": "B", "text": "A meltdown is an involuntary, overwhelmed neurological response to sensory or cognitive overload where executive control collapses, occurring regardless of an audience; a tantrum is goal-directed, ceases when the desired object is granted, and requires an audience"},
            {"id": "C", "text": "There are no differences; both should be treated with immediate physical punishment"},
            {"id": "D", "text": "A meltdown occurs only in adults, whereas tantrums occur only in infants"}
        ],
        "correctAnswer": "B",
        "explanation": "A tantrum is operant, goal-directed behavior designed to achieve a specific reinforcer (e.g., a toy or candy); it typically stops once the demand is met. An autistic meltdown is an involuntary autonomic fight-or-flight crisis triggered by neurological overload. The individual has lost emotional control, safety is compromised, and meeting demands will not abort the episode.",
        "incorrectExplanations": {
            "A": "Meltdowns are completely involuntary and non-manipulative.",
            "C": "Physical punishment is unethical, abusive, and ineffective.",
            "D": "Autistic meltdowns occur across the lifespan from early childhood through adulthood."
        },
        "learningObjective": "Differentiate an autistic sensory meltdown from a behavioral temper tantrum to guide appropriate de-escalation.",
        "reference": "Lipsky, D. (2011). From Anxiety to Meltdown: How Individuals on the Autism Spectrum Deal with Anxiety. Jessica Kingsley Publishers.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q732",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Advanced",
        "questionText": "A 10-year-old child with ASD displays severe, intractable physical aggression and self-injurious biting that has caused severe soft-tissue trauma and resisted all behavioural interventions. The child and adolescent psychiatrist considers pharmacotherapy. Which medications have formal regulatory (FDA/NICE) approval specifically for managing severe irritability and aggression associated with autism in children?",
        "options": [
            {"id": "A", "text": "Intravenous morphine and high-dose barbiturates"},
            {"id": "B", "text": "High-dose tricyclic antidepressants and ketamine infusions"},
            {"id": "C", "text": "Penicillin and high-dose ascorbic acid"},
            {"id": "D", "text": "Atypical antipsychotics: Risperidone and Aripiprazole"}
        ],
        "correctAnswer": "D",
        "explanation": "Risperidone and Aripiprazole are the only two psychopharmacological agents with FDA and international regulatory approvals for treating severe irritability, physical aggression, and self-injurious behavior associated with autistic disorder in children and adolescents. They do not treat core social-communication deficits.",
        "incorrectExplanations": {
            "A": "Opioids and barbiturates carry severe respiratory depression and addiction risks without efficacy for autism.",
            "B": "TCAs carry high cardiotoxicity risks and lack evidence for irritability in ASD.",
            "C": "Antibiotics and vitamins have no therapeutic role in managing acute psychiatric aggression."
        },
        "learningObjective": "Identify evidence-based and approved psychopharmacological treatments for severe irritability in paediatric autism.",
        "reference": "Scahill, L., et al. (2015). Psychopharmacology in children and adolescents with autism spectrum disorder. Child and Adolescent Psychiatric Clinics, 24(1), 83-97.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q733",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Advanced",
        "questionText": "An autistic young person is brought to an emergency department with severe acute abdominal distension, vomiting, and extreme distress. A triage nurse remarks: 'He is just exhibiting autistic vocalizations and rocking; that's normal for him,' and delays medical triage. What dangerous clinical cognitive error has occurred?",
        "options": [
            {"id": "A", "text": "Diagnostic overshadowing, where severe acute surgical pathology (e.g. bowel obstruction or peritonitis) is erroneously attributed to the neurodevelopmental diagnosis"},
            {"id": "B", "text": "Exemplary trauma-informed psychiatric triage"},
            {"id": "C", "text": "Factitious somatoform projection"},
            {"id": "D", "text": "Appropriate behavioral extinction protocol"}
        ],
        "correctAnswer": "A",
        "explanation": "Diagnostic overshadowing is a major contributor to premature morbidity and mortality in autistic individuals. Healthcare providers frequently misattribute signs of acute physical illness (e.g. abdominal surgical emergencies, bowel impaction) to 'autistic behaviors,' resulting in catastrophic diagnostic delays.",
        "incorrectExplanations": {
            "B": "Dismissing signs of bowel obstruction is medical neglect, not trauma-informed care.",
            "C": "The patient has objective physical signs (vomiting, distension), not factitious disorder.",
            "D": "Ignoring acute surgical symptoms is dangerous and breaches the duty of care."
        },
        "learningObjective": "Analyze and prevent diagnostic overshadowing when evaluating acute physical symptoms in autistic individuals.",
        "reference": "Mason, D., et al. (2019). Predictors of quality of life for autistic adults. Autism Research, 12(9), 1388-1397.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q734",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Autism Spectrum Disorder (ASD)",
        "difficulty": "Expert",
        "questionText": "A 16-year-old academically high-achieving female is referred for severe recurrent depression, chronic fatigue, and pervasive anxiety. During comprehensive developmental assessment, it is revealed that she has spent years consciously forcing eye contact, scripting social conversations from television shows, suppressing her natural repetitive movements ('stimming'), and enduring profound exhaustion after school. How should the clinical nurse specialist conceptualize this clinical picture?",
        "options": [
            {"id": "A", "text": "Malingering for secondary educational gain"},
            {"id": "B", "text": "Histrionic personality disorder with narcissistic features"},
            {"id": "C", "text": "Autistic 'Camouflaging' (masking), which is highly prevalent in autistic females and frequently leads to delayed diagnosis, severe chronic psychological distress, and 'autistic burnout'"},
            {"id": "D", "text": "Catatonic schizophrenia requiring emergency ECT"}
        ],
        "correctAnswer": "C",
        "explanation": "Camouflaging (or social masking) refers to strategies used by autistic individuals—predominantly females—to hide autistic traits and mimic neurotypical social behaviors. While it facilitates superficial social fitting-in, extensive masking carries immense cognitive and emotional costs, leading to late diagnosis, severe anxiety, depression, and 'autistic burnout.'",
        "incorrectExplanations": {
            "A": "Masking is a survival coping response, not deceptive malingering.",
            "B": "Personality disorder diagnoses often misdiagnose underlying unrecognized female autism profiles.",
            "D": "Social masking and subsequent exhaustion bear no resemblance to catatonia."
        },
        "learningObjective": "Critique the clinical presentation, gender disparities, and mental health consequences of autistic camouflaging (masking).",
        "reference": "Hull, L., et al. (2017). 'Putting on my best normal': Social camouflaging in adults with autism spectrum conditions. Journal of Autism and Developmental Disorders, 47(8), 2519-2534.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 3: Childhood anxiety and depression (MHN-Q735 - MHN-Q744)
    # Target Answers: A, C, B, D, A, C, B, A, D, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q735",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Foundation",
        "questionText": "In paediatric mental health nursing, how does the clinical presentation of Major Depressive Disorder in children and young adolescents differ most prominently from the typical presentation seen in adults?",
        "options": [
            {"id": "A", "text": "Children frequently present with irritable, cranky, or angry mood, unexplained somatic complaints (stomachaches/headaches), and failure to make expected developmental weight gains, rather than classic depressed verbalizations"},
            {"id": "B", "text": "Children with depression always experience acute continuous auditory hallucinations"},
            {"id": "C", "text": "Paediatric depression never involves sleep disturbance or changes in energy"},
            {"id": "D", "text": "Children always present with fluent, insightful philosophical monologues regarding existential nihilism"}
        ],
        "correctAnswer": "A",
        "explanation": "DSM-5 explicitly notes that in children and adolescents, depressive mood can present predominantly as persistent irritability, grouchiness, or explosive anger rather than overt sadness. Furthermore, somatic complaints (headaches, abdominal pain) and failure to make expected developmental weight gains are cardinal paediatric features.",
        "incorrectExplanations": {
            "B": "Hallucinations are rare and indicate psychotic depression, not universal paediatric depression.",
            "C": "Vegetative signs like sleep disturbance and fatigue are common in childhood depression.",
            "D": "Children rarely express abstract existential nihilism; distress is somatic and behavioural."
        },
        "learningObjective": "Identify unique developmental presentations of major depressive disorder in children compared to adults.",
        "reference": "American Psychiatric Association. (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed., DSM-5). APA.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q736",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Foundation",
        "questionText": "What distinguishes Emotionally Based School Avoidance (EBSA) / school refusal from antisocial truancy in school-aged children?",
        "options": [
            {"id": "A", "text": "In truancy, the child stays home with the full knowledge and consent of their parents"},
            {"id": "B", "text": "There are no clinical distinctions between school refusal and truancy"},
            {"id": "C", "text": "In school refusal, the child experiences severe emotional distress/panic about attending school and stays home with parents' knowledge without antisocial conduct; in truancy, the student skips school secretly without parental knowledge, often engaging in delinquent peer activities"},
            {"id": "D", "text": "School refusal occurs exclusively in children with criminal convictions"}
        ],
        "correctAnswer": "C",
        "explanation": "School refusal (EBSA) is driven by emotional distress (separation anxiety, social phobia, depression, sensory overload). The child remains at home with parental knowledge and shows no major antisocial behaviors. Truancy, by contrast, is covert, lacks anxiety/panic, occurs without parental awareness, and often accompanies antisocial behaviors.",
        "incorrectExplanations": {
            "A": "In truancy, parents are typically unaware their child has skipped school.",
            "B": "The clinical and psychological distinctions are well-established and dictate different treatment pathways.",
            "D": "School refusal is an internalizing anxiety disorder, not criminal delinquency."
        },
        "learningObjective": "Differentiate between emotionally based school avoidance (school refusal) and truancy.",
        "reference": "Heyne, D., et al. (2019). Differentiation between school attendance problems: Why and how? Cognitive and Behavioral Practice, 26(1), 8-34.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q737",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Foundation",
        "questionText": "A 7-year-old girl displays developmentally inappropriate, excessive panic whenever separated from her mother. She refuses to sleep alone, has nightmares about catastrophic harm befalling her parents, and complains of severe morning nausea on school days. What diagnosis is most consistent with this presentation?",
        "options": [
            {"id": "A", "text": "Schizoid personality disorder"},
            {"id": "B", "text": "Separation Anxiety Disorder"},
            {"id": "C", "text": "Conduct disorder, adolescent onset"},
            {"id": "D", "text": "Bipolar I mania with psychotic features"}
        ],
        "correctAnswer": "B",
        "explanation": "Separation Anxiety Disorder in DSM-5 requires developmentally inappropriate and excessive anxiety concerning separation from attachment figures, evidenced by recurrent distress upon separation, persistent worry about harm to attachment figures, reluctance to go to school or sleep alone, and anticipatory somatic complaints.",
        "incorrectExplanations": {
            "A": "Schizoid personality involves detachment from social relationships, the opposite of clingy attachment anxiety.",
            "C": "Conduct disorder involves violating rights of others, not anxiety-driven separation panic.",
            "D": "There is no elevated mood, grandiosity, or hyperactivity to suggest bipolar mania."
        },
        "learningObjective": "Recognize the clinical criteria and presentation of Separation Anxiety Disorder in childhood.",
        "reference": "American Psychiatric Association. (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed., DSM-5). APA.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q738",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Intermediate",
        "questionText": "An 8-year-old boy presents with sudden, explosive onset of severe obsessive-compulsive rituals, motor tics, and emotional lability following a severe sore throat 10 days earlier. Which paediatric autoimmune condition must the mental health nurse consider, and what is the standard psychological treatment for paediatric OCD?",
        "options": [
            {"id": "A", "text": "Huntington's chorea; treated with immediate frontal lobotomy"},
            {"id": "B", "text": "Wernicke encephalopathy; treated with parenteral thiamine only"},
            {"id": "C", "text": "Temporal lobe epilepsy; treated with chronic carbamazepine monotherapy"},
            {"id": "D", "text": "PANDAS (Paediatric Autoimmune Neuropsychiatric Disorders Associated with Streptococcal Infections); while standard paediatric OCD is treated with Exposure and Response Prevention (ERP)"}
        ],
        "correctAnswer": "D",
        "explanation": "PANDAS / PANS describes acute-onset paediatric OCD or tics linked to post-streptococcal autoimmune basal ganglia inflammation. Across all paediatric OCD, Exposure and Response Prevention (ERP)—a specialized form of CBT where the child confronts triggers while resisting compulsions—is the first-line evidence-based psychological treatment.",
        "incorrectExplanations": {
            "A": "Huntington's is an adult-onset autosomal dominant genetic disease, and lobotomy is obsolete.",
            "B": "Wernicke's results from thiamine deficiency in chronic alcohol use, not paediatric post-strep infections.",
            "C": "Sudden post-streptococcal tics and OCD are autoimmune phenomena, not epilepsy."
        },
        "learningObjective": "Identify PANDAS/PANS clinical presentations and identify Exposure and Response Prevention (ERP) as gold-standard psychotherapy for paediatric OCD.",
        "reference": "Swedo, S. E., et al. (1998). Pediatric autoimmune neuropsychiatric disorders associated with streptococcal infections: Clinical description of the first 50 cases. American Journal of Psychiatry, 155(2), 264-271.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q739",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Intermediate",
        "questionText": "When considering antidepressant pharmacotherapy for moderate to severe major depressive disorder in children and adolescents (under 18), which SSRI has the most robust evidence base and is recognized by NICE and the FDA as the first-line medication of choice?",
        "options": [
            {"id": "A", "text": "Fluoxetine"},
            {"id": "B", "text": "Paroxetine"},
            {"id": "C", "text": "Amitriptyline"},
            {"id": "D", "text": "Phenelzine"}
        ],
        "correctAnswer": "A",
        "explanation": "Fluoxetine is the only antidepressant consistently demonstrated in multiple clinical trials to have a favorable risk-benefit profile for treating moderate to severe depression in children and adolescents (aged 8-18). It is the first-line agent recommended by NICE (NG134) and FDA-approved for youth depression, always combined with psychological therapy.",
        "incorrectExplanations": {
            "B": "Paroxetine has poor efficacy and carries an unacceptably high risk of suicidal ideation in young people; it is contraindicated.",
            "C": "Amitriptyline is a cardiotoxic tricyclic antidepressant with no demonstrated efficacy in paediatric depression.",
            "D": "Phenelzine is an MAOI carrying severe dietary restrictions and toxicity risks."
        },
        "learningObjective": "Select evidence-based antidepressant pharmacotherapy for paediatric depression based on clinical guidelines.",
        "reference": "NICE. (2019). Depression in children and young people: identification and management (NICE Guideline NG134).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q740",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Intermediate",
        "questionText": "In 2004, regulatory agencies (FDA and MHRA) issued a 'Black Box Warning' for all antidepressant medications prescribed to children, adolescents, and young adults up to age 24. What specific risk does this warning articulate, and what monitoring protocol is mandated?",
        "options": [
            {"id": "A", "text": "Immediate permanent blindness; patients must undergo weekly ophthalmology retinal scans"},
            {"id": "B", "text": "Irreversible renal necrosis occurring within 48 hours of ingestion"},
            {"id": "C", "text": "A small statistically significant increased risk of suicidal thoughts and behaviors (approximately 4% vs 2% on placebo) during the initial weeks of treatment, mandating close weekly clinical review during the first month"},
            {"id": "D", "text": "Rapid bone demineralization requiring full skeletal traction"}
        ],
        "correctAnswer": "C",
        "explanation": "Meta-analyses of paediatric trials identified a small increased risk of emergent suicidal ideation and behaviors (approx. 4% in drug-treated vs 2% in placebo) in youths taking antidepressants. The Black Box warning mandates alerting families and conducting close clinical monitoring—especially weekly during the first 4 weeks of therapy or following dose titrations.",
        "incorrectExplanations": {
            "A": "Antidepressants do not cause blindness or require retinal monitoring.",
            "B": "SSRIs are not nephrotoxic compounds causing acute renal necrosis.",
            "D": "Bone demineralization is not the subject of the black box suicidality warning."
        },
        "learningObjective": "Explain the regulatory rationale, statistical parameters, and clinical monitoring mandates of the antidepressant Black Box Warning in youth.",
        "reference": "Bridge, J. A., et al. (2007). Clinical response and risk for reported suicidal ideation and suicide attempts in pediatric antidepressant trials. JAMA, 297(15), 1683-1696.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q741",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Advanced",
        "questionText": "A child psychiatric nurse is conducting adapted Cognitive Behavioural Therapy (CBT) for a 9-year-old child using the manualized 'Coping Cat' program (Kendall). Which therapeutic technique exemplifies developmentally adapted paediatric CBT?",
        "options": [
            {"id": "A", "text": "Conducting silent adult psychoanalysis with the child lying on a couch for 50 minutes"},
            {"id": "B", "text": "Teaching somatic recognition of anxiety (the 'FEAR' plan), externalizing anxiety as a distinct character (e.g. the 'Worry Bully'), using feelings thermometers to grade distress, and practicing gradual exposure hierarchies"},
            {"id": "C", "text": "Administering severe electrical shocks whenever the child expresses fear"},
            {"id": "D", "text": "Instructing the child to write a 300-page academic thesis on neurotransmitters"}
        ],
        "correctAnswer": "B",
        "explanation": "Adapted paediatric CBT (like Philip Kendall's Coping Cat) uses developmentally accessible concepts: somatic awareness (FEAR plan: Feeling frightened, Expecting bad things, Attitudes/actions that help, Results/rewards), externalizing worry ('Worry Monster'), visual feelings thermometers (0-10 scale), and fun, collaborative graded exposure challenges.",
        "incorrectExplanations": {
            "A": "Silent psychoanalysis is developmentally inappropriate and ineffective for young children.",
            "C": "Aversive electric shocks are unethical, abusive, and obsolete.",
            "D": "Writing academic theses is developmentally impossible for an anxious 9-year-old."
        },
        "learningObjective": "Apply developmentally tailored Cognitive Behavioural Therapy techniques (e.g., Coping Cat) for childhood anxiety.",
        "reference": "Kendall, P. C., & Hedtke, K. A. (2006). Cognitive-Behavioral Therapy for Anxious Children: Therapist Manual (3rd ed.). Workbook Publishing.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q742",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Advanced",
        "questionText": "The parents of an 11-year-old with severe generalized anxiety disorder report that they answer the child's repetitive reassurance questions ('Are you sure I won't get sick?') up to 50 times an hour, check his backpack five times every morning, and sleep in his bed every night to prevent panic. What clinical phenomenon is occurring, and how should the nurse intervene?",
        "options": [
            {"id": "A", "text": "Family Accommodation; the nurse should utilize programs like SPACE (Supportive Parenting for Anxious Childhood Emotions) to train parents to systematically reduce accommodations while providing emotional validation"},
            {"id": "B", "text": "Exemplary parenting that should be doubled in frequency to eliminate all anxiety"},
            {"id": "C", "text": "Munchausen syndrome by proxy requiring immediate removal by police"},
            {"id": "D", "text": "Parental malingering requiring prosecution"}
        ],
        "correctAnswer": "A",
        "explanation": "Family accommodation occurs when caregivers modify their routines, provide endless reassurance, or facilitate avoidance to reduce the child's distress. While well-intentioned, accommodation maintains and worsens anxiety over time. Evidence-based interventions like SPACE (Lebowitz) train parents to systematically reduce accommodations while maintaining warmth and support.",
        "incorrectExplanations": {
            "B": "Excessive accommodation reinforces anxiety and prevents the child from developing distress tolerance.",
            "C": "Family accommodation is an anxiety maintenance cycle, completely distinct from factitious illness fabrication.",
            "D": "Caregivers are seeking to relieve distress, not engaging in criminal malingering."
        },
        "learningObjective": "Analyze family accommodation dynamics in childhood anxiety and implement parent-based reduction interventions (SPACE).",
        "reference": "Lebowitz, E. R., et al. (2020). Parent-based treatment for childhood anxiety disorders: A randomized controlled trial. Journal of the American Academy of Child & Adolescent Psychiatry, 59(7), 828-838.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q743",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Advanced",
        "questionText": "A 6-year-old girl speaks fluently, animatedly, and normally at home with her parents and siblings. However, since entering primary school 8 months ago, she has never spoken a single word to her teacher, classmates, or school staff, communicating only through nodding. There is no speech or language deficit. What condition does this child exhibit, and what behavioural intervention is indicated?",
        "options": [
            {"id": "A", "text": "Severe receptive aphasia; requiring neurosurgical deep brain stimulation"},
            {"id": "B", "text": "Deliberate hostile oppositional mutism; requiring punitive detention"},
            {"id": "C", "text": "Childhood disintegrative disorder with catatonia"},
            {"id": "D", "text": "Selective Mutism; treated using behavioural techniques including stimulus fading, shaping, and graded exposure in the school setting"}
        ],
        "correctAnswer": "D",
        "explanation": "Selective Mutism is a severe childhood anxiety disorder characterized by a consistent failure to speak in specific social situations (e.g. school) where there is an expectation to speak, despite speaking in other settings (e.g. home). It impairs educational and social functioning. First-line treatments are behavioural interventions: stimulus fading, shaping, and systematic desensitization.",
        "incorrectExplanations": {
            "A": "Fluent speech at home rules out receptive aphasia; surgery is completely unwarranted.",
            "B": "Selective mutism is an anxiety-based condition, not a willful oppositional act.",
            "C": "Language is preserved, ruling out neurodegenerative disintegrative disorder."
        },
        "learningObjective": "Diagnose Selective Mutism and formulate behavioural stimulus-fading interventions in educational settings.",
        "reference": "Cohan, S. L., et al. (2006). Refining the classification of children with selective mutism: A latent profile analysis. Journal of Clinical Child and Adolescent Psychology, 35(4), 570-581.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q744",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Childhood anxiety and depression",
        "difficulty": "Expert",
        "questionText": "A 13-year-old adolescent with severe major depression and active suicidal ideation is being discharged home following emergency crisis stabilization. When formulating the lethal means restriction component of the collaborative safety plan with the adolescent and caregivers, what specific environmental interventions must the nurse verify?",
        "options": [
            {"id": "A", "text": "Requesting the adolescent sign a non-suicide contract and trusting their word without altering the home"},
            {"id": "B", "text": "Leaving medications out on the counter to demonstrate trust in the adolescent"},
            {"id": "C", "text": "Ensuring all household prescription and over-the-counter medications (especially paracetamol/acetaminophen) are locked in a secure lockbox with the code known only to parents, removing/locking all firearms, securing sharp implements, and eliminating ligature points where feasible"},
            {"id": "D", "text": "Advising the parents that lethal means restriction has no evidence for preventing suicide"}
        ],
        "correctAnswer": "C",
        "explanation": "Lethal means restriction is one of the most effective, empirically validated suicide prevention strategies. In youth crisis safety planning, nurses mandate that parents secure all household medications (including lethal OTC drugs like paracetamol) in a locked safe, remove or trigger-lock firearms, secure sharp objects, and minimize lethal means in the home.",
        "incorrectExplanations": {
            "A": "'Contracts for safety' have no empirical evidence and create a false sense of security.",
            "B": "Leaving lethal medications accessible during an acute depressive crisis invites impulsive fatal overdose.",
            "D": "Epidemiological research unequivocally proves restricting lethal means saves lives."
        },
        "learningObjective": "Execute comprehensive lethal means restriction and environmental safety planning for depressed paediatric patients.",
        "reference": "Brent, D. A., et al. (2013). Protecting youth from suicide: Lethal means restriction. Journal of the American Academy of Child & Adolescent Psychiatry, 52(9), 896-898.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 4: Adolescent risk-taking and self-harm (MHN-Q745 - MHN-Q754)
    # Target Answers: B, D, A, C, B, D, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q745",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Foundation",
        "questionText": "How is Non-Suicidal Self-Injury (NSSI) defined in clinical psychiatric mental health nursing, and what is its most common psychological function?",
        "options": [
            {"id": "A", "text": "An accidental physical injury sustained during athletic sports"},
            {"id": "B", "text": "The direct, deliberate destruction of body tissue (most commonly cutting, burning, or scratching) without suicidal intent, most frequently utilized as a maladaptive strategy to regulate unbearable negative affect or relieve emotional numbness"},
            {"id": "C", "text": "A calculated political demonstration to protest government taxation"},
            {"id": "D", "text": "A surgical procedure performed by licensed plastic surgeons"}
        ],
        "correctAnswer": "B",
        "explanation": "Non-Suicidal Self-Injury (NSSI) involves deliberate, direct destruction of body tissue (e.g. cutting, burning, severe scratching) in the absence of lethal intent. Research shows its primary function is affect regulation: reducing overwhelming distress, alleviating severe emotional pain, terminating dissociative numbness, or self-punishment.",
        "incorrectExplanations": {
            "A": "Accidental athletic trauma lacks intentional self-directed injury.",
            "C": "NSSI is an intrapersonal emotional coping mechanism, not political protest.",
            "D": "Plastic surgery is legitimate medical treatment, completely distinct from self-injury."
        },
        "learningObjective": "Define Non-Suicidal Self-Injury (NSSI) and explain its primary psychological and emotion-regulation functions.",
        "reference": "Nock, M. K. (2009). Why do people hurt themselves? New insights into the nature and functions of self-injury. Current Directions in Psychological Science, 18(2), 78-83.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q746",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Foundation",
        "questionText": "When conducting a clinical assessment of an adolescent who presents with superficial forearm lacerations, which critical feature distinguishes Non-Suicidal Self-Injury (NSSI) from a genuine suicide attempt?",
        "options": [
            {"id": "A", "text": "The patient's age and grade level in secondary school"},
            {"id": "B", "text": "Whether the patient has health insurance coverage"},
            {"id": "C", "text": "The time of day the clinical assessment takes place"},
            {"id": "D", "text": "The presence or absence of explicit or implicit intent to die as an outcome of the act"}
        ],
        "correctAnswer": "D",
        "explanation": "The fundamental distinction between NSSI and a suicide attempt is the person's intent. In NSSI, the individual hurts themselves to cope with life, regulate affect, or feel relief—with no desire to end their life. In a suicide attempt, there is at least some intent (explicit or implicit) to die as a consequence of the act.",
        "incorrectExplanations": {
            "A": "Age does not differentiate intent; both NSSI and suicide attempts occur across adolescence.",
            "B": "Insurance status is an administrative metric with no diagnostic bearing on intent.",
            "C": "Time of presentation does not differentiate suicidal intent from non-suicidal affect regulation."
        },
        "learningObjective": "Differentiate Non-Suicidal Self-Injury from a suicide attempt based on intent, expectation, and clinical features.",
        "reference": "Silverman, M. M., et al. (2007). Rebuilding the Tower of Babel: a revised nomenclature for the study of suicide and suicidal behaviors. Part 2: Suicide-related ideations, communications, and behaviors. Suicide and Life-Threatening Behavior, 37(3), 264-277.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q747",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Intermediate",
        "questionText": "A 15-year-old adolescent presents to a school mental health clinic with self-inflicted linear cuts on both forearms. Which clinical assessment battery must the psychiatric nurse systematically conduct?",
        "options": [
            {"id": "A", "text": "Examine physical wound depth and infection risk, evaluate the psychological intent/function of the behavior, screen for active suicidal ideation and lethal plans, assess co-occurring substance use and mood disorders, and explore peer/social media influences"},
            {"id": "B", "text": "Administer an intelligence IQ test and conduct an immediate hearing exam"},
            {"id": "C", "text": "Instruct the adolescent to sign an agreement promising never to feel sad again"},
            {"id": "D", "text": "Photograph the cuts and broadcast them to the entire school assembly as a warning"}
        ],
        "correctAnswer": "A",
        "explanation": "Comprehensive self-harm assessment requires a multidimensional evaluation: assessing medical wound acuity and infection, clarifying intent (suicidal vs non-suicidal), exploring emotional triggers, screening for concurrent depression or trauma, assessing substance use, evaluating digital/online peer contagion, and identifying strengths.",
        "incorrectExplanations": {
            "B": "IQ and hearing tests do not assess acute psychiatric risk or wound safety.",
            "C": "Promising never to feel sad is impossible and invalidating.",
            "D": "Broadcasting images breaches confidentiality, induces public humiliation, and causes self-harm contagion."
        },
        "learningObjective": "Conduct a multidimensional psychiatric nursing assessment of adolescent self-harm and concurrent suicide risk.",
        "reference": "NICE. (2022). Self-harm: assessment, management and preventing recurrence (NICE Guideline NG225).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q748",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Intermediate",
        "questionText": "Dialectical Behaviour Therapy for Adolescents (DBT-A), adapted by Alec Miller and Jill Rathus from Marsha Linehan's model, is an established evidence-based treatment for chronic adolescent self-harm and emotional dysregulation. What five core skills modules are taught in DBT-A?",
        "options": [
            {"id": "A", "text": "Hypnosis, Dream Interpretation, Free Association, Regressive Analysis, and Catharsis"},
            {"id": "B", "text": "Dieting, Marathon Running, Weightlifting, Calisthenics, and Yoga"},
            {"id": "C", "text": "Mindfulness, Distress Tolerance, Emotion Regulation, Interpersonal Effectiveness, and Walking the Middle Path"},
            {"id": "D", "text": "Spelling, Arithmetic, World Geography, Chemistry, and Geometry"}
        ],
        "correctAnswer": "C",
        "explanation": "DBT-A includes the four standard adult DBT skills modules—Mindfulness, Distress Tolerance, Emotion Regulation, and Interpersonal Effectiveness—plus a specialized fifth module designed for youth and caregivers: 'Walking the Middle Path', which addresses family dialectical dilemmas, validation, and behavioral change principles.",
        "incorrectExplanations": {
            "A": "These are psychoanalytic techniques, not skills-based dialectical behavioural therapy.",
            "B": "These are physical athletic disciplines unrelated to DBT-A skill modules.",
            "D": "Academic classroom subjects are not psychotherapeutic emotion-regulation modules."
        },
        "learningObjective": "Identify the five core skills modules comprising Dialectical Behaviour Therapy for Adolescents (DBT-A).",
        "reference": "Miller, A. L., Rathus, J. H., & Linehan, M. M. (2007). Dialectical Behavior Therapy with Suicidal Adolescents. Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q749",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Intermediate",
        "questionText": "In DBT-A, the nurse helps families navigate 'Dialectical Dilemmas'. Which of the following represents a classic dialectical dilemma frequently encountered between adolescents experiencing severe emotional dysregulation and their parents?",
        "options": [
            {"id": "A", "text": "Deciding between taking a bus or a train to school"},
            {"id": "B", "text": "Excessive leniency versus authoritarian control, and normalizing pathological behaviors versus invalidating typical adolescent emotions"},
            {"id": "C", "text": "Choosing between eating vanilla or chocolate ice cream"},
            {"id": "D", "text": "Debating whether to paint the clinical office blue or green"}
        ],
        "correctAnswer": "B",
        "explanation": "DBT-A identifies three primary family dialectical polarities: 1) Excessive Leniency vs Authoritarian Control, 2) Normalizing Pathological Behaviors vs Overpathologizing/Invalidating Normal Adolescent Emotions, and 3) Fostering Dependence vs Forcing Premature Autonomy. Finding synthesis ('walking the middle path') is the therapeutic goal.",
        "incorrectExplanations": {
            "A": "Transportation choices are simple practical decisions, not clinical dialectical dilemmas.",
            "C": "Food flavors represent trivial personal preferences.",
            "D": "Interior decorating has no connection to dialectical family dilemmas."
        },
        "learningObjective": "Analyze dialectical dilemmas and family polarities in adolescent emotional dysregulation.",
        "reference": "Rathus, J. H., & Miller, A. L. (2014). DBT Skills Manual for Adolescents. Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q750",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Intermediate",
        "questionText": "An adolescent who engages in repetitive cutting states: 'I feel an overwhelming urge to cut tonight, and nothing can stop me.' When applying harm-minimization and distress tolerance techniques (such as DBT TIPP skills or substitution), what should the nurse advise?",
        "options": [
            {"id": "A", "text": "Encourage the adolescent to immediately cut as deeply as possible to get it over with"},
            {"id": "B", "text": "Advise the adolescent to consume high doses of unprescribed sedatives"},
            {"id": "C", "text": "Instruct parents to handcuff the adolescent to a radiator for the night"},
            {"id": "D", "text": "Utilize Temperature change (holding an ice cube tightly or splashing icy water on the face), intense exercise for 60 seconds, paced breathing, or delayed cutting (waiting 15 minutes while using a sensory alternative like snapping a rubber band or drawing on the skin with a red marker)"}
        ],
        "correctAnswer": "D",
        "explanation": "DBT Distress Tolerance TIPP skills (Temperature, Intense exercise, Paced breathing, Paired muscle relaxation) rapidly activate the parasympathetic nervous system via the dive reflex, reducing acute autonomic hyper-arousal. Harm minimization substitutions (ice cubes, red marker, rubber band snapping, delaying tactics) provide sensory grounding without physical tissue damage.",
        "incorrectExplanations": {
            "A": "Encouraging deep lacerations is dangerous malpractice that risks catastrophic hemorrhage.",
            "B": "Recommending unprescribed sedatives promotes substance misuse and overdose.",
            "C": "Handcuffing is abusive, illegal, and causes severe psychological trauma."
        },
        "learningObjective": "Apply DBT distress tolerance (TIPP skills) and harm-reduction strategies for acute self-harm urges.",
        "reference": "Linehan, M. M. (2015). DBT Skills Training Manual (2nd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q751",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Advanced",
        "questionText": "Developmental cognitive neuroscience explains adolescent sensation-seeking and risk-taking through the 'Dual Systems' (maturational mismatch) model. How does this neurodevelopmental model explain high-risk behaviors in teenagers?",
        "options": [
            {"id": "A", "text": "Adolescents have completely fully matured brains identical to 40-year-olds at age 12"},
            {"id": "B", "text": "The socioemotional and reward-seeking limbic system (ventral striatum, amygdala) matures rapidly during puberty under gonadal hormone surges, while the cognitive control network (prefrontal cortex) responsible for impulse regulation and future planning undergoes protracted development until the mid-20s"},
            {"id": "C", "text": "Adolescent brains lack an amygdala entirely until age 21"},
            {"id": "D", "text": "Risk-taking is caused entirely by an acute allergic reaction to school textbooks"}
        ],
        "correctAnswer": "B",
        "explanation": "The Dual Systems Model (Steinberg) posits a neurodevelopmental timing mismatch: the subcortical socioemotional system matures early around puberty, producing high reward sensitivity, dopamine reactivity, and sensation seeking. In contrast, the prefrontal cortical systems governing executive function, impulse inhibition, and risk evaluation mature gradually into early adulthood (mid-20s).",
        "incorrectExplanations": {
            "A": "Prefrontal synaptic pruning and myelination continue well past adolescence into early adulthood.",
            "C": "The amygdala is present at birth and hyper-reactive during puberty.",
            "D": "Textbook allergies are a fictional absurdity."
        },
        "learningObjective": "Explain the neurodevelopmental basis of adolescent risk-taking using the Dual Systems / Maturational Mismatch model.",
        "reference": "Steinberg, L. (2010). A dual-systems model of adolescent risk-taking. Developmental Psychobiology, 52(3), 216-224.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q752",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Advanced",
        "questionText": "A 14-year-old adolescent discloses belonging to an online messaging group where members share graphic images of self-injury, exchange cutting techniques, and encourage each other to hide injuries from parents. How should the mental health nurse address this digital environment?",
        "options": [
            {"id": "A", "text": "Immediately confiscate and destroy the smartphone in front of the adolescent without discussion"},
            {"id": "B", "text": "Tell the adolescent that everything on the internet is harmless fiction and ignore the disclosure"},
            {"id": "C", "text": "Join the group anonymously to post sarcastic comments"},
            {"id": "D", "text": "Collaboratively explore the social contagion and triggering effects of the online group, formulate a digital safety plan, educate parents on supportive digital monitoring rather than punitive isolation, and support the youth in disconnecting from toxic forums while finding healthy peer connections"}
        ],
        "correctAnswer": "D",
        "explanation": "Online self-harm contagion and algorithmic echo chambers can normalize self-harm and escalate lethality. Punitive confiscation often alienates the youth and removes their broader social lifeline. Best practice entails collaborative digital safety planning: discussing triggers, helping the youth curate healthy digital boundaries, and involving parents supportively.",
        "incorrectExplanations": {
            "A": "Punitive destruction of phones destroys clinical rapport and drives digital self-harm underground.",
            "B": "Online self-harm forums present significant documented risks of contagion, escalation, and suicide pacts.",
            "C": "Mocking online users is unethical and unprofessional."
        },
        "learningObjective": "Formulate clinical nursing interventions and digital safety plans addressing online self-harm contagion.",
        "reference": "Daine, K., et al. (2013). The power of the web: A systematic review of studies of the influence of the internet on self-harm and suicide in young people. PLOS ONE, 8(10), e77555.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q753",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Advanced",
        "questionText": "An adolescent reveals fresh, bleeding self-harm cuts to an inpatient psychiatric nurse on evening shift. What is the nurse's optimal therapeutic and emotional response?",
        "options": [
            {"id": "A", "text": "Maintain a calm, compassionate, non-judgmental demeanor, attend to the physical wound cleansing and medical dressings first, explore the preceding emotional triggers gently, and avoid both punitive anger and overly dramatic emotional reactions that might inadvertently reinforce the behavior"},
            {"id": "B", "text": "Express intense horror, scream in disgust, and accuse the adolescent of trying to manipulate the ward staff"},
            {"id": "C", "text": "Lock the adolescent in a seclusion room for 48 hours without cleaning or dressing the wounds"},
            {"id": "D", "text": "Offer the adolescent expensive gifts and promise to cancel all ward rules if they stop crying"}
        ],
        "correctAnswer": "A",
        "explanation": "Optimal nursing response to self-harm requires 'matter-of-fact compassion': remaining calm, non-reactive, and non-judgmental while providing professional physical wound care. Expressing shock, disgust, or anger shames the adolescent, while overly effusive emotional attention can inadvertently provide secondary reinforcement for self-injury.",
        "incorrectExplanations": {
            "B": "Shaming and accusing patients of manipulation escalates distress, self-hatred, and further self-injury.",
            "C": "Withholding wound care and isolating patients is punitive, neglectful, and abusive.",
            "D": "Excessive secondary gain or bribing reinforces self-harm as an operant behavior."
        },
        "learningObjective": "Demonstrate calm, validating, and clinically balanced communication when responding to acute self-harm disclosure.",
        "reference": "Royal College of Psychiatrists. (2014). Managing self-harm in young people (College Report CR192).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q754",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Adolescent risk-taking and self-harm",
        "difficulty": "Expert",
        "questionText": "A 16-year-old adolescent in outpatient therapy discloses active suicidal intent with a detailed plan to jump from a local bridge tonight, begging the nurse: 'You promised our sessions were strictly confidential! If you tell my parents, I will never trust you again and I will run away right now!' How must the advanced practice nurse navigate confidentiality versus safety?",
        "options": [
            {"id": "A", "text": "Maintain absolute silence and keep the secret because adolescent confidentiality always overrides physical survival"},
            {"id": "B", "text": "Promise the adolescent you will not tell anyone, then slip away quietly to go home for the weekend"},
            {"id": "C", "text": "Transparently explain that professional ethical codes and statutory safeguarding laws mandate breaching confidentiality when there is imminent risk of death; validate their distress, involve the adolescent in how the parents will be informed, and initiate immediate emergency crisis containment"},
            {"id": "D", "text": "Call the local newspaper to publish the adolescent's name and suicide plan"}
        ],
        "correctAnswer": "C",
        "explanation": "Confidentiality in child and adolescent mental health is never absolute; it is legally and ethically bounded by the duty to protect life and safeguard against significant harm. The nurse must clearly, transparently explain that imminent suicide risk requires sharing information, support the adolescent through disclosure to parents, and mobilize crisis safety protocols.",
        "incorrectExplanations": {
            "A": "Prioritizing confidentiality over imminent loss of life breaches duty of care and nursing law.",
            "B": "Abandoning an acutely suicidal adolescent constitutes gross negligence.",
            "D": "Publicly exposing medical confidences violates all privacy laws."
        },
        "learningObjective": "Resolve complex ethical and legal tensions between adolescent confidentiality and the mandatory duty of care in acute suicidality.",
        "reference": "General Medical Council (GMC). (2018). 0-18 years: guidance for all doctors - Protecting children and young people. GMC.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 5: Child safeguarding (MHN-Q755 - MHN-Q764)
    # Target Answers: A, C, B, D, A, C, B, A, D, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q755",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Foundation",
        "questionText": "In international child welfare frameworks and statutory safeguarding guidance (e.g., UK 'Working Together to Safeguard Children'), what are the four recognized primary categories of child maltreatment?",
        "options": [
            {"id": "A", "text": "Physical abuse, Emotional abuse, Sexual abuse, and Neglect"},
            {"id": "B", "text": "Academic failure, Truancy, Shyness, and Sibling rivalry"},
            {"id": "C", "text": "Economic poverty, Lack of private vehicle, Apartment living, and Single parenting"},
            {"id": "D", "text": "Poor sportsmanship, Disobeying bedtimes, Refusing vegetables, and Untidy bedrooms"}
        ],
        "correctAnswer": "A",
        "explanation": "Statutory child protection frameworks across the UK, Commonwealth, and international bodies categorize child abuse into four primary statutory domains: 1) Physical abuse, 2) Emotional abuse, 3) Sexual abuse, and 4) Neglect. Exposure to domestic abuse is recognized as causing significant emotional and developmental harm.",
        "incorrectExplanations": {
            "B": "These are common childhood developmental and educational challenges, not statutory abuse categories.",
            "C": "Poverty and social circumstances are socioeconomic determinants, not definitions of maltreatment.",
            "D": "Normative childhood misbehaviour does not constitute statutory maltreatment."
        },
        "learningObjective": "Recall the four primary statutory categories of child maltreatment under child safeguarding frameworks.",
        "reference": "HM Government. (2018). Working Together to Safeguard Children: A guide to inter-agency working. Department for Education.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q756",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Foundation",
        "questionText": "A mental health nurse conducts a home visit and observes cutaneous injuries on a 4-year-old child. Which of the following physical injury patterns is highly suspicious of non-accidental trauma (physical abuse) rather than typical childhood accidental play bruising?",
        "options": [
            {"id": "A", "text": "A small isolated bruise over the anterior tibial shin"},
            {"id": "B", "text": "A tiny scrape on the forehead sustained while falling off a bicycle on gravel"},
            {"id": "C", "text": "Bruising on soft, non-bony, protected anatomical areas (such as cheeks, neck, ears, buttocks, and abdomen), or symmetrical immersion burns with sharp demarcations ('glove and stocking' or 'doughnut' pattern)"},
            {"id": "D", "text": "A minor scab on the patella sustained during playground football"}
        ],
        "correctAnswer": "C",
        "explanation": "Accidental bruises in active young children occur almost exclusively over bony prominences (shins, knees, elbows, forehead). Bruising in soft, protected, or non-bony areas (ears, neck, cheeks, abdomen, genitalia, buttocks) or patterned injuries (belt marks, cigarette burns, immersion burns with sparing) strongly indicate physical abuse.",
        "incorrectExplanations": {
            "A": "Shin bruises are the most common benign accidental bruises in toddlers.",
            "B": "Forehead scrapes from bicycle falls are typical childhood accidental injuries.",
            "D": "Knee scabs from sports represent normal accidental physical play."
        },
        "learningObjective": "Differentiate suspicious non-accidental physical abuse indicators from normative accidental injuries.",
        "reference": "NICE. (2017). Child abuse and neglect (NICE Guideline NG76).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q757",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Foundation",
        "questionText": "What constellation of observations most clearly indicates chronic Child Neglect during a community psychiatric nursing assessment?",
        "options": [
            {"id": "A", "text": "A child wearing clean, secondhand clothing that is slightly out of fashion"},
            {"id": "B", "text": "Persistent severe untreated dental decay/abscesses, severe unaddressed medical needs, chronic lack of adequate clothing for freezing winter weather, persistent unwashed state, severe hunger, and lack of developmental supervision"},
            {"id": "C", "text": "A child having one messy toy scattered across their bedroom floor"},
            {"id": "D", "text": "A child who dislikes broccoli and prefers fruit juice"}
        ],
        "correctAnswer": "B",
        "explanation": "Neglect is the persistent failure to meet a child's basic physical, emotional, and psychological needs, resulting in serious impairment of health or development. Indicators include failure to seek medical/dental care for severe disease, chronic severe hygiene deprivation, inadequate clothing for weather, malnutrition, and abandonment.",
        "incorrectExplanations": {
            "A": "Wearing clean secondhand clothes reflects financial budgeting, not parental neglect.",
            "C": "Messy toys are normative play artifacts, not signs of neglect.",
            "D": "Dietary food preferences are normal childhood behaviors."
        },
        "learningObjective": "Identify physical, medical, and behavioral indicators of chronic child neglect.",
        "reference": "NSPCC. (2021). Neglect: Understanding and addressing child neglect in health settings.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q758",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Intermediate",
        "questionText": "During a family therapy session, a psychiatric nurse observes a mother repeatedly telling her 8-year-old son: 'You are completely worthless, evil, and I wish you had died at birth,' locking him out of the room while praising her other children. What category of child maltreatment is being enacted?",
        "options": [
            {"id": "A", "text": "Appropriate behavioral limit-setting"},
            {"id": "B", "text": "Normative parental sibling management"},
            {"id": "C", "text": "Physical neglect"},
            {"id": "D", "text": "Emotional abuse (psychological maltreatment)"}
        ],
        "correctAnswer": "D",
        "explanation": "Emotional abuse involves persistent ill-treatment of a child that causes severe adverse effects on emotional development: conveying that the child is worthless, unloved, or inadequate; scapegoating; terrorizing; severe persistent rejection; or isolating them from family members.",
        "incorrectExplanations": {
            "A": "Telling a child they are evil and wishing their death is abusive, never legitimate discipline.",
            "B": "Scapegoating and cruel rejection are severe emotional maltreatment.",
            "C": "While abusive, this scenario involves verbal and psychological cruelty, falling under emotional abuse."
        },
        "learningObjective": "Recognize signs, dynamics, and definitions of emotional abuse and psychological maltreatment.",
        "reference": "Glaser, D. (2002). Emotional abuse and neglect (psychological maltreatment): a conceptual framework. Child Abuse & Neglect, 26(6-7), 697-714.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q759",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Intermediate",
        "questionText": "In modern child protection legislation, witnessing or experiencing chronic domestic abuse / intimate partner violence within the household is recognized as inflicting what primary impact on children?",
        "options": [
            {"id": "A", "text": "Severe emotional abuse resulting in toxic stress, altered neurodevelopment (HPA axis dysregulation), chronic anxiety, behavioral disturbance, and impaired attachment security"},
            {"id": "B", "text": "Immediate superior athletic performance and increased physical height"},
            {"id": "C", "text": "Zero psychological impact because children do not pay attention to adult conflict"},
            {"id": "D", "text": "Immunity against future relationship difficulties"}
        ],
        "correctAnswer": "A",
        "explanation": "Exposure to domestic abuse is recognized in modern safeguarding legislation (such as the UK Domestic Abuse Act 2021) as a form of child abuse in its own right. Witnessing terror, violence, and coercive control between caregivers induces toxic stress, hyper-arousal, attachment disruption, and long-term neurobiological trauma.",
        "incorrectExplanations": {
            "B": "Domestic violence does not enhance athletics; it impairs emotional and somatic health.",
            "C": "Children are profoundly attuned to emotional threat in their living environment.",
            "D": "Children exposed to domestic abuse are at elevated risk for revictimization or trauma perpetuation."
        },
        "learningObjective": "Explain the psychological, neurodevelopmental, and legal impacts of domestic abuse exposure on children.",
        "reference": "Holt, S., et al. (2008). The impact of exposure to domestic violence on children and young people: A review of the literature. Child Abuse & Neglect, 32(8), 797-810.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q760",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Intermediate",
        "questionText": "A community psychiatric nurse visits an adult patient with severe bipolar mania and alcohol dependence. The nurse discovers the patient has left their 3-year-old child locked in a soiled cot without food for 18 hours while the parent was unconscious from alcohol. What is the nurse's mandatory statutory professional duty?",
        "options": [
            {"id": "A", "text": "Leave a polite sticky note on the refrigerator and check back in two weeks"},
            {"id": "B", "text": "Give the toddler a biscuit and promise the parent you will never report them"},
            {"id": "C", "text": "Immediately take action to ensure the child's immediate physical safety and make an urgent child protection referral to statutory children's social care / child welfare services and emergency services without delay"},
            {"id": "D", "text": "Assume the parent will resolve the issue once they sleep off the intoxication"}
        ],
        "correctAnswer": "C",
        "explanation": "Mental health nurses owe an overriding legal and professional duty of care to protect children from significant harm. Discovering an unattended, malnourished, neglected toddler requires immediate action: securing the child's immediate safety and making an emergency child safeguarding referral to statutory child welfare and police.",
        "incorrectExplanations": {
            "A": "Leaving an unattended toddler for weeks constitutes gross medical abandonment.",
            "B": "Concealing child neglect violates statutory safeguarding law and professional registration.",
            "D": "Assuming an incapacitated substance-abusing parent will provide safety is dangerous complacency."
        },
        "learningObjective": "Demonstrate statutory mandatory reporting duties and immediate protective actions during acute child neglect crises.",
        "reference": "Nursing and Midwifery Council (NMC). (2018). The Code: Professional standards of practice and behaviour for nurses, midwives and nursing associates.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q761",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Advanced",
        "questionText": "Under the UK Children Act 1989/2004 framework, what is the crucial legal distinction between a Section 17 inquiry ('Child in Need') and a Section 47 inquiry ('Child Protection')?",
        "options": [
            {"id": "A", "text": "Section 17 involves criminal incarceration of the parents, whereas Section 47 provides cash bonuses"},
            {"id": "B", "text": "Section 17 provides voluntary supportive family services to promote the welfare of a 'Child in Need', whereas Section 47 mandates a formal inter-agency child protection investigation because there is reasonable cause to suspect the child is suffering, or is likely to suffer, 'significant harm'"},
            {"id": "C", "text": "Section 17 applies only to orphans, whereas Section 47 applies only to adolescents over 18"},
            {"id": "D", "text": "There is no legal difference between Section 17 and Section 47"}
        ],
        "correctAnswer": "B",
        "explanation": "Section 17 (Children Act 1989) assesses a 'Child in Need' where local authorities provide voluntary supportive social, health, and family services. Section 47 mandates statutory multi-agency child protection investigations when there is reasonable cause to suspect a child is suffering or likely to suffer 'significant harm' (abuse/neglect).",
        "incorrectExplanations": {
            "A": "Section 17 provides family support, not criminal imprisonment.",
            "C": "Both sections apply to any child under the age of 18.",
            "D": "The distinction between voluntary support (S17) and mandatory harm investigation (S47) is central to child law."
        },
        "learningObjective": "Differentiate between Section 17 ('Child in Need') and Section 47 ('Significant Harm') statutory frameworks.",
        "reference": "Department for Education. (2018). Working Together to Safeguard Children. UK Government.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q762",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Advanced",
        "questionText": "When documenting a child safeguarding disclosure or injury in the clinical electronic health record, what documentation standard must the psychiatric mental health nurse uphold to satisfy legal scrutiny in family court proceedings?",
        "options": [
            {"id": "A", "text": "Record the child's exact words in verbatim quotation marks, document objective physical observations (size, shape, color of marks) on standardized body maps, record timings precisely, and clearly separate factual observations from professional opinion or speculation"},
            {"id": "B", "text": "Write emotional interpretations and personal hunches without quoting the child"},
            {"id": "C", "text": "Destroy all written records after 24 hours to prevent subpoena"},
            {"id": "D", "text": "Summarize complex interviews with single words like 'unremarkable'"}
        ],
        "correctAnswer": "A",
        "explanation": "Safeguarding documentation must withstand rigorous family and criminal court standards. Best practice mandates recording exact verbatim statements from the child (avoiding paraphrasing), using standardized body maps with measurements for physical marks, recording dates/times, and explicitly delineating observed facts from clinical opinions.",
        "incorrectExplanations": {
            "B": "Unsubstantiated speculation and hunches compromise judicial credibility and child protection.",
            "C": "Destroying clinical records is an illegal offense and violates professional standards.",
            "D": "Vague summaries fail to capture critical disclosure details required for legal protection."
        },
        "learningObjective": "Execute court-defensible child safeguarding clinical documentation standards, including body maps and verbatim recording.",
        "reference": "General Medical Council (GMC). (2018). Protecting children and young people: The responsibilities of all doctors. GMC.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q763",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Advanced",
        "questionText": "Under the established legal precedents of 'Gillick Competence' and the 'Fraser Guidelines', when can a young person under 16 years of age provide lawful consent to their own psychiatric or medical treatment without parental knowledge or consent?",
        "options": [
            {"id": "A", "text": "Whenever the child pays a private cash fee to the hospital"},
            {"id": "B", "text": "Children under 16 can never, under any legal circumstances, make decisions regarding their own body"},
            {"id": "C", "text": "Only if the child has passed a university entrance exam in bioethics"},
            {"id": "D", "text": "When the clinician assesses that the young person has sufficient maturity, intelligence, and understanding to fully comprehend the nature, purpose, risks, and implications of the proposed treatment, and their physical or mental health is likely to suffer without it"}
        ],
        "correctAnswer": "D",
        "explanation": "The Gillick competency principle (originating from the UK House of Lords 1985 ruling) establishes that a child under 16 has the legal capacity to consent to treatment if they possess sufficient maturity and intelligence to understand fully what is proposed, its risks, benefits, and alternatives, balancing child autonomy and protection.",
        "incorrectExplanations": {
            "A": "Financial payments have no bearing on legal capacity or competence.",
            "B": "Gillick competence established that children under 16 can have autonomous legal capacity.",
            "C": "Academic testing is not the legal standard; developmental maturity and understanding are."
        },
        "learningObjective": "Apply Gillick competence and Fraser guidelines to evaluate capacity and consent in young people under 16.",
        "reference": "Gillick v West Norfolk and Wisbech Area Health Authority [1985] UKHL 7, [1986] AC 112.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q764",
        "module": "8. Child, Adolescent, and Older Adult Mental Health",
        "topic": "Child safeguarding",
        "difficulty": "Expert",
        "questionText": "A Multi-Agency Safeguarding Hub (MASH) convenes an Initial Child Protection Conference (ICPC) regarding an infant whose mother has severe postpartum psychosis with command delusions and whose father has severe domestic violence convictions. As the lead psychiatric liaison nurse presenting at the ICPC, what is your primary clinical governance objective?",
        "options": [
            {"id": "A", "text": "Defend the adult psychiatric patient at all costs by minimizing all risks to the infant"},
            {"id": "B", "text": "Advocate that the conference be canceled because mental illness is a private medical matter"},
            {"id": "C", "text": "Synthesize psychiatric risk formulations regarding maternal delusions, evaluate the co-occurring domestic violence, collaborate with social care and police to determine whether threshold for a Child Protection Plan (under categories of emotional harm/neglect) is met, and design an enforceable multi-agency safety plan"},
            {"id": "D", "text": "Recommend immediate criminal imprisonment of the infant in a secure facility"}
        ],
        "correctAnswer": "C",
        "explanation": "At an Initial Child Protection Conference (ICPC), the psychiatric nurse bridges adult mental health and child protection. The nurse provides objective risk analysis: translating maternal command delusions into practical child safety risks, evaluating protective capacities, collaborating with multi-agency partners (MASH/police/social care), and formulating a robust Child Protection Plan.",
        "incorrectExplanations": {
            "A": "In child protection, the child's safety is paramount; adult advocacy cannot override infant survival.",
            "B": "Mental illness affecting parenting capacity is a statutory safeguarding concern, not a private secret.",
            "D": "Incarcerating an infant is an absurdity; infants are victims requiring protection."
        },
        "learningObjective": "Lead psychiatric multidisciplinary contributions within Multi-Agency Safeguarding Hubs (MASH) and Child Protection Conferences.",
        "reference": "HM Government. (2018). Working Together to Safeguard Children. UK Department for Education.",
        "contentReviewStatus": "Peer Reviewed"
    }
]
