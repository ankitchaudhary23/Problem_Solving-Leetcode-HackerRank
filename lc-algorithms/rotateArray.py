class Solution:
	def rotateArray(self, nums, k):
		# @param nums, list of integer; k, steps
		# @return nothin, modifying list in-place
		n = len(nums)
		k = k % n
		nums[:] = nums[n-k:] + nums[:n-k]
		return nums


def main():
	print('Given Array: {}'.format(array))
	sol = Solution()
	result = sol.rotateArray(array, steps)
	print(result)


if __name__ == '__main__':
	arrCount =  int(input())
	steps = int(input())
	array = list(map(str, input().split()))
	main()