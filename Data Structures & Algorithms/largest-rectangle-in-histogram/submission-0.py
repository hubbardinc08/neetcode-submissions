class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rightLimiter = []
        leftLimiter = []
        stackHeights = []

        for i in range(len(heights)):
            rightLimiter.append(-1)
            leftLimiter.append(-1)

        # right limiter
        for i in range(len(heights)):
            if (len(stackHeights) == 0):
                stackHeights.append([heights[i], i])
                continue
            
            while (len(stackHeights) > 0 and heights[i] < stackHeights[-1][0]):
                rightLimiter[stackHeights.pop()[1]] = i
            
            stackHeights.append([heights[i], i])
        
        while len(stackHeights) > 0:
            rightLimiter[stackHeights.pop()[1]] = len(heights)
        
        # left limiter
        for i in range(len(heights) - 1, -1, -1):
            if (len(stackHeights) == 0):
                stackHeights.append([heights[i], i])
                continue
            
            while (len(stackHeights) > 0 and heights[i] < stackHeights[-1][0]):
                leftLimiter[stackHeights.pop()[1]] = i
            
            stackHeights.append([heights[i], i])
        
        while len(stackHeights) > 0:
            leftLimiter[stackHeights.pop()[1]] = -1
        
        # finding largest area
        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(heights[i] * (rightLimiter[i] - leftLimiter[i] - 1), maxArea)
        
        return maxArea



        

            
            