class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        freq = {}
        n = len(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] in freq:
                    freq[nums[i][j]] += 1
                else:
                    freq[nums[i][j]] = 1
        op = []
        for key,values in freq.items():
            
            if values == n:
                op.append(key)
        return sorted(op)
                