def flow(student_marks):
    for i in range(len(student_marks)):
    	print(student_marks[i])


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
flow(student_marks)
