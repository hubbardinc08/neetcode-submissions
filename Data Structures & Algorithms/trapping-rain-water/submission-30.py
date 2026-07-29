class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = defaultdict(int)
        max_right = defaultdict(int)
        area = 0

        for i in range(len(height)):
            if (i == 0):
                max_left[i] = height[i]
                continue
            
            max_left[i] = max(max_left[i - 1], height[i])
        
            
        for i in range(len(height) - 1, -1, -1):
            if (i == len(height) - 1):
                max_right[i] = height[i]
                continue
            
            max_right[i] = (max(max_right[i + 1], height[i]))
        
        for i in range(len(height)):
            area = area + min(max_left[i], max_right[i]) - height[i]
        
        return area

