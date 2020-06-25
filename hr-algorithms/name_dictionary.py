import operator

def person_lister(f):
	def inner(people):

		print("before Execution") 

		# getting the returned value 
		returned_value = map(f, sorted(people, key = lambda x: int(x[2])))
		print("after Execution") 

		# returning the value to the original frame - 
		return returned_value
		
	return inner

# adding decorator to the function 
@person_lister
def name_format(person):
	print("Inside the function") 
	return ('Mr. ' if person[3] == 'M' else 'Ms. ') + person[0] + ' ' + person[1]


if __name__ == '__main__':
	
	people = [input().split() for _ in range(int(input()))]
	# getting the value through return of the function 
	print(*name_format(people), sep='\n')
	


