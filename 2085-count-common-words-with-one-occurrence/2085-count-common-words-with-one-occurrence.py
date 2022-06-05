class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        freq1 = {}
        freq2 = {}
        
        for i in words1:
            if i in freq1:
                freq1[i] += 1
            else:
                freq1[i] = 1
                
        for i in words2:
            if i in freq2:
                freq2[i] += 1
            else:
                freq2[i] = 1
        
        op = []
        op2 = []
        for k,v in freq1.items():
            if v == 1:
                op.append(k)
                
        for k,v in freq2.items():
            if v == 1:
                op2.append(k)
         
        count = 0
        for i in op:
            if i in op2:
                count += 1
            
        return count
                