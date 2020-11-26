#PartB.py
import sys
import string

alphanumeric = [str(x) for x in range(0, 10)] + [x for x in string.ascii_lowercase]

# O(1)
def read_in_chunks(file, chunk_size):
    """Creates an iterable that reads from a file in chunk_size bytes at a time"""
    return iter(lambda: file.read(chunk_size), "")

# O(N)
def create_file_set(file):
    """Creates a set with every token in a file"""
    return_set = set()
    with open(file) as fileobject:
        token = ""
        for chunk in read_in_chunks(fileobject, 4096):
            for byte in chunk:
                """This loop creates tokens and adds them to a set"""
                if byte.lower() in alphanumeric:
                    token += byte
                else:
                    if token:
                        return_set.add(token.lower())
                        token = ""
        #Handles Edge Case
        if token:
            return_set.add(token.lower())
    return return_set
                        
                    

if __name__ == '__main__':
    file1, file2 = sys.argv[1], sys.argv[2]
    print(len(create_file_set(file1).intersection(create_file_set(file2))))
