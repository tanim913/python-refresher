

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        half = (len(nums1) + len(nums2)) // 2
        left, right = 0, len(nums1) - 1
        while True:
            cut1 = (left + right) // 2  # A
            cut2 = half - (cut1 + 1) - 1  # B

            nums1_left = nums1[cut1] if cut1 >= 0 else float("-infinity")
            nums1_right = nums1[cut1 + 1] if (cut1 + 1) < len(nums1) else float("infinity")
            nums2_left = nums2[cut2] if cut2 >= 0 else float("-infinity")
            nums2_right = nums2[cut2 + 1] if (cut2 + 1) < len(nums2) else float("infinity")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (len(nums1) + len(nums2)) % 2:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = cut1 - 1
            else:
                left = cut1 + 1
