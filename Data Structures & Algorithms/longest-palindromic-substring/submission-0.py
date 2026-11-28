class Solution:
    def longestPalindrome(self, s: str) -> str:
        l1, l2 = 0, 0
        w1, w2 = "", ""

        for idx in range(len(s)):
            lp, rp = idx, idx
            curr_len = 0
            curr_word = ""
            while (lp >= 0 and rp < len(s) and s[lp] == s[rp]):
                curr_word = s[lp:rp + 1]
                if (lp == rp):
                    curr_len += 1
                else:
                    curr_len += 2
                lp -= 1
                rp += 1
                
            if (curr_len > l1):
                l1 = curr_len
                w1 = curr_word
            
        for idx in range(len(s) - 1):
            lp, rp = idx, idx + 1
            curr_len = 0
            curr_word = ""
            while (lp >= 0 and rp < len(s) and s[lp] == s[rp]):
                curr_word = s[lp:rp + 1]
                curr_len += 2
                lp -= 1
                rp += 1
                
            if (curr_len > l2):
                l2 = curr_len
                w2 = curr_word

        return w1 if len(w1) > len(w2) else w2
            
        
        

