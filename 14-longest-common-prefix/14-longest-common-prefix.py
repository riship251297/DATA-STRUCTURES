class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = ''
        
        for i in range(len(min(strs))):
            c = strs[0][i]
            
            if all(a[i] == c for a in strs):
                pre += c
                
            else:
                break
        return pre
        