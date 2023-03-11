class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)] 
        pair.sort(reverse=True)
        stack = []
        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        '''
        i) making pair from given position and speed list 
        ii) sort the array in reverse order according the position 
        iii) calculating time by (target - position) / speed and append them to a stack
        iv) if the below condition gets true then two car fleet becomes one car, so we need to pop the stack
        v) at last the size of the stack would determine how many car fleet would happen

        ------------------------------------------------------------------------------------------------------------------------
            t=20           t=12            t=12                    t=4                t=8                t=7            t=5

        |   20  |---->| car fleet occured even if a single car would reach alone at the target point
        |   12  |---->| car fleet occured cuase both two car would reach to the end point at the same time 
        |   12  |______^
        |   4   |----> stack [-1]    |car fleet occured cause the faster car had to slow down for the slow car in front of it
        |   8   |----> stack [-2]____^
        |   7   |----> car fleet didnt occur because the faster car would reach to the target earlier
        |   5   |_____^       
        '''
