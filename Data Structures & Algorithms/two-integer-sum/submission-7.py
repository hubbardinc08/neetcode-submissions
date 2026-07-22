class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        answer = []
        for i in range(len(nums)):
            if (s.get(target - nums[i], -1) != -1):
                i1 = i
                i2 = s[target - nums[i]]
                if (i < (i1 + i2) / 2):
                    answer.extend([i1, i2])
                else:
                    answer.extend([i2, i1])
                break
            else:
                s[nums[i]] = i
        
        return answer