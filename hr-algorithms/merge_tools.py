def merge_the_tools(string, k):
	#sublen = int(len(string) / k)
	

	for i in range(0, len(string), k):
		sub = string[i:i+k]
		temp = []
		for j in sub:
			if j in sub:
				temp.append(j)
		print(''.join(temp))

	'''temp = []
				len_temp = 0
				for i in string:
					len_temp += 1
					if i not in temp:
						temp.append(i)
					if len_temp == k:
						print (''.join(temp))
						temp = []
						len_temp = 0'''

	'''for i in range(0, len(string), 3):
					for j in range(3):
						t[j] = string[i:i+3]
					print(t)
					'''



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)