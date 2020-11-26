#PartA.py
import sys
import string
from collections import defaultdict



# O(1)
def read_in_chunks(file, chunk_size):
    """Creates an iterable that reads from a file in chunk_size bytes at a time"""
    return iter(lambda: file.read(chunk_size), "")

# O(Tokens)
def print_dict(dictionary):
    """Prints dictionary in desired format"""
    
    for k in sorted(dictionary, key = lambda y: (dictionary[y] * -1, y)):
        print(k + '\t' + str(dictionary[k]))

if __name__ == '__main__':
    filename = sys.argv[1]
    token_dictionary = defaultdict(int)
    alphanumeric = [str(x) for x in range(0, 10)] + [x for x in string.ascii_lowercase]

    with open(filename) as fileobject:
        token = ""
        for chunk in read_in_chunks(fileobject, 4096):
            # O(N)
            for byte in chunk:
                """This loop adds each byte to the token string if it is alphanumeric
                If a byte isn't alphanumeric, loop increments current token string in
                dict and resets token string"""
                if byte.lower() in alphanumeric:
                    token += byte
                else:
                    if token:
                        token_dictionary[token.lower()] += 1
                        token = ""
        # Handles Edge Case
        if token:
            token_dictionary[token.lower()] += 1

    print_dict(token_dictionary)
