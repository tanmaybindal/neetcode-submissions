class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        row_set = set()
        col_set = set()
        block_set = set()

        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val == ".":
                    continue

                r_key = (val, r)
                c_key = (val, c)
                b_key = (val, r // 3, c // 3)


                if r_key in row_set or c_key in col_set or b_key in block_set:
                    return False

                row_set.add(r_key)
                col_set.add(c_key)
                block_set.add(b_key)

        return True
