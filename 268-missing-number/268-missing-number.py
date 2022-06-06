class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        freq = {}
        
        for i in nums:
            freq[i] = 1
            
        for i in range(0,len(nums)+1):
            if i not in freq:
                return i