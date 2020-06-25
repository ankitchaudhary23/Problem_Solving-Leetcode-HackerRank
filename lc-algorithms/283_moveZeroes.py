class Solution:
	def moveZeroes(self, nums):
		idx = 0

		for i in range(len(nums)):
			if nums[i] != 0:
				nums[i], nums[idx] = nums[idx], nums[i]
				idx+=1
		return nums


def main():
	sol = Solution()
	result = sol.moveZeroes(array)
	print('Moved Zeroes at the end: {}'.format(result))


if __name__ == '__main__':
	array = list(map(int, input().split()))
	print('Given Array: {}'.format(array))
	main()