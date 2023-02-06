class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        if len(sentence) < 26:
            return False
        else:
            alphabet = []
            start = ord('a')
            for i in range(26):
                alphabet.append(chr(start + i))
            
            p = [*sentence]
            for i in alphabet:
                if i not in p:
                    return False
            return True

        