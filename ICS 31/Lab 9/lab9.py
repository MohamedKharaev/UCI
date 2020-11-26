#Mohamed Kharaev 43121144 & Jarod Robinson 87289947. Lab Section 7

#Part C

from random import *
NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4 # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E


#Part C.1

def generate_answers() -> str:
    '''generates and returns a string of letters representing the correct answers to the test'''
    answers = ''
    for i in range(NUMBER_OF_QUESTIONS):
        answers += choice('ABCD')
    return answers

ANSWERS = generate_answers()

#Part C.2 - Part C.3

from collections import namedtuple
Student = namedtuple('Student', 'name answers correct_answers score')

def random_students(students_size: int) -> 'List of Students':
    '''generates and return a list of Student namedtuples.'''
    students = []
    for i in range(students_size):
        student_answers = generate_answers()
        correct_answers = []
        score_count = 0
        for j in range(len(student_answers)):
            if student_answers[j] == ANSWERS[j]:
                correct_answers.append(1)
                score_count += 1
            else:
                correct_answers.append(0)
        students.append(Student(i, student_answers, correct_answers, score_count))        
    return students

def get_student_score(student: 'Student') -> int:
    '''returns the students score'''
    return student.score

RANDOM_STUDENTS = random_students(NUMBER_OF_STUDENTS)

def print_top_students(students: 'List of Students'):
    '''print the top 10 students' names along with the average test score'''
    students.sort(key = get_student_score, reverse = True)
    scores = []
    for student in range(10):
        print(students[student].name)
        scores.append(students[student].score)
    print('AVERAGE SCORE:', sum(scores)/len(scores))

print(print_top_students(RANDOM_STUDENTS))

#Part C.4

def generate_weighted_student_answer(correct_answer: str) -> str:
    '''takes a string (one character, the correct answer) and returns a string (one character, the student answer chosen randomly from the enhanced group of alternatives'''
    altered_answers = 'ABCD' + correct_answer + correct_answer 
    return choice(altered_answers)

def random_student2(students_size: int) -> 'List of Students':
    '''generates each student's answer to each question by calling generate_weighted_student_answer.'''
    students = []
    for i in range(students_size):
        student_answers = []
        for j in range(NUMBER_OF_QUESTIONS):
            student_answers.append(generate_weighted_student_answer(ANSWERS[j]))
        correct_answers = []
        score_count = 0
        for j in range(len(student_answers)):
            if student_answers[j] == ANSWERS[j]:
                correct_answers.append(1)
                score_count += 1
            else:
                correct_answers.append(0)
        students.append(Student(i, student_answers, correct_answers, score_count))        
    return students

RANDOM_STUDENTS2 = random_student2(NUMBER_OF_STUDENTS)

print(print_top_students(RANDOM_STUDENTS2))

#Part C.5

def question_weights(students: 'List of Students') -> 'List of Numbers':
    '''takes a list of Student records and returns a list of numbers, one number for each question on the test, where each number is the number of students who answered that question incorrectly.'''
    weights = []
    for i in range(NUMBER_OF_QUESTIONS):
        question_weight = 0
        for j in range(len(students)):
            if students[j].correct_answers[i] == 0:
                question_weight += 1
        weights.append(question_weight)
    return weights

def Student_weighted_score(students: 'List of Students', weights: 'List of ints') -> 'List of Students':
    '''takes a Student record and the list of question weights and returns that Student record with its total field changed to reflect that student's score based on his or her correct answers and the corresponding question weights'''
    weighted_students = []
    for i in range(len(students)):
        weighted_score_count = 0
        for j in range(NUMBER_OF_QUESTIONS):
            weighted_score_count += (students[i].correct_answers[j] * weights[j])
        weighted_students.append(students[i]._replace(score = weighted_score_count))
    return weighted_students
            
WEIGHTED_RANDOM_STUDENTS2 = Student_weighted_score(RANDOM_STUDENTS2, question_weights(RANDOM_STUDENTS2))

print(print_top_students(WEIGHTED_RANDOM_STUDENTS2))

#Part D

#Part D.1

def calculate_GPA(grades: 'List of str') -> float:
    '''takes as input a list of strings representing letter grades and returns the grade point average (out of 4 with A=4, B=3, C=2, D=1, and F=0) computed from the list'''
    grade_converter = str.maketrans('ABCDF', '43210')
    for i in range(len(grades)):
        grades[i] = int(grades[i].translate(grade_converter))
    return sum(grades)/len(grades)

#Part D.1B

def calculate_GPA2(grades: 'List of str') -> float:
    '''also computes a GPA from a list of grades'''
    GPA = 0
    grade_converter_dict = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3,
                            'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0,
                            'C-': 1.7, 'D+': 1.3, 'D': 1.0}
    for grade in grades:
        GPA += grade_converter_dict[grade]
    return GPA/len(grades)

#Part D.2

def flatten_2D_list(TwoD_list: 'List of Lists') -> list:
    '''takes as input a two-dimensional table and return the input as a single list ocntaining, in orddder, all the elemnts on the original nested list.'''
    answer = []
    for item in TwoD_list:
        answer += item
    return answer

#Part D.3A

def skip_every_third_item(lst: 'List'):
    '''input a list and prints out each item on the list, except that it skips every third item '''
    for i in range(len(lst)):
        if (i+1)%3 == 0:
            pass
        else:
            print(lst[i])

#Part D.3B
        
def skip_every_nth_item(lst: 'List', n: int):
    '''takes as input a list and an int (call it n) and prints out each item on the list, except that it skips every nth item'''
    for i in range(len(lst)):
        if (i+1)%n == 0:
            pass
        else:
            print(lst[i])


#Part D.4

def tally_days_worked(worked: 'List of str') -> dict:
    '''takes as input the list described above and returns a dictionary where every key is a name of an employee and the value is the number of days that employee worked in the given week, according to the list'''
    worked_dict = {}
    for worker in worked:
        if worker in worked_dict:
            worked_dict[worker] += 1
        else:
            worked_dict[worker] = 1
    return worked_dict

work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']

#Part D.4B

hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50,
                'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}

def pay_employees(workers: dict, wages: dict):
    '''takes as input the two dictionaries described above and prints out how much each employee will be paid'''
    for worker in workers:
        print(worker, ' will be paid $', workers[worker] * wages[worker], ' for ',
              workers[worker], ' hours of work at $', wages[worker], ' per hour.', sep='')

#Part D.5

def reverse_dict(dict1: dict) -> dict:
    '''takes as a parameter a dictionary and returns a new dictionary with the keys and values of the original dictionary reversed:'''
    answer = {}
    for item in dict1:
        answer.update({dict1[item]: item})
    return answer


