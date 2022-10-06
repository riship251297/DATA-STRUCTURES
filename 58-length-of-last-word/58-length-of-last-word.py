class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        st = s.strip()
        sttt = list(st.split())
        
        return len(sttt[-1])