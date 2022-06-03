class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
                
            else:
                freq[i] = 1
        n = len(nums) 
        op = []
        for key,values in freq.items():
            if values > n / 3:
                print(values)
                op.append(key)
                
        return op
        