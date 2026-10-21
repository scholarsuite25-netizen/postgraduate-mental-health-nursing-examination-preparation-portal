# test_permute.py
import sys, os
sys.path.insert(0, os.path.abspath('.'))
from scripts.generate_mod5_part1 import mod5_part1

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

q0 = mod5_part1[0]
print('Original:', q0['correctAnswer'], [o['text'] for o in q0['options']])
q_new = reassign_correct(q0, 'C')
print('After C:', q_new['correctAnswer'], [f"{o['id']}: {o['text']}" for o in q_new['options']])
print('Incorrect keys:', list(q_new['incorrectExplanations'].keys()))
