"""
Postfix notation is an unambiguous way of writing an arithmetic expression without parentheses. It is defined so that if “(exp1)op(exp2)” is a normal, fully parenthesized expression whose operation is op, the postfix version of this is “pexp1 pexp2 op”, where pexp1 is the postfix version of exp1 and pexp2 is the postfix version of exp2. The postfix version of a single number or variable is just that number or variable. For example, the postfix version of “((5+2) ∗ (8−3))/4” is “5 2 + 8 3 − ∗ 4 /”. Describe a nonrecursive way of evaluating an expression in postfix notation.
"""

import time
from collections import deque

def isnum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def eval_postfix1(expr):
    """
    recursive function which solves postfix notation problem.
    """
    l = expr
    ops = ['+', '-', '*', '/', '^']
    new_exp_replacements = []

    if type(expr) == str:
        l = expr.split()

    if len(l) == 1:
        return l.pop()
    else:
        for i in range(2, len(l)):
            op = l[i]
            res = l[i-2]

            if op in ops:
                op1 = l[i-2]
                op2 = l[i-1]

                if isnum(op1) and isnum(op2):
                    if op == '+':
                        res = float(op1) + float(op2)
                    elif op == '-':
                        res = float(op1) - float(op2)
                    elif op == '*':
                        res = float(op1) * float(op2)
                    elif op == '/':
                        res = float(op1) / float(op2)
                    elif op == '^':
                        res = float(op1) ** float(op2)
                    new_exp_replacements.append(((i-2, i), res))

        # apply calculated replacements
        for ids, res in new_exp_replacements:
            lo, hi = ids
            l[lo] = res
            l[lo+1:hi+1] = ['#'] * (hi-lo) # put placeholders so indexes are still in right place

        l = [e for e in l if e != '#']

        return eval_postfix1(l)


e1 = '4 5 * 31 2 - + 9 -' # 40
e2 = '8 2 / 2 2 + *' # 16
e3 = '4 8 3 * +' # 28

print("---eval_postfix1---")
print(eval_postfix1(e1))
print(eval_postfix1(e2))
print(eval_postfix1(e3))



def eval_postfix2(expr):
    """
    a non-recursive way of resolving postfix notation
    """
    ops = ['+', '-', '*', '/', '^']
    l = expr.split()
    s = []

    for c in l:
        if isnum(c):
            s.append(c)
        elif c in ops:
            op = c
            op2 = s.pop()
            op1 = s.pop()
            res = 0

            if op == '+':
                res = float(op1) + float(op2)
            elif op == '-':
                res = float(op1) - float(op2)
            elif op == '*':
                res = float(op1) * float(op2)
            elif op == '/':
                res = float(op1) / float(op2)
            elif op == '^':
                res = float(op1) ** float(op2)

            s.append(res)
    return s.pop()

print("---eval_postfix2---")
print(eval_postfix2(e1))
print(eval_postfix2(e2))
print(eval_postfix2(e3))

print("--- benchmarking ---")

eb = "2 20 * 2 / 3 4 + 3 2 ^ * + 6 - 15 +"
n = 1000000

t0 = time.clock()
for i in range(0, n):
    eval_postfix1(eb)
print(f"time elapsed for eval_postfix1: {time.clock()-t0}")

t0 = time.clock()
for i in range(0, n):
    eval_postfix2(eb)
print(f"time elapsed for eval_postfix2: {time.clock()-t0}")
