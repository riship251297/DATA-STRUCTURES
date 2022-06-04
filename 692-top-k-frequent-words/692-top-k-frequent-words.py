class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = {}
        for i in words:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        op = sorted(freq.items(),key= lambda x:(-x[1],x[0]))
        
        print(op)
        po = []
        for i in range(k):
            po.append(op[i][0])
            
        return po
            
            