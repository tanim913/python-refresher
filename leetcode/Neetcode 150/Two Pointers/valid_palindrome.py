class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1 #initialising two pointers 
        while l < r:
            while l < r and not self.isAlphanum(s[l]): #if the left character is not alphanumeric value then keep going left as long as it doesnot cross the right pointer.
                l = l + 1
            while l < r and not self.isAlphanum(s[r]): #if the right character is not alphanumeric value then keep going right as long as it doesnot cross the left pointer.
                r = r - 1
            if s[l].lower() != s[r].lower(): #if any of the character is not equal then immidietly return false
                return False
            l, r = l+1, r-1
        return True

    def isAlphanum(self, c):
        return ((ord('A') <= ord(c) <= ord('Z'))
                or (ord('a') <= ord(c) <= ord('z'))
                or (ord('0') <= ord(c) <= ord('9'))
                )
