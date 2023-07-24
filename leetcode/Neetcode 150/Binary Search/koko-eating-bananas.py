class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        '''
            piles = [3,6,7,11], h = 8
            koko has to eat p bananas in k bananas/hour.
            so for k banana/ hour, k can be from 1 to the max 
            pile size from the piles. we can check and calculate 
            total hour for every number from 1 to max(piles) but that 
            would be a TLE. so we chose Binary search method. where if 
            we get a time that is less than or equal to required h then 
            we look for even smaller mid(k). so we shift the right pointer 
            before the mid. but if we get a time which is larger than the 
            given h then we increase the speed so that we can get the minimum 
            speed to finish the pile.
        '''
        ans = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans