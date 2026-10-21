"""
Module 7 Part 2: Questions MHN-Q665 to MHN-Q714 (50 questions)
Topics 6 to 10:
6. Housing models (MHN-Q665 to MHN-Q674)
7. Stigma and mental health (MHN-Q675 to MHN-Q684)
8. Peer support specialists (MHN-Q685 to MHN-Q694)
9. Deinstitutionalisation (MHN-Q695 to MHN-Q704)
10. Cultural and social determinants of mental health (MHN-Q705 to MHN-Q714)
"""

QUESTIONS_MOD7_PART2 = [
    # -------------------------------------------------------------------------
    # Topic 6: Housing models (MHN-Q665 - MHN-Q674)
    # Target Answers: B, D, B, D, A, C, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q665",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Foundation",
        "questionText": "What is the defining operational principle of the 'Housing First' model, pioneered by Sam Tsemberis and Pathways to Housing, for individuals experiencing chronic homelessness and severe mental illness?",
        "options": [
            {"id": "A", "text": "Individuals must prove 12 months of sustained sobriety and 100% medication compliance before receiving keys to independent housing"},
            {"id": "B", "text": "Immediate provision of permanent, independent lease-holding housing without prerequisites of sobriety, treatment compliance, or psychiatric stability, accompanied by voluntary wrap-around supports"},
            {"id": "C", "text": "Housing is temporary and conditional on completing daily vocational factory labor"},
            {"id": "D", "text": "Placement occurs exclusively in communal congregate dormitory shelters with mandatory group psychotherapy"}
        ],
        "correctAnswer": "B",
        "explanation": "Housing First views safe, secure housing as a fundamental human right rather than a reward earned through clinical compliance. It provides immediate, permanent, independent scattered-site housing without prerequisites of sobriety, psychiatric treatment adherence, or symptom remission, offering voluntary harm-reduction support services.",
        "incorrectExplanations": {
            "A": "Requiring sobriety and compliance defines the traditional 'linear continuum' (treatment first) model, which had catastrophic failure rates.",
            "C": "Housing First provides permanent tenancies with standard legal lease protections, not conditional labor-linked housing.",
            "D": "Housing First prioritizes independent, scattered-site apartments integrated within regular neighborhoods rather than segregated dormitories."
        },
        "learningObjective": "Define the foundational philosophy and operating principles of the Housing First approach.",
        "reference": "Tsemberis, S. (2010). Housing First: The Pathways Model to End Homelessness for People with Mental Illness and Addiction. Hazelden.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q666",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Foundation",
        "questionText": "In traditional mental health housing policy, what is the 'Continuum of Care' (or 'Linear Residential') model, and why has it faced widespread criticism from psychiatric rehabilitation specialists?",
        "options": [
            {"id": "A", "text": "It provides immediate luxury penthouses to all psychiatric inpatients upon arrival"},
            {"id": "B", "text": "It prohibits all healthcare professionals from entering residential care facilities"},
            {"id": "C", "text": "It relies exclusively on prison cells to house unhoused psychiatric patients"},
            {"id": "D", "text": "It requires clients to progress step-by-step through residential stages (emergency shelter -> transitional group home -> semi-supervised flat -> independent flat), where a single relapse or symptom spike results in eviction back to the beginning"}
        ],
        "correctAnswer": "D",
        "explanation": "The 'Linear Continuum' model required clients to demonstrate 'housing readiness' by graduating through increasingly independent residential tiers. It faced severe criticism because any behavioral relapse, symptom exacerbation, or non-compliance led to immediate eviction back to the shelter, causing traumatic residential instability.",
        "incorrectExplanations": {
            "A": "The linear continuum is characterized by austerity and institutional control, not luxury housing.",
            "B": "Linear models are heavily staffed by psychiatric personnel who monitor compliance closely.",
            "C": "While incarceration was an unintended byproduct of model failure, it was not the formal theoretical design."
        },
        "learningObjective": "Critique the structural limitations of the traditional Linear Continuum of Care housing model.",
        "reference": "Ridgway, P., & Zipple, A. M. (1990). The challenge for consumer research: The case for supported housing. Psychosocial Rehabilitation Journal, 13(4), 11-30.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q667",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Intermediate",
        "questionText": "How does Permanent Supportive Housing (PSH) legally and operationally separate housing tenure from clinical mental health treatment?",
        "options": [
            {"id": "A", "text": "If a tenant cancels an appointment with their psychiatrist, their residential lease is instantly terminated that same day"},
            {"id": "B", "text": "Tenancy rights are governed by standard civil landlord-tenant law; participation in psychiatric treatment is encouraged but entirely voluntary and cannot be used as grounds for lease termination"},
            {"id": "C", "text": "Psychiatric nurses hold the master keys and conduct surprise midnight room searches for contraband"},
            {"id": "D", "text": "Tenants are prohibited from holding legal residential contracts in their own name"}
        ],
        "correctAnswer": "B",
        "explanation": "In Permanent Supportive Housing (PSH), the tenancy agreement is completely decoupled from clinical service utilization. Clients hold normal, legal tenancy leases protected by civil landlord-tenant law. While comprehensive supportive services are offered assertively, choosing not to engage in mental health treatment cannot legally result in eviction unless lease agreements (rent, safety, noise) are breached.",
        "incorrectExplanations": {
            "A": "Tying residential leases directly to medical appointment attendance is characteristic of obsolete institutional transitional facilities.",
            "C": "Surprise room inspections violate basic tenant privacy rights under landlord-tenant law.",
            "D": "Holding an individual lease contract in one's own name is a defining feature of PSH."
        },
        "learningObjective": "Differentiate tenancy rights from clinical compliance in Permanent Supportive Housing models.",
        "reference": "Rog, D. J., et al. (2014). Permanent supportive housing: Assessing the evidence. Psychiatric Services, 65(3), 287-294.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q668",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Intermediate",
        "questionText": "What distinguishes the Oxford House model of peer-supported recovery housing from professionally staffed group homes?",
        "options": [
            {"id": "A", "text": "It is staffed 24/7 by registered psychiatric nurses and security officers"},
            {"id": "B", "text": "It requires all residents to take high-dose oral antabuse under direct visual supervision"},
            {"id": "C", "text": "It is funded entirely by corporate pharmaceutical sponsorship with locked bedrooms"},
            {"id": "D", "text": "It is a democratically run, self-governing, and financially self-supporting communal home operated entirely by peers in recovery without professional staff, requiring total abstinence and equitable chore/expense sharing"}
        ],
        "correctAnswer": "D",
        "explanation": "Oxford Houses are democratically run, peer-managed recovery houses where residents live communally, share household expenses, vote on admissions and household decisions, and maintain an abstinence-focused environment without professional on-site staff. Research demonstrates high long-term sobriety and employment rates.",
        "incorrectExplanations": {
            "A": "Oxford Houses explicitly operate without professional healthcare or security staff.",
            "B": "Medication compliance is not monitored through direct observed administration; residents manage their own healthcare.",
            "C": "Oxford Houses are completely self-financed by the residents themselves, not corporate pharmaceutical companies."
        },
        "learningObjective": "Describe the operational structure and peer-led governance of the Oxford House recovery home model.",
        "reference": "Jason, L. A., et al. (2006). Evaluating an abstinence-based, self-governed recovery housing model: Oxford House. Alcoholism Treatment Quarterly, 24(1-2), 19-33.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q669",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Intermediate",
        "questionText": "A community psychiatric nurse is conducting a home assessment for a client with schizophrenia living in supportive housing who has accumulated extensive stacks of old newspapers, broken electronics, and rotting food, blocking exit pathways. What should the nurse prioritize to prevent eviction and safeguard the client?",
        "options": [
            {"id": "A", "text": "Conduct an environmental and fire safety assessment, explore the emotional meaning of possessions using a harm-reduction hoarding framework, and collaborate with the client and housing provider on clearing egress paths"},
            {"id": "B", "text": "Call the municipal waste authority to forcibly dispose of all client possessions without their knowledge or presence"},
            {"id": "C", "text": "Issue an immediate notice of eviction and cancel all community mental health support"},
            {"id": "D", "text": "Instruct the landlord to bolt the windows and doors from the outside"}
        ],
        "correctAnswer": "A",
        "explanation": "Severe hoarding behavior poses serious tenancy and fire safety hazards. Trauma-informed nursing uses harm-reduction approaches: establishing rapport, understanding the emotional attachment to possessions, conducting risk assessments (fire egress, biohazards), and negotiating step-by-step clearance of critical pathways with the client's consent.",
        "incorrectExplanations": {
            "B": "Forcible clearing without the individual's consent causes intense psychological trauma, grief, and immediate rapid re-hoarding.",
            "C": "Eviction increases vulnerability to street homelessness, decompensation, and premature mortality.",
            "D": "Bolting exits creates an illegal, fatal fire hazard and breaches human rights."
        },
        "learningObjective": "Formulate harm-reduction and tenancy-preservation nursing interventions for hoarding and environmental hazards.",
        "reference": "Frost, R. O., et al. (2012). A hoarding rating scale: Development and properties. Depression and Anxiety, 25(8), 695-703.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q670",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Intermediate",
        "questionText": "A client with post-traumatic stress disorder and auditory hallucinations is placed in a high-density, noisy downtown apartment complex adjacent to a train line. The client reports severe insomnia, intense agitation, and paranoid thoughts about neighbors. How should the community nurse conceptualize this problem?",
        "options": [
            {"id": "A", "text": "The client is clearly malingering to seek financial compensation from the landlord"},
            {"id": "B", "text": "The client has incurable treatment-resistant schizophrenia that requires immediate permanent custodial asylum placement"},
            {"id": "C", "text": "The physical and sensory environment (ambient noise, crowding, hyper-arousal triggers) is poorly matched to the client's sensory processing vulnerabilities, requiring environmental modifications or relocation advocacy"},
            {"id": "D", "text": "The nurse should advise the client to drink alcohol every night to block the environmental noises"}
        ],
        "correctAnswer": "C",
        "explanation": "Environmental fit is critical in psychiatric rehabilitation. High-density, hyper-stimulating, or noisy housing can trigger trauma flashbacks, exacerbate perceptual distortions, and disrupt sleep-wake cycles. Nurses assess person-environment fit and advocate for sensory modifications (white noise, heavy drapes) or transfer to a calmer residential setting.",
        "incorrectExplanations": {
            "A": "Attributing environmental distress to malingering invalidates legitimate physiological and psychological distress.",
            "B": "Sensory overload from adverse housing does not warrant lifelong custodial asylum commitment.",
            "D": "Recommending alcohol self-medication promotes addiction and worsens psychiatric stability."
        },
        "learningObjective": "Evaluate the impact of sensory and architectural housing environments on psychiatric symptom stability and recovery.",
        "reference": "Dunn, J. R. (2000). Housing and health inequalities: Review and prospects for research. Housing Studies, 15(3), 341-366.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q671",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Advanced",
        "questionText": "A housing association issues an eviction notice to a service user with bipolar disorder for playing loud music at night during an acute manic episode. When advocating for tenancy sustainment, what is the community psychiatric nurse's best clinical and legal course of action?",
        "options": [
            {"id": "A", "text": "Encourage the landlord to immediately hire bailiffs to remove the tenant's belongings onto the street"},
            {"id": "B", "text": "Liaise with the housing manager, explain that the behavior was a manifestation of an acute health relapse that is now being medically stabilized, negotiate a behavioral management plan, and request reasonable adjustments under equality law"},
            {"id": "C", "text": "Advise the client to stop paying rent as retaliation against the housing provider"},
            {"id": "D", "text": "Agree with the landlord that individuals with affective disorders should not be permitted to live in independent housing"}
        ],
        "correctAnswer": "B",
        "explanation": "Advanced psychiatric nursing advocacy involves intervening early during housing crises. By explaining the medical context of the behavioral disturbance, demonstrating that active treatment has resolved the acute crisis, and requesting reasonable adjustments under disability legislation, the nurse can negotiate a formal agreement that averts eviction.",
        "incorrectExplanations": {
            "A": "Bailiff eviction leads directly to street homelessness and acute clinical decompensation.",
            "C": "Withholding rent breaches lease contracts and accelerates lawful court-ordered eviction.",
            "D": "Endorsing housing discrimination against people with mood disorders breaches professional nursing ethics."
        },
        "learningObjective": "Demonstrate clinical advocacy to preserve tenancy and prevent homelessness during psychiatric relapses.",
        "reference": "Pleace, N. (2016). Housing First Guide Europe. FEANTSA.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q672",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Advanced",
        "questionText": "An older adult with chronic schizophrenia and mild cognitive impairment resides in a private for-profit 'Board and Care' residential home. During a routine visit, the community nurse observes that the manager confiscates residents' government pension debit cards, locks the food pantry between meals, and administers unprescribed sedatives to enforce early bedtime. What is the nurse's legal and ethical obligation?",
        "options": [
            {"id": "A", "text": "Ignore the situation because private businesses are exempt from human rights standards"},
            {"id": "B", "text": "Praise the manager for maintaining strict behavioral order and discipline"},
            {"id": "C", "text": "Advise the residents that they must accept these conditions in exchange for having a bed"},
            {"id": "D", "text": "Initiate an immediate adult safeguarding alert for financial exploitation, institutional abuse, and chemical restraint, notifying statutory regulatory authorities and adult protective services"}
        ],
        "correctAnswer": "D",
        "explanation": "Confiscating personal financial benefits, depriving individuals of food, and using chemical restraints represent severe institutional abuse, financial exploitation, and human rights violations. The nurse has an immediate statutory duty to report these abuses to adult protective services, licensing bodies, and safeguarding boards.",
        "incorrectExplanations": {
            "A": "Private care homes are strictly subject to adult safeguarding legislation and human rights laws.",
            "B": "Treating institutional deprivation and illegal sedation as 'order' condones criminal abuse.",
            "C": "Passivity breaches professional regulatory codes and ethical duties to protect vulnerable adults."
        },
        "learningObjective": "Identify institutional abuse and execute mandatory adult safeguarding reporting in residential care facilities.",
        "reference": "World Health Organization. (2021). Guidance on community mental health services: Promoting person-centred and rights-based approaches. WHO.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q673",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Advanced",
        "questionText": "In a 'Wet Housing' (managed alcohol or low-barrier harm reduction) supportive housing program for chronically unhoused individuals with severe alcohol use disorder and psychiatric comorbidity, what clinical harm-reduction intervention should the psychiatric nurse implement?",
        "options": [
            {"id": "A", "text": "Provision of overdose prevention education, naloxone training, regulated managed alcohol distribution where indicated, thiamine supplementation, and non-judgmental wound and mental health care"},
            {"id": "B", "text": "Mandatory breathalyzer testing three times daily with instant street expulsion upon any detectable blood alcohol level"},
            {"id": "C", "text": "Locking residents in their rooms until they complete 30 days of cold-turkey delirium tremens withdrawal"},
            {"id": "D", "text": "Supplying toxic industrial rubbing alcohol to save program budget funds"}
        ],
        "correctAnswer": "A",
        "explanation": "Low-barrier 'wet housing' and managed alcohol programs (MAP) target individuals who have repeatedly failed abstinence-based shelters. Clinical nursing care focuses on pragmatic harm reduction: providing thiamine/folate prophylaxis to prevent Wernicke-Korsakoff syndrome, managed alcohol dosing to prevent withdrawal seizures, naloxone distribution, wound care, and relationship-based mental health support.",
        "incorrectExplanations": {
            "B": "Mandatory breathalyzers with expulsion define high-barrier abstinence programs that exclude this vulnerable group.",
            "C": "Unmonitored unmedicated alcohol withdrawal ('cold-turkey') carries significant mortality from seizures and delirium tremens.",
            "D": "Providing toxic non-beverage alcohols is homicidal negligence."
        },
        "learningObjective": "Formulate harm-reduction clinical interventions within low-barrier and managed alcohol housing environments.",
        "reference": "Stockwell, T., et al. (2018). Managed Alcohol Programs: Is it time to expand harm reduction to alcohol? Canadian Journal of Public Health, 109(5), 778-782.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q674",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Housing models",
        "difficulty": "Expert",
        "questionText": "In landmark randomized controlled trials of Housing First (such as the Canadian At Home / Chez Soi study and US multi-site studies), what empirical outcome was conclusively demonstrated regarding housing stability and public cost offsets?",
        "options": [
            {"id": "A", "text": "Housing First increased street homelessness by 400% compared to usual care"},
            {"id": "B", "text": "Housing First resulted in 0% housing retention at 12 months and astronomical increases in prison costs"},
            {"id": "C", "text": "Housing First achieved exceptional housing retention (~80-85% at 24 months) and demonstrated substantial cost offsets by reducing emergency department visits, acute hospital bed days, and criminal justice incarcerations"},
            {"id": "D", "text": "Housing First was effective only when clients attended mandatory weekly religious sermons"}
        ],
        "correctAnswer": "C",
        "explanation": "The Canadian At Home/Chez Soi trial (the largest randomized controlled trial of Housing First in history) and US trials demonstrated that Housing First achieved 80-85% housing retention over two years (compared to ~30% in treatment-as-usual), with dramatic cost offsets resulting from reductions in acute psychiatric bed use, emergency room visits, and incarceration.",
        "incorrectExplanations": {
            "A": "Housing First consistently produced massive reductions in street homelessness.",
            "B": "Retention was over 80%, with dramatic reductions in judicial and correctional expenditures.",
            "D": "Housing First is secular, human-rights-based, and non-coercive, rejecting mandatory religious participation."
        },
        "learningObjective": "Appraise epidemiological evidence from randomized controlled trials (At Home/Chez Soi) demonstrating the efficacy and cost-effectiveness of Housing First.",
        "reference": "Stergiopoulos, V., et al. (2015). Effect of scattered-site housing using Housing First on housing stability in adults with mental illness and homelessness: A randomized clinical trial. JAMA, 313(9), 905-915.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 7: Stigma and mental health (MHN-Q675 - MHN-Q684)
    # Target Answers: A, C, B, D, A, C, B, A, D, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q675",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Foundation",
        "questionText": "Sociological and psychiatric research divides stigma into multiple operational levels. How is 'Structural Stigma' accurately defined?",
        "options": [
            {"id": "A", "text": "Societal-level conditions, cultural norms, institutional policies, and laws that systematically restrict the opportunities, resources, and wellbeing of people living with mental illness"},
            {"id": "B", "text": "An individual's personal belief that they are incapable of recovering from their psychiatric diagnosis"},
            {"id": "C", "text": "Interpersonal name-calling between two individuals during a casual social interaction"},
            {"id": "D", "text": "A psychological reaction occurring exclusively within family therapy sessions"}
        ],
        "correctAnswer": "A",
        "explanation": "Structural stigma refers to macro-level institutional policies, laws, administrative rules, and cultural norms that systematically disadvantage individuals with mental illness (e.g., discriminatory insurance parity rules, unequal research funding, voting restrictions, restrictive child custody laws).",
        "incorrectExplanations": {
            "B": "An individual's internalized negative belief about themselves defines 'self-stigma' or 'internalized stigma.'",
            "C": "Interpersonal slurs and prejudice represent 'interpersonal' or 'public stigma.'",
            "D": "Family dynamics relate to courtesy or associative stigma, not systemic structural barriers."
        },
        "learningObjective": "Differentiate structural stigma from interpersonal and internalized stigma.",
        "reference": "Corrigan, P. W., et al. (2004). Structural stigma in state legislation. Psychiatric Services, 55(5), 542-548.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q676",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Foundation",
        "questionText": "Public stigma consists of three interrelated psychological components: stereotypes, prejudice, and discrimination. Which of the following examples specifically illustrates 'Discrimination'?",
        "options": [
            {"id": "A", "text": "A general cognitive belief that all people with psychosis are volatile (Stereotype)"},
            {"id": "B", "text": "An emotional feeling of fear and revulsion when meeting someone with a mental illness (Prejudice)"},
            {"id": "C", "text": "A landlord refusing to rent a vacant apartment to an applicant upon discovering they attend an outpatient psychiatric clinic (Discrimination)"},
            {"id": "D", "text": "A client feeling guilty about taking an antidepressant tablet (Self-stigma)"}
        ],
        "correctAnswer": "C",
        "explanation": "In social psychology, stereotypes are cognitive beliefs; prejudice is the affective emotional endorsement of those stereotypes (fear/anger); and discrimination is the behavioral enactment that disadvantages or denies rights and opportunities to the stigmatized group (e.g., refusing housing or employment).",
        "incorrectExplanations": {
            "A": "General cognitive beliefs represent stereotypes.",
            "B": "Emotional reactions of fear/hostility represent prejudice.",
            "D": "Personal feelings of guilt over medication reflect internalized self-stigma."
        },
        "learningObjective": "Classify clinical and social scenarios into stereotypes, prejudice, and behavioral discrimination.",
        "reference": "Corrigan, P. W., & Watson, A. C. (2002). The paradox of self-stigma and mental illness. Clinical Psychology: Science and Practice, 9(1), 35-53.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q677",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Foundation",
        "questionText": "What is the 'Why Try' effect described in the self-stigma literature by Patrick Corrigan?",
        "options": [
            {"id": "A", "text": "A clinical trial methodology testing novel antipsychotic compounds against placebos"},
            {"id": "B", "text": "The psychological process where internalized stereotypes lead an individual to believe they are incompetent, causing them to abandon aspirations for work, housing, or relationships ('Why should I try to work? Someone like me can't succeed')"},
            {"id": "C", "text": "A therapeutic technique where nurses repeatedly urge clients to try difficult gymnastics"},
            {"id": "D", "text": "The legal process of appealing an involuntary psychiatric admission in court"}
        ],
        "correctAnswer": "B",
        "explanation": "The 'Why Try' effect occurs when individuals internalize societal stereotypes about mental illness (self-stigma), leading to diminished self-esteem, reduced self-efficacy, and anticipatory defeat. They conclude that because of their diagnosis, attempting to achieve personal goals (employment, education, romance) is pointless.",
        "incorrectExplanations": {
            "A": "The 'Why Try' effect is a psychosocial phenomenon, not a pharmacological clinical trial design.",
            "C": "It is not a nursing gym exercise; it represents a debilitating psychological barrier to recovery.",
            "D": "Legal appeals relate to mental health legislation, not the psychology of self-stigma."
        },
        "learningObjective": "Explain the 'Why Try' effect and its impact on self-efficacy and goal attainment.",
        "reference": "Corrigan, P. W., et al. (2009). The why try effect: A model of how self-stigma inhibits recovery. American Journal of Orthopsychiatry, 79(1), 75-81.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q678",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Intermediate",
        "questionText": "The parents of a young man diagnosed with schizophrenia report that their neighbors have stopped speaking to them, friends have ceased visiting their home, and colleagues avoid them at work. What sociological concept describes this experience?",
        "options": [
            {"id": "A", "text": "Primary somatization disorder"},
            {"id": "B", "text": "Antisocial personality contagion"},
            {"id": "C", "text": "Munchausen syndrome by proxy"},
            {"id": "D", "text": "Courtesy stigma (associative stigma)"}
        ],
        "correctAnswer": "D",
        "explanation": "Courtesy stigma (or associative stigma), first conceptualized by Erving Goffman, refers to the prejudice, social ostracism, and blame experienced by individuals simply because of their affiliation with a stigmatized person (e.g., family members, caregivers, or psychiatric healthcare professionals).",
        "incorrectExplanations": {
            "A": "Somatization involves physical symptoms without medical explanation, unrelated to social exclusion.",
            "B": "Personality disorders are individual psychiatric conditions, not social stigma dynamics.",
            "C": "Munchausen by proxy is factitious medical illness imposed on another, completely distinct from stigma."
        },
        "learningObjective": "Recognize courtesy/associative stigma and formulate supportive nursing interventions for caregivers.",
        "reference": "Goffman, E. (1963). Stigma: Notes on the Management of Spoiled Identity. Prentice-Hall.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q679",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Intermediate",
        "questionText": "A 52-year-old woman with a documented history of schizoaffective disorder attends an acute medical emergency department complaining of severe crushing chest pain, dyspnea, and nausea. The triage clinician remarks, 'She is just anxious and hallucinating,' discharges her without an ECG or troponin test, and she subsequently suffers a fatal myocardial infarction. This tragic event is an example of what phenomenon?",
        "options": [
            {"id": "A", "text": "Diagnostic overshadowing"},
            {"id": "B", "text": "Factitious cardiac conversion"},
            {"id": "C", "text": "Tertiary hypochondriacal projection"},
            {"id": "D", "text": "Appropriate clinical gatekeeping"}
        ],
        "correctAnswer": "A",
        "explanation": "Diagnostic overshadowing is the insidious clinical bias where physical health symptoms in individuals with pre-existing psychiatric or intellectual disabilities are misattributed entirely to their mental health diagnosis. It leads to under-investigation, missed medical diagnoses, and premature mortality.",
        "incorrectExplanations": {
            "B": "The patient had genuine ischemic heart disease, not a factitious or conversion disorder.",
            "C": "Hypochondriasis involves excessive health anxiety, whereas this patient had fatal physical pathology.",
            "D": "Dismissing acute cardiac chest pain in emergency departments is gross malpractice, not appropriate gatekeeping."
        },
        "learningObjective": "Analyze diagnostic overshadowing in healthcare settings and implement clinical protocols to prevent physical health neglect.",
        "reference": "Jones, S., et al. (2008). Reducing diagnostic overshadowing in emergency departments. Emergency Nurse, 16(4), 20-24.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q680",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Intermediate",
        "questionText": "Meta-analyses evaluating public anti-stigma interventions have compared three main strategies: Protest (suppressing stigma), Education (providing factual biomedical knowledge), and Contact (direct interpersonal engagement with people in recovery). Which strategy has shown the strongest and most durable evidence for reducing public stigma and social distance?",
        "options": [
            {"id": "A", "text": "Protest, because public shaming reliably eliminates private bias"},
            {"id": "B", "text": "Didactic biological education presenting mental illness solely as a 'brain disease like diabetes'"},
            {"id": "C", "text": "Interpersonal contact-based interventions where people with lived experience share personal recovery stories and interact directly with audiences"},
            {"id": "D", "text": "Total media censorship of all mental health discussions"}
        ],
        "correctAnswer": "C",
        "explanation": "Interpersonal contact (direct, structured interaction between people with lived experience of mental illness and the public) has the strongest empirical evidence for reducing prejudice and social distance. Didactic 'brain disease' models, while increasing treatment acceptance, inadvertently increase public perceptions of unpredictability and dangerousness.",
        "incorrectExplanations": {
            "A": "Protest and moral shaming often produce psychological reactance and rebound prejudice.",
            "B": "Exclusive biomedical 'brain disease' framing has been shown to increase perceived dangerousness and desire for social distance.",
            "D": "Censorship eliminates literacy and exacerbates secretive myths and stigma."
        },
        "learningObjective": "Appraise empirical research on anti-stigma methodologies, comparing contact-based strategies with didactic educational models.",
        "reference": "Corrigan, P. W., et al. (2012). Challenging the public stigma of mental illness: a meta-analysis of outcome studies. Psychiatric Services, 63(10), 963-973.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q681",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Advanced",
        "questionText": "Large-scale national anti-stigma campaigns, such as the UK 'Time to Change' initiative, utilized multi-tiered population interventions. What did independent longitudinal evaluations reveal regarding the impact of these campaigns?",
        "options": [
            {"id": "A", "text": "Zero measurable change in any public metric over 15 years"},
            {"id": "B", "text": "Statistically significant, sustained improvements in public attitudes, reduced discrimination reported by service users in social and family life, and increased workplace mental health initiatives"},
            {"id": "C", "text": "A complete cessation of all psychiatric hospital admissions across the country"},
            {"id": "D", "text": "A severe increase in violence against psychiatric facilities"}
        ],
        "correctAnswer": "B",
        "explanation": "Independent evaluations of the 'Time to Change' campaign (2007-2021) demonstrated statistically significant, population-level improvements in public attitudes toward mental illness, measurable reductions in discrimination reported by service users, and widespread adoption of employer wellness pledges.",
        "incorrectExplanations": {
            "A": "Longitudinal evaluations demonstrated positive shifts across standardized discrimination indices (e.g., DISC).",
            "C": "Anti-stigma campaigns change social attitudes but do not abolish biological morbidity or acute hospital needs.",
            "D": "Public violence against facilities did not increase; community understanding improved."
        },
        "learningObjective": "Evaluate population-level public health outcomes of national anti-stigma campaigns like Time to Change.",
        "reference": "Henderson, C., et al. (2020). Mental health-related stigma in England 2009-2019: Findings from the Time to Change programme. British Journal of Psychiatry, 217(3), 483-489.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q682",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Advanced",
        "questionText": "In professional documentation and interdisciplinary clinical handovers, which linguistic formulation adheres best to anti-stigma, person-first communication standards?",
        "options": [
            {"id": "A", "text": "'A 34-year-old person living with schizophrenia who is working toward returning to college'"},
            {"id": "B", "text": "'A 34-year-old schizophrenic and frequent flyer who is non-compliant with meds'"},
            {"id": "C", "text": "'A chronic borderline who is bed-blocking bed 4'"},
            {"id": "D", "text": "'An incurable psychotic case referred for containment'"},
        ],
        "correctAnswer": "A",
        "explanation": "Person-first language ('person living with schizophrenia' rather than 'a schizophrenic') separates the human being from the illness, honoring their humanity and dignity. Pejorative labels like 'frequent flyer,' 'bed-blocker,' and equating people with their personality diagnosis ('a borderline') reflect institutional stigma that degrades care.",
        "incorrectExplanations": {
            "B": "Labels like 'schizophrenic' and 'frequent flyer' dehumanize the patient and reinforce negative biases.",
            "C": "'Chronic borderline' and 'bed-blocker' are stigmatizing clinical slurs that breach professional standards.",
            "D": "'Incurable case' and 'containment' reflect obsolete asylum-era framing."
        },
        "learningObjective": "Demonstrate person-first, recovery-oriented linguistic standards in psychiatric clinical documentation.",
        "reference": "American Psychological Association. (2020). Publication Manual of the APA (7th ed.): Bias-Free Language Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q683",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Advanced",
        "questionText": "An advanced practice nurse is facilitating a group intervention called 'Honest, Open, Proud' (HOP, formerly Coming Out Proud) developed by Patrick Corrigan. What is the central therapeutic aim of this structured program for participants with psychiatric diagnoses?",
        "options": [
            {"id": "A", "text": "To force all group members to publish their confidential psychiatric medical charts on social media"},
            {"id": "B", "text": "To teach participants how to completely suppress all emotions in public settings"},
            {"id": "C", "text": "To convince participants that mental illness does not exist and is a social conspiracy"},
            {"id": "D", "text": "To empower individuals to evaluate the personal benefits and costs of disclosing their mental health experiences, deconstruct self-stigma, and make strategic, self-directed decisions about sharing their story"}
        ],
        "correctAnswer": "D",
        "explanation": "The 'Honest, Open, Proud' (HOP) program is a validated peer-led group curriculum. It guides individuals through three structured modules: weighing the pros and cons of disclosure, exploring different ways to disclose (targeted, selective, or open), and crafting personal stories, directly reducing self-stigma and distress.",
        "incorrectExplanations": {
            "A": "HOP never coerces disclosure; it emphasizes thoughtful, autonomous decision-making.",
            "B": "Emotional suppression increases psychological distress and runs counter to recovery.",
            "C": "HOP acknowledges the reality of mental health conditions while combating societal prejudice."
        },
        "learningObjective": "Apply the principles and clinical modules of the 'Honest, Open, Proud' (HOP) program to dismantle self-stigma.",
        "reference": "Corrigan, P. W., et al. (2013). Honest, Open, Proud to Eliminate the Stigma of Mental Illness. Illinois Institute of Technology.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q684",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Stigma and mental health",
        "difficulty": "Expert",
        "questionText": "Research consistently reveals that healthcare professionals (including general hospital nurses and physicians) harbor significant implicit and explicit stigma toward psychiatric patients. When designing an institutional clinical intervention to reduce healthcare provider stigma across a general hospital trust, which combination of strategies yields the highest sustained efficacy?",
        "options": [
            {"id": "A", "text": "Distributing a mandatory one-page legal disciplinary warning memo via email without discussion"},
            {"id": "B", "text": "Requiring all clinical staff to take multiple-choice neuroanatomy exams regarding the limbic system"},
            {"id": "C", "text": "Interactive contact-based sessions co-facilitated by service users in recovery, combined with clinical simulations emphasizing practical communication skills, trauma-informed care, and institutional policy reforms"},
            {"id": "D", "text": "Closing all psychiatric consultation-liaison services to avoid contact between staff and psychiatric patients"}
        ],
        "correctAnswer": "C",
        "explanation": "Interventions that successfully shift healthcare provider attitudes combine direct social contact with service users in recovery, practical behavioural skills training (trauma-informed communication, de-escalation), reflective case discussion, and systemic policy reforms that provide adequate staffing and consultation-liaison support.",
        "incorrectExplanations": {
            "A": "Passive disciplinary memos generate cynicism and resentment rather than empathetic attitudinal change.",
            "B": "Biomedical neuroanatomy lectures fail to change attitudes or interpersonal bedside behavior.",
            "D": "Abolishing consultation-liaison care exacerbates provider frustration and worsens patient outcomes."
        },
        "learningObjective": "Design complex organizational interventions to eradicate clinician stigma and diagnostic overshadowing in general healthcare settings.",
        "reference": "Knaak, S., et al. (2017). Mental illness-related stigma in healthcare: Barriers to care and pathways to change. Healthcare Management Forum, 30(2), 111-116.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 8: Peer support specialists (MHN-Q685 - MHN-Q694)
    # Target Answers: B, D, A, C, B, D, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q685",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Foundation",
        "questionText": "What is the primary defining credential and qualification of a Certified Peer Support Specialist working in mental health services?",
        "options": [
            {"id": "A", "text": "A doctorate in neuroscience and 10 years of laboratory research"},
            {"id": "B", "text": "Personal lived experience of a mental health condition and recovery, combined with specialized formal training in peer mentoring, communication, and ethical boundaries"},
            {"id": "C", "text": "A license to prescribe schedule II controlled psychotropic medications"},
            {"id": "D", "text": "Certification in advanced martial arts and physical restraint restraint holds"}
        ],
        "correctAnswer": "B",
        "explanation": "Peer Support Specialists are individuals with personal lived experience of mental illness, addiction, or trauma who have achieved sustained recovery. They undergo formal accredited training to transform their experiential knowledge into intentional, recovery-oriented support for others walking similar paths.",
        "incorrectExplanations": {
            "A": "Academic neurobiology degrees are not credentials for peer specialist roles.",
            "C": "Peer specialists do not prescribe medications; their focus is relational and recovery-oriented.",
            "D": "Physical restraint is antithetical to the non-violent, trauma-informed ethos of peer support."
        },
        "learningObjective": "Identify the foundational role definitions and core qualifications of Peer Support Specialists.",
        "reference": "Davidson, L., et al. (2006). Peer support among adults with serious mental illness: A report from the field. Schizophrenia Bulletin, 32(3), 443-450.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q686",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Foundation",
        "questionText": "What core relational dynamic distinguishes the relationship between a peer support specialist and a service user from a traditional clinician-patient relationship?",
        "options": [
            {"id": "A", "text": "A strict hierarchical superior-subordinate dynamic where the specialist directs all daily activities"},
            {"id": "B", "text": "A commercial landlord-tenant relationship involving rent negotiations"},
            {"id": "C", "text": "A legal attorney-client relationship bound by courtroom litigation procedures"},
            {"id": "D", "text": "Mutuality and shared experiential vulnerability, characterized by an egalitarian, non-hierarchical partnership grounded in mutual learning and hope"}
        ],
        "correctAnswer": "D",
        "explanation": "Peer support is rooted in 'mutuality'—an egalitarian, reciprocal relationship that rejects the traditional hierarchical expert-patient power divide. Both parties share humanity, and support is offered through mutual validation, shared understanding, and personal experiential resonance.",
        "incorrectExplanations": {
            "A": "Hierarchical superior-subordinate dynamics describe traditional clinical models that peer support deliberately avoids.",
            "B": "Peer support is a therapeutic human relationship, not a commercial tenancy arrangement.",
            "C": "Legal representation is an adversarial judicial function outside peer mentoring."
        },
        "learningObjective": "Differentiate the egalitarian relational model of peer support from traditional clinical hierarchies.",
        "reference": "Mead, S., et al. (2001). Peer support: A theoretical perspective. Psychiatric Rehabilitation Journal, 25(2), 134-141.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q687",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Intermediate",
        "questionText": "A newly hired peer support specialist is assigned to an acute community mental health team. Which of the following clinical tasks is inappropriate and outside the professional role boundaries of a peer specialist?",
        "options": [
            {"id": "A", "text": "Administering long-acting injectable antipsychotics and conducting formal psychiatric diagnostic assessments"},
            {"id": "B", "text": "Sharing their personal recovery story to inspire hope during an initial engagement visit"},
            {"id": "C", "text": "Assisting a service user to write their personal WRAP plan"},
            {"id": "D", "text": "Accompanying a nervous client to an intimidating social welfare appointment for moral support"}
        ],
        "correctAnswer": "A",
        "explanation": "Peer specialists must not perform clinical duties reserved for licensed healthcare professionals, such as administering medications, conducting formal diagnostic evaluations, triaging acute medical emergencies, or executing legal involuntary detentions. Their role is non-clinical, psychosocial, and recovery-focused.",
        "incorrectExplanations": {
            "B": "Strategic disclosure to inspire hope is a fundamental core competency of peer support.",
            "C": "Facilitating WRAP and wellness planning is an ideal peer-led intervention.",
            "D": "Providing moral support during stressful community appointments is an evidence-based peer advocacy activity."
        },
        "learningObjective": "Delineate professional practice boundaries between registered mental health nurses and peer support specialists.",
        "reference": "Repper, J., & Carter, T. (2011). A review of the literature on peer support in mental health services. Journal of Mental Health, 20(4), 392-411.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q688",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Intermediate",
        "questionText": "In peer specialist training, how is 'Strategic Storytelling' (purposeful disclosure) defined and practiced?",
        "options": [
            {"id": "A", "text": "Fabricating fictional dramatic stories to entertain clients during recreational groups"},
            {"id": "B", "text": "Recounting every traumatic life detail indiscriminately to use the client as a therapist for personal catharsis"},
            {"id": "C", "text": "Intentionally and selectively sharing specific aspects of one's lived experience and recovery journey tailored to the service user's current challenges, specifically to build hope, normalize feelings, and model coping"},
            {"id": "D", "text": "Refusing to ever mention that one has personal experience with mental illness"}
        ],
        "correctAnswer": "C",
        "explanation": "Strategic storytelling is the intentional, disciplined use of personal lived experience. Rather than venting or seeking emotional gratification (catharsis), the peer specialist thoughtfully chooses specific experiences that directly resonate with the client's current struggles, modeling overcoming barriers and inspiring hope.",
        "incorrectExplanations": {
            "A": "Peer support requires authentic, genuine lived experience, never fabricated stories.",
            "B": "Uncensored venting uses the client for personal gratification and constitutes a serious boundary violation.",
            "D": "Concealing lived experience completely eliminates the core asset and purpose of the peer specialist role."
        },
        "learningObjective": "Apply the principles of strategic, purposeful self-disclosure within peer specialist practice.",
        "reference": "SAMHSA. (2015). Core Competencies for Peer Workers in Behavioral Health Services. Substance Abuse and Mental Health Services Administration.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q689",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Intermediate",
        "questionText": "When integrating peer support workers into traditional multidisciplinary mental health teams, what common organizational pitfall (often termed 'co-optation' or 'role drift') must the clinical nurse leader actively prevent?",
        "options": [
            {"id": "A", "text": "Peer workers being promoted to chief executive officer within 24 hours of hire"},
            {"id": "B", "text": "Peer specialists being pressured by clinical staff to act as 'junior nurses,' chaperones, security guards, or compliance informants, stripping away their distinct recovery ethos"},
            {"id": "C", "text": "Peer specialists spending too much time listening to service users' personal goals"},
            {"id": "D", "text": "Peer workers collaborating with consumer advocacy organizations"}
        ],
        "correctAnswer": "B",
        "explanation": "Co-optation (or role drift) occurs when clinical teams assimilate peer workers into traditional medical hierarchies, assigning them clerical tasks, asking them to spy on medication compliance, or expecting them to assist in physical restraints. This destroys their unique egalitarian role and creates ethical distress.",
        "incorrectExplanations": {
            "A": "Rapid executive promotion is not an empirical organizational challenge in peer specialist integration.",
            "C": "Spending time listening to personal goals is the intended core purpose of peer support.",
            "D": "Liaising with advocacy groups aligns with the peer mission and is encouraged."
        },
        "learningObjective": "Identify organizational barriers and prevent role co-optation during peer specialist team integration.",
        "reference": "Vandewalle, J., et al. (2016). Peer workers' perceptions and experiences of barriers to implementation of peer worker roles in mental health services: A literature review. International Journal of Nursing Studies, 60, 234-250.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q690",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Intermediate",
        "questionText": "What does the empirical literature demonstrate regarding the clinical and psychosocial impacts of integrating peer support specialists into community mental health teams?",
        "options": [
            {"id": "A", "text": "Peer support causes an immediate 100% increase in clinical malpractice lawsuits"},
            {"id": "B", "text": "Peer support has no measurable impact on any consumer outcome"},
            {"id": "C", "text": "Peer support workers inevitably suffer catastrophic psychotic decompensation within two weeks of hire"},
            {"id": "D", "text": "Significant increases in service user empowerment, self-efficacy, hope, treatment engagement, and community functioning, alongside reductions in acute psychiatric rehospitalization"}
        ],
        "correctAnswer": "D",
        "explanation": "Randomized controlled trials and systematic reviews demonstrate that peer support produces significant gains in service user empowerment, personal hope, self-esteem, engagement with care, and social functioning, while frequently reducing psychiatric bed days and inpatient readmissions.",
        "incorrectExplanations": {
            "A": "Malpractice claims do not increase; patient satisfaction and safety communication improve.",
            "B": "Multiple systematic reviews confirm significant positive outcomes across subjective and objective metrics.",
            "C": "Studies show that peer workers thrive when provided with adequate supervision and reasonable accommodations."
        },
        "learningObjective": "Critique empirical evidence evaluating the clinical and psychosocial efficacy of peer support services.",
        "reference": "White, S., et al. (2020). The impact of peer support on outcomes for people with serious mental illness: A systematic review. BMC Psychiatry, 20(1), 588.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q691",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Advanced",
        "questionText": "A service user in acute psychiatric distress seeks support at a 'Peer-Run Respite' (crisis respite) rather than an emergency department. How does a peer-run respite operate as an alternative crisis model?",
        "options": [
            {"id": "A", "text": "It is an involuntary locked jail ward operated by armed police guards"},
            {"id": "B", "text": "It is a warm, voluntary, home-like community residence staffed entirely by trained peer specialists where guests stay for a few days to de-escalate distress, receive peer counseling, and avoid involuntary hospitalization"},
            {"id": "C", "text": "It is an unmonitored tent city with no heating, food, or human contact"},
            {"id": "D", "text": "It is a medical surgical theater where emergency ECT is delivered under general anaesthesia"}
        ],
        "correctAnswer": "B",
        "explanation": "Peer-run respites are voluntary, non-clinical, home-like residential alternatives to emergency departments and psychiatric inpatient wards. Staffed 24/7 by trained peers, guests experiencing acute emotional distress or psychiatric crisis stay short-term (typically 3-10 days) in a trauma-informed, mutually supportive environment to find stability.",
        "incorrectExplanations": {
            "A": "Peer respites are strictly non-coercive, voluntary, unlocked community homes.",
            "C": "Respites provide comfortable, fully furnished domestic accommodations with food and holistic amenities.",
            "D": "Respites are strictly non-clinical environments; no medical procedures or surgery occur."
        },
        "learningObjective": "Evaluate the clinical utility of peer-run crisis respites as alternatives to acute hospital admission.",
        "reference": "Croft, B., & Isvan, N. (2015). Impact of peer-run respites on hospital use and costs. Psychiatric Services, 66(6), 632-637.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q692",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Advanced",
        "questionText": "In Shery Mead's model of Intentional Peer Support (IPS), what are the four core tasks that guide peer interactions?",
        "options": [
            {"id": "A", "text": "Surveillance, Interrogation, Diagnosis, and Pharmacological Titration"},
            {"id": "B", "text": "Pre-screening, Contracting, Conditioning, and Extinction"},
            {"id": "C", "text": "Isolation, Confinement, Decontamination, and Discharge"},
            {"id": "D", "text": "Connection, Worldview (exploring perspectives), Mutuality (shared responsibility), and Moving Towards (focusing on what we want rather than what we want to stop)"}
        ],
        "correctAnswer": "D",
        "explanation": "Intentional Peer Support (IPS) defines four foundational tasks: 1) Connection (building genuine trust without judgment), 2) Worldview (understanding how life experiences shape perspective), 3) Mutuality (learning together in a reciprocal relationship), and 4) Moving Towards (proactively creating positive aspirations rather than symptom avoidance).",
        "incorrectExplanations": {
            "A": "These reflect coercive policing tactics completely foreign to Intentional Peer Support.",
            "B": "These terms belong to behavioral modification paradigms, not relational peer models.",
            "C": "Institutional containment represents the antithesis of peer recovery."
        },
        "learningObjective": "Synthesize the four core operational tasks of Shery Mead's Intentional Peer Support (IPS) framework.",
        "reference": "Mead, S. (2014). Intentional Peer Support: An Alternative Approach. Intentional Peer Support Publishing.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q693",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Advanced",
        "questionText": "To maintain professional integrity and prevent burnout, what specific supervisory structure should be provided to peer support specialists working in clinical mental health trusts?",
        "options": [
            {"id": "A", "text": "Regular reflective supervision delivered by an experienced senior peer supervisor (or a clinician comprehensively trained in peer values), distinct from administrative management"},
            {"id": "B", "text": "Supervision is unnecessary because lived experience provides innate immunity to psychological stress"},
            {"id": "C", "text": "Daily disciplinary evaluations conducted by hospital security staff"},
            {"id": "D", "text": "Public peer supervision conducted in front of service users during group therapy"}
        ],
        "correctAnswer": "A",
        "explanation": "High-fidelity peer support requires dedicated reflective supervision from senior peer leaders or peer-informed supervisors. This space allows peer workers to navigate complex ethical boundaries, process vicarious trauma, prevent role drift, and maintain recovery-oriented values distinct from administrative line management.",
        "incorrectExplanations": {
            "B": "Assuming lived experience confers stress immunity ignores high risks of secondary trauma and burnout.",
            "C": "Security staff supervision is inappropriate and punitive.",
            "D": "Supervision requires confidentiality and psychological safety, not public evaluation before clients."
        },
        "learningObjective": "Design reflective supervisory structures to sustain peer support specialist practice and mitigate vicarious trauma.",
        "reference": "Repper, J., et al. (2013). Peer Support Workers: Theory and Practice (ImROC Briefing 4). Mental Health Foundation.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q694",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Peer support specialists",
        "difficulty": "Expert",
        "questionText": "An advanced practice nurse manager observes that peer support specialists on an acute crisis team are experiencing high turnover, emotional exhaustion, and expressing frustration that clinical nurses dismiss their clinical observations as 'unscientific anecdotes.' How should the nurse manager formulate a systemic leadership intervention to resolve this crisis?",
        "options": [
            {"id": "A", "text": "Abolish the peer specialist program and terminate all peer staff contracts immediately"},
            {"id": "B", "text": "Order peer specialists to remain silent during multidisciplinary team handovers"},
            {"id": "C", "text": "Execute organizational cultural transformation: provide mutual role clarity training for clinical staff, establish peer-specific reflective supervision, validate lived-experience epistemology in multidisciplinary rounds, and ensure trauma-informed caseload limits"},
            {"id": "D", "text": "Instruct peer workers to attend nursing school so their opinions become valid"}
        ],
        "correctAnswer": "C",
        "explanation": "Peer worker burnout and professional marginalization stem from organizational culture clashes where medical hierarchies devalue experiential knowledge. Effective leadership entails structural reform: educating multidisciplinary teams on peer competencies, establishing distinct peer supervision, integrating lived experience into clinical decision-making, and protecting workloads.",
        "incorrectExplanations": {
            "A": "Abandoning peer support deprives service users of an evidence-based recovery modality.",
            "B": "Silencing peer specialists reinforces stigma and exacerbates toxic workplace culture.",
            "D": "Peer support's strength lies in experiential knowledge, not assimilating into conventional nursing roles."
        },
        "learningObjective": "Formulate executive leadership strategies to overcome cultural resistance and organizational barriers when integrating peer support.",
        "reference": "Gillard, S., et al. (2017). Describing a principles-based approach to developing and evaluating peer worker roles in mental health services. BMC Health Services Research, 17(1), 741.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 9: Deinstitutionalisation (MHN-Q695 - MHN-Q704)
    # Target Answers: A, C, B, D, A, C, B, A, D, C
    # Difficulties: F, F, F, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q695",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Foundation",
        "questionText": "What constellation of historical, pharmacological, and legal factors catalyzed the global era of psychiatric deinstitutionalization between the 1950s and 1980s?",
        "options": [
            {"id": "A", "text": "The synthesis of chlorpromazine (1952), widespread exposure of abusive asylum conditions, civil rights and disability litigation, economic cost pressures, and sociological critiques of total institutions"},
            {"id": "B", "text": "The complete eradication of all psychiatric illnesses by world health authorities in 1960"},
            {"id": "C", "text": "A global treaty mandating that all mentally ill citizens be exiled to remote unpopulated islands"},
            {"id": "D", "text": "The total replacement of all medical nursing by robotic artificial intelligence"}
        ],
        "correctAnswer": "A",
        "explanation": "Deinstitutionalization was driven by a convergence of forces: the advent of chlorpromazine (the first effective antipsychotic) in 1952 which reduced acute agitation; journalistic and legal exposés of asylum squalor; the civil rights movement demanding liberty for disabled individuals; sociologists (Goffman, Foucault); and state desire to reduce massive institutional operating budgets.",
        "incorrectExplanations": {
            "B": "Psychiatric disorders were not eradicated; prevalence remained constant.",
            "C": "Exile treaties are fictional; the goal was community integration.",
            "D": "Robotics had no presence in mid-20th-century healthcare reform."
        },
        "learningObjective": "Identify historical, pharmacological, and sociopolitical drivers of the 20th-century psychiatric deinstitutionalization movement.",
        "reference": "Shorter, E. (1997). A History of Psychiatry: From the Era of the Asylum to the Age of Prozac. John Wiley & Sons.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q696",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Foundation",
        "questionText": "In psychiatric epidemiology and social policy, what does the term 'Transinstitutionalization' signify?",
        "options": [
            {"id": "A", "text": "The successful transition of all hospital inpatients into permanent high-paying executive corporate jobs"},
            {"id": "B", "text": "The transfer of psychiatric hospital administrative servers from analog to digital cloud storage"},
            {"id": "C", "text": "The phenomenon where closure of psychiatric asylums resulted in individuals with severe mental illness shifting into other custodial institutions, predominantly prisons, jails, nursing homes, and homeless shelters, due to inadequate community care"},
            {"id": "D", "text": "The gender transition procedures of adolescent inpatients"}
        ],
        "correctAnswer": "C",
        "explanation": "Transinstitutionalization describes the tragic reality where closing state psychiatric hospitals did not result in genuine community freedom for many vulnerable individuals. Instead, due to severe underfunding of community services, individuals with severe mental illness were shifted into prisons, correctional jails, for-profit nursing homes, and street homelessness.",
        "incorrectExplanations": {
            "A": "Deinstitutionalization was marked by high unemployment and poverty, not executive corporate placements.",
            "B": "Digital data transfers have no relation to clinical transinstitutionalization.",
            "D": "Transinstitutionalization refers to sociological institutional relocation, completely distinct from gender-affirming medical care."
        },
        "learningObjective": "Define transinstitutionalization and its manifestation across correctional and homeless populations.",
        "reference": "Torrey, E. F., et al. (2010). More Mentally Ill Persons Are in Jails and Prisons Than Hospitals: A Survey of the States. Treatment Advocacy Center.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q697",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Foundation",
        "questionText": "What systemic public policy failure in the 1970s and 1980s directly caused the phenomenon known as the psychiatric 'revolving door' (frequent short-term discharges followed rapidly by acute readmission)?",
        "options": [
            {"id": "A", "text": "Excessive community funding creating too many luxurious day programs"},
            {"id": "B", "text": "The rapid discharge of asylum inpatients into fragmented community environments that completely lacked subsidized housing, community crisis teams, coordinated case management, and social supports"},
            {"id": "C", "text": "A legal mandate requiring all psychiatric patients to be hospitalized every 14 days"},
            {"id": "D", "text": "The discovery that all psychotropic medications lose effectiveness after exactly 72 hours"}
        ],
        "correctAnswer": "B",
        "explanation": "The 'revolving door' phenomenon occurred because governments rapidly closed asylum beds to save money without reallocating promised financial resources into community support systems. Individuals were discharged into impoverished, fragmented communities with no housing, case management, or crisis care, precipitating rapid relapse and readmission.",
        "incorrectExplanations": {
            "A": "Community care was severely starved of funding, not overly lavish.",
            "C": "There was never a legal mandate for bi-weekly readmissions.",
            "D": "Psychotropic pharmacokinetics varies widely; the 72-hour assertion is medically false."
        },
        "learningObjective": "Explain the systemic policy failures that created the psychiatric 'revolving door' cycle.",
        "reference": "Lamb, H. R., & Bachrach, L. L. (2001). Some perspectives on deinstitutionalization. Psychiatric Services, 52(8), 1039-1045.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q698",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Intermediate",
        "questionText": "Signed into law by President John F. Kennedy in 1963, what was the primary architectural and social goal of the Community Mental Health Act (Public Law 88-164)?",
        "options": [
            {"id": "A", "text": "To construct 100 new maximum-security state asylums in remote rural areas"},
            {"id": "B", "text": "To transfer all psychiatric care exclusively into military defense installations"},
            {"id": "C", "text": "To outlaw all psychiatric nursing education across universities"},
            {"id": "D", "text": "To construct a nationwide network of 1,500 comprehensive community mental health centers allowing individuals to receive multidisciplinary care while living with their families and remaining in their home communities"}
        ],
        "correctAnswer": "D",
        "explanation": "The US Community Mental Health Act of 1963 envisioned building 1,500 community mental health centers nationwide to replace state asylums, enabling individuals with psychiatric disorders to receive comprehensive treatment in their local communities while preserving family and civic bonds. Only about half were ever funded, contributing to system shortfalls.",
        "incorrectExplanations": {
            "A": "The act specifically sought to dismantle and close remote custodial state asylums.",
            "B": "Military bases had no role in civilian community mental health legislation.",
            "C": "The act championed expanding community psychiatric nursing and multidisciplinary training."
        },
        "learningObjective": "Analyze the legislative intent and funding shortfalls of the Community Mental Health Act of 1963.",
        "reference": "Grob, G. N. (1994). The Mad Among Us: A History of the Care of America's Mentally Ill. Free Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q699",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Intermediate",
        "questionText": "In his seminal sociological work 'Asylums' (1961), Erving Goffman conceptualized mental hospitals as 'Total Institutions'. What core structural characteristics define a total institution according to Goffman?",
        "options": [
            {"id": "A", "text": "All aspects of life (sleep, play, and work) are conducted in the same place under a single authority; activities are tightly scheduled and carried out in the immediate company of a large batch of others; and a sharp binary split exists between staff and inmates"},
            {"id": "B", "text": "Voluntary democratic participation where patients hold majority voting rights over hospital policies"},
            {"id": "C", "text": "Free movement between the hospital and the external community at the patient's leisure"},
            {"id": "D", "text": "A decentralized network of private suburban apartments without staff supervision"}
        ],
        "correctAnswer": "A",
        "explanation": "Goffman defined a total institution as a place where the normal boundaries separating sleep, play, and work collapse. Inmates are stripped of personal identity ('mortification of the self'), subjected to batch living under rigid surveillance, and segregated from mainstream society by an insurmountable divide between inmates and staff.",
        "incorrectExplanations": {
            "B": "Total institutions are authoritarian hierarchies that strip inmates of democratic decision-making.",
            "C": "Physical and social containment behind locked perimeters is the central hallmark of total institutions.",
            "D": "Decentralized apartments reflect modern community rehabilitation, the antithesis of Goffman's total institution."
        },
        "learningObjective": "Critique Erving Goffman's sociological framework of the 'Total Institution' and its institutional effects on service users.",
        "reference": "Goffman, E. (1961). Asylums: Essays on the Social Situation of Mental Patients and Other Inmates. Anchor Books.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q700",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Intermediate",
        "questionText": "Italy's landmark 'Basaglia Law' (Law 180 of 1978), spearheaded by Franco Basaglia and Psichiatria Democratica, represents the most radical deinstitutionalization reform in modern history. What did Law 180 mandate?",
        "options": [
            {"id": "A", "text": "The mandatory re-hospitalization of all Italian citizens for psychoanalytic screening"},
            {"id": "B", "text": "The total replacement of doctors with criminal justice magistrates"},
            {"id": "C", "text": "The complete, permanent prohibition of new admissions to all psychiatric hospitals, the phased dismantling of existing asylums, and the total replacement of inpatient institutions with integrated territorial community services (Dipartimento di Salute Mentale)"},
            {"id": "D", "text": "The privatization of all healthcare to foreign commercial insurance conglomerates"}
        ],
        "correctAnswer": "C",
        "explanation": "Italian Law 180 (1978) was a revolutionary reform that prohibited all new admissions to psychiatric hospitals, ordered the gradual closure of all existing asylums, and established comprehensive territorial community mental health centers and small 15-bed psychiatric wards in general hospitals, shifting psychiatry permanently to community care.",
        "incorrectExplanations": {
            "A": "Law 180 championed human rights and severely restricted involuntary commitment.",
            "B": "The law emphasized territorial social medicine and psychiatric humanism, not legalist punishment.",
            "D": "Care was integrated into Italy's National Health Service (Servizio Sanitario Nazionale), not private corporations."
        },
        "learningObjective": "Examine the international policy impact and structural implementation of the Italian Basaglia Reform (Law 180).",
        "reference": "Basaglia, F. (1987). Psychiatry Inside Out: Selected Writings of Franco Basaglia. Columbia University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q701",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Advanced",
        "questionText": "In modern psychiatric mental health nursing, what acute clinical and ethical crisis has emerged from overzealous cuts to acute psychiatric inpatient bed numbers without corresponding increases in community crisis infrastructure?",
        "options": [
            {"id": "A", "text": "Hospitals having 100% empty beds and nurses with no patients to care for"},
            {"id": "B", "text": "Severe emergency department 'boarding' (vulnerable psychiatric patients waiting days in noisy ED hallways), frequent out-of-area placements hundreds of miles from home, and criminalization of mental illness in local jails"},
            {"id": "C", "text": "A sudden worldwide elimination of mental health emergencies"},
            {"id": "D", "text": "A massive influx of wealthy medical tourists seeking psychiatric asylum"}
        ],
        "correctAnswer": "B",
        "explanation": "When acute psychiatric beds are slashed without robust, intensive community crisis capacity, health systems experience severe crises: protracted emergency department boarding, delayed care, traumatic out-of-area placements far from family support networks, and diversion of untreated psychiatric distress into the criminal justice system.",
        "incorrectExplanations": {
            "A": "Modern acute psychiatric wards operate at dangerously high occupancy rates (often 95-105%).",
            "C": "Psychiatric crises remain prevalent; reducing beds without alternatives merely displaces crises to EDs and streets.",
            "D": "Out-of-area placements are an undesirable domestic crisis, not international medical tourism."
        },
        "learningObjective": "Critique modern psychiatric bed capacity crises, emergency department boarding, and out-of-area placement dynamics.",
        "reference": "Crisp, N., et al. (2016). Old Problems, New Solutions: Improving acute psychiatric care for adults in England. Commission on Acute Adult Psychiatric Care.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q702",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Advanced",
        "questionText": "How did the role and professional identity of psychiatric nurses evolve during the transition from the asylum era (pre-1960s) to modern community mental health practice?",
        "options": [
            {"id": "A", "text": "From custodial custodians focused on physical containment, institutional routines, and manual control, to autonomous community practitioners providing biopsychosocial assessment, therapeutic alliances, psychosocial interventions, and recovery advocacy in natural settings"},
            {"id": "B", "text": "From autonomous community therapists to strictly locked-ward prison guards"},
            {"id": "C", "text": "The nursing role was eliminated entirely and replaced by laboratory technicians"},
            {"id": "D", "text": "From evidence-based clinicians to administrative billing clerks with no patient contact"}
        ],
        "correctAnswer": "A",
        "explanation": "In the asylum era, psychiatric nurses were largely confined to custodial maintenance, ward order, batch feeding, and physical restraint. The deinstitutionalization era transformed psychiatric nursing into an autonomous, specialized clinical discipline focusing on therapeutic relationships, community case coordination, home visits, and psychosocial interventions.",
        "incorrectExplanations": {
            "B": "The historical trajectory moved away from locked custody toward community independence.",
            "C": "Psychiatric nursing expanded exponentially during community mental health transitions.",
            "D": "Community mental health nursing is characterized by direct in-vivo interpersonal clinical contact."
        },
        "learningObjective": "Trace the historical evolution of psychiatric nursing roles from custodial containment to autonomous community recovery practice.",
        "reference": "Nolan, P. (1993). A History of Mental Health Nursing. Chapman & Hall.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q703",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Advanced",
        "questionText": "Landmark human rights enquiries into institutional abuses in the UK (such as the Ely Hospital Enquiry in 1969) and the US (Willowbrook State School exposé in 1972) had what transformative impact on modern psychiatric nursing governance?",
        "options": [
            {"id": "A", "text": "They resulted in absolute immunity from prosecution for all hospital administrators"},
            {"id": "B", "text": "They permanently banned family members from visiting psychiatric hospitals"},
            {"id": "C", "text": "They proved that institutionalization produced superior cognitive development in children"},
            {"id": "D", "text": "They catalyzed statutory safeguarding frameworks, independent institutional inspectorates (e.g., CQC), modern clinical whistleblowing protections, and mandatory rights-based standards of care"}
        ],
        "correctAnswer": "D",
        "explanation": "The Ely Hospital Enquiry (1969) and Willowbrook exposé revealed horrific neglect, abuse, and deprivation of vulnerable individuals behind closed institutional walls. These scandals directly triggered the creation of independent hospital inspectorates, statutory safeguarding boards, patient advocacy services, and legal whistleblowing protections.",
        "incorrectExplanations": {
            "A": "The enquiries dismantled institutional immunity and established strict regulatory accountability.",
            "B": "The investigations showed that isolating patients from families fostered abuse; modern policy mandates family engagement.",
            "C": "The evidence proved that total institutions caused severe developmental regression and trauma."
        },
        "learningObjective": "Analyze the historical impact of institutional enquiry reports on the creation of modern clinical governance and safeguarding frameworks.",
        "reference": "DHSS. (1969). Report of the Committee of Inquiry into Allegations of Ill-Treatment of Patients and other irregularities at the Ely Hospital, Cardiff. HMSO.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q704",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Deinstitutionalisation",
        "difficulty": "Expert",
        "questionText": "An advanced practice nurse consultant is advising a government ministry designing a national mental health strategy. According to the WHO 'Balanced Care Model' (Thornicroft and Tansella), what is the optimal systemic relationship between acute hospital beds and community services?",
        "options": [
            {"id": "A", "text": "Community mental health services must be abolished to concentrate 100% of resources in a single national asylum"},
            {"id": "B", "text": "Acute hospital beds must be completely eliminated to 0% with no inpatient facilities permitted under any circumstances"},
            {"id": "C", "text": "The primary focus must be on comprehensive community-based services (CMHTs, crisis resolution, primary care liaison, assertive outreach), complemented by a modest volume of acute psychiatric beds in general district hospitals for short-term medical stabilization"},
            {"id": "D", "text": "All mental healthcare should be delivered exclusively through commercial retail pharmacy kiosks"}
        ],
        "correctAnswer": "C",
        "explanation": "The 'Balanced Care Model' developed by Thornicroft and Tansella posits that modern, effective mental health systems base the vast majority of their care in local community facilities (outpatient clinics, crisis home treatment, day hospitals, primary care integration), backed by a balanced, modest capacity of acute psychiatric beds located in general hospitals.",
        "incorrectExplanations": {
            "A": "Concentrating resources in centralized asylums reverses 70 years of evidence and violates international human rights standards.",
            "B": "Eliminating all acute beds causes system failure; some individuals experience crises that cannot be safely managed at home.",
            "D": "Retail pharmacy kiosks lack multidisciplinary therapeutic, assessment, and rehabilitative capacity."
        },
        "learningObjective": "Synthesize the principles of the WHO Balanced Care Model to optimize resource allocation across hospital and community sectors.",
        "reference": "Thornicroft, G., & Tansella, M. (2013). The balanced care model for global mental health. Australian & New Zealand Journal of Psychiatry, 47(1), 11-14.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------------------
    # Topic 10: Cultural and social determinants of mental health (MHN-Q705 - MHN-Q714)
    # Target Answers: B, D, A, C, B, D, B, D, A, C
    # Difficulties: F, F, I, I, I, I, A, A, A, E
    # -------------------------------------------------------------------------
    {
        "id": "MHN-Q705",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Foundation",
        "questionText": "According to the World Health Organization (WHO) Commission on Social Determinants of Health, what are the primary non-biological drivers of mental disorders and psychological distress across populations?",
        "options": [
            {"id": "A", "text": "Personal moral weakness and lack of willpower"},
            {"id": "B", "text": "The conditions in which people are born, grow, live, work, and age, including poverty, income inequality, substandard housing, unemployment, and systemic discrimination"},
            {"id": "C", "text": "Astrological alignments and cosmic radiation cycles"},
            {"id": "D", "text": "Excessive intake of dietary carbohydrates exclusively"}
        ],
        "correctAnswer": "B",
        "explanation": "Social determinants of mental health (SDOMH) encompass the structural and socioeconomic conditions of daily life—including poverty, adverse early childhood experiences, educational inequities, precarious employment, housing instability, food insecurity, and discrimination—which shape psychological vulnerability across the lifespan.",
        "incorrectExplanations": {
            "A": "Attributing mental health distress to moral weakness reflects stigmatizing victim-blaming.",
            "C": "Astrology and cosmic radiation lack scientific and epidemiological credibility.",
            "D": "While nutrition affects general health, dietary carbohydrates do not explain structural population health disparities."
        },
        "learningObjective": "Identify the primary social determinants of mental health according to the World Health Organization framework.",
        "reference": "World Health Organization. (2014). Social Determinants of Mental Health. WHO Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q706",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Foundation",
        "questionText": "In psychiatric epidemiology, how does the 'Social Causation' hypothesis differ fundamentally from the 'Social Drift' (or social selection) hypothesis regarding the link between poverty and schizophrenia?",
        "options": [
            {"id": "A", "text": "Social causation argues that schizophrenia is caused by infectious bacteria in drinking water"},
            {"id": "B", "text": "Both hypotheses state that socioeconomic conditions have zero correlation with mental illness"},
            {"id": "C", "text": "Social drift argues that living in wealthy suburbs causes acute catatonic schizophrenia"},
            {"id": "D", "text": "Social causation posits that the chronic stressors of poverty and adversity precipitate psychiatric disorders, whereas social drift posits that the cognitive and functional impairments of illness cause individuals to drift downward into lower socioeconomic classes"}
        ],
        "correctAnswer": "D",
        "explanation": "The 'Social Causation' hypothesis asserts that experiencing socioeconomic adversity, deprivation, and discrimination directly induces or precipitates psychiatric illness. Conversely, the 'Social Drift' hypothesis asserts that the biological onset of severe illness leads to educational failure, unemployment, and downward mobility into lower socioeconomic strata.",
        "incorrectExplanations": {
            "A": "Social causation focuses on psychosocial and economic adversity, not waterborne bacteria.",
            "B": "The robust statistical correlation between low socioeconomic status and severe mental illness is undisputed.",
            "C": "Social drift describes downward mobility into poverty, not residence in wealthy suburbs."
        },
        "learningObjective": "Differentiate between the Social Causation and Social Drift hypotheses in psychiatric epidemiology.",
        "reference": "Dohrenwend, B. P., et al. (1992). Socioeconomic status and psychiatric disorders: The causation-selection issue. Science, 255(5047), 946-952.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q707",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Intermediate",
        "questionText": "In community sociology and mental health promotion, how is 'Social Capital' defined, and what is its demonstrated impact on community mental health?",
        "options": [
            {"id": "A", "text": "Networks of social relations, mutual trust, civic reciprocity, and community cohesion; high social capital serves as a robust protective factor against depression, suicide, and psychological distress"},
            {"id": "B", "text": "The monetary value of corporate stock owned by psychiatric pharmaceutical executives"},
            {"id": "C", "text": "The number of psychiatric beds constructed per 100,000 population"},
            {"id": "D", "text": "The total amount of cash a patient possesses in their hospital trust account"}
        ],
        "correctAnswer": "A",
        "explanation": "Social capital refers to social networks, shared norms, trust, and mutual reciprocity within a community. Research consistently reveals that communities with high cognitive and structural social capital have significantly lower rates of major depression, anxiety, and suicide, fostering resilience against environmental stressors.",
        "incorrectExplanations": {
            "B": "Corporate investment refers to economic capital, not sociological community social capital.",
            "C": "Bed density measures institutional healthcare capacity, not civic relational cohesion.",
            "D": "Personal liquid cash is individual financial capital."
        },
        "learningObjective": "Explain the concept of social capital and its protective epidemiological role in community mental health.",
        "reference": "Kawachi, I., & Berkman, L. F. (2001). Social ties and mental health. Journal of Urban Health, 78(3), 458-467.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q708",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Intermediate",
        "questionText": "Originally conceptualized by legal scholar Kimberlé Crenshaw, how is the analytical framework of 'Intersectionality' applied in advanced psychiatric mental health nursing?",
        "options": [
            {"id": "A", "text": "It analyzes traffic intersections near community outpatient clinics to prevent vehicular accidents"},
            {"id": "B", "text": "It focuses strictly on the biological interaction between two psychotropic medications"},
            {"id": "C", "text": "It examines how multiple social identities (such as race, gender, class, sexual orientation, disability, and immigration status) intersect and interact to create unique, compounded systems of oppression, marginalization, and health disparities"},
            {"id": "D", "text": "It refers to the surgical intersection of cranial nerve pathways during lobotomy"}
        ],
        "correctAnswer": "C",
        "explanation": "Intersectionality recognizes that individuals do not experience their identities in isolation. Instead, multiple social categories (e.g., being a Black, low-income, disabled woman) intersect to produce unique, compounding experiences of structural oppression, institutional bias, and healthcare inequities that require nuanced clinical assessment.",
        "incorrectExplanations": {
            "A": "Intersectionality is a critical sociological framework, not traffic engineering.",
            "B": "Pharmacological interactions describe pharmacokinetics, not intersectional social analysis.",
            "D": "Intersectionality has no connection to surgical neuro-ablation."
        },
        "learningObjective": "Apply the analytical lens of intersectionality to assess compounded health disparities in mental health nursing.",
        "reference": "Crenshaw, K. (1989). Demarginalizing the intersection of race and sex: A black feminist critique of antidiscrimination doctrine, feminist theory and antiracist politics. University of Chicago Legal Forum, 1989(1), 139-167.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q709",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Intermediate",
        "questionText": "The DSM-5 Cultural Formulation Interview (CFI) is an evidence-based assessment protocol. What are the four core domains systematically explored during a CFI assessment?",
        "options": [
            {"id": "A", "text": "Heart rate, respiratory rate, blood pressure, and core temperature"},
            {"id": "B", "text": "1) Cultural definition of the problem, 2) Cultural perceptions of cause, context, and support, 3) Cultural factors affecting self-coping and past help-seeking, and 4) Cultural factors affecting current help-seeking (patient-clinician relationship)"},
            {"id": "C", "text": "Criminal history, ballistic weapons training, financial credit rating, and cellular phone contracts"},
            {"id": "D", "text": "Visual acuity, auditory decibel threshold, vestibular balance, and olfactory sensitivity"}
        ],
        "correctAnswer": "B",
        "explanation": "The DSM-5 Cultural Formulation Interview (CFI) uses 16 standardized questions covering four foundational clinical domains: 1) Cultural definition of the problem, 2) Cultural perceptions of cause, context, and support, 3) Cultural factors affecting self-coping and past help-seeking, and 4) Cultural factors affecting current help-seeking and preferences for care.",
        "incorrectExplanations": {
            "A": "These are routine physical vital signs, not cultural psychiatric formulation domains.",
            "C": "These are judicial and commercial credit metrics irrelevant to cultural formulation.",
            "D": "These assess sensory organ physiology, not sociocultural meaning of distress."
        },
        "learningObjective": "Demonstrate the clinical application of the four core domains of the DSM-5 Cultural Formulation Interview (CFI).",
        "reference": "American Psychiatric Association. (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed., DSM-5). Cultural Formulation Interview (pp. 749-755).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q710",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Intermediate",
        "questionText": "A 40-year-old Latina woman is brought to the clinic by her family following the sudden death of her brother. She experienced sudden trembling, uncontrollable screaming, palpitations, falling to the floor, and a sense of chest tightness. Her family refers to this as an 'Ataque de nervios'. How should the culturally competent psychiatric nurse conceptualize this presentation?",
        "options": [
            {"id": "A", "text": "An acute manifestation of malingering requiring referral to law enforcement for disorderly conduct"},
            {"id": "B", "text": "Definitive evidence of severe paranoid schizophrenia requiring immediate lifelong involuntary custodial commitment"},
            {"id": "C", "text": "A fabricated condition that should be met with cold social isolation to extinguish the behavior"},
            {"id": "D", "text": "A culturally recognized idiom of distress (cultural concept of distress) prevalent in Hispanic/Latino cultures, triggered by acute interpersonal or familial loss, which is usually transient and requires calm support, safety, and cultural validation"}
        ],
        "correctAnswer": "D",
        "explanation": "'Ataque de nervios' is a recognized cultural idiom of distress in DSM-5, commonly reported among individuals of Latino descent. It typically occurs in response to severe acute stress or bereavement, characterized by dramatic emotional expression, trembling, and dissociative episodes. It is usually transient and self-limiting, requiring supportive de-escalation rather than aggressive antipsychotic medication.",
        "incorrectExplanations": {
            "A": "Dismissing culturally patterned distress as criminal malingering demonstrates cultural incompetence.",
            "B": "Ataques de nervios do not represent chronic schizophrenia and do not require lifelong institutionalization.",
            "C": "Withholding support causes psychological harm and destroys the therapeutic alliance."
        },
        "learningObjective": "Analyze cultural concepts of distress (idioms of distress such as ataque de nervios) and differentiate them from severe psychiatric disorders.",
        "reference": "Lewis-Fernández, R., et al. (2010). Culture and psychiatric diagnosis: A DSM-5 perspective. Focus, 8(3), 332-340.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q711",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Advanced",
        "questionText": "Epidemiological audits across the UK National Health Service (and similar Western health systems) consistently document that Black and African-Caribbean individuals are 4 to 5 times more likely to be compulsorily detained under the Mental Health Act than White individuals. When analyzing the structural determinants driving this stark disparity, what factors must the advanced psychiatric nurse identify?",
        "options": [
            {"id": "A", "text": "A genetic flaw unique to individuals of African ancestry that causes resistance to all psychiatric medicine"},
            {"id": "B", "text": "Structural racism, cultural mistrust of mental health services leading to delayed help-seeking, institutional biases in perceived dangerousness, socio-economic marginalization, and coercive police-led presentation pathways"},
            {"id": "C", "text": "Complete fabrication of official government health statistics by researchers"},
            {"id": "D", "text": "A higher baseline consumption of tropical fruit in Caribbean diets"}
        ],
        "correctAnswer": "B",
        "explanation": "Extensive empirical research (including the UK Independent Review of the Mental Health Act) confirms that ethnic disparities in compulsory detention are driven by complex structural determinants: institutional racism, implicit clinician bias perceiving Black patients as 'dangerous', historic mistrust leading to delayed presentations in crisis, lack of culturally responsive primary care, and over-involvement of police pathways.",
        "incorrectExplanations": {
            "A": "Racialized genetic deficiency hypotheses have been completely refuted by modern genomics.",
            "C": "Government statistics from the CQC and NHS digital rigorously confirm these stark disparities.",
            "D": "Dietary fruit consumption is an absurd distraction from institutional systemic inequalities."
        },
        "learningObjective": "Critique structural racism and systemic factors driving racial disparities in compulsory psychiatric detention.",
        "reference": "Wessely, S., et al. (2018). Modernising the Mental Health Act: Increasing choice, reducing compulsion (The Independent Review of the Mental Health Act 1983). UK Department of Health and Social Care.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q712",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Advanced",
        "questionText": "An advanced practice mental health nurse is integrating 'Structural Competency' into the community intake assessment protocol. What practical nursing action demonstrates structural competency in clinical practice?",
        "options": [
            {"id": "A", "text": "Advising patients to change their ethnic heritage to avoid discrimination"},
            {"id": "B", "text": "Focusing solely on individual cognitive distortions without inquiring about social conditions"},
            {"id": "C", "text": "Instructing patients that poverty is an inevitable biological fate"},
            {"id": "D", "text": "Routinely screening for structural vulnerabilities (food insecurity, fuel poverty, immigration status precarity, housing hazards), and establishing direct referral pathways to legal aid, food banks, and housing advocacy"}
        ],
        "correctAnswer": "D",
        "explanation": "Structural competency is the capacity for healthcare providers to recognize how social, economic, and institutional structures create health disparities and clinical symptoms. Demonstrating this involves systematically assessing practical survival needs (food, heating, legal status) and mobilizing structural remedies (social prescribing, food banks, legal aid).",
        "incorrectExplanations": {
            "A": "Telling clients to change heritage is culturally offensive and impossible.",
            "B": "Focusing solely on cognitive distortions ignores real-world material deprivation and structural oppression.",
            "C": "Naturalizing poverty as 'biological fate' perpetuates fatalism and clinical inaction."
        },
        "learningObjective": "Apply structural competency principles to psychiatric nursing assessments and interventions.",
        "reference": "Metzl, J. M., & Hansen, H. (2014). Structural competency: Theorizing a new medical engagement with stigma and inequality. Social Science & Medicine, 103, 126-133.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q713",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Advanced",
        "questionText": "In the landmark Adverse Childhood Experiences (ACE) study by Felitti and Anda, what dose-response relationship was uncovered between cumulative childhood adversity (abuse, neglect, household dysfunction) and adult mental and physical health?",
        "options": [
            {"id": "A", "text": "A strong, graded dose-response relationship: higher ACE scores (e.g., 4 or more) dramatically increase the adult lifetime risk of depression, suicide attempts (up to 12-fold increase), severe substance use disorders, and chronic medical illnesses"},
            {"id": "B", "text": "Childhood adversity was shown to provide complete lifelong psychological immunity against adult anxiety"},
            {"id": "C", "text": "ACE scores correlated only with athletic sports achievement, having no impact on health"},
            {"id": "D", "text": "The study found zero correlation between childhood trauma and adult psychopathology"}
        ],
        "correctAnswer": "A",
        "explanation": "The CDC-Kaiser Permanente ACE Study demonstrated a powerful, graded dose-response relationship between early toxic childhood stress and adult disease. Individuals with an ACE score of 4 or more had a 460% increased risk of depression, a 1220% (12-fold) increase in attempted suicide, and massive increases in chronic physical illnesses.",
        "incorrectExplanations": {
            "B": "Childhood adversity does not confer immunity; it inflicts neurodevelopmental and biological damage.",
            "C": "The study evaluated cardiovascular disease, mental health, and mortality, not athletic prowess.",
            "D": "The correlation between trauma and psychopathology is one of the most replicated findings in epidemiology."
        },
        "learningObjective": "Analyze the epidemiological findings of the Adverse Childhood Experiences (ACE) study and integrate trauma-informed principles into community care.",
        "reference": "Felitti, V. J., et al. (1998). Relationship of childhood abuse and household dysfunction to many of the leading causes of death in adults: The Adverse Childhood Experiences (ACE) Study. American Journal of Preventive Medicine, 14(4), 245-258.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q714",
        "module": "7. Community Mental Health and Psychiatric Rehabilitation",
        "topic": "Cultural and social determinants of mental health",
        "difficulty": "Expert",
        "questionText": "When adapting evidence-based psychological and psychiatric nursing interventions for minoritized cultural communities, what defines high-quality 'Culturally Adapted Psychological Interventions' (CAPIs) according to Bernal's Ecological Validity and Cultural Adaptation Model?",
        "options": [
            {"id": "A", "text": "Simply translating manual texts into another language using an automated dictionary without changing concepts"},
            {"id": "B", "text": "Abandoning all scientific evidence and relying exclusively on horoscope reading"},
            {"id": "C", "text": "Systematic modification of language, persons, metaphors, content, concepts, goals, methods, and context to ensure congruence with the client's cultural worldview, values, and community realities while preserving core therapeutic mechanisms"},
            {"id": "D", "text": "Forbidding family members from ever attending therapy sessions"}
        ],
        "correctAnswer": "C",
        "explanation": "High-fidelity cultural adaptation (Bernal's model) requires systematic adaptation across eight clinical dimensions: Language, Persons (client-therapist ethnic matching), Metaphors (cultural idioms), Content (cultural knowledge), Concepts (explanatory models of illness), Goals (family and community values), Methods, and Context (structural environment), ensuring cultural resonance without compromising theoretical fidelity.",
        "incorrectExplanations": {
            "A": "Literal word translation without conceptual or contextual adaptation fails to achieve cultural validity.",
            "B": "CAPI maintains rigorous evidence-based cognitive-behavioural or psychotherapeutic mechanisms.",
            "D": "In many collectivist cultures, involving extended family networks is vital to therapeutic success."
        },
        "learningObjective": "Design Culturally Adapted Psychological Interventions (CAPIs) using Bernal's Ecological Validity framework.",
        "reference": "Bernal, G., et al. (1995). Ecological validity and cultural sensitivity for outcome research: Issues for the cultural adaptation and development of psychosocial treatments with Hispanics. Journal of Abnormal Child Psychology, 23(1), 67-82.",
        "contentReviewStatus": "Peer Reviewed"
    }
]
