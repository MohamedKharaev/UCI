from functools import reduce # For problem 6

def compare(s1 : str, s2 : str) -> str:
    if s1 == '' and s2 == '':
        return '='
    if s1 == '' and s2 != '':
        return '<'
    if s1 != '' and s2 == '':
        return '>' 
    if s1 != '' and s2 != '':
        if s1[0] != s2[0]:
            if s1[0] < s2[0]:
                return '<'
            else:
                return '>'
        else:
            return compare(s1[1:],s2[1:])
    
    
def is_palindrome(s : str) -> bool:
    if s == '':
        return True
    elif s[0].lower() != s[-1].lower():
        return False
    else:
        return is_palindrome(s[1:-1])



def separate(p : callable, l : [object]) -> ([object],[object]):
    if l == []:
        return [], []
    
    tl, fl = separate(p, l[1:])
    
    if p(l[0]) == True:
        tl += [l[0]]
    else:
        fl += [l[0]]
    
    return tl, fl


def sort(l : [object]) -> [object]:
    if l == []:
        return []
    else:
        y = l[0]
        l1, l2 = separate(lambda x: x <= y, l[1:])
        return sort(l1) + [y] + sort(l2)



def unnested(l : 'a nested list') -> [object]:
    if l == []:
        return []
    if type(l[0]) is list:
        return unnested(l[0]) + unnested(l[1:])
    else:
        return [l[0]] + unnested(l[1:])



def merge(x : [str], y : str) -> [str]:
    if x == []:
        return [y]
    elif len(x[0]) < len(y):
        return [y]
    elif len(x[0]) > len(y):
        return x
    else:
        return x + [y]
      
        
def all_longest(file : open) -> [str]:
    f = filter(lambda x: x[0] != '#', file)
    m = map(lambda x: x.strip(), f)
    r = reduce(lambda x, y: merge(x, y), m)
    return r
            


if __name__=="__main__":
    import predicate,random,driver
    from goody import irange
    
    print('Testing compare')
    print('',      compare('',''),          '')
    print('',      compare('','abc'),       'abc')
    print('abc',   compare('abc',''),       '')
    print('abc',   compare('abc','abc'),    'abc')
    print('bc',    compare('bc','abc'),     'abc')
    print('abc',   compare('abc','bc'),     'bc')
    print('aaaxc', compare('aaaxc','aaabc'), 'aaabc')
    print('aaabc', compare('aaabc','aaaxc'), 'aaaxc')
   
    print('\nTesting is_palindrome')
    print('DoGeeseSeeGod',          is_palindrome('DoGeeseSeeGod'))
    print('AbleWasIEreISawElba',    is_palindrome('AbleWasIEreISawElba'))
    print('AManAPlanACanalPanama',  is_palindrome('AManAPlanACanalPanama'))
    print('DoGeesesSeeGod',         is_palindrome('DoGeesesSeeGod'))
    print('AbleIWasEhenISawElba',   is_palindrome('AbleIWasEhenISawElba'))
    print('AManAPlaneACanalPanama', is_palindrome('AManAPlaneACanalPanama'))
    
    print('\nTesting separate')
    print(separate(predicate.is_positive,[]))
    print(separate(predicate.is_positive,[1, -3, -2, 4, 0, -1, 8]))
    print(separate(predicate.is_prime,[i for i in irange(2,20)]))
    print(separate(lambda x : len(x) <= 3,'to be or not to be that is the question'.split(' ')))
    print(separate(lambda x : x <= 'm','to be or not to be that is the question'.split(' ')))
     
    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = [i+1 for i in range(30)]
    random.shuffle(l)
    print(l)
    print(sort(l))
    
    print('\nTesting nested_count')
    print(unnested([1,2,4,1,8,1,3,2,1,1]))
    print(unnested([[1,2,4,1,8],[1,3,2],1,1]))
    print(unnested([[1,2,[4,[1],8],[1,3,2]],[1,1]]))

    print('\nTesting merge')
    print(merge([],'abc'))
    print(merge(['abc', 'lmn'],'wxyz'))
    print(merge(['abc', 'lmn'],'xyz'))
    print(merge(['abc', 'lmn'],'xy'))
    
    print('\nTesting all_longest')
    for l in all_longest(open('test1.txt')):
        print(l)
    print()

    driver.default_file_name = 'bsc.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
    
