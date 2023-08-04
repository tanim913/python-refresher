class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            the edge case: s1 can not be larger than 2
            and if s1 is empty then just return true 
            becuase false combination would be true in any 
            len for s2
        '''
        if len(s2) < len(s1): return False
        if not len(s1): return True
        '''
            s1_freq: A list of length 26 to store the frequency count of characters in s1. It uses the ASCII value difference to map each character to its corresponding index in the list.
            s2_freq: A list of length 26 to store the frequency count of characters in s2. It uses the ASCII value difference to map each character to its corresponding index in the list.
            left: An integer that will be used as the left pointer for the sliding window approach.
            match: An integer to keep track of how many characters have matching frequencies in s1 and s2
        '''
        s1_freq, s2_freq, left, match = [0]*26, [0]*26 , 0, 0
        
        '''
        This loop initializes the frequency count arrays s1_freq and s2_freq by going through the first len(s1) characters of both strings.
        For each character in s1, it increments the corresponding frequency count in s1_freq.
        For each character in s2, it increments the corresponding frequency count in s2_freq.
        '''
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        '''
             it also checks if the frequency of that character is equal in both s1 and s2, and if so, increments the match variable.
        '''
        for i in range (26):
            if s1_freq[i] == s2_freq[i]:
                match += 1
        '''
            Sliding window Portion:
            if upto the length of s1 index the match is 26 then when can return true instantly
            This loop uses the sliding window technique to check for permutations of s1 in s2.
            It starts from the index len(s1) in s2 and slides the window to the right until the end of s2.
            At each step of the window, it updates the frequency counts in s2_freq for the newly added character 
            at the right end of the window and removes the character at the left end of the window.
            It also updates the match variable based on the changes in frequencies.

        '''
        for right in range(len(s1), len(s2)):
            if match == 26: return True

            index = ord(s2[right]) - ord('a')
            s2_freq[index] += 1
            if s1_freq[index] == s2_freq[index]: match += 1
            elif s1_freq[index] + 1 == s2_freq[index] : match -= 1

            index = ord(s2[left]) - ord('a')
            s2_freq[index] -= 1
            if s1_freq[index] == s2_freq[index]: match += 1
            elif s1_freq[index] - 1 == s2_freq[index] : match -= 1
            left += 1

        '''
            after exiting from the loop if the value of the match is 26 in the last iteration 
            then it will return true or it will return False
        '''
        return match == 26

            
            

        
