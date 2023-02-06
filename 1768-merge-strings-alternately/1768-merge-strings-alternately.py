class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        
        result = []
        if len(word1) == len(word2):
            
            for i in range(len(word1)):
                
                result.append(word1[i])
                result.append(word2[i])
                
            return "".join(result)
             
        
            
        min_length = min(len(word1),len(word2))
        index = 0
        if len(word1) == min_length:
            index = 1
        else:
            index = 2

        if index == 1:
            for i in range(len(word1)):
                result.append(word1[i])
                result.append(word2[i])
                if i == len(word1)-1:
                    result.extend(word2[i+1:])
        else:
            for i in range(len(word2)):
                result.append(word1[i])
                result.append(word2[i])
                if i == len(word2)-1:
                    result.extend(word1[i+1:])
            
        return "".join(result)
            
            
            
        