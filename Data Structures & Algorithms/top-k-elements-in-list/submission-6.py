class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        countr = {}
        reps = []
        answer = []
        for num in nums:
            count[num] += 1
        
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

        for key, value in sorted_dict.items():
            if (k == 0):
                break
            
            answer.append(key)
            k -= 1
        return answer
        


