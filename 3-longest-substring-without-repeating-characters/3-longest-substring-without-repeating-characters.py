class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        op = {}
        i = 0
        ans = 0
        
        for j in range(len(s)):
            if s[j] in op:
                i = max(op[s[j]],i)
            
            ans = max(ans,j-i+1)
            op[s[j]] = j + 1
            
        return ans
        