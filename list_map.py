def foo(student_marks,query_name,name):
    for i in student_marks:
       if(i==query_name):
            x =(sum(student_marks[i])/len(student_marks[i]))
            print('%.2f'%x)
           






if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
foo(student_marks,query_name,name)
