class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        path = set()

        # helper for DFS
        def dfs(r, c, str_idx):
            if str_idx == len(word):
                return True
            
            # bounds + mismatch check
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[str_idx] or (r, c) in path):
                return False
            
            # 1. Mark the current node as visited
            path.add((r, c))
            
            res = (dfs(r-1, c, str_idx+1) or
                dfs(r+1, c, str_idx+1) or 
                    dfs(r, c-1, str_idx+1) or 
                    dfs(r, c+1, str_idx+1))

            path.remove((r, c))
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True

        return False
            

        

        