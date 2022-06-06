class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        if len(nums) % 2 != 0:
            return False
        
        nums.sort()
        
        op = []
        for i in range(0,len(nums)-1,2):
            op.append([nums[i],nums[i+1]])
            
        for i in op:
            if i[0] != i[1]:
                return False
        
        return True
        
        
        