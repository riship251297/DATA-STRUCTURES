class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle in haystack:
            haystack = haystack.replace(needle,'.')
            
            index_value = haystack.index('.')
            return index_value
        
        return -1
        