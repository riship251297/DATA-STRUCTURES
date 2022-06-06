class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        op = []        
        for k,v in freq.items():
            if v == 2:
                op.append(k)
                
        return op
        