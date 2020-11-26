
#Mohamed Kharaev 43121144 & Elizabeth Chen 75557458. Lab Section 7
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')

print("<-------Part C1------->")

def read_menu_with_count(str1: str) -> 'List of Dish':
    '''takes as an argument a string naming a file in this format, reads the file, and returns a list of Dish structures created from the data'''
    read_file = open(str1, 'r')
    count = read_file.readline()
    Dishes = read_file.readlines()
    read_file.close()
    answer = []

    for i in Dishes:
        answer.append(i)

    for i in range(len(answer)):
        answer[i] = answer[i].split("\t")
        answer[i][1] = answer[i][1].replace("$", "")
        answer[i][2] = answer[i][2].replace("\n", "")
        answer[i] = Dish(answer[i][0], answer[i][1], answer[i][2])

    return answer

print(read_menu_with_count('menu1.txt'))

print("<-------Part C2------->")

def read_menu(str1: str) -> 'List of Dish':
    '''takes as an argument a string naming a file in this format, reads the file, and returns a list of Dish structures created from the data.'''
    read_file = open(str1, 'r')
    Dishes = read_file.readlines()
    read_file.close()
    answer = []

    for i in Dishes:
        answer.append(i)

    for i in range(len(answer)):
        answer[i] = answer[i].split("\t")
        answer[i][1] = answer[i][1].replace("$", "")
        answer[i][2] = answer[i][2].replace("\n", "")
        answer[i] = Dish(answer[i][0], answer[i][1], answer[i][2])

    return answer

print(read_menu('menu3.txt'))

print("<-------Part C3------->")

def write_menu(Dishes: 'List of Dishes', file_name: str):
    ''' takes as its argument a list of Dish namedtuples and a string that names a file.'''
    output = open(file_name, 'w')

    output.write(str(len(Dishes)))
    output.write("\n")

    for dish in Dishes:
        output_format = "{}\t${}\t{}\n"
        output.write(output_format.format(dish.name, dish.price, dish.calories))
    
    output.close()


print("<-------Part D1------->")

Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)
  
Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])
  
StudentBody = [sW, sX, sY, sZ]

def Students_at_level(students: 'List of Students', level: str) -> 'List of Students':
    '''takes a list of Students and a string (representing a class level, e.g., 'FR' or 'SO') and returns a list of students whose class level matches the parameter'''
    answer = []
    for student in students:
        if student.level == level:
            answer.append(student)
    return answer

print(Students_at_level(StudentBody, 'FR'))
print("<-------Part D2------->")

def Students_in_majors(students: 'List of Students', major: str) -> 'List of Students':
    '''takes a list of Students and a list of strings (where each string represents a major) and returns a list of Students that have majors on the specified list.'''
    answer = []
    for student in students:
        if student.major == major:
            answer.append(student)
    return answer

print(Students_in_majors(StudentBody, 'CS'))

print("<-------Part D3------->")

def Students_in_class(students: 'List of Students', dept: str, num: str) -> 'List of Students':
    '''takes a list of Students, and two strings—a department name and a course number (e.g., 'ICS' and '31')—and returns a list of those Students who are enrolled in the specified class.'''
    answer = []
    for student in students:
            for classes in student.studylist:
                if classes.dept == dept:
                    if classes.num == num:
                        answer.append(student)
    return answer

print(Students_in_class(StudentBody, 'ICS', '31'))

print("<-------Part D4------->")

def Student_names(Students: 'List of Students') -> 'List of Students':
    '''takes a list of Students and returns a list of just the names of those students'''
    answer = []
    for student in Students:
        answer.append(student.name)
    return answer

print(Student_names(StudentBody))
print("<-------Part D5------->")

ICS_majors = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']

def Students_in_ICS(students: 'List of Students') -> 'List of Students':
    '''returns A list of Students who are majors from the School of ICS (those majors are ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS'])'''
    answer = []
    for student in students:
        if student.major in ICS_majors:
            answer.append(student)
    return answer
assert(Students_in_ICS(StudentBody) == [sX])

def Student_names_in_ICS(students: 'List of Students') -> 'List of Students':
    '''returns A list of the names of Students who are majors from the School of ICS'''
    answer = []
    for student in students:
        if student.major in ICS_majors:
            answer.append(student.name)
    return answer
assert(Student_names_in_ICS(StudentBody) == ['Anteater, Andrea'])

def Number_Students_in_ICS(students: 'List of Students') -> int:
    '''returns the number of Students who are majors from the School of ICS'''
    return len(Students_in_ICS(students))
assert(Number_Students_in_ICS(StudentBody) == 1)

def Seniors_in_ICS(students: 'List of Students') -> 'List of Students':
    '''returns A list of the names of seniors who are majors in the School of ICS'''
    answer = []
    for student in students:
        if student.level == "SR":
            if student.major in ICS_majors:
                answer.append(student)
    return answer
assert(Seniors_in_ICS(StudentBody) == [])

def Number_Seniors_in_ICS(students: 'List of Students') -> int:
    '''returns The number of seniors who are majors from the School of ICS'''
    return len(Seniors_in_ICS(students))
assert(Number_Seniors_in_ICS(StudentBody) == 0)

def Percentage_of_Senior_ICS_Majors(students: 'List of Students') -> float:
    '''returns The percentage of majors from the School of ICS who are seniors'''
    return 100*Number_Seniors_in_ICS(students)/Number_Students_in_ICS(students)
assert(Percentage_of_Senior_ICS_Majors(StudentBody) == 0.0)

def Number_of_ICS_FR_in_ICS31(students: 'List of Students') -> int:
    '''returns The number of freshmen who are majors from the School of ICS and enrolled in ICS 31'''
    temp_list = []
    answer = []
    for student in students:
        if student.level == 'FR':
            if student.major in ICS_majors:
                temp_list.append(student)
    answer = Students_in_class(temp_list, 'ICS', '31')
    return len(answer)
assert(Number_of_ICS_FR_in_ICS31(StudentBody) == 0)

def Average_Units_of_FR_in_ICS31(students: 'List of Students') -> float:
    '''returns The average number of units that freshmen in ICS 31 are enrolled in'''
    temp_list = []
    answer = 0
    for student in students:
        if student.level == 'FR':
            if student.major in ICS_majors:
                temp_list.append(student)

    if len(temp_list) == 0:
        return 0
    
    for student in temp_list:
        answer += student.units
    return answer/len(temp_list)
assert(Average_Units_of_FR_in_ICS31(StudentBody) == 0.0)
