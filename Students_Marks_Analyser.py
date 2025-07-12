import numpy as np
Students = input("Enter student names separated by space: ").split()
Marksof_students = []
total_stu = len(Students)
subjects = int(input("Enter a number of subjects: or columns"))
for i in range(total_stu):
    row = []
    print(f"Enter a marks for student:{i+1}")
    for j in range(subjects):
        values = int(input(f"subject {j+1}:"))
        row.append(values)
    Marksof_students.append(row)
Marksof_students = np.array(Marksof_students)
print(f"\n Row reprsents the marks of every student")
print(Marksof_students)
total_marks = np.sum(Marksof_students,axis=1)
topper_index = np.argmax(total_marks)
for i in range(len(Marksof_students)):
    print(f"Marks of {Students[i]}:{total_marks[i]}") 
print(f"Topper is {Students[topper_index]} with marks {total_marks[topper_index]}")

