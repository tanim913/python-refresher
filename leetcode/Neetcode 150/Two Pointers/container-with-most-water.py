class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
            we are using two pointers to make sure that the height of each side
            is maximum. so if the side of the left pointer is smaller than the right side
            our goal would be increment the left side to get the max area. the same way we would
            decrease the right side pointer if it is samller than the left side height.
            we calculating the area by width * height where width is the distance between 
            two pointer and the height would be the minimum height between two heights.
        '''
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(area, res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res