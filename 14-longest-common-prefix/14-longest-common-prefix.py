class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        min_length = len(min(strs,key=len))
        ele = ''
        for i in range(min_length):
            c = strs[0][i]
            
            if all(a[i] == c for a in strs):
                ele+=c
            else:
                break
        return "".join(ele)
            
                
        