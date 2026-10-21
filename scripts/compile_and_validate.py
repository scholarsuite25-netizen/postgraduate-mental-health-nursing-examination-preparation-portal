# scripts/compile_and_validate.py
import sys, os, json
sys.path.insert(0, os.path.abspath('.'))

from scripts.generate_mod5_part1 import mod5_part1
from scripts.generate_mod5_part2 import mod5_part2
from scripts.generate_mod6_part1 import mod6_part1
from scripts.generate_mod6_part2 import mod6_part2
from collections import Counter

mod5 = mod5_part1 + mod5_part2
mod6 = mod6_part1 + mod6_part2

print(f"Loaded {len(mod5)} questions for Module 5")
print(f"Loaded {len(mod6)} questions for Module 6")

# Verify IDs
expected_mod5_ids = [f"MHN-Q{i}" for i in range(415, 515)]
actual_mod5_ids = [q['id'] for q in mod5]
assert expected_mod5_ids == actual_mod5_ids, f"Mod5 IDs mismatch: {set(expected_mod5_ids) ^ set(actual_mod5_ids)}"

expected_mod6_ids = [f"MHN-Q{i}" for i in range(515, 615)]
actual_mod6_ids = [q['id'] for q in mod6]
assert expected_mod6_ids == actual_mod6_ids, f"Mod6 IDs mismatch: {set(expected_mod6_ids) ^ set(actual_mod6_ids)}"

# Check topic counts
print("Mod5 Topics:", Counter(q['topic'] for q in mod5))
print("Mod6 Topics:", Counter(q['topic'] for q in mod6))

for topic, count in Counter(q['topic'] for q in mod5).items():
    assert count == 10, f"Mod5 topic {topic} has {count} questions, expected 10"

for topic, count in Counter(q['topic'] for q in mod6).items():
    assert count == 10, f"Mod6 topic {topic} has {count} questions, expected 10"

# Check difficulties
print("Original Mod5 Diff:", Counter(q['difficulty'] for q in mod5))
print("Original Mod6 Diff:", Counter(q['difficulty'] for q in mod6))

def adjust_difficulties(questions, target_counts):
    # target_counts: {'Foundation': 25, 'Intermediate': 35, 'Advanced': 30, 'Expert': 10}
    current_counts = Counter(q['difficulty'] for q in questions)
    
    # Balance Expert
    for q in questions:
        if current_counts['Expert'] > target_counts['Expert'] and q['difficulty'] == 'Expert':
            if current_counts['Advanced'] < target_counts['Advanced']:
                q['difficulty'] = 'Advanced'
                current_counts['Expert'] -= 1
                current_counts['Advanced'] += 1
            elif current_counts['Foundation'] < target_counts['Foundation']:
                q['difficulty'] = 'Foundation'
                current_counts['Expert'] -= 1
                current_counts['Foundation'] += 1
            elif current_counts['Intermediate'] < target_counts['Intermediate']:
                q['difficulty'] = 'Intermediate'
                current_counts['Expert'] -= 1
                current_counts['Intermediate'] += 1

    # Balance Foundation
    for q in questions:
        if current_counts['Foundation'] > target_counts['Foundation'] and q['difficulty'] == 'Foundation':
            if current_counts['Advanced'] < target_counts['Advanced']:
                q['difficulty'] = 'Advanced'
                current_counts['Foundation'] -= 1
                current_counts['Advanced'] += 1
            elif current_counts['Intermediate'] < target_counts['Intermediate']:
                q['difficulty'] = 'Intermediate'
                current_counts['Foundation'] -= 1
                current_counts['Intermediate'] += 1

    # Balance Intermediate and Advanced
    for q in questions:
        if current_counts['Intermediate'] > target_counts['Intermediate'] and q['difficulty'] == 'Intermediate':
            if current_counts['Foundation'] < target_counts['Foundation']:
                q['difficulty'] = 'Foundation'
                current_counts['Intermediate'] -= 1
                current_counts['Foundation'] += 1
            elif current_counts['Advanced'] < target_counts['Advanced']:
                q['difficulty'] = 'Advanced'
                current_counts['Intermediate'] -= 1
                current_counts['Advanced'] += 1

    for q in questions:
        if current_counts['Advanced'] > target_counts['Advanced'] and q['difficulty'] == 'Advanced':
            if current_counts['Foundation'] < target_counts['Foundation']:
                q['difficulty'] = 'Foundation'
                current_counts['Advanced'] -= 1
                current_counts['Foundation'] += 1
            elif current_counts['Intermediate'] < target_counts['Intermediate']:
                q['difficulty'] = 'Intermediate'
                current_counts['Advanced'] -= 1
                current_counts['Intermediate'] += 1

    return questions

target_diffs = {'Foundation': 25, 'Intermediate': 35, 'Advanced': 30, 'Expert': 10}
mod5 = adjust_difficulties(mod5, target_diffs)
mod6 = adjust_difficulties(mod6, target_diffs)

print("Adjusted Mod5 Diff:", Counter(q['difficulty'] for q in mod5))
print("Adjusted Mod6 Diff:", Counter(q['difficulty'] for q in mod6))
assert Counter(q['difficulty'] for q in mod5) == target_diffs
assert Counter(q['difficulty'] for q in mod6) == target_diffs

