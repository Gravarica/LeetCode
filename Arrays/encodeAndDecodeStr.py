# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1

# input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2

# input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

##### DIFF: MEDIUM

def encode(self, strs: List[str]) -> str:
        hidden_char='\u200B'

        if len(strs) == 0: 
            return hidden_char

        return hidden_char.join(strs)


def decode(self, s: str) -> List[str]:
    hidden_char='\u200B'
    
    if s == hidden_char:
        return []
    
    return s.split(hidden_char)