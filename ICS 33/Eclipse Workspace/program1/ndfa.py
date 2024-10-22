import goody
from collections import defaultdict

def read_ndfa(file : open) -> {str:{str:{str}}}:
    return_dict = {}
    for line in file:
        s_line = line.strip().split(';')
        return_dict[s_line[0]] = defaultdict(set)
        for key in range(len(s_line))[1::2]:
            return_dict[s_line[0]][s_line[key]].add(s_line[key + 1])
        return_dict[s_line[0]] = dict(return_dict[s_line[0]])
    return return_dict



def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    return ''.join([('  ' + t + ' transitions: ' + str([(x, sorted(ndfa[t][x])) for x in sorted(ndfa[t])]) + '\n') for t in sorted(ndfa)])

def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    return_list = [state]
    for input in inputs:
        if input not in ndfa[state]:
            return_list.append((input, None))
            break
        print((input, ndfa[state][input]))
        return_list.append((input, ndfa[state][input]))
        print(return_list)
        state = ndfa[state][input]
        print(state)
    return return_list


def interpret(result : [None]) -> str:
   pass





if __name__ == '__main__':
    # Write script here
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
