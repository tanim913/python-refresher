class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                # 4 5 6 7 1 2 3
                left = mid + 1
            # if nums[right] > nums[mid]:
            # 5 6 1 2 2 3 4
            else :
                right = mid
        return nums[left]

