class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            converting nums list into a set to avoid duplicates value of the list 
        '''
        num_set = set (nums)
        longest = 0
        for n in num_set:
            '''
            checking if previous number of a number already exist in the numset. 
            If it does not then it's the beginning of a new sequence.
            '''
            if n-1 not in num_set:
                len = 1
                '''
                to know how long the sequence is , we need to check if the next value exists in the set
                and adding 1 everytime it gets the next value 
                the loop will break if the consecutive next value does not exist in the numset
                '''
                while n+len in num_set:
                    len+=1
                longest = max(len, longest)
        return longest