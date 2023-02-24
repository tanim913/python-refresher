class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        l = list()

        for i in range(1, len(nums) + 1):
            l.append(i)
  
        return sum (l) - sum (nums)