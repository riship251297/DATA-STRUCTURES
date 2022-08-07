class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            
        op = []
        
        fre = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        print(fre)
        
        for i in range(k):
            op.append(fre[i][0])
            
        return op
            
            
        