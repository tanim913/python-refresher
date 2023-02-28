class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        freq = [[] for i in range(len(nums) + 1)]
        ''' creating a list of empty lists to the size of total lenth of the given array so that even if 
            all the number is the same in the array it would not exceed the array size 
        '''
        result = []

        for n in nums:
            count[n] = count.get(n,0) + 1
        '''
            creating hashmaps that will contain the total count of each digit
        '''

        for digit, cnt in count.items():
            freq[cnt].append(digit)
        '''
        to each count append the list containing number that has the specific count
        '''

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        '''
        traversing the freq list of lists from behind and appending the numbers from the list until the len(result) becomes equal to k. 
        This works because top k elements are the numbers that were unique and sorted to the list accordingly to it's key.
        '''