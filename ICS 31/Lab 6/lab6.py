#Mohamed Kharaev 43121144 & Nicolas Obias 54865083. Lab Section 7

'<------Part C------->'

'<------Part C1------->'

def contains(s1: str, s2: str) -> bool:
    ''' checks if the second string occurs in the first string. If the second string does occur, the function returns True; if not, it returns False. '''
    return s2 in s1

assert contains('banana', 'ana')
assert not contains('racecar', 'ck')
assert contains('Hoodie', 'die')
assert not contains('Restaurant', 'wer')

'<------Part C2------->'
punctuation = ".,<>/?;:\|]}[{=+-_)(*&^%$#@!`~"

def sentence_stats(s1: str):
    '''that takes in a string as a parameter and prints out these statistics about the string: its length in characters, its length in words, and the average length of each word.'''
    s2 = ""
    for letter in s1:
        if letter in punctuation:
            s2 += " "
        else:
            s2 += letter
    print("Characters:", len(s2))
    l1 = s2.split()
    print("Words:", len(l1))
    print("Average word length:", len(s2.replace(" ", ""))/len(l1))

sentence_stats('***The ?! quick brown fox:  jumps over the lazy dog.')

'<------Part C3------->'
def initials(s1: str) -> str:
    '''takes as input a string representing a full name (e.g.,  Robert B. Qwerty) and returns the initials of the name in all capital letters'''
    answer = ""
    l1 = s1.split()
    for name in l1:
        answer += name[0]
    return answer.upper()

assert initials('Bill Cody') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'


'<------Part D------->'

'<------Part D1------->'
from random import randrange

for i in range(50):
    print(randrange(11))

for i in range(50):
    print(randrange(1,7))

def roll2dice() -> int:
    '''returns number of two dice rolls'''
    r1 = randrange(1,7)
    r2 = randrange(1,7)
    return r1 + r2

for i in range(50):
    print(roll2dice())

def distribution_of_rolls(num: int):
    '''takes a number and returns roll distribution'''
    print("Distribution of dice rolls\n")
    roll_list = [0] * 11
    for i in range(num):
        dtotal = roll2dice()
        roll_list[dtotal-2] += 1
    format_str = "{:2}:{:5} ({:4.1f}%)  {}"
    x = 2
    
    for i in roll_list:
        print(format_str.format(x,i,i/num*100,"*"*i))
        x+=1
    print("-----------------------------")
    print(" " * 6 + str(num) + " rolls")

distribution_of_rolls(200)

'<------Part E1------->'
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate_right(num: int) -> str:
    answer = ""
    for i in range(num, 26):
        answer += ALPHABET[i]
    for i in range(num):
        answer += ALPHABET[i]
    return answer


def caesar_encrypt(s1: str, num: int) -> str:
    s1 = s1.lower()
    transtab = str.maketrans(ALPHABET, rotate_right(num))
    return s1.translate(transtab)

def caesar_decrypt(s1: str, num: int) -> str:
    s1 = s1.lower()
    transtab = str.maketrans(rotate_right(num), ALPHABET)
    return s1.translate(transtab)

print(caesar_encrypt("zyzzyvas is a weird word . Like what is that", 5))
print(caesar_encrypt("like morning lectures", 5))

'<------Part E2------->'

print(caesar_decrypt("ko c qm", 2))

'<------Part E3------->'
