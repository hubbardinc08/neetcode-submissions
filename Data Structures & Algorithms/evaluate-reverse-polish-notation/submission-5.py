class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []
        opers = ['+', '-', '*', '/']

        for char in tokens:
            if (char in opers):
                v1 = vals.pop()
                v2 = vals.pop()

                if char == '+':
                    result = v2 + v1
                elif char == '-':
                    result = v2 - v1
                elif char == '*':
                    result = v2 * v1
                else:
                    result = int(v2 / v1)
            
                vals.append(result)
            else:
                vals.append(int(char))

        return vals.pop()