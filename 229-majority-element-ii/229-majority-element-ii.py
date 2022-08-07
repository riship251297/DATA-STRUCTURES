class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        op = []
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        print(freq)
                
        for key,value in freq.items():
            if value > len(nums) / 3:
                op.append(key)
                
        return op