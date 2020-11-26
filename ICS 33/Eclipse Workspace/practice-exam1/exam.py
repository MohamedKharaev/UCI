from collections import defaultdict

# Helper global variable for use in top and class_averages function
# Do not mutate it: example use, UCI['C+'] returns 2.3
UCI = {'A+': 4.0, 'A': 4.0,'A-': 3.7,
       'B+': 3.3, 'B': 3.0,'B-': 2.7,
       'C+': 2.3, 'C': 2.0,'C-': 1.7,
       'D+': 1.3, 'D': 1.0,'D-': 0.7,
       'F': 0.0}


def top(student_info : {(str,str)}) -> {str}:
    if len(student_info) == 0:
        return set()
    return_set = set()
    highest_gpa = max([UCI[student[1]] for student in student_info])
    for student in student_info:
        if UCI[student[1]] == highest_gpa:
            return_set.add(student[0])
    return return_set


def read_db(file : open) -> {str:{(str,str)}} :
    return_dict = defaultdict(set)
    for line in file:
        sections = line.strip().split(':')
        course = sections.pop(0)
        for person in sections:
            name, grade = person.split(',')
            return_dict[course].add((name, grade))
    return return_dict
        



def class_averages(db : {str:{(str,str)}}) -> {str:float}:
    return_dict = {}
    for course in db:
        return_dict[course] = sum([UCI[student[1]] for student in db[course]]) / len(db[course])
    return return_dict
 
        
def class_roster(db : {str:{(str,str)}}) -> [(str,[str])]:
    return_list = []
    for course in db:
        return_list.append((course, sorted([student[0] for student in db[course]])))
    return sorted(return_list, key = (lambda x: (len(x[1]), x[0])))


        
def student_view(db : {str:{(str,str)}}) -> {str:{(str,str)}}:
    return_dict = defaultdict(set)
    for course in db:
        for student in db[course]:
            return_dict[student[0]].add((course, student[1]))
    return return_dict


# 1 point extra credit; complete all other problems first! 
def student_scores(db : {str:{(str,str)}}) -> {str:{str:float}}:
    return_dict = defaultdict(dict)
    for course in db:
        for student in db[course]:
            return_dict[student[0]][course] = UCI[student[1]]
    return return_dict





