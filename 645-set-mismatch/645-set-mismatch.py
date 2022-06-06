class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        freq = {}
        op = []
        for i in nums:
            if i in freq:
                freq[i] += 1
                
            else:
                freq[i] = 1
                
        for k ,v in freq.items():
            if v == 2:
                op.append(k)
        
        for i in range(1,len(nums) + 1):
            if i not in freq:
                op.append(i)
                
        return op
                
        
        