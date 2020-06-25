class solution:
	def reverseDuplicates(self, nums):
		if len(nums) < 1:
			return 0

		index = 0
		for i in range(1, len(nums)):
			if nums[index]!= nums[i]:
				index += 1
				nums[index] = nums[i]
		return index+1


def main():
	print('Entered Array is {}'.format(array))
	sol = solution()
	result = sol.reverseDuplicates(array)

	print('Array Length is {} '.format(result))


if __name__ == '__main__':
	arr_count = int(input())
	array = list(map(str, input().split()))

	main()