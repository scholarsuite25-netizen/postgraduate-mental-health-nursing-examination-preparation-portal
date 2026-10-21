import json
import os
import sys
from collections import Counter

from generator.mod7_part1 import QUESTIONS_MOD7_PART1
from generator.mod7_part2 import QUESTIONS_MOD7_PART2
from generator.mod8_part1 import QUESTIONS_MOD8_PART1
from generator.mod8_part2 import QUESTIONS_MOD8_PART2

def main():
    mod7_questions = QUESTIONS_MOD7_PART1 + QUESTIONS_MOD7_PART2
    mod8_questions = QUESTIONS_MOD8_PART1 + QUESTIONS_MOD8_PART2

    print(f"Loaded Module 7 questions: {len(mod7_questions)}")
    print(f"Loaded Module 8 questions: {len(mod8_questions)}")

    assert len(mod7_questions) == 100, f"Expected 100 Mod 7 questions, got {len(mod7_questions)}"
    assert len(mod8_questions) == 100, f"Expected 100 Mod 8 questions, got {len(mod8_questions)}"

    all_questions = mod7_questions + mod8_questions
    print(f"Total questions: {len(all_questions)}")

    # 1. Check IDs
    mod7_expected_ids = [f"MHN-Q{i}" for i in range(615, 715)]
    mod8_expected_ids = [f"MHN-Q{i}" for i in range(715, 815)]

    mod7_ids = [q["id"] for q in mod7_questions]
    mod8_ids = [q["id"] for q in mod8_questions]

    assert mod7_ids == mod7_expected_ids, f"Mod 7 IDs mismatch: {mod7_ids[:3]} ... {mod7_ids[-3:]}"
    assert mod8_ids == mod8_expected_ids, f"Mod 8 IDs mismatch: {mod8_ids[:3]} ... {mod8_ids[-3:]}"
    print("All 200 IDs match exact ranges MHN-Q615..MHN-Q714 and MHN-Q715..MHN-Q814.")

    all_ids = [q["id"] for q in all_questions]
    assert len(all_ids) == len(set(all_ids)), "Duplicate IDs found!"

    # 2. Check Module names
    MOD7_NAME = "7. Community Mental Health and Psychiatric Rehabilitation"
    MOD8_NAME = "8. Child, Adolescent, and Older Adult Mental Health"

    for q in mod7_questions:
        assert q["module"] == MOD7_NAME, f"Mod 7 question {q['id']} module name mismatch: {q['module']}"
    for q in mod8_questions:
        assert q["module"] == MOD8_NAME, f"Mod 8 question {q['id']} module name mismatch: {q['module']}"
    print("Module names exact.")

    # 3. Check Uniqueness of questionText
    all_qtexts = [q["questionText"].strip() for q in all_questions]
    assert len(all_qtexts) == len(set(all_qtexts)), "Duplicate questionText detected!"
    print("All 200 question texts are 100% unique.")

    # 4. Check Answer distribution
    mod7_answers = Counter(q["correctAnswer"] for q in mod7_questions)
    mod8_answers = Counter(q["correctAnswer"] for q in mod8_questions)
    print("Mod 7 answers:", mod7_answers)
    print("Mod 8 answers:", mod8_answers)
    assert mod7_answers == {"A": 25, "B": 25, "C": 25, "D": 25}, f"Mod 7 answers unbalanced: {mod7_answers}"
    assert mod8_answers == {"A": 25, "B": 25, "C": 25, "D": 25}, f"Mod 8 answers unbalanced: {mod8_answers}"
    print("Answer distributions are EXACTLY 25 A, 25 B, 25 C, 25 D for both modules!")

    # 5. Check Difficulty distribution
    mod7_diff = Counter(q["difficulty"] for q in mod7_questions)
    mod8_diff = Counter(q["difficulty"] for q in mod8_questions)
    print("Mod 7 difficulty:", mod7_diff)
    print("Mod 8 difficulty:", mod8_diff)
    expected_diff = {"Foundation": 25, "Intermediate": 35, "Advanced": 30, "Expert": 10}
    assert mod7_diff == expected_diff, f"Mod 7 diff mismatch: {mod7_diff}"
    assert mod8_diff == expected_diff, f"Mod 8 diff mismatch: {mod8_diff}"
    print("Difficulty distributions are EXACTLY 25 Foundation, 35 Intermediate, 30 Advanced, 10 Expert!")

    # 6. Detailed field validation
    for q in all_questions:
        qid = q["id"]
        assert q["topic"], f"{qid} empty topic"
        assert q["difficulty"] in ["Foundation", "Intermediate", "Advanced", "Expert"], f"{qid} invalid difficulty"
        assert len(q["questionText"]) >= 20, f"{qid} questionText too short"
        assert len(q["options"]) == 4, f"{qid} options len != 4"
        opt_ids = [opt["id"] for opt in q["options"]]
        assert opt_ids == ["A", "B", "C", "D"], f"{qid} opt_ids != ABCD"
        opt_texts = [opt["text"].strip() for opt in q["options"]]
        assert len(set(opt_texts)) == 4, f"{qid} options are not unique"
        for opt_text in opt_texts:
            assert len(opt_text) >= 2, f"{qid} option text empty or too short"
        
        corr = q["correctAnswer"]
        assert corr in ["A", "B", "C", "D"], f"{qid} invalid correctAnswer"
        assert len(q["explanation"]) >= 20, f"{qid} explanation too short"
        
        # Check incorrectExplanations
        inc = q.get("incorrectExplanations", {})
        assert len(inc) == 3, f"{qid} incorrectExplanations len != 3, got {len(inc)}"
        for key in ["A", "B", "C", "D"]:
            if key == corr:
                assert key not in inc, f"{qid} incorrectExplanations has correct answer {key}"
            else:
                assert key in inc, f"{qid} missing incorrectExplanation for {key}"
                assert len(inc[key]) >= 5, f"{qid} incorrectExplanation for {key} too short"
        
        assert len(q["learningObjective"]) >= 10, f"{qid} learningObjective too short"
        assert len(q["reference"]) >= 10, f"{qid} reference too short"
        assert q["contentReviewStatus"] == "Peer Reviewed", f"{qid} contentReviewStatus != Peer Reviewed"

    print("All 200 questions passed 100% rigorous validation rules!")

    # 7. Write TypeScript output file
    target_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src",
            "data",
            "questions_mod7_8.ts"
        )
    )

    print(f"Writing output TypeScript file to: {target_path}")

    # Build TS content
    lines = [
        "import { Question } from '../types';",
        "",
        "export const MOD7_8_QUESTIONS: Question[] = ["
    ]

    for q in all_questions:
        q_json = json.dumps(q, indent=2, ensure_ascii=False)
        # Indent each line by 2 spaces
        indented = "\n".join("  " + l for l in q_json.split("\n"))
        lines.append(indented + ",")

    lines.append("];")
    lines.append("")

    with open(target_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    file_size_kb = os.path.getsize(target_path) / 1024
    print(f"Successfully generated {target_path} ({file_size_kb:.2f} KB)!")

if __name__ == "__main__":
    main()
