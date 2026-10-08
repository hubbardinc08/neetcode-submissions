class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * weight for weight in stones]
        
        heapq.heapify(stones)

        while (len(stones) > 1):
            w1 = (-1) * heapq.heappop(stones)
            w2 = (-1) * heapq.heappop(stones)
            
            diff = abs(w1 - w2)
            if (diff != 0):
                heapq.heappush(stones, (-1) * diff)
            else:
                continue
            
        if (len(stones) == 1):
            return (-1) * stones[0]
        else:
            return 0