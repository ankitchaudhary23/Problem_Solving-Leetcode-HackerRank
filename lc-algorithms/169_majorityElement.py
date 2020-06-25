class Solution:
	def majorityElement(self,nums):
		'''
		type nums: list[]
		rtype: return int
		'''
		majority_count = len(nums)//2
		for num in nums:
			count = sum(1 for elem in nums if elem == num)
			if count > majority_count:
				return num
		# using max function
        #return max(set(nums), key=nums.count)
'''#using Sorting
        nums.sort()
        return nums[len(nums)//2]
'''

def main():
	sol = Solution()
	result = sol.majorityElement(array)
	print(len(array))
	print('Given array {}'.format(array))
	print('Majority Element {}'.format(result))


if __name__=='__main__':
	array = list(map(int, input().split()))
	main()