class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        answer = []
        for i in range(len(nums)):
            if (s.get(target - nums[i], -1) != -1):
                answer.append(min(i, s[target - nums[i]]))
                answer.append(max(i, s[target - nums[i]]))
                break
            else:
                s[nums[i]] = i
        
        return answer