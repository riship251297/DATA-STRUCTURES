class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        
        freq = {}
        for i in arr:
            freq[i] = 1
        
        count = 0
        n = sys.maxsize
        for i in range(1,n+ 1):
            if i not in freq:
                print(i)
                count += 1
                if count == k:
                    return i