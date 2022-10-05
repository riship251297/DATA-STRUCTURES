class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq = {}
        
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        vals = list(set(freq.values()))
        val = list(freq.values())
        
        if len(vals) == len(val):
            return True
        
        return False
        