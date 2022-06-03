class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for keys,values in freq.items():
            if values == 1:
                return keys
        