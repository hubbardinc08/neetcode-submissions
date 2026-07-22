class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []
        s = []

        for i in range(len(nums)):
            if (i == 0):
                left_product.append(1)
                right_product.append(1)
                continue
            
            left_product.append(left_product[i - 1] * nums[i - 1])
            right_product.append(right_product[i - 1] * nums[len(nums) - i])

        for i in range(len(nums)):
            s.append(left_product[i] * right_product[len(nums) - i - 1])
    
        return s

# [1, 1, 2, 8]
# [1, 6, 24, 48]