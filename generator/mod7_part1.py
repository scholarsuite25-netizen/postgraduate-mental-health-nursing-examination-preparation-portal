"""
Module 7 Part 1: Questions MHN-Q615 to MHN-Q664 (50 questions)
Topics 1 to 5:
1. Assertive Community Treatment (ACT) (MHN-Q615 to MHN-Q624)
2. Psychiatric rehabilitation principles (MHN-Q625 to MHN-Q634)
3. Community Mental Health Centre (CMHC) services (MHN-Q635 to MHN-Q644)
4. Case management models (MHN-Q645 to MHN-Q654)
5. Supported employment and vocational rehabilitation (MHN-Q655 to MHN-Q664)
"""

QUESTIONS_MOD7_PART1 = [
    # -------------------------------------------------------------------------
    # Topic 1: Assertive Community Treatment (ACT) (MHN-Q615 - MHN-Q624)
    # Target Answers: B, A, C, D, A, C, B, D, A, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q615",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Foundation",
        "questionText": "A mental health trust is commissioning a new Assertive Community Treatment (ACT) service for service users with severe and persistent mental illness. According to established high-fidelity ACT model standards (such as TMACT), what is the recommended maximum staff-to-client caseload ratio?",
        "options": [
            {"id": "A", "text": "1 staff member to 25-30 clients"},
            {"id": "B", "text": "1 staff member to 10 clients"},
            {"id": "C", "text": "1 staff member to 50 clients"},
            {"id": "D", "text": "1 staff member to 3-5 clients"}
        ],
        "correctAnswer": "B",
        "explanation": "High-fidelity Assertive Community Treatment (ACT) models mandate an intensive multidisciplinary caseload ratio of no more than 1:10 (one full-time equivalent staff member per 10 clients). This low ratio ensures frequent in-vivo contact, rapid crisis response, and comprehensive shared care delivery without compromising safety.",
        "incorrectExplanations": {
            "A": "A ratio of 1:25-30 is characteristic of standard community mental health teams or intensive case management, not ACT.",
            "C": "A ratio of 1:50 reflects traditional brokerage case management, which lacks assertive outreach capacity.",
            "D": "A ratio of 1:3-5 is unnecessarily restrictive and typical of acute inpatient units or specialized forensic step-down wards."
        },
        "learningObjective": "Identify structural staffing standards and caseload ratios mandated by high-fidelity Assertive Community Treatment models.",
        "reference": "Stein, L. I., & Santos, A. B. (1998). Assertive Community Treatment of Persons with Severe Mental Illness. W.W. Norton & Co.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q616",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Foundation",
        "questionText": "An ACT community mental health nurse is planning their weekly schedule. What percentage of client contacts should ideally occur 'in vivo' (in natural community settings such as the client's home, workplace, or neighbourhood) according to evidence-based fidelity criteria?",
        "options": [
            {"id": "A", "text": "At least 75% to 80% of all face-to-face contacts"},
            {"id": "B", "text": "Between 20% and 30% of contacts, with the remainder in clinical outpatient consultation rooms"},
            {"id": "C", "text": "Exactly 50% divided equally between clinic offices and client residences"},
            {"id": "D", "text": "10% in the community, primarily during acute discharge transitions"}
        ],
        "correctAnswer": "A",
        "explanation": "A defining hallmark of high-fidelity ACT is delivering services 'in vivo'—directly within the client's natural life environment (homes, parks, workplaces, cafes). Established ACT fidelity scales (DACTS and TMACT) require that at least 75% to 80% of all client service contacts occur outside the psychiatric clinic office.",
        "incorrectExplanations": {
            "B": "Providing only 20-30% of contacts in the community violates core ACT fidelity criteria and mirrors traditional outpatient clinics.",
            "C": "A 50/50 split falls well below the required 75-80% threshold required for ACT fidelity accreditation.",
            "D": "Restricting community contacts to 10% during discharge is typical of standard inpatient liaison, not assertive outreach."
        },
        "learningObjective": "Explain the in-vivo service delivery requirements that differentiate ACT from clinic-based outpatient care.",
        "reference": "Monroe-DeVita, M., et al. (2011). The Tool for Measurement of Assertive Community Treatment (TMACT). Psychiatric Services, 62(7), 743-748.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q617",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Foundation",
        "questionText": "In contrast to conventional individual case management models where a single practitioner manages their own caseload, how does an ACT team structure clinical responsibility for enrolled clients?",
        "options": [
            {"id": "A", "text": "Individual caseworkers operate entirely autonomously without peer debriefing"},
            {"id": "B", "text": "Client care is outsourced to contracted third-party agencies every four weeks"},
            {"id": "C", "text": "The entire multidisciplinary team shares collective clinical responsibility for every client through daily organizational meetings"},
            {"id": "D", "text": "Only the consultant psychiatrist directly interacts with clients, while nurses manage administrative tasks"}
        ],
        "correctAnswer": "C",
        "explanation": "ACT operates on a shared-caseload principle where the entire multidisciplinary team (psychiatrists, nurses, social workers, vocational specialists, peer workers) shares clinical responsibility for every client. Daily morning organizational meetings are held to review every client, adjust treatment plans, and schedule visits.",
        "incorrectExplanations": {
            "A": "Autonomous individual caseloads define traditional case management, which is prone to clinician burnout and coverage gaps.",
            "B": "ACT delivers comprehensive direct services rather than subcontracting or brokering care out to external agencies.",
            "D": "ACT is an egalitarian multidisciplinary team model where nurses, social workers, and specialists provide frontline in-vivo interventions."
        },
        "learningObjective": "Contrast the shared multidisciplinary caseload structure of ACT with traditional individual casework models.",
        "reference": "Bond, G. R., & Drake, R. E. (2015). Assertive Community Treatment: Model, fidelity, and evidence. Family and Community Health, 38(2), 121-128.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q618",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Intermediate",
        "questionText": "A community psychiatric nurse is triaging referrals for an Assertive Community Treatment team. Which of the following individuals most clearly meets the priority admission criteria for an ACT program?",
        "options": [
            {"id": "A", "text": "A 19-year-old university student presenting with mild situational adjustment disorder and exam anxiety"},
            {"id": "B", "text": "A 45-year-old with stable major depressive disorder who attends monthly outpatient psychodynamic psychotherapy independently"},
            {"id": "C", "text": "A 62-year-old with vascular dementia who requires assistance with activities of daily living and physical nursing home placement"},
            {"id": "D", "text": "A 32-year-old with treatment-resistant schizophrenia, severe functional impairment, co-occurring substance dependence, and 6 involuntary admissions in the past 12 months due to disengagement"}
        ],
        "correctAnswer": "D",
        "explanation": "ACT is reserved for individuals with severe and persistent mental illness (SPMI, primarily schizophrenia spectrum or severe bipolar disorder) accompanied by severe functional impairment, frequent psychiatric rehospitalizations, high emergency service utilization, and a pattern of inability to engage with standard clinic-based outpatient services.",
        "incorrectExplanations": {
            "A": "Mild adjustment disorders are effectively managed through primary care counselling or student mental health services.",
            "B": "A stable patient capable of regular outpatient attendance does not require the resource-intensive outreach of an ACT team.",
            "C": "Vascular dementia requiring nursing home placement requires psychogeriatric or social care services rather than community psychiatric rehabilitation."
        },
        "learningObjective": "Evaluate client eligibility criteria for Assertive Community Treatment based on severity of illness and service utilization.",
        "reference": "NICE. (2014). Psychosis and schizophrenia in adults: prevention and management (NICE Guideline CG178).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q619",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Intermediate",
        "questionText": "Systematic reviews and Cochrane meta-analyses examining Assertive Community Treatment (ACT) have demonstrated the strongest and most consistent empirical evidence for which primary clinical outcome?",
        "options": [
            {"id": "A", "text": "Substantial reduction in psychiatric hospital bed days and marked improvement in housing stability"},
            {"id": "B", "text": "Complete eradication of psychotic positive symptoms within 6 months of enrollment"},
            {"id": "C", "text": "Complete cure of underlying neurocognitive deficits in schizophrenia"},
            {"id": "D", "text": "Immediate elimination of all co-occurring tobacco and substance dependence"}
        ],
        "correctAnswer": "A",
        "explanation": "The strongest and most replicated empirical evidence supporting ACT is its efficacy in significantly reducing psychiatric hospitalizations, decreasing emergency department visits, improving housing stability, and increasing engagement and treatment retention among individuals with severe mental illness.",
        "incorrectExplanations": {
            "B": "ACT improves engagement and social functioning, but it does not completely eliminate positive psychotic symptoms.",
            "C": "Neurocognitive deficits in schizophrenia are enduring traits that are not cured by intensive community models.",
            "D": "While ACT incorporates integrated dual disorder treatment, substance use reduction is gradual and rarely eliminated immediately."
        },
        "learningObjective": "Appraise empirical evidence regarding clinical and health system outcomes of Assertive Community Treatment.",
        "reference": "Dieterich, M., et al. (2017). Assertive community treatment for people with severe mental disorders. Cochrane Database of Systematic Reviews, (1), CD001089.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q620",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Intermediate",
        "questionText": "A service user on an ACT caseload experiences acute persecutory delusions and distress at 22:00 on a Saturday night. In accordance with high-fidelity ACT guidelines, how should crisis coverage be structured for this service user?",
        "options": [
            {"id": "A", "text": "The client should be directed to leave a voicemail that will be reviewed on Monday morning"},
            {"id": "B", "text": "The client must be redirected to generic police emergency dispatch with no nursing involvement"},
            {"id": "C", "text": "Direct 24/7 on-call coverage provided by ACT clinicians who personally know the client and can intervene directly in person if necessary"},
            {"id": "D", "text": "Emergency services should automatically dispatch an ambulance for compulsory hospital admission without community triage"}
        ],
        "correctAnswer": "C",
        "explanation": "High-fidelity ACT mandates 24-hour, 7-day-a-week direct crisis coverage provided by members of the ACT team itself. Because team members know the client, their personalized crisis triggers, and de-escalation strategies, they can provide immediate in-person or telephone crisis support to prevent unnecessary trauma and hospitalization.",
        "incorrectExplanations": {
            "A": "Leaving voicemails until Monday morning is standard outpatient protocol, completely contrary to ACT emergency availability.",
            "B": "Relying on generic emergency police services increases criminalization and undermines therapeutic community rapport.",
            "D": "Automatic hospital admission without evaluation contradicts the fundamental goal of ACT to provide home-based crisis stabilization."
        },
        "learningObjective": "Describe the operational delivery of 24/7 crisis intervention within Assertive Community Treatment teams.",
        "reference": "Allness, D. J., & Knoedler, W. H. (2003). A Manual for ACT Start-Up. National Alliance on Mental Illness (NAMI).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q621",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Advanced",
        "questionText": "A healthcare commissioner suggests that service users in an ACT program should be automatically discharged after a mandatory 6-month period to improve throughput. As an advanced psychiatric nurse leader, how should you critique this proposal based on ACT principles?",
        "options": [
            {"id": "A", "text": "Support the proposal, as short-term episodic care produces superior long-term clinical stability in treatment-refractory schizophrenia"},
            {"id": "B", "text": "Refute the proposal, explaining that high-fidelity ACT provides time-unlimited, continuous services because arbitrary discharge frequently precipitates relapse and rehospitalization"},
            {"id": "C", "text": "Suggest reducing the time limit to 8 weeks, as intensive behavioral conditioning occurs strictly within the first two months"},
            {"id": "D", "text": "Agree with mandatory discharge but insist that clients be transferred exclusively to inpatient custodial facilities"}
        ],
        "correctAnswer": "B",
        "explanation": "A core structural principle of ACT is its time-unlimited, longitudinal commitment. Research has repeatedly demonstrated that when clients with severe and persistent mental illness are arbitrarily transitioned off ACT to less intensive care based on predetermined calendar dates rather than sustained clinical readiness, rates of relapse, homelessness, and rehospitalization spike dramatically.",
        "incorrectExplanations": {
            "A": "Short-term episodic models have been shown to fail repeatedly in the severe and persistent mental illness population.",
            "C": "An 8-week limit is clinically inappropriate and contradicts the entire evidence base of psychiatric rehabilitation.",
            "D": "Mandatory transfer to custodial inpatient facilities reverses the goals of community integration and recovery."
        },
        "learningObjective": "Critique service commissioning proposals regarding duration of care in Assertive Community Treatment based on recovery literature.",
        "reference": "Bond, G. R., et al. (2001). Assertive community treatment for people with severe mental illness: Critical ingredients and impact on patients. Disease Management & Health Outcomes, 9(3), 141-159.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q622",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Advanced",
        "questionText": "An ACT psychiatric nurse visits a client with schizophrenia living in permanent supportive housing who is refusing oral antipsychotic medication due to severe akathisia and dry mouth. What is the nurse's most clinically appropriate, recovery-oriented action?",
        "options": [
            {"id": "A", "text": "Threaten the client with immediate eviction from their apartment unless they ingest the medication immediately in front of the nurse"},
            {"id": "B", "text": "Contact emergency police services to immediately execute an emergency detention order without medical assessment"},
            {"id": "C", "text": "Respectfully discontinue all future community visits, discharging the client from the ACT service for non-compliance"},
            {"id": "D", "text": "Acknowledge the distressing side effects, conduct a formal extrapyramidal symptom assessment (e.g., BARS or SAS), and collaborate with the team psychiatrist to adjust medication or treat the akathisia"}
        ],
        "correctAnswer": "D",
        "explanation": "Medication management in ACT is collaborative and problem-solving oriented. Acknowledging distressing subjective adverse effects, systematically assessing akathisia, and coordinating immediate pharmacological adjustments (e.g., dose reduction, switching antipsychotics, adding propranolol) addresses the root cause of refusal while maintaining engagement and autonomy.",
        "incorrectExplanations": {
            "A": "Using housing as leverage violates both tenancy rights and ethical nursing practice.",
            "B": "Involuntary detention is unwarranted for side effect-driven medication hesitancy without imminent risk.",
            "C": "Discharging clients when they refuse medication violates ACT's assertive engagement and zero-drop-out mandate."
        },
        "learningObjective": "Formulate recovery-oriented nursing interventions to resolve antipsychotic non-adherence arising from adverse neurological side effects in community settings.",
        "reference": "Boyd, M. A. (2022). Psychiatric Nursing: Contemporary Practice (7th ed.). Wolters Kluwer.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q623",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Advanced",
        "questionText": "A service user enrolled in an ACT team presents with co-occurring severe schizoaffective disorder and chronic polysubstance dependence (alcohol and crack cocaine). Which integrated intervention model should the ACT nurse employ to maximize treatment engagement?",
        "options": [
            {"id": "A", "text": "Integrated Dual Disorder Treatment (IDDT) utilizing harm reduction and stage-wise motivational interviewing within the same clinical team"},
            {"id": "B", "text": "Serial treatment requiring total abstinence for 6 months in a separate addiction facility before addressing psychiatric symptoms"},
            {"id": "C", "text": "Parallel treatment requiring simultaneous attendance at two competing, uncoordinated community clinics with conflicting goals"},
            {"id": "D", "text": "Immediate confrontation of the client's chemical denial and refusal of all mental health support until toxicology is clear"}
        ],
        "correctAnswer": "A",
        "explanation": "High-fidelity ACT incorporates Integrated Dual Disorder Treatment (IDDT). In this approach, psychiatric and substance use interventions are delivered concurrently by the same multidisciplinary team using harm reduction principles, stage-matched motivational interviewing, and personalized relapse prevention, rather than requiring pre-existing abstinence.",
        "incorrectExplanations": {
            "B": "Serial treatment has high failure rates because untreated psychiatric illness precipitates substance relapse and vice versa.",
            "C": "Parallel treatment creates contradictory therapeutic messages and results in high drop-out rates.",
            "D": "Confrontational approaches are obsolete, damage therapeutic alliance, and significantly increase client disengagement."
        },
        "learningObjective": "Apply the principles of Integrated Dual Disorder Treatment (IDDT) within community assertive outreach nursing.",
        "reference": "Drake, R. E., et al. (2001). Implementing dual diagnosis services for clients with severe mental illness. Psychiatric Services, 52(4), 469-476.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q624",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Assertive Community Treatment (ACT)",
        "difficulty": "Expert",
        "questionText": "During a formal fidelity assessment of an ACT team utilizing the Tool for Measurement of Assertive Community Treatment (TMACT), the evaluators note that the team maintains a client-to-specialist ratio of 1:10, holds daily organizational meetings, but only delivers 45% of face-to-face services in the community, and has no practicing peer specialist. How should the clinical nurse leader analyze these findings?",
        "options": [
            {"id": "A", "text": "The service achieves exemplary fidelity because caseload numbers and daily team meetings are the sole determinants of ACT efficacy"},
            {"id": "B", "text": "The service fulfills criteria for a Clubhouse psychosocial rehabilitation model rather than an outreach model"},
            {"id": "C", "text": "The service exhibits significant fidelity drift in the Core Team Structure and Community Service Delivery domains, jeopardizing expected hospitalization reduction outcomes"},
            {"id": "D", "text": "The team should immediately convert into a brokerage case management program to meet TMACT standards"}
        ],
        "correctAnswer": "C",
        "explanation": "TMACT evaluates multiple subscales across staffing, organizational boundaries, nature of services, and clinical practices. Delivering only 45% of services in the community (failing the >=75-80% threshold) and omitting peer specialists represents substantial fidelity drift. Research demonstrates that services with low fidelity fail to replicate ACT's benchmark outcomes in reducing hospital bed days.",
        "incorrectExplanations": {
            "A": "Fidelity requires compliance across all multidimensional domains, not merely caseload ratios and meetings.",
            "B": "The Clubhouse model is an intentional member-run community center, completely distinct in philosophy and structure from ACT.",
            "D": "Brokerage case management has the lowest intensity and evidence base, representing the opposite of ACT fidelity optimization."
        },
        "learningObjective": "Evaluate program fidelity using standardized evaluation instruments (TMACT) to identify fidelity drift and implement clinical remediation.",
        "reference": "Monroe-DeVita, M., et al. (2011). The Tool for Measurement of Assertive Community Treatment (TMACT). Psychiatric Services, 62(7), 743-748.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 2: Psychiatric rehabilitation principles (MHN-Q625 - MHN-Q634)
    # Target Answers: B, D, A, C, B, D, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q625",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Foundation",
        "questionText": "What is the foundational philosophy underlying recovery-oriented practice in psychiatric mental health nursing?",
        "options": [
            {"id": "A", "text": "Recovery is synonymous with complete neurobiological cure and total absence of symptoms"},
            {"id": "B", "text": "Recovery is a personal, unique process of building a meaningful, satisfying, and contributing life, regardless of ongoing psychiatric symptoms"},
            {"id": "C", "text": "Recovery can only be certified by a physician when psychotropic medication is successfully discontinued"},
            {"id": "D", "text": "Recovery requires complete conformity to normative institutional standards of behavior"}
        ],
        "correctAnswer": "B",
        "explanation": "Recovery-oriented practice posits that recovery is a deeply personal, holistic journey focused on self-determination, hope, agency, and social inclusion. It emphasizes living a purposeful, valued life in the community of one's choice, even in the presence of continuing or recurring psychiatric symptoms.",
        "incorrectExplanations": {
            "A": "Recovery in psychiatric rehabilitation is distinct from the traditional medical definition of symptom eradication or biological cure.",
            "C": "Medication decisions do not define recovery; many individuals achieve profound recovery while maintaining maintenance pharmacotherapy.",
            "D": "Imposing institutional conformity reflects an outdated asylum mindset contrary to individual autonomy and empowerment."
        },
        "learningObjective": "Define the core conceptual framework of recovery-oriented practice in modern psychiatric nursing.",
        "reference": "Anthony, W. A. (1993). Recovery from mental illness: The guiding vision of the mental health service system in the 1990s. Psychosocial Rehabilitation Journal, 16(4), 11-23.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q626",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Foundation",
        "questionText": "The Wellness Recovery Action Plan (WRAP), developed by Mary Ellen Copeland, is an evidence-based self-management system. Which of the following components constitutes a key structural section of a standard WRAP plan?",
        "options": [
            {"id": "A", "text": "The Clinician's Compulsory Treatment Directives"},
            {"id": "B", "text": "The Inpatient Bed Booking Priority Form"},
            {"id": "C", "text": "The Mandatory Diagnostic Categorization Grid"},
            {"id": "D", "text": "Triggers and Early Warning Signs paired with an Action Plan"}
        ],
        "correctAnswer": "D",
        "explanation": "A standard WRAP comprises key self-directed sections: Daily Maintenance Plan, Triggers, Early Warning Signs, When Things Are Breaking Down, Crisis Plan, and Post-Crisis Plan. Identifying triggers and early warning signs paired with concrete, proactive coping actions empowers the individual to maintain wellness.",
        "incorrectExplanations": {
            "A": "WRAP is strictly consumer-owned and authored; it is never a set of clinician-imposed directives.",
            "B": "WRAP focuses on wellness self-management in the community, not administrative hospital bed management.",
            "C": "WRAP deliberately de-emphasizes medical diagnostic labels in favor of personal experiences and coping strategies."
        },
        "learningObjective": "Identify the structural sections of the Wellness Recovery Action Plan (WRAP) used in mental health rehabilitation.",
        "reference": "Copeland, M. E. (2002). Wellness Recovery Action Plan: A system for monitoring, reducing and eliminating uncomfortable or dangerous physical and emotional symptoms. Mental Health Recovery Newsletter, 3, 1-12.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q627",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Intermediate",
        "questionText": "During a rehabilitation assessment, a psychiatric nurse focuses systematically on discovering a service user's talents, personal resilience, social networks, and personal aspirations rather than documenting pathology and deficits. Which paradigm is the nurse exemplifying?",
        "options": [
            {"id": "A", "text": "Strengths-based approach"},
            {"id": "B", "text": "Deficit-driven medical reductionism"},
            {"id": "C", "text": "Psychoanalytic drive assessment"},
            {"id": "D", "text": "Institutional behavioral conditioning"}
        ],
        "correctAnswer": "A",
        "explanation": "The strengths-based approach (championed by Rapp, Goscha, and Saleebey) shifts the focus from pathology, diagnoses, and functional deficits to identifying the person's existing abilities, coping talents, aspirations, and naturally occurring community resources to propel recovery.",
        "incorrectExplanations": {
            "B": "Deficit-driven frameworks catalog pathology and dysfunction, which can undermine hope and induce self-stigma.",
            "C": "Psychoanalytic drive assessment explores unconscious conflicts and defense mechanisms rather than conscious community strengths.",
            "D": "Behavioral conditioning focuses on shaping target behaviors through external reinforcements rather than holistic personal strengths."
        },
        "learningObjective": "Differentiate the strengths-based approach from traditional deficit-oriented psychiatric assessment models.",
        "reference": "Rapp, C. A., & Goscha, R. J. (2012). The Strengths Model: A Recovery-Oriented Approach to Mental Health Services (3rd ed.). Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q628",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Intermediate",
        "questionText": "A psychiatric rehabilitation nurse is collaborating with a client who wishes to pursue social activities. Which action best reflects the core principle of 'social inclusion'?",
        "options": [
            {"id": "A", "text": "Encouraging the client to socialize exclusively within a segregated day centre for psychiatric patients"},
            {"id": "B", "text": "Instructing the client to avoid all community interactions until their social anxiety is 100% resolved"},
            {"id": "C", "text": "Supporting the client to join an open community gardening club at the local municipal park alongside mainstream citizens"},
            {"id": "D", "text": "Restricting social interactions to monthly tele-consultations with their assigned case manager"}
        ],
        "correctAnswer": "C",
        "explanation": "Social inclusion requires enabling individuals with mental illness to participate fully in mainstream civil society, public spaces, and natural community groups (e.g., mainstream sports clubs, educational courses, arts guilds) rather than confining them to segregated, illness-dominated psychiatric enclaves.",
        "incorrectExplanations": {
            "A": "Restricting socialization to segregated psychiatric settings perpetuates institutionalization and social isolation.",
            "B": "Waiting for complete symptom resolution before community engagement is an outdated barrier that impedes recovery.",
            "D": "Professional appointments do not constitute genuine community social inclusion or peer relationships."
        },
        "learningObjective": "Apply principles of social inclusion and full citizenship when planning psychosocial interventions with clients.",
        "reference": "Boardman, J. (2011). Social inclusion and mental health. British Journal of Psychiatry, 199(6), 447-448.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q629",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Intermediate",
        "questionText": "In the Boston University Psychiatric Rehabilitation Model formulated by William Anthony and Marianne Farkas, what are the three core developmental phases through which a client progresses?",
        "options": [
            {"id": "A", "text": "Detoxification, Conditioning, and Relapse"},
            {"id": "B", "text": "Diagnosis (Readiness Assessment), Planning, and Intervention (Skills Development/Environmental Support)"},
            {"id": "C", "text": "Paternalistic containment, Institutional habituation, and Discharge"},
            {"id": "D", "text": "Symptom suppression, Pharmacological titration, and Termination"}
        ],
        "correctAnswer": "B",
        "explanation": "The Boston University Psychiatric Rehabilitation Model structures rehabilitation around three operational phases: Rehabilitation Diagnosis (assessing readiness and establishing specific environmental goals), Rehabilitation Planning (setting detailed step-by-step goals), and Rehabilitation Intervention (direct skills teaching and acquiring environmental supports).",
        "incorrectExplanations": {
            "A": "This sequence describes medical addiction withdrawal protocols, not psychiatric rehabilitation.",
            "C": "Paternalistic containment represents historical asylum practices directly opposed by psychiatric rehabilitation.",
            "D": "Symptom suppression focuses on acute biomedical stabilization rather than functional rehabilitation and community integration."
        },
        "learningObjective": "Describe the operational stages of the Boston University Psychiatric Rehabilitation Model.",
        "reference": "Anthony, W. A., & Farkas, M. D. (2009). Primer on Psychiatric Rehabilitation (3rd ed.). Boston University Center for Psychiatric Rehabilitation.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q630",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Intermediate",
        "questionText": "A service user states: 'My schizophrenia has taken away my whole identity. I used to be an engineer, a father, and a teammate.' In psychiatric rehabilitation, how is the process of re-establishing valued social identities and life positions termed?",
        "options": [
            {"id": "A", "text": "Diagnostic remission"},
            {"id": "B", "text": "Symptom desensitization"},
            {"id": "C", "text": "Regression to baseline"},
            {"id": "D", "text": "Role recovery"}
        ],
        "correctAnswer": "D",
        "explanation": "Role recovery is a central tenet of psychiatric rehabilitation that emphasizes restoring, reclaiming, or discovering valued normative social roles (e.g., student, employee, volunteer, parent, civic contributor) that transcend the stigmatizing identity of being merely a 'mental patient.'",
        "incorrectExplanations": {
            "A": "Diagnostic remission refers solely to reduction in DSM diagnostic symptoms, not the restoration of meaningful social roles.",
            "B": "Symptom desensitization is a behavioural therapy technique for phobias or trauma, not role reconstruction.",
            "C": "Regression implies psychological deterioration back to an earlier developmental stage, the opposite of growth in recovery."
        },
        "learningObjective": "Analyze the concept of role recovery and its role in rebuilding identity beyond psychiatric diagnosis.",
        "reference": "Spaniol, L., et al. (2002). The recovery process: Conceptualizing and measuring recovery. Psychiatric Rehabilitation Journal, 25(4), 327-338.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q631",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Advanced",
        "questionText": "A client with chronic bipolar disorder living independently expresses a strong desire to enroll in an evening culinary arts course. The client's family urges the mental health nurse to forbid this, fearing the stress might trigger hypomania. How should the nurse ethically and clinically navigate this situation?",
        "options": [
            {"id": "A", "text": "Agree with the family and obtain a legal guardianship order to prevent the client from enrolling in educational programs"},
            {"id": "B", "text": "Uphold the principle of the 'dignity of risk' by supporting the client's autonomous choice while collaboratively formulating a proactive wellness and stress-management contingency plan"},
            {"id": "C", "text": "Advise the client that people with affective disorders should avoid all intellectual or creative pursuits"},
            {"id": "D", "text": "Double the client's mood stabilizer medication preemptively to blunt any emotional excitement"}
        ],
        "correctAnswer": "B",
        "explanation": "The 'dignity of risk' recognizes that taking calculated personal risks and pursuing aspirations is fundamental to human dignity, growth, and self-worth. Overprotection deprives individuals of self-efficacy. Psychiatric nurses balance duty of care by co-creating proactive coping and contingency plans rather than paternalistically restricting autonomy.",
        "incorrectExplanations": {
            "A": "Depriving a competent adult of educational opportunities through legal guardianship is paternalistic and legally unjustified.",
            "C": "Disabling beliefs about affective disorders reinforce internalized stigma and learned helplessness.",
            "D": "Medication adjustments must be clinically indicated based on symptoms, not used to suppress normal human enthusiasm."
        },
        "learningObjective": "Synthesize the ethical tension between duty of care and the 'dignity of risk' in recovery-oriented nursing.",
        "reference": "Deegan, P. E. (1992). The Independent Living Movement and people with psychiatric disabilities: Taking back control over our own lives. Psychosocial Rehabilitation Journal, 15(3), 3-19.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q632",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Advanced",
        "questionText": "A client enrolled in community psychiatric rehabilitation continues to hear distressing auditory hallucinations ('voices') despite optimal clozapine therapy. Which nursing intervention aligns best with evidence-based coping strategy enhancement?",
        "options": [
            {"id": "A", "text": "Instruct the client to argue aggressively with the voices whenever they speak to prove they are false"},
            {"id": "B", "text": "Administer high-dose parenteral sedatives whenever the client reports auditory perceptions"},
            {"id": "C", "text": "Tell the client that listening to music or engaging in conversation will permanently damage their auditory cortex"},
            {"id": "D", "text": "Collaborate with the client to systematically test behavioral coping strategies (e.g., listening to personal music with headphones, subvocal counting, focused activity) to enhance perceived control over the voices"}
        ],
        "correctAnswer": "D",
        "explanation": "Coping Strategy Enhancement (CSE) is an evidence-based cognitive-behavioral psychiatric rehabilitation intervention. When residual psychotic symptoms persist despite optimized pharmacotherapy, the nurse collaborates with the client to explore, test, and master practical compensatory cognitive and behavioural tactics (e.g. music distraction, humming, scheduled 'voice listening' times) to re-establish mastery and reduce distress.",
        "incorrectExplanations": {
            "A": "Confronting or arguing aggressively with hallucinatory voices frequently escalates emotional distress and physiological arousal.",
            "B": "Chemical sedation produces debilitating adverse effects and prevents functional cognitive mastery.",
            "C": "Music and engaging activities are well-established, safe sensory diversion techniques that do not harm the brain."
        },
        "learningObjective": "Design coping strategy enhancement interventions for individuals experiencing medication-resistant hallucinations.",
        "reference": "Tarrier, N., et al. (1993). Coping strategy enhancement in schizophrenia. Behavioural Psychotherapy, 21(1), 41-55.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q633",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Advanced",
        "questionText": "When facilitating the creation of a psychiatric advance directive or crisis plan within a client's WRAP document, what critical element must the nurse ensure is explicitly articulated to protect the client's rights and preferences during acute incapacity?",
        "options": [
            {"id": "A", "text": "Specific preferences regarding acceptable and unacceptable psychotropic medications, chosen trusted supporters, preferred treatment facilities, and designated substitute decision-makers"},
            {"id": "B", "text": "A blanket legal waiver granting clinicians immunity from medical malpractice liability"},
            {"id": "C", "text": "A complete transfer of all personal bank accounts and financial assets to the hospital administrative fund"},
            {"id": "D", "text": "A binding pledge never to request medical leave or voluntary discharge"}
        ],
        "correctAnswer": "A",
        "explanation": "A robust crisis plan / psychiatric advance statement articulates clear advance preferences: identifying early warning signs, preferred medications, treatments to avoid (due to past trauma or severe adverse effects), names and contact details of trusted family/peer supporters, preferred facilities, and clear instructions for managing domestic affairs during hospitalization.",
        "incorrectExplanations": {
            "B": "Crisis plans protect consumer self-determination; they are not legal indemnity waivers for providers.",
            "C": "Psychiatric advance planning does not involve signing over financial assets to medical institutions.",
            "D": "Crisis plans cannot be used to coerce patients into forfeiting statutory discharge or review rights."
        },
        "learningObjective": "Formulate a comprehensive psychiatric advance directive and crisis plan within a recovery framework.",
        "reference": "Henderson, C., et al. (2008). Joint crisis plans for people with psychosis: randomized controlled trial. British Journal of Psychiatry, 192(2), 152-158.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q634",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Psychiatric rehabilitation principles",
        "difficulty": "Expert",
        "questionText": "A psychiatric nurse researcher is evaluating the recovery outcomes of a newly implemented recovery academy. Rather than measuring symptom frequency on the PANSS, which validated consumer-rated instrument should the researcher select to capture personal recovery dimensions such as hope, agency, meaning, and self-advocacy?",
        "options": [
            {"id": "A", "text": "Hamilton Depression Rating Scale (HAM-D)"},
            {"id": "B", "text": "Brief Psychiatric Rating Scale (BPRS)"},
            {"id": "C", "text": "Recovery Assessment Scale (RAS) or Stages of Recovery Instrument (STORI)"},
            {"id": "D", "text": "Abnormal Involuntary Movement Scale (AIMS)"},
        ],
        "correctAnswer": "C",
        "explanation": "The Recovery Assessment Scale (RAS) and the Stages of Recovery Instrument (STORI) are validated, standardized self-report instruments specifically developed to measure personal recovery domains—including hope, confidence, goal striving, reliance on others, and overcoming biographical disruption—in contrast to clinician-rated symptom scales.",
        "incorrectExplanations": {
            "A": "The HAM-D is a clinician-rated scale measuring biological and affective symptoms of depression.",
            "B": "The BPRS evaluates clinician-observed positive, negative, and general psychiatric pathology.",
            "D": "The AIMS specifically assesses involuntary movements (tardive dyskinesia), not psychosocial recovery."
        },
        "learningObjective": "Select and evaluate validated psychometric instruments designed to measure personal recovery in mental health research.",
        "reference": "Corrigan, P. W., et al. (2004). The Recovery Assessment Scale: Reliability and validity. Psychiatric Services, 55(4), 442-444.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 3: Community Mental Health Centre (CMHC) services (MHN-Q635 - MHN-Q644)
    # Target Answers: A, C, B, D, A, C, B, A, D, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q635",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Foundation",
        "questionText": "Historically codified under landmark community mental health legislation, what are the five essential mandated core services that a comprehensive Community Mental Health Centre (CMHC) must provide to its catchment population?",
        "options": [
            {"id": "A", "text": "Outpatient services, 24-hour emergency/crisis services, day treatment/partial hospitalization, inpatient psychiatric services, and consultation/education"},
            {"id": "B", "text": "Custodial asylum detention, mandatory electroconvulsive therapy, surgical lobotomy, isolation units, and vocational factory work"},
            {"id": "C", "text": "Primary cosmetic dermatology, dental surgery, intensive care cardiology, orthopaedics, and pediatric neonatal intensive care"},
            {"id": "D", "text": "Exclusive tele-psychiatry, mail-order pharmacotherapy, private legal arbitration, and commercial real estate brokerage"}
        ],
        "correctAnswer": "A",
        "explanation": "Under the US Community Mental Health Centers Act of 1963 and subsequent international community mental health frameworks, comprehensive CMHCs were mandated to provide five core pillars: 1) Inpatient care, 2) Outpatient services, 3) Partial hospitalization/day treatment, 4) 24/7 emergency response, and 5) Community consultation and education.",
        "incorrectExplanations": {
            "B": "These represent coercive, obsolete historical asylum practices that the community mental health movement was designed to eradicate.",
            "C": "These are specialized acute physical medicine disciplines outside the specialized remit of a mental health centre.",
            "D": "These commercial services bear no resemblance to the public psychiatric mandate of community mental health centers."
        },
        "learningObjective": "Recall the five mandated core clinical components of comprehensive community mental health centers.",
        "reference": "Grob, G. N. (1991). From Asylum to Community: Mental Health Policy in Modern America. Princeton University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q636",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Foundation",
        "questionText": "In the continuum of community mental health care, what is the primary structural difference between a Partial Hospitalization Program (PHP) and an Intensive Outpatient Program (IOP)?",
        "options": [
            {"id": "A", "text": "PHP requires involuntary legal commitment, whereas IOP is strictly voluntary"},
            {"id": "B", "text": "IOP provides 24-hour inpatient bed stays, whereas PHP provides only annual reviews"},
            {"id": "C", "text": "PHP provides intensive daytime clinical programming (typically 5-6 hours/day, 5 days/week) as an alternative to acute inpatient admission, whereas IOP offers fewer hours (typically 3 hours/day, 3 days/week)"},
            {"id": "D", "text": "PHP provides only somatic electroconvulsive therapy, whereas IOP offers only recreational field trips"}
        ],
        "correctAnswer": "C",
        "explanation": "PHP (often termed 'day hospital') provides structured, multimodal clinical stabilization (typically 20-30 hours per week) for acute symptoms, serving as a step-down from inpatient care or a diversion from admission. IOP is less intensive (typically 9-12 hours per week), allowing clients to maintain employment, school, or independent living while receiving structured therapy.",
        "incorrectExplanations": {
            "A": "Both PHP and IOP are typically voluntary community ambulatory programs.",
            "B": "Neither PHP nor IOP provides overnight inpatient bed accommodation.",
            "D": "Both PHP and IOP utilize multidisciplinary psychotherapeutic, psychoeducational, and nursing modalities."
        },
        "learningObjective": "Differentiate between Partial Hospitalization Programs (PHP) and Intensive Outpatient Programs (IOP) in ambulatory community mental health.",
        "reference": "American Association for Community Psychiatry. (2010). Level of Care Utilization System (LOCUS).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q637",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Foundation",
        "questionText": "What is the primary clinical objective of a community-based Crisis Stabilization Unit (CSU) staffed by psychiatric mental health nurses?",
        "options": [
            {"id": "A", "text": "To detain individuals long-term for multi-year rehabilitation"},
            {"id": "B", "text": "To provide short-term (24 to 72 hours) rapid assessment, psychiatric de-escalation, and medical triage to avert unnecessary acute inpatient hospital admissions"},
            {"id": "C", "text": "To manage severe surgical emergencies and complex physical trauma resuscitation"},
            {"id": "D", "text": "To provide permanent residential housing for unhoused individuals with severe dementia"}
        ],
        "correctAnswer": "B",
        "explanation": "Crisis Stabilization Units (CSUs) are rapid-access, community-based bed facilities offering intensive psychiatric nursing and medical intervention for up to 24-72 hours. Their goal is prompt stabilization of acute psychological crises, safety planning, and immediate linkage to outpatient supports, preventing traumatic hospitalizations.",
        "incorrectExplanations": {
            "A": "CSUs are strictly short-term emergency facilities, not long-stay rehabilitation homes.",
            "C": "Physical trauma and surgical resuscitations require general hospital emergency departments.",
            "D": "Permanent housing is provided via supportive housing programs, not acute crisis stabilization units."
        },
        "learningObjective": "Describe the operational function and clinical objectives of Crisis Stabilization Units.",
        "reference": "Balfour, M. E., et al. (2020). Cops, Clinicians, or Both? Collaborative Approaches to Responding to Behavioral Health Emergencies. Psychiatric Services, 71(10), 1076-1078.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q638",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Intermediate",
        "questionText": "A walk-in client arrives at a community mental health outpatient clinic visibly intoxicated, tremulous, sweating profusely, and reporting auditory hallucinations telling him to walk into traffic. When triaging this presentation, what is the psychiatric nurse's immediate priority?",
        "options": [
            {"id": "A", "text": "Schedule an intake psychotherapy appointment for three weeks later and send the client home"},
            {"id": "B", "text": "Instruct the client to wait quietly in the public reception area without vital sign assessment"},
            {"id": "C", "text": "Ask the client to complete a 40-page written questionnaire regarding developmental childhood trauma"},
            {"id": "D", "text": "Conduct an immediate physical and risk assessment (including vital signs and CIWA-Ar evaluation) and initiate emergency medical transfer/admission due to life-threatening alcohol withdrawal and acute suicidality"}
        ],
        "correctAnswer": "D",
        "explanation": "Community psychiatric triage mandates evaluating physiological stability alongside psychiatric acuity. Autonomic hyperactivity (tremor, diaphoresis) combined with command auditory hallucinations in an intoxicated individual indicates potential delirium tremens and acute life-threatening safety risk requiring immediate medical stabilization.",
        "incorrectExplanations": {
            "A": "Deferring care in acute withdrawal and suicidality constitutes gross medical neglect.",
            "B": "Leaving an unmonitored patient in autonomic storm risks fatal withdrawal seizures or acute suicide.",
            "C": "Comprehensive childhood trauma intake forms are contraindicated during acute physiological crises."
        },
        "learningObjective": "Prioritize nursing triage interventions when assessing concurrent acute medical withdrawal and psychiatric risk in community clinics.",
        "reference": "Wheeler, K. (2022). Psychotherapy for the Advanced Practice Psychiatric Nurse (3rd ed.). Springer Publishing.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q639",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Intermediate",
        "questionText": "A community psychiatric nurse specialist delivers a series of educational workshops to local secondary school teachers and police officers regarding early signs of psychosis and trauma-informed de-escalation. Under which mandated CMHC service function does this intervention fall?",
        "options": [
            {"id": "A", "text": "Consultation and education"},
            {"id": "B", "text": "Custodial inpatient containment"},
            {"id": "C", "text": "Tertiary biological remediation"},
            {"id": "D", "text": "Involuntary civil prosecution"}
        ],
        "correctAnswer": "A",
        "explanation": "Consultation and education (C&E) is a foundational preventive pillar of community mental health. It involves providing professional mental health expertise, psychoeducation, and systemic training to non-mental health community gatekeepers (teachers, police, primary care, faith leaders) to enhance early case finding and reduce stigma.",
        "incorrectExplanations": {
            "B": "Asylum containment is an obsolete institutional function, not an educational community service.",
            "C": "Tertiary biological remediation refers to high-end medical treatment, not preventive public education.",
            "D": "Involuntary legal proceedings are court-directed judicial processes outside clinical education."
        },
        "learningObjective": "Explain the role of community consultation and education as a primary and secondary prevention strategy.",
        "reference": "Thornicroft, G., & Tansella, M. (2010). The Balanced Care Model for global mental health. Australian & New Zealand Journal of Psychiatry, 47(1), 11-14.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q640",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Intermediate",
        "questionText": "A community psychiatric nurse coordinates a specialized Clozapine Monitoring Clinic within a CMHC. A client established on clozapine for 3 years presents for routine scheduled blood work. The laboratory calls with an urgent Absolute Neutrophil Count (ANC) of 0.8 x 10^9/L. What is the nurse's immediate clinical protocol action?",
        "options": [
            {"id": "A", "text": "Reassure the client that this is normal, administer the monthly injection, and recheck in one month"},
            {"id": "B", "text": "Advise the client to double the clozapine dose that evening to stimulate bone marrow production"},
            {"id": "C", "text": "Immediately halt clozapine treatment, withhold further doses, urgently contact the consultant psychiatrist, repeat ANC stat, and arrange protective isolation/haematology review for severe neutropenia/agranulocytosis"},
            {"id": "D", "text": "Instruct the client to take an over-the-counter vitamin C tablet and return in two weeks"}
        ],
        "correctAnswer": "C",
        "explanation": "An Absolute Neutrophil Count (ANC) below 1.0 x 10^9/L (0.8 x 10^9/L) indicates severe neutropenia / impending agranulocytosis (a medical emergency). The nurse must immediately withhold clozapine, alert the psychiatrist, urgently reconfirm haematology, assess for signs of infection (fever, sore throat), and initiate medical/haematological protocols.",
        "incorrectExplanations": {
            "A": "An ANC of 0.8 is life-threatening; continuing clozapine risks fatal overwhelming sepsis.",
            "B": "Doubling clozapine would further suppress the bone marrow and likely prove fatal.",
            "D": "Vitamins do not treat drug-induced neutropenia; delaying action breaches mandatory safety registries."
        },
        "learningObjective": "Manage severe haematological adverse reactions and execute clozapine monitoring protocols in community psychiatric settings.",
        "reference": "Taylor, D., et al. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q641",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Advanced",
        "questionText": "People with severe mental illness die on average 15-20 years prematurely, primarily from preventable cardiovascular disease. When implementing a nurse-led physical health screening clinic in a CMHC based on the Lester UK Adaptation / Cardiometabolic Resource, which baseline metabolic monitoring battery must the nurse conduct?",
        "options": [
            {"id": "A", "text": "Cranial CT scan, cerebrospinal fluid analysis, bone marrow biopsy, and visual evoked potentials"},
            {"id": "B", "text": "Blood pressure, body mass index (BMI) and waist circumference, fasting plasma glucose or HbA1c, and fasting lipid profile"},
            {"id": "C", "text": "Serum allergen levels, 24-hour urine copper excretion, and hair mineral analysis"},
            {"id": "D", "text": "Serum lithium level and thyroid panel only, regardless of the psychotropic regimen"}
        ],
        "correctAnswer": "B",
        "explanation": "Cardiometabolic screening protocols (such as the Lester tool and ADA/APA guidelines) mandate regular assessment of five core metabolic parameters in patients receiving antipsychotics: 1) Blood pressure, 2) BMI and waist circumference, 3) Fasting blood glucose or HbA1c, 4) Fasting lipid profile, and 5) Smoking status assessment.",
        "incorrectExplanations": {
            "A": "Invasive neurological investigations are not routine screening measures for cardiometabolic disease.",
            "C": "Allergy and trace mineral testing have no diagnostic role in routine psychiatric metabolic screening.",
            "D": "Lithium monitoring is drug-specific and omits the metabolic cardiovascular syndrome caused by second-generation antipsychotics."
        },
        "learningObjective": "Implement evidence-based physical health monitoring and cardiometabolic surveillance protocols for community mental health clients.",
        "reference": "Shiers, D. E., et al. (2014). Positive Cardiometabolic Health Resource: The Lester UK Adaptation 2014. Royal College of Psychiatrists.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q642",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Advanced",
        "questionText": "A Crisis Resolution and Home Treatment (CRHT) team receives an urgent referral for an individual experiencing an acute relapse of bipolar mania. What core operational role does the CRHT nurse perform within the local mental health economy?",
        "options": [
            {"id": "A", "text": "Serving as a gatekeeper for acute psychiatric inpatient admissions by providing rapid, intensive home visits (up to twice daily) to stabilize the crisis in the community where clinically safe"},
            {"id": "B", "text": "Conducting long-term psychoanalysis over a five-year period in an office setting"},
            {"id": "C", "text": "Managing financial trusts and managing real estate portfolios for corporate clients"},
            {"id": "D", "text": "Providing compulsory custodial sentencing in forensic judicial facilities"}
        ],
        "correctAnswer": "A",
        "explanation": "Crisis Resolution and Home Treatment (CRHT) teams act as explicit gatekeepers to acute hospital beds. They provide rapid multidisciplinary assessment (within 2-4 hours) and deliver high-intensity, short-term home treatment (often visiting 1-2 times daily) to de-escalate crises and support recovery in the least restrictive environment.",
        "incorrectExplanations": {
            "B": "CRHT provides acute, short-term crisis stabilization (typically 2-6 weeks), not long-term psychodynamic therapy.",
            "C": "Financial wealth management is entirely outside the scope of acute mental health nursing.",
            "D": "CRHT is a healthcare alternative to hospitalization, not a judicial punitive body."
        },
        "learningObjective": "Analyze the gatekeeping and crisis intervention functions of Crisis Resolution and Home Treatment teams.",
        "reference": "Johnson, S., et al. (2008). Crisis Resolution and Home Treatment in Mental Health. Cambridge University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q643",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Advanced",
        "questionText": "A community psychiatric nurse notices that a client with a history of severe persecutory delusions and poor nutritional intake has missed three consecutive scheduled depot injection appointments and has not answered telephone calls. How should the nurse proactively respond to this disengagement?",
        "options": [
            {"id": "A", "text": "Send a formal letter immediately closing the client's file for non-compliance with clinic rules"},
            {"id": "B", "text": "Report the client to criminal justice authorities for medication evasion"},
            {"id": "C", "text": "Assume the client has achieved full spontaneous recovery and cease all monitoring"},
            {"id": "D", "text": "Conduct a multidisciplinary risk review, attempt assertive outreach home visits (in pairs if safety indicated), liaise with known family/housing supporters, and execute a tiered welfare check"}
        ],
        "correctAnswer": "D",
        "explanation": "Disengagement in community mental health is frequently a direct manifestation of illness exacerbation, paranoia, or acute distress. Good practice dictates assertive outreach: reviewing risk, making unannounced home visits (with appropriate safety precautions), liaising with housing staff or emergency contacts, and escalating to welfare checks before any case closure.",
        "incorrectExplanations": {
            "A": "Administrative discharge of disengaged, vulnerable psychotic patients is a leading cause of homicide, suicide, and serious untoward incidents.",
            "B": "Missing clinical appointments is not a criminal offense.",
            "C": "Abrupt cessation of antipsychotics in chronic psychosis carries high relapse risk; assuming cure is clinically unsafe."
        },
        "learningObjective": "Formulate assertive engagement and risk management strategies when responding to service user disengagement in community nursing.",
        "reference": "Department of Health. (2001). The Mental Health Policy Implementation Guide: Community Mental Health Teams. UK Department of Health.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q644",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Community Mental Health Centre (CMHC) services",
        "difficulty": "Expert",
        "questionText": "An advanced practice psychiatric nurse is commissioned to establish an evidence-based Illness Management and Recovery (IMR) group program within a CMHC. What specific psychoeducational and behavioural curriculum components must the nurse embed to ensure programmatic fidelity?",
        "options": [
            {"id": "A", "text": "Exclusive free-association dream analysis and hypnotic regression therapy"},
            {"id": "B", "text": "Intense aerobic endurance drills without psychological discussion"},
            {"id": "C", "text": "Psychoeducation regarding mental illness, behavioral tailoring for medication adherence, relapse prevention planning, social skills training, and coping strategies for persistent symptoms"},
            {"id": "D", "text": "Instruction on avoiding all healthcare providers and relying solely on alternative magnetic therapies"}
        ],
        "correctAnswer": "C",
        "explanation": "Illness Management and Recovery (IMR) is an empirically validated psychiatric rehabilitation curriculum. High-fidelity IMR integrates five core evidence-based strategies: psychoeducation on mental illness, cognitive-behavioural approaches to medication adherence, personalized relapse prevention planning, social skills training, and coping skills training for residual symptoms.",
        "incorrectExplanations": {
            "A": "Psychoanalytic dream analysis lacks evidence in psychiatric rehabilitation for SPMI.",
            "B": "Physical exercise is beneficial adjunctively, but IMR is a psychosocial illness self-management curriculum.",
            "D": "Rejecting medical evidence directly contradicts the collaborative principles of IMR."
        },
        "learningObjective": "Synthesize the modular curriculum components of high-fidelity Illness Management and Recovery (IMR) programs.",
        "reference": "Mueser, K. T., et al. (2002). Illness management and recovery for severe mental illness: A review of the research. Clinical Psychology Review, 22(8), 1272-1298.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 4: Case management models (MHN-Q645 - MHN-Q654)
    # Target Answers: B, D, A, C, B, D, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q645",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Foundation",
        "questionText": "In psychiatric community care, how is the traditional 'Brokerage' (or generalist) case management model characterized regarding direct clinical intervention?",
        "options": [
            {"id": "A", "text": "The case manager personally provides intensive psychodynamic psychotherapy and psychiatric prescribing"},
            {"id": "B", "text": "The case manager focuses primarily on assessing needs, linking/referring the client to external community services, and monitoring resource delivery, without providing direct clinical therapy"},
            {"id": "C", "text": "The case manager lives full-time in the client's home to perform household chores"},
            {"id": "D", "text": "The case manager strictly manages inpatient hospital wards with no community interface"}
        ],
        "correctAnswer": "B",
        "explanation": "The Brokerage (generalist) model functions as a coordinator or 'broker.' The case manager identifies client needs, navigates institutional bureaucracies, refers the client to external providers (housing, income support, medical clinics), and monitors service delivery, deliberately providing minimal or no direct therapeutic or clinical counseling.",
        "incorrectExplanations": {
            "A": "Brokerage managers do not provide direct psychotherapy or medical management.",
            "C": "In-home residential domestic work is outside the scope of case management.",
            "D": "Case management is an ambulatory community-based coordination function."
        },
        "learningObjective": "Differentiate the functions and limitations of the Brokerage case management model.",
        "reference": "Holloway, F. (1991). Case management for the mentally ill: Looking at the evidence. International Journal of Social Psychiatry, 37(1), 2-13.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q646",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Foundation",
        "questionText": "Unlike the pure brokerage approach, how does the 'Clinical Case Management' model operate within community mental health nursing?",
        "options": [
            {"id": "A", "text": "It eliminates all community visits in favor of postal surveys"},
            {"id": "B", "text": "It restricts the nurse's role strictly to financial audit accounting"},
            {"id": "C", "text": "It requires clients to remain in physical restraints during case management meetings"},
            {"id": "D", "text": "It combines resource coordination and systems advocacy with direct, individualized clinical interventions such as crisis therapy, supportive psychotherapy, psychoeducation, and symptom management"}
        ],
        "correctAnswer": "D",
        "explanation": "Clinical Case Management integrates traditional resource acquisition (housing, benefits, medical care) with direct, ongoing clinical therapeutic interventions (e.g., individual supportive therapy, illness psychoeducation, family intervention, crisis counseling) delivered by the same clinician who holds an established therapeutic relationship.",
        "incorrectExplanations": {
            "A": "Clinical case management requires frequent face-to-face community contact.",
            "B": "Financial auditing is an accounting function unrelated to clinical mental health nursing.",
            "C": "Physical restraints are strictly prohibited and obsolete in community practice."
        },
        "learningObjective": "Describe how Clinical Case Management integrates therapeutic clinical practice with systems navigation.",
        "reference": "Kanter, J. (1989). Clinical case management: Definition, principles, components. Hospital and Community Psychiatry, 40(4), 361-368.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q647",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Intermediate",
        "questionText": "Charles Rapp and Richard Goscha developed the Strengths Model of Case Management. Which of the following is one of the foundational principles of this model?",
        "options": [
            {"id": "A", "text": "People with severe psychiatric disabilities have the capacity to learn, grow, and change, and the community is viewed as an oasis of potential resources rather than a barrier"},
            {"id": "B", "text": "The client must acknowledge that their psychiatric diagnosis permanently restricts their potential to segregated facilities"},
            {"id": "C", "text": "Clinicians must control all decisions regarding where the client lives and works to prevent symptom relapse"},
            {"id": "D", "text": "Assessment should exclusively focus on identifying brain pathology and biological neuro-degeneration"}
        ],
        "correctAnswer": "A",
        "explanation": "The Strengths Model rests on core principles: people have intrinsic capacity for recovery and growth; natural community resources are rich sources of opportunity; the client is the director of the helping process; the therapeutic relationship is primary; and interventions occur in the community.",
        "incorrectExplanations": {
            "B": "Accepting permanent disability and segregation contradicts the fundamental philosophy of the Strengths Model.",
            "C": "Paternalistic control is rejected; client self-direction is the guiding engine of care.",
            "D": "The Strengths Model deliberately avoids pathologizing biological deficits, focusing instead on environmental assets."
        },
        "learningObjective": "Apply the philosophical principles and assessment methodologies of the Strengths Model of Case Management.",
        "reference": "Rapp, C. A., & Goscha, R. J. (2012). The Strengths Model: A Recovery-Oriented Approach to Mental Health Services (3rd ed.). Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q648",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Intermediate",
        "questionText": "What distinguishes Intensive Case Management (ICM) from Assertive Community Treatment (ACT)?",
        "options": [
            {"id": "A", "text": "ICM caseloads are much larger (1:80), whereas ACT caseloads are strictly 1:1"},
            {"id": "B", "text": "ICM is exclusively inpatient-based, whereas ACT is strictly for school-aged children"},
            {"id": "C", "text": "ICM typically relies on an individual case manager holding primary responsibility for a small caseload (1:15-20), whereas ACT utilizes a shared multidisciplinary team approach with 24/7 internal coverage and lower ratios (1:10)"},
            {"id": "D", "text": "There are no clinical or structural distinctions between ICM and ACT"}
        ],
        "correctAnswer": "C",
        "explanation": "While both models target high-need service users, ICM typically utilizes an individual practitioner holding primary responsibility for a caseload of 15-20 clients with extended hours, whereas ACT features a whole-team shared caseload, a lower staff-to-client ratio (1:10), integrated team psychiatrists and vocational specialists, and in-house 24/7 crisis response.",
        "incorrectExplanations": {
            "A": "ICM maintains relatively small caseloads (1:15-20), not 1:80.",
            "B": "Both ICM and ACT are community-based adult psychiatric services.",
            "D": "Fidelity scales clearly differentiate the team-based structure of ACT from individual-worker ICM."
        },
        "learningObjective": "Distinguish between Intensive Case Management (ICM) and Assertive Community Treatment (ACT) in organizational design.",
        "reference": "Burns, T., et al. (2007). Case management and assertive community treatment in Europe. World Psychiatry, 6(2), 102-106.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q649",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Intermediate",
        "questionText": "A mental health case manager discovers that an administrative officer at a local government housing office unlawfully rejected a client's disability tenancy application due to their psychiatric diagnosis. When performing the case management function of 'Advocacy', what is the nurse's professional responsibility?",
        "options": [
            {"id": "A", "text": "Advise the client to accept the rejection quietly because public institutions are beyond challenge"},
            {"id": "B", "text": "Challenge the discriminatory decision, lodge a formal appeal, provide necessary medical corroboration, and uphold the client's legal entitlements to equitable housing access"},
            {"id": "C", "text": "Discharge the client from mental health services due to lack of residential stability"},
            {"id": "D", "text": "Advise the client to forge official legal documents"}
        ],
        "correctAnswer": "B",
        "explanation": "Advocacy is a core professional function of psychiatric case management. The nurse is ethically and clinically obligated to confront institutional discrimination, uphold client rights under disability and equality legislation, assist with appeals, and actively navigate bureaucratic obstacles to secure entitlements.",
        "incorrectExplanations": {
            "A": "Passivity in the face of unlawful discrimination breaches professional nursing ethical standards.",
            "C": "Discharging clients because they face housing barriers abandons vulnerable individuals in crisis.",
            "D": "Encouraging illegal fraud is unethical and violates professional regulatory codes."
        },
        "learningObjective": "Demonstrate the advocacy function of psychiatric case management in confronting structural discrimination and securing entitlements.",
        "reference": "Nursing and Midwifery Council (NMC). (2018). The Code: Professional standards of practice and behaviour for nurses, midwives and nursing associates.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q650",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Intermediate",
        "questionText": "In the core case management cycle (Assessment, Planning, Linking, Monitoring, and Advocacy), what is the primary purpose of the 'Monitoring' phase?",
        "options": [
            {"id": "A", "text": "To conduct undercover surveillance to catch clients engaging in minor legal infractions"},
            {"id": "B", "text": "To ensure insurance billing occurs without clinical contact"},
            {"id": "C", "text": "To inspect the client's home daily to ensure complete military cleanliness"},
            {"id": "D", "text": "To continuously evaluate the ongoing appropriateness, quality, and efficacy of services delivered, while tracking client progress toward self-identified recovery goals and adjusting plans accordingly"}
        ],
        "correctAnswer": "D",
        "explanation": "Monitoring in case management involves regular, ongoing evaluation of whether services are meeting the client's changing needs, whether providers are delivering agreed interventions, and whether the client is progressing toward their goals. It ensures proactive problem-solving when obstacles arise.",
        "incorrectExplanations": {
            "A": "Case management is a therapeutic supportive relationship, not punitive law enforcement surveillance.",
            "B": "Monitoring focuses on clinical quality and recovery outcomes, not administrative billing loopholes.",
            "C": "Paternalistic policing of personal domestic cleanliness violates client dignity."
        },
        "learningObjective": "Explain the operational role of the monitoring phase within the standard case management continuum.",
        "reference": "Mullahy, F. (2017). The Case Manager's Handbook (6th ed.). Jones & Bartlett Learning.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q651",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Advanced",
        "questionText": "Under the Care Programme Approach (CPA) / coordinated community care framework in mental health nursing, what is the mandatory role of the designated 'Care Coordinator'?",
        "options": [
            {"id": "A", "text": "To assume sole personal financial liability for the client's utility debts"},
            {"id": "B", "text": "To act as the single point of contact responsible for coordinating comprehensive multidisciplinary assessments, convening regular multi-agency review meetings, and ensuring a documented contingency/crisis plan exists"},
            {"id": "C", "text": "To write all prescriptions without consulting the responsible medical officer"},
            {"id": "D", "text": "To restrict the client from contacting their primary care family physician"}
        ],
        "correctAnswer": "B",
        "explanation": "A Care Coordinator under CPA / collaborative care management maintains overall responsibility for coordinating holistic care. This includes completing comprehensive assessments, formulating a person-centered care plan, liaising between disparate agencies (health, housing, social care), organizing multidisciplinary reviews, and managing risk/contingency plans.",
        "incorrectExplanations": {
            "A": "Clinicians never bear personal financial liability for client civil debts.",
            "C": "Prescribing requires formal medical qualification or non-medical prescriber certification within legal frameworks.",
            "D": "Collaboration with primary care is a mandated component of coordinated care."
        },
        "learningObjective": "Analyze the statutory responsibilities of the mental health Care Coordinator within care coordination frameworks.",
        "reference": "Department of Health. (2008). Refocusing the Care Programme Approach: Policy and Positive Practice Guidance. UK Department of Health.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q652",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Advanced",
        "questionText": "A community mental health nurse has been case managing an isolated client for four years. The nurse realizes that they have begun doing personal grocery shopping for the client on weekends and withholding critical clinical observations from the multidisciplinary team to 'protect' the client. What clinical phenomenon is occurring, and how must it be resolved?",
        "options": [
            {"id": "A", "text": "Exemplary trauma-informed dedication requiring immediate clinical promotion"},
            {"id": "B", "text": "Malingering on the part of the nurse requiring immediate criminal suspension"},
            {"id": "C", "text": "A standard requirement of high-fidelity Assertive Community Treatment"},
            {"id": "D", "text": "Boundary blur and unhealthy countertransference fostering learned helplessness; the nurse must immediately bring this to clinical supervision to restore professional boundaries"}
        ],
        "correctAnswer": "D",
        "explanation": "Overinvolvement, performing tasks outside working hours, and withholding information from the multidisciplinary team indicate compromised professional boundaries and countertransference. This impairs objective assessment and fosters dependency. It must be addressed through clinical supervision to re-establish healthy therapeutic boundaries.",
        "incorrectExplanations": {
            "A": "Overstepping boundaries is not exemplary care; it compromises objective clinical judgment and patient safety.",
            "B": "Boundary drift is a clinical and supervision issue, not criminal malingering.",
            "C": "ACT emphasizes team-shared responsibility specifically to prevent unmonitored solo overinvolvement."
        },
        "learningObjective": "Critique boundary violations and countertransference dynamics in long-term community case management through reflective supervision.",
        "reference": "Austin, W., et al. (2008). The ethics of nurse-patient boundaries: A relational perspective. Ethics & Behavior, 18(2-3), 244-259.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q653",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Advanced",
        "questionText": "A service user who has achieved sustained recovery goals (stable housing, competitive employment, stable mental state for 18 months) is preparing for discharge from intensive case management to primary care. How should the nurse plan this transition?",
        "options": [
            {"id": "A", "text": "Execute a gradual, planned step-down transition involving collaborative meetings with the primary care team, updating the relapse prevention plan, and providing a rapid re-access pathway if symptoms recur"},
            {"id": "B", "text": "Abruptly terminate all contact tomorrow without notifying the client or primary care physician to build resilience"},
            {"id": "C", "text": "Inform the client that discharge from case management means they can never re-enter psychiatric care in their lifetime"},
            {"id": "D", "text": "Transfer the client immediately to an acute psychiatric inpatient bed for a 3-month observation phase"}
        ],
        "correctAnswer": "A",
        "explanation": "Discharge and transition in recovery-oriented case management is planned collaboratively and executed gradually. It involves cross-service warm handoffs to primary care, clear documentation of crisis early warning signs, formulation of a maintenance plan, and explicit, low-barrier 'fast-track' protocols for rapid re-entry if symptoms escalate.",
        "incorrectExplanations": {
            "B": "Abrupt abandonment provokes profound attachment anxiety and significantly increases relapse risk.",
            "C": "Threatening permanent exclusion from future healthcare is coercive and unethical.",
            "D": "Inpatient admission is strictly reserved for acute crises, not routine outpatient transitions."
        },
        "learningObjective": "Design a safe, recovery-oriented discharge and step-down transition protocol from specialized case management to primary care.",
        "reference": "NICE. (2016). Transition between inpatient mental health settings and community or care home settings (NICE Guideline NG53).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q654",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Case management models",
        "difficulty": "Expert",
        "questionText": "An advanced practice psychiatric nurse is leading an audit of community case management effectiveness across an integrated behavioral health trust. Rather than solely tracking bed-day utilization, which standardized needs assessment instrument should be utilized to measure reductions in unmet clinical and social needs?",
        "options": [
            {"id": "A", "text": "Glasgow Coma Scale (GCS)"},
            {"id": "B", "text": "Mini-Mental State Examination (MMSE)"},
            {"id": "C", "text": "Camberwell Assessment of Need (CAN)"},
            {"id": "D", "text": "Norton Risk Assessment Scale for Pressure Ulcers"}
        ],
        "correctAnswer": "C",
        "explanation": "The Camberwell Assessment of Need (CAN) is a gold-standard, internationally validated comprehensive needs assessment tool developed for community mental health. It systematically evaluates 22 domains of life (accommodation, food, self-care, psychotic symptoms, safety, intimate relationships, employment), distinguishing between met and unmet needs.",
        "incorrectExplanations": {
            "A": "The GCS assesses acute conscious state in neurological trauma.",
            "B": "The MMSE screens for gross cognitive impairment and dementia.",
            "D": "The Norton Scale assesses risk for cutaneous pressure sores."
        },
        "learningObjective": "Select validated epidemiological needs assessment tools (CAN) to evaluate outcomes in community mental health programs.",
        "reference": "Phelan, M., et al. (1995). The Camberwell Assessment of Need: The validity and reliability of an instrument to assess the needs of people with severe mental illness. British Journal of Psychiatry, 167(5), 589-595.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 5: Supported employment and vocational rehabilitation (MHN-Q655 - MHN-Q664)
    # Target Answers: A, C, B, D, A, C, B, A, D, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q655",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Foundation",
        "questionText": "The Individual Placement and Support (IPS) model is recognized globally as the gold-standard evidence-based approach to vocational rehabilitation in mental health. What is the central founding philosophy of IPS regarding client employment readiness?",
        "options": [
            {"id": "A", "text": "'Place then train'—rapid job search for competitive employment based on zero-exclusion, followed by ongoing individualized on-the-job support"},
            {"id": "B", "text": "'Train then place'—requiring years of unpaid pre-vocational simulation in sheltered workshops before seeking open work"},
            {"id": "C", "text": "Employment is contraindicated for anyone carrying a diagnosis of psychotic illness"},
            {"id": "D", "text": "Clients must achieve total symptom remission and test scores above the 90th percentile on IQ tests before job placement"}
        ],
        "correctAnswer": "A",
        "explanation": "IPS is founded on the 'place then train' philosophy: any individual who wants to work is eligible (zero exclusion), rapid job searching for competitive employment begins immediately without lengthy pre-vocational preparation, and continuous, time-unlimited support is provided directly on the job.",
        "incorrectExplanations": {
            "B": "The traditional 'train then place' sheltered workshop model has consistently poor competitive employment outcomes (~15-20% vs ~60% for IPS).",
            "C": "Believing people with psychosis cannot work is an outdated, stigmatizing falsehood disproven by dozens of randomized controlled trials.",
            "D": "IPS deliberately rejects pre-condition testing or clinical prerequisites."
        },
        "learningObjective": "Define the 'place-then-train' philosophy and core principles of the Individual Placement and Support (IPS) model.",
        "reference": "Drake, R. E., et al. (2012). Individual Placement and Support: An Evidence-Based Approach to Supported Employment. Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q656",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Foundation",
        "questionText": "Under high-fidelity Individual Placement and Support (IPS) principles, what type of employment is exclusively targeted for service users?",
        "options": [
            {"id": "A", "text": "Unpaid volunteer positions in psychiatric day centers"},
            {"id": "B", "text": "Sub-minimum wage manual packaging in segregated sheltered workshops"},
            {"id": "C", "text": "Competitive employment in the open labor market at minimum wage or higher, in jobs open to anyone"},
            {"id": "D", "text": "Institutional chores within the psychiatric hospital kitchen"}
        ],
        "correctAnswer": "C",
        "explanation": "IPS explicitly mandates competitive employment as its goal. Competitive employment is defined as jobs in the open, mainstream labor market that pay at least minimum wage, are not set aside exclusively for people with disabilities, and are open to any qualified applicant.",
        "incorrectExplanations": {
            "A": "Volunteering is not competitive employment and does not generate independent economic empowerment.",
            "B": "Sheltered workshops segregate disabled individuals and often exploit them at sub-minimum wages.",
            "D": "Institutional hospital chores perpetuate asylum-era institutional habituation."
        },
        "learningObjective": "Differentiate competitive employment in the open labor market from sheltered or pre-vocational work.",
        "reference": "Bond, G. R., et al. (2008). An update on Individual Placement and Support. World Psychiatry, 7(3), 177-184.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q657",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Foundation",
        "questionText": "In an IPS supported employment program, who decides the type of job a service user should pursue and whether their mental health status should be disclosed to potential employers?",
        "options": [
            {"id": "A", "text": "The hospital medical director makes binding decisions based on pharmaceutical compliance"},
            {"id": "B", "text": "The service user's individual preferences, choices, and pace dictate job selection and disclosure decisions entirely"},
            {"id": "C", "text": "The employer decides by reviewing the client's confidential electronic medical record prior to interview"},
            {"id": "D", "text": "The case manager's personal convenience and timetable"}
        ],
        "correctAnswer": "B",
        "explanation": "Consumer preference is a primary, non-negotiable IPS principle. Job searches are based on the client's personal preferences, passions, and strengths rather than clinical judgment of suitability. Furthermore, disclosing psychiatric disability to employers is entirely the client's autonomous choice.",
        "incorrectExplanations": {
            "A": "Paternalistic medical control over personal career decisions directly violates IPS fidelity.",
            "C": "Employers have no legal right to access confidential medical records without consent.",
            "D": "IPS services are consumer-driven, not tailored to staff schedules."
        },
        "learningObjective": "Identify consumer self-determination and disclosure autonomy within IPS supported employment practice.",
        "reference": "Becker, D. R., & Drake, R. E. (2003). A Working Life for People with Severe Mental Illness. Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q658",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Intermediate",
        "questionText": "A major barrier preventing people with severe mental illness from entering paid employment is the pervasive fear of immediately losing their disability pensions, subsidized housing, and state healthcare benefits. How does high-fidelity IPS address this systemic barrier?",
        "options": [
            {"id": "A", "text": "By advising clients to work strictly off-the-books in the illegal cash economy"},
            {"id": "B", "text": "By forcing clients to sign agreements forfeiting all public benefits prior to initiating a job search"},
            {"id": "C", "text": "By concealing financial information from clients so they remain unaware of benefit cuts"},
            {"id": "D", "text": "By providing comprehensive, personalized, individualized benefits counseling prior to and throughout employment, calculating work incentive rules and tax credits"}
        ],
        "correctAnswer": "D",
        "explanation": "High-fidelity IPS mandates work incentives planning and benefits counseling. Specialized benefits specialists provide detailed, personalized financial analyses explaining disability benefit rules, work incentive thresholds (e.g., Ticket to Work, permitted work rules), ensuring clients understand that they will be financially better off working without abruptly losing essential healthcare coverage.",
        "incorrectExplanations": {
            "A": "Engaging in illegal undeclared labor exposes vulnerable clients to prosecution and severe exploitation.",
            "B": "Forfeiting benefits upfront creates catastrophic financial risk and paralyzes job seeking.",
            "C": "Deception violates nursing ethics and destroys therapeutic trust."
        },
        "learningObjective": "Explain the role of individualized work incentives planning and benefits counseling in supported employment.",
        "reference": "Drake, R. E., et al. (2009). Social Security and disability beneficiaries with mental illness: A review of the literature. Journal of Occupational Rehabilitation, 19(4), 312-321.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q659",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Intermediate",
        "questionText": "Randomized controlled trials across Europe (e.g., the EQOLISE study) and North America comparing IPS against traditional vocational services (step-wise pre-vocational training/sheltered workshops) have consistently demonstrated what comparative outcome?",
        "options": [
            {"id": "A", "text": "IPS participants achieved significantly higher rates of competitive employment (~55-65% vs ~20-25%) with longer job tenure and higher total earnings"},
            {"id": "B", "text": "Traditional sheltered workshops produced vastly superior long-term executive career placements"},
            {"id": "C", "text": "Both models yielded identical, negligible employment rates of under 5%"},
            {"id": "D", "text": "IPS resulted in universal clinical deterioration and increased hospital bed days"}
        ],
        "correctAnswer": "A",
        "explanation": "Dozens of randomized controlled trials (including the seminal European EQOLISE trial) demonstrate that IPS achieves approximately 55-65% competitive employment rates for people with severe mental illness compared to only 20-25% for traditional pre-vocational training, while demonstrating no adverse effects on clinical stability.",
        "incorrectExplanations": {
            "B": "Sheltered workshops have consistently failed to transition people into competitive open employment.",
            "C": "Substantial, statistically significant differences favoring IPS have been replicated across more than 25 randomized trials.",
            "D": "Employment through IPS actually correlates with reduced hospitalizations, enhanced self-esteem, and symptom stabilization."
        },
        "learningObjective": "Appraise the empirical research evidence base (e.g., EQOLISE trial) demonstrating the superiority of IPS over traditional vocational rehabilitation.",
        "reference": "Burns, T., et al. (2007). The effectiveness of supported employment for people with severe mental illness: A randomised controlled trial (EQOLISE). The Lancet, 370(9593), 1146-1152.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q660",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Intermediate",
        "questionText": "A 21-year-old service user who experienced a first episode of psychosis wishes to return to university to finish a computer science degree. Which psychosocial rehabilitation framework adapts IPS principles to help the client succeed in educational pursuits?",
        "options": [
            {"id": "A", "text": "Asylum Academic Isolation"},
            {"id": "B", "text": "Remedial Behavioural Detention"},
            {"id": "C", "text": "Supported Education (SEd)"},
            {"id": "D", "text": "Custodial Student Exclusion"}
        ],
        "correctAnswer": "C",
        "explanation": "Supported Education (SEd) adapts evidence-based supported employment principles to higher and further education. SEd specialists assist service users with academic re-enrollment, navigating campus disability accommodations, time-management skills, and communicating with university faculties, facilitating academic completion.",
        "incorrectExplanations": {
            "A": "Educational segregation harms young people with psychosis and impedes normal developmental trajectory.",
            "B": "Detention models are punitive and have no therapeutic role in academic rehabilitation.",
            "D": "Exclusion violates disability rights and international conventions guaranteeing equal access to education."
        },
        "learningObjective": "Describe the core tenets of Supported Education (SEd) for young adults recovering from psychiatric episodes.",
        "reference": "Mowbray, C. T., et al. (2005). Supported education for individuals with psychiatric disabilities: Long-term outcomes from an experimental study. Social Work Research, 29(4), 223-235.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q661",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Advanced",
        "questionText": "A client with schizophrenia enrolled in supported employment asks the mental health nurse: 'Should I tell my new employer that I have schizophrenia?' How should the nurse guide this client regarding disability disclosure in the workplace?",
        "options": [
            {"id": "A", "text": "Tell the client they are legally obligated to disclose their complete psychiatric history on day one or face immediate imprisonment"},
            {"id": "B", "text": "Facilitate a structured exploration of the pros and cons of disclosure, explaining that disclosure is optional but necessary if seeking statutory reasonable workplace accommodations, and respect the client's decision"},
            {"id": "C", "text": "Secretly call the employer behind the client's back to disclose the medical diagnosis without authorization"},
            {"id": "D", "text": "Forbid the client from ever discussing their illness under any circumstances under threat of clinical discharge"}
        ],
        "correctAnswer": "B",
        "explanation": "Psychiatric disability disclosure is an autonomous personal choice. The nurse's role is to facilitate an objective discussion of advantages (access to statutory reasonable adjustments/accommodations, employer understanding, reduced anxiety) and disadvantages (potential stigma or subtle bias), supporting the client's choice.",
        "incorrectExplanations": {
            "A": "There is no legal duty to disclose psychiatric history unless required for specific security/safety roles.",
            "C": "Disclosing confidential medical information without client consent violates professional registration codes and data protection laws.",
            "D": "Coercing clients against disclosure deprives them of lawful statutory accommodations."
        },
        "learningObjective": "Facilitate evidence-based clinical guidance regarding disability disclosure and statutory rights in the workplace.",
        "reference": "Corrigan, P. W., & Rao, D. (2012). On the self-stigma of mental illness: Stages, disclosure, and strategies for change. Canadian Journal of Psychiatry, 57(8), 464-469.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q662",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Advanced",
        "questionText": "An employee recovering from major depression with severe concentration impairment and social fatigue requests reasonable adjustments under equality and disability legislation. Which of the following represents a legally recognized and clinically appropriate workplace reasonable accommodation?",
        "options": [
            {"id": "A", "text": "Flexible start and finish times, a designated quiet workspace away from high sensory traffic, divided/checklisted tasks, and scheduled micro-breaks for stress regulation"},
            {"id": "B", "text": "Exemption from all job duties while receiving full executive pay indefinitely"},
            {"id": "C", "text": "Immediate demotion to an unpaid janitorial role without client consent"},
            {"id": "D", "text": "Mandatory installation of live video feeds to broadcast the employee's work to the clinical team"}
        ],
        "correctAnswer": "A",
        "explanation": "Reasonable adjustments (under the UK Equality Act 2010 or US Americans with Disabilities Act) for psychiatric conditions include adjustments such as flexible working hours, quiet sensory-reduced desk allocation, broken-down task structures, written instructions, and brief self-regulation breaks.",
        "incorrectExplanations": {
            "B": "Accommodations must be reasonable; exempting employees from performing essential job functions is unreasonable.",
            "C": "Involuntary demotion to an unpaid position constitutes unlawful disability discrimination.",
            "D": "Surveillance violates workplace dignity and privacy laws."
        },
        "learningObjective": "Formulate clinically appropriate reasonable workplace adjustments for individuals experiencing psychiatric disabilities.",
        "reference": "Equality and Human Rights Commission (EHRC). (2011). Equality Act 2010 Code of Practice: Employment.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q663",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Advanced",
        "questionText": "A service user working 20 hours per week in a retail job reports overwhelming morning grogginess and cognitive sluggishness, which caused them to receive a written warning for lateness. The nurse notes the client takes Olanzapine 20 mg at 23:30 every night. How can the nurse intervene to protect the client's vocational placement?",
        "options": [
            {"id": "A", "text": "Advise the client to abruptly discontinue olanzapine without medical consultation"},
            {"id": "B", "text": "Tell the client to resign from their job immediately because people on olanzapine cannot work"},
            {"id": "C", "text": "Instruct the employer to pay the client for morning hours even when absent"},
            {"id": "D", "text": "Liaise with the prescribing psychiatrist to shift the administration time earlier (e.g., 20:00) or consider switching to a less sedating antipsychotic, while exploring workplace schedule adjustments with the client's consent"}
        ],
        "correctAnswer": "D",
        "explanation": "Psychiatric nurses play a vital role in integrating psychopharmacology with vocational goals. Shifting the evening administration of sedating atypical antipsychotics earlier (e.g., 20:00 instead of 23:30) allows peak sedation to clear prior to morning awakening. If morning grogginess persists, collaborating to switch to a less sedating agent prevents job loss.",
        "incorrectExplanations": {
            "A": "Abrupt antipsychotic discontinuation induces rapid rebound psychosis and cholinergic rebound.",
            "B": "Telling clients to quit reinforces defeatist attitudes; medication schedules should adapt to support vocational life.",
            "C": "Demanding pay for unworked hours without negotiated adjustments is unreasonable and alienates employers."
        },
        "learningObjective": "Align clinical medication management and chronopharmacology with client vocational schedules to preserve employment.",
        "reference": "Taylor, D., et al. (2021). The Maudsley Prescribing Guidelines in Psychiatry (14th ed.). Wiley-Blackwell.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q664",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Supported employment and vocational rehabilitation",
        "difficulty": "Expert",
        "questionText": "An IPS program manager is conducting a quality assurance evaluation using the 25-item Supported Employment Fidelity Scale (IPS-25). Which of the following benchmark operational metrics must the employment specialists achieve to score in the 'Exemplary Fidelity' band on the 'Time Spent in the Community' and 'Rapid Job Search' items?",
        "options": [
            {"id": "A", "text": "10% time in community, first employer contact occurring within 6 months of intake"},
            {"id": "B", "text": "30% time in community, first employer contact occurring after 12 months of skills screening"},
            {"id": "C", "text": "At least 65% of specialist time spent out of the office in the community, with the first face-to-face employer contact occurring within 30 days of program enrollment"},
            {"id": "D", "text": "100% time spent in classroom simulation, with no real-world employer contact permitted"}
        ],
        "correctAnswer": "C",
        "explanation": "The IPS-25 fidelity scale defines strict quantitative benchmarks: employment specialists must spend at least 65% of their working hours outside the clinic in the community meeting employers and clients, and the first face-to-face contact with an open labor market employer must occur rapidly (within 30 days of program entry).",
        "incorrectExplanations": {
            "A": "A 10% community threshold and 6-month delay reflect failed fidelity characteristic of obsolete pre-vocational programs.",
            "B": "A 12-month delay violates the core rapid-job-search mandate of IPS.",
            "D": "Classroom simulation is contrary to IPS, which rejects simulated pre-vocational work."
        },
        "learningObjective": "Evaluate employment program adherence against the quantitative criteria of the IPS-25 Fidelity Scale.",
        "reference": "Bond, G. R., et al. (2012). A fidelity scale for supported employment. In Evidence-Based Mental Health Practice (pp. 41-58). Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    }
]
