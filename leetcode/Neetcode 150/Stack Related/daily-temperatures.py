class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= stack[-1][1]:
                stack.pop()
            if stack and temperatures[i] < stack[-1][1]:
                result[i] = stack[-1][0] - i
            stack.append((i,temperatures[i])) 
        return result 
            


'''
travesing from the behind of the temperature array. 
----> while stack is not empty and the current temperature 
      value is greater than the top value of the stack then keep poping
----> if the stack is not empty and current temperature value 
      is less than the top of the stack , that means we got a higher value of 
      the current temperature, so store the result to that index
-----> keep pushing the pair of index and value to the stack 
'''
