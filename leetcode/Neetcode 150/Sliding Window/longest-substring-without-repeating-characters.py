class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            '''
            as long as the right pointer is getting the character that was added to the set earlier
            it is removing the character at left pointer and increasing the left pointer at the same
            time. But if the character was not it right pointer it adds to the set and calculate the 
            distance. The distance is right - left + 1 because the left and right pointer is 0 indexed
            '''
            while s[right] in char:
                char.remove(s[left])
                left += 1
            char.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len