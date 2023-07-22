class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        time complexity : o(n)
        space complexity: o(n)
        calculating max_left and max_right array. the result for each positon 
        would be value = ( min(max_left[i] , max_right[i]) ) - height[i]. The final 
        result would the total sum of the value.
        '''
        max_left = []
        max_right = []
        m = 0
        sum = 0
        for h in height:
            m = max(m,h)
            max_left.append(m)
        m =0
        for i in range(len(height)-1, -1, -1):
            m = max(m, height[i])
            max_right.append(m)
        max_right = max_right[::-1]

        for i in range(len(max_left)):
            val = ( min(max_left[i] , max_right[i]) ) - height[i]
            if val >= 0:
                sum += val
        return sum

########################################
# 
# time complexity : o(n)
# memory complexity : o(1)    

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        while left < right:
            '''
            as we are checking if height[left] < height[right] then we do not need to check if max_right
            smaller or not because we would move the pointer (left) because it is smaller than the right 
            pointer at the first place. and max left is the min value. and from it we can substract the 
            height of the curruent left index.
            '''
            if height[left] < height[right]:
                left += 1
                max_left = max(max_left, height[left])
                res += max_left - height[left]
                '''
                    about the res += leftMax - height[l], at the line above it.
                > leftMax = max(leftMax, height[l])

                    If leftMax is less than (or equal to) height[l], we set leftMax equal to height[l] and then subtract height[l] from it, which would equal zero.
                    On the other hand, if leftMax is greater than height[l], we keep leftMax as is and subtract height[l] from it, which would be a positive value.
                    In either case, the result will always be greater than or equal to zero, which means you don't have to check for negatives.
                '''
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max_right - height[right]
        return res