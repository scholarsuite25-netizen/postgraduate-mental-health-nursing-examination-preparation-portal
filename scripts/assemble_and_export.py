import sys
import os
import json
import copy
from collections import Counter

# Add repo root to path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, REPO_ROOT)

import scripts.mod11_part1 as m11p1
import scripts.mod11_part2 as m11p2
import scripts.mod12_part1 as m12p1
import scripts.mod12_part2 as m12p2

def reassign_correct(q, target):
    """
    Safely reassigns the correct answer of question q to `target` (A, B, C, or D).
    Swaps options and preserves exact distractor explanations.
    """
    curr = q['correctAnswer']
    if curr == target:
        return q

    # Map original option texts to their explanation
    text_to_incorr_expl = {}
    for o in q['options']:
        if o['id'] != curr:
            text_to_incorr_expl[o['text']] = q['incorrectExplanations'][o['id']]

    corr_opt = next(o for o in q['options'] if o['id'] == curr)
    incorr_opts = [o for o in q['options'] if o['id'] != curr]

    letters = ['A', 'B', 'C', 'D']
    other_letters = [l for l in letters if l != target]

    new_options = []
    new_incorrect_expls = {}

    for l in letters:
        if l == target:
            new_options.append({'id': l, 'text': corr_opt['text']})
        else:
            idx = other_letters.index(l)
            opt_text = incorr_opts[idx]['text']
            new_options.append({'id': l, 'text': opt_text})
            new_incorrect_expls[l] = text_to_incorr_expl[opt_text]

    q['options'] = new_options
    q['correctAnswer'] = target
    q['incorrectExplanations'] = new_incorrect_expls
    return q

ODD_TARGET = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B']
EVEN_TARGET = ['C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']

def balance_module(qlist):
    new_list = []
    for topic_idx in range(10):
        target_seq = ODD_TARGET if topic_idx % 2 == 0 else EVEN_TARGET
        for q_idx in range(10):
            q = copy.deepcopy(qlist[topic_idx * 10 + q_idx])
            target_ans = target_seq[q_idx]
            q = reassign_correct(q, target_ans)
            new_list.append(q)
    return new_list

m11_raw = m11p1.MOD11_PART1 + m11p2.MOD11_PART2
m12_raw = m12p1.MOD12_PART1 + m12p2.MOD12_PART2

assert len(m11_raw) == 100, f"Expected 100 questions for Module 11, got {len(m11_raw)}"
assert len(m12_raw) == 100, f"Expected 100 questions for Module 12, got {len(m12_raw)}"

m11 = balance_module(m11_raw)
m12 = balance_module(m12_raw)
all_questions = m11 + m12

print(f"Total questions assembled: {len(all_questions)}")

# Validation: IDs
expected_m11_ids = [f"MHN-Q{i}" for i in range(1015, 1115)]
expected_m12_ids = [f"MHN-Q{i}" for i in range(1115, 1215)]

m11_ids = [q['id'] for q in m11]
m12_ids = [q['id'] for q in m12]

assert m11_ids == expected_m11_ids, f"M11 ID mismatch! Expected {expected_m11_ids[0]}..{expected_m11_ids[-1]}, got {m11_ids[0]}..{m11_ids[-1]}"
assert m12_ids == expected_m12_ids, f"M12 ID mismatch! Expected {expected_m12_ids[0]}..{expected_m12_ids[-1]}, got {m12_ids[0]}..{m12_ids[-1]}"

# Uniqueness
all_ids = [q['id'] for q in all_questions]
assert len(all_ids) == len(set(all_ids)), "Duplicate IDs found!"

all_texts = [q['questionText'].strip().lower() for q in all_questions]
assert len(all_texts) == len(set(all_texts)), "Duplicate question texts found!"

# Answer keys
m11_answers = Counter(q['correctAnswer'] for q in m11)
m12_answers = Counter(q['correctAnswer'] for q in m12)
print("M11 answers:", m11_answers)
print("M12 answers:", m12_answers)
assert m11_answers == Counter({'A': 25, 'B': 25, 'C': 25, 'D': 25}), "M11 answers not 25 each"
assert m12_answers == Counter({'A': 25, 'B': 25, 'C': 25, 'D': 25}), "M12 answers not 25 each"

# Difficulty distribution
expected_diff = Counter({'Intermediate': 35, 'Advanced': 30, 'Foundation': 25, 'Expert': 10})
m11_diff = Counter(q['difficulty'] for q in m11)
m12_diff = Counter(q['difficulty'] for q in m12)
print("M11 difficulties:", m11_diff)
print("M12 difficulties:", m12_diff)
assert m11_diff == expected_diff, f"M11 difficulty mismatch: {m11_diff}"
assert m12_diff == expected_diff, f"M12 difficulty mismatch: {m12_diff}"

# Detailed question integrity check
for q in all_questions:
    assert 'id' in q and q['id'].startswith('MHN-Q'), f"Invalid ID in {q}"
    assert 'module' in q and q['module'] in ['11. Advanced Clinical Scenarios', '12. Leadership and Professional Practice']
    assert 'topic' in q and len(q['topic']) > 3
    assert q['difficulty'] in ['Foundation', 'Intermediate', 'Advanced', 'Expert']
    assert 'questionText' in q and len(q['questionText']) >= 20
    assert 'options' in q and len(q['options']) == 4
    opt_ids = [o['id'] for o in q['options']]
    assert opt_ids == ['A', 'B', 'C', 'D'], f"Options not A-D in {q['id']}"
    opt_texts = [o['text'].strip() for o in q['options']]
    assert len(opt_texts) == len(set(opt_texts)), f"Duplicate option text in {q['id']}"
    for opt in q['options']:
        assert len(opt['text']) > 0, f"Empty option text in {q['id']}"
    assert q['correctAnswer'] in ['A', 'B', 'C', 'D']
    assert 'explanation' in q and len(q['explanation']) >= 20
    assert 'incorrectExplanations' in q
    for opt_id in ['A', 'B', 'C', 'D']:
        if opt_id != q['correctAnswer']:
            assert opt_id in q['incorrectExplanations'], f"Question {q['id']} missing incorrect explanation for {opt_id}"
            assert len(q['incorrectExplanations'][opt_id]) > 5, f"Question {q['id']} has empty explanation for {opt_id}"
        else:
            assert opt_id not in q['incorrectExplanations'], f"Question {q['id']} has incorrect explanation for correct answer {opt_id}"
    assert 'learningObjective' in q and len(q['learningObjective']) >= 10
    assert 'reference' in q and len(q['reference']) >= 5
    assert q['contentReviewStatus'] == 'Peer Reviewed'

print("All integrity checks passed successfully!")

# Format TypeScript output
def escape_str(s):
    return json.dumps(s, ensure_ascii=False)

ts_lines = [
    "import { Question } from '../types';",
    "",
    "export const MOD11_12_QUESTIONS: Question[] = ["
]

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

out_path = os.path.join(REPO_ROOT, "src", "data", "questions_mod11_12.ts")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(ts_lines))

print(f"Successfully generated {out_path} with {len(all_questions)} questions!")
