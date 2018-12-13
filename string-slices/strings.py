example = input('Enter a string')
'''
String sliciing:
    a string is a like a python list and each and every element can be accessed by square bracket notation.
'''
print("example string's  start to fifth characters "+example[:5])
print("example string's  first to third characters "+example[1:3])
print("example string's  fourth to the end of the string "+example[4:])
print("example string's  fifth character from the end to first character from the end "+example[-5:-1])
print("example string's  first to fifth characters "+example[1:5])

'''
Output:

Enter a string talentaccurate
example string's  start to fifth characters  tale
example string's  first to third characters ta
example string's  fourth to the end of the string entaccurate
example string's  fifth character from the end to first character from the end urat
example string's  first to fifth characters tale

Explanation:
    t  a  l   e    n   t   a  c  c  u  r  a  t  e
    0  1  2   3    4   5   6  7  8  9  10 11 12 13
  -14 -13 -12 -11 -10 -9  -8 -7 -6 -5 -4  -3 -2 -1         
'''
