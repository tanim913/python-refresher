'''
The main of this problem is to get the minimum value from the stack in O(1) time. for this we need to find the min value 
for each value that would be pushed in the main stack. 
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        '''
        calculating the min value up to the value that are pushed. if the min stack is empty then take the cuurent value as the min value
        '''
        if self.min_stack: 
            val = min(self.min_stack[-1], val) # on the top of the min_stack , there would be the most minimum among values that were pushed in the stack.
        else:
            val = val   # if the min stack is empty then take the current value as the most minimum value
            
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()