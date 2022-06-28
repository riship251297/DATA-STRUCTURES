class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        if len(s) < 3:
            return len(s)
        
        left , right = 0,0
        des = {}
        max_len = 2
        while right < len(s):
            des[s[right]] = right
            right += 1
            
            if len(des) == 3:
                del_index = min(des.values())
                del des[s[del_index]]
                
                left = del_index + 1
                
            max_len = max(max_len,right - left)
            
        return max_len
            