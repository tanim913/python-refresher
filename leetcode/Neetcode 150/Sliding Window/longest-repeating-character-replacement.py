class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, res, max_f = 0, 0, 0
        count = {}

        for right in range(len(s)):
            '''
            here we are using sliding window method to start from the beginning with
            right and left pointer. as the right pointer goes on, we keep calculating
            how many times the characters are found. and we store the max frequency 
            from the current character frequency and the max frequncy till low. Now to
            understand if a window length is valid we calculate the 
            validity = window length - max frequency <= k. if it is valid we store the highest
            window lenght to the result. but before that if the opposite scenario happens 
            which means window length - max frequency > k then we move our left pointer forward to 
            find for a window length and at the same time we need decrease the char freq at
            left pointer becuase it would not be inside the window.
            
            '''
            count[s[right]] = count.get(s[right], 0) + 1
            max_f = max(count[s[right]], max_f)
            if (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            res = max(right - left + 1, res)
        return res
