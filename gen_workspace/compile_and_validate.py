import sys
import os
import json

sys.path.append('gen_workspace')
from gen_mod3_part1 import MOD3_P1
from gen_mod3_part2 import MOD3_P2
from gen_mod4_part1 import MOD4_P1
from gen_mod4_part2 import MOD4_P2

mod3 = MOD3_P1 + MOD3_P2
mod4 = MOD4_P1 + MOD4_P2
all_questions = mod3 + mod4

print(f"Total questions loaded: {len(all_questions)}")
assert len(mod3) == 100, f"Mod3 count expected 100, got {len(mod3)}"
assert len(mod4) == 100, f"Mod4 count expected 100, got {len(mod4)}"
assert len(all_questions) == 200, f"Total count expected 200, got {len(all_questions)}"

# Check IDs
expected_ids = [f"MHN-Q{i:03d}" for i in range(215, 415)]
actual_ids = [q['id'] for q in all_questions]
assert actual_ids == expected_ids, f"IDs mismatch! Differences: {[a for a, b in zip(actual_ids, expected_ids) if a != b]}"

# Check unique question texts
texts = [q['questionText'].strip().lower() for q in all_questions]
assert len(set(texts)) == 200, f"Duplicate questionText found! Unique: {len(set(texts))}"

# Check modules
for q in mod3:
    assert q['module'] == "3. Psychopathology and Psychiatric Diagnosis", f"Wrong module in {q['id']}: {q['module']}"
for q in mod4:
    assert q['module'] == "4. Psychopharmacology and Medication Management", f"Wrong module in {q['id']}: {q['module']}"

# Check options and fields
from collections import Counter

for mod_name, q_list in [("Module 3", mod3), ("Module 4", mod4)]:
    ans_counts = Counter(q['correctAnswer'] for q in q_list)
    diff_counts = Counter(q['difficulty'] for q in q_list)
    print(f"\n{mod_name} Validation:")
    print(f"  Answers: {dict(ans_counts)}")
    print(f"  Difficulty: {dict(diff_counts)}")
    assert ans_counts['A'] == 25 and ans_counts['B'] == 25 and ans_counts['C'] == 25 and ans_counts['D'] == 25, \
        f"{mod_name} answers not 25 each: {ans_counts}"
    assert diff_counts['Foundation'] == 25 and diff_counts['Intermediate'] == 35 and diff_counts['Advanced'] == 30 and diff_counts['Expert'] == 10, \
        f"{mod_name} difficulty counts invalid: {diff_counts}"

for q in all_questions:
    assert len(q['options']) == 4, f"{q['id']} does not have 4 options"
    opt_ids = [opt['id'] for opt in q['options']]
    assert opt_ids == ['A', 'B', 'C', 'D'], f"{q['id']} options ids invalid: {opt_ids}"
    assert q['correctAnswer'] in ['A', 'B', 'C', 'D'], f"{q['id']} invalid correctAnswer"
    assert q['explanation'] and len(q['explanation']) > 20, f"{q['id']} explanation too short"
    assert q['learningObjective'] and len(q['learningObjective']) > 15, f"{q['id']} learningObjective too short"
    assert q['reference'] and len(q['reference']) > 10, f"{q['id']} reference too short"
    assert q['contentReviewStatus'] == "Peer Reviewed", f"{q['id']} wrong status"
    assert 'incorrectExplanations' in q, f"{q['id']} missing incorrectExplanations"
    # Ensure options text is unique
    opt_texts = [opt['text'].strip().lower() for opt in q['options']]
    assert len(set(opt_texts)) == 4, f"{q['id']} has duplicate options text: {opt_texts}"

print("\nAll validations PASSED successfully!")

# Format TypeScript
out_path = os.path.join('src', 'data', 'questions_mod3_4.ts')

def escape_ts(s: str) -> str:
    # We can use json.dumps for safe string quoting
    return json.dumps(s, ensure_ascii=False)

lines = []
lines.append("import { Question } from '../types';")
lines.append("")
lines.append("export const MOD3_4_QUESTIONS: Question[] = [")

for q in all_questions:
    lines.append("  {")
    lines.append(f"    id: {escape_ts(q['id'])},")
    lines.append(f"    module: {escape_ts(q['module'])},")
    lines.append(f"    topic: {escape_ts(q['topic'])},")
    lines.append(f"    difficulty: {escape_ts(q['difficulty'])},")
    lines.append(f"    questionText: {escape_ts(q['questionText'])},")
    lines.append("    options: [")
    for opt in q['options']:
        lines.append(f"      {{ id: {escape_ts(opt['id'])}, text: {escape_ts(opt['text'])} }},")
    lines.append("    ],")
    lines.append(f"    correctAnswer: {escape_ts(q['correctAnswer'])},")
    lines.append(f"    explanation: {escape_ts(q['explanation'])},")
    lines.append("    incorrectExplanations: {")
    for key in ['A', 'B', 'C', 'D']:
        if key in q['incorrectExplanations']:
            lines.append(f"      {key}: {escape_ts(q['incorrectExplanations'][key])},")
    lines.append("    },")
    lines.append(f"    learningObjective: {escape_ts(q['learningObjective'])},")
    lines.append(f"    reference: {escape_ts(q['reference'])},")
    lines.append(f"    contentReviewStatus: {escape_ts(q['contentReviewStatus'])}")
    lines.append("  },")

lines.append("];")
lines.append("")

content = "\n".join(lines)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated {out_path} with {len(content)} characters and {len(lines)} lines.")
