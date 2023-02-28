'''
TC : O(n)
SC : O(1) ; result array does not contain extra memory
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []
        '''
        computing the prefix array where result[i] contains the multiplication result of the previous values
        '''
        for i in nums:
            result.append(product)
            product = product * i
        
        postfix = 1 
        
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * postfix # calculating result multiplying prefix(result[i]) and postfix
            postfix = postfix * nums[i] #updating postfix value by multiplying by nums[i]
            
        return result
    
    '''
        class Solution:
            def productExceptSelf(self, nums: List[int]) -> List[int]:
                #---initialise prefix postfix and result array---
                prefix = [1 for i in range(len(nums))]
                postfix = [1 for i in range(len(nums))]
                res = [1 for i in range(len(nums))]
                product = 1
                #---creating prefix array---
                for i in range(len(nums)):
                    product = product * nums[i]
                    prefix[i] = product
                product = 1
                #---creating postfix array---
                for i in range(len(nums) -1, -1, -1):
                    product = product * nums[i]
                    postfix[i] = product

                # res[0] = 1 * postfix[1]
                # res[len(nums)-1] = prefix[len(nums) -2] * 1
                # for i in range(1, len(nums)-1, 1):
                #     res[i] = prefix[i-1] * postfix[i+1]

                # --- calculating result array by multiplying previous prefix value and next postfix value of the current index ---
                for i in range(0, len(nums), 1):
                    if i == 0:
                        res[i] = 1 * postfix[i+1] # when it's first index prefix is 1
                    if i == len(nums)-1:
                        res[i] = prefix[len(nums)-2] * 1 # when it's last index postfix is 1
                    if i !=0 and i!= len(nums)-1:
                        res[i] = prefix[i-1] * postfix[i+1]
                return res


    '''