import goody


def read_fa(file : open) -> {str:{str:str}}:
    return_dict = {}
    for line in file:
        s_line = line.strip().split(';')
        return_dict[s_line[0]] = dict(zip(s_line[1::2], s_line[2::2]))
    return return_dict

def fa_as_str(fa : {str:{str:str}}) -> str:
    return ''.join([('  ' + t + ' transitions: ' + str([(x, fa[t][x]) for x in sorted(fa[t])]) + '\n') for t in sorted(fa)]) 
    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    return_list = [state]
    for input in inputs:
        if input not in fa[state]:
            return_list.append((input, None))
            break
        return_list.append((input, fa[state][input]))
        state = fa[state][input]
    return return_list

def interpret(fa_result : [None]) -> str:
    return_str = ''
    return_str += 'Start state = {}\n'.format(fa_result[0])
    for trans in fa_result[1:]:
        if trans[1] == None:
            return_str += '  Input = {}; illegal input: simulation terminated\n'.format(trans[0])
            break
        return_str += '  Input = {}; new state = {}\n'.format(trans[0], trans[1])
    return_str += 'Stop state = {}\n'.format(fa_result[-1][-1])
    return return_str

if __name__ == '__main__':
    # Write script here
    fa = read_fa(goody.safe_open('Enter a file representing a finite automaton', 'r', 'file not found or there was an error'))
    print('\nThe Description of the Finite Automaton', fa_as_str(fa), sep = '\n')
    for line in goody.safe_open('Enter a file representing a start-state and inputs', 'r', 'file not found or there was an error'):
        sims = line.strip().split(';')
        state = sims.pop(0)
        print('Starting a new FA simulation', interpret(process(fa, state, sims)), sep = '\n')
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
