class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if (len(nums) == 1):
            return True
        

        d = 1
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] >= d):
                return self.canJump(nums[:i + 1])
            
            d += 1
        
        return False