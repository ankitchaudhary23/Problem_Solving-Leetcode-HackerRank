class Solution:
	def plusOne(self, digits):
		num = 0
		for i in range(len(digits)):
			num += digits[i] * pow(10, (len(digits)-1-i))
		num+=1
		return [int(i) for i in str(num)]

'''		
		return [int(i) for i in str(int(''.join(map(str,digits)))+1)]
'''
'''	Addition with Carry	
		n = len(digits)

		for i in range(n):
			indx = n-1-i
			if digits[indx] == 9:
				digits[indx] = 0
			else:
				digits[indx] += 1
				return digits
		return [1] + digits
'''

def main():
	sol = Solution()
	result = sol.plusOne(array)
	print('Plus One Digit Representation: {}'.format(result))


if __name__ == '__main__':
	arrCount = int(input())
	array = list(map(int, input().split()))
	main()