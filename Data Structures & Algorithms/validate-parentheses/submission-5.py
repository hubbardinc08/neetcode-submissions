class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open_char = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if (char in open_char.keys()):
                stack.append(char)
            else:
                if (len(stack) == 0):
                    return False
                key = stack.pop()
                if (char != open_char[key]):
                    return False
        
        if (len(stack) == 0):
            return True
        else:
            return False