class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if (len(nums) == 0):
            return 0

        currLongest = 1
        prevNum = nums[0]
        currCounter = 1

        for i in range(1, len(nums)):
            if (nums[i] == prevNum):
                continue
            if (nums[i] - prevNum == 1):
                currCounter += 1
                prevNum = nums[i]
            else:
                currCounter = 1
        
            currLongest = max(currLongest, currCounter)
            prevNum = nums[i]
            
        return currLongest

