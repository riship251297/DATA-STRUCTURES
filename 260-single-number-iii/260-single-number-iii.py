class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        once = []
        for key,values in freq.items():
            if values == 1:
                once.append(key)
        
        return once
        