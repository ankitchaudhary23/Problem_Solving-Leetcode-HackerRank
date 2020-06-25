class Solution:
	def reverseInteger(self, x):
		'''
		:type nums: int
		:rtype: int
		'''
		#return str(nums)[::-1]
		res = 0

		if x<0:
			symbol = -1
			x = -x
		else:
			symbol = 1

		while x:
			res = res*10 + x%10
			x //= 10

		return 0 if (res > pow(2,31)) else (res*symbol)


def main():
	print('Given array: {}'.format(array))
	sol = Solution()
	result = sol.reverseInteger(array)
	print('Returned indicies: {}'.format(result))


if __name__ == '__main__':
	#target = int(input())
	#array = list(map(int, input().split()))
	array = 123
	main()