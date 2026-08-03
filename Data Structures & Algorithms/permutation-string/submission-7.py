class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lp = 0
        visited = defaultdict(int)
        target = defaultdict(int)
        diff = len(s1)

        for elem in s1:
            target[elem] += 1
        
        for i in range(len(s2)):
            visited[s2[i]] += 1
            if (target[s2[i]] != 0):
                if (visited[s2[i]] <= target[s2[i]]):
                    diff -= 1
                else:
                    diff += 1
            if (i < len(s1)):
                if (diff == 0):
                    return True
                continue

            if (target[s2[lp]] != 0):
                if (visited[s2[lp]] <= target[s2[lp]]):
                    diff += 1
                else:
                    diff -= 1
                
            visited[s2[lp]] -= 1

            lp += 1

            if (diff == 0):
                return True
        
        return False



