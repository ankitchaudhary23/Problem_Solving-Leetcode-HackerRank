class Solution:
	def isValidSudoku(self, board):
		rows = [set() for i in range(9)]
		cols = [set() for i in range(9)]
		matX = [set() for i in range(9)]

		for i in range(9):
            for j in range(9):
            	cur = board[i][j]
                if cur != '.':
                    
                    k = (i // 3 ) * 3 + j // 3
                
                    if cur not in rows[i]: rows[i].add(cur)
                    else: return False
                    
                    if cur not in cols[j]: cols[j].add(cur)
                    else: return False
                
                    if cur not in mMat[k]: mMat[k].add(cur)
                    else: return False
        return True
       


def main():
	sol = Solution()
	result = sol.isValidSudoku(matrix)
	print('Is Sudoku Valid {}'.format(result))


if __name__ == '__main__':
	matrix = [  ["5","3",".",".","7",".",".",".","."],
				["6",".",".","1","9","5",".",".","."],
				[".","9","8",".",".",".",".","6","."],
				["8",".",".",".","6",".",".",".","3"],
				["4",".",".","8",".","3",".",".","1"],
				["7",".",".",".","2",".",".",".","6"],
				[".","6",".",".",".",".","2","8","."],
				[".",".",".","4","1","9",".",".","5"],
				[".",".",".",".","8",".",".","7","9"]
			]
	main()