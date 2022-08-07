class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        count = 0
        if n == 1 or n == 0:
            return 0
        
        while n > 0:
            if n == 1:
                return count 
            if n % 2 == 0:
                count += int(n / 2)
                n = n / 2
            if n % 2 != 0:
                count += int((n-1) / 2)
                n = ((n - 1) / 2) + 1
                
                
        return int(count)
                
        
        