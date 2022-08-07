class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        fre = sorted(freq.items(),key = lambda x:x[1],reverse=True)
        op = []
        
        print(fre)
        
        for key,value in fre:
            op.append(key * value)
            
        return ''.join(op)
                
        