class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums:
            return -1
        
        if target in nums:
            val = nums.index(target)
            return val
            
        