class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == '':
            return 0
        if needle not in haystack:
            return -1
        if needle in haystack:
            haystack = haystack.replace(needle,'.')
            
            return haystack.index('.')
        
        
       
    