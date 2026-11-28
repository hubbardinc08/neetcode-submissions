class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        for idx in range(len(s)):
            lp, rp = idx, idx
            while (lp >= 0 and rp < len(s) and s[lp] == s[rp]):
                total += 1
                lp -= 1
                rp += 1
                
            
        for idx in range(len(s) - 1):
            lp, rp = idx, idx + 1
            while (lp >= 0 and rp < len(s) and s[lp] == s[rp]):
                total += 1
                lp -= 1
                rp += 1


        return total