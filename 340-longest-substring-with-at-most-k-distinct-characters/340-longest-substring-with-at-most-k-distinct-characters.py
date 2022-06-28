class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if len(s) < k:
            return len(s)
        
        else:
            des = {}
            right,left = 0,0
            max_len = k
            while right < len(s):
                des[s[right]] = right
                right += 1
                
                if len(des) == k+1:
                    min_index = min(des.values())
                    del des[s[min_index]]
                    left = min_index + 1
                    
                max_len = max(max_len,right - left)
                
            return max_len
                    
                
        