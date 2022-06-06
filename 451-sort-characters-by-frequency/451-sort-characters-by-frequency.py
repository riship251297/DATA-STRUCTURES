class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        op = sorted(freq.items(),key = lambda x:-x[1])
        
        lp = []
        for i in op:
            lp.append(i[0]*i[1])
        
        return ''.join(lp)
        
        