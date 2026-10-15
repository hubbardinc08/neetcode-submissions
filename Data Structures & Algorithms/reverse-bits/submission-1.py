class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            last_digit = n & 1
            result = (result << 1) + last_digit
            n = n >> 1
        
        return result