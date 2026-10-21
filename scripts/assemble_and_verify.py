import sys
import os
import json
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__)))
from gen_mod13_t1_t5 import QUESTIONS_T1_T5 as m13_1
from gen_mod13_t6_t10 import QUESTIONS_T6_T10 as m13_2
from gen_mod14_t1_t5 import QUESTIONS_T1_T5_MOD14 as m14_1
from gen_mod14_t6_t10 import QUESTIONS_T6_T10_MOD14 as m14_2

m13 = m13_1 + m13_2
m14 = m14_1 + m14_2
all_questions = m13 + m14

print(f"Total questions: {len(all_questions)}")
assert len(m13) == 100, f"Expected 100 questions in M13, got {len(m13)}"
assert len(m14) == 100, f"Expected 100 questions in M14, got {len(m14)}"

# ID checks
m13_ids = [q['id'] for q in m13]
m14_ids = [q['id'] for q in m14]
expected_m13_ids = [f"MHN-Q{i}" for i in range(1215, 1315)]
expected_m14_ids = [f"MHN-Q{i}" for i in range(1315, 1415)]

assert m13_ids == expected_m13_ids, f"M13 IDs mismatch: {m13_ids[0]}..{m13_ids[-1]}"
assert m14_ids == expected_m14_ids, f"M14 IDs mismatch: {m14_ids[0]}..{m14_ids[-1]}"

# Uniqueness of IDs and Questions
all_ids = [q['id'] for q in all_questions]
assert len(all_ids) == len(set(all_ids)), "Duplicate IDs found!"

all_texts = [q['questionText'].strip().lower() for q in all_questions]
assert len(all_texts) == len(set(all_texts)), "Duplicate question texts found!"

# Check answer distribution
m13_answers = Counter(q['correctAnswer'] for q in m13)
m14_answers = Counter(q['correctAnswer'] for q in m14)
print("M13 answers:", m13_answers)
print("M14 answers:", m14_answers)
assert m13_answers == Counter({'A': 25, 'B': 25, 'C': 25, 'D': 25}), "M13 answer distribution not 25 each"
assert m14_answers == Counter({'A': 25, 'B': 25, 'C': 25, 'D': 25}), "M14 answer distribution not 25 each"

# Check difficulty distribution
m13_diff = Counter(q['difficulty'] for q in m13)
m14_diff = Counter(q['difficulty'] for q in m14)
print("M13 difficulty:", m13_diff)
print("M14 difficulty:", m14_diff)
expected_diff = Counter({'Intermediate': 35, 'Advanced': 30, 'Foundation': 25, 'Expert': 10})
assert m13_diff == expected_diff, "M13 difficulty mismatch"
assert m14_diff == expected_diff, "M14 difficulty mismatch"

# Check required fields
for i, q in enumerate(all_questions):
    assert 'id' in q and q['id']
    assert 'module' in q and q['module']
    assert 'topic' in q and q['topic']
    assert q['difficulty'] in ['Foundation', 'Intermediate', 'Advanced', 'Expert']
    assert 'questionText' in q and len(q['questionText']) > 20
    assert 'options' in q and len(q['options']) == 4
    for opt in q['options']:
        assert opt['id'] in ['A', 'B', 'C', 'D']
        assert len(opt['text']) > 0
    assert q['correctAnswer'] in ['A', 'B', 'C', 'D']
    assert 'explanation' in q and len(q['explanation']) > 20
    assert 'incorrectExplanations' in q
    # Check incorrect explanations
    for opt_id in ['A', 'B', 'C', 'D']:
        if opt_id != q['correctAnswer']:
            assert opt_id in q['incorrectExplanations'], f"Question {q['id']} missing incorrect explanation for {opt_id}"
    assert 'learningObjective' in q and len(q['learningObjective']) > 10
    assert 'reference' in q and len(q['reference']) > 5
    assert q['contentReviewStatus'] == 'Peer Reviewed'

print("All validation checks passed successfully!")

# Now format TypeScript code
ts_lines = ["import { Question } from '../types';", "", "export const MOD13_14_QUESTIONS: Question[] = ["]

def escape_str(s):
    return json.dumps(s, ensure_ascii=False)

for q in all_questions:
    ts_lines.append("  {")
    ts_lines.append(f'    id: {escape_str(q["id"])},')
    ts_lines.append(f'    module: {escape_str(q["module"])},')
    ts_lines.append(f'    topic: {escape_str(q["topic"])},')
    ts_lines.append(f'    difficulty: {escape_str(q["difficulty"])},')
    ts_lines.append(f'    questionText: {escape_str(q["questionText"])},')
    ts_lines.append("    options: [")
    for opt in q["options"]:
        ts_lines.append(f'      {{ id: {escape_str(opt["id"])}, text: {escape_str(opt["text"])} }},')
    ts_lines.append("    ],")
    ts_lines.append(f'    correctAnswer: {escape_str(q["correctAnswer"])},')
    ts_lines.append(f'    explanation: {escape_str(q["explanation"])},')
    ts_lines.append("    incorrectExplanations: {")
    for k in sorted(q["incorrectExplanations"].keys()):
        ts_lines.append(f'      {k}: {escape_str(q["incorrectExplanations"][k])},')
    ts_lines.append("    },")
    ts_lines.append(f'    learningObjective: {escape_str(q["learningObjective"])},')
    ts_lines.append(f'    reference: {escape_str(q["reference"])},')
    ts_lines.append(f'    contentReviewStatus: {escape_str(q["contentReviewStatus"])}')
    ts_lines.append("  },")

ts_lines.append("];")
ts_lines.append("")

out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "data", "questions_mod13_14.ts"))
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(ts_lines))

print(f"Successfully generated {out_path} with {len(all_questions)} questions!")
