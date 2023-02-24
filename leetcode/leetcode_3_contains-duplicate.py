'''
    set in python only stores unique values as it's element. 
    so when we are about to add an element to the set, we need to check if
    that specific element already exist in the set. If it does then the list contain
    duplicates 
'''
class Solution:
    List = []

    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set()

        for i in nums:
            if i in st:
                return True
            st.add(i)

        return False
