import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    return {(fq[:x]) for x in irange(len(fq))}


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    for x in all_prefixes(new_query):
        prefix[x].add(new_query) 
    query[new_query] += 1


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    return_tuple = (defaultdict(set), defaultdict(int))
    for line in open_file:
        return_tuple[1][tuple(line.split())] += 1
        return_tuple[0].update( zip( all_prefixes(line.split()), 1))
    return return_tuple


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    return_str = ''
    for a in sorted(d, key = key, reverse = reverse):
        return_str += ('  ' + a + ' -> ' + d[a] + '\n')
    return return_str


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    pass





# Script

if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
