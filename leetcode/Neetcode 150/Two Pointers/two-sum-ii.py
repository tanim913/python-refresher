class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            '''
                depending on the result of the sum we need move the left and the right pointer.
                if we need to increase the sum then we increase the left pointer because if we
                move forward the numberes value will eventually increase because the list is in
                sorted order. Also if we need to decrease the sum then we decrease the right 
                pointer until we can ultimately get the sum == target
            '''
            sum = numbers[left] + numbers[right]
            if sum > target: #if sum is already bigger than the target then decrease the right pointer because we need reduce the total as the list is sorted
                right = right - 1
            elif sum < target:
                left = left + 1
            else:
                return [left + 1, right+1]
        return 