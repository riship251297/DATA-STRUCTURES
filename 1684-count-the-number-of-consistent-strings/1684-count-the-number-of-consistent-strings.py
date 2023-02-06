class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = [*allowed]
        count = 0
        current = ''
        for i in words:
            current = [*i]
            flag = True
            for j in current:
                if j in allowed:
                    if flag == False:
                        flag == False
                    else:
                        flag = True
                else:
                    flag = False
            if flag == True:
                count += 1
            else:
                pass
            
        return count
            
        