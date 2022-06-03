class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left = []
        middle = []
        right = []
        
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                right.append(i)
                
        left.extend(middle)
        left.extend(right)
        
        return left
        