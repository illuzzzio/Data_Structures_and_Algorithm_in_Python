class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c =="+":
                stack.append(stack.pop()+stack.pop())

            elif c=="-":
                a,b = stack.pop(),stack.pop()
                stack.append(int(b-a))

            elif c=="*":
                a,b = stack.pop(), stack.pop()
                stack.append(int(a*b))

            elif c == "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a)) # for div and sub as we know pop is from last so a is last and b is first 

            else:
                stack.append(int(c))
        return stack[-1]
        