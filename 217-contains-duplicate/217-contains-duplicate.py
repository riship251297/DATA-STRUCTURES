class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for key,values in freq.items():
            if values >= 2:
                return True
            
        return False
        