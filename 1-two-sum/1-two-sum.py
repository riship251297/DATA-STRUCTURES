class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        difference = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in difference:
                return [i,difference[diff]]
            
            difference[nums[i]] = i
        