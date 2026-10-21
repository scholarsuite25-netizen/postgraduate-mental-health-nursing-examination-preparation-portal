# scripts/audit_mod11_12.ts audit script
import sys, os, re
sys.path.insert(0, os.path.abspath('.'))
from collections import Counter

ts_path = r"src\data\questions_mod11_12.ts"
with open(ts_path, 'r', encoding='utf-8') as f:
    text = f.read()

assert "import { Question } from '../types';" in text, "Missing import statement"
assert "export const MOD11_12_QUESTIONS: Question[] = [" in text, "Missing export declaration"
assert text.rstrip().endswith("];"), "Missing closing array bracket"

# Check questions via assemble_and_export
from scripts.assemble_and_export import all_questions

print(f"Auditing {len(all_questions)} questions from Module 11 and 12...")
assert len(all_questions) == 200, f"Expected 200 questions, got {len(all_questions)}"

# ID check
m11_ids = [q['id'] for q in all_questions[:100]]
m12_ids = [q['id'] for q in all_questions[100:]]

assert m11_ids == [f"MHN-Q{i}" for i in range(1015, 1115)], f"M11 IDs mismatch: {m11_ids[0]}..{m11_ids[-1]}"
assert m12_ids == [f"MHN-Q{i}" for i in range(1115, 1215)], f"M12 IDs mismatch: {m12_ids[0]}..{m12_ids[-1]}"

# Module names exact
for q in all_questions[:100]:
    assert q['module'] == "11. Advanced Clinical Scenarios", f"Invalid module in {q['id']}: {q['module']}"

for q in all_questions[100:]:
    assert q['module'] == "12. Leadership and Professional Practice", f"Invalid module in {q['id']}: {q['module']}"

# Unique questionText
texts = [q['questionText'].strip().lower() for q in all_questions]
assert len(set(texts)) == 200, f"Duplicate question text found: {len(set(texts))} unique"

# Answers distribution
m11_answers = Counter(q['correctAnswer'] for q in all_questions[:100])
m12_answers = Counter(q['correctAnswer'] for q in all_questions[100:])

assert m11_answers == {'A': 25, 'B': 25, 'C': 25, 'D': 25}, f"M11 answers: {m11_answers}"
assert m12_answers == {'A': 25, 'B': 25, 'C': 25, 'D': 25}, f"M12 answers: {m12_answers}"

# Difficulties distribution
m11_diffs = Counter(q['difficulty'] for q in all_questions[:100])
m12_diffs = Counter(q['difficulty'] for q in all_questions[100:])

expected_diffs = {'Foundation': 25, 'Intermediate': 35, 'Advanced': 30, 'Expert': 10}
assert m11_diffs == expected_diffs, f"M11 diffs: {m11_diffs}"
assert m12_diffs == expected_diffs, f"M12 diffs: {m12_diffs}"

# Topics
m11_topics = Counter(q['topic'] for q in all_questions[:100])
m12_topics = Counter(q['topic'] for q in all_questions[100:])

assert len(m11_topics) == 10, f"Expected 10 topics in M11, got {len(m11_topics)}"
assert len(m12_topics) == 10, f"Expected 10 topics in M12, got {len(m12_topics)}"
for t, c in m11_topics.items():
    assert c == 10, f"Topic {t} has count {c} in M11"
for t, c in m12_topics.items():
    assert c == 10, f"Topic {t} has count {c} in M12"

# Options and Explanations
for q in all_questions:
    assert len(q['options']) == 4, f"Options length != 4 in {q['id']}"
    assert [o['id'] for o in q['options']] == ['A', 'B', 'C', 'D'], f"Option ids != A-D in {q['id']}"
    opt_texts = [o['text'] for o in q['options']]
    assert len(set(opt_texts)) == 4, f"Duplicate option texts in {q['id']}"
    for o in q['options']:
        assert len(o['text'].strip()) > 0, f"Empty option text in {q['id']}"
    assert q['correctAnswer'] in ['A', 'B', 'C', 'D'], f"Invalid correctAnswer in {q['id']}"
    assert len(q['explanation'].strip()) >= 20, f"Short explanation in {q['id']}"
    assert len(q['learningObjective'].strip()) >= 10, f"Short learningObjective in {q['id']}"
    assert len(q['reference'].strip()) >= 5, f"Short reference in {q['id']}"
    assert q['contentReviewStatus'] == 'Peer Reviewed', f"Invalid contentReviewStatus in {q['id']}"
    
    # Check incorrectExplanations
    inc = q['incorrectExplanations']
    expected_inc_keys = {'A', 'B', 'C', 'D'} - {q['correctAnswer']}
    assert set(inc.keys()) == expected_inc_keys, f"Question {q['id']} incorrect keys mismatch: {set(inc.keys())} vs {expected_inc_keys}"
    for k in expected_inc_keys:
        assert len(inc[k].strip()) >= 5, f"Question {q['id']} short incorrect explanation for {k}"

print("ALL 16 AUDIT CHECKS FOR MODULES 11 AND 12 PASSED PERFECTLY!")
