class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            #left sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target and nums[mid] >= target: #left <= target <=mid
                    right = mid - 1
                else:
                    left = mid + 1
            #right sorted
            else: #mid <= target <=right
                if nums[mid] <= target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
