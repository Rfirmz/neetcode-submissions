from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        columnTable = defaultdict(set)
        rowTable = defaultdict(set)
        gridTable = defaultdict(set)

        for r, row in enumerate(board):
            for c, val in enumerate(row):

                if val == ".":
                    continue

                grid = (r // 3, c // 3)

                if val in rowTable[r] or val in columnTable[c] or val in gridTable[grid]:
                    return False
                
                rowTable[r].add(val)
                columnTable[c].add(val)
                gridTable[grid].add(val)
            
        return True