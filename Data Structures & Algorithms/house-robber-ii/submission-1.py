class Solution:
    def rob(self, nums: List[int]) -> int:
        res1, res2 = 0, 0

        if (len(nums) == 1):
            return nums[0]

        new_nums = nums[1:]
        dp = [0] * len(new_nums)

        if (len(new_nums) <= 2):
            res1 = max(new_nums)
        else:
            dp[0], dp[1] = new_nums[0], max(new_nums[0], new_nums[1])

            for i in range(2, len(new_nums)):
                dp[i] = max(dp[i - 2] + new_nums[i], dp[i - 1])
            
            res1 =  dp[len(new_nums) - 1]
    
        new_nums = nums[:-1]
        dp = [0] * len(new_nums)

        if (len(new_nums) <= 2):
            res2 = max(new_nums)
        else:
            dp[0], dp[1] = new_nums[0], max(new_nums[0], new_nums[1])

            for i in range(2, len(new_nums)):
                dp[i] = max(dp[i - 2] + new_nums[i], dp[i - 1])
            
            res2 = dp[len(new_nums) - 1]
        
        return max(res1, res2)