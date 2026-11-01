class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        deltas = []
        visited = defaultdict(int)
        if (sum(gas) - sum(cost) < 0):
            return -1

        for i in range(len(gas)):
            deltas.append(gas[i] - cost[i])

        start = 0
        curr_sum = 0
        while (visited[start] != 1):
            visited[start] = 1
            for i in range(start, len(deltas) + start):
                curr_sum += deltas[i % len(deltas)]
                if (curr_sum < 0):
                    start = (i + 1) % len(deltas)
                    curr_sum = 0
                    break
            
    
        return start

            
        
        
