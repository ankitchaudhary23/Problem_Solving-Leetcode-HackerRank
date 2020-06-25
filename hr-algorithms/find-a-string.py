def count_susbtring(string, sub_string):
	count = 0

	for i in range(0, (len(string) - len(sub_string))+1):
		
		try:
			
			if string[i : i+len(sub_string)] == sub_string:
				count += 1
		
		except IndexError:
			
			break

	return count

	'''
	c = 0
	for i in range(0, len(string)):
		if string[i] == subs_string[0]:
			flag = 1
			for j in range(0,len(subs_string)):
				if string[i+j] != subs_string[j]:
					flag = 0
					break
			if flag == 1:
				c += 1
	return c	
	'''

if __name__ == '__main__':
	string = input().strip()
	subs_string = input().strip()

	count = count_susbtring(string, sub_string)
	print(count)
