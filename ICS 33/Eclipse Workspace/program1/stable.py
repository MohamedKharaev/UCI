import prompt
import goody

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    return_dict = dict()
    for line in open_file:
        variables = line.strip().split(';')
        person = variables.pop(0)
        return_dict[person] = [None, variables]
    return return_dict


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    return ''.join(['  ' + (str(person) + ' -> ' + str(d[person]) + '\n') for person in sorted(d, key = key, reverse = reverse)])


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return order[order.index(p1) if order.index(p1) < order.index(p2) else order.index(p2)]


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(man, men[man][match]) for man in men}

def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    if trace:
        print('Women preferences (unchanging)', dict_as_str(women), sep = '\n')
    men_copy = dict(men)
    unmatched = set(men.keys())
    while unmatched:
        if trace:
            print('Men preferences (current)', dict_as_str(men), 'unmatched men = {}\n'.format(unmatched), sep = '\n')
        curr_man = unmatched.pop()
        curr_woman = men[curr_man][prefs].pop(0)
        if curr_woman not in [men[man][match] for man in men]:
            men[curr_man][match], women[curr_woman][match] = curr_woman, curr_man
            if trace:
                print('{} proposes to {}; unmatched woman accepts proposal\n'.format(curr_man, curr_woman))
        else:
            if who_prefer(women[curr_woman][prefs], curr_man, women[curr_woman][match]) == curr_man:
                ex = women[curr_woman][match]
                unmatched.add(ex)
                women[curr_woman][match], men[ex][match], men[curr_man][match] = curr_man, None, curr_woman
                if trace:
                    print('{} proposes to {}; matched woman accepts proposal, rejecting match with {}\n'.format(curr_man, curr_woman, ex))
            else: 
                unmatched.add(curr_man)
                if trace:
                    print('{} proposes to {}; matched woman rejects proposal (likes current match better)\n'.format(curr_man, curr_woman))
    return extract_matches(men)

    
if __name__ == '__main__':
    # Write script here
    men_d = read_match_preferences(goody.safe_open('Enter a file representing men', 'r', 'file not found or there was an error'))
    women_d = read_match_preferences(goody.safe_open('Enter a file representing women', 'r', 'file not found or there was an error'))
    print('Men Preferences', dict_as_str(men_d), 'Women Preferences', dict_as_str(women_d), sep = '\n')
    trace_bool = prompt.for_bool('Trace Algorithm', True, 'Please enter True or False')
    print()
    print('matches = ', make_match(men_d, women_d, trace_bool))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
