"""
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that
a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
"""


from itertools import permutations


l: list = eval(input())
valid_tuples = 0

perms = list(permutations(l, 4))

for index in range(0, len(perms)):
    t = perms[index]
    print(t)
    if t[0] * t[1] == t[2] * t[3]:
        valid_tuples += 1

print(valid_tuples)
