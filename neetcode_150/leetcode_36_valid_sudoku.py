class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows check 
        for i in range(0,9):
            store = set()
            for j in range(9):
                item = board[i][j]
                if item in store:
                    return False 
                elif item != ".":
                    store.add(item)      

        for i in range(9):
            store = set()
            for j in range(9):
                item = board[j][i]
                if item in store:
                    return False 
                elif item  != ".":
                    store.add(item)
        starting_points = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i,j in starting_points:
            s = set()
            for rows in range(i,i+3):
                for cols in range(j,j+3):
                    item = board[rows][cols]
                    if item in s:
                        return False
                    elif item !=".":
                        s.add(item)
        return True 

       
            
        