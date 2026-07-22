class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            if (s.get(target - nums[i], -1) != -1):
                return [s[target - nums[i]], i]
            s[nums[i]] = i