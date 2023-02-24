''' as we need to return a list of the index of the given list which contains numbers, 
    we need to create a map which would be contiously adding the index of the number
    until it gets the index of the difference from the target value to the currnt number
    of the list

    T.C : O(n) ; iterating through all the numbers of the string
    S.C : O(n) ; using a hashmap to potentially add every value to the hashmap from the list
'''
class Solution:
    List = []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, n in enumerate(nums):

            diff = target - n

            if diff in mp:
                return [mp[diff], i]

            mp[n] = i

        return
