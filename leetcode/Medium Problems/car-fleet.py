class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)] # making list of pair by list comprehension
        '''
            sorting the pair in descending order to know whose position is the farthest away from the target. 
            target = 100, position = [0,2,4], speed = [4,2,1]
            pair would be [(4, 1), (2, 2), (0, 4)]
            
        '''
        pair.sort(reverse=True)
        stack = []
        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
