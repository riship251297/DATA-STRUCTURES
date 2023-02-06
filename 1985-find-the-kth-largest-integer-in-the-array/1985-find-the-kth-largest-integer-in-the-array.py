class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        result = []
        for i in nums:
            result.append(int(i))
            
        res = sorted(result,reverse = True)
        
        return str(res[k-1])
        