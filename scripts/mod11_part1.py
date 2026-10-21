# scripts/mod11_part1.py
# Questions Q1015 to Q1064 (Topics 1 to 5 of Module 11)

MOD11_PART1 = [
    # -------------------------------------------------------------
    # Topic 1: Treatment-resistant depression (TRD) (Q1015 - Q1024)
    # Answers: A, B, C, D, A, B, C, D, A, B
    # Difficulties: F, F, F, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1015",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Foundation",
        "questionText": "A 44-year-old patient with major depressive disorder has shown no clinical improvement after a 6-week trial of sertraline 150 mg daily, followed by an 8-week trial of venlafaxine 225 mg daily, both with confirmed strict adherence. According to consensus clinical guidelines, which criterion defines Treatment-Resistant Depression (TRD)?",
        "options": [
            {"id": "A", "text": "Failure to achieve clinical response after at least two adequate trials of different antidepressant classes at therapeutic doses and duration"},
            {"id": "B", "text": "Persistent depressive symptoms despite receiving high-dose monotherapy with an SSRI for a minimum of 4 weeks"},
            {"id": "C", "text": "Relapse of depressive episodes occurring within 6 months of discontinuing a successful first-line antidepressant"},
            {"id": "D", "text": "Absence of remission following combination therapy with an antidepressant and high-intensity psychotherapy"}
        ],
        "correctAnswer": "A",
        "explanation": "Treatment-resistant depression (TRD) is formally defined in international guidelines (including NICE, Maudsley, and APA) as the failure to achieve meaningful clinical response or remission following at least two trials of antidepressants from different pharmacological classes, administered at adequate therapeutic dosages for an adequate duration (typically 6-8 weeks) with verified treatment adherence.",
        "incorrectExplanations": {
            "B": "A single failed trial of an SSRI for 4 weeks represents an inadequate trial or non-response, not treatment-resistant depression.",
            "C": "Relapse within 6 months following treatment discontinuation reflects recurrence/relapse, not treatment resistance.",
            "D": "Failure to achieve remission with antidepressant plus psychotherapy is refractory depression or non-response, but psychotherapy is not a mandatory prerequisite in the consensus pharmacological definition of TRD."
        },
        "learningObjective": "Define the diagnostic consensus criteria for treatment-resistant depression (TRD).",
        "reference": "NICE Guideline NG222: Depression in adults: treatment and management (2022); Maudsley Prescribing Guidelines in Psychiatry (14th Ed).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1016",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Foundation",
        "questionText": "A psychiatric nurse is reviewing the laboratory monitoring protocol for a 52-year-old patient with treatment-resistant depression who is starting lithium augmentation alongside an ongoing therapeutic dose of duloxetine. What is the recommended target serum lithium range for antidepressant augmentation, and which baseline organ systems require mandatory screening?",
        "options": [
            {"id": "A", "text": "0.8 to 1.2 mmol/L; hepatic enzymes and pulmonary function testing"},
            {"id": "B", "text": "0.6 to 0.8 mmol/L; renal function (eGFR/creatinine), thyroid function (TSH/FT4), serum calcium, and baseline ECG"},
            {"id": "C", "text": "0.2 to 0.4 mmol/L; full blood count, coagulation profile, and serum amylase"},
            {"id": "D", "text": "1.0 to 1.4 mmol/L; fasting lipid panel, HbA1c, and abdominal ultrasound"}
        ],
        "correctAnswer": "B",
        "explanation": "For lithium augmentation in unipolar treatment-resistant depression, consensus guidelines recommend a target 12-hour post-dose serum level of 0.6 to 0.8 mmol/L (lower than the 0.8-1.0 mmol/L often targeted in acute bipolar mania). Mandatory baseline monitoring includes renal function (urea, creatinine, eGFR), thyroid function tests (TSH, free T4), serum calcium (due to hyperparathyroidism risk), weight/BMI, and an ECG.",
        "incorrectExplanations": {
            "A": "0.8 to 1.2 mmol/L is the acute antimanic range and risks toxicity in long-term unipolar augmentation; pulmonary testing is not routine for lithium.",
            "C": "0.2 to 0.4 mmol/L is subtherapeutic for antidepressant augmentation and fails to confer therapeutic benefit.",
            "D": "1.0 to 1.4 mmol/L carries a significant risk of acute neurotoxicity and nephrotoxicity; abdominal ultrasound is not indicated."
        },
        "learningObjective": "Identify therapeutic serum levels and baseline monitoring parameters for lithium augmentation in TRD.",
        "reference": "Taylor, D. et al. The Maudsley Prescribing Guidelines in Psychiatry (14th Ed., 2021); NICE Guideline NG222.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1017",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Foundation",
        "questionText": "A patient with refractory major depression is commenced on aripiprazole 5 mg daily as an atypical antipsychotic augmentation strategy to their fluoxetine regimen. During the first two weeks of treatment, which common motor adverse effect must the nurse routinely screen for using a validated clinical rating scale?",
        "options": [
            {"id": "A", "text": "Oculogyric crisis using the Simpson-Angus Scale"},
            {"id": "B", "text": "Severe tardive dystonia using the Abnormal Involuntary Movement Scale"},
            {"id": "C", "text": "Akathisia (motor restlessness and inner tension) using the Barnes Akathisia Rating Scale"},
            {"id": "D", "text": "Cogwheel rigidity and resting tremor using the Unified Parkinson's Disease Rating Scale"}
        ],
        "correctAnswer": "C",
        "explanation": "Akathisia—a distressing subjective sense of inner restlessness accompanied by an urge to move the lower limbs—is the most common adverse effect during early low-dose aripiprazole augmentation (occurring in up to 25% of patients due to partial D2 agonism). It is best monitored using the Barnes Akathisia Rating Scale (BARS). Failure to detect akathisia can lead to misinterpretation as worsening depressive agitation or increased suicidality.",
        "incorrectExplanations": {
            "A": "Acute oculogyric crisis is rare with low-dose aripiprazole augmentation compared to high-potency first-generation antipsychotics.",
            "B": "Tardive dystonia is a late-onset movement disorder occurring after months or years of antipsychotic exposure, not in the first 2 weeks.",
            "D": "While parkinsonism can occur, akathisia is substantially more frequent and acute with aripiprazole augmentation."
        },
        "learningObjective": "Screen for and recognize aripiprazole-induced akathisia during antidepressant augmentation therapy.",
        "reference": "Barnes, T. R. (2003). The Barnes Akathisia Rating Scale. British Journal of Psychiatry; Maudsley Prescribing Guidelines (14th Ed).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1018",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Intermediate",
        "questionText": "A 38-year-old inpatient with TRD is receiving intranasal esketamine under a specialized Risk Evaluation and Mitigation Strategy (REMS) protocol. What are the key nursing responsibilities during and immediately following the administration session?",
        "options": [
            {"id": "A", "text": "Continuous cardiac telemetry for 6 hours and mandatory administration of prophylactic IV naloxone"},
            {"id": "B", "text": "Enforcing 24-hour strict bed rest and routine catheterization to monitor drug-induced urinary retention"},
            {"id": "C", "text": "Serial blood glucose fingersticks every 15 minutes and hourly arterial blood gas analysis"},
            {"id": "D", "text": "Monitoring blood pressure, heart rate, and dissociative symptoms for a minimum of 2 hours, ensuring the patient does not drive until the next day after restful sleep"}
        ],
        "correctAnswer": "D",
        "explanation": "Esketamine nasal spray causes transient elevations in systolic and diastolic blood pressure, heart rate, dissociation, sedation, and perceptual changes that peak at approximately 40 minutes and resolve by 90-120 minutes. REMS protocols require direct observation by a healthcare professional for at least 2 hours post-dose until clinical recovery and hemodynamic stability are confirmed, with explicit guidance not to operate heavy machinery or drive until the following day after restful sleep.",
        "incorrectExplanations": {
            "A": "Continuous telemetry for 6 hours is not indicated, and naloxone is an opioid antagonist not indicated for NMDA-receptor antagonist therapy.",
            "B": "Strict bed rest for 24 hours and routine catheterization are unnecessary and excessively restrictive.",
            "C": "Serial blood glucose and ABG analyses are clinically irrelevant for esketamine administration."
        },
        "learningObjective": "Implement nursing monitoring and patient safety protocols during intranasal esketamine administration.",
        "reference": "FDA Esketamine REMS Guidelines; European Medicines Agency (EMA) Spravato Assessment Report; NICE TA598.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1019",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Intermediate",
        "questionText": "A 56-year-old patient who failed multiple SSRIs and SNRIs is being switched to the irreversible monoamine oxidase inhibitor (MAOI) tranylcypromine. When delivering comprehensive dietary and medication education, which critical guidance must the mental health nurse provide to prevent a fatal hypertensive crisis?",
        "options": [
            {"id": "A", "text": "Strictly avoid tyramine-rich foods (such as aged cheeses, cured meats, and draft beer) and sympathomimetic decongestants, and report severe occipital headache immediately"},
            {"id": "B", "text": "Avoid leafy green vegetables high in vitamin K to prevent sudden hypocoagulability and intracranial bleeding"},
            {"id": "C", "text": "Discontinue all dietary sodium and potassium supplements to avoid acute hyperkalemic cardiac arrhythmias"},
            {"id": "D", "text": "Consume milk and dairy products freely while avoiding only citrus fruits and acidic juices"}
        ],
        "correctAnswer": "A",
        "explanation": "Irreversible non-selective MAOIs inhibit gut and hepatic MAO-A, preventing the normal catabolism of dietary tyramine. Ingestion of tyramine-rich items (mature/aged cheeses, fermented meats, tap beer, soy sauce, yeast extracts) displaces stored norepinephrine, causing severe peripheral vasoconstriction and hypertensive crisis (manifesting with severe occipital headache, palpitations, neck stiffness, and risk of stroke). Direct/indirect sympathomimetics (e.g., pseudoephedrine) and serotonergic agents must also be avoided.",
        "incorrectExplanations": {
            "B": "Vitamin K interactions occur with warfarin anticoagulation, not monoamine oxidase inhibitors.",
            "C": "Restricting dietary sodium and potassium is not related to MAOI tyramine interactions.",
            "D": "Aged dairy products are rich in tyramine and strictly contraindicated; citrus fruits do not contain dangerous tyramine levels."
        },
        "learningObjective": "Educate patients on dietary tyramine restrictions and early signs of hypertensive crisis associated with MAOI therapy.",
        "reference": "Maudsley Prescribing Guidelines in Psychiatry (14th Ed., 2021); Stahl's Essential Psychopharmacology (5th Ed).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1020",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Intermediate",
        "questionText": "An off-label intravenous ketamine infusion (0.5 mg/kg over 40 minutes) is administered to an inpatient experiencing severe treatment-resistant depression with acute active suicidal ideation. How should the mental health nurse interpret the expected therapeutic duration and trajectory of ketamine's antisuicidal effect?",
        "options": [
            {"id": "A", "text": "The rapid antidepressant and antisuicidal response usually begins within 2-4 hours, peaks at 24 hours, but often wanes within 3 to 7 days without maintenance strategies"},
            {"id": "B", "text": "Ketamine provides permanent synaptic remodeling that eliminates depressive symptoms permanently after a single 40-minute infusion"},
            {"id": "C", "text": "Antidepressant effects are strictly delayed, requiring at least 4 to 6 weeks of daily intravenous infusions to manifest"},
            {"id": "D", "text": "Ketamine is only effective in relieving depressive symptoms if the patient experiences continuous dissociative hallucinations for 48 hours"}
        ],
        "correctAnswer": "A",
        "explanation": "Subanesthetic intravenous ketamine provides rapid-onset reductions in depressive symptoms and active suicidal ideation, often detectable within 2 to 4 hours post-infusion and peaking around 24 hours. However, the effect is transient; without repeat infusions or oral continuation pharmacotherapy, symptoms typically return within 3 to 7 days. Nurses must prepare comprehensive ongoing safety plans and transition strategies.",
        "incorrectExplanations": {
            "B": "A single infusion does not produce permanent remission; relapse occurs in the vast majority within days or weeks.",
            "C": "Ketamine is noted for its rapid-acting onset within hours, unlike standard monoaminergic antidepressants which take weeks.",
            "D": "Dissociation is a transient side effect rather than a required mediator of therapeutic efficacy."
        },
        "learningObjective": "Describe the temporal response profile and transient nature of intravenous ketamine in acute treatment-resistant depression.",
        "reference": "Sanacora, G. et al. (2017). A Consensus Statement on the Use of Ketamine in the Treatment of Mood Disorders. JAMA Psychiatry, 74(4), 399-405.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1021",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Advanced",
        "questionText": "A 49-year-old patient who experienced intolerable side effects and lack of efficacy on sertraline, citalopram, and venlafaxine undergoes pharmacogenomic testing. The results reveal that the patient is a CYP2D6 'poor metabolizer' and a CYP2C19 'ultrarapid metabolizer'. How should the mental health clinical nurse specialist interpret these findings in relation to past treatment failures?",
        "options": [
            {"id": "A", "text": "The patient experienced lack of efficacy from venlafaxine due to excessive metabolism into inactive glucuronides by CYP2D6"},
            {"id": "B", "text": "Citalopram and sertraline were likely rapidly cleared due to CYP2C19 ultrarapid metabolism leading to subtherapeutic plasma levels, while standard doses of CYP2D6-dependent medications accumulated to toxic levels causing adverse effects"},
            {"id": "C", "text": "The pharmacogenomic profile indicates that all oral psychotropic medications are completely contraindicated due to hepatic bypass"},
            {"id": "D", "text": "The patient possesses defective blood-brain barrier P-glycoprotein pumps preventing any central monoamine reuptake inhibition"}
        ],
        "correctAnswer": "B",
        "explanation": "Citalopram and sertraline are predominantly metabolized by CYP2C19. An ultrarapid metabolizer clears these medications excessively fast, resulting in subtherapeutic drug concentrations and perceived lack of efficacy at standard dosages. Conversely, CYP2D6 poor metabolizers experience impaired clearance of drugs dependent on CYP2D6 (such as venlafaxine conversion to desvenlafaxine), causing elevated parent drug plasma levels and severe dose-limiting toxicities.",
        "incorrectExplanations": {
            "A": "CYP2D6 poor metabolizers fail to convert venlafaxine to desvenlafaxine, causing accumulation of parent drug and adverse effects, not rapid clearance.",
            "C": "Pharmacogenomic variants guide precision dosing and drug selection; they do not contraindicate all oral psychotropics.",
            "D": "CYP enzymes are hepatic cytochrome P450 phase I metabolic enzymes, not blood-brain barrier P-glycoprotein transporters."
        },
        "learningObjective": "Apply pharmacogenomic principles (CYP2D6 and CYP2C19 phenotypes) to analyze antidepressant treatment resistance and toxicity.",
        "reference": "Clinical Pharmacogenetics Implementation Consortium (CPIC) Guidelines for Antidepressants; Hicks, J. K. et al. (2015). Clinical Pharmacology & Therapeutics.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1022",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Advanced",
        "questionText": "When cross-tapering a patient from paroxetine 40 mg daily to phenelzine 45 mg daily for severe refractory depression, which critical transition protocol must the mental health team strictly enforce to avert potentially fatal serotonin toxicity?",
        "options": [
            {"id": "A", "text": "Start phenelzine at full dose immediately upon stopping paroxetine to maintain uninterrupted serotonin transporter occupancy"},
            {"id": "B", "text": "Administer high-dose cyproheptadine concurrently throughout a 48-hour rapid cross-taper"},
            {"id": "C", "text": "Gradually taper paroxetine, followed by a mandatory minimum 2-week drug-free washout period before introducing phenelzine"},
            {"id": "D", "text": "Maintain paroxetine at half dose for 6 weeks while titrating phenelzine to ensure antidepressant synergy"}
        ],
        "correctAnswer": "C",
        "explanation": "Switching from an SSRI (such as paroxetine) to an MAOI (such as phenelzine) carries a severe risk of serotonin toxicity (serotonin syndrome) if done without an adequate washout period. Guidelines mandate tapering and discontinuing the SSRI, followed by a minimum 2-week complete washout (or 5-6 weeks in the case of fluoxetine due to the prolonged half-life of its active metabolite norfluoxetine) before initiating an MAOI.",
        "incorrectExplanations": {
            "A": "Direct switching without washout is an absolute contraindication that frequently precipitates fatal serotonin syndrome (hyperthermia, clonus, autonomic collapse).",
            "B": "Cyproheptadine is an antidote used to treat established serotonin syndrome, not a prophylactic agent enabling unsafe concurrent administration.",
            "D": "Combining paroxetine and phenelzine concurrently is strictly contraindicated due to lethal serotonergic overstimulation."
        },
        "learningObjective": "Plan and manage safe switching and washout intervals between SSRIs and MAOIs to avoid serotonin toxicity.",
        "reference": "NICE Guideline NG222 (2022); Dunkley, E. J. et al. (2003). The Hunter Serotonin Toxicity Criteria. QJM: An International Journal of Medicine.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1023",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Advanced",
        "questionText": "A 46-year-old patient with euthyroid treatment-resistant depression is prescribed liothyronine (triiodothyronine / T3) 25 mcg daily as an adjunctive strategy to citalopram. What clinical monitoring should the mental health nurse prioritize during the initiation and titration of T3 augmentation?",
        "options": [
            {"id": "A", "text": "Signs of hyperthyroidism (such as palpitations, tachycardia, tremor, heat intolerance, and insomnia) alongside periodic bone density and cardiac assessments"},
            {"id": "B", "text": "Signs of hypothyroidism including severe hypothermia, periorbital myxedema, and profound constipation"},
            {"id": "C", "text": "Serum amylase and lipase levels every 48 hours to detect drug-induced acute necrotizing pancreatitis"},
            {"id": "D", "text": "Weekly coagulation studies due to competitive antagonism of prothrombin synthesis"}
        ],
        "correctAnswer": "A",
        "explanation": "Liothyronine (T3) augmentation enhances central noradrenergic and serotonergic neurotransmission. Even in patients who are euthyroid at baseline, exogenous T3 can induce iatrogenic hyperthyroidism. The nurse must screen for resting tachycardia, cardiac arrhythmias, fine resting tremor, diaphoresis, insomnia, and anxiety, and monitor long-term risks such as bone demineralization and osteoporosis.",
        "incorrectExplanations": {
            "B": "T3 administration introduces active thyroid hormone, causing thyrotoxic symptoms rather than myxedema or hypothermia.",
            "C": "Pancreatitis is not a known or monitored complication of thyroid hormone augmentation.",
            "D": "T3 does not antagonize prothrombin synthesis; weekly coagulation studies are unwarranted."
        },
        "learningObjective": "Monitor clinical symptoms and potential adverse outcomes of thyroid hormone (T3) augmentation in TRD.",
        "reference": "Cooper-Kazaz, R. et al. (2007). Combining Liothyronine with Antidepressants. Journal of Affective Disorders; Maudsley Prescribing Guidelines (14th Ed).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1024",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Treatment-resistant depression (TRD)",
        "difficulty": "Expert",
        "questionText": "A 61-year-old patient with severe, unremitting major depressive disorder and psychotic nihilistic delusions (Cotard's syndrome) has ceased eating and drinking for 48 hours, demonstrating progressive dehydration and severe psychomotor stupor. Two previous outpatient trials of venlafaxine 300 mg and mirtazapine 45 mg with olanzapine were unsuccessful. What is the most evidence-based, urgent clinical recommendation for the multidisciplinary psychiatric team?",
        "options": [
            {"id": "A", "text": "Commence a trial of tranylcypromine monotherapy following a 3-week inpatient washout period while maintaining palliative subcutaneous hydration"},
            {"id": "B", "text": "Initiate urgent bilateral electroconvulsive therapy (ECT) with immediate medical fluid resuscitation and nutritional stabilization"},
            {"id": "C", "text": "Begin outpatient cognitive behavioral therapy for psychosis (CBTp) combined with low-dose oral buspirone augmentation"},
            {"id": "D", "text": "Switch to high-dose IV chlorpromazine to sedate the patient until delusions spontaneously remit"}
        ],
        "correctAnswer": "B",
        "explanation": "In severe melancholic or psychotic depression accompanied by life-threatening refusal of food/fluids, profound psychomotor stupor, or catatonia, electroconvulsive therapy (ECT) is the first-line treatment of choice with highest clinical urgency. It achieves remission rates of 75-90% in psychotic depression and acts far more rapidly than any oral pharmacological combination, which would be inappropriate given the acute physical deterioration and failure of dual-action combinations.",
        "incorrectExplanations": {
            "A": "A 3-week washout in an acute, dehydrated, non-eating patient with psychotic depression is medically negligent and carries high mortality risk.",
            "C": "Psychotherapy requires intact cognitive processing and cannot treat severe catatonic psychomotor stupor or acute dehydration.",
            "D": "High-dose chlorpromazine carries severe cardiovascular/anticholinergic risks, does not treat psychotic depression effectively, and worsens catatonic stupor."
        },
        "learningObjective": "Identify life-threatening clinical indications for urgent electroconvulsive therapy in severe psychotic refractory depression.",
        "reference": "American Psychiatric Association (APA) Guideline for the Treatment of Patients with Major Depressive Disorder; NICE Guideline NG222.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 2: Electroconvulsive therapy (ECT) (Q1025 - Q1034)
    # Answers: C, D, A, B, C, D, A, B, C, D
    # Difficulties: F, F, I, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1025",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Foundation",
        "questionText": "Which clinical condition represents a primary, evidence-based indication for first-line electroconvulsive therapy (ECT) where rapid clinical response is life-saving?",
        "options": [
            {"id": "A", "text": "Mild seasonal affective disorder unresponsive to phototherapy"},
            {"id": "B", "text": "Borderline personality disorder with chronic non-suicidal self-injury"},
            {"id": "C", "text": "Lethal catatonia or severe depressive stupor with complete nutritional collapse"},
            {"id": "D", "text": "Obsessive-compulsive disorder without comorbid mood symptoms"}
        ],
        "correctAnswer": "C",
        "explanation": "Primary indications for immediate, first-line ECT include lethal catatonia (malignant catatonia), severe depressive stupor with dehydration/starvation, intractable treatment-resistant mania with exhaustion, and immediate, high-lethality suicidal intent. ECT is the most rapidly effective treatment for catatonia, with response rates exceeding 85%.",
        "incorrectExplanations": {
            "A": "Mild seasonal depression is treated with light therapy, SSRIs, and psychotherapy; ECT is not indicated.",
            "B": "ECT has no demonstrated efficacy for borderline personality disorder and may exacerbate cognitive/emotional distress.",
            "D": "Uncomplicated OCD does not respond to ECT; first-line treatments are high-dose SSRIs and exposure and response prevention (ERP)."
        },
        "learningObjective": "Identify acute, life-saving indications for electroconvulsive therapy in psychiatric emergencies.",
        "reference": "Royal College of Psychiatrists (2019). The ECT Handbook (4th Ed.); NICE Guideline IPG128.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1026",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Foundation",
        "questionText": "During the pre-ECT nursing assessment of a 68-year-old inpatient scheduled for treatment the following morning, which preparatory nursing action is essential for patient safety?",
        "options": [
            {"id": "A", "text": "Administering full-dose oral lorazepam 30 minutes before entering the ECT suite"},
            {"id": "B", "text": "Ensuring the patient drinks 500 mL of hypertonic electrolyte solution immediately prior to transfer"},
            {"id": "C", "text": "Encouraging a heavy carbohydrate meal 2 hours prior to anesthesia to prevent hypoglycemia"},
            {"id": "D", "text": "Verifying nil-by-mouth (fasting) status, checking for loose dentition/dentures, and ensuring baseline vitals and cognitive checks are documented"}
        ],
        "correctAnswer": "D",
        "explanation": "Pre-ECT nursing responsibilities include confirming nil-by-mouth status (minimum 6 hours for solids, 2 hours for clear liquids) to prevent pulmonary aspiration during general anesthesia, checking for loose teeth, crowns, or removable dentures to avoid dental injury/airway obstruction, taking baseline vital signs, and ensuring pre-treatment cognitive baseline testing is completed.",
        "incorrectExplanations": {
            "A": "Benzodiazepines elevate the seizure threshold and shorten or abolish therapeutic seizure duration; they are withheld or minimized prior to ECT.",
            "B": "Oral fluids within 2 hours of general anesthesia violate fasting guidelines and create high aspiration pneumonitis risk.",
            "C": "Consuming solid food 2 hours before anesthesia creates a grave danger of pulmonary aspiration under muscle relaxation."
        },
        "learningObjective": "Execute comprehensive pre-procedure nursing preparation and safety verification for patients undergoing ECT.",
        "reference": "Royal College of Psychiatrists (2019). The ECT Handbook (4th Ed.); Association of Anaesthetists Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1027",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Intermediate",
        "questionText": "During an ECT procedure, the anesthetist administers succinylcholine (suxamethonium) immediately after the induction agent (such as methohexital or propofol). What is the primary therapeutic purpose of succinylcholine in ECT?",
        "options": [
            {"id": "A", "text": "To induce profound skeletal muscle relaxation to prevent musculoskeletal trauma and fractures during the generalized cerebral seizure"},
            {"id": "B", "text": "To terminate the cerebral seizure if the epileptiform EEG activity exceeds 60 seconds"},
            {"id": "C", "text": "To induce unconsciousness and suppress peri-procedural autonomic sympathetic surges"},
            {"id": "D", "text": "To lower the electrical seizure threshold and facilitate bilateral cerebral synchronization"}
        ],
        "correctAnswer": "A",
        "explanation": "Succinylcholine (suxamethonium) is a depolarizing neuromuscular blocking agent. Its role in ECT is to produce temporary motor paralysis and profound muscle relaxation, thereby preventing bone fractures, joint dislocations, and muscle tearing while allowing the therapeutic epileptiform seizure to occur in the brain.",
        "incorrectExplanations": {
            "B": "Seizures that are prolonged (>120 seconds) are terminated with IV induction agents or benzodiazepines (e.g., midazolam/propofol), not neuromuscular blockers.",
            "C": "Induction agents (methohexital, propofol, etomidate) provide unconsciousness, not succinylcholine.",
            "D": "Succinylcholine acts at peripheral neuromuscular junctions and does not affect central cerebral seizure thresholds."
        },
        "learningObjective": "Explain the pharmacological mechanism and clinical rationale of neuromuscular blockade in ECT.",
        "reference": "The ECT Handbook (4th Ed., 2019); American Psychiatric Association Task Force on ECT.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1028",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Intermediate",
        "questionText": "A nurse observing an ECT treatment notes the application of a blood pressure cuff inflated above systolic pressure on the patient's right ankle prior to the administration of succinylcholine. What is the clinical rationale for this 'cuffed limb technique'?",
        "options": [
            {"id": "A", "text": "To prevent deep vein thrombosis in the lower extremities during the recovery phase"},
            {"id": "B", "text": "To isolate the foot from the muscle relaxant, allowing the clinical team to visually observe and time the motor seizure duration"},
            {"id": "C", "text": "To deliver localized transcutaneous electrical nerve stimulation to reduce post-ictal myalgia"},
            {"id": "D", "text": "To monitor peripheral capillary refill time and detect early autonomic instability"}
        ],
        "correctAnswer": "B",
        "explanation": "The 'cuff technique' involves inflating a tourniquet or sphygmomanometer cuff above systolic pressure on a distal limb (usually the ankle or wrist) before the IV injection of succinylcholine. This prevents the muscle relaxant from reaching that limb. When the electrical stimulus is delivered, the cuffed foot exhibits motor tonic-clonic convulsions, allowing direct visual timing of motor seizure duration alongside the EEG recording.",
        "incorrectExplanations": {
            "A": "The cuff technique is applied transiently during the procedure, not as a DVT prophylaxis device.",
            "C": "The cuff does not deliver transcutaneous stimulation; it is purely a vascular occlusion mechanism.",
            "D": "Capillary refill is assessed at the nailbeds, not by maintaining an occlusive ankle cuff."
        },
        "learningObjective": "Describe the purpose and nursing observation of the cuffed limb technique during ECT seizure monitoring.",
        "reference": "Royal College of Psychiatrists (2019). The ECT Handbook (4th Ed.); Fink, M. (2014). Electroconvulsive Therapy.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1029",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Intermediate",
        "questionText": "In the immediate post-ECT recovery area, a 70-year-old patient who has just begun breathing spontaneously becomes restless, attempts to pull at IV lines, and appears disoriented to person, place, and time. What is the priority nursing intervention?",
        "options": [
            {"id": "A", "text": "Apply four-point mechanical restraints and administer high-dose intramuscular haloperidol immediately"},
            {"id": "B", "text": "Administer 100 mL of 50% dextrose IV bolus under the assumption of acute hypoglycemia"},
            {"id": "C", "text": "Maintain airway patency, position in lateral recovery posture, provide calm repeated verbal reorientation, and monitor vital signs until post-ictal emergence delirium resolves"},
            {"id": "D", "text": "Instruct the patient firmly that their behavior is unacceptable and transfer them immediately back to the general ward"}
        ],
        "correctAnswer": "C",
        "explanation": "Post-ictal emergence delirium/confusion is common immediately after ECT, especially in older adults. Priority nursing management involves maintaining the ABCs (airway, lateral positioning, oxygenation), monitoring vitals every 5-15 minutes, maintaining a quiet, low-stimulus environment, and offering gentle, repetitive verbal reorientation. If extreme agitation threatens safety, low-dose midazolam or propofol can be considered per protocol, but reassurance and safety protection are primary.",
        "incorrectExplanations": {
            "A": "Mechanical restraints and high-dose typical antipsychotics escalate post-ictal confusion and lower seizure threshold; they are inappropriate first-line actions.",
            "B": "Hypoglycemia must be confirmed via glucometer before administering hypertonic dextrose boluses.",
            "D": "Berating a confused post-ictal patient is untherapeutic and transfers a hemodynamically/cognitively unstable patient prematurely."
        },
        "learningObjective": "Manage post-ictal confusion and emergence delirium following electroconvulsive therapy safely.",
        "reference": "The ECT Handbook (4th Ed., 2019); National Association of State Mental Health Program Directors (NASMHPD).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1030",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Intermediate",
        "questionText": "A patient undergoing an acute course of bitemporal ECT reports distress regarding memory problems. When educating the patient and family regarding cognitive adverse effects of ECT, which differentiation between anterograde and retrograde amnesia is accurate?",
        "options": [
            {"id": "A", "text": "Anterograde amnesia is permanent, whereas retrograde amnesia never occurs with ECT"},
            {"id": "B", "text": "Retrograde amnesia affects only the ability to speak foreign languages, while anterograde amnesia affects childhood memories"},
            {"id": "C", "text": "Both anterograde and retrograde amnesia are identical and always resolve within 1 hour post-treatment"},
            {"id": "D", "text": "Anterograde amnesia (difficulty retaining newly learned information) typically resolves within weeks after the ECT course ends, whereas retrograde amnesia (loss of memories for events preceding ECT) can sometimes leave persistent gaps for autobiographical events close to the treatment period"}
        ],
        "correctAnswer": "D",
        "explanation": "ECT commonly produces cognitive side effects. Anterograde amnesia (impaired ability to form and consolidate new memories) usually peaks during the treatment course and resolves within 2 to 4 weeks post-treatment. Retrograde amnesia (loss of past memories, particularly autobiographical events in the months preceding treatment) can be more variable, and some patients may experience persistent gaps in recall for events immediately preceding or during the course of ECT.",
        "incorrectExplanations": {
            "A": "Anterograde amnesia is transient and resolves; retrograde amnesia definitely occurs.",
            "B": "Retrograde amnesia affects past episodic and autobiographical memories, not linguistic capability.",
            "C": "Cognitive deficits do not fully clear within 1 hour; resolution takes weeks."
        },
        "learningObjective": "Differentiate between anterograde and retrograde memory changes associated with ECT and counsel patients accurately.",
        "reference": "Semkovska, M. & McLoughlin, D. M. (2010). Objective Cognitive Performance Associated with ECT: A Systematic Review. Biological Psychiatry; NICE Guideline IPG128.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1031",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Advanced",
        "questionText": "Following each ECT session, a 34-year-old patient experiences severe bifrontal headache accompanied by nausea. Which evidence-based pharmacological and nursing strategy should be incorporated into the pre- and post-procedure care pathway?",
        "options": [
            {"id": "A", "text": "Pre-emptive administration of IV paracetamol and an NSAID (such as ketorolac) plus an antiemetic (such as ondansetron) during recovery, accompanied by a dark, quiet recovery environment"},
            {"id": "B", "text": "Administration of high-dose oral sumatriptan 8 hours prior to anesthesia and high-flow nitrous oxide during recovery"},
            {"id": "C", "text": "Routine prophylactic administration of intramuscular prochlorperazine 25 mg 10 minutes prior to electrical stimulus delivery"},
            {"id": "D", "text": "Withholding all analgesia to prevent masking intracranial hematomas or cerebral edema"}
        ],
        "correctAnswer": "A",
        "explanation": "Post-ECT headache and nausea are very common (occurring in up to 45% of patients) due to transient cerebral vasodilation and muscle tension. Prophylactic or early post-procedure administration of IV paracetamol, NSAIDs (e.g., ketorolac or ibuprofen), and 5HT3 antagonists (such as ondansetron) provides effective relief. Environmental modification (dim lighting, minimal noise) is standard nursing care.",
        "incorrectExplanations": {
            "B": "Triptans are selective 5HT1B/1D agonists used for migraine and are not routine prophylaxis for post-ECT headache.",
            "C": "Prochlorperazine has potent antidopaminergic properties that lower seizure threshold and can trigger extrapyramidal reactions.",
            "D": "Withholding analgesia causes needless distress; post-ECT headaches are benign vascular/muscular phenomena."
        },
        "learningObjective": "Formulate nursing and pharmacological management protocols for post-ECT headache and nausea.",
        "reference": "The ECT Handbook (4th Ed., 2019); Ding, Z. & White, P. F. (2002). Anesthesia for Electroconvulsive Therapy. Anesthesia & Analgesia.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1032",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Advanced",
        "questionText": "A 62-year-old patient who achieved full remission from severe psychotic depression following an acute 12-session ECT course is commenced on maintenance ECT (m-ECT) alongside antidepressant pharmacotherapy. What is the clinical protocol and nursing role during maintenance ECT?",
        "options": [
            {"id": "A", "text": "Administering treatments three times weekly indefinitely without clinical psychometric evaluations"},
            {"id": "B", "text": "Spacing sessions progressively (e.g., weekly for 1 month, then biweekly, then monthly), continuously assessing depressive symptoms (via MADRS/HAM-D) and tracking cognitive status before each session"},
            {"id": "C", "text": "Discontinuing all oral psychotropics because concurrent medication administration during m-ECT is legally prohibited"},
            {"id": "D", "text": "Transitioning the patient to self-administered home transcutaneous cranial stimulation devices"}
        ],
        "correctAnswer": "B",
        "explanation": "Maintenance ECT (m-ECT) is used to prevent relapse in patients with severe, recurring refractory illness who respond to acute ECT. Protocols involve gradual tapering of treatment frequency: typically once weekly for 4 weeks, then fortnightly for 1-2 months, then extending to monthly treatments. At every visit, the nurse evaluates depressive symptoms using standardized scales (e.g., MADRS) and performs formal cognitive screening.",
        "incorrectExplanations": {
            "A": "Three times weekly is the frequency for acute induction courses, not maintenance therapy.",
            "C": "Concurrent antidepressant pharmacotherapy (e.g., lithium + nortriptyline) is standard during m-ECT to enhance relapse prevention.",
            "D": "ECT requires general anesthesia in a licensed suite; home self-administration is impossible and illegal."
        },
        "learningObjective": "Manage maintenance electroconvulsive therapy (m-ECT) scheduling, cognitive monitoring, and symptom surveillance.",
        "reference": "Kellner, C. H. et al. (2016). Continuation Electroconvulsive Therapy vs Pharmacotherapy for Relapse Prevention in Major Depression (CORE study). American Journal of Psychiatry; NICE IPG128.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1033",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Advanced",
        "questionText": "Which physiological finding or medical comorbidity poses the greatest relative contraindication and anesthetic risk during ECT, necessitating intensive pre-procedural stabilization?",
        "options": [
            {"id": "A", "text": "Mild stable asthma managed with an inhaled salbutamol PRN inhaler"},
            {"id": "B", "text": "Controlled primary hypothyroidism on a stable dose of levothyroxine"},
            {"id": "C", "text": "Significantly raised intracranial pressure (e.g., from a space-occupying intracranial mass) or an unstable cerebral aneurysm"},
            {"id": "D", "text": "Osteoarthritis of the knees without mobility restrictions"}
        ],
        "correctAnswer": "C",
        "explanation": "While ECT has no absolute medical contraindications, conditions associated with substantially elevated risk include space-occupying intracranial lesions with mass effect and significantly raised intracranial pressure (risk of cerebral herniation during transient post-stimulus intracranial pressure surges), unstable cerebral aneurysms (risk of rupture during initial sympathetic hypertensive surge), and recent myocardial infarction.",
        "incorrectExplanations": {
            "A": "Mild stable asthma requires standard pre-anesthetic airway management and is not a high-risk contraindication.",
            "B": "Well-controlled hypothyroidism requires no special alteration of ECT protocols.",
            "D": "Osteoarthritis is managed with full muscle relaxation and does not contraindicate ECT."
        },
        "learningObjective": "Identify high-risk medical comorbidities and relative contraindications requiring multidisciplinary risk mitigation prior to ECT.",
        "reference": "American Psychiatric Association Task Force on ECT; Royal College of Anaesthetists Guidelines for ECT.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1034",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Electroconvulsive therapy (ECT)",
        "difficulty": "Expert",
        "questionText": "Under mental health legislation (such as Section 58A of the Mental Health Act 1983 in England & Wales), what is the statutory requirement regarding the administration of ECT to a detained adult patient who possesses mental capacity and explicitly refuses treatment?",
        "options": [
            {"id": "A", "text": "The patient's refusal can be overridden by any approved mental health professional if two relatives give written proxy consent"},
            {"id": "B", "text": "The responsible clinician can administer ECT immediately under routine common law doctrine of necessity"},
            {"id": "C", "text": "A hospital managers' panel can authorize ECT over the patient's competent refusal if the ward manager agrees"},
            {"id": "D", "text": "ECT cannot be administered to a capacitous patient who refuses, unless it is immediately necessary to save life or prevent serious deterioration under emergency statutory provisions (e.g., Section 62)"}
        ],
        "correctAnswer": "D",
        "explanation": "Under Section 58A of the Mental Health Act (England and Wales), a patient who has capacity to consent to ECT and refuses cannot be given ECT, even if detained, except in strictly defined emergency situations under Section 62 (treatment immediately necessary to save life or prevent serious and irreversible deterioration). For capacitous non-refusing patients, valid informed consent is required; for incapacitous patients, a Second Opinion Appointed Doctor (SOAD) must certify treatment.",
        "incorrectExplanations": {
            "A": "Relatives cannot override a capacitous adult's competent refusal to consent to medical or psychiatric treatment.",
            "B": "Common law necessity cannot override specific statutory mental health protections for capacitous patients refusing ECT.",
            "C": "Hospital managers have power to discharge patients from detention, but cannot authorize medical treatment over a competent refusal."
        },
        "learningObjective": "Analyze legal frameworks, capacity assessments, and statutory safeguards governing consent and refusal of ECT.",
        "reference": "Mental Health Act 1983 (amended 2007) Code of Practice (DHSC, 2015); Section 58A & Section 62 guidance.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 3: Clozapine for treatment-resistant schizophrenia (Q1035 - Q1044)
    # Answers: A, B, C, D, A, B, C, D, A, B
    # Difficulties: F, F, F, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1035",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Foundation",
        "questionText": "A 28-year-old patient with persistent persecutory delusions and auditory hallucinations has shown no significant response to olanzapine 20 mg/day for 10 weeks, followed by risperidone 6 mg/day for 8 weeks, with confirmed adherence. Under national clinical guidelines (e.g., NICE CG178), what is the appropriate next pharmacological step?",
        "options": [
            {"id": "A", "text": "Offer clozapine monotherapy as the patient meets the criteria for treatment-resistant schizophrenia"},
            {"id": "B", "text": "Prescribe high-dose haloperidol combined with flupentixol decanoate depot injections"},
            {"id": "C", "text": "Combine risperidone, olanzapine, and quetiapine in triple high-dose antipsychotic therapy"},
            {"id": "D", "text": "Discontinue all antipsychotics and manage the patient purely with supportive milieu therapy"}
        ],
        "correctAnswer": "A",
        "explanation": "NICE Guideline CG178 states that clozapine should be offered to people with schizophrenia whose illness has not responded adequately despite the sequential use of adequate doses of at least two different antipsychotics (at least one of which should be a non-clozapine second-generation atypical antipsychotic) each prescribed for an adequate duration (at least 6-8 weeks) with verified adherence.",
        "incorrectExplanations": {
            "B": "Adding high-dose first-generation depots increases extrapyramidal symptoms and mortality without superior efficacy over clozapine.",
            "C": "Antipsychotic polypharmacy before trying clozapine is contrary to evidence-based guidelines and increases adverse effects.",
            "D": "Discontinuing antipsychotics entirely in active refractory psychosis leads to rapid relapse, behavioral deterioration, and risk of harm."
        },
        "learningObjective": "Identify prescribing criteria and clinical indications for initiating clozapine in treatment-resistant schizophrenia.",
        "reference": "NICE Guideline CG178: Psychosis and schizophrenia in adults: prevention and management (2014, updated); Maudsley Prescribing Guidelines (14th Ed).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1036",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Foundation",
        "questionText": "What is the mandatory Full Blood Count (FBC) / Absolute Neutrophil Count (ANC) monitoring schedule mandated by regulatory clozapine patient monitoring services during maintenance therapy?",
        "options": [
            {"id": "A", "text": "Daily for the first month, then weekly indefinitely"},
            {"id": "B", "text": "Weekly for the first 18 weeks, then fortnightly (every 2 weeks) from week 19 to 52, and monthly (every 4 weeks) thereafter"},
            {"id": "C", "text": "Monthly for the first 6 months, followed by once-yearly blood draws thereafter"},
            {"id": "D", "text": "Every 6 weeks during the first year, then only when clinical symptoms of fever develop"}
        ],
        "correctAnswer": "B",
        "explanation": "Due to the risk of life-threatening agranulocytosis (occurring in ~0.8% of patients, peaking in the first 18 weeks), clozapine monitoring services enforce strict mandatory blood testing schedules: weekly for the first 18 weeks of treatment; every 2 weeks from week 19 through week 52 (the remainder of the first year); and every 4 weeks (monthly) thereafter for as long as the patient remains on clozapine.",
        "incorrectExplanations": {
            "A": "Daily monitoring is not required and causes unacceptable phlebotomy burden.",
            "C": "Monthly testing during the first 6 months is dangerous; the highest risk of fatal agranulocytosis is within the first 18 weeks.",
            "D": "Symptom-triggered monitoring alone is unsafe because neutrophil counts drop precipitously before clinical infection manifests."
        },
        "learningObjective": "Recall the statutory haematological monitoring timeline for clozapine therapy.",
        "reference": "Taylor, D. et al. The Maudsley Prescribing Guidelines in Psychiatry (14th Ed., 2021); Clozaril Patient Monitoring Service (CPMS) Protocols.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1037",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Foundation",
        "questionText": "A mental health nurse reviews the weekly routine blood test results for a patient on clozapine (non-BEN status). The laboratory reports: White Blood Cell count (WBC) 2.6 x 10^9/L and Absolute Neutrophil Count (ANC) 1.2 x 10^9/L. According to standard clozapine monitoring guidelines, which action is mandatory?",
        "options": [
            {"id": "A", "text": "Continue clozapine at current dose and retest blood count in 2 weeks"},
            {"id": "B", "text": "Increase clozapine dose by 50 mg to stimulate bone marrow progenitor proliferation"},
            {"id": "C", "text": "Immediately discontinue clozapine, alert the psychiatrist and hematologist, repeat FBC within 24 hours, monitor closely for infection, and never re-challenge with clozapine"},
            {"id": "D", "text": "Switch to intramuscular depot clozapine to bypass gastrointestinal absorption issues"}
        ],
        "correctAnswer": "C",
        "explanation": "These values fall in the 'RED' alert category (WBC < 3.0 x 10^9/L or ANC < 1.5 x 10^9/L in general patients). A RED alert requires immediate cessation of clozapine to prevent progression to fulminant agranulocytosis. The nurse must notify the medical team, isolate the patient from infection sources, repeat FBC within 24 hours, consult hematology, and record a permanent contraindication—patients with a true red result must never be rechallenged.",
        "incorrectExplanations": {
            "A": "Continuing clozapine with an ANC of 1.2 x 10^9/L risks fatal neutropenic sepsis.",
            "B": "Increasing clozapine accelerates cytotoxic bone marrow destruction.",
            "D": "No depot formulation of clozapine exists, and systemic exposure would remain toxic."
        },
        "learningObjective": "Interpret clozapine haematological monitoring alerts and execute the mandatory RED protocol.",
        "reference": "Clozaril Patient Monitoring Service (CPMS) Safety Protocols; British National Formulary (BNF).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1038",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Intermediate",
        "questionText": "A 31-year-old patient of Afro-Caribbean descent with a documented history of Benign Ethnic Neutropenia (BEN) is being initiated on clozapine. How do the haematological monitoring thresholds differ for patients registered with BEN?",
        "options": [
            {"id": "A", "text": "Patients with BEN require blood draws only once every 3 months during the first year"},
            {"id": "B", "text": "The ANC thresholds are set substantially higher (Green ANC ≥ 3.0 x 10^9/L) due to hyper-reactive marrow"},
            {"id": "C", "text": "Platelet counts replace white blood cell counts as the primary monitoring parameter"},
            {"id": "D", "text": "Lower baseline and alert thresholds apply: Green is ANC ≥ 1.5 x 10^9/L, Amber is ANC 1.0–1.4 x 10^9/L, and Red is ANC < 1.0 x 10^9/L"}
        ],
        "correctAnswer": "D",
        "explanation": "Benign Ethnic Neutropenia (BEN) is a physiological condition seen in individuals of African and Middle Eastern descent characterized by lower baseline neutrophil counts without increased infection risk. Under clozapine monitoring guidelines, specific BEN criteria apply: 'Green' threshold is an ANC ≥ 1.5 x 10^9/L (compared to 2.0 in the general population); 'Amber' is 1.0 to 1.4 x 10^9/L; and 'Red' alert is ANC < 1.0 x 10^9/L.",
        "incorrectExplanations": {
            "A": "Frequency of blood testing is identical (weekly for 18 weeks, then fortnightly, then monthly); only the threshold numbers differ.",
            "B": "Thresholds are lower, not higher, reflecting physiological baseline variations.",
            "C": "Absolute Neutrophil Count remains the essential monitoring metric."
        },
        "learningObjective": "Apply Benign Ethnic Neutropenia (BEN) monitoring criteria to clozapine safety protocols.",
        "reference": "Maudsley Prescribing Guidelines (14th Ed.); UK Clozapine Central Monitoring Service (ZKLS/CPMS).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1039",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Intermediate",
        "questionText": "During week 3 of clozapine titration, a 24-year-old inpatient develops a resting heart rate of 118 bpm, a low-grade fever (38.1°C), shortness of breath on exertion, and non-specific chest discomfort. What potentially fatal clozapine-induced complication should the psychiatric nurse immediately suspect, and what diagnostic investigations must be requested urgently?",
        "options": [
            {"id": "A", "text": "Acute myocarditis; urgent troponin (I or T), C-reactive protein (CRP), 12-lead ECG, and echocardiogram"},
            {"id": "B", "text": "Clozapine-induced agranulocytosis; urgent bone marrow aspirate and platelet transfusion"},
            {"id": "C", "text": "Central anticholinergic syndrome; urgent physostigmine challenge test and EEG"},
            {"id": "D", "text": "Renal tubular acidosis; urgent 24-hour urine collection for heavy metals"}
        ],
        "correctAnswer": "A",
        "explanation": "Clozapine-induced myocarditis most commonly presents during the first 2 months of titration (peak incidence between days 14 and 28). Symptoms include unexplained persistent resting tachycardia, fever, dyspnea, chest discomfort, palpitations, or dry cough. Prompt screening with cardiac biomarkers (Troponin I/T), inflammatory markers (CRP), ECG (ST-T changes, sinus tachycardia), and echocardiography is required. If myocarditis is confirmed, clozapine must be stopped immediately.",
        "incorrectExplanations": {
            "B": "Agranulocytosis presents with infectious signs (sore throat, septic fever), not isolated cardiac dysfunction and chest discomfort.",
            "C": "Central anticholinergic syndrome manifests with delirium, mydriasis, dry flushed skin, and urinary retention.",
            "D": "Renal tubular acidosis does not produce acute fever, resting tachycardia, and chest discomfort."
        },
        "learningObjective": "Recognize early clinical signs and diagnostic workup for clozapine-induced myocarditis.",
        "reference": "Ronaldson, K. J. et al. (2011). Clinical Presentation and Management of Clozapine-Induced Myocarditis. Australian & New Zealand Journal of Psychiatry; MHRA Drug Safety Update.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1040",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Intermediate",
        "questionText": "A nurse reviews ward data showing that mortality from clozapine-induced gastrointestinal hypomotility (CIGH) and paralytic ileus equals or exceeds mortality from clozapine-induced agranulocytosis. What routine preventive nursing assessment and intervention plan must be implemented for every patient on clozapine?",
        "options": [
            {"id": "A", "text": "Strict fluid restriction to 800 mL/day and administration of loperamide with every meal"},
            {"id": "B", "text": "Daily monitoring of bowel habits using a validated stool chart (e.g., Bristol Stool Form Scale), ensuring adequate hydration, high-fiber intake, and early proactive prescription of stimulant and osmotic laxatives (e.g., macrogol, senna) while avoiding bulk-forming laxatives"},
            {"id": "C", "text": "Performing routine weekly barium enema examinations during the first 6 months of therapy"},
            {"id": "D", "text": "Encouraging high-dose calcium carbonate antacids after every meal"}
        ],
        "correctAnswer": "B",
        "explanation": "Clozapine possesses potent antimuscarinic and antiserotonergic actions that profoundly slow gut motility, leading to severe constipation, fecal impaction, bowel obstruction, toxic megacolon, bowel ischemia, and fatal perforation. Nurses must track bowel frequency daily on a Bristol Stool Scale, encourage fluids/dietary adjustments, and ensure proactive co-prescription of stimulant/osmotic laxatives. Bulk-forming laxatives (e.g., ispaghula husk) are contraindicated if obstruction is developing.",
        "incorrectExplanations": {
            "A": "Restricting fluids and giving loperamide (an antimotility agent) would precipitate fatal paralytic ileus.",
            "C": "Weekly barium enemas are invasive, unnecessary, and barium can concrete in a hypomotile colon worsening obstruction.",
            "D": "Calcium carbonate antacids can cause severe constipation, aggravating gut hypomotility."
        },
        "learningObjective": "Implement proactive nursing prevention and monitoring protocols for clozapine-induced gastrointestinal hypomotility.",
        "reference": "Every-Palmer, S. et al. (2017). Clozapine-Induced Gastrointestinal Hypomotility: A Serious and Under-Recognized Adverse Effect. CNS Drugs; MHRA Drug Safety Alert.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1041",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Advanced",
        "questionText": "A 36-year-old patient on clozapine 400 mg daily reports waking every morning with soaked pillows and clothes due to severe nocturnal hypersalivation (sialorrhoea), causing social embarrassment and choking episodes. What pharmacological mechanism explains this symptom, and which evidence-based intervention can the nurse recommend?",
        "options": [
            {"id": "A", "text": "Histaminergic H1 antagonism; managed by adding diphenhydramine at bedtime"},
            {"id": "B", "text": "Alpha-2 adrenergic stimulation; managed by discontinuing all oral fluids after 12:00 PM"},
            {"id": "C", "text": "Agonism at muscarinic M4 receptors combined with impaired swallowing reflex during sleep; managed with sublingual 1% atropine eye drops (1-2 drops under tongue at bedtime) or hyoscine hydrobromide"},
            {"id": "D", "text": "Direct destruction of the salivary parotid glands; managed by surgical parotid duct ligation"}
        ],
        "correctAnswer": "C",
        "explanation": "Clozapine-induced sialorrhoea occurs in up to 30-50% of patients. Paradoxically, despite clozapine being an anticholinergic drug, it acts as a potent agonist at muscarinic M4 receptors and has alpha-2 adrenoceptor antagonist properties, while central sedation impairs the nocturnal swallowing reflex. Aspiration pneumonia is a major risk. Sublingual anticholinergics (such as 1-2 drops of 1% atropine ophthalmic solution sublingually at night, or oral hyoscine) are widely recommended.",
        "incorrectExplanations": {
            "A": "H1 antagonism causes sedation and weight gain, not hypersalivation.",
            "B": "Dehydration by withholding fluids is medically hazardous and ineffective for receptor-mediated sialorrhoea.",
            "D": "Salivary glands are not destroyed; surgical duct ligation is an extreme and unnecessary measure."
        },
        "learningObjective": "Formulate management plans for clozapine-induced sialorrhoea to improve quality of life and prevent aspiration.",
        "reference": "Bird, A. M. et al. (2011). Pharmacological Management of Clozapine-Induced Sialorrhea. Annals of Pharmacotherapy; Maudsley Prescribing Guidelines (14th Ed).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1042",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Advanced",
        "questionText": "A patient receiving clozapine 650 mg/day develops brief, sudden involuntary muscle jerks of the upper extremities in the morning, dropping their coffee cup. The nurse recognizes this as myoclonic jerking. Why is this finding clinically significant, and what is the appropriate management strategy?",
        "options": [
            {"id": "A", "text": "Myoclonic jerks are harmless extrapyramidal symptoms that require no clinical changes"},
            {"id": "B", "text": "Myoclonus indicates severe conversion disorder and requires immediate behavioral therapy"},
            {"id": "C", "text": "Myoclonus is an allergic reaction requiring urgent epinephrine and corticosteroid administration"},
            {"id": "D", "text": "Myoclonus is a dose-dependent prodromal warning sign of impending generalized tonic-clonic seizures; the clozapine dose should be reduced and an antiepileptic (such as sodium valproate) considered, while avoiding carbamazepine"}
        ],
        "correctAnswer": "D",
        "explanation": "Clozapine lowers the seizure threshold in a dose-dependent manner (seizure incidence exceeds 5% at doses above 600 mg/day or with rapid dose escalation). Myoclonic jerks are an early warning sign (prodrome) of impending generalized tonic-clonic seizures. The clozapine dose should be reduced, serum levels checked, and prophylactic anticonvulsant therapy (e.g., sodium valproate or lamotrigine) initiated. Carbamazepine is strictly contraindicated because it also causes bone marrow suppression/agranulocytosis.",
        "incorrectExplanations": {
            "A": "Myoclonic jerks are not benign EPS; they herald generalized tonic-clonic seizures.",
            "B": "Attributing physiological myoclonus to conversion disorder is dangerous diagnostic overshadowing.",
            "C": "Myoclonus is a central neuro-epileptogenic effect, not an IgE-mediated anaphylactic reaction."
        },
        "learningObjective": "Identify seizure risk factors, prodromal signs (myoclonus), and antiepileptic co-prescription rules in clozapine therapy.",
        "reference": "Wong, J. & Delva, N. (2007). Clozapine-Induced Seizures and EEG Changes. Journal of Psychiatry and Neuroscience; Maudsley Prescribing Guidelines (14th Ed).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1043",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Advanced",
        "questionText": "An outpatient taking clozapine 300 mg daily misplaced their medication and missed their doses for 5 consecutive days (over 48 hours). When they present to the community mental health clinic requesting a renewal, what mandatory prescribing and titration protocol must be followed?",
        "options": [
            {"id": "A", "text": "Resume clozapine immediately at the full 300 mg daily dose to avoid acute psychotic decompensation"},
            {"id": "B", "text": "Administer a double dose (600 mg) on the first day to compensate for missing days"},
            {"id": "C", "text": "The patient must be restarted at 12.5 mg once or twice daily and slowly re-titrated to their target dose due to loss of cardiovascular tolerance and risk of profound hypotension, syncope, and cardiac arrest"},
            {"id": "D", "text": "Switch permanently to oral fluphenazine because missing doses invalidates clozapine candidacy"}
        ],
        "correctAnswer": "C",
        "explanation": "Tolerance to clozapine's potent alpha-1 adrenergic blocking and histaminergic effects is lost rapidly after missing doses for 48 hours or more. Resuming at the previous maintenance dose carries an acute risk of severe orthostatic hypotension, syncope, respiratory depression, seizures, and cardiovascular collapse. The patient must restart from 12.5 mg (once or twice on day 1) and undergo gradual dose titration as if beginning initial therapy.",
        "incorrectExplanations": {
            "A": "Resuming at full 300 mg dose after >48 hours without titration can cause fatal hypotension and cardiac arrest.",
            "B": "Doubling the dose is lethally toxic.",
            "D": "Missing doses does not disqualify a patient from clozapine; proper re-titration is standard protocol."
        },
        "learningObjective": "Explain and execute the clinical protocol for clozapine re-titration following treatment interruption greater than 48 hours.",
        "reference": "Taylor, D. et al. The Maudsley Prescribing Guidelines in Psychiatry (14th Ed., 2021); BNF Clozapine Monograph.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1044",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Clozapine for treatment-resistant schizophrenia",
        "difficulty": "Expert",
        "questionText": "A 42-year-old inpatient with schizophrenia who smoked 25 cigarettes per day has been stabilized on clozapine 400 mg daily for 2 years with a steady therapeutic plasma level of 450 mcg/L. Following the implementation of a strict hospital smoke-free policy, the patient abruptly stops smoking all tobacco. What physiological effect does this have on clozapine metabolism, and what should the psychiatric team do?",
        "options": [
            {"id": "A", "text": "Smoking cessation has no impact on clozapine because nicotine is eliminated purely through renal filtration"},
            {"id": "B", "text": "Hydrocarbons in tobacco smoke induce hepatic CYP1A2; sudden cessation removes this induction, causing clozapine serum concentrations to rise by 50-100%, necessitating proactive dose reduction and close monitoring for toxicity"},
            {"id": "C", "text": "Clozapine clearance will drastically accelerate, dropping plasma levels below the therapeutic window and triggering acute psychosis"},
            {"id": "D", "text": "The patient will develop immediate agranulocytosis because tobacco smoke protects white blood cell precursors"}
        ],
        "correctAnswer": "B",
        "explanation": "Polycyclic aromatic hydrocarbons in tobacco smoke (not nicotine itself) are potent inducers of the cytochrome P450 enzyme CYP1A2, which is the primary metabolic pathway for clozapine. When a heavy smoker abruptly ceases smoking, CYP1A2 enzyme activity declines over 1-2 weeks, causing clozapine clearance to fall and serum levels to surge by 50% to over 100%. Without a dose reduction (often by 30-50%), the patient can experience severe clozapine toxicity (sedation, seizures, ataxia, hypotension).",
        "incorrectExplanations": {
            "A": "Hydrocarbons in smoke profoundly alter hepatic drug metabolism; nicotine replacement therapy does not prevent this effect.",
            "C": "Clearance decreases rather than accelerates, leading to toxic elevation of drug levels.",
            "D": "Tobacco smoke does not protect against agranulocytosis; bone marrow toxicity is independent of smoking status."
        },
        "learningObjective": "Anticipate and manage the pharmacokinetics of CYP1A2 induction and tobacco smoking cessation on clozapine plasma levels.",
        "reference": "de Leon, J. et al. (2020). The Effects of Smoking on Clozapine and Olanzapine Kinetics. Journal of Clinical Psychopharmacology; Maudsley Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 4: Complex dual diagnosis (Q1045 - Q1054)
    # Answers: C, D, A, B, C, D, A, B, C, D
    # Difficulties: F, F, I, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1045",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Foundation",
        "questionText": "Which service delivery model for individuals with severe mental illness and co-occurring substance use disorder (dual diagnosis) is supported by the strongest clinical evidence for reducing hospital admissions and improving recovery outcomes?",
        "options": [
            {"id": "A", "text": "Sequential model: treating the substance use disorder in a residential rehab facility to completion before addressing psychiatric symptoms"},
            {"id": "B", "text": "Parallel model: requiring the patient to attend independent mental health and addiction clinics concurrently with separate care coordinators"},
            {"id": "C", "text": "Integrated Dual Diagnosis Treatment (IDDT): a single multidisciplinary team providing concurrent, coordinated treatment for both mental illness and substance use"},
            {"id": "D", "text": "Exclusionary model: denying psychiatric admission until the patient produces 6 consecutive months of drug-free urine screens"}
        ],
        "correctAnswer": "C",
        "explanation": "The Integrated Dual Diagnosis Treatment (IDDT) model is recommended by NICE, SAMHSA, and WHO. In IDDT, both psychiatric illness and substance use disorders are treated simultaneously by the same clinical team in a coordinated, unified manner using harm reduction, motivational interviewing, stage-matched interventions, and continuous engagement, eliminating the fragmentation of parallel or sequential systems.",
        "incorrectExplanations": {
            "A": "Sequential treatment fails because untreated mental illness often triggers substance relapse, and substance abuse impairs psychiatric stabilization.",
            "B": "Parallel treatment creates disjointed care, contradictory treatment advice, and high dropout rates.",
            "D": "Exclusionary policies are unethical, increase mortality, and create severe barriers to care for vulnerable populations."
        },
        "learningObjective": "Differentiate integrated dual diagnosis care from fragmented sequential and parallel treatment models.",
        "reference": "Drake, R. E. et al. (2001). Implementing Dual Diagnosis Services for Clients with Severe Mental Illness. Psychiatric Services; NICE Guideline CG120.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1046",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Foundation",
        "questionText": "A 30-year-old patient with bipolar affective disorder and cannabis dependence tells the dual diagnosis nurse: 'Smoking weed helps my racing thoughts. I don't see any reason to stop, and doctors just don't understand.' In Prochaska and DiClemente's Stages of Change model, which stage is the patient exhibiting, and what is the nurse's primary goal?",
        "options": [
            {"id": "A", "text": "Action stage; enforce immediate attendance at 12-step Narcotics Anonymous meetings"},
            {"id": "B", "text": "Preparation stage; design a concrete 30-day detoxification schedule"},
            {"id": "C", "text": "Maintenance stage; teach relapse prevention techniques and craving coping skills"},
            {"id": "D", "text": "Precontemplation stage; build rapport, raise non-judgmental awareness of potential harms, and explore the patient's personal perspectives without confrontation"}
        ],
        "correctAnswer": "D",
        "explanation": "In the Precontemplation stage of the Transtheoretical Model, the individual does not acknowledge a problem or intend to change behavior in the foreseeable future. The nurse's objective is not to force change or confront denial, but to establish therapeutic rapport, validate their lived experience, use reflective listening, and gently explore discrepancy between their substance use and broader life goals.",
        "incorrectExplanations": {
            "A": "The patient is not in the Action stage; demanding 12-step attendance at this point increases resistance and ruptures the therapeutic alliance.",
            "B": "Preparation involves actively intending to take action and planning steps, which this patient clearly rejects.",
            "C": "Maintenance occurs when sustained change has been maintained for >6 months."
        },
        "learningObjective": "Identify stages of change and apply stage-matched motivational interviewing strategies in dual diagnosis care.",
        "reference": "Prochaska, J. O. & DiClemente, C. C. (1983). Stages and Processes of Self-Change. Journal of Consulting and Clinical Psychology; SAMHSA TIP 35.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1047",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Intermediate",
        "questionText": "A 45-year-old patient with chronic severe alcohol dependence and major depression is admitted to an acute psychiatric unit. Within 12 hours of their last drink, the patient displays gross tremor, diaphoresis, nausea, anxiety, and a heart rate of 112 bpm. Why must parenteral thiamine (e.g., Pabrinex) be administered BEFORE any intravenous glucose infusion?",
        "options": [
            {"id": "A", "text": "Glucose metabolism rapidly consumes remaining thiamine pyrophosphate stores, precipitating acute Wernicke's encephalopathy and irreversible Korsakoff's psychosis"},
            {"id": "B", "text": "Thiamine binds directly to glucose to prevent acute hyperosmolar non-ketotic hyperglycemic coma"},
            {"id": "C", "text": "Glucose infusion triggers severe anaphylaxis unless premedicated with high-potency B-complex vitamins"},
            {"id": "D", "text": "Thiamine acts as an osmotic diuretic that accelerates the renal excretion of blood alcohol"}
        ],
        "correctAnswer": "A",
        "explanation": "Thiamine (vitamin B1) is a critical cofactor for glucose metabolism enzymes (pyruvate dehydrogenase, alpha-ketoglutarate dehydrogenase, and transketolase). Administering a glucose load to a thiamine-deficient patient rapidly exhausts residual intracellular thiamine stores, precipitating acute Wernicke's encephalopathy (triad of confusion, ataxia, and ophthalmoplegia) or progression to permanent Korsakoff's amnestic syndrome. Parenteral thiamine must always precede glucose.",
        "incorrectExplanations": {
            "B": "Thiamine does not bind to glucose to alter hyperosmolarity.",
            "C": "Glucose does not cause anaphylaxis.",
            "D": "Thiamine has no osmotic diuretic effect and does not metabolize circulating ethanol."
        },
        "learningObjective": "Explain the biochemical rationale for administering parenteral thiamine prior to glucose in severe alcohol withdrawal.",
        "reference": "NICE Guideline CG115: Alcohol-use disorders: diagnosis and management (2011); Royal College of Physicians Alcohol Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1048",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Intermediate",
        "questionText": "A 23-year-old male with a 4-year history of daily high-potency synthetic cannabinoid ('Spice') use presents with acute agitation, paranoia, and auditory hallucinations. How do synthetic cannabinoid receptor agonists differ clinically from natural cannabis (delta-9-THC), and what acute psychiatric and physical risks must the nurse anticipate?",
        "options": [
            {"id": "A", "text": "Synthetic cannabinoids are partial CB1 agonists that produce milder, predominantly sedating effects compared to natural herbal cannabis"},
            {"id": "B", "text": "Synthetic cannabinoids are full, high-potency agonists at CB1 and CB2 receptors, lacking protective cannabidiol (CBD), and can trigger severe agitated delirium, seizures, acute kidney injury, and refractory psychosis"},
            {"id": "C", "text": "Synthetic cannabinoids contain zero psychoactive compounds and only cause mild contact dermatitis"},
            {"id": "D", "text": "Synthetic cannabinoids are completely safe because they are regulated pharmaceutical compounds"}
        ],
        "correctAnswer": "B",
        "explanation": "Synthetic cannabinoid receptor agonists (SCRAs) are full agonists at cannabinoid CB1 and CB2 receptors with binding affinities up to hundreds of times greater than delta-9-THC. Crucially, they lack cannabidiol (CBD), which normally buffers psychotic effects. Clinical presentations are frequently unpredictable and life-threatening, including extreme agitation, delirium, catatonia, violent outbursts, seizures, arrhythmias, rhabdomyolysis, acute kidney injury, and treatment-resistant psychosis.",
        "incorrectExplanations": {
            "A": "Natural THC is a partial agonist; synthetic cannabinoids are full high-affinity agonists and far more potent and dangerous.",
            "C": "Synthetic cannabinoids are intensely psychoactive synthetic molecules sprayed onto inert plant matter.",
            "D": "They are illicit, unregulated, toxic research chemicals with high morbidity and mortality."
        },
        "learningObjective": "Recognize the neuropharmacological differences and life-threatening clinical risks of synthetic cannabinoids.",
        "reference": "Every-Palmer, S. (2011). Synthetic Cannabinoid Receptor Agonists and Psychosis. Addiction; European Monitoring Centre for Drugs and Drug Addiction (EMCDDA).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1049",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Intermediate",
        "questionText": "When evaluating an acute psychotic presentation in an emergency department, which clinical features most strongly suggest methamphetamine-induced psychosis rather than an exacerbation of primary schizophrenia?",
        "options": [
            {"id": "A", "text": "Profound blunted affect, poverty of speech, and insidious onset over two years"},
            {"id": "B", "text": "Prominent thought insertion, somatic passivity phenomena, and a lack of sympathetic nervous system arousal"},
            {"id": "C", "text": "Prominent tactile hallucinations (e.g., formication or 'meth bugs'), intense persecutory paranoia, marked psychomotor agitation, hypervigilance, pupillary dilation, and tachycardia"},
            {"id": "D", "text": "Severe catatonic waxy flexibility and prominent thought block without motor hyperactivity"}
        ],
        "correctAnswer": "C",
        "explanation": "Methamphetamine causes massive presynaptic dopamine and norepinephrine release. Methamphetamine-induced psychosis is characterized by abrupt onset, intense persecutory paranoia, extreme agitation, tactile hallucinations (e.g., formication: sensation of bugs crawling under skin, leading to skin picking/excoriation), visual hallucinations, and overt sympathetic arousal (mydriasis, tachycardia, hypertension, diaphoresis). Primary schizophrenia typically features more prominent negative symptoms and Schneiderian first-rank symptoms without autonomic overdrive.",
        "incorrectExplanations": {
            "A": "Blunted affect and poverty of speech are classic negative symptoms of primary chronic schizophrenia.",
            "B": "Thought insertion and passivity without sympathetic arousal are classic core symptoms of primary schizophrenia.",
            "D": "Waxy flexibility and thought block suggest catatonia rather than acute amphetamine toxidrome."
        },
        "learningObjective": "Differentiate acute stimulant-induced psychosis from acute exacerbations of primary schizophrenia.",
        "reference": "Grant, K. M. et al. (2012). Methamphetamine-Associated Psychosis. Journal of Neuroimmune Pharmacology; DSM-5-TR.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1050",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Intermediate",
        "questionText": "A 38-year-old patient with severe opioid use disorder and recurrent major depressive disorder is being initiated on buprenorphine/naloxone (Suboxone) substitution therapy. What essential nursing assessment must be conducted immediately prior to administering the first sublingual buprenorphine dose?",
        "options": [
            {"id": "A", "text": "Verify that the patient has consumed a full opioid dose within the past 2 hours to avoid craving"},
            {"id": "B", "text": "Administer intramuscular naloxone bolus to confirm absence of physical dependence"},
            {"id": "C", "text": "Perform a 24-hour continuous ECG Holter monitor to check for asymptomatic ST elevations"},
            {"id": "D", "text": "Assess the patient using the Clinical Opiate Withdrawal Scale (COWS) to confirm that they are in moderate opioid withdrawal (score ≥ 12-13) before administration"}
        ],
        "correctAnswer": "D",
        "explanation": "Buprenorphine is a high-affinity partial mu-opioid receptor agonist. If administered to a patient who has active full-agonist opioids (e.g., heroin, methadone, oxycodone) bound to their mu receptors, buprenorphine rapidly displaces the full agonists due to its higher affinity, but triggers lower intrinsic receptor activity, precipitating severe and excruciating 'precipitated withdrawal'. The nurse must confirm moderate withdrawal (COWS score ≥ 12) before induction.",
        "incorrectExplanations": {
            "A": "Giving buprenorphine 2 hours after full agonists causes immediate severe precipitated withdrawal.",
            "B": "Injecting naloxone would cause instantaneous precipitated withdrawal and is not used as a test.",
            "C": "While methadone prolongs QTc, buprenorphine has a favorable cardiac safety profile; 24-hour Holter is unnecessary."
        },
        "learningObjective": "Apply the Clinical Opiate Withdrawal Scale (COWS) to prevent precipitated withdrawal during buprenorphine induction.",
        "reference": "World Health Organization (WHO) Guidelines for the Psychosocially Assisted Pharmacotherapy of Opioid Dependence; Clinical Opiate Withdrawal Scale (COWS).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1051",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Advanced",
        "questionText": "A 50-year-old patient with schizophrenia and opioid dependence is maintained on methadone 80 mg daily. The psychiatric team intends to prescribe an antipsychotic for worsening auditory hallucinations. Which electrocardiographic risk must the mental health nurse highlight to the team?",
        "options": [
            {"id": "A", "text": "Methadone can cause dose-dependent QTc interval prolongation; combining it with antipsychotics known to prolong QTc (e.g., amisulpride, haloperidol, or quetiapine) significantly increases the risk of Torsades de Pointes and sudden cardiac death"},
            {"id": "B", "text": "Methadone causes profound shortening of the PR interval leading to Wolff-Parkinson-White bypass tract excitation"},
            {"id": "C", "text": "Methadone completely blocks cardiac muscarinic receptors causing persistent supraventricular reentry tachycardia"},
            {"id": "D", "text": "Antipsychotics prevent methadone from crossing the blood-brain barrier resulting in intractable opioid withdrawal"}
        ],
        "correctAnswer": "A",
        "explanation": "Methadone blocks the hERG potassium channel in cardiac myocytes, producing dose-dependent prolongation of the corrected QT (QTc) interval. Co-prescribing psychotropic medications that also prolong the QTc interval (such as amisulpride, haloperidol, chlorpromazine, or citalopram) creates a dangerous cumulative risk of polymorphic ventricular tachycardia (Torsades de Pointes) and fatal ventricular fibrillation. Baseline and serial ECG monitoring is mandatory.",
        "incorrectExplanations": {
            "B": "Methadone prolongs ventricular repolarization (QTc), not the PR interval.",
            "C": "The primary cardiac risk is hERG potassium channel blockade, not anticholinergic supraventricular tachycardia.",
            "D": "Antipsychotics do not block methadone at the blood-brain barrier."
        },
        "learningObjective": "Analyze drug-drug interactions between opioid maintenance pharmacotherapy (methadone) and psychotropics regarding QTc prolongation.",
        "reference": "Krantz, M. J. et al. (2009). QTc Interval Screening in Methadone Treatment. Annals of Internal Medicine; Maudsley Prescribing Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1052",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Advanced",
        "questionText": "According to DSM-5-TR and ICD-11 diagnostic guidelines, how should a mental health nurse differentiate between an independent major depressive disorder and a substance-induced depressive disorder in a patient with heavy alcohol misuse?",
        "options": [
            {"id": "A", "text": "Depression is always classified as substance-induced as long as the patient has consumed alcohol at any point in their lifetime"},
            {"id": "B", "text": "If depressive symptoms precede the onset of heavy drinking, or persist for at least 1 month after the complete cessation of acute alcohol withdrawal and intoxication, an independent depressive disorder is diagnosed"},
            {"id": "C", "text": "Alcohol-induced depression is identified purely by measuring elevated serum carbohydrate-deficient transferrin (CDT)"},
            {"id": "D", "text": "Independent depression only occurs in individuals with a family history of suicide"}
        ],
        "correctAnswer": "B",
        "explanation": "Diagnostic criteria (DSM-5-TR / ICD-11) specify that a depressive disorder is considered primary/independent if depressive episodes occurred prior to the onset of the substance use disorder, or if substantial depressive symptoms persist for a significant period of time (typically at least 4 weeks / 1 month) following the cessation of acute intoxication or severe withdrawal. Symptoms clearing rapidly during withdrawal point toward a substance-induced etiology.",
        "incorrectExplanations": {
            "A": "Past lifetime alcohol consumption does not automatically render all future mood episodes substance-induced.",
            "C": "CDT is a biomarker for chronic heavy alcohol consumption, not a diagnostic marker of psychiatric etiology.",
            "D": "Family history of suicide is a general risk factor, not a diagnostic criterion separating primary from substance-induced mood disorders."
        },
        "learningObjective": "Differentiate between substance-induced and independent psychiatric disorders using temporal assessment criteria.",
        "reference": "Diagnostic and Statistical Manual of Mental Disorders (DSM-5-TR); Schuckit, M. A. et al. (1997). Clinical Implications of Primary vs Substance-Induced Depression.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1053",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Advanced",
        "questionText": "A 29-year-old patient with borderline personality disorder and severe chronic polysubstance use has developed physical dependence on illicit street diazepam and alprazolam (equivalent to ~80 mg diazepam daily). What is the safest clinical protocol for discontinuing high-dose chronic benzodiazepines in an inpatient dual diagnosis setting?",
        "options": [
            {"id": "A", "text": "Abrupt cessation with PRN oral chlorpromazine for agitation to promote personal accountability"},
            {"id": "B", "text": "Immediate induction onto buprenorphine/naloxone combined with high-dose melatonin"},
            {"id": "C", "text": "Conversion to a standardized long-acting equivalent (diazepam), followed by a gradual, stepwise dose reduction (e.g., tapering by 10-20% every 1-2 weeks) while monitoring for withdrawal delirium and seizures"},
            {"id": "D", "text": "Rapid flumazenil infusion over 24 hours to accelerate receptor clearance"}
        ],
        "correctAnswer": "C",
        "explanation": "Abrupt cessation of high-dose benzodiazepines causes life-threatening withdrawal complications, including generalized status epilepticus, delirium tremens, extreme autonomic instability, and psychosis. The evidence-based approach involves converting short-acting benzodiazepines (e.g., alprazolam) to a long-acting agent (diazepam) to eliminate peaks and troughs, followed by a slow, gradual taper (reducing by 10-20% every 1 to 2 weeks), tailored to patient stability.",
        "incorrectExplanations": {
            "A": "Abrupt cessation carries high mortality from seizures and autonomic rebound; chlorpromazine lowers seizure threshold further.",
            "B": "Buprenorphine is an opioid partial agonist with zero action on GABA-A receptors; it will not prevent benzodiazepine withdrawal seizures.",
            "D": "Flumazenil is a benzodiazepine antagonist that instantly precipitates severe refractory status epilepticus in benzodiazepine-dependent individuals."
        },
        "learningObjective": "Manage safe pharmacological detoxification and tapering regimens for high-dose benzodiazepine dependence.",
        "reference": "Maudsley Prescribing Guidelines (14th Ed.); Ashton, H. (2002). The Ashton Manual: Benzodiazepines - How They Work & How to Withdraw.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1054",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex dual diagnosis",
        "difficulty": "Expert",
        "questionText": "A dual diagnosis nurse is implementing the evidence-based 'Seeking Safety' model for a cohort of patients experiencing comorbid severe Post-Traumatic Stress Disorder (PTSD) and active substance use disorders. What is the defining clinical philosophy and operational focus of the Seeking Safety manualized protocol?",
        "options": [
            {"id": "A", "text": "Patients are required to achieve 60 days of total abstinence before any discussion of traumatic stress is permitted"},
            {"id": "B", "text": "Patients must undergo intensive prolonged exposure therapy, recounting detailed trauma narratives while under physiological stress monitoring"},
            {"id": "C", "text": "The program relies primarily on pharmacological aversion therapy combined with confrontational group dynamics"},
            {"id": "D", "text": "It is an integrated, present-focused cognitive-behavioral model emphasizing safety across cognitive, behavioral, and interpersonal domains without requiring patients to delve into detailed trauma narrative processing while actively unstable"}
        ],
        "correctAnswer": "D",
        "explanation": "Seeking Safety (developed by Lisa Najavits) is an evidence-based, manualized integrated therapy for co-occurring PTSD and substance use disorders. Its fundamental principle is prioritizing 'safety' as the first stage of recovery across thinking, behavior, emotions, and relationships. Crucially, it does not require patients to recount detailed trauma memories (which could trigger severe substance craving or decompensation in early recovery), making it safe and effective even when patients are still actively using substances.",
        "incorrectExplanations": {
            "A": "Seeking Safety specifically allows individuals to participate while still working toward abstinence; it does not demand 60 days of sobriety.",
            "B": "Prolonged exposure is past-focused trauma processing and is inappropriate during early unstable dual diagnosis crisis.",
            "C": "The model is compassionate, psychoeducational, and cognitive-behavioral; it rejects confrontational methods and aversion therapy."
        },
        "learningObjective": "Explicate the principles and clinical application of the Seeking Safety model in co-occurring PTSD and substance use.",
        "reference": "Najavits, L. M. (2002). Seeking Safety: A Treatment Manual for PTSD and Substance Abuse. Guilford Press; SAMHSA NREPP.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 5: Forensic psychiatric nursing (Q1055 - Q1064)
    # Answers: A, B, C, D, A, B, C, D, A, B
    # Difficulties: F, F, F, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1055",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Foundation",
        "questionText": "In forensic mental health environments, security is conceptualized into three interdependent domains: physical, procedural, and relational security. Which scenario best exemplifies effective 'relational security' in daily nursing practice?",
        "options": [
            {"id": "A", "text": "A nurse develops an in-depth understanding of a patient's personality, early warning signs of distress, relationship dynamics, and behavioral patterns, enabling proactive intervention before risk escalates"},
            {"id": "B", "text": "Installing 5-meter perimeter fences with razor wire, anti-climb mesh, and biometric airlocks at all ward entrances"},
            {"id": "C", "text": "Conducting daily searches of patient lockers, counting cutlery after every meal, and auditing key fobs strictly at shift handovers"},
            {"id": "D", "text": "Requiring all patients to wear electronic GPS tracking tags when walking within the secure courtyard"}
        ],
        "correctAnswer": "A",
        "explanation": "Relational security (as defined by the UK Department of Health's 'See Think Act' framework) is the knowledge and understanding staff have of a patient and of the ward climate, and how this knowledge is translated into clinical care and dynamic risk management. Physical security involves fences, doors, and architecture; procedural security involves policies, searches, and audits.",
        "incorrectExplanations": {
            "B": "Perimeter fences and physical barriers represent physical security.",
            "C": "Searches, key audits, and cutlery counts are classic components of procedural security.",
            "D": "Electronic tags and physical tracking devices fall under physical and procedural security domains."
        },
        "learningObjective": "Distinguish between physical, procedural, and relational security in forensic mental health nursing.",
        "reference": "Department of Health (2015). See Think Act: Your Guide to Relational Security (2nd Ed.); Royal College of Psychiatrists Quality Network for Forensic Mental Health.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1056",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Foundation",
        "questionText": "A forensic psychiatric nurse is utilizing the Historical Clinical Risk Management-20 Version 3 (HCR-20 v3) to assess violent recidivism risk. How does the structure of the HCR-20 v3 categorize risk factors, and why is this distinction clinically vital for nursing care planning?",
        "options": [
            {"id": "A", "text": "It divides risk strictly by chronological age and biological sex without examining psychological mechanisms"},
            {"id": "B", "text": "It separates fixed Historical factors (static, unchangeable) from Clinical factors (current, dynamic psychological state) and Risk Management factors (future environmental scenarios), allowing nurses to identify modifiable dynamic treatment targets"},
            {"id": "C", "text": "It classifies patients into numerical delinquency percentiles that permanently determine security classification without reassessment"},
            {"id": "D", "text": "It relies entirely on computerized facial recognition algorithms to predict physical aggression"}
        ],
        "correctAnswer": "B",
        "explanation": "The HCR-20 v3 utilizes Structured Professional Judgment (SPJ). It comprises 10 Historical items (static past events like history of violence, substance abuse, childhood trauma), 5 Clinical items (current dynamic factors like lack of insight, active symptoms, impulsivity), and 5 Risk Management items (future contextual factors like housing, support, stress). Nurses focus care plans on modifiable dynamic Clinical and Risk factors to reduce risk.",
        "incorrectExplanations": {
            "A": "The tool does not reduce risk assessment to age and sex; it evaluates 20 comprehensive clinical and contextual items.",
            "C": "HCR-20 v3 is not an actuarial scoring scale that fixes a permanent percentile; it guides individualized, dynamic formulation.",
            "D": "The tool is an evidence-based clinical judgment guide, not a facial recognition system."
        },
        "learningObjective": "Differentiate static historical and dynamic clinical risk factors using structured professional judgment tools (HCR-20 v3).",
        "reference": "Douglas, K. S. et al. (2013). HCR-20 Version 3: Assessing Risk for Violence. Mental Health, Law, and Policy Institute; NICE CG133.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1057",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Foundation",
        "questionText": "Under common law criminal jurisprudence (originating from the Pritchard criteria in English law), what core legal capacities are assessed when determining an individual's 'fitness to plead' and stand trial?",
        "options": [
            {"id": "A", "text": "Whether the defendant has an IQ greater than 100 and can draft their own legal brief"},
            {"id": "B", "text": "Whether the defendant feels remorse for the alleged victim and expresses moral regret"},
            {"id": "C", "text": "Whether the defendant understands the nature of the charges, can plead with understanding to the indictment, comprehend the trial proceedings, instruct legal counsel, and challenge a juror"},
            {"id": "D", "text": "Whether the defendant agrees with all witness statements submitted by the prosecution"}
        ],
        "correctAnswer": "C",
        "explanation": "Fitness to plead (the Pritchard test, R v Pritchard 1836) evaluates whether a defendant has sufficient mental capacity to participate meaningfully in trial proceedings. Criteria include: capacity to comprehend the course of proceedings; capacity to understand the nature of the charge; capacity to plead to the indictment; capacity to instruct legal representatives; and capacity to challenge a juror.",
        "incorrectExplanations": {
            "A": "An IQ over 100 and ability to draft legal briefs are not required; basic comprehension and communication suffice.",
            "B": "Remorse and moral regret relate to sentencing and character, not trial competence.",
            "D": "Defendants are expected to contest evidence if they plead not guilty; agreeing with prosecution is not a criterion of fitness."
        },
        "learningObjective": "Identify the legal criteria and nursing assessment elements regarding fitness to plead.",
        "reference": "R v Pritchard (1836); Law Commission (2016). Unfitness to Plead (Law Com No 364); Grubin, D. (1996). What Does Fitness to Plead Mean? Criminal Behaviour and Mental Health.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1058",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Intermediate",
        "questionText": "The legal standard for the insanity defence in many common law jurisdictions is derived from the historic M'Naghten Rules (1843). To establish a defence on the ground of insanity, what must be clearly proven regarding the defendant's mental state at the time of committing the act?",
        "options": [
            {"id": "A", "text": "That the defendant was under the voluntary influence of alcohol or non-prescribed narcotics"},
            {"id": "B", "text": "That the defendant was experiencing severe emotional distress following marital separation"},
            {"id": "C", "text": "That the defendant possessed a personality disorder characterized by persistent antisocial traits"},
            {"id": "D", "text": "That the party accused was labouring under such a defect of reason, from disease of the mind, as not to know the nature and quality of the act they were doing; or, if they did know it, that they did not know they were doing what was wrong"}
        ],
        "correctAnswer": "D",
        "explanation": "The M'Naghten Rules establish that to mount an insanity defence, it must be proved that at the time of the committing of the act, the accused was laboring under such a defect of reason, from disease of the mind, as not to know the nature and quality of the act they were doing, or if they did know it, that they did not know that what they were doing was wrong. This is an objective legal test.",
        "incorrectExplanations": {
            "A": "Voluntary intoxication explicitly negates the defence of insanity in common law jurisdictions.",
            "B": "Situational emotional distress does not meet the legal threshold of a 'disease of the mind' causing defect of reason.",
            "C": "Antisocial personality disorder alone does not satisfy the criteria for legal insanity."
        },
        "learningObjective": "Articulate the legal principles and mental status criteria comprising the M'Naghten rules for the insanity defence.",
        "reference": "M'Naghten's Case (1843) 10 Cl & Fin 200; East, N. (2012). Forensic Psychiatry and the Law; Mackay, R. D. (1995). Mental Condition Defences in the Criminal Law.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1059",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Intermediate",
        "questionText": "A patient detained in a medium secure forensic unit under Section 37/41 of the Mental Health Act 1983 (Hospital Order with Restriction Order) has applied to the First-tier Tribunal (Mental Health). What is the primary role and responsibility of the named forensic primary nurse during the Tribunal hearing?",
        "options": [
            {"id": "A", "text": "Submit a comprehensive nursing report detailing behavioral observations, progress in therapeutic programs, compliance, and dynamic risk formulation, and provide objective oral testimony under questioning"},
            {"id": "B", "text": "Advocate unconditionally for the patient's immediate discharge regardless of active psychotic symptoms or violent threats"},
            {"id": "C", "text": "Act as the patient's legal defense barrister and cross-examine the medical witnesses"},
            {"id": "D", "text": "Serve as the presiding judicial authority determining whether the Section should be rescinded"}
        ],
        "correctAnswer": "A",
        "explanation": "At a Mental Health Review Tribunal, the named nurse provides an independent, professional nursing report documenting the patient's day-to-day presentation, engagement with treatment, mental state, relational interactions, self-harm or violence incidents, and dynamic risk factors. In the hearing, the nurse gives oral evidence and answers questions from the legal panel, the patient's solicitor, and the medical member with professional objectivity.",
        "incorrectExplanations": {
            "B": "Nurses must remain professional, objective witnesses to fact and clinical risk; unconditional advocacy that ignores safety breaches professional codes.",
            "C": "The patient is represented by an independent legal representative (mental health solicitor), not the ward nurse.",
            "D": "The tribunal panel (consisting of a Judge, a Medical Member, and a Specialist Lay Member) holds judicial authority."
        },
        "learningObjective": "Prepare nursing documentation and provide professional evidence for Mental Health Review Tribunals.",
        "reference": "Mental Health Act 1983: Code of Practice (DHSC, 2015); Tribunal Procedure (First-tier Tribunal) (Health, Education and Social Care Chamber) Rules.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1060",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Intermediate",
        "questionText": "A restricted forensic patient subject to Section 37/41 wishes to participate in unescorted ground leave within the hospital perimeter. Under forensic mental health legislation in England and Wales, whose statutory permission is required before Section 17 leave can be granted to a restricted patient?",
        "options": [
            {"id": "A", "text": "The hospital ward manager and senior healthcare assistant on duty"},
            {"id": "B", "text": "The Secretary of State for Justice (Ministry of Justice Mental Health Casework Section)"},
            {"id": "C", "text": "The patient's nearest relative or nominated person"},
            {"id": "D", "text": "The local magistrates' court bench"}
        ],
        "correctAnswer": "B",
        "explanation": "A Section 41 restriction order transfers key management decisions from the clinical team alone to the Ministry of Justice. Under Section 17 of the Mental Health Act, any leave of absence (whether escorted or unescorted, short or extended) for a restricted patient (Section 37/41, 47/49, or 48/49) requires the explicit prior approval of the Secretary of State for Justice (via the Mental Health Casework Section).",
        "incorrectExplanations": {
            "A": "Ward staff cannot authorize leave for a restricted patient without Ministry of Justice consent.",
            "C": "The nearest relative has rights of consultation or notification, but cannot grant statutory leave.",
            "D": "Magistrates have no jurisdiction over Section 17 leave in restricted mental health cases."
        },
        "learningObjective": "Explain statutory governance and legal restrictions (Section 41) concerning community and ground leave.",
        "reference": "Mental Health Act 1983; Ministry of Justice Mental Health Casework Section (MHCS) Guidance on Restricted Patients (2020).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1061",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Advanced",
        "questionText": "A forensic Community Mental Health Nurse (forensic CMHN) is supervising a conditionally discharged patient with paranoid schizophrenia who has a past history of violent offending when unwell. During a routine home visit, the nurse notes early warning signs: mild persecutory ideas regarding neighbors, social withdrawal, and erratic medication compliance. Which clinical strategy is most effective?",
        "options": [
            {"id": "A", "text": "Utilize the patient's pre-agreed personalized Relapse Prevention Plan / Relapse Signature, increase contact frequency, coordinate with the responsible clinician, and consider recall powers if risk escalates"},
            {"id": "B", "text": "Discharge the patient from the forensic service immediately to reduce their paranoia about being monitored"},
            {"id": "C", "text": "Contact the local police and request immediate SWAT team entry without clinical assessment"},
            {"id": "D", "text": "Wait for 3 months until the next scheduled outpatient clinic to see if the symptoms spontaneously remit"}
        ],
        "correctAnswer": "A",
        "explanation": "Effective forensic community nursing hinges on the early detection of the patient's individual 'relapse signature' (the unique sequence of thoughts, feelings, and subtle behaviors that precede overt psychosis and risk). Proactive intervention includes reviewing the relapse plan, increasing visits, engaging family/carers, reviewing medication, and liaising with the Responsible Clinician. For conditionally discharged patients, the Secretary of State can issue an urgent warrant of recall if risk to public safety becomes acute.",
        "incorrectExplanations": {
            "B": "Discharging an escalating forensic patient abandons public protection and clinical duty of care.",
            "C": "Calling armed police without evidence of an imminent armed threat is disproportionate and traumatizing.",
            "D": "Waiting 3 months allows insidious psychosis and risk of violent recidivism to manifest fully."
        },
        "learningObjective": "Implement relapse signature monitoring and risk management protocols in community forensic mental health nursing.",
        "reference": "Birchwood, M. et al. (2000). Early Intervention in Psychosis: The Critical Period Hypothesis; Ministry of Justice Recall Guidance (2021).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1062",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Advanced",
        "questionText": "A forensic nurse participates in Multi-Agency Public Protection Arrangements (MAPPA) meetings regarding the planned discharge of a high-risk offender with severe mental illness. What is the statutory function of MAPPA, and what are its three management levels?",
        "options": [
            {"id": "A", "text": "A charity organization providing microloans to former prisoners across three financial categories"},
            {"id": "B", "text": "A multi-agency statutory framework (Police, Prison, and Probation as Responsible Authorities, with Health as a duty-to-cooperate body) operating across Level 1 (Ordinary Agency Management), Level 2 (Multi-Agency Public Protection Meetings), and Level 3 (Senior Multi-Agency Management for critical cases)"},
            {"id": "C", "text": "A private security contractor providing electronic surveillance in low-security outpatient clinics"},
            {"id": "D", "text": "An internal hospital committee that audits pharmacy dispensing errors on forensic rehabilitation wards"}
        ],
        "correctAnswer": "B",
        "explanation": "MAPPA (Multi-Agency Public Protection Arrangements) was established by the Criminal Justice Act 2003. It brings together the Police, Prison, and National Probation Services (Responsible Authority) alongside mental health trusts and social care (duty-to-cooperate bodies) to assess and manage sexual and violent offenders. Level 1 involves single-agency management; Level 2 involves multi-agency case conferences; and Level 3 is reserved for the highest-risk cases requiring senior leadership intervention and substantial resources.",
        "incorrectExplanations": {
            "A": "MAPPA is a statutory public protection framework, not a charity providing financial loans.",
            "C": "MAPPA is not a private security contractor.",
            "D": "MAPPA oversees community public safety and violent offenders, not internal pharmacy audits."
        },
        "learningObjective": "Explain the operational structure, statutory obligations, and risk tiers of Multi-Agency Public Protection Arrangements (MAPPA).",
        "reference": "Ministry of Justice (2020). MAPPA Guidance (Version 4.5); Criminal Justice Act 2003 Sections 325-327.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1063",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Advanced",
        "questionText": "When working with perpetrators of severe index offenses (such as homicide or sexual violence) in a high-secure hospital, a forensic nurse notices emerging feelings of revulsion, anxiety, and a desire to avoid interacting with a newly admitted patient. How should the nurse professionally address this countertransference?",
        "options": [
            {"id": "A", "text": "Suppress all emotional reactions and treat the patient with punitive coldness to demonstrate authority"},
            {"id": "B", "text": "Refuse to provide nursing care and demand the patient be immediately transferred to another ward"},
            {"id": "C", "text": "Bring these reactions to regular, reflective clinical supervision to explore countertransference, maintain professional boundaries, and ensure therapeutic, non-judgmental, yet risk-aware nursing care"},
            {"id": "D", "text": "Discuss the patient's horrific crime details openly on social media to seek peer emotional validation"}
        ],
        "correctAnswer": "C",
        "explanation": "Countertransference is unavoidable when working with forensic patients who have committed serious harm. Unprocessed countertransference can lead to unconscious avoidance, punitive attitudes, or boundary violations. Forensic nurses must utilize clinical supervision, reflective practice groups, and psychodynamic formulations to examine their internal reactions, maintaining a balance between therapeutic alliance, compassion, and vigilant risk awareness.",
        "incorrectExplanations": {
            "A": "Punitive attitudes and emotional withdrawal compromise relational security and violate professional codes of conduct.",
            "B": "Demanding transfers without reflective exploration prevents professional growth and disrupts continuity of care.",
            "D": "Sharing clinical details on social media is an egregious breach of confidentiality and statutory law."
        },
        "learningObjective": "Manage countertransference, emotional distress, and professional boundaries when caring for forensic psychiatric patients.",
        "reference": "Mason, T. & Mercer, D. (2010). Forensic Mental Health Nursing: Interpersonal Processes; NMC Code (2018).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1064",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Forensic psychiatric nursing",
        "difficulty": "Expert",
        "questionText": "A 35-year-old patient with delusional disorder (erotomanic subtype) has a history of stalking a prominent public figure, sending intrusive communications and attempting forced entry into the victim's workplace. Using the Stalking Risk Profile (SRP), how should the forensic mental health nurse categorize the motivation, and which clinical intervention is indicated?",
        "options": [
            {"id": "A", "text": "Predatory stalker driven purely by sadistic sexual gratification; manage solely with behavioral aversion shocks"},
            {"id": "B", "text": "Intimacy Seeker driven by a fixed delusional belief that the victim reciprocates their profound romantic love; manage with antipsychotic pharmacotherapy, psychological reality-testing interventions, strict legal non-contact boundaries, and ongoing victim protection liaisons"},
            {"id": "C", "text": "Incompetent Suitor with no mental illness; manage by arranging social dance lessons to improve courtship skills"},
            {"id": "D", "text": "Resentful stalker seeking financial compensation; manage through civil small claims mediation"}
        ],
        "correctAnswer": "B",
        "explanation": "The Stalking Risk Profile (Mullen et al.) categorizes stalkers by psychological motivation: Intimacy Seeker, Rejected, Resentful, Incompetent Suitor, and Predatory. Intimacy Seekers often suffer from delusional disorder (erotomania) or schizophrenia, firmly believing that true love exists between them and the target. They are persistent and resistant to simple legal warnings. Management requires treating the underlying psychosis, firm containment boundaries, and multi-agency victim safety coordination.",
        "incorrectExplanations": {
            "A": "Erotomanic delusions are not predatory sadistic stalking.",
            "C": "An erotomanic stalker has a fixed psychotic delusion, not merely awkward dating skills.",
            "D": "Resentful stalkers are motivated by a sense of injustice/revenge, unlike erotomanic intimacy seekers."
        },
        "learningObjective": "Utilize the Stalking Risk Profile to categorize stalking typologies and formulate psychiatric management strategies.",
        "reference": "Mullen, P. E., Pathé, M., & Purcell, R. (2009). The Stalking Risk Profile: Guidelines for the Assessment and Management of Stalkers; Fixated Threat Assessment Centre (FTAC).",
        "contentReviewStatus": "Peer Reviewed"
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(MOD11_PART1)} questions for Module 11 Part 1.")
