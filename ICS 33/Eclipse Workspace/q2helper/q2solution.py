import re
from goody import irange

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. The patterns must be all on the first line

def pages (page_spec : str, unique) -> [int]: #result in ascending order
    result = []
    pages = page_spec.split(',')
    for page in pages:
        m = re.match('^([1-9][0-9]*)(?:(:|-)([1-9][0-9]*)(?:/([1-9][0-9]*))?)?$', page)
        assert m != None
        fpage, extra, lpage, skip = m.groups()
        if extra == None:
            result.append(int(fpage))
        else:
            if extra == '-':
                assert int(fpage) <= int(lpage)
                if skip == None:
                    result.extend(irange(int(fpage), int(lpage)))
                else:
                    result.extend(irange(int(fpage), int(lpage), int(skip)))
            else:
                if skip == None:
                    result.extend(range(int(fpage), (int(fpage) + int(lpage))))
                else:
                    result.extend(range(int(fpage), (int(fpage) + int(lpage)), int(skip)))
    if unique:
        return sorted(set(result))
    else:
        return sorted(result)



def expand_re(pat_dict:{str:str}):
    for key in pat_dict:
        m = re.compile('#' + key + '#')
        for key2 in pat_dict:
            pat_dict[key2] = re.sub(m, ('(?:' + pat_dict[key] + ')'), pat_dict[key2])



if __name__ == '__main__':
    
    p1a = open('repattern1a.txt').read().rstrip() # Read pattern on first line
    print('Testing the pattern p1a: ',p1a)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1a,text)
        print(' ','Matched' if m != None else "Not matched")
        
    p1b = open('repattern1b.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p1b: ',p1b)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1b,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
        
    p2 = open('repattern2a.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2: ',p2)
    for text in open('bm2a.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
    print('\nTesting pages function')
    for text in open('bm2b.txt'):
        text = text.rstrip().split(';')
        text,unique = text[0], text[1]=='True'
        try:
            p = pages(text,unique)
            print('  ','pages('+text+','+str(unique)+') = ',p)
        except:
            print('  ','pages('+text+','+str(unique)+') = raised exception')
        
    
    print('\nTesting expand_re')
    pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary
    # {'digit': '\\d', 'integer': '[=-]?(?:\\d)(?:\\d)*'}
    
    pd = dict(integer       = r'[+-]?\d+',
              integer_range = r'#integer#(..#integer#)?',
              integer_list  = r'#integer_range#(?,#integer_range#)*',
              integer_set   = r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer':       '[+-]?\\d+',
    #  'integer_range': '(?:[+-]?\\d+)(..(?:[+-]?\\d+))?',
    #  'integer_list':  '(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?)(?,(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?))*',
    #  'integer_set':    '{(?:(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?)(?,(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'a': 'correct',
    #  'b': '(?:correct)',
    #  'c': '(?:(?:correct))',
    #  'd': '(?:(?:(?:correct)))',
    #  'e': '(?:(?:(?:(?:correct))))',
    #  'f': '(?:(?:(?:(?:(?:correct)))))',
    #  'g': '(?:(?:(?:(?:(?:(?:correct))))))'
    # }
    
    print()
    print()
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
