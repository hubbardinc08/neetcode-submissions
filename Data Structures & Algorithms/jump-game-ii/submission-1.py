class Solution:
    def jump(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 0

        for i in range(len(nums) - 1):
            if (nums[i] >= len(nums) - 1 - i):
                return 1 + self.jump(nums[:i + 1])
        
        return -1

