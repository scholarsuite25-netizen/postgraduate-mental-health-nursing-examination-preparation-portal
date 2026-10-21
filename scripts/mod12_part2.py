# scripts/mod12_part2.py
# Questions Q1165 to Q1214 (Topics 6 to 10 of Module 12)

MOD12_PART2 = [
    # -------------------------------------------------------------
    # Topic 6: Quality improvement methodologies (Q1165 - Q1174)
    # Answers: C, D, A, B, C, D, A, B, C, D
    # Difficulties: F, F, I, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1165",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Foundation",
        "questionText": "The Institute for Healthcare Improvement (IHI) 'Model for Improvement' is built around two integrated components. What are the three fundamental questions that precede testing changes with Plan-Do-Study-Act (PDSA) cycles?",
        "options": [
            {"id": "A", "text": "Who is to blame? How much will it cost? When can we terminate staff?"},
            {"id": "B", "text": "What is the hospital's stock price? How many beds can we close? What is the marketing budget?"},
            {"id": "C", "text": "1. What are we trying to accomplish? (Aim); 2. How will we know that a change is an improvement? (Measures); 3. What change can we make that will result in improvement? (Ideas)"},
            {"id": "D", "text": "Which patients complain most? Which doctors are easiest to manage? Which shifts have lowest sickness?"}
        ],
        "correctAnswer": "C",
        "explanation": "The IHI Model for Improvement (Langley et al.) asks three foundational questions before implementing any change: (1) What are we trying to accomplish? (Setting a clear, time-bound, measurable SMART aim); (2) How will we know that a change is an improvement? (Establishing outcome, process, and balancing measures); and (3) What change can we make that will result in improvement? (Developing evidence-based change ideas). These ideas are then tested iteratively using PDSA cycles.",
        "incorrectExplanations": {
            "A": "Blame, cost-cutting, and staff dismissals reflect a toxic culture, not healthcare quality improvement.",
            "B": "Stock prices and bed closures are commercial/administrative concerns unrelated to the IHI model.",
            "D": "Focusing on complaints and doctor management does not address systematic quality improvement science."
        },
        "learningObjective": "Identify the three fundamental questions of the Institute for Healthcare Improvement (IHI) Model for Improvement.",
        "reference": "Langley, G. J. et al. (2009). The Improvement Guide: A Practical Approach to Enhancing Organizational Performance (2nd Ed.). Jossey-Bass; IHI Open School.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1166",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Foundation",
        "questionText": "When applying the Plan-Do-Study-Act (PDSA) cycle to reduce medication administration delays on an acute psychiatric ward, what occurs during the 'Study' phase?",
        "options": [
            {"id": "A", "text": "Nurses enroll in full-time university master's degrees while leaving the ward unstaffed"},
            {"id": "B", "text": "Staff rewrite all trust clinical policies without collecting baseline data"},
            {"id": "C", "text": "The change is rolled out to 50 hospital wards simultaneously without checking results"},
            {"id": "D", "text": "The team analyzes the data collected during the test, compares the observed outcomes against predictions, reflects on lessons learned, and examines unintended consequences"}
        ],
        "correctAnswer": "D",
        "explanation": "In a PDSA cycle: Plan = identify test of change and predict outcome; Do = run the test on a small scale and collect data; Study = complete data analysis, compare results against initial predictions, reflect on what worked and what didn't, and identify unexpected effects; Act = decide whether to adopt, adapt, or abandon the change for the next cycle.",
        "incorrectExplanations": {
            "A": "The 'Study' phase is data analysis of a test of change, not individual university degree enrollment.",
            "B": "Rewriting policies without data analysis bypasses the scientific methodology of PDSA.",
            "C": "Rolling out changes hospital-wide without studying small-scale data violates PDSA iterative testing principles."
        },
        "learningObjective": "Execute the 'Study' phase of a PDSA cycle by analyzing data against initial clinical predictions.",
        "reference": "Deming, W. E. (1986). Out of the Crisis. MIT Center for Advanced Educational Services; NHS England QI Hub.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1167",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Intermediate",
        "questionText": "Lean healthcare methodology focuses on eliminating non-value-added activities ('waste' or 'muda') to streamline patient flow. In an acute psychiatric admissions pathway, what is an example of 'Waiting' waste, and how does Lean redesign eliminate it?",
        "options": [
            {"id": "A", "text": "A medically cleared, acutely distressed patient remaining in an emergency department cubicle for 36 hours awaiting an inpatient psychiatric bed; eliminated by stream-mapping the admission pipeline, establishing dedicated crisis assessment lounges, and removing redundant authorization bottlenecks"},
            {"id": "B", "text": "A patient waiting 5 minutes in line for lunch in the ward dining room"},
            {"id": "C", "text": "A nurse waiting for the kettle to boil in the staffroom during a scheduled break"},
            {"id": "D", "text": "A visitor waiting for the ward front door bell to be answered for 30 seconds"}
        ],
        "correctAnswer": "A",
        "explanation": "In Lean manufacturing and healthcare (Womack & Jones), 'Waiting' is one of the classic 8 wastes (DOWNTIME). A patient in severe mental distress waiting 36 hours in an emergency department represents systemic flow failure, leading to clinical deterioration, increased aggression, and bed-blocking. Lean uses Value Stream Mapping to identify non-value-adding steps, eliminate redundant approvals, and synchronize crisis services.",
        "incorrectExplanations": {
            "B": "Waiting 5 minutes for dining is a normal social expectation, not a critical clinical bottleneck.",
            "C": "Staff tea breaks are personal rest time, not an organizational patient care process.",
            "D": "A 30-second security door check is standard procedural safety, not Lean process waste."
        },
        "learningObjective": "Apply Lean methodology principles to identify and eliminate 'waiting' waste in psychiatric admission pathways.",
        "reference": "Womack, J. P. & Jones, D. T. (2003). Lean Thinking: Banish Waste and Create Wealth in Your Corporation. Free Press; NHS Improvement Lean Healthcare Guide.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1168",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Intermediate",
        "questionText": "Six Sigma quality methodology uses the DMAIC framework to reduce process variation and defect rates. What does the acronym DMAIC stand for?",
        "options": [
            {"id": "A", "text": "Document, Monitor, Audit, Inspect, and Certify"},
            {"id": "B", "text": "Define, Measure, Analyze, Improve, and Control"},
            {"id": "C", "text": "Diagnose, Medicate, Admit, Isolate, and Discharge"},
            {"id": "D", "text": "Delegate, Motivate, Appraise, Instruct, and Correct"}
        ],
        "correctAnswer": "B",
        "explanation": "DMAIC is the foundational 5-phase data-driven improvement cycle of Six Sigma: (1) Define the clinical problem and customer/patient requirements; (2) Measure current process performance and baseline defect rates; (3) Analyze root causes of defects and process variation; (4) Improve the process by designing and implementing targeted solutions; and (5) Control future process performance to sustain improvements.",
        "incorrectExplanations": {
            "A": "Document, monitor, audit, inspect, and certify describe traditional quality assurance inspections, not Six Sigma DMAIC.",
            "C": "Diagnose, medicate, admit, isolate, discharge describe medicalized patient management steps.",
            "D": "Delegate, motivate, appraise, instruct, correct are general supervisory tasks."
        },
        "learningObjective": "Recall the five sequential phases of the Six Sigma DMAIC framework in healthcare quality improvement.",
        "reference": "Chassin, M. R. (1998). Is Health Care Ready for Six Sigma Quality? The Milbank Quarterly; ASQ Six Sigma Handbook.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1169",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Intermediate",
        "questionText": "When analyzing run charts or Statistical Process Control (SPC) charts monitoring the monthly incidence of physical restraints on a psychiatric unit, how is 'special cause variation' differentiated from 'common cause variation'?",
        "options": [
            {"id": "A", "text": "Special cause variation is caused by natural seasonal weather changes that occur every year"},
            {"id": "B", "text": "Common cause variation occurs only when consultants are on annual leave"},
            {"id": "C", "text": "Common cause variation represents the inherent, predictable, day-to-day background noise of the stable system, whereas special cause variation represents an unusual, statistically significant shift or signal (such as a run of 8 consecutive points above the centerline or a point outside control limits) arising from a specific external change or intervention"},
            {"id": "D", "text": "All variation on SPC charts is purely random error and should never be investigated"}
        ],
        "correctAnswer": "C",
        "explanation": "In Statistical Process Control (Shewhart / Deming), common cause variation is the predictable variation inherent within the design of the system itself. Special cause variation arises from unexpected events, new variables, or deliberate quality improvement interventions. On a run or SPC chart, special cause rules include: a single point outside upper/lower control limits, a 'run' of 8 consecutive points on one side of the center line, or a continuous trend of 6 points increasing or decreasing.",
        "incorrectExplanations": {
            "A": "Seasonal patterns can be common cause or special cause depending on system design.",
            "B": "Attributing common cause variation solely to consultant leave is clinically inaccurate.",
            "D": "Ignoring variation guarantees that real deterioration goes unchecked and true improvements are missed."
        },
        "learningObjective": "Interpret Statistical Process Control (SPC) charts and distinguish special cause from common cause variation in clinical safety data.",
        "reference": "Provost, L. P. & Murray, R. M. (2011). The Health Care Data Guide: Learning from Data for Improvement. Jossey-Bass; NHS England Making Data Count.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1170",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Intermediate",
        "questionText": "In John Kotter's 8-Step Change Model, what is the crucial first step a clinical nurse leader must execute to successfully initiate ward-level clinical practice transformation?",
        "options": [
            {"id": "A", "text": "Rewrite job descriptions and reduce staff salaries"},
            {"id": "B", "text": "Declare immediate victory and disband the project team"},
            {"id": "C", "text": "Publish a glossy promotional brochure for hospital visitors"},
            {"id": "D", "text": "Establish a Sense of Urgency: demonstrating compelling data on why the status quo is unacceptable, identifying patient safety risks, and inspiring staff with the urgent need for change"}
        ],
        "correctAnswer": "D",
        "explanation": "Kotter's 8-Step Change Model begins with: Step 1: Create a Sense of Urgency. Without establishing why change is urgently necessary (e.g., highlighting harm from restrictive practices, patient dissatisfaction, or audit failures), complacency dominates, and change initiatives fail. Subsequent steps include: creating a guiding coalition, developing a strategic vision, communicating the vision, empowering action, generating short-term wins, consolidating gains, and anchoring in culture.",
        "incorrectExplanations": {
            "A": "Salary cuts and job description overhauls breed hostility and sabotage change efforts.",
            "B": "Declaring victory prematurely (Kotter's Step 7 pitfall) destroys momentum before changes are embedded.",
            "C": "Marketing brochures do nothing to engage frontline clinicians in urgent practice transformation."
        },
        "learningObjective": "Apply John Kotter's 8-Step Change Model with focus on establishing a sense of urgency for clinical innovation.",
        "reference": "Kotter, J. P. (1996). Leading Change. Harvard Business School Press; NHS Leadership Academy Change Management Guidance.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1171",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Advanced",
        "questionText": "The 'Safewards' model (Professor Len Bowers) is a landmark evidence-based quality improvement framework that significantly reduces conflict (aggression, self-harm, rule-breaking) and containment (restraint, seclusion, rapid tranquilisation) in psychiatric inpatient wards. What are the core conceptual components of the Safewards model?",
        "options": [
            {"id": "A", "text": "Six originating domains of ward conflict potential (Staff modifier, Physical environment, Outside world, Patient community, Patient characteristics, Regulatory framework) counterbalanced by 10 specific nursing interventions (e.g., Clear Mutual Expectations, Soft Words, Talk Down, Reassurance, Mutual Help Meeting)"},
            {"id": "B", "text": "High-voltage perimeter stun fences, automated water cannons, and mandatory sedation at 20:00"},
            {"id": "C", "text": "Total reliance on solitary confinement and elimination of all ward group activities"},
            {"id": "D", "text": "Abolishing all ward rules and allowing patients to prescribe their own psychotropics"}
        ],
        "correctAnswer": "A",
        "explanation": "Safewards (Bowers et al., 2014) identifies that flashpoints and conflict arise from six structural domains: Staff modifier, Physical environment, Outside world, Patient community, Patient characteristics, and the Regulatory framework. To mitigate these flashpoints, Safewards introduced 10 evidence-based nursing interventions (e.g., Mutual Help Meetings, Clear Mutual Expectations, Soft Words, Talk Down/de-escalation, Positive Words at handover, Discharge Messages) that dramatically reduce both conflict and restrictive containment.",
        "incorrectExplanations": {
            "B": "Coercive mechanical force is abusive, illegal, and increases inpatient violence.",
            "C": "Solitary confinement causes profound psychiatric deterioration and violates international human rights conventions.",
            "D": "Safewards fosters clear, collaboratively agreed mutual boundaries, not chaotic absence of rules."
        },
        "learningObjective": "Explain the theoretical architecture and evidence-based interventions of the Safewards model.",
        "reference": "Bowers, L. et al. (2015). Reducing Conflict and Containment Rates on Acute Psychiatric Wards: The Safewards Cluster Randomised Controlled Trial. International Journal of Nursing Studies, 52(9), 1412-1422.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1172",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Advanced",
        "questionText": "A Quality Improvement (QI) team constructs a 'Driver Diagram' to achieve the aim: 'Reduce prone (face-down) physical restraint incidents on Ward B by 50% within 12 months.' How are Primary Drivers, Secondary Drivers, and Change Ideas structured on a Driver Diagram?",
        "options": [
            {"id": "A", "text": "Primary Drivers are individual nurses; Secondary Drivers are security guards; Change Ideas are disciplinary sanctions"},
            {"id": "B", "text": "The diagram displays Aim on the left, branching into Primary Drivers (high-level system components that directly contribute to achieving the aim), which branch into Secondary Drivers (specific, actionable areas or processes necessary to impact primary drivers), which link directly to concrete Change Ideas (specific interventions tested via PDSAs)"},
            {"id": "C", "text": "It is an architectural blueprint showing electrical wiring and plumbing in the hospital basement"},
            {"id": "D", "text": "A list of vehicle drivers licensed to operate the trust patient transport minibuses"}
        ],
        "correctAnswer": "B",
        "explanation": "A Driver Diagram is a visual logic chart translating an improvement aim into a clear execution strategy. On the far left is the SMART Aim; branching to the right are Primary Drivers (the major system pillars necessary to achieve the aim, e.g., staff de-escalation skills, sensory modulation access, trauma-informed debriefing); branching from these are Secondary Drivers (actionable leverage points, e.g., real-time training, sensory room availability); which connect directly to specific Change Ideas tested via PDSA cycles.",
        "incorrectExplanations": {
            "A": "Driver diagrams organize system components and process logic, not individual staff blame.",
            "C": "Basement blueprints are facility engineering schematics.",
            "D": "The term 'driver' refers to system causal factors, not vehicular drivers."
        },
        "learningObjective": "Construct and interpret a clinical Driver Diagram linking SMART aims to primary drivers, secondary drivers, and PDSA change ideas.",
        "reference": "Institute for Healthcare Improvement (IHI) (2019). Driver Diagram Tool; NHS Improvement Quality Improvement Hub.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1173",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Advanced",
        "questionText": "When facilitating a 'Process Mapping' (Value Stream Mapping) exercise with acute ward staff to examine the discharge planning pathway, what is the primary clinical objective of walking through the current real-world steps?",
        "options": [
            {"id": "A", "text": "To identify where the idealized trust policy is being followed perfectly by everyone"},
            {"id": "B", "text": "To identify which individual staff members work slowest so they can be assigned overtime"},
            {"id": "C", "text": "To visualize the actual, lived patient journey from admission to discharge, identifying bottlenecks, redundant handoffs, duplicated paperwork, unnecessary delays, and gaps in communication from both staff and patient perspectives"},
            {"id": "D", "text": "To calculate the total distance walked by nurses to win a pedometer competition"}
        ],
        "correctAnswer": "C",
        "explanation": "Process mapping brings the multidisciplinary team and patients together to visually lay out every granular step of a care pathway as it actually occurs (not how policy manuals imagine it occurs). By mapping the real-world flow, the team visibly uncovers hidden bottlenecks, duplicated administrative forms, communication breakdowns, unnecessary waiting periods, and opportunities to eliminate waste and enhance patient experience.",
        "incorrectExplanations": {
            "A": "Process maps reveal the messy real-world reality, not idealized policy compliance.",
            "B": "Process mapping focuses on fixing broken systems, not policing individual work speed.",
            "D": "Pedometer tracking is personal fitness monitoring, not clinical process mapping."
        },
        "learningObjective": "Facilitate clinical Process Mapping to identify bottlenecks and flow failures in mental health care pathways.",
        "reference": "NHS Institute for Innovation and Improvement (2008). Quality and Service Improvement Tools: Process Mapping; The King's Fund.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1174",
        "module": "12. Leadership and Professional Practice",
        "topic": "Quality improvement methodologies",
        "difficulty": "Expert",
        "questionText": "Many well-intentioned healthcare quality improvement projects suffer from the 'Improvement Evaporation Effect'—where gains achieved during an active pilot project erode and practice reverts to old habits within 6 months of the QI team departing. Under the NHS Sustainability Model, what factors ensure lasting clinical sustainability and spread?",
        "options": [
            {"id": "A", "text": "Leaving the project entirely undocumented and hoping staff remember the pilot"},
            {"id": "B", "text": "Threatening staff with immediate suspension if they ever stop using the new tool"},
            {"id": "C", "text": "Publishing an academic paper and immediately moving all resources to a new project"},
            {"id": "D", "text": "Addressing all 10 factors of the NHS Sustainability Model across Process (benefits beyond cost, adaptability), Staff (involvement from inception, shared clinical values), and Organization (leadership support, robust infrastructure, embedding new habits into routine induction, electronic workflows, and ongoing audit feedback)"}
        ],
        "correctAnswer": "D",
        "explanation": "The NHS Institute Sustainability Model identifies 10 factors across three dimensions essential for sustaining improvement: (1) Process: clear demonstrable clinical benefits beyond cost, adaptability to changing conditions, and continuous measurement; (2) Staff: staff engagement from inception, alignment with professional values, and staff empowerment; and (3) Organization: visible senior leadership support, organizational infrastructure, and hardwiring changes into standard induction, EHR templates, and operational audits.",
        "incorrectExplanations": {
            "A": "Lack of documentation guarantees rapid reversion to legacy practices.",
            "B": "Coercive threats generate resentment and active subversion once surveillance ends.",
            "C": "Abandoning project oversight after publication is a classic cause of project collapse."
        },
        "learningObjective": "Evaluate the NHS Sustainability Model to prevent the 'improvement evaporation effect' and scale clinical changes.",
        "reference": "Maher, L. et al. (2010). The NHS Sustainability Model and Guide. NHS Institute for Innovation and Improvement; Dixon-Woods, M. et al. (2012) BMJ Quality & Safety.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 7: Preventing burnout and compassion fatigue (Q1175 - Q1184)
    # Answers: A, B, C, D, A, B, C, D, A, B
    # Difficulties: F, F, F, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1175",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Foundation",
        "questionText": "The Maslach Burnout Inventory (MBI, Christina Maslach) is the gold-standard psychometric tool assessing occupational burnout in healthcare professionals. Which three core psychological dimensions constitute the burnout syndrome in the MBI?",
        "options": [
            {"id": "A", "text": "Emotional Exhaustion, Depersonalization (Cynicism), and Reduced Personal Accomplishment (Professional Inefficacy)"},
            {"id": "B", "text": "Physical Hunger, Insomnia, and Gastrointestinal Distress"},
            {"id": "C", "text": "Auditory Hallucinations, Delusional Paranoia, and Thought Disorder"},
            {"id": "D", "text": "Financial Indebtedness, Legal Liability, and Administrative Incompetence"}
        ],
        "correctAnswer": "A",
        "explanation": "The Maslach Burnout Inventory defines burnout as a three-dimensional psychological syndrome resulting from chronic workplace stress: (1) Emotional Exhaustion: feelings of being emotionally overextended, drained, and depleted of emotional resources; (2) Depersonalization / Cynicism: negative, callous, cynical, or excessively detached responses to patients and colleagues; and (3) Reduced Personal Accomplishment: feelings of incompetence, lack of achievement, and loss of professional self-efficacy.",
        "incorrectExplanations": {
            "B": "Physical symptoms may accompany stress, but are not the psychometric dimensions of the MBI.",
            "C": "Psychotic symptoms represent severe Axis I pathology, not occupational burnout.",
            "D": "Financial and legal matters are external stressors, not psychological burnout dimensions."
        },
        "learningObjective": "Identify the three core psychometric dimensions of occupational burnout according to the Maslach Burnout Inventory.",
        "reference": "Maslach, C., Jackson, S. E., & Leiter, M. P. (1996). Maslach Burnout Inventory Manual (3rd Ed.); World Health Organization ICD-11 (QD85: Burnout).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1176",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Foundation",
        "questionText": "Dr. Charles Figley famously defined 'Compassion Fatigue' as 'the cost of caring' for individuals suffering emotional pain. How does compassion fatigue differ fundamentally from chronic burnout in mental health nursing?",
        "options": [
            {"id": "A", "text": "Compassion fatigue only occurs in veterinary surgeons, whereas burnout occurs only in accountants"},
            {"id": "B", "text": "Compassion fatigue typically has an acute, rapid onset driven by absorbing the traumatic distress and suffering of patients, whereas burnout develops insidiously over months or years from chronic organizational workload and bureaucratic stress"},
            {"id": "C", "text": "Compassion fatigue is cured permanently by drinking caffeinated energy beverages"},
            {"id": "D", "text": "Burnout occurs only after 40 years of nursing, while compassion fatigue occurs only on Monday mornings"}
        ],
        "correctAnswer": "B",
        "explanation": "Charles Figley differentiated Compassion Fatigue (often used interchangeably with Secondary Traumatic Stress) from Burnout: Burnout emerges slowly and progressively from organizational overload, bureaucratic friction, understaffing, and lack of administrative control. In contrast, Compassion Fatigue can have an acute, sudden onset resulting directly from deep empathic exposure to patients' traumatic experiences and profound psychic agony.",
        "incorrectExplanations": {
            "A": "Compassion fatigue affects all caregiving professionals, especially psychiatric nurses and trauma therapists.",
            "C": "Caffeine does not cure emotional exhaustion or secondary trauma; it can exacerbate physiological anxiety.",
            "D": "Burnout can develop within months of chronic workplace stress at any career stage."
        },
        "learningObjective": "Differentiate the etiology, onset trajectory, and clinical characteristics of compassion fatigue versus burnout.",
        "reference": "Figley, C. R. (1995). Compassion Fatigue: Coping with Secondary Traumatic Stress Disorder in Those Who Treat the Traumatized. Brunner/Mazel; Stamm, B. H. (2010) ProQOL.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1177",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Foundation",
        "questionText": "What are 'Schwartz Center Rounds', and what is their primary objective in supporting hospital staff well-being?",
        "options": [
            {"id": "A", "text": "A rigorous weekly interrogation where managers audit nurses' documentation errors"},
            {"id": "B", "text": "A mandatory physical exercise boot-camp conducted on the hospital roof"},
            {"id": "C", "text": "Multidisciplinary, confidential monthly forums where healthcare staff from all backgrounds gather to discuss the emotional, social, and psychological challenges of providing care, focusing on personal feelings rather than clinical problem-solving"},
            {"id": "D", "text": "A pharmaceutical sales conference demonstrating new psychotropic drug formulations"}
        ],
        "correctAnswer": "C",
        "explanation": "Schwartz Center Rounds (founded by Ken Schwartz and widely adopted across the NHS via The Point of Care Foundation) are regular, multidisciplinary forums where all staff (clinical and non-clinical) explore the emotional, social, and ethical impact of caregiving. Unlike clinical ward rounds or morbidity conferences, Schwartz Rounds do not problem-solve clinical cases; they provide a psychologically safe space to share feelings, normalize vulnerability, and build mutual compassion.",
        "incorrectExplanations": {
            "A": "Auditing and interrogation are the exact opposite of Schwartz Rounds' supportive ethos.",
            "B": "Physical boot-camps are not Schwartz Rounds.",
            "D": "Schwartz Rounds have zero connection to commercial pharmaceutical promotion."
        },
        "learningObjective": "Describe the purpose and non-clinical, emotional focus of Schwartz Center Rounds in healthcare organizations.",
        "reference": "The Point of Care Foundation (2020). Schwartz Rounds: A Practical Guide; Goodrich, J. (2012). Supporting Hospital Staff to Provide Compassionate Care.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1178",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Intermediate",
        "questionText": "During an unprecedented bed crisis, an acute ward nurse is ordered to discharge a severely suicidal patient prematurely to free a bed for a police detainee. The nurse feels deep shame, anguish, and guilt, feeling forced to violate their personal and professional ethical values. What psychological condition is the nurse experiencing?",
        "options": [
            {"id": "A", "text": "Factitious malingering"},
            {"id": "B", "text": "Antisocial personality traits"},
            {"id": "C", "text": "Histrionic emotional exaggeration"},
            {"id": "D", "text": "Moral Injury: the profound psychological distress resulting from actions, or inactions, that violate an individual's deeply held moral or ethical code, often triggered by systemic organizational failures"}
        ],
        "correctAnswer": "D",
        "explanation": "Moral Injury (originally described by Jonathan Shay in combat veterans and now widely recognized in healthcare by Litz, Greenberg, and Royal College of Psychiatrists) occurs when clinicians are forced by systemic resource deficits, institutional directives, or working conditions to act, or witness actions, that transgress their core ethical values (e.g., providing suboptimal care or premature discharge due to lack of beds). It generates intense guilt, shame, and betrayal.",
        "incorrectExplanations": {
            "A": "Malingering is faking symptoms for secondary tangible gain, not genuine ethical distress.",
            "B": "Experiencing moral anguish demonstrates intact conscience and high empathy, not antisocial traits.",
            "C": "Moral injury is a recognized, severe psychological syndrome, not histrionic drama."
        },
        "learningObjective": "Identify symptoms and systemic causes of Moral Injury in mental health professionals.",
        "reference": "Greenberg, N. et al. (2020). Managing Mental Health Challenges Faced by Healthcare Workers During COVID-19. BMJ; Shay, J. (2014). Moral Injury. Psychoanalytic Psychology.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1179",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Intermediate",
        "questionText": "Dr. Kristin Neff's empirical research identifies three core components of 'Mindful Self-Compassion'. How can a psychiatric nurse apply these components when reflecting on an unpreventable inpatient suicide?",
        "options": [
            {"id": "A", "text": "Self-Kindness vs Self-Judgment (treating oneself with understanding rather than harsh self-criticism); Common Humanity vs Isolation (recognizing that suffering, clinical tragedy, and limitations are shared human experiences); and Mindfulness vs Over-Identification (holding emotional pain in balanced awareness without getting consumed by catastrophic guilt)"},
            {"id": "B", "text": "Self-Doubt, Constant Isolation, and Over-Identification with patient delusions"},
            {"id": "C", "text": "Arrogance, Complete Emotional Detachment, and Blaming the deceased patient"},
            {"id": "D", "text": "Suppression of memory, Denial of reality, and Refusal to participate in supervision"}
        ],
        "correctAnswer": "A",
        "explanation": "Kristin Neff's Self-Compassion framework comprises: (1) Self-Kindness (being gentle, forgiving, and understanding toward oneself when suffering or failing, rather than mercilessly critical); (2) Common Humanity (perceiving one's painful experiences and fallibility as part of the universal human condition, rather than feeling uniquely defective and isolated); and (3) Mindfulness (observing one's thoughts and painful feelings with open, balanced awareness without suppressing or exaggerating them).",
        "incorrectExplanations": {
            "B": "Self-doubt, isolation, and over-identification are the exact pathologies that self-compassion reverses.",
            "C": "Blaming patients and emotional callousness reflect toxic defense mechanisms, not self-compassion.",
            "D": "Suppression and denial are maladaptive avoidance strategies that prevent healing."
        },
        "learningObjective": "Apply Kristin Neff's Mindful Self-Compassion framework to manage clinical trauma and alleviate self-blame.",
        "reference": "Neff, K. D. (2003). Self-Compassion: An Alternative Conceptualization of a Healthy Attitude Toward Oneself. Self and Identity, 2(2), 85-101; Germer, C. & Neff, K. (2019).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1180",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Intermediate",
        "questionText": "A systematic review and meta-analysis of healthcare burnout interventions (e.g., West et al., The Lancet) evaluated individual-focused strategies (mindfulness apps, yoga, resilience seminars) versus organization-directed structural interventions (improving nurse-to-patient ratios, flexible scheduling, supportive leadership, reducing documentation burden). What did the empirical evidence demonstrate regarding their relative effectiveness?",
        "options": [
            {"id": "A", "text": "Individual resilience workshops are 100% effective, proving that burnout is purely an individual personal weakness"},
            {"id": "B", "text": "Organization-directed structural interventions achieve significantly greater, more sustainable reductions in clinician burnout than individual-focused resilience programs alone, demonstrating that burnout is an organizational disease requiring systemic solutions"},
            {"id": "C", "text": "Neither individual nor organizational interventions have any effect on burnout"},
            {"id": "D", "text": "Providing mandatory yoga at 06:00 completely eliminates staff turnover"}
        ],
        "correctAnswer": "B",
        "explanation": "Extensive meta-analyses (West et al., 2016; Panagioti et al., 2017) demonstrate that while individual mindfulness/coping strategies provide modest, short-term relief, organizational-directed structural interventions (e.g., safe staffing ratios, optimized shift scheduling, reducing administrative EHR burden, fostering compassionate leadership) produce significantly greater and more enduring reductions in burnout. Treating burnout purely as a personal resilience deficit is ineffective and patronizing.",
        "incorrectExplanations": {
            "A": "Burnout is an occupational hazard caused by systemic overload, not an individual defect or weakness.",
            "C": "Substantial evidence proves that organizational redesign significantly mitigates burnout.",
            "D": "Mandatory off-shift activities increase exhaustion and resentment."
        },
        "learningObjective": "Evaluate systemic organizational interventions versus individual resilience strategies in mitigating nursing burnout.",
        "reference": "West, C. P. et al. (2016). Interventions to Prevent and Reduce Physician Burnout: A Systematic Review and Meta-Analysis. The Lancet, 388(10057), 2272-2281; National Academy of Medicine (2019).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1181",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Advanced",
        "questionText": "Following a violent assault on a staff member by an inpatient, the ward manager gathers the team for immediate 'Psychological First Aid' (PFA) and crisis defusing. Under World Health Organization and NICE PTSD guidelines, what are the core principles of immediate post-incident Psychological First Aid, and which intervention is strictly CONTRAINDICATED?",
        "options": [
            {"id": "A", "text": "PFA provides immediate practical comfort, emotional validation, checking physical injuries, ensuring basic safety and hydration, and facilitating peer connection; mandatory single-session psychological debriefing that forces staff to recount graphic trauma details is strictly contraindicated as it can worsen trauma symptoms"},
            {"id": "B", "text": "Force all staff to undergo hypnosis within 2 hours of the assault"},
            {"id": "C", "text": "Administer high-dose oral propranolol to erase the memory of the assault"},
            {"id": "D", "text": "Instruct staff never to speak of the incident under threat of termination"}
        ],
        "correctAnswer": "A",
        "explanation": "WHO and NICE NG116 guidelines recommend Psychological First Aid (PFA): humane, supportive, and practical assistance (ensuring physical safety, treating wounds, providing food/tea, offering calm presence, listening without pressure, facilitating natural social support). Crucially, formal single-session 'critical incident stress debriefing' (CISD) that forces individuals to re-live and recount graphic emotional details immediately after trauma is contraindicated, as clinical trials show it interferes with natural processing and increases PTSD risk.",
        "incorrectExplanations": {
            "B": "Immediate hypnosis has no evidence base and can induce false memories and dissociative panic.",
            "C": "Erasing memory with drugs is medically unrealistic and ethically fraught.",
            "D": "Silencing staff isolates traumatized individuals and worsens psychological morbidity."
        },
        "learningObjective": "Implement Psychological First Aid (PFA) and identify contraindications regarding mandatory single-session psychological debriefing.",
        "reference": "World Health Organization (2011). Psychological First Aid: Guide for Field Workers; NICE Guideline NG116: Post-traumatic stress disorder (2018).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1182",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Advanced",
        "questionText": "A community psychiatric nurse managing a caseload of 45 complex patients presents to clinical supervision describing chronic insomnia, feeling emotionally numb toward suicidal patients, arriving late for visits, and feeling cynical about the profession. Using the Professional Quality of Life (ProQOL) framework (Beth Hudnall Stamm), what assessment and intervention plan should the supervisor implement?",
        "options": [
            {"id": "A", "text": "Immediately dismiss the nurse from employment and report them to the police"},
            {"id": "B", "text": "Administer the ProQOL-5 scale to differentiate Compassion Satisfaction, Burnout, and Secondary Traumatic Stress; implement a collaborative workload adjustment (temporarily capping complex referrals, reallocating acute cases), review self-care boundaries, and arrange confidential occupational health counseling"},
            {"id": "C", "text": "Double the nurse's caseload to 90 patients to force them to focus on work"},
            {"id": "D", "text": "Tell the nurse that true psychiatric nurses never experience fatigue"}
        ],
        "correctAnswer": "B",
        "explanation": "The Professional Quality of Life (ProQOL) scale assesses three subscales: Compassion Satisfaction (the positive pleasure derived from caregiving), Burnout (exhaustion and frustration with the system), and Secondary Traumatic Stress (fear and trauma symptoms from work). When scores show high burnout/STS and low compassion satisfaction, supportive leadership responds by adjusting caseload acuity, auditing unmanageable workload, reinforcing boundaries, and providing specialized psychological support.",
        "incorrectExplanations": {
            "A": "Burnout is an occupational injury, not a crime; firing struggling staff destroys the workforce and is unethical.",
            "C": "Doubling caseloads in severe burnout causes clinical errors, severe depression, and suicidal crisis.",
            "D": "Denying that nurses experience stress perpetuates toxic stigma and prevents help-seeking."
        },
        "learningObjective": "Utilize the ProQOL scale to formulate supportive supervisory interventions for nurses experiencing compassion fatigue and burnout.",
        "reference": "Stamm, B. H. (2010). The Concise ProQOL Manual (2nd Ed.); Royal College of Nursing (2020) Rest, Rehydrate, Refuel Guidance.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1183",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Advanced",
        "questionText": "In occupational health psychology, what is 'Presenteeism' in mental health nursing, and what are its clinical safety implications for inpatient psychiatric care?",
        "options": [
            {"id": "A", "text": "The practice of wrapping holiday gifts for colleagues in the staffroom"},
            {"id": "B", "text": "Attending clinical shifts while physically, emotionally, or psychologically unwell (impaired presenteeism), resulting in significantly higher rates of medication administration errors, compromised situational awareness, boundary slips, patient falls, and eventual long-term sickness absence"},
            {"id": "C", "text": "Being physically present on time for every single handover for 10 consecutive years"},
            {"id": "D", "text": "The psychological theory that only the present moment exists in reality"}
        ],
        "correctAnswer": "B",
        "explanation": "Presenteeism refers to the phenomenon of employees reporting to work despite being physically, cognitively, or psychologically compromised by illness or extreme exhaustion. In psychiatric nursing, driven by staffing shortages and guilt over burdening colleagues, presenteeism is widespread. It carries severe hidden costs: impaired clinical judgment, medication errors, reduced vigilance during observation checks, relational irritability with patients, and higher ultimate disability.",
        "incorrectExplanations": {
            "A": "Presenteeism is an occupational health metric, not gift-giving.",
            "C": "Consistent punctuality is good attendance, not impaired presenteeism.",
            "D": "The philosophical concept of 'the present' is mindfulness, not occupational presenteeism."
        },
        "learningObjective": "Evaluate the clinical safety risks and organizational costs of presenteeism in psychiatric nursing.",
        "reference": "Aronsson, G. et al. (2000). Sick but Yet at Work: An Empirical Study of Sickness Presenteeism. Journal of Epidemiology & Community Health; Royal College of Physicians (2015) Work and Wellbeing in the NHS.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1184",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preventing burnout and compassion fatigue",
        "difficulty": "Expert",
        "questionText": "A psychiatric hospital executive board seeks to transition the entire mental health organization into a 'Trauma-Informed Workplace'. Beyond patient care protocols, what organizational systems must be implemented to support workforce psychological safety and resilience?",
        "options": [
            {"id": "A", "text": "Install biometric surveillance cameras in staff restrooms to ensure staff are not resting"},
            {"id": "B", "text": "Embed trauma-informed principles into human resources and management: non-punitive incident reporting, routine post-incident psychological first aid, accessible reflective supervision, trauma-informed performance appraisals, transparent leadership communication, peer support networks, and wellness environments that honor staff physical and psychological recovery needs"},
            {"id": "C", "text": "Mandate that any staff member who admits to feeling stressed is demoted immediately"},
            {"id": "D", "text": "Eliminate all sick leave entitlements to encourage psychological grit"}
        ],
        "correctAnswer": "B",
        "explanation": "A truly trauma-informed organization applies the Sanctuary Model (Bloom) or SAMHSA trauma-informed principles internally to its own staff. This involves: creating psychological safety, transparent leadership, eliminating toxic blame cultures, viewing distress as an understandable reaction to occupational trauma rather than incompetence, providing high-quality reflective supervision, ensuring safe staffing, and creating restorative physical spaces for staff.",
        "incorrectExplanations": {
            "A": "Intrusive surveillance in staff areas destroys trust, dignity, and psychological safety.",
            "C": "Punishing staff for acknowledging distress drives suffering underground and leads to catastrophic burnout and suicide.",
            "D": "Abolishing sick leave is illegal, abusive, and accelerates physical and mental collapse."
        },
        "learningObjective": "Design organizational systems and human resource policies that embody trauma-informed workplace principles for staff well-being.",
        "reference": "Bloom, S. L. (2013). Creating Presence: Organizational Supervision and the Sanctuary Model. Routledge; SAMHSA (2014) Trauma-Informed Organizational Framework.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 8: Mental health policy and legislation (Q1185 - Q1194)
    # Answers: C, D, A, B, C, D, A, B, C, D
    # Difficulties: F, F, I, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1185",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Foundation",
        "questionText": "The National Service Framework (NSF) for Mental Health (Department of Health, 1999) was a landmark 10-year policy blueprint in England. What core specialized community psychiatric services were established nationally as a direct result of the NSF standards?",
        "options": [
            {"id": "A", "text": "Private luxury psychiatric spas and exclusive residential retreats"},
            {"id": "B", "text": "Asylum re-construction programs and involuntary workhouses"},
            {"id": "C", "text": "Crisis Resolution Home Treatment (CRHT) teams, Early Intervention in Psychosis (EIP) services, and Assertive Outreach teams"},
            {"id": "D", "text": "Mandatory electroconvulsive therapy centers in local post offices"}
        ],
        "correctAnswer": "C",
        "explanation": "The 1999 National Service Framework (NSF) for Mental Health introduced 7 national standards and mandated the nationwide rollout of specialized, community-based mental health teams: Crisis Resolution and Home Treatment (CRHT) teams as an alternative to admission; Early Intervention in Psychosis (EIP) teams for young people aged 14-35; and Assertive Outreach (AO) teams for complex, hard-to-engage service users.",
        "incorrectExplanations": {
            "A": "The NSF focused on equitable, public NHS community mental health, not private spas.",
            "B": "The NSF drove modern community mental health, not asylum reconstruction.",
            "D": "ECT is administered exclusively in licensed hospital clinical suites under strict governance, not post offices."
        },
        "learningObjective": "Identify historical benchmark achievements of the National Service Framework for Mental Health.",
        "reference": "Department of Health (1999). Modernising Mental Health Services: Safe, Sound and Supportive; The National Service Framework for Mental Health.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1186",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Foundation",
        "questionText": "The concept of 'Parity of Esteem' was formally enshrined into UK statutory law through the Health and Social Care Act 2012. What does Parity of Esteem legally mandate regarding mental health services?",
        "options": [
            {"id": "A", "text": "Mental health nurses must receive the exact same uniform colors as dental hygienists"},
            {"id": "B", "text": "All psychiatric medications must cost less than £5 per prescription"},
            {"id": "C", "text": "Every general hospital must convert 90% of its surgical suites into locked psychiatric wards"},
            {"id": "D", "text": "Mental health must be valued, funded, prioritized, and treated with equal standing, urgency, and resource allocation as physical health across the entire healthcare system"}
        ],
        "correctAnswer": "D",
        "explanation": "The Health and Social Care Act 2012 established for the first time in statute the requirement to achieve 'Parity of Esteem': ensuring that mental health is valued equally with physical health. This means equitable access to evidence-based treatments, equal allocation of funding and research investment, eliminating the premature mortality gap for people with mental illness, and treating mental health crises with the same clinical urgency as physical medical emergencies.",
        "incorrectExplanations": {
            "A": "Uniform color is a local laundry/branding decision, not the statutory meaning of parity.",
            "B": "Parity of esteem is about equal healthcare priority, funding, and quality, not fixed retail medication prices.",
            "C": "Parity does not mean converting 90% of surgical beds; it means treating mental illness with equal clinical value."
        },
        "learningObjective": "Define the legal and clinical principle of 'Parity of Esteem' between mental and physical healthcare.",
        "reference": "Health and Social Care Act 2012 (c.7); Royal College of Psychiatrists (2013). Whole-person care: from rhetoric to reality (Occasional Paper OP88).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1187",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Intermediate",
        "questionText": "The National Institute for Health and Care Excellence (NICE) develops evidence-based clinical guidelines. What methodological grading system is widely utilized by NICE guideline development committees to evaluate the certainty and strength of clinical trial evidence?",
        "options": [
            {"id": "A", "text": "The GRADE framework (Grading of Recommendations Assessment, Development and Evaluation), which systematically assesses risk of bias, inconsistency, indirectness, imprecision, and publication bias across synthesized evidence"},
            {"id": "B", "text": "The Personal Preference Index of the Lead Psychiatrist"},
            {"id": "C", "text": "The Social Media Upvote Algorithm"},
            {"id": "D", "text": "The Commercial Sponsorship Value Scale"}
        ],
        "correctAnswer": "A",
        "explanation": "NICE utilizes the GRADE (Grading of Recommendations Assessment, Development and Evaluation) approach to evaluate the quality/certainty of evidence across systematic reviews and clinical trials. GRADE assesses five domains: study limitations (risk of bias), inconsistency of results, indirectness of evidence, imprecision, and publication bias, classifying evidence certainty as High, Moderate, Low, or Very Low to guide clinical recommendations.",
        "incorrectExplanations": {
            "B": "NICE guidelines rely on objective systematic review methodology, not the personal whim of a single psychiatrist.",
            "C": "Social media popularity has no place in evidence-based clinical medicine.",
            "D": "Commercial sponsorship is strictly declared and managed to prevent bias, not used as an evidence grading scale."
        },
        "learningObjective": "Describe the GRADE methodological framework used by NICE in evaluating healthcare evidence certainty.",
        "reference": "Guyatt, G. H. et al. (2008). GRADE: An Emerging Consensus on Rating Quality of Evidence and Strength of Recommendations. BMJ, 336(7650), 924-926; NICE Guidelines Manual.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1188",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Intermediate",
        "questionText": "The World Health Organization (WHO) launched the Mental Health Gap Action Programme (mhGAP). What is the primary strategic objective of mhGAP globally?",
        "options": [
            {"id": "A", "text": "To build multi-story psychiatric institutions in capital cities of low-income countries"},
            {"id": "B", "text": "To scale up evidence-based care for mental, neurological, and substance use (MNS) disorders in low- and middle-income countries (LMICs) by task-sharing and training non-specialized primary healthcare nurses and community workers in universal clinical intervention guidelines"},
            {"id": "C", "text": "To export expensive branded psychotropics exclusively to affluent private hospitals"},
            {"id": "D", "text": "To eliminate the role of registered nurses in global health policy"}
        ],
        "correctAnswer": "B",
        "explanation": "WHO mhGAP was developed to address the massive mental health treatment gap in low- and middle-income countries (where over 75% of people with mental illness receive zero treatment). mhGAP uses evidence-based 'task-shifting' and 'task-sharing', training general primary healthcare nurses, clinical officers, and community workers using the mhGAP Intervention Guide (mhGAP-IG) to identify and treat priority conditions (depression, psychosis, epilepsy, dementia, substance abuse).",
        "incorrectExplanations": {
            "A": "WHO advocates for community-based deinstitutionalized primary mental healthcare, not building new asylums.",
            "C": "mhGAP promotes essential, affordable generic psychotropics and psychosocial therapies.",
            "D": "Nurses are the central frontline delivery vehicle of the mhGAP strategy globally."
        },
        "learningObjective": "Explain the global health strategy, task-sharing approach, and clinical aims of the WHO mhGAP programme.",
        "reference": "World Health Organization (2016). mhGAP Intervention Guide for Mental, Neurological and Substance Use Disorders in Non-Specialized Health Settings (Version 2.0); WHO.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1189",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Intermediate",
        "questionText": "Article 12 of the United Nations Convention on the Rights of Persons with Disabilities (UN CRPD) addresses 'Equal recognition before the law'. What profound paradigm shift does the UN CRPD demand regarding decision-making for people with mental disabilities?",
        "options": [
            {"id": "A", "text": "A return to total paternalistic custody where hospital directors sign all life decisions"},
            {"id": "B", "text": "Denying individuals with psychiatric illness the right to vote or hold bank accounts"},
            {"id": "C", "text": "A transition from 'Substituted Decision-Making' (where doctors or guardians decide for the person based on best interests) to 'Supported Decision-Making' (where the person's will and preferences are respected, and resources/support are provided to help them make their own autonomous choices)"},
            {"id": "D", "text": "Abolishing all courts and legal systems internationally"}
        ],
        "correctAnswer": "C",
        "explanation": "Article 12 of the UN CRPD asserts that persons with disabilities, including psychosocial and cognitive disabilities, enjoy legal capacity on an equal basis with others in all aspects of life. It calls for a paradigm shift from 'substituted decision-making' (paternalistically appointing others to decide what is in the patient's 'best interests') to 'supported decision-making' (empowering and providing accommodations so the individual can express and realize their own 'will and preferences').",
        "incorrectExplanations": {
            "A": "Paternalistic institutional custody violates core human rights treaties.",
            "B": "The CRPD explicitly protects the right to vote, own property, and manage financial affairs on an equal basis.",
            "D": "CRPD operates within international and domestic legal frameworks."
        },
        "learningObjective": "Differentiate substituted decision-making from supported decision-making under the UN Convention on the Rights of Persons with Disabilities.",
        "reference": "United Nations (2006). Convention on the Rights of Persons with Disabilities (CRPD), Article 12; UN Committee on the Rights of Persons with Disabilities (General Comment No. 1, 2014).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1190",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Intermediate",
        "questionText": "The Independent Review of the Mental Health Act 1983 (chaired by Professor Sir Simon Wessely, 'Modernising the Mental Health Act', 2018) highlighted stark racial inequalities. What major finding regarding black service users prompted calls for urgent legislative reform?",
        "options": [
            {"id": "A", "text": "Black individuals were found to have zero rates of mental health hospitalizations"},
            {"id": "B", "text": "Black people were over four times more likely to be detained under the Mental Health Act, over eight times more likely to be subject to Community Treatment Orders (CTOs), and disproportionately subject to physical restraint and seclusion compared to white individuals"},
            {"id": "C", "text": "Black service users received five times more psychotherapy sessions than other demographic groups"},
            {"id": "D", "text": "Psychiatric legislation applies only to individuals born in the European Union"}
        ],
        "correctAnswer": "B",
        "explanation": "The 2018 Wessely Review exposed deep racial disparities: people of Black African and Caribbean descent in England and Wales are over four times more likely to be detained under the Mental Health Act, over eight times more likely to be made subject to a Community Treatment Order (CTO), and significantly more likely to experience police involvement, prone restraint, and seclusion. The review proposed four core principles: Choice and Autonomy, Least Restriction, Therapeutic Benefit, and the Person as an Individual.",
        "incorrectExplanations": {
            "A": "Black individuals have disproportionately higher detention rates, not zero rates.",
            "C": "Black patients face substantial barriers and lower access to early psychological therapies.",
            "D": "Domestic mental health legislation applies universally to all persons within the territorial jurisdiction."
        },
        "learningObjective": "Analyze the racial disparities identified in the Independent Review of the Mental Health Act (Wessely Review).",
        "reference": "Department of Health and Social Care (2018). Modernising the Mental Health Act: Increasing Choice, Reducing Compulsion (Wessely Review); NHS Race and Health Observatory.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1191",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Advanced",
        "questionText": "The Care Act 2014 establishes the statutory framework for adult safeguarding across England. Which six core principles of safeguarding must guide mental health nurses when responding to abuse, neglect, or exploitation of vulnerable adults?",
        "options": [
            {"id": "A", "text": "Empowerment, Prevention, Proportionality, Protection, Partnership, and Accountability"},
            {"id": "B", "text": "Prosecution, Punishment, Publicity, Paternalism, Paranoia, and Profit"},
            {"id": "C", "text": "Surveillance, Segregation, Sedation, Subjugation, Seclusion, and Silence"},
            {"id": "D", "text": "Assessment, Admission, Administration, Auditing, Arbitration, and Appeals"}
        ],
        "correctAnswer": "A",
        "explanation": "The Care Act 2014 (Section 42-46) outlines six foundational safeguarding principles: (1) Empowerment (presumption of person-led decisions and informed consent); (2) Prevention (taking action before harm occurs); (3) Proportionality (least intrusive response appropriate to the risk); (4) Protection (support and representation for those in greatest need); (5) Partnership (local multi-agency collaboration); and (6) Accountability (transparency and clear roles).",
        "incorrectExplanations": {
            "B": "Prosecution and paternalism are punitive legal concepts, not the Care Act safeguarding principles.",
            "C": "Surveillance, segregation, and sedation are abusive practices that safeguarding aims to eradicate.",
            "D": "These are general administrative steps, not statutory safeguarding principles."
        },
        "learningObjective": "Apply the six statutory safeguarding principles of the Care Act 2014 in adult mental health protection.",
        "reference": "Care Act 2014 (c.23); Department of Health and Social Care (2020). Care and Support Statutory Guidance; Social Care Institute for Excellence (SCIE).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1192",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Advanced",
        "questionText": "Under the Mental Capacity Act 2005 (England & Wales), what is the statutory definition of the 'Two-Stage Functional Test of Capacity' that a mental health nurse must conduct when assessing whether an individual can make a specific decision?",
        "options": [
            {"id": "A", "text": "Stage 1: Determining whether the patient has an IQ below 70; Stage 2: Asking if their relatives agree with the decision"},
            {"id": "B", "text": "Stage 1: Stage 1 requires a brain CT scan; Stage 2 requires an electroencephalogram"},
            {"id": "C", "text": "Stage 1 (Diagnostic threshold): Is there an impairment of, or disturbance in the functioning of, the mind or brain? Stage 2 (Functional assessment): Does that impairment render the person unable to (a) understand relevant information, (b) retain that information, (c) use or weigh that information as part of the decision-making process, or (d) communicate their decision?"},
            {"id": "D", "text": "Stage 1: Checking if the decision is wise; Stage 2: Overriding the decision if it appears eccentric"}
        ],
        "correctAnswer": "C",
        "explanation": "The MCA 2005 Two-Stage Test requires: Stage 1 (Diagnostic): Proof of an impairment or disturbance in the functioning of the mind or brain (temporary or permanent). Stage 2 (Functional): Proving that the impairment prevents the person from performing at least one of the four cognitive steps for that specific decision: (1) Understanding the information relevant to the decision; (2) Retaining that information long enough to decide; (3) Using or weighing that information; or (4) Communicating their decision (by any means).",
        "incorrectExplanations": {
            "A": "IQ scores and relative opinions do not define mental capacity under the law.",
            "B": "Neuroimaging is not a legal test of functional decision-making capacity.",
            "D": "Principle 3 of the MCA explicitly states that an individual is not to be treated as lacking capacity merely because they make an unwise decision."
        },
        "learningObjective": "Conduct the statutory Two-Stage Functional Test of Mental Capacity according to the Mental Capacity Act 2005.",
        "reference": "Mental Capacity Act 2005 (c.9) Sections 2 & 3; Department for Constitutional Affairs (2007). Mental Capacity Act Code of Practice.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1193",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Advanced",
        "questionText": "What are the legal powers and limitations of Section 5(2) of the Mental Health Act 1983 (Doctor's / Approved Clinician's Holding Power) when applied to an informal (voluntary) psychiatric inpatient?",
        "options": [
            {"id": "A", "text": "It detains an inpatient for up to 72 hours to allow a formal assessment for Section 2 or 3 to be arranged; it cannot be used in emergency departments or outpatient clinics, and it does NOT authorize treatment without consent"},
            {"id": "B", "text": "It allows a doctor to detain an outpatient in their private residence for up to 6 months"},
            {"id": "C", "text": "It permits immediate involuntary administration of depot antipsychotics without patient consent for 30 days"},
            {"id": "D", "text": "It authorizes any hospital security officer to detain visitors in the car park for 12 hours"}
        ],
        "correctAnswer": "A",
        "explanation": "Section 5(2) is a doctor's (or nominated deputy's) holding power applicable ONLY to informal inpatients currently admitted to a hospital bed (not outpatients or patients in ED who have not been formally admitted). It lasts for a maximum of 72 hours, cannot be renewed, and its sole purpose is to hold the patient safely until an assessment for detention under Section 2 or 3 can take place. Crucially, Section 5(2) does NOT grant statutory authority to treat against consent (Part 4 powers do not apply).",
        "incorrectExplanations": {
            "B": "Section 5(2) applies only to hospital inpatients, never to private residences or outpatients.",
            "C": "Section 5(2) conveys zero power to treat without consent; Part 4 treatment powers do not apply under Section 5(2).",
            "D": "Holding powers apply only to patients admitted to hospital beds, not visitors or car parks."
        },
        "learningObjective": "Explain the statutory scope, duration, and legal treatment limitations of Section 5(2) holding powers.",
        "reference": "Mental Health Act 1983: Code of Practice (DHSC, 2015); Section 5(2) Statutory Guidance.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1194",
        "module": "12. Leadership and Professional Practice",
        "topic": "Mental health policy and legislation",
        "difficulty": "Expert",
        "questionText": "In international mental health policy, Italy's 'Law 180' (the Basaglia Law, 1978) represented the world's most radical deinstitutionalization experiment, mandating the complete closure of all psychiatric asylums. What critical historical lesson does the international implementation of Law 180 teach modern mental health nurse leaders about deinstitutionalization?",
        "options": [
            {"id": "A", "text": "Closing psychiatric hospitals without first establishing comprehensive, well-funded, 24/7 community mental health networks, crisis alternatives, supported housing, and social services leads to 'trans-institutionalization'—shifting vulnerable patients from hospitals to prisons, homeless shelters, and forensic institutions"},
            {"id": "B", "text": "Mental illness vanishes spontaneously when hospital buildings are physically demolished"},
            {"id": "C", "text": "Asylums were optimal therapeutic environments and should be re-opened in every town"},
            {"id": "D", "text": "All psychotropic medications should be abolished by law"}
        ],
        "correctAnswer": "A",
        "explanation": "The Italian Basaglia Law (Law 180) pioneered human-rights-based deinstitutionalization by dismantling abusive asylums. However, international evaluations demonstrated a vital policy lesson: closing beds without having robust, well-funded community crisis teams, supported housing, assertive outreach, and vocational infrastructure already operational in the community results in 'trans-institutionalization' (the criminalization of mental illness, homelessness, and explosive growth of forensic and prison mental health populations).",
        "incorrectExplanations": {
            "B": "Demolishing buildings does not cure psychiatric illnesses; community treatment and social support are vital.",
            "C": "Asylums were characterized by human rights abuses, institutionalism, and neglect; returning to them is regressive.",
            "D": "Law 180 reformed hospital infrastructure and human rights; it did not abolish psychopharmacology."
        },
        "learningObjective": "Evaluate the systemic policy lessons and trans-institutionalization risks of international psychiatric deinstitutionalization.",
        "reference": "Basaglia, F. (1987). Psychiatry Inside Out: Selected Writings of Franco Basaglia. Columbia University Press; Thornicroft, G. & Tansella, M. (2004). Components of a Modern Mental Health Service. British Journal of Psychiatry.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 9: Workforce development and staffing (Q1195 - Q1204)
    # Answers: A, B, C, D, A, B, C, D, A, B
    # Difficulties: F, F, F, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1195",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Foundation",
        "questionText": "According to the NICE Guideline on Safe Staffing for Adult Inpatient Mental Health Wards (NG105) and empirical nursing research (Aiken, Rycroft-Malone), how does registered nurse staffing directly impact clinical outcomes on psychiatric wards?",
        "options": [
            {"id": "A", "text": "Higher proportions of registered mental health nurses (RMNs) relative to unregistered support workers and lower nurse-to-patient ratios are directly correlated with significant reductions in medication administration errors, patient-on-staff violence, self-harm incidents, seclusion use, and unplanned readmissions"},
            {"id": "B", "text": "Staffing ratios have zero impact on patient safety because outcomes are dictated purely by genetics"},
            {"id": "C", "text": "Having fewer registered nurses improves ward safety by reducing staff interference with patients"},
            {"id": "D", "text": "Replacing all registered nurses with commercial security guards reduces patient anxiety"}
        ],
        "correctAnswer": "A",
        "explanation": "Extensive empirical research (Aiken et al., Needleman, Rycroft-Malone, NICE NG105) conclusively demonstrates that higher nurse staffing levels and a richer skill-mix (higher proportion of registered mental health nurses to healthcare assistants) are associated with statistically significant decreases in adverse clinical events: reduced medication errors, lower rates of physical restraint, reduced seclusion duration, fewer violent assaults, decreased self-harm, and shorter length of stay.",
        "incorrectExplanations": {
            "B": "Decades of health services research prove that nurse staffing directly impacts clinical morbidity and mortality.",
            "C": "Fewer nurses dramatically escalates patient incidents, burnout, and preventable deaths.",
            "D": "Replacing nurses with security guards escalates violence, trauma, and coercive incidents."
        },
        "learningObjective": "Analyze empirical evidence linking registered nurse staffing levels and skill mix to inpatient clinical safety outcomes.",
        "reference": "NICE Guideline NG105: Safe staffing for adult inpatient wards in mental health (2018); Aiken, L. H. et al. (2014). Nurse Staffing and Education and Hospital Mortality in Nine European Countries. The Lancet.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1196",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Foundation",
        "questionText": "Rather than relying on static, arbitrary nurse-to-patient headcounts (e.g., '1 nurse to 5 beds'), modern psychiatric workforce planning utilizes validated patient acuity and dependency tools. What is an example of a validated psychiatric acuity tool, and how does it dynamically determine shift staffing needs?",
        "options": [
            {"id": "A", "text": "Flipping a coin at the start of each morning shift"},
            {"id": "B", "text": "Tools such as the Mental Health Optimal Staffing Tool (MHOST) or DIAS: assessing real-time patient clinical acuity (psychosis, violence, self-harm risk, observation levels) and care dependency (hygiene, eating, mobility) to calculate the precise nursing hours and skill mix required for that shift"},
            {"id": "C", "text": "Staffing the ward based purely on whichever nurse volunteers to work on a given day"},
            {"id": "D", "text": "Calculating staffing purely based on the square footage of the ward garden"}
        ],
        "correctAnswer": "B",
        "explanation": "Validated acuity/dependency instruments, such as the Mental Health Optimal Staffing Tool (MHOST), evaluate real-time patient need: levels of active psychotic symptoms, suicidality, violence risk, enhanced observation requirements (1:1 or 2:1), and physical dependency (ADL assistance). This converts dynamic patient acuity into required nursing hours per patient day (NHPPD) and skill mix, ensuring staffing flexes dynamically with clinical risk.",
        "incorrectExplanations": {
            "A": "Coin flipping is unscientific, negligent, and dangerous.",
            "C": "Volunteering neglects actual patient acuity and guarantees dangerous understaffing.",
            "D": "Garden dimensions have no correlation with acute psychiatric nursing acuity."
        },
        "learningObjective": "Utilize validated patient acuity and dependency scoring tools (e.g., MHOST) for dynamic psychiatric workforce planning.",
        "reference": "National Quality Board (NQB) (2018). Safe, Sustainable and Productive Staffing in Mental Health Services; MHOST Framework.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1197",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Foundation",
        "questionText": "When an acute psychiatric ward experiences high usage of temporary bank and agency nursing staff, which clinical governance risk is most acute, and what onboarding measure is mandatory?",
        "options": [
            {"id": "A", "text": "Bank staff may demand higher quality coffee than permanent employees"},
            {"id": "B", "text": "Agency staff will refuse to wear shoes while on duty"},
            {"id": "C", "text": "Unfamiliarity with ward layout, fire exits, emergency duress alarms, ligature anchor points, patient risk profiles, and local restrictive intervention policies; mitigated by mandatory, structured ward induction checklists and verification of PMVA competencies prior to commencing the shift"},
            {"id": "D", "text": "Temporary staff are legally forbidden from talking to registered permanent nurses"}
        ],
        "correctAnswer": "C",
        "explanation": "High reliance on temporary and agency staff is an established risk factor for patient safety incidents and adverse events. Temporary nurses often lack familiar knowledge of ward physical layout, alarm systems, ligature locations, local resuscitation equipment, and individual patient triggers. Clinical governance mandates that every temporary worker completes a formal ward orientation checklist, verifies identity/competency (including PMVA/restraint training), and receives a safety handover.",
        "incorrectExplanations": {
            "A": "Coffee preferences are trivial and unrelated to patient safety governance.",
            "B": "Professional uniform policies mandate appropriate footwear for all staff.",
            "D": "Interprofessional collaboration between permanent and temporary staff is essential for ward safety."
        },
        "learningObjective": "Identify clinical risks associated with temporary bank/agency staffing and execute mandatory ward induction protocols.",
        "reference": "NICE Guideline NG105 (2018); Care Quality Commission (CQC) Brief Guide: Staffing in Mental Health Services.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1198",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Intermediate",
        "questionText": "What are the mandatory statutory requirements for registered nurses completing the Nursing and Midwifery Council (NMC) 'Revalidation' process every three years to maintain professional registration?",
        "options": [
            {"id": "A", "text": "Passing a written 500-question medical jurisprudence exam in person at the Royal Courts of Justice"},
            {"id": "B", "text": "Paying £10,000 in cash to the professional nursing association"},
            {"id": "C", "text": "Receiving a personal recommendation letter signed by the Prime Minister"},
            {"id": "D", "text": "450 practice hours (900 if dual-registered), 35 hours of Continuing Professional Development (including at least 20 hours of participatory learning), 5 pieces of practice-related feedback, 5 written reflective accounts, a reflective discussion with an NMC registrant, a health and character declaration, professional indemnity arrangement, and confirmation from an appropriate confirmer"}
        ],
        "correctAnswer": "D",
        "explanation": "NMC Revalidation occurs triennially and requires: 450 practice hours as a registered nurse; 35 hours of CPD (with at least 20 hours participatory); 5 pieces of practice feedback (from patients, colleagues, audits); 5 written reflective accounts aligned with the Code; an official Reflective Discussion with another NMC registrant; a declaration of good health and character; valid professional indemnity insurance; and a Confirmation interview with an approved confirmer.",
        "incorrectExplanations": {
            "A": "There is no written exam at the Royal Courts for routine revalidation.",
            "B": "The annual registration fee is £120, not £10,000.",
            "C": "The Prime Minister does not sign nursing registration renewals."
        },
        "learningObjective": "Recall and fulfill all statutory components of the triennial NMC Revalidation framework.",
        "reference": "Nursing and Midwifery Council (NMC) (2019). How to Revalidate with the NMC: Requirements for Nurses and Midwives.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1199",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Intermediate",
        "questionText": "In mental health workforce scheduling, what does the research literature (e.g., Griffiths et al., Dall'Ora et al.) indicate regarding the clinical impact of 12-hour shifts compared to 8-hour shifts on psychiatric nurses and patient safety?",
        "options": [
            {"id": "A", "text": "Shifts lasting 12 hours or longer are consistently associated with significant fatigue, cognitive vigilance decrements during the final 4 hours, increased medication administration errors, higher burnout rates, and increased needle-stick injuries, despite staff favoring 12-hour shifts for condensed working weeks"},
            {"id": "B", "text": "Working 12-hour shifts completely eliminates fatigue and improves IQ by 20 points"},
            {"id": "C", "text": "Eight-hour shifts are legally prohibited in all healthcare systems worldwide"},
            {"id": "D", "text": "Shift duration has zero impact on circadian biology or human alertness"}
        ],
        "correctAnswer": "A",
        "explanation": "Extensive nursing workforce studies (Griffiths, Dall'Ora, Aiken) reveal a paradox: while nurses often prefer 12-hour shifts because working three days a week provides compressed leisure time, shifts ≥12 hours are objectively associated with severe cumulative fatigue, vigilance deficits, increased medication errors, delayed response to escalating ward conflict, occupational needle-stick injuries, and long-term burnout.",
        "incorrectExplanations": {
            "B": "Long shifts impair cognitive functioning and executive processing due to fatigue, not improve IQ.",
            "C": "Eight-hour shifts are standard across many international health systems.",
            "D": "Circadian biology and sleep pressure profoundly affect human alertness over a 12-hour period."
        },
        "learningObjective": "Critically analyze evidence regarding the impact of 12-hour shift patterns on fatigue, clinical errors, and nurse well-being.",
        "reference": "Dall'Ora, C., Griffiths, P., et al. (2016). Association of 12-Hour Shifts and Nurses' Job Satisfaction, Burnout and Intention to Leave: Findings from a European Cross-Sectional Study. BMJ Open; Royal College of Nursing Fatigue Guidance.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1200",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Intermediate",
        "questionText": "The World Health Organization (WHO) Global Code of Practice on the International Recruitment of Health Personnel establishes ethical guidelines for recruiting healthcare staff from overseas. What is the fundamental ethical mandate of this Code regarding 'Red List' countries?",
        "options": [
            {"id": "A", "text": "High-income countries must actively target and aggressively recruit all doctors and nurses from impoverished nations"},
            {"id": "B", "text": "Targeted active recruitment of healthcare workers from designated developing countries with severe universal health coverage health-workforce shortages ('Red List' nations) is strictly prohibited to prevent devastating brain-drain in vulnerable health systems"},
            {"id": "C", "text": "International nurses must surrender their passports to hospital employers upon arrival"},
            {"id": "D", "text": "International nurses are barred from receiving paid salaries during their first 5 years of service"}
        ],
        "correctAnswer": "B",
        "explanation": "The WHO Global Code of Practice on International Recruitment (and the UK Department of Health Code of Practice) enforces ethical recruitment. Countries on the WHO Health Workforce Support and Safeguards List ('Red List') face critical universal health coverage shortages. High-income countries are strictly prohibited from active, targeted recruitment of healthcare personnel from Red List countries to prevent 'brain drain' that collapses fragile healthcare infrastructures in developing nations.",
        "incorrectExplanations": {
            "A": "Aggressive recruitment from vulnerable nations is the exact unethical practice the Code was created to halt.",
            "C": "Confiscating passports is human trafficking, illegal, and a gross human rights violation.",
            "D": "International nurses are entitled to equal, fair pay and full employment rights from day one."
        },
        "learningObjective": "Explain ethical recruitment principles and 'Red List' country protections under the WHO Global Code of Practice on International Recruitment.",
        "reference": "World Health Organization (2010). WHO Global Code of Practice on the International Recruitment of Health Personnel; Department of Health and Social Care (2021) Code of Practice for the International Recruitment of Health and Social Care Personnel.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1201",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Advanced",
        "questionText": "What are the 'Four Pillars of Advanced Practice' defined by Health Education England (HEE) and NHS multi-professional advanced practice frameworks for Advanced Clinical Practitioners (ACPs) in mental health?",
        "options": [
            {"id": "A", "text": "Clinical Practice, Leadership and Management, Education, and Research"},
            {"id": "B", "text": "Policing, Restraining, Sedating, and Secluding"},
            {"id": "C", "text": "Accounting, Auditing, Billing, and Budgeting"},
            {"id": "D", "text": "Diagnosing, Prescribing, Operating, and Discharging"}
        ],
        "correctAnswer": "A",
        "explanation": "The Multi-professional Framework for Advanced Clinical Practice in England (Health Education England / NHS England) defines Advanced Clinical Practice across Four Pillars: (1) Clinical Practice (expert comprehensive clinical assessment, diagnostic reasoning, complex management, independent prescribing); (2) Leadership and Management (strategic clinical leadership, service redesign); (3) Education (educating teams, students, patients); and (4) Research (generating, evaluating, and applying research evidence to clinical practice).",
        "incorrectExplanations": {
            "B": "Coercive containment practices are not pillars of advanced practice.",
            "C": "Financial accounting is corporate management, not the HEE clinical advanced practice framework.",
            "D": "Diagnosing and prescribing are clinical tasks within the clinical practice pillar, not the four overarching pillars."
        },
        "learningObjective": "Identify and define the Four Pillars of Advanced Clinical Practice in mental health nursing.",
        "reference": "Health Education England (2017). Multi-Professional Framework for Advanced Clinical Practice in England; Royal College of Nursing Advanced Practice Standards.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1202",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Advanced",
        "questionText": "An acute psychiatric trust experiences high turnover among early-career registered mental health nurses (years 1 to 3 post-registration). What does the evidence base identify as the most effective retention strategies to stabilize the nursing workforce?",
        "options": [
            {"id": "A", "text": "Threatening nurses with legal prosecution if they resign within 5 years"},
            {"id": "B", "text": "Canceling all annual leave entitlements and increasing night shift allocations"},
            {"id": "C", "text": "Structured preceptorship frameworks, access to high-quality restorative clinical supervision, clear professional career development pathways (e.g., funded specialist courses, ACP/CNS trajectories), flexible working options, and supportive, compassionate ward leadership"},
            {"id": "D", "text": "Replacing registered nurses entirely with uncertified volunteers"}
        ],
        "correctAnswer": "C",
        "explanation": "Research on nursing retention (The King's Fund, RCN, West et al.) consistently demonstrates that nurse attrition is driven by unmanageable workload, lack of professional support, inflexible working patterns, and toxic leadership. Proven retention strategies include comprehensive 12-month preceptorships, restorative clinical supervision, clear clinical academic/specialist career ladders (e.g., non-medical prescribing, CBT), flexible self-rostering, and compassionate leadership.",
        "incorrectExplanations": {
            "A": "Legal threats are coercive, unlawful under employment law, and accelerate mass resignations.",
            "B": "Canceling annual leave breaches statutory labor laws and causes immediate burnout.",
            "D": "Replacing nurses with volunteers collapses clinical safety and quality."
        },
        "learningObjective": "Formulate evidence-based workforce retention strategies for early-career psychiatric nurses.",
        "reference": "The King's Fund (2020). The Courage of Compassion: Supporting Nurses and Midwives to Deliver High-Quality Care; Health Education England (2018) Mental Health Workforce Plan.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1203",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Advanced",
        "questionText": "In independent non-medical prescribing for mental health nurses, what legal and professional governance requirement governs an Advanced Nurse Practitioner Prescriber when prescribing psychotropic medications off-label (outside licensed indications)?",
        "options": [
            {"id": "A", "text": "Off-label prescribing by nurse prescribers is strictly illegal and incurs automatic imprisonment"},
            {"id": "B", "text": "The nurse prescriber can prescribe off-label provided they ensure there is a clear, evidence-based body of clinical literature supporting the use, the medication meets the distinct clinical needs of the individual patient where no licensed alternative is suitable, informed consent is obtained, and the clinical rationale is documented thoroughly in the health record"},
            {"id": "C", "text": "The nurse must obtain written authorization from the Secretary of State for Health for every off-label dose"},
            {"id": "D", "text": "The nurse must administer the medication secretly without telling the patient it is off-label"}
        ],
        "correctAnswer": "B",
        "explanation": "Independent nurse prescribers have the statutory authority to prescribe medicines off-label (unlicensed indications), provided they practice within their competence. Clinical governance (NMC, MHRA, Royal Pharmaceutical Society Competency Framework) mandates that off-label prescribing must be justified by robust evidence (e.g., NICE, Maudsley), used when no licensed option suffices, explained transparently to the patient with valid informed consent, and documented meticulously.",
        "incorrectExplanations": {
            "A": "Off-label prescribing is entirely legal and routine in psychiatric practice for competent prescribers.",
            "C": "Government ministers do not approve routine individual clinical prescriptions.",
            "D": "Concealing off-label status violates informed consent, professional ethics, and duty of candour."
        },
        "learningObjective": "Explain the professional and legal governance frameworks regulating off-label non-medical prescribing in mental health.",
        "reference": "Royal Pharmaceutical Society (2021). A Competency Framework for All Prescribers; Nursing and Midwifery Council (2018) Standards for Prescribing Programmes.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1204",
        "module": "12. Leadership and Professional Practice",
        "topic": "Workforce development and staffing",
        "difficulty": "Expert",
        "questionText": "During a national pandemic crisis or severe civil emergency, a mental health trust issues an emergency redeployment protocol moving psychiatric nurses to acute physical medical ICUs. How must nursing executive leadership maintain ethical and professional governance during emergency workforce redeployment?",
        "options": [
            {"id": "A", "text": "Ordering psychiatric nurses to manage complex arterial ECMO machines independently on day one without induction"},
            {"id": "B", "text": "Establish rapid competency-based skill mapping, deploy psychiatric nurses into paired/buddy models where they provide specialist psychological support and basic physiological care under senior ICU supervision, establish rapid training in PPE and infection control, ensure psychological support hubs are accessible, and maintain clear ethical escalation pathways for moral distress"},
            {"id": "C", "text": "Revoke the NMC Code of Conduct and declare that professional negligence no longer exists"},
            {"id": "D", "text": "Forbid redeployed nurses from returning to psychiatric duties permanently"}
        ],
        "correctAnswer": "B",
        "explanation": "Emergency redeployment requires rigorous clinical and ethical governance. Leaders must map competencies, deploy staff into roles that utilize their skills (e.g., managing delirium, acute agitation, supporting terrified families and dying patients), pair them with experienced ICU registrants, provide rapid skills training, and maintain psychological decompression hubs. The NMC Code remains fully in force, protecting staff who practice within their redeployed competence.",
        "incorrectExplanations": {
            "A": "Expecting specialized intensive care technical procedures without competence violates the Code and kills patients.",
            "C": "The NMC Code cannot be revoked; it provides the ethical anchor during crises.",
            "D": "Redeployment is a temporary crisis measure, not permanent forced career re-assignment."
        },
        "learningObjective": "Formulate ethical and clinical governance frameworks for crisis workforce redeployment in mental healthcare.",
        "reference": "NMC, GMC, & Health Leaders Joint Statement on Supporting Healthcare Professionals in Emergencies; Royal College of Nursing Deployment Principles.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 10: Preceptorship, mentorship and lifelong learning (Q1205 - Q1214)
    # Answers: C, D, A, B, C, D, A, B, C, D
    # Difficulties: F, F, I, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1205",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Foundation",
        "questionText": "According to the National Institute for Health and Care Excellence (NICE) and the NMC National Preceptorship Framework (2022), what is the core purpose and recommended duration of a clinical preceptorship for a newly registered mental health nurse?",
        "options": [
            {"id": "A", "text": "A 2-day classroom orientation followed by immediate assignment as the sole night coordinator for 4 wards"},
            {"id": "B", "text": "A lifetime unpaid internship where the nurse is barred from administering medications"},
            {"id": "C", "text": "A structured transition period (minimum 12 months recommended) providing dedicated preceptor support, protected learning time, regular reflective meetings, and clinical consolidation to translate theoretical knowledge into autonomous, confident, and safe professional practice"},
            {"id": "D", "text": "A disciplinary observation program for nurses who received poor degree grades"}
        ],
        "correctAnswer": "C",
        "explanation": "The NMC and NHS National Preceptorship Framework (2022) defines preceptorship as a structured transition period of around 12 months for newly registered nurses. It provides protected time, an allocated trained preceptor, structured development goals, and regular supportive meetings to bridge the gap between student status and independent clinical practitioner, fostering professional resilience and reducing first-year turnover.",
        "incorrectExplanations": {
            "A": "A 2-day orientation followed by high-acuity sole coordination is reckless, unsafe, and causes rapid burnout and clinical error.",
            "B": "Preceptorship is a fully paid professional transition for registered nurses.",
            "D": "Preceptorship is a universal developmental right for all newly qualified practitioners, not a disciplinary measure."
        },
        "learningObjective": "Define the purpose, structure, and duration of the NMC National Preceptorship Framework.",
        "reference": "NHS England (2022). National Preceptorship Framework for Nursing; Nursing and Midwifery Council (NMC) Principles for Preceptorship.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1206",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Foundation",
        "questionText": "What is the primary role and professional relationship between a designated 'Preceptor' and a newly registered mental health nurse (preceptee)?",
        "options": [
            {"id": "A", "text": "An undercover disciplinary officer whose job is to report minor mistakes to management"},
            {"id": "B", "text": "A personal assistant who handles the preceptee's administrative paperwork"},
            {"id": "C", "text": "A commercial recruiter attempting to hire the preceptee into private agency work"},
            {"id": "D", "text": "An experienced registered practitioner who acts as an approachable role model, coach, and professional guide, facilitating clinical socialization, offering regular constructive feedback, providing emotional containment, and supporting competence development without acting as a formal disciplinary judge"}
        ],
        "correctAnswer": "D",
        "explanation": "A preceptor is an experienced practitioner who supports the newly qualified nurse's professional growth. The relationship is collegial, developmental, and supportive: modeling clinical excellence, observing practice, conducting monthly 1:1 reviews, debriefing complex cases, validating feelings of imposter syndrome, and setting achievable learning milestones. The preceptor is a mentor and guide, not a disciplinary manager.",
        "incorrectExplanations": {
            "A": "A policing or surveillance role destroys trust and prevents honest reflection on learning needs.",
            "B": "Preceptors do not act as personal assistants; the preceptee must develop autonomous organizational skills.",
            "C": "Preceptorship is an internal NHS professional development partnership, not agency recruitment."
        },
        "learningObjective": "Differentiate the developmental, supportive role of a preceptor from punitive management oversight.",
        "reference": "NMC (2020). Principles for Preceptorship; Health Education England (HEE) Preceptorship Standards.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1207",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Intermediate",
        "questionText": "Graham Gibbs' Reflective Cycle (1988) is widely utilized by mental health nurses to structure post-incident learning. What are the six cyclical stages of Gibbs' Reflective Cycle in correct sequential order?",
        "options": [
            {"id": "A", "text": "Description, Feelings, Evaluation, Analysis, Conclusion, and Action Plan"},
            {"id": "B", "text": "Denial, Anger, Bargaining, Depression, Acceptance, and Relapse"},
            {"id": "C", "text": "Admit, Medicate, Restrain, Sedate, Discharge, and Bill"},
            {"id": "D", "text": "Observe, Orient, Decide, Act, Panic, and Retreat"}
        ],
        "correctAnswer": "A",
        "explanation": "Gibbs' Reflective Cycle (1988) consists of six sequential stages: (1) Description (What happened?); (2) Feelings (What were you thinking and feeling?); (3) Evaluation (What was good and bad about the experience?); (4) Analysis (What sense can you make of the situation? Linking theory to practice); (5) Conclusion (What else could you have done?); and (6) Action Plan (If it arose again, what would you do differently?).",
        "incorrectExplanations": {
            "B": "These are the stages of grief (Kübler-Ross), not Gibbs' reflective model.",
            "C": "These are clinical medical interventions, not a reflective learning cycle.",
            "D": "Observe, Orient, Decide, Act is the military OODA loop, not reflective nursing practice."
        },
        "learningObjective": "Execute Gibbs' Reflective Cycle through all six sequential stages to analyze clinical psychiatric incidents.",
        "reference": "Gibbs, G. (1988). Learning by Doing: A Guide to Teaching and Learning Methods. Further Education Unit, Oxford Polytechnic; NMC Revalidation.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1208",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Intermediate",
        "questionText": "Donald Schön's seminal work on professional knowledge distinguishes between 'Reflection-in-Action' and 'Reflection-on-Action'. How are these two reflective modes applied during acute psychiatric de-escalation?",
        "options": [
            {"id": "A", "text": "Reflection-in-action occurs only while sleeping, while reflection-on-action occurs only while eating"},
            {"id": "B", "text": "Reflection-in-action is thinking on one's feet—monitoring, reshaping, and adjusting communication dynamically in real-time as a patient escalates; reflection-on-action is the post-hoc retrospective cognitive analysis conducted after the incident to understand what occurred and inform future practice"},
            {"id": "C", "text": "Reflection-in-action is writing a blog post, while reflection-on-action is writing a hospital policy"},
            {"id": "D", "text": "Reflection-in-action is strictly illegal, while reflection-on-action is mandatory"}
        ],
        "correctAnswer": "B",
        "explanation": "Donald Schön (The Reflective Practitioner, 1983) defined Reflection-in-Action as the capacity of an expert practitioner to 'think on their feet' during ongoing practice—observing unexpected responses, reframing the situation, and adjusting actions in real time (e.g., softening vocal tone, changing posture when noticing a patient tense up). Reflection-on-Action is retrospective critical contemplation after the event, exploring why things occurred and developing future knowledge.",
        "incorrectExplanations": {
            "A": "Schön's model describes active conscious professional cognition, not sleep/eating.",
            "C": "Reflective practice is an internal cognitive process, not blog or policy writing.",
            "D": "Both modes are foundational, celebrated components of reflective nursing excellence."
        },
        "learningObjective": "Differentiate Donald Schön's 'Reflection-in-Action' from 'Reflection-on-Action' during psychiatric nursing interventions.",
        "reference": "Schön, D. A. (1983). The Reflective Practitioner: How Professionals Think in Action. Basic Books; Rolfe, G. et al. (2011). Critical Reflection in Practice.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1209",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Intermediate",
        "questionText": "Christopher Johns' Model of Structured Reflection guides clinicians through 'Looking In' and 'Looking Out'. What does the nurse examine during the 'Looking In' phase?",
        "options": [
            {"id": "A", "text": "Examining microscope slides of peripheral blood smears"},
            {"id": "B", "text": "Looking inside the patient's bedside cabinet for contraband items"},
            {"id": "C", "text": "Examining one's internal self: engaging with personal thoughts, sensations, emotions, values, biases, and visceral reactions experienced during the clinical encounter"},
            {"id": "D", "text": "Inspecting the interior architecture of the ward seclusion suite"}
        ],
        "correctAnswer": "C",
        "explanation": "Johns' Model of Structured Reflection (2000) structures reflection across two perspectives: 'Looking In' (turning inward to examine personal thoughts, sensations, bodily reactions, emotional triggers, and core values that arose during the situation) and 'Looking Out' (examining the external context: what was happening around the nurse, what choices were available, what ethics/literature applied, and what the consequences were).",
        "incorrectExplanations": {
            "A": "Microscope examinations are laboratory pathology tasks.",
            "B": "Cabinet searches are procedural security measures.",
            "D": "Inspecting seclusion architecture is physical safety auditing."
        },
        "learningObjective": "Apply Johns' Model of Structured Reflection to explore internal self-awareness ('Looking In') in psychiatric nursing.",
        "reference": "Johns, C. (2000). Becoming a Reflective Practitioner. Blackwell Science; Johns, C. (2009). Engaging Reflection in Practice.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1210",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Intermediate",
        "questionText": "In Malcolm Knowles' Theory of Adult Learning (Andragogy), what are the foundational assumptions regarding adult learners that nurse educators must apply when designing continuing professional development (CPD) programs?",
        "options": [
            {"id": "A", "text": "Adults learn best through rote memorization, strict corporal punishment, and standardized silent examinations"},
            {"id": "B", "text": "Adults have zero life experience to contribute and must be treated as completely empty vessels"},
            {"id": "C", "text": "Adults are motivated purely by fear of management dismissal"},
            {"id": "D", "text": "Adults are self-directed, bring a rich reservoir of prior lived and professional experience, are readiness-oriented when learning connects to real-world tasks, seek immediate problem-centered application, and are driven by internal intrinsic motivators"}
        ],
        "correctAnswer": "D",
        "explanation": "Malcolm Knowles' Andragogy outlines 6 core assumptions of adult learners: (1) Self-concept: adults move from dependency to self-direction; (2) Experience: adults possess an expanding reservoir of experience that serves as a rich learning resource; (3) Readiness to learn: oriented toward developmental social/work roles; (4) Orientation: problem-centered and task-centered rather than subject-centered; (5) Need to know: why they need to learn something; and (6) Motivation: primarily intrinsic (personal growth, pride, self-efficacy).",
        "incorrectExplanations": {
            "A": "Rote memorization and punishment describe authoritarian pedagogy, the opposite of andragogy.",
            "B": "Treating adults as empty vessels (Freire's 'banking model of education') alienates learners.",
            "C": "Adults are primarily driven by intrinsic motivation and desire for mastery."
        },
        "learningObjective": "Apply Malcolm Knowles' principles of andragogy to design effective continuing professional development in mental healthcare.",
        "reference": "Knowles, M. S. (1984). Andragogy in Action: Applying Modern Principles of Adult Learning. Jossey-Bass; Kaufman, D. M. (2003). Applying Educational Theory in Practice. BMJ.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1211",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Advanced",
        "questionText": "What is an 'Action Learning Set' (Reg Revans), and how does it foster complex problem-solving in postgraduate psychiatric nursing leadership?",
        "options": [
            {"id": "A", "text": "A small, consistent peer group that meets regularly where a 'presenter' shares an actual, unresolved workplace dilemma, and fellow members support learning by asking insightful, open, non-judgmental questions rather than giving immediate advice, empowering the presenter to reframe the problem and formulate their own action strategy"},
            {"id": "B", "text": "A formal disciplinary tribunal convened to punish failing nurses"},
            {"id": "C", "text": "A traditional didactic lecture where a professor reads PowerPoint slides for 8 hours without questions"},
            {"id": "D", "text": "A physical sports team organized to compete in hospital football tournaments"}
        ],
        "correctAnswer": "A",
        "explanation": "Action Learning (Revans, 1982) is a powerful experiential learning methodology. A small cohort (typically 6-8 peers) forms an Action Learning Set. Members take turns presenting real, intractable workplace challenges (e.g., managing ward conflict, implementing least restrictive practice). Set members do not jump in with quick-fix advice; instead, they ask probing, reflective, open questions that challenge assumptions, enabling the presenter to discover innovative solutions, commit to action, and report back at the next meeting.",
        "incorrectExplanations": {
            "B": "Action Learning Sets are non-evaluative, supportive peer coaching environments, not disciplinary panels.",
            "C": "Didactic lectures are passive teaching; Action Learning is active, peer-driven inquiry.",
            "D": "Sports teams are recreational activities, not Action Learning Sets."
        },
        "learningObjective": "Facilitate Action Learning Sets (ALS) to resolve complex psychiatric leadership and clinical governance challenges.",
        "reference": "Revans, R. (1982). The Origin and Growth of Action Learning. Chartwell-Bratt; McGill, I. & Beaty, L. (2001). Action Learning: A Guide for Professional, Management and Educational Development. Routledge.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1212",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Advanced",
        "questionText": "How does a professional developmental 'Portfolio' differ from a simple chronological resume/CV in postgraduate mental health nursing practice?",
        "options": [
            {"id": "A", "text": "A portfolio contains only passport photographs and tax returns"},
            {"id": "B", "text": "A portfolio is a dynamic, curated collection of evidence demonstrating progressive clinical competence, critical event analyses, reflective writing, patient/peer feedback, quality improvement project audits, CPD certificates, and ethical self-appraisal aligned directly with regulatory professional standards"},
            {"id": "C", "text": "A portfolio is required only for nurses who have received formal disciplinary warnings"},
            {"id": "D", "text": "A portfolio is an investment folder containing private stock certificates and company bonds"}
        ],
        "correctAnswer": "B",
        "explanation": "Unlike a curriculum vitae (which simply lists chronological employment dates and degrees), a professional nursing portfolio is an evidence-based reflective dossier. It synthesizes evidence of lifelong learning, mapped directly against professional standards (such as the NMC Code): reflective accounts on practice, patient testimonials, critical incident reviews, clinical audit data, CPD certificates, peer evaluations, and future development goals.",
        "incorrectExplanations": {
            "A": "Passports and tax records are administrative identity documents, not a clinical portfolio.",
            "C": "Portfolios are mandatory for all registered nurses (e.g., for NMC revalidation), not just disciplined staff.",
            "D": "Financial stock portfolios are commercial assets, not clinical nursing portfolios."
        },
        "learningObjective": "Construct and maintain an evidence-based professional learning portfolio aligned with regulatory standards.",
        "reference": "Jasper, M. (2006). Professional Development, Reflection and Decision-Making in Nursing and Healthcare. Blackwell; NMC Revalidation Guidance.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1213",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Advanced",
        "questionText": "In organizational mentoring theory (e.g., David Clutterbuck / Kathy Kram), what is the key distinction between a 'Formal Mentorship' program and an 'Informal Mentorship' relationship?",
        "options": [
            {"id": "A", "text": "Formal mentorship is assigned and organized by the institution with explicit objectives, structured contracts, scheduled reviews, and organizational monitoring, whereas informal mentorship develops organically through mutual professional chemistry, shared values, and spontaneous peer support without administrative mandates"},
            {"id": "B", "text": "Formal mentors are paid £1,000 per hour, while informal mentors receive free hospital meals"},
            {"id": "C", "text": "Formal mentorship occurs only via social media text messages, while informal mentorship occurs in courtroom hearings"},
            {"id": "D", "text": "Formal mentorship is legally restricted to physicians, while nurses may only access informal mentoring"}
        ],
        "correctAnswer": "A",
        "explanation": "Mentorship theory (Kram, 1985; Clutterbuck, 2014) identifies two primary forms: Formal Mentorship (institutionally facilitated, structured matching of mentor and mentee, clear developmental contracts, established goals, fixed duration, and HR evaluation) and Informal Mentorship (emerging spontaneously based on mutual rapport, shared clinical passions, and natural alignment, often lasting for decades). Both forms provide vital career and psychosocial support.",
        "incorrectExplanations": {
            "B": "Mentorship in nursing is a voluntary or professional development role, not commercial hourly cash contracting.",
            "C": "Formal mentoring is professional and structured, not social media texting.",
            "D": "Mentorship is widely established across all healthcare professions, especially nursing."
        },
        "learningObjective": "Compare the structure, psychological dynamics, and organizational outcomes of formal versus informal mentorship in psychiatric nursing.",
        "reference": "Kram, K. E. (1985). Mentoring at Work: Developmental Relationships in Organizational Life. Scott Foresman; Clutterbuck, D. (2014). Everyone Needs a Mentor (5th Ed.).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1214",
        "module": "12. Leadership and Professional Practice",
        "topic": "Preceptorship, mentorship and lifelong learning",
        "difficulty": "Expert",
        "questionText": "The National Institute for Health and Care Research (NIHR) and NHS England have established 'Clinical Academic Career Pathways' for nurses. What is the defining characteristic and strategic value of a Clinical Academic Mental Health Nurse?",
        "options": [
            {"id": "A", "text": "They leave bedside nursing permanently to write abstract poetry in an isolated library"},
            {"id": "B", "text": "They surrender their nursing registration to become full-time pharmaceutical sales agents"},
            {"id": "C", "text": "They work exclusively in hospital catering while auditing cafeteria recipes"},
            {"id": "D", "text": "They concurrently maintain active clinical psychiatric nursing practice while leading rigorous academic health research (e.g., through PhDs/post-doctoral fellowships), directly bridging the gap between empirical evidence and ward bedside practice to drive innovation, clinical trial delivery, and evidence-based patient outcomes"}
        ],
        "correctAnswer": "D",
        "explanation": "Clinical Academic Nurses (supported by NIHR, HEE, and university partnerships) maintain a dual clinical-academic career: actively delivering expert clinical care to patients while simultaneously holding academic research appointments. This bridges the notorious 'theory-practice gap' by embedding research questions generated directly at the clinical bedside, testing interventions in real-world psychiatric settings, and translating empirical findings into immediate healthcare improvements.",
        "incorrectExplanations": {
            "A": "Clinical academics maintain active clinical practice; they do not abandon patients for pure abstraction.",
            "B": "Clinical academics are registered nurse scientists and researchers, not pharmaceutical salespersons.",
            "C": "Catering recipe audits are facilities tasks unrelated to clinical academic nursing research."
        },
        "learningObjective": "Evaluate the structure and strategic clinical value of Clinical Academic Career Pathways in mental health nursing.",
        "reference": "National Institute for Health and Care Research (NIHR) (2021). Clinical Academic Careers: Nursing, Midwifery and Allied Health Professionals; Health Education England.",
        "contentReviewStatus": "Peer Reviewed"
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(MOD12_PART2)} questions for Module 12 Part 2.")
