class Solution:
    def hammingWeight(self, n: int) -> int:
        total_ones = 0
        while (n > 0):
            total_ones += n & 1
            n = n >> 1

            print(n, total_ones)
        
        return total_ones


1011