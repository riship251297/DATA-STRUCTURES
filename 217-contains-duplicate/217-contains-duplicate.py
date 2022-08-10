class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for key,value in freq.items():
            if value > 1:
                return True
        
        return False
            
        