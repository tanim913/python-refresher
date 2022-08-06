class Solution:
    List = []

    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set()

        for i in nums:
            if i in st:
                return True
            st.add(i)

        return False
