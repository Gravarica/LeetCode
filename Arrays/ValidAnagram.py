def makeDictionary(s: str): 
    countS = {}
    for i in range(len(s)):
        if s[i] in countS: 
            countS[s[i]] += 1
        else: 
            countS[s[i]] = 1
    
    return countS

def isAnagram(self, s:str, t:str) -> bool: 
    if len(s) != len(t):
        return False 
    
    countS = {}
    countT = {} 

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countS[t[i]] = 1 + countT.get(t[i], 0)
    
    return countS == countT

# Ideja:: Napravi mapu koja za svaki karakter ima broj njegovih pojavljivanja 
# Dve takve mape 