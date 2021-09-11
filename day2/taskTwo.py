# Task 2: WAP to create a function in which the arguements are users and their marks and return three value.
# User with maximum mark, Average_marks, Users below failing marks. Below is sample of output:
# ("Raul": 99),("avg_marks","55"),["Hidan", "Goku", "Timon", "Sasuke", "Saitama"]

def marks(**students_list):
    max_mark = tuple()
    avg_mark = ("avg_marks", str(sum(students_list.values())/len(students_list)))
    failed = []
    for i in students_list:
        if max(students_list.values()) == students_list[i]:
            max_mark = (i, max(students_list.values()))
        if students_list[i] < 50:
            failed.append(i)
    return f"{max_mark},{avg_mark},{failed}"
    #max_mark = tuple(f"{students_list[max(students_list.values())]}", max(students_list.values()))
    #print(max_mark)


print(marks(Hamdi=99, Achref=40, Rahma=70, Nick=20, Amal=90))