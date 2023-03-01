'''
TC: O(n^2)
SC: O(n^2)

'''
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            Using three different defaultdict for rows , columns and 3X3 square.
            for rows defaultdict the key would be the row index
            for columns defaultdict the key would be the column index
            for square defaultdict the key would be the pair of two index (row // 3, col // 3) 
            to get remind index of three 3x3 square from the 9x9 square 
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or 
                    board[row][col] in square[(row//3,col//3)]):
                    return False # checking if the values already exists in according defaultdicts
                ''' 
                adding the values in each defaultdict to specific keys
                
                '''
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                square[(row//3,col//3)].add(board[row][col])
        return True