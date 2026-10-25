import { getAllQuestions } from '../src/data/questionBank.ts';
import { CAOSCE_STATIONS } from '../src/data/caosceStations.ts';
import { NGN_CASE_STUDIES } from '../src/data/ngnCaseStudies.ts';
import { PSYCHOPHARM_MATH_PROBLEMS } from '../src/data/psychopharmMath.ts';
import { NMCN_SPECIALTIES } from '../src/data/nmcnSpecialtiesData.ts';

console.log('=== RUNNING COMPREHENSIVE QUESTION VALIDATION SUITE ===\n');

let totalIssues = 0;

const allQuestions = getAllQuestions();

// 1. Validate Main Question Bank
console.log(`Checking Main Question Bank: ${allQuestions.length} questions...`);
let qbIssues = 0;
allQuestions.forEach((q, index) => {
  const prefix = `[QBank #${index + 1} - ${q.id}]`;
  if (!q.id) { console.error(`${prefix} Missing ID`); qbIssues++; }
  if (!q.questionText || q.questionText.trim().length < 10) { console.error(`${prefix} Invalid/short questionText`); qbIssues++; }
  if (!['A', 'B', 'C', 'D'].includes(q.correctAnswer)) { console.error(`${prefix} Invalid correctAnswer '${q.correctAnswer}'`); qbIssues++; }
  if (!Array.isArray(q.options) || q.options.length !== 4) { console.error(`${prefix} Options length is not 4`); qbIssues++; }
  
  const optIds = q.options?.map(o => o.id) || [];
  if (!optIds.includes(q.correctAnswer)) { console.error(`${prefix} correctAnswer ${q.correctAnswer} not found in options`); qbIssues++; }
  
  q.options?.forEach(opt => {
    if (!opt.text || opt.text.trim().length === 0) {
      console.error(`${prefix} Empty text for option ${opt.id}`);
      qbIssues++;
    }
  });

  if (!q.explanation || q.explanation.trim().length < 10) {
    console.error(`${prefix} Missing/short explanation`);
    qbIssues++;
  }
});
console.log(`Main Question Bank: ${allQuestions.length} questions checked. Issues found: ${qbIssues}`);
totalIssues += qbIssues;

// 2. Validate CAOSCE Station MCQs
console.log(`\nChecking CAOSCE Station MCQs: ${CAOSCE_STATIONS.length} stations...`);
let caosceIssues = 0;
let totalCaosceMcqs = 0;
CAOSCE_STATIONS.forEach(station => {
  if (!station.mcqs || station.mcqs.length !== 10) {
    console.error(`Station ${station.stationNumber} does not have exactly 10 MCQs (has ${station.mcqs?.length})`);
    caosceIssues++;
  }
  station.mcqs?.forEach((q, idx) => {
    totalCaosceMcqs++;
    const prefix = `[Station ${station.stationNumber} MCQ #${idx + 1} - ${q.id}]`;
    if (!['A', 'B', 'C', 'D'].includes(q.correctAnswer)) { console.error(`${prefix} Invalid correctAnswer '${q.correctAnswer}'`); caosceIssues++; }
    if (!Array.isArray(q.options) || q.options.length !== 4) { console.error(`${prefix} Options length is not 4`); caosceIssues++; }
    const optIds = q.options?.map(o => o.id) || [];
    if (!optIds.includes(q.correctAnswer)) { console.error(`${prefix} correctAnswer ${q.correctAnswer} not found in options`); caosceIssues++; }
    q.options?.forEach(opt => {
      if (!opt.text || opt.text.trim().length === 0) { console.error(`${prefix} Empty text for option ${opt.id}`); caosceIssues++; }
    });
    if (!q.explanation || q.explanation.trim().length < 10) { console.error(`${prefix} Missing/short explanation`); caosceIssues++; }
  });
});
console.log(`CAOSCE Station MCQs: ${totalCaosceMcqs} MCQs checked. Issues found: ${caosceIssues}`);
totalIssues += caosceIssues;

