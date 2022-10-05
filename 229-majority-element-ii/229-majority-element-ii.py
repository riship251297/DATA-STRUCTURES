class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = {}
        n = len(nums) / 3
        
        ele = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for key,values in freq.items():
            if values > n:
                ele.append(key)
                
        return ele
        