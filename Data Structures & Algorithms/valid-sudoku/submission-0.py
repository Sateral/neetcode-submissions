class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colHash = defaultdict(list)
        rowHash = defaultdict(list)
        subSquare = defaultdict(list)
        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                # Check if unique in column
                if (num in colHash[col] or
                    num in rowHash[row] or
                    num in subSquare[(row // 3, col // 3)]):
                    return False
                    
                colHash[col].append(num)
                rowHash[row].append(num)
                subSquare[row // 3, col // 3].append(num)
            
        return True

                

                