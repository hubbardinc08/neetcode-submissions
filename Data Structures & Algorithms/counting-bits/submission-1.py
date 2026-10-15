class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for num in range(n + 1):
            dp[num] = dp[num >> 1] + (num & 1)
        
        return dp



        # "cheater" approach
        # result = []
        # for num in range(n + 1):
        #     result.append(bin(num).count('1'))

        # return result
