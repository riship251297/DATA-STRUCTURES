class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        freq = {}
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] in freq:
                    freq[mat[i][j]] += 1
                else:
                    freq[mat[i][j]] = 1
        
        op = []
        for k,v in freq.items():
            if v == len(mat):
                op.append(k)
        if len(op) == 0:
            return -1
        
        return min(op)