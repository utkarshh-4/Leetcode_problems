
# lambda function approach
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        unordered_map={
            "+":lambda a,b:a+b,
            "-":lambda a,b:a-b,
            "/":lambda a,b:int(a/b),
            "*":lambda a,b:(a*b)
        }

        for token in tokens:
            if token not in unordered_map:
                stack.append(int(token))
            else:
                b=stack.pop()
                a=stack.pop()
                stack.append(unordered_map[token](a,b))

        return stack[-1]

#normal approach


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

        return stack[-1]
