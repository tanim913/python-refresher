class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) -1
        
        while left < right: # can't be equal cause there would be 1 index diff. to calculate area
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res