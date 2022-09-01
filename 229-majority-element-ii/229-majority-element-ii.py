class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        maj_list = []
        for key,value in freq.items():
            if value > len(nums) / 3:
                maj_list.append(key)
                
        
        return maj_list
        