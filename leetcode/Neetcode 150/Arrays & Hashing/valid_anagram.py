
# The approach is to use two different hashmaps to store the count of each character of the string. if the keys and count of two different 
# hashmap matches then it's a valid anagram 
# Time complexity is O(s+t); cause they have to iterate through every character of the string
# Space Complexity is O(s+t); cause they are creating two new hashmaps which is the size of s and t
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}

        for i in range(len(s)):
            # count_s[s[i]] = 1 + count_s[s[i]]
            count_s[s[i]] = count_s.get(s[i],0) + 1 #take s[i] and add 1 to the key. If the key does not exist yet , then take the defualt value 0.
            count_t[t[i]] = count_t.get(t[i],0) + 1
            
        # for s = "anagram" , t = "nagaram"
        # {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        # {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

        for idx in count_s:
            # key count isn't the same of the hashmap , then immidietly return false
            if count_s[idx] != count_t.get(idx, 0): #get 0 if c does not exist yet
                return False
        return True
    

  
    # def isAnagram2(self, s: str, t: str) -> bool:
    #     return Counter(s) == Counter(t)
    
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return ''.join(sorted(s)) == ''.join(sorted(t))



    
