from collections import defaultdict
from math import sqrt,atan2


def integrate(f : callable, n : int) -> callable:
    try:
        if int(n) <= 0:
            raise AssertionError('n must be an int greater than 0')
    except:
        raise AssertionError('n must be an int greater than 0')
    
    def integral_f(a: float, b: float):
        dx = (b - a) / n
        area = 0
        for i in range(n):
            area += f(a + (i * dx)) * dx
        return area
    
    return integral_f
    

def sorted1 (ps : {int:(int,int)}) -> [(int,(int,int))]:
    return sorted(ps.items(), key = (lambda x: (x[1][0], x[1][1])))


def sorted2 (ps : {int:(int,int)}) -> [(int,int)]:
    return sorted(ps.values(), key = (lambda x: (-atan2(x[1], x[0]), sqrt(x[0]**2 + x[1]**2))))


def sorted3 (ps : {int:(int,int)}) -> [int]:
    return sorted(ps.keys(), key = (lambda x: (sqrt(ps[x][0]**2 + ps[x][1]**2), x)))


def points (ps : {int:(int,int)}) -> [(int,int)]:
    return [x[1] for x in sorted(ps.items())]


def first_quad (ps : {int:(int,int)}) -> {(int,int):float}:
    return {x[1] : sqrt(x[1][0]**2 + x[1][1]**2) for x in ps.items() if (x[1][0] >= 0 and x[1][1] >= 0)}


def movie_rank(db : {str:{(str,int)}}) -> [(str,float)]:
    return sorted([(x[0], sum([rating[1] for rating in x[1]])/len(x[1])) for x in db.items()], key = lambda results: (-results[1], results[0]))


def reviewer_dict(db : {str:{(str,int)}}) -> {str:{(str,int)}}:
    rev_dict = defaultdict(set)
    for rev in db.items():
        for name in rev[1]:
            rev_dict[name[0]].add((rev[0], name[1]))

    return dict(rev_dict)




if __name__ == '__main__':
    # This code is useful for debugging your functions, especially
    #   when they raise exceptions: better than using driver.driver().
    # Feel free to add more tests (including tests showing in the bsc.txt file)
    # Use the driver.driver() code only after you have removed anybugs
    #   uncovered by these test cases.
    
    print('Testing integrate')
    f = integrate( (lambda x : x), 100)
    print(f(0,1),f(0,2),f(-1,1))
    f = integrate( (lambda x : 3*x**2 - 2*x + 1), 1000)
    print(f(0,1),f(0,2),f(-1,1))
 
 
    print('\nTesting sorted1')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted1(ps1))
    print(sorted1(ps2))
 
    print('\nTesting sorted2')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted2(ps1))
    print(sorted2(ps2))
 
    print('\nTesting sorted3')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted3(ps1))
    print(sorted3(ps2))
    
    print('\nTesting points')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(points(ps1))
    print(points(ps2))
 
    print('\nTesting first_quad')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(first_quad(ps1))
    print(first_quad(ps2))
 
    print('\nTesting movie_rank')
    db1 = {'Psycho':  {('Bob',5),  ('Carry',5), ('Alan', 1), ('Diane', 1), }, 'Amadeus': {('Bob',3),  ('Carry',3), ('Diane',3)}, 'Up': {('Alan',2), ('Diane',5)} }
    db2 = {'Psycho':  {('Bob',5),  ('Carry',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
           'Amadeus': {('Bob',3),  ('Carry',3), ('Diane',3)},
           'Up': {('Alan',2), ('Diane',5)},
           'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
           'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
           'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
    print(movie_rank(db1))
    print(movie_rank(db2))
 
    print('\nTesting reviewer_dict')
    db1 = {'Psycho':  {('Bob',5),  ('Carry',5), ('Alan', 1), ('Diane', 1)}, 'Amadeus': {('Bob',3),  ('Carry',3), ('Diane',3)}, 'Up': {('Alan',2), ('Diane',5)} }
    db2 = {'Psycho':  {('Bob',5),  ('Carry',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
           'Amadeus': {('Bob',3),  ('Carry',3), ('Diane',3)},
           'Up': {('Alan',2), ('Diane',5)},
           'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
           'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
           'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
    print(reviewer_dict(db1))
    print(reviewer_dict(db2))
 
 
    print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()           

