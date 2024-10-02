def characterReplacement(s: str, k: int) -> int: 
    start = 0 
    end = 0
    chars = {}
    longest = 0
    while start < len(s):
        window = end - start + 1
        while window - longest > k:
            chars[start] -= 1
            longest = max(longest, s[start])
            start += 1
        chars[end] = 1 + chars.get(s[end], 0) 
        longest = max(longest, s[end])
        end += 1

    return longest

s = "ABBA"
print(characterReplacement(s, 2))