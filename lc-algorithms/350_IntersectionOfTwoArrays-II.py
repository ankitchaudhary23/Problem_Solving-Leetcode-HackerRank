class Solution:
	def intersetcion(self, nums1, nums2):
		# using two pointers method
		result = []
		nums1, nums2 = sorted(nums1), sorted(nums2)
		i, j = 0

		while True:
			try:
				if nums1[i] > nums2[j]:
					j+=1
				elif nums1[i] < nums2[j]:
					i+=1
				else:
					result.append(nums1[i])
					i+=1
					j+=1
			except IndexError:
				break
		return result

''' solution 1
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                result.append(nums1[i])
        return result
'''
''' solution 2
		for i in range(len(nums1)):
			for j in range(len(nums2)):
				print(j)
				if nums1[i] == nums2[j]:
					temp.append(nums1[i])
					break
		return temp'''


def main():
	sol = Solution()

	print('Array 1 :{}'.format(array1))
	print('Array 2 :{}'.format(array2))

	if len(array1)<len(array2):
		result = sol.intersetcion(array1, array2)
	else:
		result = sol.intersetcion(array2, array1)

	print('intersetcion of two array is {}'.format(result))


if __name__ == '__main__':

	array1 = list(map(int, input().split()))
	array2 = list(map(int, input().split()))
	main()