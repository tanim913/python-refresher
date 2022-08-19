class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx = nums [0]
        cur = 0
        
        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            mx = max(cur,mx)
            
        return mx        