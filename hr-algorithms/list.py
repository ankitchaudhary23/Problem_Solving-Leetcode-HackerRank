if __name__ == '__main__':
    n = int(input())

    arr = []

   
    for _ in range(n): 
        inputs = input().split() 
        if len(inputs)==1: 
            command =inputs[0] 
        if len(inputs)==2: 
            command = inputs[0] 
            e = int(inputs[1]) 
        if len(inputs)==3: 
            command = inputs[0] 
            i = int(inputs[1]) 
            e = int(inputs[2])
        
        if command=="insert":
            arr.insert(i,e)
        elif command=="remove":
            arr.remove(e)
        elif command=="append":
            arr.append(e)
        elif command=="sort":
            arr.sort()
        elif command=="pop":
            arr.pop()
        elif command=="reverse":
            arr.reverse()
        elif command=="print":
            print(arr)