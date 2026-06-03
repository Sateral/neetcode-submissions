class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        cell_hash = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == '.':
                    continue 

                if (char in row_hash[r] or
                    char in col_hash[c] or
                    char in cell_hash[(r//3,c//3)]):
                    return False

                row_hash[r].add(char)
                col_hash[c].add(char)
                cell_hash[(r//3,c//3)].add(char)

        return True