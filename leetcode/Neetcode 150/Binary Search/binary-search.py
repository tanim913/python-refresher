# log2n= x => 2^x = n times
# log n algorithm

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            # mid = l + ((r-l) // 2) 
            '''
                dist between right and left is the total length.
                dividing it by two would be half of the distance.
                then we add the l because from the starting point
                to the half away would be mid point
            '''
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1