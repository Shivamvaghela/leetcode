class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Step 1: Fill sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        # Step 2: Backtracking
        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in '123456789':
                            box_index = (r // 3) * 3 + (c // 3)
                            
                            if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                                # Place number
                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[box_index].add(num)

                                if backtrack():
                                    return True

                                # Undo (backtrack)
                                board[r][c] = '.'
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[box_index].remove(num)

                        return False
            return True

        backtrack()