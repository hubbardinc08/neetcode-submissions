class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        left_pointer = 0
        right_pointer = len(s) - 1
        print(f"DEBUG: left pointer: {left_pointer}, right pointer: {right_pointer}")

        while (left_pointer < right_pointer):
            print(f"DEBUG:  left: {s[left_pointer]}, right: {s[right_pointer]}")
            if (s[left_pointer] != s[right_pointer]):
                return False
            
            left_pointer += 1
            right_pointer -= 1
        
        return True