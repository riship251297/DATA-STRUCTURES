class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        fre = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in fre:
                return [i,fre[difference]]
            
            fre[nums[i]] = i
        