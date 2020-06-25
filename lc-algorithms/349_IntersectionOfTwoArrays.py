class Solution:
	def intersetcion(self, set1, set2):
		cmn = []
		return list(set1 & set2)
'''
		for num in set1:
			if num in set2:
				cmn.append(num)
		return cmn'''


def main():
	sol = Solution()

	print('Array 1 :{}'.format(array1))
	print('Array 2 :{}'.format(array2))

	set1 = set(array1)
	set2 = set(array2)

	if len(set1) < len(set2):
		result = sol.intersetcion(set1, set2)
	else:
		result = sol.intersetcion(set2, set1)

	#result = sol.intersetcion(set1, set2)

	print('intersetcion of two array is {}'.format(result))
	#print('Set 2 is {}'.format(result.set2))



if __name__ == '__main__':

	array1 = list(map(int, input().split()))
	array2 = list(map(int, input().split()))
	main()