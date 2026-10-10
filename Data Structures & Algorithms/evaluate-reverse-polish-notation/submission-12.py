class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {
        "+": lambda x, y: x + y,
        "-": lambda y, x: x - y,
        "*": lambda x, y: x * y,
        "/": lambda y, x: int(x / y),
        }

        stack = list()

        for tok in tokens:

            if tok in ops:
                stack.append(ops[tok](stack.pop(), stack.pop()))
                continue
            
            stack.append(int(tok))

        return stack[-1]
            


