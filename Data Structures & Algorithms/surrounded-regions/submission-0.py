class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            j = 0
            while j < len(board[0]):
                if board[i][j] == 'O':
                    def dfs(i, j):
                        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == 'X' or board[i][j] == 'V':
                            return
                        #otherwise spot is in board and an O
                        board[i][j] = 'V'
                        dfs(i + 1, j)
                        dfs(i - 1, j)
                        dfs(i, j + 1)
                        dfs(i, j - 1)
                    
                    dfs(i, j)
                if i != 0 and i != len(board) - 1 and j == 0:
                    j = len(board[0]) - 1
                else:
                    j += 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'


