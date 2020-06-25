if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        #print(student_marks)
    query_name = input()

    #query_scores = student_marks[query_name]
    #print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
    
    if query_name in student_marks:
        marks  = student_marks.get(query_name, '')
        #print(marks)
        average = sum(marks)/len(marks)
        print('%.2f' %(average))