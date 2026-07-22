class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for num in nums:
            if (s.get(num, 0) != 0):
                return True
            
            s[num] = 1
        
        return False