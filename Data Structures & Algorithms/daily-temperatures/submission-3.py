class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            result.append(0)
        
        nums = [[temperatures[0], 0]]
        for i in range(1, len(temperatures)):
            while (len(nums) > 0 and temperatures[i] > nums[-1][0]):
                result[nums[-1][1]] = i - nums[-1][1]
                nums.pop()
            
            nums.append([temperatures[i], i])
        
        while (len(nums) > 0):
            result[nums[-1][1]] = 0
            nums.pop()
        
        return result
