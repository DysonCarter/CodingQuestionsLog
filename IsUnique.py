'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

# Normal Solution - O(n)
def IsUnique(s: str):
    seen = set()

    for c in s:
        if c in seen:
            return False
        else:
            seen.append(c)
    
    return True

# No Additional Data Structures - O(n log(n))
def IsUnique(s: str):
    sorted_s = sorted(s)

    prev = ""
    for c in sorted_s:
        if c == prev:
            return False
        else:
            prev = c

    return True
