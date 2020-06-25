marksheet=[]
scorelist=[]
if __name__ == '__main__':
    for _ in range(int(input())):
            name = input()
            score = float(input())

            marksheet.append([name, score])
            #marksheet+=[[name,score]]
            scorelist+=[score]
           #print(scorelist)
            print('Student List {}' .format(marksheet))

    second_score = sorted(list(set(scorelist)))[1]
    #print(2ndhigh_score)
    for a, c in sorted(marksheet):
    	if c == second_score:
    		print(a)



#    b=sorted(list(set(scorelist)))[1] 

 #   for a,c in sorted(marksheet):
  #          if c==b:
   #	            print(a)