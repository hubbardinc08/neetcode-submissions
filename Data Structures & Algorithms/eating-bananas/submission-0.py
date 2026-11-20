class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lbound, ubound = 1, max(piles)

        while lbound < ubound:
            mid = (lbound + ubound) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid   # integer ceil, avoids float issues

            if hours > h:
                lbound = mid + 1   # too slow, need a faster speed
            else:
                ubound = mid       # mid works, but a slower speed might too

        return lbound

