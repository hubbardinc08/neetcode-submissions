class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        max_area = 0
        curr_area = 0

        while (lp < rp):
            curr_area = (rp - lp) * min(heights[lp], heights[rp])
            max_area = max(curr_area, max_area)

            if (heights[lp] <= heights[rp]):
                lp += 1
            else:
                rp -= 1

        return max_area

