class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
             
        ele = []
        for key,values in freq.items():
            if values == 2:
                ele.append(key)
                
        return ele
        