if __name__ == '__main__':
    import prompt
     
    # checks whether answer is correct, printing appropriate information
    # Note that dict/defaultdict will compare == if they have the same keys and
    #   associated values, regardless of the fact that they print differently
    def check (answer, correct):
        if (answer   == correct):
            print ('    Correct')
        else:
            print ('    INCORRECT')
            print ('      was       =',answer)
            print ('      should be =',correct)
        print()
 
 
 
    if prompt.for_bool('Test top_students?', True):        
        students = {('Alice','C'),('Bob','B-'),('Carol','B-'),('David','D'),('Evelyn','C+')}
        print('  argument =',students)
        answer   = top(students)
        print('  answer   =', answer)
        check(answer, {'Bob','Carol'})
         
        students = {('Alice','B+'),('Bob','B'),('Carol','C'),('David','B-')}
        print('  argument =',students)
        answer   = top(students)
        print('  answer   =', answer)
        check(answer, {'Alice'})
         
        students = {('Alice','C'),('Bob','D'),('Carol','C'),('David','F'),('Evelyn','C')}
        print('  argument =',students)
        answer   = top(students)
        print('  answer   =', answer)
        check(answer, {'Alice','Carol','Evelyn'})
         
        students = set()            # No students
        print('  argument =',students)
        answer   = top(students)
        print('  answer   =', answer)
        check(answer, set())
         
 
 
    if prompt.for_bool('Test read_db?', True):        
        print('  argument = fall15.txt')
        answer   = read_db(open('fall15.txt'))
        print('  answer   =', answer)
        check(answer, {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}})
 
        print('  argument = spring15.txt')
        answer   = read_db(open('spring15.txt'))
        print('  answer   =', answer)
        check(answer, {'ICS-6D': {('Bob', 'B'), ('Alice', 'A')},
                       'Math-3A': {('Bob', 'B'), ('Alice', 'A'), ('Evelyn', 'A-'), ('Frank', 'C+')},
                       'ICS-31': {('Frank', 'C-'), ('Bob', 'B+'), ('Carol', 'C+'), ('David', 'B-')},
                       'English-28A': {('David', 'A'), ('Evelyn', 'A'), ('Carol', 'A')}})
 
 
 
    if prompt.for_bool('Test class_averages?', True):        
        db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
        print('  argument =',db)
        answer   = class_averages(db)
        print('  answer   =', answer)
        check(answer, {'Math-3A': 3.5, 'ICS-31': 3.0})
 
        db = {'ICS-6D': {('Bob', 'B'), ('Alice', 'A')},
              'Math-3A': {('Bob', 'B'), ('Alice', 'A'), ('Evelyn', 'A'), ('Frank', 'C')},
              'ICS-31': {('Frank', 'C'), ('Bob', 'B'), ('Carol', 'C'), ('David', 'B')},
              'English-28A': {('David', 'A'), ('Evelyn', 'A'), ('Carol', 'A')}}
        print('  argument =',db)
        answer   = class_averages(db)
        print('  answer   =', answer)
        check(answer, {'ICS-6D': 3.5, 'ICS-31': 2.5, 'Math-3A': 3.25, 'English-28A': 4.0})
 
 
 
    if prompt.for_bool('Test class_roster?', True):        
        db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
        print('  argument =',db)
        answer   = class_roster(db)
        print('  answer   =', answer)
        check(answer, [('Math-3A', ['Alice', 'Bob']), ('ICS-31', ['Bob', 'Carol', 'David'])] )
 
        db = {'ICS-6D': {('Bob', 'B'), ('Alice', 'A')},
              'Math-3A': {('Bob', 'B'), ('Alice', 'A'), ('Evelyn', 'A-'), ('Frank', 'C+')},
              'ICS-31': {('Frank', 'C-'), ('Bob', 'B+'), ('Carol', 'C+'), ('David', 'B-')},
              'English-28A': {('David', 'A'), ('Evelyn', 'A'), ('Carol', 'A')}}
        print('  argument =',db)
        answer   = class_roster(db)
        print('  answer   =', answer)
        check(answer, [('ICS-6D', ['Alice', 'Bob']),
                       ('English-28A', ['Carol', 'David', 'Evelyn']),
                       ('ICS-31', ['Bob', 'Carol', 'David', 'Frank']),
                       ('Math-3A', ['Alice', 'Bob', 'Evelyn', 'Frank'])] )
 
 
 
    if prompt.for_bool('Test student_view?', True):        
        db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
        print('  argument =',db)
        answer   = student_view(db)
        print('  answer   =', answer)
        check(answer, {'Carol': {('ICS-31', 'B')}, 'Alice': {('Math-3A', 'A')}, 'Bob': {('Math-3A', 'B'), ('ICS-31', 'A')}, 'David': {('ICS-31', 'C')}} )
 
        db = {'ICS-6D': {('Bob', 'B'), ('Alice', 'A')},
                       'Math-3A': {('Bob', 'B'), ('Alice', 'A'), ('Evelyn', 'A-'), ('Frank', 'C+')},
                       'ICS-31': {('Frank', 'C-'), ('Bob', 'B+'), ('Carol', 'C+'), ('David', 'B-')},
                       'English-28A': {('David', 'A'), ('Evelyn', 'A'), ('Carol', 'A')}}
        print('  argument =',db)
        answer   = student_view(db)
        print('  answer   =', answer)
        check(answer, {'Frank': {('ICS-31', 'C-'), ('Math-3A', 'C+')},
                       'David': {('ICS-31', 'B-'), ('English-28A', 'A')},
                       'Evelyn': {('Math-3A', 'A-'), ('English-28A', 'A')},
                       'Carol': {('ICS-31', 'C+'), ('English-28A', 'A')},
                       'Alice': {('Math-3A', 'A'), ('ICS-6D', 'A')},
                       'Bob': {('Math-3A', 'B'), ('ICS-31', 'B+'), ('ICS-6D', 'B')}} )
    
    
    if prompt.for_bool('Test student_scores: worth only 1 point extra credit?', True):        
        db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
        print('  argument =',db)
        answer   = student_scores(db)
        print('  answer   =', answer)
        check(answer, {'Carol': {'ICS-31': 3.0}, 'Alice': {'Math-3A': 4.0}, 'Bob': {'Math-3A': 3.0, 'ICS-31': 4.0}, 'David': {'ICS-31': 2.0}} )
 
        db = {'ICS-6D': {('Bob', 'B'), ('Alice', 'A')},
                       'Math-3A': {('Bob', 'B'), ('Alice', 'A'), ('Evelyn', 'A-'), ('Frank', 'C+')},
                       'ICS-31': {('Frank', 'C-'), ('Bob', 'B+'), ('Carol', 'C+'), ('David', 'B-')},
                       'English-28A': {('David', 'A'), ('Evelyn', 'A'), ('Carol', 'A')}}
        print('  argument =',db)
        answer   = student_scores(db)
        print('  answer   =', answer)
        check(answer, {'Frank': {'ICS-31': 1.7, 'Math-3A': 2.3},
                       'David': {'ICS-31': 2.7, 'English-28A': 4.0},
                       'Evelyn': {'Math-3A': 3.7, 'English-28A': 4.0},
                       'Carol': {'ICS-31': 2.3, 'English-28A': 4.0},
                       'Alice': {'Math-3A': 4.0, 'ICS-6D': 4.0},
                       'Bob': {'Math-3A': 3.0, 'ICS-31': 3.3, 'ICS-6D': 3.0}} )
