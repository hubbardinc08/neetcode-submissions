class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        if (len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            letters[s[i]] = letters.get(s[i], 0) - 1
            letters[t[i]] = letters.get(t[i], 0) + 1
        
        return all(value == 0 for value in letters.values())