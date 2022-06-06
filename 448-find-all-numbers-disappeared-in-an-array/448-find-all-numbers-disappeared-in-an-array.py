class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        freq = {}
        
        for i in nums:
            freq[i] = 1
            
        op = []
        for i in range(1,len(nums) + 1):
            if i not in freq:
                op.append(i)
                
        return op
        