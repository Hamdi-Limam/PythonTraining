# simple solution
# n = int(input())

students = []
grades = []
name = input()
score = float(input())
min = score
students.append([name, score])
grades.append(min)
for _ in range(n-1):
        name = input()
        score = float(input())
        if score < min:
            min = score
        grades.append(score)
        students.append([name, score])

grades.sort(reverse=True)
second_lowest_grade = grades[grades.index(min)-1]
students.sort()
for i in students:
    if i[1] == second_lowest_grade:
        print(i[0])

# Shorter solution
# students = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name, score])
# students.sort(reverse=True, key=lambda x: x[1])

# print(students)
# print(students.index(students[len(students)-1][1])) -> index
# print(students[students.index(students[len(students)-1][1])][1])