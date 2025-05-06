#student_gradebook

from pprint import pprint

student_info = {}
grades = {}

def add_student(id_, name):
    if id_ in student_info:
        print(f'Error : Student {id_} already existing')
        return
    
    student_info[id_] = {"name" : name, "courses" : set()}
    print(f"Student ({id_} : '{student_info[id_]['name']}') added successfully")


def enroll(id_, course):
    if id_ not in student_info:
        print(f'Error : Student {id_} not found')
        return
    
    student_info[id_]['courses'].add(course)
    print(f"Student ({id_}:'{student_info[id_]['name']}') enrolled in '{course}'")

    
def add_grade(id_,course,grade):
    if id_ not in student_info:
        print(f'Error : Student {id_} not found')
        return
    
    if course not in student_info[id_]['courses']:
        print(f'Error: Student {id_} is not enrolled for {course}')
        return
    
    grades[(id_,course)]=grade
    print(f"Grade for student ({id_} : '{student_info[id_]['name']}') in '{course}' : {grade} ")


def average_grade(id_):
    if id_ not in student_info:
        print(f'Error : Student {id_} not found')
        return None
    
    student_grades = [grade for (s_id, course), grade in grades.items() if s_id == id_]

    if not student_grades:
        print(f"No grades recorded for student '{student_info[id_]['name']}")
        return 0
    
    average = sum(student_grades)/len(student_grades)
    print(f"Average grade for student '{student_info[id_]['name']}' : {average:2f}")
    return average


def students_in_course(course):
    enrolled_students = []
    for id_, info in student_info.items():
        if course in info['courses']:
            enrolled_students.append(info['name'])

    if enrolled_students:
            print(f"Students enrolled in '{course}' : {','.join(enrolled_students)}")
    else:
            print(f"No students enrolled in '{course}'.")
    return enrolled_students


def main():
    add_student(101,'Albert')
    add_student(102,'Bobert')
    add_student(102,'Bobert') #already existing
    
    print("------------------")

    enroll(101,'Maths')
    enroll(101,'Science')
    enroll(102,'Maths')
    enroll(102,'Social')
    enroll(103,'Social') #id not found

    print("------------------")

    add_grade(101,'Maths',89)
    add_grade(101,'Science',69)
    add_grade(102,'Maths',78)
    add_grade(102,'Social',90)
    add_grade(103,'Social',90) #id not found 
    add_grade(102,'English',90) #not enrolled for english

    print("\n-----Average Grades--------")
    average_grade(101)
    average_grade(102)
    average_grade(103)

    print("\n------Students in courses-------")
    students_in_course('Maths')
    students_in_course('Science')
    students_in_course('Social')
    students_in_course('Arts')

    print('\n-----Student information-----')
    pprint(student_info)

    print('\n-----Student grades-----')
    pprint(grades)

if __name__ == "__main__":
    main()
