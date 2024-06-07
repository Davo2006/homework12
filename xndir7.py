#xndir7 (Write a function that takes a dictionary with information about students. Return info about the youngest student)
def the_youngest_student(m):
    x = 0
    for i in m:
        if m[i]['age'] > x:
            x = m[i]['age']
    return x
students_info = {'student1': {'name': 'John Doe','age': 20,'subjects': ['Math', 'Physics', 'English'],'scores': [7, 9, 9, 6],},'student2': {'name': 'Jane Smith','age': 19,'subjects': ['Chemistry', 'Biology', 'History'],'scores': [5, 6, 8, 10],},'student3': {'name': 'Bob Johnson','age': 21,'subjects': ['Computer Science', 'Statistics', 'Psychology'],'scores': [8, 8, 9, 9, 9],},}
y = the_youngest_student(students_info)
print(y)
#xndir8 ()
def highest_average_score(m:dict):
    y = 0
    for i in m:
        x = 0
        for t in m[i]['scores']:
            x += t
            if x > y:
                y = x    
    return y
u = students_info = {'student1': {'name': 'John Doe','age': 20,'subjects': ['Math', 'Physics', 'English'],'scores': [7, 9, 9, 6],},'student2': {'name': 'Jane Smith','age': 19,'subjects': ['Chemistry', 'Biology', 'History'],'scores': [5, 6, 8, 10],},'student3': {'name': 'Bob Johnson','age': 21,'subjects': ['Computer Science', 'Statistics', 'Psychology'],'scores': [8, 8, 9, 9, 9],},}
d = highest_average_score(u)
print(d)
