import re
import json

with open('src/data/questions_mod11_12.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Assert header and footer
assert content.startswith("import { Question } from '../types';\n\nexport const MOD11_12_QUESTIONS: Question[] = [")
assert content.rstrip().endswith("];")

# Extract question IDs
ids = re.findall(r'id:\s*"(MHN-Q\d+)"', content)
print(f"Total question IDs found: {len(ids)}")
assert len(ids) == 200
assert ids[0] == "MHN-Q1015"
assert ids[-1] == "MHN-Q1214"
assert len(set(ids)) == 200

# Extract modules
modules = re.findall(r'module:\s*"([^"]+)"', content)
print(f"Module 11 count: {modules.count('11. Advanced Clinical Scenarios')}")
print(f"Module 12 count: {modules.count('12. Leadership and Professional Practice')}")
assert modules.count('11. Advanced Clinical Scenarios') == 100
assert modules.count('12. Leadership and Professional Practice') == 100

# Extract difficulties
difficulties = re.findall(r'difficulty:\s*"([^"]+)"', content)
from collections import Counter
m11_diff = Counter(difficulties[:100])
m12_diff = Counter(difficulties[100:])
print("M11 diff:", m11_diff)
print("M12 diff:", m12_diff)
expected_diff = Counter({'Intermediate': 35, 'Advanced': 30, 'Foundation': 25, 'Expert': 10})
assert m11_diff == expected_diff
assert m12_diff == expected_diff

# Extract correct answers
answers = re.findall(r'correctAnswer:\s*"([^"]+)"', content)
m11_ans = Counter(answers[:100])
m12_ans = Counter(answers[100:])
print("M11 answers:", m11_ans)
print("M12 answers:", m12_ans)
expected_ans = Counter({'A': 25, 'B': 25, 'C': 25, 'D': 25})
assert m11_ans == expected_ans
assert m12_ans == expected_ans

print("\n--- ALL VALIDATION CHECKS PASSED PERFECTLY ---")
