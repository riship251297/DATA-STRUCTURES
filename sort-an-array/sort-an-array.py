class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def merge(left_list,right_list):
            
            left_cursor = right_cursor = 0
            result = []
            
            while left_cursor < len(left_list) and right_cursor < len(right_list):
                if left_list[left_cursor] < right_list[right_cursor]:
                    result.append(left_list[left_cursor])
                    left_cursor += 1
                else:
                    result.append(right_list[right_cursor])
                    right_cursor += 1
            
            result.extend(left_list[left_cursor:])
            result.extend(right_list[right_cursor:])
            
            return result
        
        if len(nums) <= 1:
            return nums

        pivot_element = int(len(nums) / 2)
        left_list = self.sortArray(nums[0:pivot_element])
        right_list = self.sortArray(nums[pivot_element:])

        return merge(left_list,right_list)
    
        
        
        