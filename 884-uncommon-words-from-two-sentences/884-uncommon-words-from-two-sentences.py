class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        op = []
        
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        
        
        freq = {}
        for i in s1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for i in s2:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        
        for k,v in freq.items():
            if v == 1:
                op.append(k)
                
        return op