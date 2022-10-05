class Solution:
    def removeVowels(self, s: str) -> str:
        
        a = ['a','e','i','o','u']
        ele = ''
        
        for i in s:
            if i in a:
                pass
            else:
                ele += i
                
        return ele
                