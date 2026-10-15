class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        correct_res = 0
        for num in nums:
            correct_res = correct_res ^ num

        incorrect_res = 0
        for i in range(len(nums) + 1):
            incorrect_res = incorrect_res ^ i
        
        answer = correct_res ^ incorrect_res

        return answer

