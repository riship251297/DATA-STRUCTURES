class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        result = []
        
        wordss1 = Counter(s1.split(' '))
        wordss2 = Counter(s2.split(' '))
        
        print(wordss1,wordss2)
        
        for key,value in wordss1.items():
            print(key,value)
            if value == 1:
                if key not in wordss2:
                    result.append(key)
                    
        for key,values in wordss2.items():
            if values == 1:
                print(key)
                if key not in wordss1:
                    result.append(key)
                        
        return result
        
        
        