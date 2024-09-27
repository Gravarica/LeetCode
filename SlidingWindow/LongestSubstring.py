def lengthOfLognestSubstring(s: str) -> int: 
    chars = {}
    maxLength = 0
    
    while i < len(s): 
        if s[i] in chars: 
            i = chars[s[i]]
            chars = {}
        else: 
            chars[s[i]] = i
            maxLength = max(maxLength, len(chars))
        
        i += 1

    return max(maxLength, len(chars))


s1 = "zxyzxyz"
s2 = "xxxx"
s3 = "xxxyyyxzyh"
s4 = "aab"

# print(lengthOfLognestSubstring(s1))
# print(lengthOfLognestSubstring(s2))
print(lengthOfLognestSubstring(s4))