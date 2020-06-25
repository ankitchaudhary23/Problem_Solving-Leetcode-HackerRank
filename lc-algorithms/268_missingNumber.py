class Solution:
	def missingNumber(self,nums):
		'''
		type nums: list[]
		rtype: return int
		'''
		#Bit Manipulation		
		missing = len(nums)
		for i, num in enumerate(nums):
			missing ^= i^num
		return missing

'''#Gauss's Formula [using PEMDAS]
		actual_sum = sum(nums)
		expected_sum = len(nums)*(len(nums)+1)//2
		print(expected_sum)
		return expected_sum - actual_sum
'''


def main():
	sol = Solution()
	result = sol.missingNumber(array)
	print(len(array))
	print('Given array {}'.format(array))
	print('Missing number {}'.format(result))


if __name__=='__main__':
	array = list(map(int, input().split()))
	main()