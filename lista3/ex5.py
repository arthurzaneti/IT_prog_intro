def is_anagram(s,t):
    if(len(s) != len(t)):
         return False
    for z in set(s):
         if(s.count(z) != t.count(z)):
              return(False)
    return(True)

"""
print(is_anagram("a", "a"))
print(is_anagram("abcd", "acdb"))
print(is_anagram("aaab", "ab"))
print(is_anagram("aAá", "áaA"))
"""