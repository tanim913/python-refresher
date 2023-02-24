class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()

        for i, n in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                if n + nums[left] + nums[right] > 0:
                    right -= 1

                elif n + nums[left] + nums[right] < 0:
                    left += 1

                else :
                    res.append([n, nums[left], nums[right]])
                    left += 1 # for next number in the list

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
