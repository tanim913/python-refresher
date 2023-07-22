class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        '''
            firstly we need to sort the given array so that we can apply the
            two sum ii advantage. taking first element and try to build three
            number from it. if the digit is consequtive same number then ignore 
            that case by continueing the outer loop for the next iteration.
            keeping the first number of the 3 numberset, for the rest of the two
            numbers we need to apply two pointer approach, where the left pointer
            would be index+1 and the right pointer would be the last index.
            total sum should be the number from the outer loop + the number for 
            left pointer and the number for the right pointer. They should be sum 
            upto 0. If the sum is less than 0 then increase the left pointer. 
            if the sum is greater than 0 then decrease the right pointer. if the 
            sum is 0 then we got a set of three numbers. But we are not done here.
            we need need to increase the left pointer for next two numbers.
            so we inrease our left pointer.we do not need to decrease the right 
            pointer because when the sum is larger than 0, it will automatically 
            happen in the loop. if after increasing the left pointer we still have
            consequtive number then we need to keep increasing until left pointer
            does not cross right pointer.
        '''
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]: #ignoring consequtive same numbers in the sorted array
                continue
            left, right = i+1, len(nums)-1
            while(left < right):
                tsum = n + nums[left] + nums[right]
                if tsum > 0:
                    right -= 1
                elif tsum < 0:
                    left +=1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1 #for the next number
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return res 