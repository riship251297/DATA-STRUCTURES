class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        freq = {}
        for i in nums:
            freq[i] = 1
        
        missing = []
        for i in range(len(nums)+1):
            if i in freq:
                pass
            else:
                missing.append(i)
                
        return missing[0]
        