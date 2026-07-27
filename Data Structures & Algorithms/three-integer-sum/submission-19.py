class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # p = 0
        # while True:
        #     if ((target - numbers[p]) in numbers):
        #         return [p + 1, numbers.index(target - numbers[p]) + 1]
            
        #     p += 1

        lp = 0
        rp = len(numbers) - 1

        lst = []

        while lp < rp:
            if (numbers[lp] + numbers[rp] > target):
                rp -= 1
            elif (numbers[lp] + numbers[rp] < target):
                lp += 1
            else:
                lst.append([numbers[lp], numbers[rp]])
                lp += 1
                rp -= 1
        
        return lst
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []
        visited = defaultdict(int)

        for i in range(len(nums) - 2):
            lp = i
            target = 0 - nums[lp]

            lst = self.twoSum(nums[lp + 1:], target)

            if (len(lst) != 0):
                for i in range(len(lst)):
                    c = ''.join(map(str, lst[i]))
                    if (visited[c] == 1):
                        continue
                    lst[i] = [nums[lp]] + lst[i]
                    visited[c] = 1
                    answer.append(lst[i])
        
        return answer


        