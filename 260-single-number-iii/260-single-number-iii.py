class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        op = []       
        for keys,values in freq.items():
            if values == 1:
                op.append(keys)
                
        return op
        