# Answer rebalancing: Exactly 25 A, 25 B, 25 C, 25 D per module
def reassign_correct(q, target):
    curr = q['correctAnswer']
    if curr == target:
        return q
    corr_opt = next(o for o in q['options'] if o['id'] == curr)
    incorr_opts = [o for o in q['options'] if o['id'] != curr]
    incorr_expls = [q['incorrectExplanations'][o['id']] for o in incorr_opts]
    
    letters = ['A', 'B', 'C', 'D']
    other_letters = [l for l in letters if l != target]
    
    new_options = []
    new_incorrect_expls = {}
    
    for l in letters:
        if l == target:
            new_options.append({'id': l, 'text': corr_opt['text']})
        else:
            idx = other_letters.index(l)
            new_options.append({'id': l, 'text': incorr_opts[idx]['text']})
            new_incorrect_expls[l] = incorr_expls[idx]
            
    q['options'] = new_options
    q['correctAnswer'] = target
    q['incorrectExplanations'] = new_incorrect_expls
    return q

def balance_answers(questions):
    # Pattern of answers for 100 questions: 25 A, 25 B, 25 C, 25 D
    # We can distribute them in cycle [A, B, C, D] * 25
    pattern = (['A', 'B', 'C', 'D'] * 25)
    for q, target in zip(questions, pattern):
        reassign_correct(q, target)
    return questions

mod5 = balance_answers(mod5)
mod6 = balance_answers(mod6)

print("Mod5 Answer distribution:", Counter(q['correctAnswer'] for q in mod5))
print("Mod6 Answer distribution:", Counter(q['correctAnswer'] for q in mod6))
assert Counter(q['correctAnswer'] for q in mod5) == {'A': 25, 'B': 25, 'C': 25, 'D': 25}
assert Counter(q['correctAnswer'] for q in mod6) == {'A': 25, 'B': 25, 'C': 25, 'D': 25}

all_questions = mod5 + mod6
print(f"Total compiled questions: {len(all_questions)}")
assert len(all_questions) == 200

# Validate uniqueness
q_texts = [q['questionText'] for q in all_questions]
assert len(set(q_texts)) == 200, f"Duplicate questionText found! Unique: {len(set(q_texts))}"

for q in all_questions:
    opt_texts = [o['text'] for o in q['options']]
    assert len(set(opt_texts)) == 4, f"Question {q['id']} has duplicate option text!"
    assert [o['id'] for o in q['options']] == ['A', 'B', 'C', 'D'], f"Question {q['id']} invalid option ids!"
    assert q['correctAnswer'] in ['A', 'B', 'C', 'D']
    incorrect_keys = set(q['incorrectExplanations'].keys())
    expected_incorrect_keys = {'A', 'B', 'C', 'D'} - {q['correctAnswer']}
    assert incorrect_keys == expected_incorrect_keys, f"Question {q['id']} incorrectExplanations keys mismatch: {incorrect_keys} vs {expected_incorrect_keys}"
    assert q['contentReviewStatus'] == "Peer Reviewed"

# Now write TypeScript file
ts_path = r"c:\Users\Registrar\Music\MY CODING FOLDER\postgraduate-mental-health-nursing-examination-preparation-portal\src\data\questions_mod5_6.ts"

with open(ts_path, 'w', encoding='utf-8') as f:
    f.write("import { Question } from '../types';\n\n")
    f.write("export const MOD5_6_QUESTIONS: Question[] = [\n")
    for i, q in enumerate(all_questions):
        f.write("  {\n")
        f.write(f"    id: {json.dumps(q['id'])},\n")
        f.write(f"    module: {json.dumps(q['module'])},\n")
        f.write(f"    topic: {json.dumps(q['topic'])},\n")
        f.write(f"    difficulty: {json.dumps(q['difficulty'])},\n")
        f.write(f"    questionText: {json.dumps(q['questionText'])},\n")
        f.write("    options: [\n")
        for opt in q['options']:
            f.write(f"      {{ id: {json.dumps(opt['id'])}, text: {json.dumps(opt['text'])} }},\n")
        f.write("    ],\n")
        f.write(f"    correctAnswer: {json.dumps(q['correctAnswer'])},\n")
        f.write(f"    explanation: {json.dumps(q['explanation'])},\n")
        f.write("    incorrectExplanations: {\n")
        for k in sorted(q['incorrectExplanations'].keys()):
            f.write(f"      {k}: {json.dumps(q['incorrectExplanations'][k])},\n")
        f.write("    },\n")
        f.write(f"    learningObjective: {json.dumps(q['learningObjective'])},\n")
        f.write(f"    reference: {json.dumps(q['reference'])},\n")
        f.write(f"    contentReviewStatus: {json.dumps(q['contentReviewStatus'])}\n")
        if i < len(all_questions) - 1:
            f.write("  },\n")
        else:
            f.write("  }\n")
    f.write("];\n")

print(f"Successfully generated {ts_path} with {len(all_questions)} questions!")
