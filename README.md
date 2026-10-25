# Postgraduate Mental Health Nursing Examination Preparation Portal
### Associated with West African Postgraduate College of Nurses and Midwives (WAPCNM) Specialty Preparation

An interactive, client-side examination preparation, learning, and self-assessment web portal for postgraduate mental health nursing candidates.

---

## 🌟 Key Features for Testers

- **Complete Curriculum Coverage:** 1,414 peer-reviewed multiple-choice questions across all 14 specialty modules:
  1. Foundations of Mental Health Nursing
  2. Psychiatric Assessment and Mental Status Examination
  3. Psychopathology and Psychiatric Diagnosis
  4. Psychopharmacology and Medication Management
  5. Psychotherapy and Therapeutic Communication
  6. Psychiatric Emergencies and Crisis Intervention
  7. Community Mental Health and Psychiatric Rehabilitation
  8. Child, Adolescent, and Older Adult Mental Health
  9. Psychiatric Nursing Ethics, Law, and Human Rights
  10. Research Methods and Evidence-Based Practice
  11. Advanced Clinical Scenarios
  12. Leadership and Professional Practice
  13. Substance Use Disorders and Dual Diagnosis
  14. Special Populations and Culturally Relevant Practice

- **Immediate Corrective Clinical Feedback:**
  - Selecting an answer immediately reveals whether it is correct or incorrect.
  - If wrong, the candidate's choice is highlighted in red, the correct choice is highlighted in green, and an in-depth clinical explanation with option-by-option rationale is displayed.
  - Includes a "Try Again" option to test recall.

- **Timed Mock Examination (WAPCNM Standard):**
  - Samples a balanced set of 70 questions (5 from each module).
  - 60-minute countdown timer with warnings.
  - Question palette navigation and bookmarking.
  - 70% Pass Mark criterion with detailed result slip generation.

- **Postgraduate Clinical Examination Center (CAOSCE & Clinical Suites):**
  - **6-Station Autonomous CAOSCE Circuit**: Clock-synchronized 120-minute simulation (10-min practical checklist + 10-min scenario MCQs per station) with synthesized 750Hz warning bell and 1000Hz rotation chime via Web Audio API.
  - **Non-Negotiable Red Flag Safety Policy**: Breaching or omitting predefined critical patient safety steps automatically caps practical marks at 49% (Station Referral) with statutory remedial directives.
  - **Specialized Postgraduate Mental Health Stations**:
    1. Acute Psychiatric Emergency, Aggression De-escalation & Rapid Tranquilization
    2. Suicide Risk Stratification (C-SSRS) & Structured Safety Planning
    3. Neuroleptic Malignant Syndrome (NMS) vs Serotonin Toxicity Emergency
    4. Dual Diagnosis & Severe Alcohol Delirium Tremens (CIWA-Ar Protocol)
    5. Forensic Psychiatric Assessment & Mental Health Act Jurisprudence
    6. Perinatal Psychosis, Mother-Infant Safety & Lewy Body Dementia Sensitivity
  - **Next Generation NCLEX (NGN) Clinical Judgment Case Studies**: Unfolding 6-stage clinical decision cases mapped to the NCSBN cognitive framework.
  - **Psychopharmacology Titration & Math Lab**: Practical calculation scenarios including Cockcroft-Gault creatinine clearance for lithium titration, Clozapine ANC REMS monitoring thresholds, long-acting depot conversions, and Bazett QTc interval correction.

- **Offline-First & Local Persistence:**
  - Powered by browser IndexedDB (`WAPCNM_MHN_DB_V2`).
  - No external database or credentials required—runs 100% offline.
  - Saves candidate profile, bookmarks, and automated incorrect-question review queue.

- **Downloadable Assessment Slips:**
  - Complete HTML report export and printable PDF result slips with full question-by-question breakdown.

---

## 🚀 How to Run Locally

### Prerequisites
- [Node.js](https://nodejs.org/) (v18 or newer)
- npm (installed with Node)

### Installation & Launch
```bash
# 1. Install dependencies
npm install

# 2. Start the development server
npm run dev
```

Open your browser at `http://localhost:3000` (or the port shown in terminal).

### Production Build
```bash
# Type check and build static assets for production deployment
npm run lint
npm run build
```
The compiled static assets will be output in `dist/`, ready to be hosted on GitHub Pages, Vercel, Netlify, or any static hosting service.

---

## 🧪 Tester Feedback Checklist

When testing the portal, please verify:
1. **Module Practice Flow:** Does starting a module display questions with accurate topics and immediate answer explanations?
2. **Incorrect Question Handling:** Does answering incorrectly show the red/green indicators, explanation, and add the question to **Bookmarks & Review**?
3. **Timed Mock Exam:** Does launching the mock exam start a 60-minute countdown with 70 balanced questions, and generate a PASS/FAIL result slip upon submission?
4. **Report Export:** Does clicking "Download Complete Report" or "Print / Save as PDF" generate a readable assessment record?
5. **Data Persistence:** Does refreshing the browser retain your saved candidate name, completed test history, and bookmarks?
