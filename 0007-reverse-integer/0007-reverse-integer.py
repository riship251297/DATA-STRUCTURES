class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
 

        p = []
        temp = 0
        if x < 0:
            p = str(x)[::-1].strip('-')
            p = int(p) * -1
            if p < INT_MIN:
                return 0
            else:
                return p
        else:
            p = str(x)[::-1]
            if int(p) > INT_MAX:
                return 0
            else:
                return int(p)
            