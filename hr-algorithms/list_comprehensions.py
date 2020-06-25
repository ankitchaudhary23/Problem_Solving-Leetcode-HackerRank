if __name__ == '__main__':
	#x = int(input())
	#y = int(input())
	#z = int(input())
	#n = int(input())
	x, y, z, n = (int(input()) for _ in range(4))
#	for i in range(x+1):
#		for j in range(y+1):
#			for k in range(z+1):
#					print([i,j,k])

	print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])