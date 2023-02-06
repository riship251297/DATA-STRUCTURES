class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        wordss1 = Counter(words1)
        wordss2 = Counter(words2)
        count = 0
        
        for key,value in wordss1.items():
            if value == 1:
                if wordss2[key] == 1:
                    count += 1
                    
        return count 