# gen_workspace/gen_mod3_part2.py
"""
Module 3 Part 2: Topics 6 to 10 (Q265 - Q314, 50 questions)
Module: "3. Psychopathology and Psychiatric Diagnosis"
"""

MOD3_P2 = [
    # -------------------------------------------------------------
    # Topic 6: Trauma- and Stressor-Related Disorders (Q265 - Q274)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q265",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Foundation",
        "questionText": "A 36-year-old paramedic who survived a fatal multi-vehicle collision 4 months ago reports recurrent involuntary distressing memories of the event, waking in terror from nightmares of the crash, and experiencing dissociative flashbacks where they feel as if the collision is recurring right now. Which DSM-5-TR symptom cluster of Posttraumatic Stress Disorder (PTSD) is demonstrated?",
        "options": [
            {"id": "A", "text": "Intrusion symptoms (Criterion B)"},
            {"id": "B", "text": "Persistent avoidance of trauma-related stimuli (Criterion C)"},
            {"id": "C", "text": "Negative alterations in cognitions and mood (Criterion D)"},
            {"id": "D", "text": "Alterations in arousal and reactivity (Criterion E)"}
        ],
        "correctAnswer": "A",
        "explanation": "Criterion B of DSM-5-TR PTSD encompasses intrusion symptoms associated with the traumatic event, beginning after the event occurred. These include recurrent, involuntary, and intrusive distressing memories; recurrent distressing trauma dreams/nightmares; dissociative reactions (flashbacks) where the individual feels or acts as if the trauma were recurring; and marked psychological distress or physiological reactivity upon exposure to trauma reminders.",
        "incorrectExplanations": {
            "A": "Intrusion symptoms include intrusive memories, nightmares, and flashbacks where trauma feels recurrent.",
            "B": "Criterion C avoidance involves efforts to avoid internal thoughts/feelings or external reminders (people, places).",
            "C": "Criterion D involves persistent negative beliefs, emotional numbing, detachment, and anhedonia.",
            "D": "Criterion E includes hypervigilance, exaggerated startle, irritability, and sleep disturbance."
        },
        "learningObjective": "Differentiate between the four core DSM-5-TR symptom clusters in PTSD.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Posttraumatic Stress Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q266",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Foundation",
        "questionText": "A mental health nurse evaluates an individual 10 days after surviving an armed robbery. The individual presents with severe emotional numbing, depersonalisation, intrusive memories, insomnia, and hyperarousal. What diagnostic timeline distinguishes Acute Stress Disorder (ASD) from Posttraumatic Stress Disorder (PTSD)?",
        "options": [
            {"id": "A", "text": "ASD requires symptoms to persist for at least 6 months, whereas PTSD resolves within 4 weeks"},
            {"id": "B", "text": "ASD occurs between 3 days and 1 month following trauma exposure, whereas PTSD requires symptoms to persist for greater than 1 month"},
            {"id": "C", "text": "ASD is diagnosed only if physical bodily injury occurred, whereas PTSD applies solely to psychological witnesses"},
            {"id": "D", "text": "ASD excludes dissociative symptoms, whereas PTSD mandates persistent dissociative fugue"}
        ],
        "correctAnswer": "B",
        "explanation": "Acute Stress Disorder (ASD) is diagnosed when symptoms develop immediately and persist from 3 days to 1 month following exposure to a traumatic event. If characteristic trauma symptoms persist beyond 1 month, the diagnosis transitions from ASD to Posttraumatic Stress Disorder (PTSD).",
        "incorrectExplanations": {
            "A": "ASD is an acute post-trauma condition lasting 3 days to 1 month; PTSD requires symptoms exceeding 1 month.",
            "B": "ASD spans 3 days to 1 month post-trauma; PTSD requires symptom persistence beyond 1 month.",
            "C": "Physical injury is not required for either diagnosis; witnessing or direct trauma exposure suffices.",
            "D": "Dissociative symptoms (depersonalization, derealization) are prominent features of ASD."
        },
        "learningObjective": "Distinguish between Acute Stress Disorder and PTSD based on clinical duration thresholds.",
        "reference": "Bryant, R. A. (2018). The current status of acute stress disorder. Dialogues in Clinical Neuroscience, 20(3), 229-234.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q267",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Intermediate",
        "questionText": "Under the World Health Organization International Classification of Diseases (ICD-11), how is Complex Post-Traumatic Stress Disorder (Complex PTSD) differentiated from classic PTSD?",
        "options": [
            {"id": "A", "text": "Complex PTSD requires a single adult vehicular accident accompanied by psychotic delusions"},
            {"id": "B", "text": "Complex PTSD requires complete retrograde amnesia without affective distress"},
            {"id": "C", "text": "Complex PTSD encompasses the core PTSD triad PLUS severe disturbances in self-organization: affect dysregulation, negative self-concept, and interpersonal difficulties"},
            {"id": "D", "text": "Complex PTSD is diagnosed exclusively in children aged under 5 years presenting with selective mutism"}
        ],
        "correctAnswer": "C",
        "explanation": "ICD-11 defines Complex PTSD (CPTSD) as a severe disorder that typically arises following prolonged, repeated interpersonal trauma from which escape is difficult or impossible (e.g., childhood abuse, domestic captivity). It includes the three core PTSD symptoms (re-experiencing, avoidance, persistent perception of current threat) PLUS three disturbances in self-organization (DSO): (1) severe affect dysregulation, (2) persistent negative self-concept (feelings of worthlessness, deep shame), and (3) persistent difficulties in sustaining relationships.",
        "incorrectExplanations": {
            "A": "Complex PTSD typically arises from chronic, prolonged interpersonal trauma, not single-event adult accidents.",
            "B": "Complex PTSD involves intense affective distress and emotional lability, not isolated amnesia.",
            "C": "Complex PTSD combines the core PTSD triad with disturbances in self-organization (affect, self-concept, relationships).",
            "D": "Complex PTSD is diagnosed across the lifespan, predominantly recognized in adolescents and adults with complex trauma histories."
        },
        "learningObjective": "Compare and contrast ICD-11 Complex PTSD with classic PTSD.",
        "reference": "World Health Organization. (2018). International Classification of Diseases (11th rev.; ICD-11). Geneva: WHO.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q268",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Intermediate",
        "questionText": "A combat veteran with PTSD exhibits pervasive detachment from family members, states they feel 'completely dead inside and incapable of loving my children,' blames themselves entirely for the death of a comrade, and holds the rigid belief that 'no human being can ever be trusted again.' Which symptom cluster under DSM-5-TR does this represent?",
        "options": [
            {"id": "A", "text": "Criterion A: Traumatic exposure severity index"},
            {"id": "B", "text": "Criterion B: Dissociative somatisation cluster"},
            {"id": "C", "text": "Criterion C: Physiological reactivity to acoustic triggers"},
            {"id": "D", "text": "Criterion D: Negative alterations in cognitions and mood"}
        ],
        "correctAnswer": "D",
        "explanation": "DSM-5-TR Criterion D encompasses negative alterations in cognitions and mood associated with the traumatic event. Key manifestations include persistent exaggerated negative beliefs about oneself or the world ('no one can be trusted'), persistent distorted blame of self or others, persistent negative emotional states, marked anhedonia, feelings of detachment or estrangement from others, and persistent inability to experience positive emotions (emotional numbing).",
        "incorrectExplanations": {
            "A": "Criterion A defines the trauma exposure itself, not post-trauma cognitive and emotional changes.",
            "B": "Criterion B comprises intrusion symptoms like nightmares and flashbacks.",
            "C": "Criterion C involves active avoidance of reminders, thoughts, or feelings.",
            "D": "Criterion D covers distorted cognitions, self-blame, detachment, and persistent negative emotional states."
        },
        "learningObjective": "Identify manifestations of negative alterations in cognitions and mood in chronic PTSD.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Posttraumatic Stress Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q269",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Intermediate",
        "questionText": "An inpatient psychiatric nurse observes that a trauma survivor constantly sits with their back against the corner wall, repeatedly scans room exits, startles violently when a food trolley rattles, and displays explosive verbal anger at minor delays. Which symptom cluster of PTSD is demonstrated?",
        "options": [
            {"id": "A", "text": "Alterations in arousal and reactivity (Criterion E)"},
            {"id": "B", "text": "Dissociative depersonalisation (Criterion B)"},
            {"id": "C", "text": "Cognitive blunting and apathy (Criterion D)"},
            {"id": "D", "text": "Situational agoraphobia (Criterion C)"}
        ],
        "correctAnswer": "A",
        "explanation": "Criterion E in DSM-5-TR PTSD reflects marked alterations in arousal and reactivity associated with the traumatic event. Features include irritable behavior and angry outbursts, reckless or self-destructive behavior, hypervigilance (e.g., scanning exits, sitting against walls), exaggerated startle response, concentration problems, and sleep disturbance.",
        "incorrectExplanations": {
            "A": "Hypervigilance, exaggerated startle, and irritability are classic Criterion E arousal symptoms.",
            "B": "Depersonalization is an altered sense of self/detachment, not physiological hyperarousal.",
            "C": "Cognitive blunting represents emotional numbing in Criterion D, not autonomic reactivity.",
            "D": "Agoraphobia is a separate fear of open/enclosed spaces, whereas this patient demonstrates trauma hypervigilance."
        },
        "learningObjective": "Recognize behavioral signs of hyperarousal and hypervigilance in inpatient trauma survivors.",
        "reference": "Townsend, M. C., & Morgan, K. I. (2020). Psychiatric Mental Health Nursing (10th ed.). F.A. Davis.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q270",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 28-year-old trauma patient with PTSD reports that during emotional stress, they feel as though they are floating outside their physical body looking down at themselves, or that their surrounding physical environment appears dreamy, artificial, and two-dimensional. Which DSM-5-TR specifier applies?",
        "options": [
            {"id": "A", "text": "With melancholic features"},
            {"id": "B", "text": "With dissociative symptoms (depersonalization or derealization)"},
            {"id": "C", "text": "With delayed expression (>12 months)"},
            {"id": "D", "text": "With psychotic thought broadcasting"}
        ],
        "correctAnswer": "B",
        "explanation": "DSM-5-TR includes the specifier 'with dissociative symptoms' for PTSD when the individual's symptoms meet criteria for PTSD and in addition, in response to the stressor, the individual experiences persistent or recurrent symptoms of either: (1) Depersonalization (feeling detached from one's body/mental processes, like an outside observer), or (2) Derealization (experiencing surroundings as unreal, dreamlike, distant, or distorted).",
        "incorrectExplanations": {
            "A": "Melancholic features apply to major depressive episodes, not PTSD specifiers.",
            "B": "The dissociative subtype of PTSD captures depersonalization and derealization phenomena.",
            "C": "Delayed expression applies when full diagnostic criteria are not met until at least 6 months after the trauma.",
            "D": "Thought broadcasting is a psychotic delusion, whereas reality testing remains intact in dissociative specifiers."
        },
        "learningObjective": "Differentiate the dissociative subtype of PTSD using depersonalization and derealization criteria.",
        "reference": "Lanius, R. A., et al. (2010). Emotion modulation in PTSD: clinical and neurobiological evidence for a dissociative subtype. American Journal of Psychiatry, 167(6), 640-647.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q271",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Advanced",
        "questionText": "A psychiatric nurse manager is redesigning unit policies around Trauma-Informed Care (TIC) on an acute inpatient unit. Which core principle of trauma-informed care directly addresses preventing re-traumatisation of patients with complex trauma?",
        "options": [
            {"id": "A", "text": "Enforcing mandatory seclusion room stays upon admission to desensitize patients to isolation"},
            {"id": "B", "text": "Restricting patient telephone access until all trauma memories have been verbally disclosed in group"},
            {"id": "C", "text": "Fostering physical and psychological safety, transparency, peer support, collaboration, empowerment, and minimizing coercive practices like physical restraints"},
            {"id": "D", "text": "Insisting on immediate detailed trauma disclosure interviews during the first triage assessment"}
        ],
        "correctAnswer": "C",
        "explanation": "Trauma-Informed Care (TIC) is guided by SAMHSA's core principles: Safety (physical and emotional); Trustworthiness and Transparency; Peer Support; Collaboration and Mutuality; and Empowerment, Voice, and Choice. Minimizing coercive interventions (physical restraints, seclusion) is vital to resist re-traumatization of individuals whose trauma involved physical helplessness and violation.",
        "incorrectExplanations": {
            "A": "Seclusion rooms reproduce feelings of entrapment and are deeply re-traumatizing.",
            "B": "Coercive restrictions on communication breach TIC principles of empowerment and safety.",
            "C": "TIC prioritizes safety, trust, collaboration, voice, and eliminating coercive practices.",
            "D": "Forcing premature detailed trauma disclosure before stabilization can destabilize patients and precipitate crises."
        },
        "learningObjective": "Apply the principles of Trauma-Informed Care to acute psychiatric nursing environments.",
        "reference": "Substance Abuse and Mental Health Services Administration. (2014). SAMHSA's Concept of Trauma and Guidance for a Trauma-Informed Approach. HHS Publication No. (SMA) 14-4884.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q272",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Advanced",
        "questionText": "When educating a patient with PTSD regarding evidence-based psychological treatments recommended by NICE guidelines, how should the nurse explain the mechanism of Eye Movement Desensitization and Reprocessing (EMDR)?",
        "options": [
            {"id": "A", "text": "It hypnotises the patient to selectively delete traumatic synaptic pathways from cortical memory banks"},
            {"id": "B", "text": "It provokes acute hyperventilation to induce cerebral vasoconstriction, blocking trauma recall"},
            {"id": "C", "text": "It provides rapid autonomic sedation through direct mechanical stimulation of optic nerve GABA receptors"},
            {"id": "D", "text": "It uses bilateral dual-attention stimulation (such as side-to-side eye movements) while recalling the trauma memory to facilitate information reprocessing and decrease emotional charge"}
        ],
        "correctAnswer": "D",
        "explanation": "EMDR is an evidence-based psychotherapy for PTSD that pairs the recall of distressing trauma memories and associated negative cognitions with bilateral dual-attention sensory stimulation (typically horizontal saccadic eye movements, alternating auditory tones, or bilateral hand taps). This taxes working memory and stimulates adaptive information processing, reducing the vividness and emotional intensity of traumatic memories.",
        "incorrectExplanations": {
            "A": "EMDR does not involve hypnosis and does not erase or delete memories.",
            "B": "EMDR avoids hyperventilation and focuses on grounded, controlled memory reprocessing.",
            "C": "Bilateral eye movements do not mechanically stimulate optic nerve GABA receptors.",
            "D": "EMDR facilitates cognitive and emotional reprocessing of trauma via bilateral dual-attention stimulation."
        },
        "learningObjective": "Describe the therapeutic principles and clinical application of EMDR for PTSD.",
        "reference": "National Institute for Health and Care Excellence. (2018). Post-traumatic stress disorder (NICE Guideline NG116). London: NICE.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q273",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Advanced",
        "questionText": "A 52-year-old individual whose spouse died 16 months ago experiences intense yearning and longing for the deceased daily, accompanied by disbelief about the death, intense emotional pain, identity disruption ('feeling as if part of myself died with them'), and marked avoidance of reminders of the loss, severely impairing vocational functioning. Under DSM-5-TR, what is the diagnosis?",
        "options": [
            {"id": "A", "text": "Prolonged Grief Disorder"},
            {"id": "B", "text": "Normal uncomplicated bereavement reaction"},
            {"id": "C", "text": "Adjustment Disorder with mixed anxiety and depressed mood"},
            {"id": "D", "text": "Persistent Complex Schizoaffective Bereavement"}
        ],
        "correctAnswer": "A",
        "explanation": "DSM-5-TR formally added Prolonged Grief Disorder to Trauma- and Stressor-Related Disorders. It requires the death of a close person at least 12 months ago (for adults; 6 months for children/adolescents), characterized by persistent intense yearning/longing for the deceased and/or preoccupation with thoughts or memories of the deceased, accompanied by at least 3 of 8 grief-related symptoms occurring almost every day for at least the past month, impairing daily functioning.",
        "incorrectExplanations": {
            "A": "Prolonged Grief Disorder is diagnosed when disabling yearning and identity disruption persist >12 months post-loss.",
            "B": "Uncomplicated bereavement resolves without disabling, daily identity disruption and yearning 16 months later.",
            "C": "Adjustment disorder cannot be diagnosed if symptoms meet criteria for Prolonged Grief Disorder.",
            "D": "Persistent complex schizoaffective bereavement is an invalid, non-existent diagnostic entity."
        },
        "learningObjective": "Identify DSM-5-TR diagnostic criteria for Prolonged Grief Disorder.",
        "reference": "Prigerson, H. G., et al. (2021). Prolonged Grief Disorder: diagnostic utility and validity of DSM-5-TR criteria. World Psychiatry, 20(3), 397-406.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q274",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Trauma- and Stressor-Related Disorders",
        "difficulty": "Expert",
        "questionText": "Neuroimaging and neuroendocrine investigations in patients with chronic severe PTSD characteristically reveal which pattern of structural and neurochemical alterations?",
        "options": [
            {"id": "A", "text": "Hypoactivity of the amygdala with increased anterior cingulate inhibition and elevated morning salivary cortisol"},
            {"id": "B", "text": "Hyperactivity of the amygdala, decreased volume and functional hyporeactivity of the hippocampus, impaired medial prefrontal cortex inhibitory gating, and enhanced glucocorticoid receptor sensitivity with lower basal cortisol levels"},
            {"id": "C", "text": "Massive hypersecretion of hypothalamic oxytocin with bilateral enlargement of the caudate nuclei"},
            {"id": "D", "text": "Selective necrosis of the dorsolateral prefrontal cortex with suppressed sympathetic locus coeruleus output"}
        ],
        "correctAnswer": "B",
        "explanation": "PTSD neurobiology involves: (1) Amygdala hyperresponsiveness generating exaggerated fear and vigilance; (2) Reduced hippocampal volume and impaired contextual processing, preventing discrimination between past trauma and present safety; (3) Medial prefrontal cortex (mPFC / anterior cingulate) hypoactivity, failing to exert top-down extinction of fear; and (4) Altered HPA-axis with heightened glucocorticoid receptor sensitivity and low-to-normal basal cortisol (distinguishing PTSD from major depression).",
        "incorrectExplanations": {
            "A": "The amygdala is hyperactive in PTSD, not hypoactive, and cortisol levels are often lower/sensitized rather than elevated.",
            "B": "Amygdalar hyperactivity, reduced hippocampal volume, deficient prefrontal inhibition, and glucocorticoid receptor hypersensitivity characterize PTSD.",
            "C": "Oxytocin hypersecretion and caudate enlargement are not primary PTSD neurobiological hallmarks.",
            "D": "Locus coeruleus noradrenergic output is hyperactive (causing adrenergic storm), not suppressed."
        },
        "learningObjective": "Analyze the neurobiological, neuroendocrine, and structural neuroimaging findings underlying PTSD pathophysiology.",
        "reference": "Rauch, S. L., et al. (2006). Neurocircuitry models of PTSD and anxiety disorders. Biological Psychiatry, 60(4), 376-382.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 7: Personality Disorders (Q275 - Q284)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q275",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Foundation",
        "questionText": "A 44-year-old computer programmer lives alone in a remote cottage, has no close friends or confidants other than a first-degree relative, consistently chooses solitary occupations and hobbies, expresses no desire for sexual experiences or intimate relationships, and appears completely indifferent to both the praise and criticism of colleagues. Which Cluster A personality disorder is represented?",
        "options": [
            {"id": "A", "text": "Paranoid Personality Disorder"},
            {"id": "B", "text": "Avoidant Personality Disorder"},
            {"id": "C", "text": "Schizoid Personality Disorder"},
            {"id": "D", "text": "Schizotypal Personality Disorder"}
        ],
        "correctAnswer": "C",
        "explanation": "Schizoid Personality Disorder (Cluster A) is characterized by a pervasive pattern of detachment from social relationships and a restricted range of expression of emotions in interpersonal settings. Key criteria include neither desiring nor enjoying close relationships, almost always choosing solitary activities, little interest in sexual experiences, indifference to praise or criticism, and emotional coldness or flattened affectivity.",
        "incorrectExplanations": {
            "A": "Paranoid PD involves pervasive distrust and suspiciousness of malevolent motives, which is absent here.",
            "B": "Avoidant PD individuals deeply desire relationships but avoid them out of fear of rejection and inadequacy.",
            "C": "Schizoid PD is characterized by genuine disinterest in interpersonal relationships and preference for solitary living.",
            "D": "Schizotypal PD features odd beliefs, magical thinking, and eccentricities, not pure social detachment."
        },
        "learningObjective": "Differentiate Schizoid Personality Disorder from avoidant and other Cluster A personality disorders.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Schizoid Personality Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q276",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Foundation",
        "questionText": "A 30-year-old outpatient presents with odd, eccentric clothing, speaks in an elaborate metaphorical and circumstantial manner, and describes beliefs that they can read others' minds via 'telepathic vibrations.' They have no close friends, experience chronic social anxiety related to paranoid suspicions, but reality-testing remains intact with no sustained delusions or hallucinations. Which disorder is this?",
        "options": [
            {"id": "A", "text": "Chronic undifferentiated schizophrenia"},
            {"id": "B", "text": "Bipolar I Disorder with psychotic mania"},
            {"id": "C", "text": "Autism Spectrum Disorder, Level 3"},
            {"id": "D", "text": "Schizotypal Personality Disorder"}
        ],
        "correctAnswer": "D",
        "explanation": "Schizotypal Personality Disorder (Cluster A) is characterized by a pervasive pattern of social and interpersonal deficits marked by acute discomfort with, and reduced capacity for, close relationships as well as by cognitive or perceptual distortions and eccentricities of behavior. Key features include ideas of reference, odd beliefs or magical thinking (e.g., telepathy), unusual perceptual experiences, odd speech, and paranoid ideation.",
        "incorrectExplanations": {
            "A": "Schizophrenia involves persistent, prominent frank delusions or hallucinations and functional deterioration.",
            "B": "Bipolar I mania involves episodic mood elevation, grandiosity, and flight of ideas, not baseline eccentricity.",
            "C": "Autism Spectrum Disorder involves deficits in social communication and restricted repetitive motor patterns without magical thinking/telepathy.",
            "D": "Schizotypal Personality Disorder is defined by cognitive distortions, magical thinking, and eccentric behavior."
        },
        "learningObjective": "Recognize the diagnostic features of Schizotypal Personality Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Schizotypal Personality Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q277",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Intermediate",
        "questionText": "Under DSM-5-TR, which developmental and age requirement is mandatory before a clinician can formally diagnose Antisocial Personality Disorder in an adult?",
        "options": [
            {"id": "A", "text": "The individual must be at least 18 years of age, and there must be objective evidence of Conduct Disorder with onset before age 15"},
            {"id": "B", "text": "The individual must be at least 25 years of age, and there must be evidence of childhood enuresis and pyromania"},
            {"id": "C", "text": "The individual must have a formal conviction in a criminal court of law before age 16"},
            {"id": "D", "text": "The individual must be at least 21 years of age, with comorbid Oppositional Defiant Disorder lasting 7 years"}
        ],
        "correctAnswer": "A",
        "explanation": "DSM-5-TR Criterion B and C for Antisocial Personality Disorder state that the individual must be at least 18 years of age (Criterion B), and there must be evidence of Conduct Disorder with onset before age 15 years (Criterion C). This reflects the enduring, developmental nature of the pathology.",
        "incorrectExplanations": {
            "A": "The age must be at least 18 years with evidence of Conduct Disorder before age 15.",
            "B": "Age 25 and the Macdonald triad (enuresis/pyromania) are not official DSM-5-TR criteria.",
            "C": "Legal conviction is not required; clinical evidence of persistent rule-breaking and aggression suffices.",
            "D": "Age 21 and 7-year ODD are incorrect criteria thresholds."
        },
        "learningObjective": "Identify mandatory age and developmental prerequisites for diagnosing Antisocial Personality Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Antisocial Personality Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q278",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 23-year-old female presents to the emergency department with superficial wrist lacerations following an argument with her partner. She describes an overwhelming terror of being abandoned, feelings of chronic emptiness, intense episodic shifts from euphoria to deep despair lasting several hours, unstable relationships alternating between idealization and devaluation, and frequent impulsive spending. Which personality disorder is demonstrated?",
        "options": [
            {"id": "A", "text": "Histrionic Personality Disorder"},
            {"id": "B", "text": "Borderline Personality Disorder (BPD)"},
            {"id": "C", "text": "Bipolar II Disorder"},
            {"id": "D", "text": "Dependent Personality Disorder"}
        ],
        "correctAnswer": "B",
        "explanation": "Borderline Personality Disorder (Cluster B) is characterized by a pervasive pattern of instability of interpersonal relationships, self-image, and affects, and marked impulsivity. Cardinal features shown here include frantic efforts to avoid abandonment, alternating idealization and devaluation (splitting), affective instability over hours, chronic emptiness, impulsivity, and recurrent self-harm behavior.",
        "incorrectExplanations": {
            "A": "Histrionic PD centers on dramatic attention-seeking and theatrical emotionality without chronic self-harm or abandonment panic.",
            "B": "Borderline Personality Disorder is defined by relational instability, fear of abandonment, impulsivity, self-harm, and affective lability.",
            "C": "Bipolar II episodes last days to weeks, whereas BPD affective shifts occur within hours triggered by interpersonal events.",
            "D": "Dependent PD involves submissive clinging to ensure care, without the rage, impulsivity, splitting, and self-harm seen in BPD."
        },
        "learningObjective": "Recognize the core psychopathological features of Borderline Personality Disorder.",
        "reference": "Gunderson, J. G., et al. (2018). Borderline personality disorder. Nature Reviews Disease Primers, 4, 18029.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q279",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Intermediate",
        "questionText": "On an inpatient unit, a patient with Borderline Personality Disorder tells the day nurse: 'You are the only nurse who understands me; the night nurses are cruel, incompetent monsters.' Later that evening, the patient attempts to bypass unit rules by requesting privileges from the night team. What primitive psychological defense mechanism is being exhibited, and how should the nursing team respond?",
        "options": [
            {"id": "A", "text": "Projection; the nursing team should reassign the patient exclusively to the favored day nurse"},
            {"id": "B", "text": "Reaction formation; the team should reprimand the patient and enforce 48 hours of solitary confinement"},
            {"id": "C", "text": "Splitting; the nursing team must maintain clear inter-shift communication, consistent unified boundaries, and avoid taking polarizing roles"},
            {"id": "D", "text": "Sublimation; the team should encourage the patient to channel their feelings into competitive physical sports"}
        ],
        "correctAnswer": "C",
        "explanation": "Splitting is an immature defense mechanism common in BPD where individuals view people, situations, or self as all-good or all-bad, unable to integrate positive and negative qualities. It frequently divides multidisciplinary teams into 'rescuers' and 'persecutors.' The evidence-based nursing approach requires frequent multidisciplinary communication, consistent adherence to unit rules, and a unified, non-defensive stance.",
        "incorrectExplanations": {
            "A": "Reassigning only to the favored nurse reinforces splitting and worsens staff polarization.",
            "B": "Reprimand and solitary confinement are punitive and breach professional ethical nursing standards.",
            "C": "Splitting requires unified team communication, consistent limit-setting, and neutral boundary maintenance.",
            "D": "Sublimation is a mature defense mechanism; splitting is an immature, polarizing defense mechanism."
        },
        "learningObjective": "Identify the defense mechanism of splitting and formulate unified nursing boundary management strategies.",
        "reference": "Townsend, M. C., & Morgan, K. I. (2020). Psychiatric Mental Health Nursing (10th ed.). F.A. Davis.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q280",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Intermediate",
        "questionText": "Dialectical Behaviour Therapy (DBT), developed by Marsha Linehan, is the gold-standard psychosocial intervention for Borderline Personality Disorder. Which four specific skill training modules comprise comprehensive DBT?",
        "options": [
            {"id": "A", "text": "Hypnosis, Cognitive restructuring, Psychoanalysis, and Free association"},
            {"id": "B", "text": "Aversion therapy, System desensitization, Flooding, and Operant conditioning"},
            {"id": "C", "text": "Dream analysis, Catharsis, Transference resolution, and Countertransference mapping"},
            {"id": "D", "text": "Core Mindfulness, Distress Tolerance, Emotion Regulation, and Interpersonal Effectiveness"}
        ],
        "correctAnswer": "D",
        "explanation": "Standard Dialectical Behavior Therapy (DBT) delivers behavioral skills training across four distinct modules: (1) Core Mindfulness (balancing emotion mind and reasonable mind to reach wise mind), (2) Distress Tolerance (crisis survival skills like TIPP, radical acceptance), (3) Emotion Regulation (identifying and modulating emotional states), and (4) Interpersonal Effectiveness (assertiveness and relationship maintenance, e.g., DEAR MAN).",
        "incorrectExplanations": {
            "A": "Hypnosis and psychoanalysis are psychodynamic modalities, not DBT skill modules.",
            "B": "Flooding and aversion therapy are classical conditioning techniques not included in DBT skills training.",
            "C": "Dream analysis and catharsis are psychoanalytic methods contrary to DBT's behavioral approach.",
            "D": "The four DBT modules are Mindfulness, Distress Tolerance, Emotion Regulation, and Interpersonal Effectiveness."
        },
        "learningObjective": "Outline the four core skill training modules of Dialectical Behavior Therapy (DBT).",
        "reference": "Linehan, M. M. (2015). DBT Skills Training Manual (2nd ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q281",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Foundation",
        "questionText": "A 32-year-old actor feels intensely uncomfortable in clinical consultations when they are not the center of attention. They dress in provocative, theatrical clothing, display rapidly shifting and shallow emotional expressions, speak with impressionistic speech lacking detail, and assume relationships with staff are far more intimate than they actually are. What personality disorder is indicated?",
        "options": [
            {"id": "A", "text": "Histrionic Personality Disorder"},
            {"id": "B", "text": "Narcissistic Personality Disorder"},
            {"id": "C", "text": "Borderline Personality Disorder"},
            {"id": "D", "text": "Schizotypal Personality Disorder"}
        ],
        "correctAnswer": "A",
        "explanation": "Histrionic Personality Disorder (Cluster B) is characterized by a pervasive pattern of excessive emotionality and attention-seeking. Criteria include discomfort when not the center of attention, inappropriate sexually seductive or provocative behavior, rapidly shifting and shallow emotions, consistently using physical appearance to draw attention, impressionistic speech, theatricality, and misinterpreting relationships as more intimate than they are.",
        "incorrectExplanations": {
            "A": "Histrionic Personality Disorder is defined by excessive emotionality, theatricality, and intense need to be the center of attention.",
            "B": "Narcissistic PD focuses on grandiosity, need for admiration, and lack of empathy, rather than pure emotional theatrics.",
            "C": "Borderline PD involves severe identity disturbance, self-harm, and terror of abandonment, which are absent here.",
            "D": "Schizotypal PD involves magical thinking and social discomfort, rather than dramatic attention-seeking."
        },
        "learningObjective": "Identify diagnostic features of Histrionic Personality Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Histrionic Personality Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q282",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Advanced",
        "questionText": "How does Obsessive-Compulsive Personality Disorder (OCPD) fundamentally differ from Obsessive-Compulsive Disorder (OCD) in psychopathological assessment?",
        "options": [
            {"id": "A", "text": "OCPD is characterized by prominent auditory hallucinations, whereas OCD involves only olfactory illusions"},
            {"id": "B", "text": "OCPD features pervasive, ego-syntonic perfectionism, preoccupation with orderliness, and moral rigidity, whereas OCD features intrusive, ego-dystonic obsessions and compulsions performed to neutralize distress"},
            {"id": "C", "text": "OCPD involves childhood motor tics, whereas OCD occurs exclusively in geriatric dementia"},
            {"id": "D", "text": "OCPD responds rapidly to low-dose benzodiazepines, whereas OCD requires surgical lobotomy"}
        ],
        "correctAnswer": "B",
        "explanation": "The fundamental difference lies in ego-syntonicity versus ego-dystonicity. OCPD (Cluster C) is a pervasive personality construct characterized by perfectionism, orderliness, rigidity, and control; the individual perceives their high standards as correct, necessary, and desirable (ego-syntonic). In contrast, OCD involves intrusive, unwanted obsessions and repetitive compulsions that the patient experiences as distressing, irrational, and alien to their self (ego-dystonic).",
        "incorrectExplanations": {
            "A": "Neither OCPD nor uncomplicated OCD involves hallucinations.",
            "B": "OCPD is ego-syntonic (perceived as proper and desirable), whereas OCD is ego-dystonic (intrusive, distressing, unwanted).",
            "C": "OCPD does not involve motor tics, and OCD typically has onset in adolescence or early adulthood, not dementia.",
            "D": "Benzodiazepines are ineffective for OCPD; SSRIs and ERP are first-line for OCD, with surgery reserved only for extreme refractoriness."
        },
        "learningObjective": "Differentiate between Obsessive-Compulsive Personality Disorder (OCPD) and Obsessive-Compulsive Disorder (OCD).",
        "reference": "Fineberg, N. A., et al. (2014). Obsessive-compulsive personality disorder: a review of symptomatology and clinical implications. Dialogues in Clinical Neuroscience, 16(2), 173-182.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q283",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Advanced",
        "questionText": "A 26-year-old clerk desires friendships and romantic relationships deeply, but avoids social work functions, turns down promotions requiring presentations, and declines invitations because of pervasive feelings of inadequacy, extreme fear of criticism or rejection, and viewing themselves as socially inept and inferior. How is Avoidant Personality Disorder distinguished from Schizoid Personality Disorder?",
        "options": [
            {"id": "A", "text": "Individuals with Avoidant PD crave social connection but avoid it due to intense fear of rejection, whereas individuals with Schizoid PD have no desire for social connection and prefer isolation"},
            {"id": "B", "text": "Avoidant PD involves persecutory delusions, whereas Schizoid PD involves hypomanic cheerfulness"},
            {"id": "C", "text": "Avoidant PD is classified as Cluster A, whereas Schizoid PD is classified as Cluster B"},
            {"id": "D", "text": "Avoidant PD occurs exclusively in males, whereas Schizoid PD is confined to postmenopausal females"}
        ],
        "correctAnswer": "A",
        "explanation": "Individuals with Avoidant Personality Disorder (Cluster C) genuinely yearn for interpersonal intimacy and social acceptance, but their hypersensitivity to potential rejection, humiliation, and perceived inadequacy leads to social inhibition and avoidance. In contrast, individuals with Schizoid Personality Disorder (Cluster A) have no inner desire for relationships and are genuinely content in solitary isolation.",
        "incorrectExplanations": {
            "A": "Avoidant PD individuals crave connection but fear rejection; Schizoid PD individuals lack interest in connection.",
            "B": "Neither disorder features persecutory delusions or hypomanic cheerfulness.",
            "C": "Avoidant PD is Cluster C; Schizoid PD is Cluster A.",
            "D": "Both disorders occur across genders without gender-exclusive limitations."
        },
        "learningObjective": "Distinguish the interpersonal motivations of Avoidant Personality Disorder from Schizoid Personality Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Avoidant Personality Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q284",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Personality Disorders",
        "difficulty": "Expert",
        "questionText": "Mentalization-Based Treatment (MBT), pioneered by Bateman and Fonagy, conceptualizes borderline personality pathology as a breakdown in which psychological capacity under attachment stress?",
        "options": [
            {"id": "A", "text": "The capacity for rapid sensory adaptation in the cerebellar vestibular pathways"},
            {"id": "B", "text": "The reflective capacity to understand one's own and others' mental states in terms of thoughts, feelings, desires, and intentions"},
            {"id": "C", "text": "The intellectual capacity to calculate complex abstract mathematical probabilities"},
            {"id": "D", "text": "The autonomic capacity to suppress sympathetic pupillary dilation during fear"}
        ],
        "correctAnswer": "B",
        "explanation": "Mentalization is the mental process by which an individual implicitly and explicitly interprets actions of self and others as meaningful on the basis of intentional mental states (e.g., desires, feelings, beliefs, goals). In BPD, interpersonal or attachment stress triggers emotional arousal that collapses mentalizing, causing non-mentalizing modes: psychic equivalence (subjective feelings equate to external reality), pretend mode, and teleological mode (only physical actions prove mental states).",
        "incorrectExplanations": {
            "A": "Vestibular adaptation is a biological sensory function, not the mentalization capacity.",
            "B": "Mentalization is the capacity to interpret behavior as arising from underlying thoughts, feelings, and beliefs.",
            "C": "Abstract mathematical reasoning is general cognitive IQ, not social cognition or mentalizing.",
            "D": "Autonomic pupil control is a neurological reflex unrelated to mentalization theory."
        },
        "learningObjective": "Synthesize the concept of mentalization failure and the theoretical foundation of Mentalization-Based Treatment (MBT).",
        "reference": "Bateman, A., & Fonagy, P. (2016). Mentalization-Based Treatment for Personality Disorders: A Practical Guide. Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 8: Dissociative Disorders (Q285 - Q294)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q285",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Foundation",
        "questionText": "A 24-year-old student reports persistent, distressing episodes where they feel completely detached from their body, as if they are a robotic spectator watching their own actions from above. Simultaneously, they state: 'I know I am sitting here in front of you and that this is my body, but it feels foreign.' Crucially, reality-testing remains entirely intact. What is the diagnosis?",
        "options": [
            {"id": "A", "text": "Schizophrenia, first-episode catatonia"},
            {"id": "B", "text": "Somatic Delusional Disorder"},
            {"id": "C", "text": "Depersonalization/Derealization Disorder"},
            {"id": "D", "text": "Temporal Lobe Complex Partial Epilepsy with psychosis"}
        ],
        "correctAnswer": "C",
        "explanation": "Depersonalization/Derealization Disorder is characterized by persistent or recurrent experiences of depersonalization (unreality or detachment from one's mind, self, or body) and/or derealization (unreality or detachment from surroundings). A mandatory diagnostic criterion is that reality-testing remains intact throughout the episodes, distinguishing it from psychotic disorders.",
        "incorrectExplanations": {
            "A": "In schizophrenia, reality testing is impaired and delusional explanations are adopted.",
            "B": "Delusional disorder involves unshakeable false beliefs without intact reality-testing.",
            "C": "Depersonalization/Derealization Disorder features feeling detached from oneself or surroundings while reality-testing remains fully intact.",
            "D": "Epileptic seizures involve paroxysmal EEG discharges and post-ictal confusion, which are absent here."
        },
        "learningObjective": "Differentiate Depersonalization/Derealization Disorder from psychotic conditions based on intact reality testing.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Depersonalization/Derealization Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q286",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Foundation",
        "questionText": "A 35-year-old driver survives a catastrophic highway pileup in which several motorists died. In the emergency department, the driver has no physical head injury or intoxication, yet cannot recall any memories from the moment of the crash until arriving at the hospital 3 hours later. How is this memory loss classified?",
        "options": [
            {"id": "A", "text": "Anterograde amnesia secondary to Korsakoff syndrome"},
            {"id": "B", "text": "Transient global amnesia"},
            {"id": "C", "text": "Malingered amnesia for secondary insurance compensation"},
            {"id": "D", "text": "Dissociative Amnesia, localized type"}
        ],
        "correctAnswer": "D",
        "explanation": "Dissociative Amnesia is characterized by an inability to recall important autobiographical information, usually of a traumatic or stressful nature, that is inconsistent with ordinary forgetfulness. In localized amnesia, the individual fails to recall all events that occurred during a circumscribed period of time (such as the traumatic crash).",
        "incorrectExplanations": {
            "A": "Korsakoff syndrome results from chronic thiamine deficiency in alcohol use disorder, causing anterograde amnesia and confabulation.",
            "B": "Transient global amnesia involves sudden anterograde amnesia and repetitive questioning in older adults without specific trauma.",
            "C": "Malingering requires evidence of deliberate falsification for secondary gain, which is not indicated here.",
            "D": "Dissociative Amnesia (localized) specifically involves memory loss for a discrete traumatic period without neuro-organic insult."
        },
        "learningObjective": "Identify Dissociative Amnesia and differentiate localized from generalized amnesic patterns.",
        "reference": "Spiegel, D., et al. (2011). Dissociative disorders in DSM-5. Depression and Anxiety, 28(12), 824-852.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q287",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 42-year-old bank clerk mysteriously vanishes from their home city following a major corporate crisis. Two months later, they are located 800 miles away working as a gardener under a completely new name. They have no recollection of their previous identity, family, or profession. What clinical specifier applies to this presentation of Dissociative Amnesia?",
        "options": [
            {"id": "A", "text": "With dissociative fugue"},
            {"id": "B", "text": "With somatoform wandering"},
            {"id": "C", "text": "With catatonic excitement"},
            {"id": "D", "text": "With depersonalized delirium"}
        ],
        "correctAnswer": "A",
        "explanation": "Under DSM-5-TR, Dissociative Amnesia includes the specifier 'with dissociative fugue'. A dissociative fugue involves purposeful travel or bewildered wandering that is associated with amnesia for one's identity or for other important autobiographical information, often accompanied by the assumption of a partial or new identity.",
        "incorrectExplanations": {
            "A": "Dissociative fugue involves unexpected travel away from home combined with amnesia for identity.",
            "B": "Somatoform wandering is not a recognized diagnostic entity.",
            "C": "Catatonic excitement involves purposeless, non-goal-directed motor frenzy.",
            "D": "Depersonalized delirium is an invalid clinical construct."
        },
        "learningObjective": "Recognize the diagnostic criteria and clinical features of Dissociative Amnesia with dissociative fugue.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Dissociative Amnesia.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q288",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 29-year-old patient reports severe recurrent memory lapses where hours or days go missing. During these periods, acquaintances state the patient dresses completely differently, speaks with a distinct dialect, uses a different name, and behaves aggressively. The patient finds unfamiliar clothes and handwritten notes in their home with different handwriting. Which disorder is described?",
        "options": [
            {"id": "A", "text": "Borderline Personality Disorder with micropsychotic episodes"},
            {"id": "B", "text": "Dissociative Identity Disorder (DID)"},
            {"id": "C", "text": "Schizophrenia, paranoid subtype"},
            {"id": "D", "text": "Bipolar I Disorder, rapid cycling mania"}
        ],
        "correctAnswer": "B",
        "explanation": "Dissociative Identity Disorder (DID) is characterized by: (1) A disruption of identity characterized by two or more distinct personality states (alters), involving marked discontinuity in sense of self and agency; and (2) Recurrent gaps in the recall of everyday events, important personal information, and/or traumatic events that are inconsistent with ordinary forgetfulness.",
        "incorrectExplanations": {
            "A": "BPD involves identity diffusion and affective instability, but not discrete distinct personality states with amnesic barriers.",
            "B": "DID is defined by two or more distinct personality states with recurrent amnesia for daily events.",
            "C": "Schizophrenia involves delusions, hallucinations, and thought disorganization, not separate distinct executive identities.",
            "D": "Bipolar rapid cycling involves mood switches, not distinct dissociated identity states with amnesia."
        },
        "learningObjective": "Identify DSM-5-TR diagnostic criteria for Dissociative Identity Disorder (DID).",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Dissociative Identity Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q289",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 32-year-old patient is admitted to a neurology ward presenting with sudden right leg paralysis. Neurological testing reveals Hoover's sign is positive (involuntary hip extension of the paralyzed leg when flexing the contralateral hip against resistance). Organic neurology workups (MRI, EMG) are normal. What condition is demonstrated, and how should nursing staff understand its conscious intent?",
        "options": [
            {"id": "A", "text": "Malingering; the patient is consciously simulating weakness to obtain disability payments"},
            {"id": "B", "text": "Factitious Disorder; the patient is deliberately injecting neurotoxins to assume the sick role"},
            {"id": "C", "text": "Functional Neurological Disorder (Conversion Disorder); the neurological deficit is involuntary, internally inconsistent, and not deliberately feigned"},
            {"id": "D", "text": "Guillain-Barre syndrome; the patient has acute inflammatory demyelinating polyneuropathy"}
        ],
        "correctAnswer": "C",
        "explanation": "Functional Neurological Disorder (Conversion Disorder) involves one or more symptoms of altered voluntary motor or sensory function that show clinical findings providing clear evidence of incompatibility between the symptom and recognized neurological or medical conditions (e.g., positive Hoover's sign). Crucially, the deficit is not consciously feigned or produced; it is an involuntary neuropsychiatric manifestation.",
        "incorrectExplanations": {
            "A": "Malingering involves conscious, intentional production of symptoms for external material/legal gain.",
            "B": "Factitious disorder involves intentional falsification without external incentive to adopt the sick role.",
            "C": "Functional Neurological Disorder involves genuine, involuntary symptoms with clinical evidence of internal inconsistency (e.g., positive Hoover's sign).",
            "D": "Guillain-Barre presents with ascending flaccid paralysis and absent reflexes with albuminocytologic dissociation on LP."
        },
        "learningObjective": "Differentiate Functional Neurological Disorder (Conversion Disorder) from malingering and factitious disorder.",
        "reference": "Stone, J., et al. (2010). Who is referred to neurology clinics? The diagnoses of 3781 new patients. Clinical Neurology and Neurosurgery, 112(9), 747-751.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q290",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Intermediate",
        "questionText": "During a therapeutic conversation on an inpatient unit, a trauma survivor suddenly stops speaking, stares blankly into space, does not respond to verbal calls, and experiences acute dissociative detachment. Which immediate nursing intervention provides the most effective sensory grounding?",
        "options": [
            {"id": "A", "text": "Shake the patient vigorously by the shoulders and shout their name into their ear"},
            {"id": "B", "text": "Immediately administer 10 mg intramuscular haloperidol for acute psychotic stupor"},
            {"id": "C", "text": "Leave the patient alone in an unlit seclusion room until the dissociation naturally resolves"},
            {"id": "D", "text": "Use a calm, orienting voice to guide sensory grounding: placing feet firmly on the floor, holding an ice cube, and naming 5 visible objects in the room (5-4-3-2-1 technique)"}
        ],
        "correctAnswer": "D",
        "explanation": "Sensory grounding interventions activate the sensory cortex and re-orient the dissociating individual to the here-and-now present physical environment. The nurse speaks calmly, encourages physical anchoring (feet on the floor, holding an ice cube or textured object), and guides the 5-4-3-2-1 sensory technique (naming 5 things seen, 4 touched, 3 heard, 2 smelled, 1 tasted).",
        "incorrectExplanations": {
            "A": "Vigorous physical shaking is perceived as an assault and can trigger traumatic flashbacks and panic.",
            "B": "Dissociation is not psychosis; antipsychotics are ineffective and inappropriate for dissociative episodes.",
            "C": "Abandoning the patient in isolation heightens terror and deepens dissociative withdrawal.",
            "D": "Calm verbal orientation combined with sensory grounding (feet on floor, ice cube, 5-4-3-2-1 technique) safely re-anchors the patient."
        },
        "learningObjective": "Implement evidence-based sensory grounding techniques for acute dissociative states in mental health nursing.",
        "reference": "International Society for the Study of Trauma and Dissociation. (2011). Guidelines for treating dissociative identity disorder in adults. Journal of Trauma & Dissociation, 12(2), 115-187.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q291",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Advanced",
        "questionText": "According to van der Hart, Nijenhuis, and Steele's Theory of Structural Dissociation of the Personality, how are the divided components of personality conceptualized in severe complex trauma and Dissociative Identity Disorder?",
        "options": [
            {"id": "A", "text": "Division between the Apparently Normal Part of the personality (ANP) dedicated to daily living and emotional avoidance, and one or more Emotional Parts (EP) that hold traumatic memories and defensive actions"},
            {"id": "B", "text": "Division between conscious superego moral censorship and unconscious id instinctual aggression"},
            {"id": "C", "text": "Division between right hemisphere linguistic faculties and left hemisphere motor reflexes"},
            {"id": "D", "text": "Complete separation of the sympathetic fight response from the parasympathetic rest response at the level of the spinal cord"}
        ],
        "correctAnswer": "A",
        "explanation": "The Theory of Structural Dissociation posits that traumatic stress causes a failure of psychobiological integration, dividing the personality into: (1) The Apparently Normal Part (ANP), which manages daily survival tasks and avoids trauma-related stimuli; and (2) One or more Emotional Parts (EP), which remain fixated in traumatic memories, reliving the trauma and maintaining evolutionary defensive responses (fight, flight, freeze, submit).",
        "incorrectExplanations": {
            "A": "Structural dissociation divides personality into the Apparently Normal Part (ANP) and Emotional Parts (EP).",
            "B": "This describes classical Freudian structural psychoanalytic theory, not the trauma model of structural dissociation.",
            "C": "Hemispheric division is an anatomical split-brain concept, not structural personality dissociation.",
            "D": "Spinal cord autonomic separation is a physiological misstatement."
        },
        "learningObjective": "Explain the Theory of Structural Dissociation of the Personality in trauma and dissociative disorders.",
        "reference": "van der Hart, O., Nijenhuis, E. R., & Steele, K. (2006). The Haunted Self: Structural Dissociation and the Treatment of Chronic Traumatization. W.W. Norton & Co.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q292",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Advanced",
        "questionText": "A 30-year-old patient repeatedly presents to multiple hospitals under aliases with fabricated medical histories, injecting contaminated saliva into subcutaneous tissues to induce recurrent polymicrobial sepsis and undergo multiple laparotomies. When evaluated, there is no evidence of financial gain, evasion of criminal prosecution, or obtaining opioids. How does Factitious Disorder (Munchausen syndrome) differ from Malingering?",
        "options": [
            {"id": "A", "text": "Factitious Disorder is caused by an inherited autosomal dominant enzyme defect"},
            {"id": "B", "text": "Factitious Disorder involves deliberate fabrication of symptoms driven by an internal psychological motivation to adopt the sick role, whereas Malingering is motivated by external secondary incentives (money, avoiding prosecution, housing)"},
            {"id": "C", "text": "Factitious Disorder involves unconscious somatic symptoms, whereas Malingering is an involuntary tic disorder"},
            {"id": "D", "text": "Factitious Disorder is exclusively diagnosed in children under age 10"},
        ],
        "correctAnswer": "B",
        "explanation": "In Factitious Disorder (Munchausen syndrome), the patient intentionally feigns, exaggerates, or induces physical or psychological symptoms in the absence of obvious external rewards, driven by an unconscious, internal psychological need to assume the sick role and receive medical attention. In Malingering, symptom fabrication is driven by clear, external secondary gain (such as financial compensation, dodging military duty, or obtaining prescription drugs).",
        "incorrectExplanations": {
            "A": "Factitious disorder is a psychiatric disorder, not an inherited genetic metabolic disease.",
            "B": "Factitious disorder is driven by the internal need to adopt the sick role; malingering is driven by external secondary gain.",
            "C": "Factitious symptoms are consciously and deliberately fabricated, unlike conversion disorder.",
            "D": "Factitious disorder occurs predominantly in adults, though Factitious Disorder Imposed on Another (by proxy) involves adult perpetrators and child victims."
        },
        "learningObjective": "Differentiate Factitious Disorder from Malingering based on motivational incentives.",
        "reference": "Bass, C., & Halligan, P. (2014). Factitious disorders and malingering: challenges for clinical assessment and management. The Lancet, 383(9926), 1422-1432.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q293",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Advanced",
        "questionText": "A 22-year-old patient brought to the emergency department is mute, motionless, and unresponsive to verbal questions following a severe psychosocial breakup. Neurological examination reveals normal pupillary reflexes, active resistance to eyelid opening with the eyes turning upward upon forced opening (Bell's phenomenon), intact blink reflex to menace, and normal muscle tone without waxy flexibility or lead-pipe rigidity. How is Dissociative Stupor distinguished from Catatonic Stupor?",
        "options": [
            {"id": "A", "text": "Dissociative stupor presents with elevated serum creatine kinase above 10,000 IU/L"},
            {"id": "B", "text": "Catatonic stupor responds only to surgical craniotomy, whereas dissociative stupor requires dialysis"},
            {"id": "C", "text": "Dissociative stupor lacks classic catatonic motor signs (catalepsy, waxy flexibility, posturing, negativism), shows active resistance to eye opening with normal muscle tone, and follows a severe psychogenic stressor"},
            {"id": "D", "text": "Dissociative stupor requires continuous electroencephalographic epileptiform spike-and-wave discharges"}
        ],
        "correctAnswer": "C",
        "explanation": "Dissociative stupor is characterized by profound diminution or absence of voluntary movement and responsiveness to external stimuli, but normal muscle tone, preserved physiological reflexes, active resistance to forced eyelid opening (often with eye deviation away from the examiner), and the absence of catatonic motor signs (waxy flexibility, catalepsy, posturing). It occurs in direct temporal relation to a traumatic psychosocial stressor.",
        "incorrectExplanations": {
            "A": "Elevated CK is a hallmark of Neuroleptic Malignant Syndrome or rhabdomyolysis, not dissociative stupor.",
            "B": "Neither condition requires craniotomy or dialysis; catatonia responds to benzodiazepines or ECT.",
            "C": "Dissociative stupor lacks specific catatonic motor phenomena (waxy flexibility) and exhibits active resistance to eyelid opening.",
            "D": "EEG in dissociative stupor shows normal wakeful alpha rhythms without epileptiform discharges."
        },
        "learningObjective": "Distinguish Dissociative Stupor from catatonic stupor and organic coma in acute psychiatric triage.",
        "reference": "World Health Organization. (2018). ICD-11. Dissociative neurological symptom disorder, with stupor.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q294",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Dissociative Disorders",
        "difficulty": "Expert",
        "questionText": "Functional neuroimaging studies by Lanius and colleagues in patients experiencing acute trauma-related dissociation reveal which distinct neurobiological signature compared to individuals experiencing hyperarousal/flashbacks?",
        "options": [
            {"id": "A", "text": "Complete absence of cerebral blood flow across the occipital lobes"},
            {"id": "B", "text": "Marked hyperactivation of the left temporal lobe and cerebellar vermis"},
            {"id": "C", "text": "Profound shutdown of the ventromedial prefrontal cortex accompanied by hyperarousal tachycardia"},
            {"id": "D", "text": "Hyperactivation of the medial prefrontal cortex and rostral anterior cingulate cortex, resulting in top-down emotional overmodulation and suppression of amygdala activity"}
        ],
        "correctAnswer": "D",
        "explanation": "Lanius and colleagues demonstrated two distinct neurobiological phenotypes in response to trauma reminders: (1) The hyperarousal/re-experiencing phenotype, characterized by prefrontal failure and massive amygdalar hyperactivation; and (2) The dissociative phenotype, characterized by emotional overmodulation, where hyperactivation of the medial prefrontal cortex (mPFC) and rostral anterior cingulate cortex (rACC) aggressively inhibits and shuts down the amygdala, producing subjective emotional detachment, depersonalization, and numbing.",
        "incorrectExplanations": {
            "A": "Occipital blood flow shutdown does not represent the corticolimbic dissociative circuit.",
            "B": "Temporal and vermis hyperactivity are not the validated markers of dissociative emotional overmodulation.",
            "C": "Shutdown of vmPFC with tachycardia reflects the hyperarousal phenotype, which is the exact opposite of dissociation.",
            "D": "Prefrontal hyperactivation suppressing the amygdala (emotional overmodulation) is the neuroimaging hallmark of dissociation."
        },
        "learningObjective": "Synthesize the neurocircuitry of emotional overmodulation and prefrontal-amygdalar dynamics in dissociative states.",
        "reference": "Lanius, R. A., et al. (2010). Emotion modulation in PTSD: clinical and neurobiological evidence for a dissociative subtype. American Journal of Psychiatry, 167(6), 640-647.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 9: Feeding and Eating Disorders (Q295 - Q304)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q295",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Foundation",
        "questionText": "A 19-year-old woman is admitted with a body mass index (BMI) of 14.8 kg/m2. She restricts intake to 400 kcal daily, exercises obsessively for 3 hours every day, expresses an intense terror of becoming fat, and insists her protruding clavicles and sunken abdomen are 'dangerously obese.' She denies bingeing or purging. Which diagnosis and subtype are present?",
        "options": [
            {"id": "A", "text": "Anorexia Nervosa, restricting type"},
            {"id": "B", "text": "Anorexia Nervosa, binge-eating/purging type"},
            {"id": "C", "text": "Bulimia Nervosa, non-purging type"},
            {"id": "D", "text": "Avoidant/Restrictive Food Intake Disorder (ARFID)"}
        ],
        "correctAnswer": "A",
        "explanation": "Anorexia Nervosa requires: (1) Restriction of energy intake leading to significantly low body weight in the context of age, sex, developmental trajectory, and physical health; (2) Intense fear of gaining weight or becoming fat; and (3) Disturbance in the way in which one's body weight or shape is experienced. The restricting type applies when during the last 3 months, weight loss is accomplished primarily through dieting, fasting, and/or excessive exercise without recurrent episodes of binge eating or purging.",
        "incorrectExplanations": {
            "A": "Severe low weight (BMI 14.8), body image distortion, weight fear, and caloric restriction define Anorexia Nervosa, restricting type.",
            "B": "The binge-eating/purging subtype requires recurrent episodes of binge eating or purging (vomiting, laxatives) during the past 3 months.",
            "C": "Bulimia Nervosa requires recurrent binge eating, compensatory behaviors, and maintenance of normal or above-normal weight.",
            "D": "ARFID explicitly excludes disturbance in body image and fear of weight gain."
        },
        "learningObjective": "Apply DSM-5-TR diagnostic criteria to categorize Anorexia Nervosa and its subtypes.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Anorexia Nervosa.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q296",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Foundation",
        "questionText": "A 22-year-old university student of normal weight (BMI 22.4 kg/m2) reports consuming massive quantities of high-calorie food (entire loaves of bread, tubs of ice cream) in secret 3 times a week, feeling a profound loss of control during the episodes. Following each binge, she induces self-vomiting and takes 10 stimulant laxative tablets due to extreme guilt. This behavior has occurred continuously for 5 months. What is the diagnosis?",
        "options": [
            {"id": "A", "text": "Binge-Eating Disorder with purging features"},
            {"id": "B", "text": "Bulimia Nervosa"},
            {"id": "C", "text": "Anorexia Nervosa, binge-eating/purging type"},
            {"id": "D", "text": "Atypical Anorexia Nervosa"}
        ],
        "correctAnswer": "B",
        "explanation": "Bulimia Nervosa requires: (1) Recurrent episodes of binge eating characterized by eating an abnormally large amount of food with a sense of lack of control; (2) Recurrent inappropriate compensatory behaviors to prevent weight gain (self-induced vomiting, laxative misuse, fasting, excessive exercise); (3) The behaviors occur, on average, at least once a week for 3 months; and (4) Self-evaluation is unduly influenced by body shape and weight. Crucially, the individual is NOT underweight.",
        "incorrectExplanations": {
            "A": "Binge-Eating Disorder explicitly excludes recurrent inappropriate compensatory behaviors like vomiting and laxatives.",
            "B": "Normal body weight combined with recurrent binges and compensatory purging defines Bulimia Nervosa.",
            "C": "Anorexia Nervosa binge-eating/purging type strictly requires significantly low body weight (BMI < 18.5), which is absent here.",
            "D": "Atypical anorexia involves significant weight loss but weight remains within or above normal range, without bingeing/purging cycles."
        },
        "learningObjective": "Differentiate Bulimia Nervosa from Anorexia Nervosa and Binge-Eating Disorder based on weight and compensatory behaviors.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Bulimia Nervosa.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q297",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 38-year-old accountant with a BMI of 33.2 kg/m2 describes weekly episodes where they consume large pizzas, family-sized packs of crisps, and boxes of chocolates within 90 minutes until feeling uncomfortably full, experiencing disgust, depression, and intense guilt afterward. They never vomit, take laxatives, or fast. What is the primary diagnosis?",
        "options": [
            {"id": "A", "text": "Bulimia Nervosa, non-purging subtype"},
            {"id": "B", "text": "Prader-Willi Syndrome"},
            {"id": "C", "text": "Binge-Eating Disorder (BED)"},
            {"id": "D", "text": "Substance Use Disorder (food addiction)"}
        ],
        "correctAnswer": "C",
        "explanation": "Binge-Eating Disorder (BED) is characterized by recurrent episodes of binge eating occurring, on average, at least once a week for 3 months. Binge episodes are associated with at least 3 of: eating much more rapidly than normal, eating until uncomfortably full, eating large amounts when not hungry, eating alone out of embarrassment, and feeling disgusted/depressed/guilty. Crucially, BED lacks inappropriate compensatory behaviors (purging, fasting).",
        "incorrectExplanations": {
            "A": "Bulimia Nervosa non-purging subtype was removed in DSM-5; compensatory behaviors are required for bulimia.",
            "B": "Prader-Willi is a genetic deletion syndrome presenting with neonatal hypotonia, dysmorphic features, and hyperphagia.",
            "C": "Recurrent binges with distress in the absolute absence of compensatory purging define Binge-Eating Disorder.",
            "D": "Food addiction is not an official DSM-5-TR diagnosis; BED is the correct classification."
        },
        "learningObjective": "Identify DSM-5-TR criteria for Binge-Eating Disorder.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Binge-Eating Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q298",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Intermediate",
        "questionText": "An 8-year-old child refuses to eat foods that are crunchy, textured, or green, restricting intake solely to smooth vanilla custard and plain white bread. The child has experienced severe nutritional deficiencies and faltering growth, but exhibits zero concern regarding body weight, zero fear of becoming fat, and no distortion in body image. Which feeding and eating disorder is represented?",
        "options": [
            {"id": "A", "text": "Anorexia Nervosa, atypical childhood form"},
            {"id": "B", "text": "Pica with sensory processing sensitivity"},
            {"id": "C", "text": "Rumination Disorder"},
            {"id": "D", "text": "Avoidant/Restrictive Food Intake Disorder (ARFID)"}
        ],
        "correctAnswer": "D",
        "explanation": "Avoidant/Restrictive Food Intake Disorder (ARFID) is an eating or feeding disturbance manifested by persistent failure to meet appropriate nutritional and/or energy needs associated with significant weight loss, nutritional deficiency, or dependence on enteral feeding/supplements. It is commonly driven by sensory sensitivity to food characteristics, lack of interest in eating, or fear of aversive consequences (e.g., choking), and explicitly lacks body image disturbance.",
        "incorrectExplanations": {
            "A": "Anorexia Nervosa requires fear of fatness and disturbance in body image, which are absent in ARFID.",
            "B": "Pica is the persistent eating of non-nutritive, non-food substances (e.g., dirt, paint, chalk).",
            "C": "Rumination disorder involves repeated regurgitation of food that is re-chewed, re-swallowed, or spit out.",
            "D": "ARFID involves restrictive food intake based on sensory characteristics or aversive fear without body image concern."
        },
        "learningObjective": "Differentiate Avoidant/Restrictive Food Intake Disorder (ARFID) from Anorexia Nervosa.",
        "reference": "Bryant-Waugh, R. (2013). Avoidant restrictive food intake disorder: an overview. Journal of Eating Disorders, 1(Suppl 1), O38.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q299",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Intermediate",
        "questionText": "During a physical health assessment of a patient with suspected chronic self-induced vomiting, the mental health nurse observes calluses and abrasions on the dorsum of the patient's dominant hand, bilateral enlargement of the parotid glands, and severe erosion of dental enamel on the lingual surfaces of the maxillary incisors. What are these clinical signs called?",
        "options": [
            {"id": "A", "text": "Russell's sign, parotid hypertrophy (sialadenosis), and perimylolysis"},
            {"id": "B", "text": "Trousseau's sign, mumps, and fluorosis"},
            {"id": "C", "text": "Chvostek's sign, Mikulicz syndrome, and amelogenesis imperfecta"},
            {"id": "D", "text": "Osler's nodes, Sjogren's syndrome, and Hutchinson's incisors"}
        ],
        "correctAnswer": "A",
        "explanation": "The physical triad of chronic purging consists of: (1) Russell's sign: calluses or abrasions on the knuckles/dorsum of the hand caused by repeated friction against the incisors during manual gag reflex induction; (2) Sialadenosis: non-inflammatory bilateral hypertrophy of the parotid salivary glands triggered by chronic acid exposure and hyperamylasemia; and (3) Perimylolysis: severe chemical erosion of dental enamel caused by repeated exposure to gastric hydrochloric acid.",
        "incorrectExplanations": {
            "A": "Russell's sign (knuckle calluses), sialadenosis (parotid swelling), and perimylolysis (enamel erosion) indicate chronic purging.",
            "B": "Trousseau's sign indicates hypocalcemia; mumps is viral parotitis; fluorosis is excess fluoride exposure.",
            "C": "Chvostek's sign indicates hypocalcemia; Mikulicz syndrome involves benign lymphoepithelial lesions.",
            "D": "Osler's nodes indicate infective endocarditis; Hutchinson's incisors indicate congenital syphilis."
        },
        "learningObjective": "Recognize the physical examination signs of chronic self-induced vomiting and purging.",
        "reference": "Mehler, P. S., & Rylander, M. (2015). Bulimia Nervosa - medical complications. Journal of Eating Disorders, 3, 12.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q300",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 17-year-old patient with severe anorexia nervosa (BMI 12.2 kg/m2) is started on high-calorie oral refeeding. Within 48 hours, the patient develops profound peripheral edema, muscular weakness, confusion, and ventricular arrhythmias. Serum biochemistry reveals severe hypophosphatemia, hypokalemia, and hypomagnesemia. What life-threatening metabolic complication has occurred?",
        "options": [
            {"id": "A", "text": "Ketoacidotic hyperosmolar crisis"},
            {"id": "B", "text": "Refeeding Syndrome"},
            {"id": "C", "text": "Acute adrenal crisis (Addisonian storm)"},
            {"id": "D", "text": "Wernicke-Korsakoff encephalopathy monopathy"}
        ],
        "correctAnswer": "B",
        "explanation": "Refeeding syndrome is a potentially fatal metabolic complication occurring when malnourished patients receive rapid nutritional reintroduction. Ingested carbohydrates stimulate insulin secretion, driving phosphate, potassium, and magnesium into cells for glycolysis and ATP synthesis. This precipitously depletes extracellular serum levels, triggering severe hypophosphatemia (cardiac failure, arrhythmias, rhabdomyolysis, seizures, death).",
        "incorrectExplanations": {
            "A": "Diabetic ketoacidosis involves insulin deficiency and hyperglycemia, not refeeding-induced insulin-driven electrolyte shift.",
            "B": "Refeeding syndrome presents with severe hypophosphatemia, cardiac arrhythmias, and fluid shifts upon refeeding.",
            "C": "Adrenal crisis causes hyperkalemia and hyponatremia, not profound hypophosphatemia.",
            "D": "Wernicke's encephalopathy is caused by thiamine deficiency (ataxia, ophthalmoplegia, confusion) without the profound multi-electrolyte crash."
        },
        "learningObjective": "Explain the pathophysiology and clinical manifestations of Refeeding Syndrome in severe anorexia nervosa.",
        "reference": "National Institute for Health and Care Excellence. (2017). Eating disorders: recognition and treatment (NICE Guideline NG69). London: NICE.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q301",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Advanced",
        "questionText": "According to the MARSIPAN / MEED (Medical Emergencies in Eating Disorders) guidelines, which combination of physical assessment parameters indicates 'extremely high medical risk' mandating urgent medical admission?",
        "options": [
            {"id": "A", "text": "BMI of 17.5 kg/m2, blood pressure 110/70 mmHg, and heart rate 65 bpm"},
            {"id": "B", "text": "Weight loss of 0.2 kg over 4 weeks, serum potassium 4.2 mmol/L, and core body temperature 36.8 C"},
            {"id": "C", "text": "BMI < 13 kg/m2, heart rate < 40 bpm, systolic blood pressure < 90 mmHg, core temperature < 35.5 C, and QTc interval > 460 ms"},
            {"id": "D", "text": "Isolated serum sodium of 134 mmol/L with normal physical examination"}
        ],
        "correctAnswer": "C",
        "explanation": "Under MARSIPAN (now MEED) guidelines, criteria denoting critical medical instability include: BMI < 13 kg/m2; rapid weight loss (>1 kg/week); bradycardia with pulse < 40 bpm; hypotension (systolic BP < 90 mmHg or diastolic < 60 mmHg); postural blood pressure drop > 20 mmHg; hypothermia (temperature < 35.5 C); and prolonged QTc interval (>440 ms in males, >460 ms in females), indicating imminent risk of fatal cardiac arrest.",
        "incorrectExplanations": {
            "A": "These parameters represent mild/moderate status, not critical high-risk medical instability.",
            "B": "These parameters are normal and do not meet emergency MARSIPAN thresholds.",
            "C": "BMI <13, pulse <40, BP <90, temp <35.5 C, and QTc >460 ms are red-flag indicators of critical medical emergency.",
            "D": "Mild hyponatremia in isolation does not constitute a critical medical emergency."
        },
        "learningObjective": "Apply MARSIPAN/MEED risk assessment criteria to triage medical emergencies in severe anorexia nervosa.",
        "reference": "Royal College of Psychiatrists. (2022). Medical Emergencies in Eating Disorders (MEED): Guidance on Recognition and Management (CR233). London.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q302",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Advanced",
        "questionText": "In a specialist eating disorder service, the nurse conducts the 'Sit-Up Squat-Stand' (SUSS) test. The patient cannot sit up from a supine position without rolling over and pushing with their hands, and cannot rise from a deep squat without pulling on furniture. What does a failing score on this bedside test signify?",
        "options": [
            {"id": "A", "text": "Cerebellar ataxia requiring urgent neuroimaging"},
            {"id": "B", "text": "Conversion paralysis indicating dissociative motor dysfunction"},
            {"id": "C", "text": "Tardive dyskinesia secondary to antipsychotic blockade"},
            {"id": "D", "text": "Severe proximal muscle wasting and myopathy, correlating with critical medical morbidity and cardiac collapse"},
        ],
        "correctAnswer": "D",
        "explanation": "The Sit-Up Squat-Stand (SUSS) test is a validated clinical bedside tool used in eating disorder units to assess proximal muscle weakness and catabolism. A failing score (score 0 or 1 on either the sit-up or squat-stand component) reflects critical proximal myopathy from muscle protein catabolism, which closely parallels cardiac muscle atrophy, indicating imminent medical mortality risk.",
        "incorrectExplanations": {
            "A": "The test measures proximal muscle power (myopathy), not cerebellar dysmetria or ataxia.",
            "B": "The muscle weakness is caused by profound metabolic and protein catabolism, not conversion disorder.",
            "C": "Tardive dyskinesia involves involuntary choreoathetoid movements, not proximal muscle weakness.",
            "D": "A failing SUSS test identifies severe proximal muscle wasting that correlates directly with cardiac muscle atrophy and mortality."
        },
        "learningObjective": "Utilize the Sit-Up Squat-Stand (SUSS) test to detect severe muscle catabolism in anorexia nervosa.",
        "reference": "Royal College of Psychiatrists. (2022). Medical Emergencies in Eating Disorders (CR233). Appendix 2.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q303",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Advanced",
        "questionText": "Following meals on an inpatient specialist eating disorder unit, what is the standard evidenced nursing protocol regarding patient supervision?",
        "options": [
            {"id": "A", "text": "Supervise patients in a communal, therapeutic lounge for at least 1 to 2 hours post-meal with locked access to private bathrooms"},
            {"id": "B", "text": "Encourage patients to immediately retire to private bedrooms for solitary relaxation"},
            {"id": "C", "text": "Mandate 60 minutes of intensive cardiovascular treadmill exercise to assist gastrointestinal motility"},
            {"id": "D", "text": "Allow unrestricted bathroom access to promote autonomy and personal dignity"}
        ],
        "correctAnswer": "A",
        "explanation": "Post-prandial nursing care on inpatient eating disorder units requires direct 1:1 or group supervision in a communal area for at least 60 to 120 minutes following meals. This prevents compensatory purging (vomiting), disposal of hidden food, or excessive post-meal physical exercising. Bathrooms are kept locked, or supervised if essential, while nurses provide distraction and containment for severe post-meal anxiety.",
        "incorrectExplanations": {
            "A": "Direct supervision for 1-2 hours post-meal with locked bathrooms prevents purging and hidden exercise.",
            "B": "Retiring to private rooms unobserved facilitates immediate self-induced vomiting and exercising.",
            "C": "Cardiovascular exercise is contraindicated in acute refeeding due to cardiac strain and energy deficit.",
            "D": "Unrestricted bathroom access during high-anxiety post-meal windows reliably leads to covert purging."
        },
        "learningObjective": "Formulate evidence-based nursing protocols for post-prandial containment in eating disorder units.",
        "reference": "Robinson, P. H. (2009). Severe and Enduring Eating Disorders: A Clinician's Guide. Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q304",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Feeding and Eating Disorders",
        "difficulty": "Expert",
        "questionText": "Which neuroendocrine adaptive profile is typically identified in laboratory evaluations of patients with severe restricting-type anorexia nervosa?",
        "options": [
            {"id": "A", "text": "Marked elevations of luteinizing hormone (LH), follicle-stimulating hormone (FSH), and systemic estradiol"},
            {"id": "B", "text": "Hypothalamic hypogonadotropic hypogonadism (suppressed LH and FSH), sick euthyroid syndrome (low triiodothyronine [T3] with normal TSH), elevated resting growth hormone, and hypercortisolemia"},
            {"id": "C", "text": "Profound suppression of basal cortisol with toxic elevations of serum leptin"},
            {"id": "D", "text": "Severe primary thyroid failure with massive TSH elevations and undetectable reverse T3"}
        ],
        "correctAnswer": "B",
        "explanation": "Starvation in anorexia nervosa triggers systemic neuroendocrine conservation: (1) Hypothalamic amenorrhea / hypogonadotropic hypogonadism: GnRH pulsatility ceases, suppressing LH, FSH, and estrogens; (2) Sick euthyroid syndrome: peripheral conversion of T4 to active T3 is shunted to inactive reverse T3 to lower basal metabolic rate; (3) HPA-axis hyperactivity: elevated baseline cortisol to maintain gluconeogenesis; and (4) Elevated growth hormone (due to target tissue resistance) combined with markedly suppressed leptin (reflecting adipose depletion).",
        "incorrectExplanations": {
            "A": "LH, FSH, and estradiol are profoundly suppressed in functional hypothalamic amenorrhea, not elevated.",
            "B": "Starvation features suppressed LH/FSH, low T3 with normal TSH (sick euthyroid), high growth hormone, and high cortisol.",
            "C": "Cortisol is elevated (hypercortisolemia) and leptin is profoundly suppressed due to loss of fat mass.",
            "D": "TSH is typically normal in sick euthyroid syndrome, and reverse T3 is elevated, not undetectable."
        },
        "learningObjective": "Synthesize the neuroendocrine adaptations to starvation in severe Anorexia Nervosa.",
        "reference": "Miller, K. K. (2011). Endocrine dysregulation in anorexia nervosa. Endocrinology and Metabolism Clinics of North America, 40(1), 71-88.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 10: Neurodevelopmental Disorders (Q305 - Q314)
    # -------------------------------------------------------------
    {
        "id": "MHN-Q305",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Foundation",
        "questionText": "According to DSM-5-TR, what is the minimum number of inattentive and/or hyperactive-impulsive symptoms required to diagnose Attention-Deficit/Hyperactivity Disorder (ADHD) in an adult aged 17 or older, and by what age must several symptoms have been present?",
        "options": [
            {"id": "A", "text": "At least 4 symptoms; must have been present before age 6"},
            {"id": "B", "text": "At least 6 symptoms; must have been present before age 18"},
            {"id": "C", "text": "At least 5 symptoms in either category; several symptoms must have been present prior to age 12"},
            {"id": "D", "text": "At least 8 symptoms; must have been present prior to age 15"}
        ],
        "correctAnswer": "C",
        "explanation": "DSM-5-TR specifies that for older adolescents and adults (age 17 and older), at least 5 symptoms of inattention and/or at least 5 symptoms of hyperactivity and impulsivity are required (compared to 6 symptoms for children). Additionally, Criterion B mandates that several inattentive or hyperactive-impulsive symptoms must have been present prior to age 12 years.",
        "incorrectExplanations": {
            "A": "4 symptoms is below the diagnostic threshold, and age 6 was the obsolete DSM-IV criterion.",
            "B": "6 symptoms is required for children under 17, but adults require 5, and onset must be before age 12, not 18.",
            "C": "Adults require at least 5 symptoms, with several symptoms present prior to age 12.",
            "D": "8 symptoms is an excessively high threshold not supported by DSM-5-TR."
        },
        "learningObjective": "Identify DSM-5-TR diagnostic thresholds and age-of-onset criteria for adult ADHD.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Attention-Deficit/Hyperactivity Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q306",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Foundation",
        "questionText": "Under DSM-5-TR, Autism Spectrum Disorder (ASD) is characterized by persistent impairment across which two core diagnostic domains?",
        "options": [
            {"id": "A", "text": "Visual hallucinations and Auditory hallucinations"},
            {"id": "B", "text": "Fluctuating mood elevation and Catatonic motor stupor"},
            {"id": "C", "text": "Intellectual disability and Conduct disorder"},
            {"id": "D", "text": "Persistent deficits in social communication and social interaction, AND restricted, repetitive patterns of behavior, interests, or activities"}
        ],
        "correctAnswer": "D",
        "explanation": "DSM-5-TR defines Autism Spectrum Disorder around two fundamental domains: Criterion A: Persistent deficits in social communication and social interaction across multiple contexts (social-emotional reciprocity, nonverbal communication, developing/maintaining relationships); and Criterion B: Restricted, repetitive patterns of behavior, interests, or activities (stereotyped motor movements, insistence on sameness, highly fixated interests, sensory hyper/hypo-reactivity).",
        "incorrectExplanations": {
            "A": "Hallucinations are psychotic symptoms, not diagnostic criteria for ASD.",
            "B": "Mood fluctuations define affective disorders, not the core autism domains.",
            "C": "Intellectual disability and conduct disorder are separate conditions that may co-occur but do not define ASD.",
            "D": "Social communication/interaction deficits AND restricted/repetitive behaviors constitute the two core ASD domains."
        },
        "learningObjective": "Define the two cardinal diagnostic domains of Autism Spectrum Disorder under DSM-5-TR.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Autism Spectrum Disorder.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q307",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Intermediate",
        "questionText": "To establish a diagnosis of Intellectual Disability (Intellectual Developmental Disorder) under DSM-5-TR, which triad of criteria must be met during the developmental period?",
        "options": [
            {"id": "A", "text": "Deficits in intellectual functions (reasoning, problem solving, abstract thinking), deficits in adaptive functioning (conceptual, social, practical domains), and onset during the developmental period"},
            {"id": "B", "text": "Isolated IQ score below 85, lack of employment history, and physical dysmorphic facial features"},
            {"id": "C", "text": "Presence of chromosomal trisomy, severe motor paralysis, and total absence of verbal language"},
            {"id": "D", "text": "Executive memory impairment, choreiform tremors, and onset after age 65"}
        ],
        "correctAnswer": "A",
        "explanation": "DSM-5-TR criteria for Intellectual Disability require: (1) Deficits in intellectual functions (reasoning, problem-solving, planning, abstract thinking, judgment, confirmed by clinical assessment and standardized intelligence testing); (2) Deficits in adaptive functioning that result in failure to meet developmental and sociocultural standards for personal independence and social responsibility across conceptual, social, and practical domains; and (3) Onset of intellectual and adaptive deficits during the developmental period.",
        "incorrectExplanations": {
            "A": "Intellectual deficits, adaptive functioning deficits across domains, and developmental onset define Intellectual Disability.",
            "B": "An IQ below 85 represents borderline intellectual functioning, not intellectual disability (typically < 70 +/- 5).",
            "C": "Chromosomal anomalies and motor paralysis are not required for diagnosis.",
            "D": "Onset after age 65 defines dementia or major neurocognitive disorder, not developmental intellectual disability."
        },
        "learningObjective": "Explain DSM-5-TR diagnostic criteria for Intellectual Disability, emphasizing adaptive functioning over strict IQ cutoffs.",
        "reference": "American Psychiatric Association. (2022). DSM-5-TR. Intellectual Disability (Intellectual Developmental Disorder).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q308",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 34-year-old manager presents with chronic disorganisation, severe procrastination, losing essential work files, internal mental restlessness, difficulty sitting through long board meetings, and impulsive emotional outbursts when frustrated. School reports from childhood note: 'bright but daydreamer, rarely completes assignments on time.' Which clinical presentation does this represent?",
        "options": [
            {"id": "A", "text": "Early-onset Vascular Dementia"},
            {"id": "B", "text": "Adult Attention-Deficit/Hyperactivity Disorder (ADHD), combined presentation"},
            {"id": "C", "text": "Type 1 Bipolar Mania"},
            {"id": "D", "text": "Antisocial Personality Disorder with malingering"}
        ],
        "correctAnswer": "B",
        "explanation": "Adult ADHD frequently manifests as executive dysfunction (procrastination, time blindness, disorganisation), chronic inattention (losing items, mind wandering), and internalized hyperactivity/impulsivity (inner motor restlessness, difficulty tolerating stillness, emotional dysregulation). Childhood history confirming similar difficulties fulfills the developmental onset requirement.",
        "incorrectExplanations": {
            "A": "Vascular dementia causes progressive cognitive loss following cerebrovascular accidents, not lifelong executive difficulties.",
            "B": "Adult ADHD (combined presentation) features executive inattention and internalized hyperactivity/impulsivity dating back to childhood.",
            "C": "Bipolar mania is episodic with grandiosity and decreased need for sleep, rather than chronic lifelong trait-based executive disorganization.",
            "D": "The presentation involves executive cognitive struggle, not antisocial disregard for laws and violence."
        },
        "learningObjective": "Identify adult presentations of ADHD and reconstruct childhood developmental trajectories.",
        "reference": "Kooij, S. J., et al. (2019). Updated European Consensus Statement on diagnosis and treatment of adult ADHD. European Psychiatry, 56, 14-34.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q309",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Intermediate",
        "questionText": "An autistic adult inpatient on a busy, noisy psychiatric ward experiences an 'autistic meltdown'—screaming, covering their ears, and curling into a ball on the floor. A junior staff member suggests this is 'deliberate oppositional behavior requiring physical restraint.' How should the specialist mental health nurse correct this understanding and intervene?",
        "options": [
            {"id": "A", "text": "Agree with restraint, as behavioral defiance must be curtailed immediately"},
            {"id": "B", "text": "Initiate high-dose intramuscular zuclopenthixol acetate to suppress aggressive vocalizations"},
            {"id": "C", "text": "Recognize that autistic meltdowns represent involuntary neurological overload from sensory overstimulation; reduce auditory/visual stimuli, provide a low-arousal quiet space, avoid physical touch, and give time to de-escalate"},
            {"id": "D", "text": "Place the patient in a cold bath to reset the autonomic parasympathetic tone"}
        ],
        "correctAnswer": "C",
        "explanation": "An autistic meltdown is not purposeful, defiant, or manipulative behavior; it is an intense involuntary response to overwhelming sensory, emotional, or cognitive overstimulation. Staff must apply a 'Low-Arousal Approach': eliminate noise, dim bright lights, give physical space, avoid touch, use minimal verbal communication, and allow the individual time to recover autonomic equilibrium.",
        "incorrectExplanations": {
            "A": "Restraint is traumatic, dangerous, and directly contradicts autism best practice.",
            "B": "Chemical restraint with high-potency depots is inappropriate and harmful for sensory overload.",
            "C": "Autistic meltdowns arise from sensory overload; a low-arousal approach with sensory reduction is the gold standard.",
            "D": "Cold baths are punitive, abusive, and medically contraindicated."
        },
        "learningObjective": "Distinguish autistic sensory meltdowns from oppositional behavior and implement low-arousal nursing care.",
        "reference": "National Institute for Health and Care Excellence. (2012). Autism spectrum disorder in adults: diagnosis and management (NICE Guideline CG142). London: NICE.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q310",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Intermediate",
        "questionText": "A 28-year-old with moderate intellectual disability suddenly exhibits food refusal, pacing, insomnia, crying episodes, and self-injurious head-banging over 3 weeks. Staff dismiss the behavior as 'just part of their learning disability.' What clinical diagnostic error is occurring?",
        "options": [
            {"id": "A", "text": "Confirmation bias toward physical epilepsy"},
            {"id": "B", "text": "Actor-observer cognitive distortion"},
            {"id": "C", "text": "Munchausen syndrome by proxy"},
            {"id": "D", "text": "Diagnostic overshadowing"}
        ],
        "correctAnswer": "D",
        "explanation": "Diagnostic overshadowing occurs when clinicians erroneously attribute new emotional or behavioral changes (such as symptoms of an acute major depressive episode, physical illness, or psychosis) to the individual's pre-existing intellectual disability or autism, resulting in missed psychiatric diagnoses and delayed medical care.",
        "incorrectExplanations": {
            "A": "Confirmation bias for epilepsy does not explain attributing affective distress to learning disability.",
            "B": "Actor-observer distortion relates to social attribution theory, not clinical psychiatric misattribution.",
            "C": "Munchausen by proxy involves intentional falsification of illness in a dependent.",
            "D": "Diagnostic overshadowing is the misattribution of new psychiatric/medical symptoms to an existing developmental disability."
        },
        "learningObjective": "Define and avoid diagnostic overshadowing in intellectual disability nursing.",
        "reference": "Mason, J., & Scior, K. (2004). Diagnostic overshadowing among clinicians working with people with intellectual disabilities in the UK. Journal of Applied Research in Intellectual Disabilities, 17(2), 85-90.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q311",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Advanced",
        "questionText": "A 21-year-old female university student is repeatedly admitted to acute psychiatric units with diagnoses of Borderline Personality Disorder, Anorexia Nervosa, and chronic depression. A specialist assessment discovers she has spent years consciously mimicking neurotypical social behaviors ('camouflaging' or 'masking'), leading to profound exhaustion, sensory burnout, and shutdowns. Which underlying diagnosis has been missed due to female phenotypic presentation?",
        "options": [
            {"id": "A", "text": "Autism Spectrum Disorder (late-diagnosed female phenotype)"},
            {"id": "B", "text": "Histrionic Personality Disorder with secondary somatisation"},
            {"id": "C", "text": "Schizoaffective Disorder, bipolar type"},
            {"id": "D", "text": "Dissociative Identity Disorder with anorexic alter"}
        ],
        "correctAnswer": "A",
        "explanation": "Autistic females frequently present with a distinct phenotype characterized by social 'masking' or 'camouflaging' (intellectually studying social cues, scripting conversations, forcing eye contact). This high cognitive effort leads to chronic exhaustion, autistic burnout, sensory overload, and secondary anxiety, depression, and eating disorders. They are frequently misdiagnosed with BPD or primary eating disorders.",
        "incorrectExplanations": {
            "A": "Autistic females often mask their deficits, leading to late diagnosis following burnout and misdiagnosis as BPD or eating disorders.",
            "B": "Histrionic PD involves theatrical attention-seeking, not exhausted social masking and sensory burnout.",
            "C": "Schizoaffective disorder involves delusions and hallucinations, which are not present.",
            "D": "Masking does not represent separate dissociative identity states."
        },
        "learningObjective": "Recognize the female autism phenotype, the impact of camouflaging/masking, and common diagnostic misattributions.",
        "reference": "Hull, L., et al. (2017). 'Putting on my best normal': social camouflaging in adults with autism spectrum conditions. Journal of Autism and Developmental Disorders, 47(8), 2519-2534.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q312",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Advanced",
        "questionText": "Prior to initiating psychostimulant therapy (such as methylphenidate or lisdexamfetamine) in an adult diagnosed with ADHD, which baseline physiological assessments are clinically mandatory under NICE guidelines?",
        "options": [
            {"id": "A", "text": "Serum lithium level and 24-hour urinary free cortisol"},
            {"id": "B", "text": "Comprehensive cardiovascular history (family sudden death, syncope), baseline pulse, blood pressure, and an ECG if cardiac risk factors are identified"},
            {"id": "C", "text": "Lumbar puncture for cerebrospinal fluid opening pressure and oligoclonal bands"},
            {"id": "D", "text": "Serum copper, ceruloplasmin, and visual evoked potentials"}
        ],
        "correctAnswer": "B",
        "explanation": "NICE NG87 guidelines state that before starting medication for ADHD, a full medical history must be taken, including: personal/family history of sudden cardiac death, syncope with exercise, or cardiac structural abnormalities; baseline cardiovascular examination including blood pressure and pulse (plotted on a centile chart for children); and an electrocardiogram (ECG) if there is any cardiac history or signs.",
        "incorrectExplanations": {
            "A": "Lithium levels and urinary cortisol are irrelevant to stimulant initiation.",
            "B": "Comprehensive cardiovascular assessment (pulse, BP, personal/family cardiac history, ECG if indicated) is mandatory.",
            "C": "Lumbar puncture is an invasive neurological test with no indication in routine ADHD workups.",
            "D": "Copper and ceruloplasmin test for Wilson's disease, not stimulant baseline workup."
        },
        "learningObjective": "Identify mandatory baseline pre-treatment medical screening requirements for ADHD pharmacotherapy.",
        "reference": "National Institute for Health and Care Excellence. (2018). Attention deficit hyperactivity disorder: diagnosis and management (NICE Guideline NG87). London: NICE.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q313",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Advanced",
        "questionText": "The national STOMP campaign (Stopping Over-Medication of People with a learning disability, autism or both) is a major quality-improvement initiative across healthcare. What is the primary objective of STOMP?",
        "options": [
            {"id": "A", "text": "Mandating lifelong depot antipsychotic injections for all individuals with intellectual disabilities to prevent hospital admissions"},
            {"id": "B", "text": "Eliminating all oral antibiotic usage across community residential group homes"},
            {"id": "C", "text": "Stopping the inappropriate prescribing of psychotropic medications (antipsychotics, sedatives) to manage behaviors that challenge, promoting non-pharmacological Positive Behavioural Support (PBS) instead"},
            {"id": "D", "text": "Restricting the use of vitamin D supplements in children with neurodevelopmental conditions"}
        ],
        "correctAnswer": "C",
        "explanation": "STOMP (Stopping Over-Medication of People with a learning disability, autism or both with psychotropic medicines) is an NHS initiative aimed at stopping the inappropriate prescribing of psychotropic medicines (antipsychotics, antidepressants, mood stabilizers). Psychotropics were historically overused as chemical restraints to control 'behaviors that challenge.' STOMP promotes regular medication reviews and non-pharmacological Positive Behaviour Support (PBS).",
        "incorrectExplanations": {
            "A": "Mandating depots is the exact opposite of STOMP's goal to eliminate inappropriate chemical restraint.",
            "B": "STOMP focuses on psychotropic medications, not antibiotics.",
            "C": "STOMP aims to reduce inappropriate psychotropic prescribing and implement Positive Behavioural Support.",
            "D": "STOMP does not target vitamin D supplementation."
        },
        "learningObjective": "Explain the objectives and nursing responsibilities of the STOMP initiative in learning disability and autism care.",
        "reference": "NHS England. (2017). Stopping over medication of people with a learning disability, autism or both (STOMP). Leeds: NHS England.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q314",
        "module": "3. Psychopathology and Psychiatric Diagnosis",
        "topic": "Neurodevelopmental Disorders",
        "difficulty": "Expert",
        "questionText": "Which chromosomal microdeletion syndrome is associated with a 25- to 30-fold increased risk of developing schizophrenia in adulthood, typically preceded by mild learning disabilities, velopharyngeal insufficiency (cleft palate), and congenital cardiac anomalies (conotruncal defects)?",
        "options": [
            {"id": "A", "text": "Trisomy 21 (Down syndrome)"},
            {"id": "B", "text": "Fragile X syndrome (FMR1 trinucleotide repeat)"},
            {"id": "C", "text": "Huntington's chorea (HTT CAG repeat expansion)"},
            {"id": "D", "text": "22q11.2 Deletion Syndrome (DiGeorge / Velocardiofacial syndrome)"}
        ],
        "correctAnswer": "D",
        "explanation": "22q11.2 Deletion Syndrome (also known as DiGeorge or Velocardiofacial syndrome) involves a microdeletion on chromosome 22. It presents with cardiac defects, immune dysfunction, palatal abnormalities, and mild intellectual disability. Crucially, up to 25-30% of affected individuals develop schizophrenia or schizoaffective disorder in late adolescence or adulthood, making it one of the strongest single genetic risk factors for psychotic illness.",
        "incorrectExplanations": {
            "A": "Down syndrome (Trisomy 21) is associated with early-onset Alzheimer's disease by age 40, not schizophrenia.",
            "B": "Fragile X syndrome is the most common inherited cause of intellectual disability and autism, but does not carry a 30-fold schizophrenia risk.",
            "C": "Huntington's disease causes progressive subcortical motor chorea, cognitive decline, and psychiatric changes with onset in middle age.",
            "D": "22q11.2 deletion syndrome is the classic genetic condition linking cleft palate, congenital cardiac anomalies, and a 25-30% lifetime schizophrenia risk."
        },
        "learningObjective": "Analyze the genetic neurodevelopmental link between 22q11.2 Deletion Syndrome and adult schizophrenia.",
        "reference": "Schneider, M., et al. (2014). Psychiatric disorders from childhood to adulthood in 22q11.2 deletion syndrome. American Journal of Psychiatry, 171(6), 627-639.",
        "contentReviewStatus": "Peer Reviewed"
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(MOD3_P2)} questions for Module 3 Part 2")
