class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # selecting the row that may contain the specific target
        top, bottom = 0, rows-1 # selecting the top row as 0 and the bottom row is the last row
        while top <= bottom :
            mid = (top + bottom) // 2 # calculating the mid row 
            if target > matrix[mid][-1]:
                '''
                    1 2 3
                    4 5 6
                    7 8 9
                    suppose the target is 7
                    and the last value of the mid row is smaller 
                    than 7. In that case the top row would be mid + 1
                '''
                top = mid + 1
            elif target < matrix[mid][0]:
                '''
                    1 2 3
                    4 5 6
                    7 8 9
                    suppose the target is 3
                    and the first value of the mid row is greater than 
                    3. In that case the bottom would be mid - 1
                '''
                bottom = mid - 1
            else: 
                break
        if not top <=bottom:
            '''
                if going out the loop caused by anything other than the break then we haven't found 
                any row than can contain the target
            '''
            return False

        mid = (top + bottom) // 2 #calculating the mid row
        left, right = 0, cols-1 #calculating the left and right pointer
        while left <= right:
            '''
                this section is like liner binary search
            '''
            m = (left + right) // 2
            if target > matrix[mid][m]:
                left = m + 1
            elif target < matrix[mid][m]:
                right = m - 1
            else:
                return True
        return False