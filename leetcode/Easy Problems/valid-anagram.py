class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i],0) + 1
            count_t[t[i]] = count_t.get(t[i],0) + 1

        for c in count_s:
            if count_s[c] != count_t.get(c, 0): #get 0 if c does not exist
                return False
        return True
    
  
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)



    
