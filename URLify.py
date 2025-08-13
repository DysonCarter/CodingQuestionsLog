'''
URLify: Write a method to replace all spaces in a string with '%20', You may assume tha the string has 
sufficient space at the end to hold the additional characters, and that you are given the "true" kebgtg if the string
'''

# Python Cheat code
def URLify(s: str, length: int):
    s = s.replace(' ', '%20')
    return s
