class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def helper(n):
            if (n == len(cost)):
                return 0
            if (n > len(cost)):
                return math.inf
            
            if ((n + 1) in cache):
                one_step = cost[n] + cache[n + 1]
            else:
                one_step = cost[n] + helper(n + 1)
            if ((n + 2) in cache):
                two_step = cost[n] + cache[n + 2]
            else:
                two_step = cost[n] + helper(n + 2)
            
            result = min(one_step, two_step)

            cache[n] = result
            return result
        
            

        
        return min(helper(0), helper(1))