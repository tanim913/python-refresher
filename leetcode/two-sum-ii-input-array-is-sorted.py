class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) -1
        l = []
        
        while left <= right:
            if numbers[left] + numbers[right] < target:
                left += 1
                
            if numbers[left] + numbers[right] > target:
                right -= 1
                
            if numbers[left] + numbers[right] == target:
                l.append(left+1)
                l.append(right+1)
                return l
            
        return -1