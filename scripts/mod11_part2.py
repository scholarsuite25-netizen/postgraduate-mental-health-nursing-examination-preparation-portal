# scripts/mod11_part2.py
# Questions Q1065 to Q1114 (Topics 6 to 10 of Module 11)

MOD11_PART2 = [
    # -------------------------------------------------------------
    # Topic 6: Medical comorbidities in psychiatry (Q1065 - Q1074)
    # Answers: C, D, A, B, C, D, A, B, C, D
    # Difficulties: F, F, I, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1065",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Foundation",
        "questionText": "Epidemiological studies consistently document that individuals with severe and persistent mental illness (SPMI), such as schizophrenia and bipolar disorder, experience a 15 to 20-year reduction in life expectancy compared to the general population. What represents the leading cause of this premature mortality gap?",
        "options": [
            {"id": "A", "text": "Completed suicide and violent accidental injuries"},
            {"id": "B", "text": "Homicidal assault occurring in inpatient secure settings"},
            {"id": "C", "text": "Preventable cardiovascular disease, type 2 diabetes, and metabolic disorders compounded by lifestyle factors and psychotropic side effects"},
            {"id": "D", "text": "Fatal adverse reactions to electroconvulsive therapy"}
        ],
        "correctAnswer": "C",
        "explanation": "While suicide is a tragic contributor, the vast majority (approx. 75-80%) of the 15-20 year premature mortality gap in severe mental illness is driven by preventable physical health conditions, primarily cardiovascular disease (ischemic heart disease, stroke), metabolic syndrome, type 2 diabetes, respiratory disease, and cancers. This inequality is driven by antipsychotic cardiometabolic adverse effects, high smoking rates, sedentary lifestyle, poor diet, and diagnostic overshadowing.",
        "incorrectExplanations": {
            "A": "Suicide accounts for approximately 15-20% of excess deaths, whereas cardiovascular and physical illnesses account for the large majority.",
            "B": "Homicide within secure units is exceedingly rare and statistically negligible as a driver of national life expectancy gaps.",
            "D": "ECT has an extremely low mortality rate (less than 1 in 50,000 treatments) and does not explain population-level mortality gaps."
        },
        "learningObjective": "Identify the primary causes and epidemiological drivers of the 15-20 year life expectancy gap in severe mental illness.",
        "reference": "World Health Organization (WHO) (2018). Guidelines on Management of Physical Health Conditions in Adults with Severe Mental Disorders; Royal College of Psychiatrists (2013). Whole-Person Care.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1066",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Foundation",
        "questionText": "Under the International Diabetes Federation (IDF) and NCEP ATP III consensus guidelines, which cluster of physical and laboratory findings confirms the clinical diagnosis of Metabolic Syndrome?",
        "options": [
            {"id": "A", "text": "Isolated resting bradycardia, low serum urea, and elevated serum albumin"},
            {"id": "B", "text": "Generalized lymphadenopathy, leukocytosis, and profound weight loss"},
            {"id": "C", "text": "Hypercalcemia, low serum creatinine, and resting hypotension"},
            {"id": "D", "text": "Central adiposity (elevated waist circumference) PLUS any two of: elevated triglycerides (≥1.7 mmol/L), reduced HDL cholesterol (<1.03 mmol/L in men, <1.29 mmol/L in women), elevated blood pressure (≥130/85 mmHg), or elevated fasting plasma glucose (≥5.6 mmol/L)"}
        ],
        "correctAnswer": "D",
        "explanation": "Metabolic syndrome is a constellation of cardiometabolic risk factors. The IDF consensus criteria require central obesity (waist circumference with ethnicity-specific cut-offs) plus any two of the following: raised triglycerides (≥1.7 mmol/L / 150 mg/dL), reduced HDL cholesterol (<1.03 mmol/L in men, <1.29 mmol/L in women), elevated blood pressure (systolic ≥130 or diastolic ≥85 mmHg), or raised fasting plasma glucose (≥5.6 mmol/L / 100 mg/dL) or diagnosed type 2 diabetes.",
        "incorrectExplanations": {
            "A": "Bradycardia and low urea are not components of metabolic syndrome.",
            "B": "Lymphadenopathy and weight loss suggest infectious, inflammatory, or malignant pathologies.",
            "C": "Hypercalcemia and hypotension are unrelated to cardiometabolic syndrome."
        },
        "learningObjective": "Identify the diagnostic clinical and laboratory criteria for metabolic syndrome.",
        "reference": "Alberti, K. G. et al. (2009). Harmonizing the Metabolic Syndrome: A Joint Interim Statement. Circulation; NICE Guideline CG178.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1067",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Intermediate",
        "questionText": "The 'Lester UK Adaptation' of the cardiometabolic resource provides mental health nurses with an evidence-based monitoring framework for patients prescribed antipsychotics. What is the recommended timeline for cardiometabolic screening (waist circumference, BMI, blood pressure, fasting glucose/HbA1c, and lipid panel) following the initiation of a new antipsychotic?",
        "options": [
            {"id": "A", "text": "At baseline, at 12 weeks, at 1 year, and annually thereafter (with weight/BMI monitored weekly for the first 6 weeks and at 12 weeks)"},
            {"id": "B", "text": "Only once every 5 years, unless the patient gains more than 30 kilograms"},
            {"id": "C", "text": "Daily for the first 2 weeks, then completely discontinued after discharge"},
            {"id": "D", "text": "Baseline only, because metabolic changes caused by psychotropics are strictly transient and harmless"}
        ],
        "correctAnswer": "A",
        "explanation": "The Lester cardiometabolic tool (endorsed by the Royal College of Psychiatrists and NICE) mandates comprehensive physical health monitoring: baseline measurement of weight, BMI, waist circumference, blood pressure, fasting blood glucose (or HbA1c), and lipid profile; weekly weight checks for the first 6 weeks; full assessment at 12 weeks; at 1 year; and at least annually thereafter.",
        "incorrectExplanations": {
            "B": "Every 5 years is grossly inadequate and allows devastating metabolic decompensation to progress undetected.",
            "C": "Daily laboratory blood draws are inappropriate and impractical, and stopping after discharge abandons chronic risk surveillance.",
            "D": "Metabolic changes from atypical antipsychotics are enduring, progressive, and carry severe morbidity if unmonitored."
        },
        "learningObjective": "Apply the Lester cardiometabolic monitoring framework schedule for patients on antipsychotic pharmacotherapy.",
        "reference": "Shiers, D. et al. (2014). Positive Cardiometabolic Health Resource: The Lester UK Adaptation. Royal College of Psychiatrists; NICE CG178.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1068",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Intermediate",
        "questionText": "A mental health nurse evaluates four different patients with first-episode psychosis about to start antipsychotic therapy. Ranking antipsychotics by metabolic liability, which agents confer the HIGHEST risk of profound weight gain, dyslipidemia, and new-onset type 2 diabetes?",
        "options": [
            {"id": "A", "text": "Aripiprazole, ziprasidone, and lurasidone"},
            {"id": "B", "text": "Clozapine and olanzapine"},
            {"id": "C", "text": "Haloperidol, sulpiride, and pimozide"},
            {"id": "D", "text": "Amisulpride and fluphenazine"}
        ],
        "correctAnswer": "B",
        "explanation": "Clozapine and olanzapine carry the highest liability for severe cardiometabolic disturbance, profound weight gain (often >10-15% of body weight), hypertriglyceridemia, and insulin resistance leading to new-onset type 2 diabetes, independent of weight gain due to direct pancreatic beta-cell receptor antagonism. Conversely, aripiprazole, ziprasidone, and lurasidone have the lowest metabolic risk.",
        "incorrectExplanations": {
            "A": "Aripiprazole, ziprasidone, and lurasidone are considered metabolically neutral or low-risk second-generation antipsychotics.",
            "C": "Typical antipsychotics (haloperidol, pimozide) have high neurological EPS risks but significantly lower metabolic liability than clozapine or olanzapine.",
            "D": "Amisulpride has high hyperprolactinemic risk but moderate-to-low metabolic risk."
        },
        "learningObjective": "Stratify second-generation antipsychotics according to their cardiometabolic risk profiles.",
        "reference": "American Diabetes Association & APA (2004). Consensus Development Conference on Antipsychotic Drugs and Obesity and Diabetes. Diabetes Care; Maudsley Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1069",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Intermediate",
        "questionText": "A 58-year-old psychiatric inpatient has a baseline ECG that shows a heart rate-corrected QT interval (QTc) of 510 ms. The patient is currently prescribed citalopram 40 mg daily and quetiapine 300 mg daily. Why is a QTc interval exceeding 500 ms considered a critical medical emergency?",
        "options": [
            {"id": "A", "text": "It causes acute coronary vasospasm mimicking Prinzmetal's angina"},
            {"id": "B", "text": "It leads directly to acute aortic dissection through vascular shear stress"},
            {"id": "C", "text": "A QTc > 500 ms (or an increase > 60 ms from baseline) significantly increases the risk of early afterdepolarizations triggering Torsades de Pointes, a polymorphic ventricular tachycardia that can degenerate into fatal ventricular fibrillation"},
            {"id": "D", "text": "It indicates irreversible sinoatrial node fibrosis requiring immediate permanent pacemaker implantation"}
        ],
        "correctAnswer": "C",
        "explanation": "The QTc interval reflects the duration of ventricular electrical depolarization and repolarization. A QTc interval greater than 500 ms (or an increase of >60 ms over baseline) represents a critical threshold above which the risk of polymorphic ventricular tachycardia (Torsades de Pointes) escalates exponentially. Torsades de Pointes can rapidly deteriorate into ventricular fibrillation and sudden cardiac death. Offending agents must be stopped immediately and electrolytes (potassium, magnesium) corrected.",
        "incorrectExplanations": {
            "A": "Prinzmetal's angina is coronary vasospasm, not related to delayed ventricular repolarization.",
            "B": "Aortic dissection is a structural vascular tear driven by hypertension and connective tissue defects, not delayed repolarization.",
            "D": "Prolonged QTc does not imply sinus node fibrosis; it is predominantly an ion channelopathy (hERG K+ channel delay)."
        },
        "learningObjective": "Interpret ECG QTc interval prolongation thresholds and describe the clinical danger of Torsades de Pointes in psychiatric pharmacotherapy.",
        "reference": "Taylor, D. et al. The Maudsley Prescribing Guidelines in Psychiatry (14th Ed., 2021); CredibleMeds QTc Classification.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1070",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Intermediate",
        "questionText": "A mental health nurse on an acute ward is facilitating a smoking cessation group. Several patients express anxiety that quitting cigarettes will worsen their psychiatric illness. What does the evidence base (such as the EAGLES trial and systematic reviews) indicate regarding smoking cessation in severe mental illness?",
        "options": [
            {"id": "A", "text": "Smoking cessation is strictly contraindicated in schizophrenia because nicotine is essential for cognitive stability"},
            {"id": "B", "text": "Cessation of smoking is associated with significant increases in completed suicide across all psychiatric diagnoses"},
            {"id": "C", "text": "Varenicline and bupropion are totally prohibited in psychiatric inpatients due to neurotoxic interactions"},
            {"id": "D", "text": "Smoking cessation is associated with reduced depression, anxiety, and stress, improved quality of life, and is safe and effective when supported with smoking cessation pharmacotherapy (e.g., varenicline, dual NRT) alongside psychotropic dose adjustments"}
        ],
        "correctAnswer": "D",
        "explanation": "Robust evidence (including the landmark EAGLES randomized trial and Cochrane reviews by Taylor et al.) demonstrates that smoking cessation in people with psychiatric disorders is associated with long-term reductions in depression, anxiety, and stress, with effect sizes equal to or larger than antidepressant therapy. Varenicline, bupropion, and Nicotine Replacement Therapy (NRT) are effective and safe in SPMI, provided therapeutic drug monitoring (e.g., for clozapine or olanzapine) is maintained as CYP1A2 activity shifts.",
        "incorrectExplanations": {
            "A": "Tobacco smoking causes immense premature cardiovascular and pulmonary death in SPMI; it is never clinically contraindicated to support cessation.",
            "B": "Smoking cessation does not increase suicide rates; mental well-being improves significantly following smoking cessation.",
            "C": "The EAGLES trial confirmed the psychiatric safety and superior efficacy of varenicline and bupropion in individuals with psychiatric disorders."
        },
        "learningObjective": "Advocate for evidence-based smoking cessation interventions in psychiatric populations and dispel myths regarding cessation and mental stability.",
        "reference": "Anthenelli, R. M. et al. (2016). Neuropsychiatric Safety and Efficacy of Varenicline, Bupropion, and Nicotine Patch in Smokers With and Without Psychiatric Disorders (EAGLES). The Lancet, 387(10037), 2507-2520.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1071",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Advanced",
        "questionText": "A 32-year-old patient with first-episode psychosis has gained 14 kg within 4 months of commencing olanzapine 15 mg daily, with a BMI rising from 24 to 28.5 kg/m^2. What evidence-based pharmacological co-prescription has the strongest trial evidence for preventing and attenuating antipsychotic-induced weight gain and insulin resistance?",
        "options": [
            {"id": "A", "text": "Metformin (titrated up to 1000-2000 mg/day in divided doses)"},
            {"id": "B", "text": "High-dose oral prednisone 40 mg daily"},
            {"id": "C", "text": "Phenobarbital 100 mg at bedtime"},
            {"id": "D", "text": "Propranolol 80 mg twice daily"}
        ],
        "correctAnswer": "A",
        "explanation": "Extensive meta-analyses and clinical guidelines recommend metformin (titrated to 1000-2000 mg daily) as the pharmacological intervention of choice for both preventing and treating antipsychotic-induced weight gain, insulin resistance, and metabolic dysfunction when lifestyle measures alone are insufficient. Metformin decreases hepatic gluconeogenesis, enhances peripheral insulin sensitivity, and reduces visceral adiposity.",
        "incorrectExplanations": {
            "B": "Prednisone is a glucocorticoid that accelerates severe weight gain, visceral fat accumulation, and steroid-induced diabetes.",
            "C": "Phenobarbital is a sedating barbiturate with significant abuse liability that provides no metabolic benefit.",
            "D": "Propranolol is a non-selective beta-blocker that can worsen dyslipidemia and insulin resistance."
        },
        "learningObjective": "Evaluate pharmacological interventions (metformin) for the mitigation of antipsychotic-induced weight gain and metabolic dysregulation.",
        "reference": "Zheng, W. et al. (2019). Metformin for Weight Gain and Metabolic Abnormalities Associated with Antipsychotic Use: A Systematic Review and Meta-Analysis. Journal of Psychopharmacology; NICE CG178.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1072",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Advanced",
        "questionText": "A 54-year-old inpatient with chronic schizophrenia presents with tachypnea, acute confusion, diaphoresis, and restless agitation. The on-call junior nurse documents 'escalating psychotic agitation' and offers oral lorazepam. Subsequent emergency physical assessment reveals blood glucose of 28 mmol/L, arterial pH of 7.15, positive serum ketones, and severe diabetic ketoacidosis (DKA). What critical diagnostic failure does this scenario illustrate?",
        "options": [
            {"id": "A", "text": "Malingering syndrome"},
            {"id": "B", "text": "Diagnostic overshadowing: the cognitive bias where acute physical symptoms are mistakenly attributed to a patient's pre-existing psychiatric illness"},
            {"id": "C", "text": "Factitious disorder imposed on self"},
            {"id": "D", "text": "Ganser syndrome"}
        ],
        "correctAnswer": "B",
        "explanation": "Diagnostic overshadowing is a pervasive and dangerous clinical error wherein physical symptoms (such as hypoxia, sepsis, DKA, intracranial lesions, or myocardial ischemia) are incorrectly attributed to a patient's known psychiatric diagnosis, leading to diagnostic delays, inappropriate sedation, and preventable death. Nurses must maintain vigilance that acute changes in mental status or agitation demand physical assessment first.",
        "incorrectExplanations": {
            "A": "Malingering is intentional production of false symptoms for secondary tangible gain, which is not present in severe physiological DKA.",
            "C": "Factitious disorder involves deliberate falsification of illness without external incentives.",
            "D": "Ganser syndrome is characterized by approximate answers ('paralogia') and dissociative symptoms, unrelated to life-threatening diabetic ketoacidosis."
        },
        "learningObjective": "Recognize and prevent diagnostic overshadowing during the assessment of acute physical deterioration in psychiatric patients.",
        "reference": "Jones, S. et al. (2008). Diagnostic Overshadowing: Worse Physical Health Care for People with Mental Illness. Mental Health in Family Medicine; NHS England Physical Health Strategies.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1073",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Advanced",
        "questionText": "A 40-year-old female with schizoaffective disorder on long-term risperidone 6 mg daily reports amenorrhea for 18 months and galactorrhea. Her fasting serum prolactin is markedly elevated at 2,400 mIU/L (normal < 500 mIU/L). What underlying neuroendocrine mechanism and long-term physical morbidity must the psychiatric nurse recognize?",
        "options": [
            {"id": "A", "text": "Dopamine D2 receptor blockade in the tuberoinfundibular pathway disinhibits prolactin release, leading to hypogonadism, low estrogen levels, accelerated bone mineral density loss, and premature osteoporosis"},
            {"id": "B", "text": "Serotonin 5HT2A agonism in the pineal gland stimulating melatonin hypersecretion"},
            {"id": "C", "text": "Histamine H1 blockade causing primary ovarian failure and adrenal insufficiency"},
            {"id": "D", "text": "Direct stimulation of anterior pituitary somatotrophs causing gigantism"}
        ],
        "correctAnswer": "A",
        "explanation": "Dopamine normally acts as the physiological prolactin-inhibiting factor via D2 receptors in the pituitary tuberoinfundibular tract. Antipsychotics with high D2 affinity (particularly risperidone, paliperidone, and amisulpride) block these receptors, leading to hyperprolactinaemia. Chronic hyperprolactinaemia suppresses the hypothalamic-pituitary-gonadal axis, causing hypogonadism (amenorrhea, anovulation, low estrogen in women; erectile dysfunction, low testosterone in men), which results in accelerated bone resorption and early osteoporosis.",
        "incorrectExplanations": {
            "B": "The mechanism involves pituitary D2 dopamine blockade, not pineal 5HT2A receptors.",
            "C": "H1 blockade causes weight gain and sedation, not prolactin secretion or ovarian failure.",
            "D": "Hyperprolactinaemia causes galactorrhea and hypogonadism, not growth hormone excess (gigantism)."
        },
        "learningObjective": "Explain the tuberoinfundibular pathway mechanism of antipsychotic-induced hyperprolactinaemia and its bone demineralization risks.",
        "reference": "Haddad, P. M. & Wieck, A. (2004). Antipsychotic-Induced Hyperprolactinaemia: Mechanisms, Clinical Features and Management. Drugs; Maudsley Guidelines (14th Ed).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1074",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Medical comorbidities in psychiatry",
        "difficulty": "Expert",
        "questionText": "A 62-year-old patient with a 30-year history of treatment-resistant schizophrenia managed with clozapine and anticholinergic medication has severe xerostomia (dry mouth) and widespread dental caries with multiple abscesses. How does poor oral health directly interface with systemic mortality in severe mental illness, and what clinical actions must the nurse take?",
        "options": [
            {"id": "A", "text": "Poor dentition has zero clinical impact on physical health and is purely a cosmetic concern"},
            {"id": "B", "text": "Dental caries can be cured simply by increasing clozapine dosages to induce sialorrhoea"},
            {"id": "C", "text": "Root canal therapy is legally prohibited in individuals with chronic psychoses"},
            {"id": "D", "text": "Severe periodontal disease and chronic odontogenic infections generate persistent systemic inflammatory cytokine cascades that accelerate atherosclerosis, infective endocarditis, and aspiration pneumonia, requiring routine dental referral, artificial saliva, and fluoridated toothpastes"}
        ],
        "correctAnswer": "D",
        "explanation": "Oral disease is dramatically elevated in SPMI due to psychotropic-induced xerostomia (loss of antimicrobial saliva), poor self-care, smoking, and sugar-rich diets. Chronic periodontal infection causes bacteremia and chronic systemic inflammation (elevated IL-6, TNF-alpha, CRP), which accelerates vascular endothelial injury, atherosclerosis, infective endocarditis, and in sedated patients, fatal aspiration pneumonia. Nursing care involves dry mouth management, fluoridated toothpaste, and formal dental service pathways.",
        "incorrectExplanations": {
            "A": "Dismissing dental health as cosmetic ignores its direct link to cardiovascular death, sepsis, and aspiration pneumonia.",
            "B": "Clozapine-induced hypersalivation does not restore normal protective salivary enzymes and can worsen oral fungal infections and aspiration.",
            "C": "Dental procedures are not legally prohibited; denying dental care violates fundamental human rights."
        },
        "learningObjective": "Formulate nursing interventions addressing oral health disparities and their systemic cardiovascular implications in chronic psychiatry.",
        "reference": "Kisely, S. et al. (2015). Advanced Dental Disease in People with Severe Mental Illness: Systematic Review and Meta-Analysis. British Journal of Psychiatry; Department of Health Oral Health Guidance.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 7: Rapid tranquilisation (RT) (Q1075 - Q1084)
    # Answers: A, B, C, D, A, B, C, D, A, B
    # Difficulties: F, F, F, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1075",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Foundation",
        "questionText": "According to the NICE Guideline on Violence and Aggression (NG10), what is the primary therapeutic aim of rapid tranquilisation (RT) in an acute psychiatric crisis?",
        "options": [
            {"id": "A", "text": "To achieve a state of calm and reduce acute behavioral agitation to minimize immediate risk of harm to the patient or others, while avoiding deep sedation or unconsciousness"},
            {"id": "B", "text": "To induce immediate, deep general anesthesia lasting a minimum of 12 hours"},
            {"id": "C", "text": "To administer punitive pharmacological restraint to enforce ward behavioral rules"},
            {"id": "D", "text": "To rapidly eradicate chronic delusional beliefs within 30 minutes"}
        ],
        "correctAnswer": "A",
        "explanation": "NICE NG10 explicitly defines the goal of rapid tranquilisation not as deep sedation, narcosis, or punishment, but to reduce agitation, distress, and immediate physical risk to the patient or others, achieving an optimal state of calm where the patient can be safely engaged in psychosocial de-escalation and ongoing clinical assessment.",
        "incorrectExplanations": {
            "B": "Inducing unconsciousness or general anesthesia is dangerous, unnecessary, and represents over-sedation with high risk of airway collapse.",
            "C": "Using medication as punishment or coercion violates human rights, legal statutes, and professional nursing codes.",
            "D": "RT does not rapidly cure chronic delusions; it acts as an acute sedative and calming intervention."
        },
        "learningObjective": "Define the therapeutic purpose and clinical goals of rapid tranquilisation per national clinical guidelines.",
        "reference": "NICE Guideline NG10: Violence and aggression: short-term management in mental health, health and community settings (2015).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1076",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Foundation",
        "questionText": "Prior to initiating pharmacological rapid tranquilisation for an acutely agitated and aggressive patient on an inpatient ward, which intervention hierarchy must the psychiatric nursing team follow?",
        "options": [
            {"id": "A", "text": "Immediately administer intramuscular medication without verbal interaction to prevent confrontation"},
            {"id": "B", "text": "Exhaust verbal de-escalation, sensory modulation, time-out, and environmental modifications; if medication is necessary, offer oral medication collaboratively before considering parenteral (intramuscular) administration as a last resort"},
            {"id": "C", "text": "Apply four-point mechanical restraints first, then administer rapid IV barbiturates"},
            {"id": "D", "text": "Place the patient in solitary seclusion for 24 hours prior to attempting any communication"}
        ],
        "correctAnswer": "B",
        "explanation": "Guidelines mandate a stepped, least-restrictive care approach: non-pharmacological verbal de-escalation, reducing noise/stimuli, active listening, and offering a quiet area must always be attempted first. If medication is required to avert serious harm, oral administration (such as oral lorazepam or oral antipsychotic) must be offered collaboratively. Intramuscular injection is reserved as a last resort when oral medication is refused and severe danger is imminent.",
        "incorrectExplanations": {
            "A": "Skipping verbal de-escalation and immediately using IM injections breaches the least restrictive principle.",
            "C": "Mechanical restraints and IV barbiturates are high-risk, coercive, and contrary to modern trauma-informed standards.",
            "D": "Seclusion must not be used as an automatic precursor or substitute for de-escalation and active nursing care."
        },
        "learningObjective": "Apply the least restrictive hierarchy of interventions prior to administering rapid tranquilisation.",
        "reference": "NICE Guideline NG10 (2015); Royal College of Nursing (RCN) Restraint Reduction Network Training Standards.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1077",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Foundation",
        "questionText": "Which oral pharmacological combination is widely recommended by evidence-based psychiatric guidelines (e.g., NICE, Maudsley) as a preferred first-line option for rapid tranquilisation when oral medication is accepted?",
        "options": [
            {"id": "A", "text": "Oral lithium carbonate 1200 mg combined with oral carbamazepine"},
            {"id": "B", "text": "Oral clozapine 100 mg combined with oral disulfiram"},
            {"id": "C", "text": "Oral lorazepam (1-2 mg) combined with an oral second-generation antipsychotic (such as olanzapine 5-10 mg or risperidone 1-2 mg), or oral haloperidol combined with promethazine"},
            {"id": "D", "text": "Oral fluoxetine 60 mg combined with oral buspirone"}
        ],
        "correctAnswer": "C",
        "explanation": "Preferred first-line oral RT regimens combine a short-acting benzodiazepine (such as oral lorazepam 1-2 mg) with an oral antipsychotic (such as olanzapine 5-10 mg or risperidone 1-2 mg). Alternatively, where typical antipsychotics are used, oral haloperidol is combined with promethazine to provide sedation and prevent acute dystonic reactions. This dual approach provides rapid calming with lower doses of each drug.",
        "incorrectExplanations": {
            "A": "Lithium and carbamazepine have no acute calming effect and take days to weeks to reach therapeutic blood levels.",
            "B": "Clozapine must never be used for rapid tranquilisation due to severe risk of hypotension, collapse, and required titration schedules.",
            "D": "SSRIs take 2-4 weeks to produce clinical effects and have zero immediate tranquilising utility."
        },
        "learningObjective": "Select appropriate first-line oral medication combinations for rapid tranquilisation.",
        "reference": "Taylor, D. et al. The Maudsley Prescribing Guidelines in Psychiatry (14th Ed., 2021); NICE Guideline NG10.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1078",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Intermediate",
        "questionText": "Which parenteral drug combination is strictly CONTRAINDICATED in rapid tranquilisation protocols due to significant clinical trial and post-marketing reports of fatal cardiorespiratory arrest and profound hypotension?",
        "options": [
            {"id": "A", "text": "IM Haloperidol and IM Promethazine administered in the same syringe"},
            {"id": "B", "text": "IM Lorazepam administered alone"},
            {"id": "C", "text": "IM Haloperidol followed by oral propranolol"},
            {"id": "D", "text": "IM Olanzapine administered concurrently with or within 1 hour of IM Lorazepam (or another parenteral benzodiazepine)"}
        ],
        "correctAnswer": "D",
        "explanation": "The concurrent administration of intramuscular olanzapine and intramuscular benzodiazepines (such as IM lorazepam) is strictly contraindicated by regulatory agencies (MHRA, FDA) and clinical guidelines. Post-marketing surveillance demonstrated multiple fatalities due to profound hypotension, severe central nervous system depression, and fatal cardiorespiratory arrest. If both are necessary, a minimum interval of at least 1 hour (preferably 2 hours) must elapse between IM injections, accompanied by intense physical monitoring.",
        "incorrectExplanations": {
            "A": "IM haloperidol combined with IM promethazine is an established, guideline-endorsed regimen (TREC collaborative trials).",
            "B": "IM lorazepam monotherapy is safe, widely recommended, and not contraindicated.",
            "C": "Oral propranolol after IM haloperidol is not contraindicated, though vitals must be observed."
        },
        "learningObjective": "Identify contraindicated drug combinations (IM olanzapine and IM benzodiazepines) during parenteral rapid tranquilisation.",
        "reference": "MHRA Drug Safety Update: Olanzapine injection (2007); NICE Guideline NG10; Maudsley Guidelines (14th Ed).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1079",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Intermediate",
        "questionText": "Following the administration of intramuscular rapid tranquilisation (IM haloperidol and IM lorazepam) to an acutely agitated patient who is now resting in their room, what is the mandatory physical health monitoring protocol required by NICE guidelines?",
        "options": [
            {"id": "A", "text": "Monitor vital signs (respiratory rate, blood pressure, heart rate, temperature, oxygen saturation) and level of consciousness / sedation score every 15 minutes for the first hour, and then every 30 minutes until the patient is awake and ambulatory"},
            {"id": "B", "text": "Check the patient through the observation window once every 2 hours without entering the room"},
            {"id": "C", "text": "Perform continuous invasive arterial line blood pressure monitoring and endotracheal capnography"},
            {"id": "D", "text": "Take vital signs only if the patient wakes up and requests a drink of water"}
        ],
        "correctAnswer": "A",
        "explanation": "NICE NG10 mandates that after parenteral rapid tranquilisation, vital signs (respiratory rate, oxygen saturation, blood pressure, pulse, temperature) and level of consciousness/sedation score must be monitored every 15 minutes for the first hour. If stable, monitoring continues every 30 minutes until the patient is fully ambulatory and alert. Resuscitation equipment must be immediately accessible.",
        "incorrectExplanations": {
            "B": "Window checks every 2 hours fail to detect hypoventilation, respiratory depression, or hypoxia, and have resulted in preventable deaths.",
            "C": "Invasive arterial lines and intubation capnography belong in intensive care units, not psychiatric inpatient wards.",
            "D": "Waiting for the patient to wake up is negligent; respiratory arrest occurs while the patient appears to be 'sleeping peacefully'."
        },
        "learningObjective": "Execute post-rapid tranquilisation physical health and vital sign monitoring protocols according to NICE guidelines.",
        "reference": "NICE Guideline NG10: Violence and aggression (2015); Royal College of Psychiatrists CR190.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1080",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Intermediate",
        "questionText": "Twenty minutes after receiving IM lorazepam 2 mg for severe behavioral disturbance, a patient becomes unresponsive to verbal stimuli, exhibits shallow respirations at 6 breaths per minute, and has an SpO2 of 84% on room air. What is the immediate sequence of emergency nursing actions?",
        "options": [
            {"id": "A", "text": "Administer immediate oral caffeine and position the patient upright in a chair"},
            {"id": "B", "text": "Open the airway (head tilt/chin lift or jaw thrust), initiate high-flow oxygen via non-rebreather mask or bag-valve-mask ventilations, call the emergency medical crash team, and prepare IV flumazenil under medical direction while maintaining seizure precautions"},
            {"id": "C", "text": "Administer 10 mg of intramuscular haloperidol to stimulate cortical arousal"},
            {"id": "D", "text": "Wait for 60 minutes for the benzodiazepine to be naturally redistributed from the brain"}
        ],
        "correctAnswer": "B",
        "explanation": "Severe respiratory depression (<8-10 breaths/min, hypoxia SpO2 <90%) is a life-threatening complication of benzodiazepine administration. Immediate nursing action requires basic life support: opening the airway, providing bag-valve-mask manual ventilations with high-flow 100% oxygen, calling the medical emergency/cardiac arrest team, and preparing the specific benzodiazepine antagonist flumazenil. Flumazenil must be titrated cautiously in patients with known benzodiazepine tolerance or concurrent pro-convulsant drug exposure to avoid precipitating status epilepticus.",
        "incorrectExplanations": {
            "A": "Oral caffeine is ineffective, contraindicated in unresponsiveness, and causes fatal pulmonary aspiration.",
            "C": "Giving haloperidol will worsen central nervous system depression and cardiorespiratory collapse.",
            "D": "Waiting 60 minutes during acute hypoxemic respiratory arrest leads to irreversible hypoxic brain injury and death."
        },
        "learningObjective": "Manage acute respiratory arrest and benzodiazepine toxicity following rapid tranquilisation.",
        "reference": "Resuscitation Council UK Guidelines (2021); British National Formulary (BNF) Flumazenil Monograph; NICE NG10.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1081",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Advanced",
        "questionText": "Forty-five minutes after receiving intramuscular haloperidol 5 mg, a 21-year-old male becomes acutely distressed, with his eyes locked in an involuntary upward gaze (oculogyric crisis), neck severely hyperextended and twisted (torticollis), and difficulty speaking. What acute neurological condition has occurred, and what is the emergency antidote?",
        "options": [
            {"id": "A", "text": "Acute dystonic reaction; administer anticholinergic medication (such as IM or slow IV procyclidine 5-10 mg or benztropine 1-2 mg) immediately"},
            {"id": "B", "text": "Tardive dyskinesia; administer high-dose oral vitamin E and wait 6 months"},
            {"id": "C", "text": "Neuroleptic malignant syndrome; administer subcutaneous heparin and dantrolene"},
            {"id": "D", "text": "Functional neurological symptom disorder; provide firm confrontation and behavioral extinction"}
        ],
        "correctAnswer": "A",
        "explanation": "Acute dystonia is a dramatic extrapyramidal adverse effect characterized by acute, painful, involuntary muscle spasms, occurring most frequently in young males receiving high-potency first-generation antipsychotics. Clinical manifestations include oculogyric crisis (upward ocular deviation), torticollis (neck twist), retrocollis, and potentially fatal laryngeal dystonia. Treatment is immediate parenteral administration of an anticholinergic antiparkinsonian agent (e.g., IM procyclidine 5-10 mg or benztropine 1-2 mg), which resolves spasms within minutes.",
        "incorrectExplanations": {
            "B": "Tardive dyskinesia occurs after prolonged exposure (months/years) and is characterized by choreoathetoid movements, not acute neck spasms within 45 minutes.",
            "C": "Neuroleptic Malignant Syndrome features severe hyperthermia, 'lead-pipe' muscle rigidity, autonomic instability, and elevated CK over days.",
            "D": "Oculogyric crisis is an organic dopamine/acetylcholine imbalance, not a functional/conversion disorder."
        },
        "learningObjective": "Diagnose acute dystonic reactions and administer emergency anticholinergic antidotes (procyclidine).",
        "reference": "Maudsley Prescribing Guidelines in Psychiatry (14th Ed., 2021); NICE Guideline NG10.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1082",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Advanced",
        "questionText": "To maintain resuscitation readiness in mental health facilities where parenteral rapid tranquilisation is practiced, which minimum emergency equipment and pharmacological reversal agents must be immediately accessible in the clinical area according to regulatory and safety standards?",
        "options": [
            {"id": "A", "text": "A standard home first-aid kit containing adhesive bandages, antiseptic wipes, and oral paracetamol"},
            {"id": "B", "text": "An emergency resuscitation trolley equipped with bag-valve-mask (Ambu bag), working suction apparatus, portable oxygen cylinders, oral/nasopharyngeal airways, automated external defibrillator (AED), pulse oximeter, blood glucose monitor, and IV reversal agents (flumazenil, naloxone, and procyclidine)"},
            {"id": "C", "text": "Only an external landline telephone to call municipal paramedic services"},
            {"id": "D", "text": "An advanced surgical laparotomy tray and central venous catheter insertion kit"}
        ],
        "correctAnswer": "B",
        "explanation": "National standards (NICE NG10, Resuscitation Council UK) state that any psychiatric facility administering parenteral rapid tranquilisation must have immediate access to complete resuscitation equipment. This includes oxygen with appropriate delivery masks, bag-valve-mask manual resuscitator, suction equipment, basic airway adjuncts, AED, vital signs monitors (pulse oximeter, BP cuff, thermometer, glucometer), and emergency drugs including flumazenil (benzodiazepine reversal), naloxone (opioid reversal), and procyclidine (acute dystonia reversal).",
        "incorrectExplanations": {
            "A": "Basic first-aid supplies cannot treat hypoxia, cardiac arrest, or severe respiratory collapse.",
            "C": "Relying solely on external ambulance arrival while a patient suffers hypoxic arrest leads to death within 4-6 minutes.",
            "D": "Surgical laparotomy equipment is not relevant for psychiatric resuscitation."
        },
        "learningObjective": "Specify mandatory resuscitation equipment, monitoring devices, and reversal agents required for rapid tranquilisation.",
        "reference": "Resuscitation Council UK: Quality Standards for Mental Health Inpatient Care (2020); NICE Guideline NG10.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1083",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Advanced",
        "questionText": "A 74-year-old patient with vascular dementia and acute delirium on an acute psychogeriatric ward becomes intensely combative, striking staff members. When rapid tranquilisation is clinically unavoidable in frail older adults, what dosing and pharmacological adaptations must be implemented?",
        "options": [
            {"id": "A", "text": "Administer doses starting at one-quarter to one-half of the standard adult dose, prioritize low-dose oral options (e.g., haloperidol 0.5 mg or lorazepam 0.5 mg), avoid anticholinergic sedatives that exacerbate delirium, and monitor closely for paradoxical excitation and orthostatic falls"},
            {"id": "B", "text": "Administer double the adult dose due to age-related hepatic enzyme induction"},
            {"id": "C", "text": "Use high-dose intravenous diazepam boluses as first-line therapy"},
            {"id": "D", "text": "Administer high-dose promethazine monotherapy because antihistamines have zero adverse effects in dementia"}
        ],
        "correctAnswer": "A",
        "explanation": "In older adults, altered pharmacokinetics (reduced renal clearance, decreased hepatic metabolism, higher body fat percentage prolonging lipophilic drug half-lives) and increased pharmacodynamic sensitivity elevate the risks of oversedation, respiratory depression, paradoxical disinhibition, stroke, and falls. Dosing must begin at 25-50% of typical adult doses. Anticholinergic agents must be minimized because they exacerbate confusion and delirium.",
        "incorrectExplanations": {
            "B": "Older adults have reduced drug clearance; doubling doses would cause severe toxicity and death.",
            "C": "IV diazepam carries extreme risk of apnea, hypotension, and phlebitis; IV use is contraindicated in ward agitation.",
            "D": "Promethazine has strong anticholinergic properties that worsen delirium and cognitive decline in dementia."
        },
        "learningObjective": "Adapt rapid tranquilisation pharmacokinetics, dosing, and safety precautions for frail older adults with dementia.",
        "reference": "NICE Guideline NG97: Dementia: assessment, management and support (2018); British Geriatrics Society Delirium Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1084",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Rapid tranquilisation (RT)",
        "difficulty": "Expert",
        "questionText": "Following an episode of restrictive physical restraint and parenteral rapid tranquilisation, what are the key components of an evidence-based post-incident review and debriefing process for the service user?",
        "options": [
            {"id": "A", "text": "Requiring the patient to sign an admission of guilt and disciplinary agreement before being permitted out of their room"},
            {"id": "B", "text": "Conducting a structured, trauma-informed debrief once the patient is calm and receptive: exploring triggers, assessing emotional impact, providing a clear explanation of what occurred, checking for physical injuries, and updating the patient's Advance Choice Document / Crisis Plan to prevent future restrictive interventions"},
            {"id": "C", "text": "Having the security team deliver a formal reprimand regarding hospital rules"},
            {"id": "D", "text": "Avoiding any mention of the incident to prevent triggering retroactive cognitive dissonance"}
        ],
        "correctAnswer": "B",
        "explanation": "NICE NG10 and the Restraint Reduction Network mandate structured post-incident reviews following restrictive interventions. Debriefing must be trauma-informed and collaborative, conducted once the individual has fully recovered from sedation. It serves to address psychological trauma, check physical well-being, explore precipitating triggers, review what helped or hindered, and update the patient's crisis plan/advance choice document to avoid future coercion.",
        "incorrectExplanations": {
            "A": "Forcing admissions of guilt is punitive, non-therapeutic, and violates human rights and dignity.",
            "C": "Lectures from security officers increase hostility, trauma, and staff-patient conflict.",
            "D": "Ignoring the event prevents clinical learning, leaves unresolved trauma, and fails to identify modifiable triggers."
        },
        "learningObjective": "Conduct trauma-informed post-incident debriefing and co-produce preventative crisis plans following rapid tranquilisation.",
        "reference": "Restraint Reduction Network (RRN) Training Standards; NICE Guideline NG10; Care Quality Commission (CQC) Brief Guide on Restraint.",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 8: Palliative care in end-stage psychiatric conditions (Q1085 - Q1094)
    # Answers: C, D, A, B, C, D, A, B, C, D
    # Difficulties: F, F, I, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1085",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Foundation",
        "questionText": "What is the defining clinical philosophy when shifting from curative/rehabilitative treatment to a palliative psychiatric approach for patients with Severe and Enduring Anorexia Nervosa (SEED-AN)?",
        "options": [
            {"id": "A", "text": "Withdrawing all medical monitoring and encouraging active voluntary euthanasia"},
            {"id": "B", "text": "Enforcing continuous involuntary nasogastric hyperalimentation until a BMI > 22 is achieved"},
            {"id": "C", "text": "Shifting the clinical focus from aggressive, coercive weight restoration to maximizing quality of life, harm reduction, symptom relief, medical stabilization, and psychosocial support in accordance with patient values"},
            {"id": "D", "text": "Discharging the patient into independent living without any psychiatric or physical follow-up"}
        ],
        "correctAnswer": "C",
        "explanation": "For patients with Severe and Enduring Eating Disorders / Anorexia Nervosa (SEED-AN) who have experienced decades of treatment failure and multiple involuntary refeedings, a palliative psychiatric approach focuses on harm reduction, compassionate symptom control, preserving autonomy, maintaining nutritional stability sufficient to prevent acute death, and optimizing psychosocial quality of life rather than coercive weight restoration.",
        "incorrectExplanations": {
            "A": "Palliative care is active, compassionate life-affirming symptom management, not abandonment or active euthanasia.",
            "B": "Enforcing coercive feeding reflects the curative/re-feeding paradigm that has repeatedly failed and caused iatrogenic trauma.",
            "D": "Abandonment without community support violates clinical duty of care and leads to rapid death."
        },
        "learningObjective": "Define the principles and clinical goals of palliative psychiatric care in severe and enduring anorexia nervosa (SEED-AN).",
        "reference": "Wonderlich, S. et al. (2012). Severe and Enduring Anorexia Nervosa: Update and Guidelines. International Journal of Eating Disorders; Robinson, P. (2014). Severe and Enduring Eating Disorders.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1086",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Foundation",
        "questionText": "Under mental capacity legislation (such as the Mental Capacity Act 2005 in England & Wales), what criteria must be fulfilled for an Advance Decision to Refuse Treatment (ADRT) regarding life-sustaining treatment to be legally binding?",
        "options": [
            {"id": "A", "text": "It can be made verbally to any junior nurse without documentation"},
            {"id": "B", "text": "It must be witnessed and signed by a High Court judge and the local mayor"},
            {"id": "C", "text": "It is valid only if created after the individual has lost mental capacity"},
            {"id": "D", "text": "It must be in writing, signed, witnessed, explicitly state that it applies even if life is at risk, and the author must have possessed mental capacity at the time of its creation and not withdrawn it"}
        ],
        "correctAnswer": "D",
        "explanation": "Under Section 25 of the Mental Capacity Act 2005, an Advance Decision to Refuse Treatment (ADRT) that encompasses life-sustaining treatment must: be in writing; be signed by the person (or by another person in their presence and by their direction); be witnessed; contain an explicit statement that it applies 'even if life is at risk'; and have been made when the individual was 18 or older and possessed full mental capacity to make the decision.",
        "incorrectExplanations": {
            "A": "Refusal of life-sustaining treatment cannot be verbal; it must be written, signed, and witnessed.",
            "B": "Judges and mayors are not required; standard independent adult witnesses suffice.",
            "C": "An ADRT can only be created by an individual while they currently possess mental capacity."
        },
        "learningObjective": "Identify statutory criteria for valid and applicable Advance Decisions to Refuse Treatment (ADRT).",
        "reference": "Mental Capacity Act 2005 (c.9) Sections 24-26; Office of the Public Guardian (OPG) Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1087",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Intermediate",
        "questionText": "A 79-year-old resident with advanced Alzheimer's dementia who has lost verbal communication skills displays grimacing, clenching of fists, groaning during repositioning, and resistance to morning care. Which validated observational tool should the mental health nurse utilize to assess pain objectively?",
        "options": [
            {"id": "A", "text": "PAINAD (Pain Assessment in Advanced Dementia) or Abbey Pain Scale"},
            {"id": "B", "text": "The Visual Analog Scale (VAS) 0-10 self-report ruler"},
            {"id": "C", "text": "The Positive and Negative Syndrome Scale (PANSS)"},
            {"id": "D", "text": "The Alcohol Use Disorders Identification Test (AUDIT)"}
        ],
        "correctAnswer": "A",
        "explanation": "In non-verbal patients with advanced dementia, self-report scales (like the Visual Analog Scale or Numerical Rating Scale) are invalid because the patient cannot conceptualize or communicate the numerical score. Validated observational behavioral pain tools, such as the PAINAD (Pain Assessment in Advanced Dementia) scale or the Abbey Pain Scale, assess breathing, vocalization, facial expression, body language, and consolability.",
        "incorrectExplanations": {
            "B": "Self-report VAS requires abstract numerical comprehension that is lost in severe dementia.",
            "C": "The PANSS assesses schizophrenia psychopathology, not somatic pain.",
            "D": "The AUDIT screens for alcohol misuse."
        },
        "learningObjective": "Select and utilize validated behavioral pain assessment tools for individuals with non-verbal advanced dementia.",
        "reference": "Warden, V. et al. (2003). Development and Psychometric Evaluation of the Pain Assessment in Advanced Dementia (PAINAD) Scale. JAMDA; British Pain Society Dementia Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1088",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Intermediate",
        "questionText": "In end-stage dementia complicated by progressive oropharyngeal dysphagia and recurrent choking episodes, what does the clinical evidence indicate regarding the placement of a percutaneous endoscopic gastrostomy (PEG) feeding tube versus assisted oral 'comfort feeding'?",
        "options": [
            {"id": "A", "text": "PEG feeding tubes dramatically increase survival by 5 to 10 years and completely eliminate aspiration pneumonia"},
            {"id": "B", "text": "PEG tube placement does not prolong survival, does not prevent aspiration pneumonia, increases the risk of pressure ulcers, agitation, and mechanical restraint use, whereas careful hand comfort feeding promotes dignity, taste sensation, and quality of life"},
            {"id": "C", "text": "Comfort feeding is considered active euthanasia and is prohibited in residential memory care units"},
            {"id": "D", "text": "PEG tube insertion is mandatory under international human rights law for every person with dysphagia"}
        ],
        "correctAnswer": "B",
        "explanation": "Extensive empirical research and consensus guidelines (American Geriatrics Society, British Geriatrics Society, NICE) demonstrate that enteral tube feeding (PEG tubes) in advanced dementia does NOT prolong survival, improve nutritional status, heal pressure ulcers, or prevent aspiration pneumonia (since oral secretions are still aspirated). Furthermore, tube feeding frequently causes discomfort, agitation, and the use of physical/chemical restraints. Careful, assisted hand-feeding for comfort ('comfort feeding') is the standard of care.",
        "incorrectExplanations": {
            "A": "PEG tubes do not prevent aspiration of oral secretions and do not prolong life in advanced dementia.",
            "C": "Careful comfort feeding is compassionate palliative care, not euthanasia.",
            "D": "Tube feeding is an invasive medical procedure requiring capacity/best-interests justification; it is never legally mandatory."
        },
        "learningObjective": "Critically analyze evidence regarding artificial enteral nutrition (PEG) versus comfort feeding in advanced end-stage dementia.",
        "reference": "American Geriatrics Society (AGS) Ethics Committee (2014). Feeding Tubes in Advanced Dementia. Journal of the American Geriatrics Society; NICE NG97.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1089",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Intermediate",
        "questionText": "During the final days of life of a patient with terminal neurodegenerative disease in an inpatient psychiatric hospice environment, the patient develops severe terminal agitation, purposeless motor movements, moaning, and distress unresponsive to non-pharmacological positioning. Which pharmacological palliative regimen is standard for managing terminal restlessness?",
        "options": [
            {"id": "A", "text": "Subcutaneous continuous infusion of midazolam (a short-acting benzodiazepine) alone or combined with levomepromazine (an antipsychotic with strong sedative and antiemetic properties)"},
            {"id": "B", "text": "Intravenous bolus infusions of methylphenidate to restore cortical alertness"},
            {"id": "C", "text": "Oral fluoxetine 80 mg daily administered via crushed tablets"},
            {"id": "D", "text": "Intramuscular flumazenil every 30 minutes"}
        ],
        "correctAnswer": "A",
        "explanation": "Terminal restlessness and agitated delirium at the end of life cause profound suffering for the patient and family. Standard palliative care protocols utilize subcutaneous syringe drivers delivering a combination of a sedative benzodiazepine (such as midazolam) and an atypical or sedating first-generation antipsychotic (such as levomepromazine or haloperidol) to achieve calm, relieve distress, and provide peaceful end-of-life comfort.",
        "incorrectExplanations": {
            "B": "Methylphenidate is a central stimulant that worsens agitation, delirium, and tachycardia.",
            "C": "Oral fluoxetine takes weeks to act, cannot be absorbed reliably, and provides no immediate sedation or comfort.",
            "D": "Flumazenil is a benzodiazepine antagonist that would provoke acute withdrawal agitation and panic."
        },
        "learningObjective": "Manage terminal agitation and restlessness in palliative psychiatric care using appropriate subcutaneous regimens.",
        "reference": "National Institute for Health and Care Excellence (NICE) NG31: Care of dying adults in the last days of life (2015); Oxford Textbook of Palliative Medicine.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1090",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Intermediate",
        "questionText": "A palliative mental health nurse is administering subcutaneous morphine and midazolam to relieve intractable dyspnea and distress in an end-stage patient. A student nurse asks whether this medication might hasten the patient's death. How does the ethical 'Doctrine of Double Effect' apply to this clinical situation?",
        "options": [
            {"id": "A", "text": "The doctrine prohibits the administration of any opioids if there is even a theoretical possibility of secondary respiratory depression"},
            {"id": "B", "text": "The doctrine allows clinicians to deliberately cause patient death as long as verbal consent was provided"},
            {"id": "C", "text": "The doctrine holds that an action having two foreseeable effects (one good: relieving intractable pain/distress; one bad: potential slight shortening of life) is morally and legally permissible, provided the primary intention is the good effect, the bad effect is not the means to the good, and the clinical need is proportionate"},
            {"id": "D", "text": "The doctrine applies only to organ transplantation protocols"}
        ],
        "correctAnswer": "C",
        "explanation": "The Doctrine of Double Effect is a foundational ethical and legal principle in palliative care. It justifies providing adequate doses of analgesics and sedatives to alleviate severe, unremitting suffering, even if a foreseeable secondary consequence might be the shortening of life, provided that the clinician's intention is solely to relieve pain/distress, the death of the patient is not the chosen means of achieving relief, and the severity of suffering justifies the clinical risk.",
        "incorrectExplanations": {
            "A": "If opioids were prohibited due to theoretical risk of respiratory depression, untreated agony would be universal in palliative care.",
            "B": "Double effect strictly prohibits intending or causing death; euthanasia remains legally distinct.",
            "D": "The doctrine is a cornerstone of end-of-life palliative pharmacology, not transplantation."
        },
        "learningObjective": "Apply the ethical Doctrine of Double Effect to end-of-life symptom control and palliative nursing care.",
        "reference": "Beauchamp, T. L. & Childress, J. F. (2019). Principles of Biomedical Ethics (8th Ed.); General Medical Council (GMC) End of Life Care Guidance.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1091",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Advanced",
        "questionText": "When determining whether further aggressive medical interventions (such as continuous mechanical restraint, surgical feeding tubes, or invasive critical care) are clinically 'futile' in end-stage psychiatric conditions, which multidisciplinary governance process ensures ethical integrity?",
        "options": [
            {"id": "A", "text": "Convene a formal Clinical Ethics Committee / multidisciplinary best-interests case conference involving the primary care team, palliative specialists, independent mental capacity advocates (IMCA), and family to balance beneficence, non-maleficence, and patient values"},
            {"id": "B", "text": "Allow the most junior nurse on duty to make the sole determination based on bed occupancy"},
            {"id": "C", "text": "Hold an anonymous ward ballot among all inpatient service users"},
            {"id": "D", "text": "Rely entirely on hospital financial accountants to calculate cost-utility thresholds"}
        ],
        "correctAnswer": "A",
        "explanation": "Determining medical futility and transitioning from curative to palliative goals in chronic severe mental illness is fraught with ethical and clinical complexity. Decisions must never be unilateral; they require comprehensive multidisciplinary case conferences, clinical ethics committee review, independent advocacy (e.g., IMCA), family consultation, and explicit alignment with statutory frameworks (e.g., Mental Capacity Act 2005 Best Interests checklist).",
        "incorrectExplanations": {
            "B": "Unilateral decisions by single junior staff breach clinical governance and legal standards.",
            "C": "Ward ballots breach patient confidentiality and have no legal standing.",
            "D": "Financial considerations must not dictate clinical decisions regarding life-sustaining treatment."
        },
        "learningObjective": "Navigate multidisciplinary ethics committees and best-interests decision-making in palliative psychiatry.",
        "reference": "General Medical Council (GMC) (2010). Treatment and Care Towards the End of Life: Good Practice in Decision Making; Mental Capacity Act 2005.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1092",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Advanced",
        "questionText": "A mental health nurse is supporting the family of a 55-year-old patient who has lived with severe refractory schizophrenia and institutionalization for 35 years and is now dying of metastatic lung cancer. The family expresses guilt, stating: 'We grieved the loss of our brother decades ago when his mind was destroyed by illness, and now we feel awful that we don't have tears left.' What psychological phenomenon is the family describing?",
        "options": [
            {"id": "A", "text": "Antisocial callousness"},
            {"id": "B", "text": "Anticipatory grief and chronic ambiguous loss: where the psychological death of the person as they were known preceded physical death by years, leading to complex, protracted bereavement"},
            {"id": "C", "text": "Shared psychotic delusion (folie à deux)"},
            {"id": "D", "text": "Post-traumatic stress disorder hyperarousal"},
        ],
        "correctAnswer": "B",
        "explanation": "Ambiguous loss (Pauline Boss) occurs when a person is physically present but psychologically absent, as in severe chronic schizophrenia or dementia. Family members experience anticipatory mourning and prolonged chronic grief over decades as they watch their loved one's personality and potential slip away. When physical death approaches, families often experience emotional exhaustion, complicated bereavement, and guilt, requiring validation and supportive psychiatric nursing care.",
        "incorrectExplanations": {
            "A": "The family is experiencing genuine, exhausting grief, not callousness.",
            "C": "Folie à deux is shared delusional psychosis, not normal anticipatory mourning.",
            "D": "This presentation lacks PTSD criteria; it is a classic manifestation of chronic ambiguous loss."
        },
        "learningObjective": "Identify and support families experiencing ambiguous loss and anticipatory grief in chronic psychiatric illness.",
        "reference": "Boss, P. (1999). Ambiguous Loss: Learning to Live with Unresolved Grief. Harvard University Press; Bland, R. (2007). Mental Illness and Loss: Families' Experiences.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1093",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Advanced",
        "questionText": "Dame Cicely Saunders introduced the seminal concept of 'Total Pain' in modern palliative medicine. How should a psychiatric nurse apply the Total Pain model when caring for a patient dying with severe comorbid psychiatric and physical disease?",
        "options": [
            {"id": "A", "text": "Focus exclusively on somatic physical nociception and administer only escalating opioid doses"},
            {"id": "B", "text": "Treat only the spiritual dimension by enforcing institutional religious rituals"},
            {"id": "C", "text": "Recognize that the patient's pain experience is a multi-dimensional construct comprising physical symptoms, psychological distress (fear, depression, guilt), social suffering (isolation, stigma, loss of role), and spiritual/existential crises, requiring holistic multidisciplinary interventions across all four domains"},
            {"id": "D", "text": "Classify all psychiatric suffering as imaginary and ignore complaints of pain"}
        ],
        "correctAnswer": "C",
        "explanation": "The 'Total Pain' model (Saunders) recognizes that pain encompasses physical (somatic, visceral, neuropathic), psychological (depression, anxiety, helplessness, anger), social (interpersonal isolation, stigma, financial loss), and spiritual (meaninglessness, existential crisis, loss of faith) dimensions. In psychiatric palliative care, psychological and social pain are frequently profound, amplifying somatic pain; effective relief requires treating all four dimensions.",
        "incorrectExplanations": {
            "A": "Sole reliance on opioids ignores psychological, social, and spiritual sources of distress that do not respond to analgesics.",
            "B": "Imposing religious rituals is coercive and addresses only a narrow aspect of the spiritual domain.",
            "D": "Dismissing pain in psychiatric patients is diagnostic overshadowing that causes severe suffering."
        },
        "learningObjective": "Apply Cicely Saunders' 'Total Pain' framework to psychiatric palliative nursing care.",
        "reference": "Saunders, C. (1967). The Management of Terminal Illness; Clark, D. (1999). 'Total Pain', Disciplinary Power and the Body in the Work of Cicely Saunders. Social Science & Medicine.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1094",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Palliative care in end-stage psychiatric conditions",
        "difficulty": "Expert",
        "questionText": "An 82-year-old patient with severe vascular dementia residing in an EMI (Elderly Mentally Infirm) hospice unit is under 24-hour continuous supervision, is prevented from walking outside unaccompanied due to road danger, and lacks mental capacity to consent to their residence and care arrangements. Under the landmark UK Supreme Court 'Cheshire West' ruling (2014), what is the 'acid test' for determining whether this situation constitutes a Deprivation of Liberty requiring statutory safeguards (DoLS / LPS)?",
        "options": [
            {"id": "A", "text": "Whether the resident actively attempts to jump over the garden fence on a daily basis"},
            {"id": "B", "text": "Whether the resident's relatives submit a written complaint regarding room furnishings"},
            {"id": "C", "text": "Whether the hospice charges more than standard local authority care tariffs"},
            {"id": "D", "text": "Whether the person is subject to continuous supervision and control AND is not free to leave, irrespective of whether the person objects or whether the placement is comfortable and benevolent"}
        ],
        "correctAnswer": "D",
        "explanation": "In the Cheshire West ruling (P v Cheshire West [2014] UKSC 19), Lady Hale articulated the 'acid test' for deprivation of liberty under Article 5 of the European Convention on Human Rights: Is the person under continuous supervision and control AND not free to leave? The court affirmed that benevolence, comfort, lack of objection, or physical disability do not negate a deprivation of liberty; vulnerable people are entitled to the same human rights safeguards as anyone else.",
        "incorrectExplanations": {
            "A": "Active resistance or escape attempts are not required; an unobjecting, compliant bed-bound patient can still be deprived of liberty under the acid test.",
            "B": "Relative complaints are irrelevant to whether a legal deprivation of liberty exists.",
            "C": "Financial tariffs have no bearing on Article 5 human rights law."
        },
        "learningObjective": "Apply the 'acid test' from Cheshire West to identify Deprivation of Liberty in advanced dementia and psychiatric palliative care.",
        "reference": "P v Cheshire West and Chester Council [2014] UKSC 19; Law Commission Mental Capacity and Deprivation of Liberty (2017).",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 9: Personality disorder in acute settings (Q1095 - Q1104)
    # Answers: A, B, C, D, A, B, C, D, A, B
    # Difficulties: F, F, F, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1095",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Foundation",
        "questionText": "According to contemporary clinical guidelines (such as NICE CG78) and recovery-oriented mental health practice, what is the recommended philosophy regarding acute inpatient admissions for individuals with Borderline Personality Disorder (BPD) experiencing acute emotional crisis?",
        "options": [
            {"id": "A", "text": "Admissions should be planned, brief (typically 48 to 72 hours), crisis-focused, and aimed at acute stabilization, because prolonged inpatient stays frequently lead to institutional regression, behavioral escalation, loss of social networks, and increased self-harm"},
            {"id": "B", "text": "Patients should be admitted involuntarily for a minimum of 6 to 12 months in locked wards to eliminate all risk of self-injury"},
            {"id": "C", "text": "Inpatient admission is strictly illegal and permanently prohibited under all circumstances"},
            {"id": "D", "text": "Admissions must be open-ended, lasting until the patient guarantees they will never experience suicidal ideation again"}
        ],
        "correctAnswer": "A",
        "explanation": "NICE Guideline CG78 emphasizes that inpatient admissions for borderline personality disorder should be brief, goal-oriented, and negotiated in advance as part of a crisis plan (typically lasting 48-72 hours, rarely exceeding 1-2 weeks). Lengthy, unstructured hospitalizations are counter-therapeutic, promoting regressive dependence, loss of coping skills, institutionalization, contagion of self-harm behaviors, and increased long-term suicide risk.",
        "incorrectExplanations": {
            "B": "Prolonged involuntary admissions cause severe iatrogenic harm and behavioral regression.",
            "C": "Admissions are not illegal; brief respite admissions can be life-saving during acute crises.",
            "D": "Demanding a guarantee of never experiencing suicidal thoughts is unrealistic, unachievable, and invalidates the patient's emotional struggle."
        },
        "learningObjective": "Explain the rationale for brief, crisis-focused inpatient admissions for borderline personality disorder.",
        "reference": "NICE Clinical Guideline CG78: Borderline personality disorder: recognition and management (2009); Royal College of Psychiatrists (2020) CR227.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1096",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Foundation",
        "questionText": "On an acute psychiatric ward, a patient with BPD tells the night nurse: 'The day nurses are cruel, uncaring, and abusive to me. You are the only nurse on this entire unit who actually cares and understands my pain.' The night nurse agrees and secretly extends the patient's curfew without telling the team. What defense mechanism has occurred, and how has the nurse breached professional practice?",
        "options": [
            {"id": "A", "text": "Sublimation; the nurse demonstrated optimal therapeutic attunement"},
            {"id": "B", "text": "Splitting; the patient polarized the team into 'all-good' and 'all-bad', and the nurse colluded with the split by making unilateral rule exceptions rather than maintaining consistent team boundaries"},
            {"id": "C", "text": "Intellectualization; the patient analyzed nursing shift patterns objectively"},
            {"id": "D", "text": "Reaction formation; the nurse acted out unresolved sibling rivalry"}
        ],
        "correctAnswer": "B",
        "explanation": "Splitting is a primitive defense mechanism where individuals view others, themselves, or the world in polarized, dichotomous terms (all-good or all-bad) because they cannot integrate contradictory qualities. In inpatient settings, splitting causes severe staff conflict, polarization, and team resentment. Effective nursing care requires consistent team communication, adhering to unified care plans, avoiding unilateral exceptions, and bringing splitting dynamics to team handovers.",
        "incorrectExplanations": {
            "A": "Sublimation is a mature defense mechanism (channeling drives into constructive activities); secretly breaking ward rules is a boundary failure.",
            "C": "Intellectualization involves excessive abstract cognitive reasoning, not emotional polarization.",
            "D": "Reaction formation is converting unwanted feelings into their opposite; the primary dynamic here is splitting and staff collusion."
        },
        "learningObjective": "Recognize splitting in acute inpatient wards and maintain unified multidisciplinary boundary consistency.",
        "reference": "Gunderson, J. G. (2008). Borderline Personality Disorder: A Clinical Guide (2nd Ed.); Linehan, M. M. (1993).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1097",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Foundation",
        "questionText": "In Dialectical Behavior Therapy (DBT), what does the acronym 'TIPP' represent when teaching acute distress tolerance skills to a patient experiencing overwhelming emotional dysregulation and urges to self-harm?",
        "options": [
            {"id": "A", "text": "Timed Isolation, Passive Processing, and Parentification"},
            {"id": "B", "text": "Transference Interpretation, Psychoanalytic Projection, and Pharmacotherapy"},
            {"id": "C", "text": "Temperature (e.g., cold water face immersion), Intense exercise, Paced breathing, and Paired muscle relaxation"},
            {"id": "D", "text": "Total Inpatient Protection Protocol"}
        ],
        "correctAnswer": "C",
        "explanation": "In DBT distress tolerance skills (Linehan), TIPP skills rapidly reduce extreme physiological autonomic arousal: T = Temperature change (activating the mammalian dive reflex via cold water or ice to slow heart rate); I = Intense exercise (burning off fight-or-flight energy); P = Paced breathing (slow deep diaphragmatic breathing, breathing out longer than in); P = Paired muscle relaxation (tensing and deliberately relaxing muscle groups).",
        "incorrectExplanations": {
            "A": "Isolation and passive processing are not DBT skills and can exacerbate distress.",
            "B": "Transference interpretation belongs to psychoanalytic therapy, not DBT behavioral distress tolerance.",
            "D": "Total Inpatient Protection Protocol is a fictitious coercive construct."
        },
        "learningObjective": "Teach and coach DBT distress tolerance skills (TIPP) during acute emotional crises.",
        "reference": "Linehan, M. M. (2014). DBT Skills Training Manual (2nd Ed.). Guilford Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1098",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Intermediate",
        "questionText": "In Mentalization-Based Treatment (MBT, Bateman & Fonagy), what is meant by the mental health nurse adopting a 'not-knowing stance' during interactions with a patient in crisis?",
        "options": [
            {"id": "A", "text": "Pretending to have zero professional knowledge or nursing qualifications"},
            {"id": "B", "text": "Refusing to read the patient's medical records or handover notes"},
            {"id": "C", "text": "Assuming a stance of genuine, non-judgmental curiosity and openness about the patient's internal mental state, avoiding premature assumptions about what the patient thinks or feels, and actively collaborating to explore their experience"},
            {"id": "D", "text": "Feigning confusion whenever the patient asks for medication"}
        ],
        "correctAnswer": "C",
        "explanation": "In MBT, mentalizing is the capacity to interpret and understand behavior in terms of underlying mental states (needs, desires, feelings, beliefs). When patients lose mentalizing capacity during acute affective arousal, clinicians must avoid 'knowing' or assuming what the patient thinks ('You're just angry because...'). The 'not-knowing stance' is an open, curious, inquisitive, and transparent posture that models mentalizing and invites the patient to explore their own mind collaboratively.",
        "incorrectExplanations": {
            "A": "It is a reflective psychotherapeutic technique, not pretending to lack medical qualifications.",
            "B": "Nurses must remain fully informed about risk, clinical history, and handovers.",
            "D": "Feigning confusion is manipulative and damages the therapeutic alliance."
        },
        "learningObjective": "Demonstrate the 'not-knowing stance' of Mentalization-Based Treatment (MBT) to restore mentalizing capacity.",
        "reference": "Bateman, A. & Fonagy, P. (2016). Mentalization-Based Treatment for Borderline Personality Disorder: A Practical Guide. Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1099",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Intermediate",
        "questionText": "A patient with severe borderline personality disorder inflicts superficial lacerations on their forearm in their ward bedroom. How should the mental health nurse respond immediately following this self-harm incident to maintain therapeutic boundaries and avoid inadvertently reinforcing self-injurious behavior?",
        "options": [
            {"id": "A", "text": "Provide calm, matter-of-fact, compassionate first-aid and wound care without emotional drama, moralizing, or punitive withdrawal, followed later by a collaborative behavioral chain analysis once the patient is emotionally stable"},
            {"id": "B", "text": "Gather five staff members into the room to deliver an impassioned emotional lecture on how much pain the patient causes the ward staff"},
            {"id": "C", "text": "Withhold all analgesia and suture without local anesthetic to deter future cutting"},
            {"id": "D", "text": "Offer hot chocolate, special treats, and 3 hours of exclusive 1:1 attention immediately following the cutting"}
        ],
        "correctAnswer": "A",
        "explanation": "Responding to self-harm requires a balanced, calm, matter-of-fact approach. The nurse provides gentle, professional wound care with dignity, avoiding both punitive hostility (which causes shame and triggers further cutting) and excessive dramatic secondary gain (such as sudden lavishing of attention, sweets, or privileges that operantly reinforces self-harm as the only way to obtain connection). Once stabilized, a functional chain analysis explores the sequence of thoughts and feelings.",
        "incorrectExplanations": {
            "B": "Emotional lectures fuel intense shame, guilt, and escalation of self-harming behavior.",
            "C": "Withholding local anesthesia is cruel, unethical, illegal, and constitutes battery/assault.",
            "D": "Lavishing special rewards and unearned privileges operantly conditions self-harm as an effective communication tool."
        },
        "learningObjective": "Implement therapeutic, non-punitive, and non-reinforcing nursing responses to acute inpatient self-harm.",
        "reference": "NICE Guideline CG16: Self-harm in over 8s: short-term management and prevention (2004/2022); Linehan, M. M. (1993).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1100",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Intermediate",
        "questionText": "What does NICE Clinical Guideline CG78 explicitly state regarding the routine use of psychotropic medications for the primary treatment of Borderline Personality Disorder?",
        "options": [
            {"id": "A", "text": "Every patient with BPD must be prescribed at least two antipsychotics, an SSRI, and a mood stabilizer indefinitely"},
            {"id": "B", "text": "High-dose long-term benzodiazepine therapy is the gold-standard treatment for emotional lability"},
            {"id": "C", "text": "Drug treatment should not be used routinely for borderline personality disorder or for the individual symptoms or behavior associated with the disorder (such as repeated self-harm, emotional instability, or impulsivity)"},
            {"id": "D", "text": "Stimulant medications are mandatory to enhance prefrontal executive control in all personality disorders"}
        ],
        "correctAnswer": "C",
        "explanation": "NICE Guideline CG78 explicitly advises that drug treatment should NOT be used routinely for borderline personality disorder or for the individual symptoms or behavior associated with the disorder (e.g., emotional instability, chronic suicidal ideation, self-harm). While short-term medication (rarely exceeding 1-2 weeks) may occasionally be used during acute crises or to treat comorbid Axis I disorders (e.g., major depressive episode), evidence shows no long-term benefit and significant risks of polypharmacy and overdose.",
        "incorrectExplanations": {
            "A": "Routine polypharmacy in BPD is contrary to evidence-based practice and increases toxicity and mortality.",
            "B": "Benzodiazepines cause behavioral disinhibition, rapid tolerance, severe dependence, and are contraindicated for long-term BPD management.",
            "D": "Stimulants are not indicated for BPD traits."
        },
        "learningObjective": "Articulate evidence-based guideline recommendations regarding the limited role of psychotropics in borderline personality disorder.",
        "reference": "NICE Clinical Guideline CG78: Borderline personality disorder (2009); Stoffers-Winterling, J. et al. (2020). Pharmacotherapy for BPD. Cochrane Database of Systematic Reviews.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1101",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Advanced",
        "questionText": "In Transference-Focused Psychotherapy (TFP) and psychodynamic formulations of severe personality organization (Kernberg), how is 'projective identification' recognized in ward interactions?",
        "options": [
            {"id": "A", "text": "The patient identifies with historical political figures and quotes their speeches verbatim"},
            {"id": "B", "text": "The patient projects an intolerable, disowned aspect of their own internal emotional state (such as intense vulnerability, terror, or murderous rage) onto the nurse, and unconsciously pressures the nurse to experience and act out that exact emotional state"},
            {"id": "C", "text": "The patient copies the nurse's hairstyle and clothing to seek approval"},
            {"id": "D", "text": "The patient develops amnesia for all events occurring during daylight hours"}
        ],
        "correctAnswer": "B",
        "explanation": "Projective identification (Klein, Kernberg, Bion) is a complex defense mechanism in which a patient unconsciously attributes an unbearable part of themselves (e.g., helplessness, sadistic rage, panic) onto an external other (the nurse), and subtly behaves in ways that manipulate or provoke the other into feeling and enacting those exact feelings. Recognizing this dynamic enables the nurse to process the feeling reflectively rather than retaliating or acting out.",
        "incorrectExplanations": {
            "A": "Quoting political figures is delusional identification or eccentric communication.",
            "C": "Imitating clothing is simple behavioral mimicry or idealization.",
            "D": "Amnesia for daytime events is a dissociative symptom, not projective identification."
        },
        "learningObjective": "Analyze projective identification and countertransference reactions in acute psychiatric nursing practice.",
        "reference": "Kernberg, O. F. (1984). Severe Personality Disorders: Psychotherapeutic Strategies. Yale University Press; Bateman & Holmes (2000).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1102",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Advanced",
        "questionText": "A newly qualified nurse admits to a senior mentor: 'Every time I work with that patient with BPD, I feel completely incompetent, intensely angry, and tempted to walk off the shift. I'm afraid I'm a terrible nurse.' How should the mentor reframe and guide the nurse's countertransference?",
        "options": [
            {"id": "A", "text": "Confirm that experiencing anger proves the nurse is unsuited for psychiatric practice and recommend career change"},
            {"id": "B", "text": "Advise the nurse to swallow their feelings and pretend to be extremely cheerful and agreeable at all times"},
            {"id": "C", "text": "Reframe the nurse's intense emotional reaction as valuable clinical data reflecting the patient's internal chaos and projected distress, and use reflective supervision to process these feelings safely without acting them out"},
            {"id": "D", "text": "Instruct the nurse to confront the patient immediately and accuse them of emotional manipulation"}
        ],
        "correctAnswer": "C",
        "explanation": "Countertransference is a universal, highly informative phenomenon in mental health nursing. When working with severe personality pathology, intense countertransferential feelings (anger, impotence, rescue fantasies, dread) reflect the patient's projective processes and internal torment. A skilled supervisor normalizes these reactions as valuable diagnostic data, helping the nurse understand what the patient is experiencing without retaliating or abandoning boundaries.",
        "incorrectExplanations": {
            "A": "Experiencing countertransference is normal and universal; it does not indicate incompetence or unsuitability.",
            "B": "Superficial cheerfulness ('inauthentic smiling') suppresses feelings that eventually burst into cynical burn-out or punitive behavior.",
            "D": "Aggressive confrontation damages rapport and retraumatizes the patient."
        },
        "learningObjective": "Utilize clinical supervision to transform intense countertransference into therapeutic insight.",
        "reference": "Bowers, L. (2014). Association Between Staff Countertransference and Conflict on Psychiatric Wards. Journal of Advanced Nursing; NMC Code (2018).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1103",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Advanced",
        "questionText": "Structured Clinical Management (SCM, Bateman & Krawitz) is widely implemented across psychiatric services. What are the core organizational principles of an effective SCM inpatient ward framework?",
        "options": [
            {"id": "A", "text": "A generalist, team-based approach combining clear treatment contracts, psychoeducation, consistent interprofessional communication, problem-solving, active crisis planning, and proactive management of self-harm without requiring intensive specialist psychotherapists"},
            {"id": "B", "text": "Enforcing 24-hour video surveillance and mandatory daily polygraph testing"},
            {"id": "C", "text": "Replacing all registered nurses with psychodynamic psychoanalysts delivering 5 sessions per day"},
            {"id": "D", "text": "Prohibiting all discussions of emotions, focusing exclusively on physical fitness and manual labor"}
        ],
        "correctAnswer": "A",
        "explanation": "Structured Clinical Management (SCM) is an evidence-based general psychiatric framework designed for mainstream mental health teams. It emphasizes a consistent, reliable structure: transparent treatment contracts, crisis plans, proactive risk management, psychoeducation, practical problem-solving, clear boundaries, and team supervision. SCM achieves clinical outcomes comparable to specialized treatments (like MBT or DBT) using existing nursing and psychiatric staff.",
        "incorrectExplanations": {
            "B": "Polygraphs and continuous intrusive surveillance violate basic rights and promote paranoia.",
            "C": "SCM was specifically designed to be delivered by general mental health nurses and psychiatrists, not specialized psychoanalysts.",
            "D": "SCM emphasizes processing emotional crises constructively, not suppressing emotional dialogue."
        },
        "learningObjective": "Explain the organizational framework and clinical components of Structured Clinical Management (SCM).",
        "reference": "Bateman, A. & Krawitz, R. (2013). Borderline Personality Disorder: An Evidence-Based Guide for Generalist Mental Health Professionals. Oxford University Press.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1104",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Personality disorder in acute settings",
        "difficulty": "Expert",
        "questionText": "A qualitative audit reveals that ward staff frequently use pejorative labels such as 'attention-seeking', 'manipulative', and 'frequent flyer' in nursing handovers for patients with complex trauma and personality disorder diagnoses. How should the clinical nurse leader dismantle this culture and shift toward trauma-informed co-production?",
        "options": [
            {"id": "A", "text": "Immediately issue disciplinary dismissal warnings to all nurses on the unit"},
            {"id": "B", "text": "Facilitate reflective practice sessions and trauma-informed training to reframe behaviors from 'manipulative' to 'distress-communicating' or 'attachment-seeking', establish co-produced care plans with service users, and enforce respectful, objective documentation standards"},
            {"id": "C", "text": "Ban all nursing progress notes and verbal handovers on the ward"},
            {"id": "D", "text": "Segregate all patients with personality disorder into an isolated wing without staff contact"}
        ],
        "correctAnswer": "B",
        "explanation": "Stigmatizing terminology such as 'attention-seeking' or 'manipulative' dehumanizes patients, justifies punitive neglect, and triggers iatrogenic behavioral escalation. Clinical nurse leaders must reframe behaviors using trauma-informed frameworks—recognizing that so-called 'manipulation' is often a desperate, learned survival strategy to communicate intolerable distress and get core attachment needs met. Implementing co-production, reflective practice, and objective language shifts ward culture toward recovery.",
        "incorrectExplanations": {
            "A": "Punitive dismissal threats create a toxic defensive culture that deepens cynicism and worsens care.",
            "C": "Banning notes and handovers eliminates clinical safety and destroys continuity of care.",
            "D": "Segregation into isolated wings is regressive, stigmatizing, and abusive."
        },
        "learningObjective": "Lead clinical cultural change to eliminate pejorative labeling and embed trauma-informed care for personality disorders.",
        "reference": "Royal College of Psychiatrists (2020). Services for People Diagnosable with Personality Disorder (CR227); NMC Code (2018).",
        "contentReviewStatus": "Peer Reviewed"
    },

    # -------------------------------------------------------------
    # Topic 10: Complex trauma and dissociation (Q1105 - Q1114)
    # Answers: C, D, A, B, C, D, A, B, C, D
    # Difficulties: F, F, I, I, I, I, Adv, Adv, Adv, Exp
    # -------------------------------------------------------------
    {
        "id": "MHN-Q1105",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Foundation",
        "questionText": "In the World Health Organization's ICD-11 classification, how is Complex Post-Traumatic Stress Disorder (Complex PTSD) formally distinguished from standard PTSD?",
        "options": [
            {"id": "A", "text": "Complex PTSD requires proof of head trauma causing structural brain lesions on MRI"},
            {"id": "B", "text": "Complex PTSD occurs only in combat veterans who have experienced blast injuries"},
            {"id": "C", "text": "Complex PTSD requires all three core elements of PTSD (re-experiencing, avoidance, persistent sense of threat) PLUS the 'Disturbances in Self-Organization' (DSO) triad: severe affect dysregulation, persistent negative self-concept (feelings of worthlessness/shame), and severe difficulties in sustaining interpersonal relationships"},
            {"id": "D", "text": "Complex PTSD is identical to schizophrenia and requires lifetime antipsychotic therapy"}
        ],
        "correctAnswer": "C",
        "explanation": "ICD-11 established Complex PTSD as a distinct diagnostic entity resulting from severe, prolonged, or repetitive traumatic events from which escape is difficult or impossible (e.g., childhood abuse, domestic captivity). It encompasses the 3 core PTSD symptoms (re-experiencing in the present, avoidance of reminders, persistent perception of threat) PLUS the 3 'Disturbances in Self-Organization' (DSO) features: (1) severe affect dysregulation, (2) persistent beliefs about oneself as diminished, defeated, or worthless accompanied by deep shame, and (3) pervasive difficulties in sustaining relationships and feeling close to others.",
        "incorrectExplanations": {
            "A": "Complex PTSD is a psychological trauma-related disorder, not structural traumatic brain injury.",
            "B": "Combat trauma is only one etiology; developmental abuse, neglect, human trafficking, and domestic violence are major causes.",
            "D": "Complex PTSD is not a psychotic disorder, though severe dissociative flashbacks can be mistaken for hallucinations."
        },
        "learningObjective": "Identify the ICD-11 diagnostic criteria separating Complex PTSD from standard PTSD.",
        "reference": "World Health Organization (WHO) (2018). ICD-11 Clinical Descriptions and Diagnostic Guidelines; Cloitre, M. et al. (2018). The ICD-11 Trauma Questionnaire.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1106",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Foundation",
        "questionText": "The Phase-Based Trauma Treatment model (Judith Herman / ISTSS consensus guidelines) outlines three progressive stages of recovery. What is the PRIMARY nursing focus during Phase 1?",
        "options": [
            {"id": "A", "text": "In-depth trauma narrative processing and recounting graphic details of childhood abuse"},
            {"id": "B", "text": "Vocational retraining and complete termination of all mental health support"},
            {"id": "C", "text": "Hypnotic age regression to uncover repressed memories"},
            {"id": "D", "text": "Establishing safety, stabilization, emotional regulation skills, grounding techniques, and a reliable therapeutic alliance"}
        ],
        "correctAnswer": "D",
        "explanation": "The tri-phasic trauma model (Herman, 1992; ISTSS) structures trauma treatment into: Phase 1: Safety and Stabilization; Phase 2: Processing of Traumatic Memories; and Phase 3: Reconnection and Integration. In acute and inpatient nursing settings, the priority is almost exclusively Phase 1: creating physical and psychological safety, teaching affect regulation, practicing grounding skills, building trust, and stopping self-harm. Attempting deep trauma memory processing (Phase 2) prior to establishing stabilization leads to severe destabilization.",
        "incorrectExplanations": {
            "A": "Recounting graphic trauma memories belongs to Phase 2 and is destabilizing if initiated prematurely without coping skills.",
            "B": "Vocational reintegration belongs to Phase 3 (Reconnection).",
            "C": "Hypnotic age regression is clinically hazardous, unreliable, and contradicts evidence-based stabilization."
        },
        "learningObjective": "Describe the three phases of the Phase-Based Trauma Treatment model with emphasis on Phase 1 nursing stabilization.",
        "reference": "Herman, J. L. (1992). Trauma and Recovery. Basic Books; Cloitre, M. et al. (2012). ISTSS Expert Consensus Treatment Guidelines for Complex PTSD.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1107",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Intermediate",
        "questionText": "In Dan Siegel's 'Window of Tolerance' framework for trauma and autonomic regulation, what behavioral signs indicate that a patient has tipped into 'hypoarousal' (the dorsal vagal freeze state), and how should the nurse intervene?",
        "options": [
            {"id": "A", "text": "The patient exhibits emotional numbness, depersonalization, blank staring, extreme lethargy, mutism, or dissociative stupor; the nurse should use gentle somatic grounding, sensory stimulation (touching textured items, warm blanket), and slow orientation to current reality"},
            {"id": "B", "text": "The patient is screaming, pacing, hyperventilating, and physically aggressive; the nurse should administer immediate intramuscular haloperidol"},
            {"id": "C", "text": "The patient is singing joyfully and engaging with peers; the nurse should restrict them to bed rest"},
            {"id": "D", "text": "The patient is experiencing manic grandiosity; the nurse should initiate high-dose lithium carbonate"}
        ],
        "correctAnswer": "A",
        "explanation": "The 'Window of Tolerance' describes the zone of optimal autonomic arousal where a person can function and process emotions. Hyperarousal (sympathetic fight-or-flight) involves panic, rage, racing thoughts, and trembling. Hypoarousal (dorsal vagal parasympathetic shutdown/freeze) manifests as numbness, flat affect, dissociation, depersonalization, brain fog, and psychomotor immobility. For hypoarousal, the nurse gently stimulates the nervous system back into the window using sensory grounding.",
        "incorrectExplanations": {
            "B": "Screaming, pacing, and hyperventilation are manifestations of hyperarousal, not hypoarousal.",
            "C": "Joyful singing and social engagement reflect regulation within the window of tolerance.",
            "D": "Manic grandiosity is an affective pole, not the traumatic dorsal vagal freeze response."
        },
        "learningObjective": "Differentiate hyperarousal and hypoarousal within the Window of Tolerance and apply phase-appropriate grounding interventions.",
        "reference": "Siegel, D. J. (1999). The Developing Mind. Guilford Press; Ogden, P. et al. (2006). Trauma and the Body: A Sensorimotor Approach to Psychotherapy.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1108",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Intermediate",
        "questionText": "A 33-year-old inpatient with Dissociative Identity Disorder (DID) suddenly begins speaking with the voice, vocabulary, and terrified posture of a 6-year-old child ('an alter part'), stating that 'the monster is coming.' How should the mental health nurse therapeutically respond during this dissociative switch?",
        "options": [
            {"id": "A", "text": "Confront the patient sternly that they are an adult and demand that they stop playing games immediately"},
            {"id": "B", "text": "Respond in a calm, soothing, age-appropriate, reassuring tone, validating the fear, orienting the part to the present date, adult age, and safe hospital room, without reinforcing dramatic elaboration or acting out the trauma dynamic"},
            {"id": "C", "text": "Bring toys and diapers into the room and agree to become the child's new biological mother"},
            {"id": "D", "text": "Administer emergency rapid tranquilisation to suppress the child alter"}
        ],
        "correctAnswer": "B",
        "explanation": "In Dissociative Identity Disorder (ISSTD guidelines), nursing care requires calm, respectful, stabilizing engagement. When a child alter emerges in distress, the nurse responds with compassionate, reassuring, and gentle verbal communication, validating the emotional distress while grounding the patient in the 'here-and-now' (e.g., 'You are safe here, the year is 2026, you are in a safe hospital, and no one can hurt you'). The nurse avoids both harsh confrontation (which increases terrified dissociation) and infantile over-involvement.",
        "incorrectExplanations": {
            "A": "Harsh confrontation induces panic, deepens dissociation, and retraumatizes the vulnerable patient.",
            "C": "Infantilizing the patient and making promises of adoption breaches professional boundaries and causes harmful regression.",
            "D": "Chemical sedation does not resolve dissociative switching and can cause confusion and trauma flashbacks."
        },
        "learningObjective": "Demonstrate supportive, grounding, and boundary-maintaining nursing interventions during dissociative switches in DID.",
        "reference": "International Society for the Study of Trauma and Dissociation (ISSTD) (2011). Guidelines for Treating Dissociative Identity Disorder in Adults.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1109",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Intermediate",
        "questionText": "How should a psychiatric nurse clinically distinguish a traumatic flashback from an auditory/visual hallucination in a patient with severe Complex PTSD?",
        "options": [
            {"id": "A", "text": "Traumatic flashbacks are accompanied by absolute delusional conviction that the year is 1850 and never resolve"},
            {"id": "B", "text": "Hallucinations only occur when patients are asleep, while flashbacks occur only when running"},
            {"id": "C", "text": "A flashback is an involuntary intrusive reliving of an actual past traumatic event with sensory, affective, and physiological re-enactment ('acting or feeling as if the trauma were recurring right now'); once reoriented and grounded, the patient recognizes it was a past memory, whereas true psychotic hallucinations typically lack this historical reliving quality and are accompanied by persistent delusional explanations"},
            {"id": "D", "text": "Flashbacks always feature olfactory hallucinations of burning rubber"}
        ],
        "correctAnswer": "C",
        "explanation": "Traumatic flashbacks involve vivid sensory re-experiencing where the past intrudes into the present consciousness. During the flashback, the person feels and acts as if the traumatic event is occurring right now, driven by high autonomic arousal. Crucially, once sensory grounding re-establishes contact with the present, reality testing returns, and the person recognizes it was a traumatic memory. In schizophrenia, hallucinations are often continuous, commentating, and bound to fixed non-trauma-related delusional beliefs.",
        "incorrectExplanations": {
            "A": "Delusional beliefs about past centuries are not characteristic of trauma flashbacks.",
            "B": "Hallucinations occur in clear consciousness during waking hours; sleep hallucinations are hypnagogic/hypnopompic.",
            "D": "Burning rubber is an olfactory hallucination seen in uncinate temporal lobe epilepsy, not a defining feature of PTSD."
        },
        "learningObjective": "Differentiate traumatic flashbacks from psychotic hallucinations using phenomenological and reality-testing assessments.",
        "reference": "Brewin, C. R. (2015). Re-experiencing in Posttraumatic Stress Disorder. Journal of Traumatic Stress; ICD-11 Guidelines.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1110",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Intermediate",
        "questionText": "A patient experiencing acute dissociative depersonalization and panic states: 'I can't feel my hands, my body isn't real, and the walls are melting.' Which sensory grounding protocol should the nurse immediately initiate?",
        "options": [
            {"id": "A", "text": "The 5-4-3-2-1 sensory technique (naming 5 things seen, 4 felt, 3 heard, 2 smelled, 1 tasted), coupled with pressing feet firmly onto the floor and holding a cold ice pack"},
            {"id": "B", "text": "Administering high-dose intramuscular ketamine to deepen the dissociation until it clears"},
            {"id": "C", "text": "Instructing the patient to close their eyes and meditate on their earliest traumatic memories"},
            {"id": "D", "text": "Applying a blindfold and noise-cancelling headphones to remove all external sensory stimuli"}
        ],
        "correctAnswer": "A",
        "explanation": "Grounding techniques use the five senses to bring the nervous system out of internal dissociative processing back into physical reality. The '5-4-3-2-1' sensory grounding method engages the frontal cortex and sensory pathways: identifying 5 visual objects, 4 tactile sensations, 3 auditory sounds, 2 olfactory scents, and 1 taste. Physical anchors like holding an ice cube, splashing cold water on the face, or pressing heels firmly into the floor provide strong somatic signals that anchor the patient in the present.",
        "incorrectExplanations": {
            "B": "Ketamine is a dissociative anesthetic that worsens depersonalization and derealization.",
            "C": "Focusing on early trauma memories during acute panic exacerbates terror and dissociation.",
            "D": "Sensory deprivation increases internal hallucinatory and dissociative experiences."
        },
        "learningObjective": "Guide service users through the 5-4-3-2-1 sensory grounding technique to manage acute depersonalization and derealization.",
        "reference": "Najavits, L. M. (2002). Seeking Safety; Fisher, J. (2017). Healing the Fragmented Selves of Trauma Survivors. Routledge.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1111",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Advanced",
        "questionText": "What are the five core universal principles of Trauma-Informed Care (TIC) that every mental health inpatient environment should embody to avoid retraumatizing service users?",
        "options": [
            {"id": "A", "text": "Physical Safety, Trustworthiness & Transparency, Peer Support & Collaboration, Empowerment & Choice, and Cultural, Historical & Gender Responsiveness"},
            {"id": "B", "text": "Surveillance, Strict Hierarchy, Pharmacological Restraint, Mandatory Isolation, and Conformity"},
            {"id": "C", "text": "Cost Containment, Rapid Turnover, Standardized Rules, Uniform Dress Codes, and Paternalism"},
            {"id": "D", "text": "Aversion Therapy, Systematic Desensitization, Psychoanalysis, Hypnosis, and Catharsis"}
        ],
        "correctAnswer": "A",
        "explanation": "Trauma-Informed Care (SAMHSA framework) is based on five core pillars: (1) Safety (physical and psychological safety for patients and staff); (2) Trustworthiness and Transparency (decisions made openly with clear goals); (3) Peer Support and Collaboration (flattening power hierarchies and partnering with service users); (4) Empowerment, Voice, and Choice (validating strengths and supporting autonomy); and (5) Cultural, Historical, and Gender Responsiveness (actively moving past cultural biases).",
        "incorrectExplanations": {
            "B": "Surveillance and coercion are the exact opposite of trauma-informed care and mirror abusive dynamics.",
            "C": "Paternalism and rigid institutional rules strip autonomy and trigger trauma re-enactment.",
            "D": "These are psychotherapeutic techniques, not the organizational principles of trauma-informed care."
        },
        "learningObjective": "Identify and apply the five core principles of Trauma-Informed Care (TIC) in mental health ward design and culture.",
        "reference": "SAMHSA (2014). Concept of Trauma and Guidance for a Trauma-Informed Approach (HHS Publication No. SMA 14-4884).",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1112",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Advanced",
        "questionText": "In Onno van der Hart's Theory of Structural Dissociation of the Personality, how are the 'Apparently Normal Part of the Personality' (ANP) and the 'Emotional Part of the Personality' (EP) differentiated in individuals with complex dissociative conditions?",
        "options": [
            {"id": "A", "text": "The ANP is the biological body, while the EP is an imaginary spiritual ghost"},
            {"id": "B", "text": "The ANP handles daily living, attachment, and adaptive functioning (often maintaining phobic avoidance of trauma memories), while the EP remains fixated in the traumatic past, holding intense trauma memories, survival defense mechanisms (fight, flight, freeze), and overwhelming affect"},
            {"id": "C", "text": "The ANP represents daytime personality, and the EP is only active during rapid eye movement (REM) sleep"},
            {"id": "D", "text": "The ANP is caused by excess dopamine, whereas the EP is caused by a deficiency of GABA"}
        ],
        "correctAnswer": "B",
        "explanation": "The Theory of Structural Dissociation posits that following severe chronic trauma, personality cohesion fails to integrate. The Apparently Normal Part (ANP) operates daily survival systems (work, socializing, parenting) and often phobically avoids anything related to the trauma. The Emotional Part(s) (EP) remain frozen in trauma time, storing the unintegrated sensory impressions, horrific affects, and physiological action systems (fight, flight, freeze, submit) of the traumatic experience.",
        "incorrectExplanations": {
            "A": "Structural dissociation is an unintegrated psychological personality structure, not a spiritual divide.",
            "C": "Both ANP and EP are waking personality systems that can switch or co-exist in intrusion.",
            "D": "Reducing structural dissociation to single neurotransmitter levels ignores psychological and neurobiological integrative failure."
        },
        "learningObjective": "Explain the operational division between ANP and EP in the Theory of Structural Dissociation.",
        "reference": "Van der Hart, O., Nijenhuis, E. R. S., & Steele, K. (2006). The Haunted Self: Structural Dissociation and the Treatment of Chronic Traumatization. W. W. Norton.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1113",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Advanced",
        "questionText": "A psychiatric nurse who has spent 18 months providing intensive 1:1 care for survivors of severe childhood sexual abuse begins experiencing intrusive nightmares of abuse scenes, chronic hypervigilance, profound emotional exhaustion, and a cynical belief that the world is entirely evil. What professional occupational syndrome is the nurse experiencing?",
        "options": [
            {"id": "A", "text": "Vicarious traumatization (secondary traumatic stress), where cumulative empathetic engagement with trauma survivors alters the clinician's own cognitive schemas, worldview, and emotional well-being"},
            {"id": "B", "text": "Factitious disorder by proxy"},
            {"id": "C", "text": "Bipolar I disorder with rapid cycling"},
            {"id": "D", "text": "Organic amnestic syndrome"}
        ],
        "correctAnswer": "A",
        "explanation": "Vicarious traumatization (McCann & Pearlman, 1990; Figley) refers to the profound psychological transformation that occurs in healthcare professionals as a result of empathetic engagement with trauma survivors. Unlike simple burnout (which is general emotional exhaustion from workload), vicarious trauma mirrors PTSD symptoms: intrusive imagery/nightmares of clients' trauma, hyperarousal, dread, and fundamental disruptions in the clinician's core beliefs regarding safety, trust, control, and esteem.",
        "incorrectExplanations": {
            "B": "Factitious disorder by proxy involves intentionally falsifying illness in another person for psychological gratification.",
            "C": "Bipolar rapid cycling features distinct hypomanic and depressive episodes, not trauma-mirroring intrusive imagery.",
            "D": "Organic amnestic syndrome involves memory failure due to brain damage, unrelated to empathic trauma exposure."
        },
        "learningObjective": "Identify symptoms of vicarious traumatization in mental health nurses and differentiate them from general workplace burnout.",
        "reference": "Pearlman, L. A. & Saakvitne, K. W. (1995). Trauma and the Therapist: Countertransference and Vicarious Traumatization in Psychotherapy; NMC Code.",
        "contentReviewStatus": "Peer Reviewed"
    },
    {
        "id": "MHN-Q1114",
        "module": "11. Advanced Clinical Scenarios",
        "topic": "Complex trauma and dissociation",
        "difficulty": "Expert",
        "questionText": "According to Stephen Porges' Polyvagal Theory, which neurobiological hierarchy governs autonomic nervous system responses to perceived mortal threat and safety in traumatized individuals?",
        "options": [
            {"id": "A", "text": "Direct cortical control bypasses the brainstem entirely during fear conditioning"},
            {"id": "B", "text": "The enteric nervous system acts as the sole controller of the flight response"},
            {"id": "C", "text": "Sympathetic arousal operates only during sleep and is suppressed during waking life"},
            {"id": "D", "text": "A phylogenetically ordered hierarchy of three neural circuits: (1) Ventral Vagal complex (social engagement, facial expressivity, vocal prosody, calm); (2) Sympathetic Nervous System (mobilization, fight-or-flight); and (3) Dorsal Vagal complex (unmyelinated, ancient system mediating immobilization, freeze, collapse, and profound dissociation)"}
        ],
        "correctAnswer": "D",
        "explanation": "Polyvagal Theory (Porges) describes three evolutionary tiers of the autonomic nervous system: (1) Ventral Vagal System (newest, myelinated vagus): enables social communication, calm, eye contact, and soothing; (2) Sympathetic Adrenal System: mobilizes fight-or-flight responses when safety is lost; (3) Dorsal Vagal System (oldest, unmyelinated vagus): triggered when fight-or-flight fails or inescapable mortal terror is detected, inducing immobilization, metabolic shutdown, fainting, depersonalization, and profound dissociative freeze.",
        "incorrectExplanations": {
            "A": "During extreme threat, prefrontal cortical control is inhibited ('offline') while evolutionary subcortical brainstem circuits dominate.",
            "B": "The enteric system governs gastrointestinal function, not whole-body flight mobilization.",
            "C": "Sympathetic fight-or-flight is active during daytime waking threat perception."
        },
        "learningObjective": "Explain the Polyvagal Theory hierarchy and the neurobiology of the dorsal vagal dissociative freeze response.",
        "reference": "Porges, S. W. (2011). The Polyvagal Theory: Neurophysiological Foundations of Emotions, Attachment, Communication, and Self-Regulation. W. W. Norton.",
        "contentReviewStatus": "Peer Reviewed"
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(MOD11_PART2)} questions for Module 11 Part 2.")
