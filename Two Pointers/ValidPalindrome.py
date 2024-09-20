import re

def alphaNum(c): 
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))

def isPalindrome(self, s: str) -> bool: 
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    l = 0 
    r = len(s) - 1
    while l < r: 
        if s[l] != s[r]:
            return False 
        l += 1
        r -= 1

    return True 

    
