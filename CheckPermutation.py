'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
'''

# O(n log(n))
def CheckPermutation(s_1: str, s_2: str):
    if len(s_1) != len(s_2):
        return False

    s_1_sorted = sorted(s_1)
    s_2_sorted = sorted(s_2)

    return s_1_sorted == s_2_sorted

# O(n)
def CheckPermutation(s_1: str, s_2: str):
    # Counter from scratch:
    s_1_counter = {}
    s_2_counter = {}

    for c in s_1:
        if c not in s_1_counter:
            s_1_counter[c] = 1
        else:
            s_1_counter[c] += 1

    for c in s_2:
        if c not in s_2_counter:
            s_2_counter[c] = 1
        else:
            s_2_counter[c] += 1

    return s_1_counter == s_2_counter
