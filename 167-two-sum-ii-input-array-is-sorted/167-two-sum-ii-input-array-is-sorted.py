class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(0,len(numbers)):
            diff = target - numbers[i]
            
            if numbers[i] in freq:
                return[freq[target - diff]+1,i+1]
            else:
                freq[diff] = i        