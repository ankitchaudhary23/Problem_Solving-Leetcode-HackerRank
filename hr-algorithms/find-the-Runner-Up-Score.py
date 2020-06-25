if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    maxv = max(arr)

    while max(arr) == maxv:
    	arr.remove(max(arr))
    print(max(arr))

    
    #if len(arrl) > 1:
    	#print('Max value is {}' .format(arrl[-2]))