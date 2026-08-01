class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fp = 0
        bp = 0
        counter = defaultdict(int)
        max_app = 0

        for char in s:
            counter[char] += 1
            max_app = max(max_app, counter[char])
            if ((bp - fp + 1) - max_app <= k):
                bp += 1
            else:
                counter[s[fp]] -= 1
                fp += 1
                bp += 1
            
        return bp - fp




# Pseudo Code
# 1. We keep a front index and back index that track the values leaving and entering
# 2. We have a dictionary that stores the num of appearance of every letter
# 3. We have a variable storing the length of the longest substr
# 4. 