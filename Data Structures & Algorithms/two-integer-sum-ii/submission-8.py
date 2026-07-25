class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # p = 0
        # while True:
        #     if ((target - numbers[p]) in numbers):
        #         return [p + 1, numbers.index(target - numbers[p]) + 1]
            
        #     p += 1

        lp = 0
        rp = len(numbers) - 1

        while True:
            if (numbers[lp] + numbers[rp] > target):
                rp -= 1
            elif (numbers[lp] + numbers[rp] < target):
                lp += 1
            else:
                return [lp + 1, rp + 1]
                
            