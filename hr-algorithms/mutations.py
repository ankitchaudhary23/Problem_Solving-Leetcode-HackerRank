def mutate_string(string, position, character):
	# 1st method
	#l = list(string)
	#l[position] = character
	#string = ''.join(l)
	#return string

	# 2nd method
	string = string[:position] + character + string[position+1 :]
	return string

if __name__ == '__main__':
	s = input()
	i, c = input().split()
	s_new = mutate_string(s, int(i), c)
	print(s_new)