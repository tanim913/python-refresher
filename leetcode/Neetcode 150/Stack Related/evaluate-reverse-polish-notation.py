class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif char == "*":
                 stack.append(stack.pop() * stack.pop())
            elif char == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(char))
        return stack[0]
    '''
    using stack everytime when a number char would appear it would be converted into a integer and then pushed into the stack.
    if there is any of the four operator then previous two value of the stack would be calculated according to the operator 
    and would be appended in the stack. In case of divison and subtraction the order would be reverse. lastly the result would be 
    at the first index of the stack 
    '''