class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_val = 0
        max_val = -10001

        for idx, num in enumerate(nums):
            curr_val += num

            max_val = max(max_val, curr_val)

            if (curr_val < 0):
                curr_val = 0

        return max_val

