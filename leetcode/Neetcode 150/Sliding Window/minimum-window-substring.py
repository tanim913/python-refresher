class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if the length of t is 0, then there's no need to proceed.
        if not len(t): return "" 

        # Initialize dictionaries to store the frequency of characters in t and the current window
        t_freq, window = {}, {}

        # Count the frequency of each character in string t.
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        # Initialize pointers and variables to keep track of the current window and characters found.
        left, have, need = 0 , 0, len(t_freq) 
        res , min_len = [-1, -1], float("inf")

        # Sliding window approach using two pointers, left and right.
        for right in range(len(s)):
            # Sliding window approach using two pointers, left and right.
            window[s[right]] = window.get(s[right], 0) + 1

            # Check if the current character is in t and if its frequency in the window matches its frequency in t.
            # If yes, increment the 'have' variable, which keeps track of characters found so far.
            if s[right] in t_freq and  window[s[right]] == t_freq[s[right]]:
                have += 1

            # While all characters in t are found at least once in the current window, try to minimize the window size.
            while have == need:
                # Update the minimum window size and save the left and right pointers in 'res'.
                if (right - left + 1) < min_len:
                    res = [left, right]
                    min_len = right - left + 1

                # Remove the leftmost character from the window and update its frequency.
                window[s[left]] -=1

                # Check if the removed character is in t and if its frequency in the window becomes less than its frequency in t.
                # If yes, decrement the 'have' variable, as we need to find this character again.
                if s[left] in t_freq  and window[s[left]] < t_freq[s[left]]:
                    have -=1

                # Move the left pointer to the right, as we try to minimize the window size.
                left +=1
                
        # Extract the minimum window substring using the 'res' pointers or return an empty string if no valid window found.
        left, right = res 
        return s[left: right+1] if min_len != float("inf") else ""

