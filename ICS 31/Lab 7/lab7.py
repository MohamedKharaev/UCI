#Mohamed Kharaev 43121144 & Cameron Maberto 14068416. Lab Section 7

surnames = open('surnames.txt', 'r')
malenames = open('malenames.txt', 'r')
femalenames = open('femalenames.txt', 'r')
dictionary = open('wordlist.txt', 'r')

surnames_list = surnames.readlines()
malenames_list = malenames.readlines()
femalenames_list = femalenames.readlines()
dictionary_list = dictionary.readlines()

surnames.close()
malenames.close()
femalenames.close()
dictionary.close()
print('<-------Part C-------->')

import random

def random_names(num: int) -> 'List of names':
    '''takes an integer and returns a list of
    that many strings, with each string a randomly generated name'''
    answer = []

    for i in range(num):
        Last_index = random.randrange(1000)
        First_index = random.randrange(1000)
        Gender_index = random.randrange(2)

        Lastname = surnames_list[Last_index].split()[0].lower()

        if Gender_index == 0:
            Firstname = malenames_list[First_index].split()[0].lower()
        else:
            Firstname = femalenames_list[First_index].split()[0].lower()

        answer.append(Lastname.title() + ", " + Firstname.title())

    return answer

print(random_names(5))

print('<-------Part D-------->')

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate_right(num: int) -> str:
    answer = ""
    for i in range(num, 26):
        answer += ALPHABET[i]
    for i in range(num):
        answer += ALPHABET[i]
    return answer

def caesar_decrypt(s1: str, num: int) -> str:
    s1 = s1.lower()
    transtab = str.maketrans(rotate_right(num), ALPHABET)
    return s1.translate(transtab)

def Caesar_break(text: str) -> str:
    '''takes a ciphertext string (encrypted using a Caesar cipher as we
    did last week) and returns the plaintext for that string, without
    having the key.'''
    max_index = 0
    max_dictionary_words = 0
    for i in range(26):
        temp = caesar_decrypt(text, i)
        temp = temp.split(" ")
        count = 0
        for word in temp:
            if word+"\n" in dictionary_list:
                count += 1
        if count > max_dictionary_words:
            max_dictionary_words = count
            max_index = i
    return caesar_decrypt(text, max_index)

print('<-------Part D2-------->')

print(Caesar_break("edeedafx nx f bjnwi btwi . qnpj bmfy nx ymfy"))
print(Caesar_break("qjhyzwjx"))
                
print('<-------Part E2-------->')
print('<-------Part E3-------->')
print('<-------Part E4-------->')

def copy_file(s1: str): 
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w')
    lines = infile.readlines()

    if s1 == 'line numbers':
        count = 1
        for line in lines:
            str1 = '{:5}: {}'.format(count, line)
            outfile.write(str1)
            count += 1
    elif s1 == 'Gutenberg trim':
        firstline = 0
        lastline = 0
        for line in range(len(lines)):
            if "*** START" in lines[line]:
                firstline = line + 1
                break
        for line in range(len(lines)):
            if "*** END" in lines[line]:
                lastline = line
                break
        for line_num in range(firstline, lastline):
            outfile.write(lines[line_num])
    elif s1 == 'statistics':
        empty_lines = 0
        for line in lines:
            if line == "\n":
                empty_lines += 1

        avg_characters_per_line = 0

        characters = 0
        for line in lines:
            characters += len(line)
        
        outfile.write("{:8.1f} lines in the file\n".format(len(lines)))
        outfile.write("{:8.1f} empty lines\n".format(empty_lines))
        outfile.write("{:8.1f} average characters per line\n".format(characters/len(lines)))
        outfile.write("{:8.1f} average characters per non-empty line\n".format(characters/(len(lines)-empty_lines)))
        for line in lines:
            outfile.write(line)
    else:
        for line in lines:
            outfile.write(line)

    infile.close()
    outfile.close()

copy_file('statistics')







