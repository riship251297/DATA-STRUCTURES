class Solution:
    def reverse(self, x: int) -> int:
        
        negative = False
        
        x = list(str(x))
        if x[0] == '-':
            negative = True
            x = x[1:]
            
        x = int(''.join(x[::-1]))
        
        if x < -2**31 or x > 2**31:
            return 0
        
        if negative:
            return -x
        else:
            return x
        
        
        
      
    
    
    
    
    
    
   
        # If the number was negative just return its negative
        if negative:
            return -x
        return x