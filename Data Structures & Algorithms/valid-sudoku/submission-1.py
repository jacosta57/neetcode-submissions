class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRows = defaultdict(set)
        seenCols = defaultdict(set)
        seenSquares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                current = board[i][j]

                if current == ".":
                    continue
                if (current in seenRows[i]
                 or current in seenCols[j]
                 or current in seenSquares[(i//3, j//3)]):
                    return False
                seenRows[i].add(current)
                seenCols[j].add(current)
                seenSquares[(i//3, j//3)].add(current)
        return True