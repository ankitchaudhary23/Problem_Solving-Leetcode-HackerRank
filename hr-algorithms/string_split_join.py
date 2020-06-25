
def split_and_join(line):
	sline = line.split(' ')
	jline = '-'.join(sline)
	return jline


if __name__ == '__main__':
	line = input()
	results = split_and_join(line)
	print(results)