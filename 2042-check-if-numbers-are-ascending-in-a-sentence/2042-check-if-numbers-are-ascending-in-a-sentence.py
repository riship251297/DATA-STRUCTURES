class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        nums = s.split(' ')
        prev = pow(-2,31)
        
        for i in s.split(' '):
            if i.isdigit():
                current = int(i)
                print(current,prev)
                if current <= prev:
                    return False
                else:
                    prev = current
        return True
        
        