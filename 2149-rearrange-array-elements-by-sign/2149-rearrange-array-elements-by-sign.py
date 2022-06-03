class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positive = []
        negative = []
        
        
        
        for i in nums:
            if i < 0 :
                negative.append(i)
            else:
                positive.append(i)
        main = []       
        for i in range(int(len(nums) / 2)):
            main.append(positive[i])
            main.append(negative[i])
            
            
        return main
            
            
        