# scripts/full_audit.py
import sys, os, re
sys.path.insert(0, os.path.abspath('.'))
from collections import Counter

ts_path = r"src\data\questions_mod5_6.ts"
with open(ts_path, 'r', encoding='utf-8') as f:
    text = f.read()

assert "import { Question } from '../types';" in text
assert "export const MOD5_6_QUESTIONS: Question[] = [" in text

# Import the parsed questions via python
from scripts.compile_and_validate import all_questions

print(f"Auditing {len(all_questions)} questions...")

assert len(all_questions) == 200, f"Expected 200 questions, got {len(all_questions)}"

# IDs check
m5_ids = [q['id'] for q in all_questions[:100]]
m6_ids = [q['id'] for q in all_questions[100:]]

assert m5_ids == [f"MHN-Q{i}" for i in range(415, 515)]
assert m6_ids == [f"MHN-Q{i}" for i in range(515, 615)]

# Module names exact
for q in all_questions[:100]:
    assert q['module'] == "5. Psychotherapy and Therapeutic Communication", f"Invalid module in {q['id']}: {q['module']}"

for q in all_questions[100:]:
    assert q['module'] == "6. Psychiatric Emergencies and Crisis Intervention", f"Invalid module in {q['id']}: {q['module']}"

# Unique questionText
texts = [q['questionText'] for q in all_questions]
assert len(set(texts)) == 200, f"Duplicate question text found: {len(set(texts))} unique"

# Answers distribution
m5_answers = Counter(q['correctAnswer'] for q in all_questions[:100])
m6_answers = Counter(q['correctAnswer'] for q in all_questions[100:])

assert m5_answers == {'A': 25, 'B': 25, 'C': 25, 'D': 25}, f"M5 answers: {m5_answers}"
assert m6_answers == {'A': 25, 'B': 25, 'C': 25, 'D': 25}, f"M6 answers: {m6_answers}"

# Difficulties distribution
m5_diffs = Counter(q['difficulty'] for q in all_questions[:100])
m6_diffs = Counter(q['difficulty'] for q in all_questions[100:])

expected_diffs = {'Foundation': 25, 'Intermediate': 35, 'Advanced': 30, 'Expert': 10}
assert m5_diffs == expected_diffs, f"M5 diffs: {m5_diffs}"
assert m6_diffs == expected_diffs, f"M6 diffs: {m6_diffs}"

# Topics
m5_topics = Counter(q['topic'] for q in all_questions[:100])
m6_topics = Counter(q['topic'] for q in all_questions[100:])

assert len(m5_topics) == 10
assert len(m6_topics) == 10
for t, c in m5_topics.items():
    assert c == 10, f"Topic {t} has count {c}"
for t, c in m6_topics.items():
    assert c == 10, f"Topic {t} has count {c}"

# Options and Explanations
for q in all_questions:
    assert len(q['options']) == 4
    assert [o['id'] for o in q['options']] == ['A', 'B', 'C', 'D']
    opt_texts = [o['text'] for o in q['options']]
    assert len(set(opt_texts)) == 4
    for o in q['options']:
        assert len(o['text'].strip()) > 0
    assert q['correctAnswer'] in ['A', 'B', 'C', 'D']
    assert len(q['explanation'].strip()) > 30
    assert len(q['learningObjective'].strip()) > 15
    assert len(q['reference'].strip()) > 10
    assert q['contentReviewStatus'] == 'Peer Reviewed'
    
    # Check incorrectExplanations
    inc = q['incorrectExplanations']
    expected_inc_keys = {'A', 'B', 'C', 'D'} - {q['correctAnswer']}
    assert set(inc.keys()) == expected_inc_keys, f"Question {q['id']} incorrect keys mismatch: {set(inc.keys())} vs {expected_inc_keys}"
    for k in expected_inc_keys:
        assert len(inc[k].strip()) > 10

print("ALL 16 AUDIT CHECKS PASSED PERFECTLY!")
