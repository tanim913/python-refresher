from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Find the maximum sliding window in an array of integers.

        Args:
            nums (List[int]): The input array of integers.
            k (int): The size of the sliding window.

        Returns:
            List[int]: The list containing the maximum values in each sliding window.

        Example:
            Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
            Output: [3, 3, 5, 5, 6, 7]
        """
        q, res = collections.deque(), []  # Use a deque for efficient operations.
        
        # Iterate through the array from left to right.
        for r in range(len(nums)):
            # Remove smaller elements from the deque.
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            # Add the current index to the deque.
            q.append(r)
            
            # Check if the window has enough elements.
            if r + 1 < k:
                continue
            
            # Check if the leftmost element is outside the window [r+1-k, r], remove it from the deque.
            # checking if the index at q[0] is smaller than left = r+1-k, if it is then just pop the index at left 
            if q[0] < (r + 1 - k): 
                q.popleft()
            
            # Append the maximum value in the current window to the result list.
            res.append(nums[q[0]])
        
        return res
