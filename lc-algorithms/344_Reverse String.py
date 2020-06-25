class Solution:
	def reverseString(self, array):
		left, right = 0, len(array)-1
		while left < right:
			array[left], array[right] = array[right], array[left]
			left += 1
			right -= 1
		return array
		
	'''
		self.temp = []
		self.temp = array[::-1]
		return self.temp
	'''

	''' in-built function

		array.reverse()
		return array
	'''
	''' backward iteration

		self. temp = []
		for i in range(len(array)-1, -1, -1):
			self.temp.append(array[i])
		return self.temp
	'''


def main():
	print('String is : {}'.format(array))

	sol = Solution()
	res = sol.reverseString(array)

	print('Reversed String : {}'.format(res))


if __name__ == '__main__':
	arr_count = int(input())
	array = list(map(str, input().split()))

	main()
