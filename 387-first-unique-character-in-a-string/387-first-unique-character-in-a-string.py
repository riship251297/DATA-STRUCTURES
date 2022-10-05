class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for key,values in freq.items():
            if values == 1:
                index_value = s.index(key)
                return index_value
        
        return -1
        