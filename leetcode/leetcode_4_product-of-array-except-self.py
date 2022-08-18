class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []
        
        for i in nums:
            result.append(product)
            product = product * i
        
        product = 1
        
        for i in range(len(nums)-1, -1, -1):
            result[i] = product * result[i]
            product = product * nums[i]
            
        return result