class Solution:
	def rotate(self, board):
		'''
		type matrix: List[List[int]]
		rtype: void, modify matrix in-place
		'''
		matLen = len(matrix[0])

		for i in range(matLen):
			for j in range(i,matLen):
				board[i][j], board[j][i] = board[j][i], board[i][j]

		# reverse column 
		for i in range(matLen):
			matrix[i].reverse()
		return board

def main():
	sol = Solution()
	result = sol.rotate(matrix)
	print('Is Sudoku Valid {}'.format(result))


if __name__ == '__main__':
	matrix = [  [1,2,3],
				[4,5,6],
				[7,8,9]
			  ]
	main()