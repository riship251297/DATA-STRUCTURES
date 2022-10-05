class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        freq = {}
        for i in nums:
            freq[i] = 1
            
        ele = []
        for i in range(1,len(nums)+1):
            if i in freq:
                pass
            else:
                ele.append(i)
            
        return ele
        