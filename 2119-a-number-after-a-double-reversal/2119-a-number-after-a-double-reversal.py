class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        if len(str(num)) == 1:
            return True
        
        else:
            if num % 10 == 0:
                return False
            else:
                x = list(str(num))
                x = int(''.join(x[::-1]))
                
                return x
                