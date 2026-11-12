class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # for each O item check if all 4 dirs are x

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        ROWS, COLS = len(board), len(board[0])
        seen = set()
       
        def check(r, c):
            
            # cur flag
            board[r][c] = "1"

            for dr, dc in dirs:
                rdr, cdc = r + dr, c+dc

                # edge check
                if (rdr < 0 or cdc < 0 or
                    rdr == ROWS or cdc == COLS):
                    continue
                

                if (board[rdr][cdc] == "O"):
                    board[rdr][cdc] == "1"
                    check(rdr, cdc)
                

        for r in range(ROWS):
            for c in range(COLS):
                on_border = (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1)
                if (board[r][c] == "O" and on_border):
                    check(r,c)

        for r in range(ROWS):
            for c in range(COLS):

                if (board[r][c] == "O"):
                    board[r][c] = "X"
                elif (board[r][c] == "1"):
                    board[r][c] = "O"

