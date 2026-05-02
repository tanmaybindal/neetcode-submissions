class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        def traverse_block(sr: int, sc: int) -> bool:
            freq_set = set()
            for r in range(sr, sr + 3):
                for c in range(sc, sc + 3):
                    val = board[r][c]
                    if val == ".":
                        continue
                    if val in freq_set:
                        print(val, "false")
                        return False
                    freq_set.add(val)
            return True

        # check all rows
        for r in range(rows):
            freq_set = set()
            for c in range(cols):
                val = board[r][c]
                if val == ".":
                    continue
                if val in freq_set:
                    print(val, "false")
                    return False
                freq_set.add(val)

        for c in range(cols):
            freq_set = set()
            for r in range(rows):
                val = board[r][c]
                if val == ".":
                    continue
                if val in freq_set:
                    print(val, "false")
                    return False
                freq_set.add(val)

        for r in range(0, rows, 3):
            for c in range(0, cols, 3):
                if not traverse_block(r, c):
                    print(r, c, "false")
                    return False

        return True
