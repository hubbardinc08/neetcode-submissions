class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        mp = (lp + rp) // 2

        if (nums[lp] == target):
            return lp
        if (nums[rp] == target):
            return rp

        while mp > lp:
            if (nums[mp] == target):
                return mp
            elif (nums[mp] > target):
                rp = mp
                mp = (lp + rp) // 2
            else:
                lp = mp
                mp = (lp + rp) // 2
        
        return -1