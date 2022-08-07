class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for key,value in freq.items():
            if value > len(nums) / 2:
                if key == target:
                    return True
                
        return False
        