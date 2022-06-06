class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        n = len(s)
        
        freq = {}
        
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for k,v in freq.items():
            if k == letter:
                return int((v * 100) / n)
            
        return 0