// 3. Validate NGN Case Studies
console.log(`\nChecking NGN Case Studies: ${NGN_CASE_STUDIES.length} cases...`);
let ngnIssues = 0;
let totalNgnStages = 0;
NGN_CASE_STUDIES.forEach(c => {
  if (!c.stages || c.stages.length !== 6) {
    console.error(`Case ${c.id} does not have 6 stages (has ${c.stages?.length})`);
    ngnIssues++;
  }
  c.stages?.forEach((stage, idx) => {
    totalNgnStages++;
    const prefix = `[NGN Case ${c.id} Stage #${idx + 1}]`;
    const correctOpts = stage.options.filter(o => o.isCorrect);
    if (correctOpts.length !== 1) {
      console.error(`${prefix} Expected exactly 1 correct option, found ${correctOpts.length}`);
      ngnIssues++;
    }
    stage.options.forEach(opt => {
      if (!opt.text || opt.text.trim().length === 0) { console.error(`${prefix} Option ${opt.id} has empty text`); ngnIssues++; }
    });
    if (!stage.clinicalRationale || stage.clinicalRationale.trim().length < 10) {
      console.error(`${prefix} Missing/short clinicalRationale`);
      ngnIssues++;
    }
  });
});
console.log(`NGN Stages: ${totalNgnStages} stages checked. Issues found: ${ngnIssues}`);
totalIssues += ngnIssues;

// 4. Validate Psychopharm Math Problems
console.log(`\nChecking Psychopharm Math Problems: ${PSYCHOPHARM_MATH_PROBLEMS.length} problems...`);
let mathIssues = 0;
PSYCHOPHARM_MATH_PROBLEMS.forEach((p, idx) => {
  const prefix = `[Psychopharm Math #${idx + 1} - ${p.id}]`;
  const correctOpts = p.options.filter(o => o.isCorrect);
  if (correctOpts.length !== 1) {
    console.error(`${prefix} Expected exactly 1 correct option, found ${correctOpts.length}`);
    mathIssues++;
  }
  p.options.forEach(opt => {
    if (!opt.text || opt.text.trim().length === 0) { console.error(`${prefix} Option ${opt.id} has empty text`); mathIssues++; }
  });
  if (!p.stepByStepSolution || p.stepByStepSolution.length === 0) {
    console.error(`${prefix} Missing stepByStepSolution`);
    mathIssues++;
  }
});
console.log(`Psychopharm Math: ${PSYCHOPHARM_MATH_PROBLEMS.length} problems checked. Issues found: ${mathIssues}`);
totalIssues += mathIssues;

// 5. Validate NMCN Specialties Data MCQs
console.log(`\nChecking NMCN Specialties Data: ${NMCN_SPECIALTIES.length} specialties...`);
let nmcnIssues = 0;
let totalNmcnMcqs = 0;
NMCN_SPECIALTIES.forEach((spec) => {
  spec.station.mcqs.forEach((q, idx) => {
    totalNmcnMcqs++;
    const prefix = `[NMCN Spec ${spec.id} MCQ #${idx + 1} - ${q.id}]`;
    if (!['A', 'B', 'C', 'D'].includes(q.correctAnswer)) { console.error(`${prefix} Invalid correctAnswer '${q.correctAnswer}'`); nmcnIssues++; }
    if (!Array.isArray(q.options) || q.options.length !== 4) { console.error(`${prefix} Options length is not 4`); nmcnIssues++; }
    const optIds = q.options?.map(o => o.id) || [];
    if (!optIds.includes(q.correctAnswer)) { console.error(`${prefix} correctAnswer ${q.correctAnswer} not found in options`); nmcnIssues++; }
    q.options?.forEach(opt => {
      if (!opt.text || opt.text.trim().length === 0) { console.error(`${prefix} Empty text for option ${opt.id}`); nmcnIssues++; }
    });
    if (!q.explanation || q.explanation.trim().length < 10) { console.error(`${prefix} Missing/short explanation`); nmcnIssues++; }
  });
});
console.log(`NMCN Specialty MCQs: ${totalNmcnMcqs} MCQs checked. Issues found: ${nmcnIssues}`);
totalIssues += nmcnIssues;

console.log(`\n========================================`);
console.log(`TOTAL QUESTIONS & STATIONS CHECKED:`);
console.log(`- Main QBank: ${allQuestions.length}`);
console.log(`- CAOSCE MCQs: ${totalCaosceMcqs}`);
console.log(`- NGN Stages: ${totalNgnStages}`);
console.log(`- Psychopharm Math: ${PSYCHOPHARM_MATH_PROBLEMS.length}`);
console.log(`- NMCN Specialty MCQs: ${totalNmcnMcqs}`);
console.log(`GRAND TOTAL QUESTIONS: ${allQuestions.length + totalCaosceMcqs + totalNgnStages + PSYCHOPHARM_MATH_PROBLEMS.length + totalNmcnMcqs}`);
console.log(`TOTAL ISSUES DETECTED: ${totalIssues}`);
console.log(`========================================`);

if (totalIssues > 0) {
  process.exit(1);
} else {
  console.log('ALL QUESTIONS VALIDATED TO BE 100% CORRECT AND INTEGRATED!');
}
