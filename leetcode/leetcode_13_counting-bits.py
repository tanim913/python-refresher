
class Solution:
    
    def countBits(self, n: int) -> List[int]:
        l = list()
        for i in range (n+1):
            cnt = 0
            k = i 
            while k:
                k = k & (k-1)
                cnt += 1
            l.append(cnt)
        return l
        
# dp solution

class Solution:
    
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1 
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = dp [i - offset] + 1
        
        return dp

