class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        n = 9
        m = 9
        # print("start")
        for i in range(n):
            rowSet: set[str] = set()
            for j in range(m):
                s = board[i][j]
                if s != "." and s in rowSet:
                    # print("row:: ")
                    return False
                rowSet.add(s)

        # print("row pass")

        # col check
        for i in range(n):
            colSet: set[str] = set()
            for j in range(m):
                s = board[j][i]
                if s != "." and s in colSet:
                    return False
                colSet.add(s)
        
        # print("col pass")

        boxes : List[List[int]] = [
                                [0,0],[0,3],[0,6],
                                [3,0],[3,3],[3,6],
                                [6,0],[6,3],[6,6],    
                                ]
        
        for i in range(len(boxes)):
            x = boxes[i][0]
            y = boxes[i][1]

            boxSet: set[str] = set()
            for j in range(3):
                for k in range(3):
                    s = board[x+j][y+k]
                    if s != "." and s in boxSet:
                        return False
                    boxSet.add(s)

        # print("box pass")

        return True