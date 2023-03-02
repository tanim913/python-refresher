class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {'[': -1, '{': -2, '(': -3, ']': 1, '}': 2, ')': 3}
        stack = []
        '''
        creating a map for the brackets. The opening bracket contains negative integer and the closing bracket contains 
        equvalent positive integer numbers of the specific closing bracket
        '''
        for char in s:
            if bracket_map[char] < 0:
                stack.append(char)
                '''
                pushing the character that are only openning brackets from the test string to the stack 
                '''
            else:
                if len(stack) == 0: #if there is no opening bracket then return false immidietly
                    return False
                top = stack[-1] #getting the top character from the stack which would be any of three opening brackets
                stack.pop()
                if bracket_map[top] + bracket_map[char] != 0: #if the opening bracket does not match with it's corresponding closing bracket the result would not be 0
                    return False 
        if len(stack) == 0: #if every opening bracket founds it's closing backet then the stack would be empty 
            return True
        return False