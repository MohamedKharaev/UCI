#Mohamed Kharaev 43121144 & Ziyuan Zhang 18658215. Lab Section 7

print("<------- 1 ------->")

def test_number(num: int, sign: str) -> bool:
    '''returns True if the number has the property indicated
    by the string, and False if it doesn't'''
    lst = ["even", 'odd', 'positive', 'negative']
    if sign not in lst:
        return False
    elif sign == "even":
        if num % 2 != 0:
            return False
    elif sign == "odd":
        if num % 2 != 1:
            return False
    elif sign == "positive":
        if num < 0:
            return False
    elif sign == "negative":
        if num > 0:
            return False
        
    return True

assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')

print("<------- 2 ------->")

def display():
    '''prompts the user to enter any word or phrase and
    then prints out every character in that phrase, one per line'''
    ui = input('Enter a word: ')
    for l in ui:
        print (l)
display()

print("<------- 3 ------->")

def square_list(numbers: list):
    '''takes a list of integers and prints out each integer squared'''
    for nums in numbers:
        print(nums ** 2)

square_list([2,3,4,10])

print("<------- 4 ------->")

def match_first_letter(letter: str, lst2:list):
    '''takes a one-character string and a list of strings and prints
    all the strings in the list that start with the specified character'''
    for things in lst2:
        if letter in things:
            print(things)
match_first_letter('I', ['Iron Man', "Iron Man 2",
                         'The avengers', 'Superman', 'I am Legend'])

print("<------- 5 ------->")

def match_area_code(acodes: list, pcodes: list):
    '''takes as a list of telephone area codes (three-digit strings) and a
    list of phone numbers in the form shown below. The function will
    print the phone numbers whose area code is on the list of area codes.'''
    for pcode in pcodes:
        if pcode[1:4] in acodes:
            print(pcode)

match_area_code(['949', '714'], ['(714)824-1234',
                                 '(419)312-8732', '(949)555-1234'])

print("<------- 6 ------->")

def match_area_codes(acodes: list, pcodes: list)-> list:
    '''returns a list of the matching numbers. '''
    result = []
    for pcode in pcodes:
        if pcode[1:4] in acodes:
            result.append(pcode)
    return result

assert match_area_codes(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234']) == ["(714)824-1234", "(949)555-1234"]

print("<------- d.1 ------->")

def is_vowel (iv: str) -> bool:
    '''takes a one-character-long string and returns True
    if that character is a vowel and False otherwise.'''
    vowels = "aeiouAEIOU"
    if iv in vowels:
        return True
    else:
        return False
assert is_vowel('v') == False

print("<------- d.2 ------->")

def print_nonvowels(nv: str):
    '''takes a string and prints out all the characters
    in the string that are not vowels'''
    for letter in nv:
        if is_vowel(letter) == False:
            print(letter)

print_nonvowels("Hello")

print("<------- d.3 ------->")
    
def non_vowels(nv2: str):
    '''takes a string and returns a string containing all
    the characters in the parameter string that are not vowels'''
    result = ""
    for letter in nv2:
        if is_vowel(letter) == False:
            result += letter
    return result

assert non_vowels("Hello") == "Hll"

print("<------- d.4 ------->")

def consanants(nv3: str):
    '''takes a string and returns a string containing all
    the letters in the parameter string that are not vowels'''
    consanant_str = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result = ""
    for letter in nv3:
        if letter in consanant_str:
            result += letter
    return result

assert consanants("Hello World") == "HllWrld"

print("<------- d.5 ------->")

def select_letters(sl1:str, sl2:str) -> str:
    '''takes two parameters, both strings, and returns a string. If the first
    parameter is 'v', it returns a string containing all the vowels in
    the second parameter; if the first parameter is 'c', it returns a
    string containing all the consonants in the second parameter. If the
    first parameter is anything else, it returns the empty string'''
    result = ''
    if sl1 == 'v':
        for letter in sl2:
            if is_vowel(letter) == True:
                result += letter
        return result
    elif sl1 == 'c':
        return consanants(sl2)
    else:
        return result

assert select_letters('v', 'facetiously') == "aeiou"
assert select_letters('c', 'facetiously') == "fctsly"

print("<------- d.6 ------->")

def hide_vowels(hv: str) -> str:
    '''takes a string and returns a string in which every vowel in the parameter
    is replaced with a hyphen ("-") and all other characters remain unchanged.'''
    result = ""
    for letter in hv:
        if is_vowel(letter) == True:
            result += "-"
        else:
            result += letter
    return result

assert hide_vowels("Hello There") == "H-ll- Th-r-"

print("<------- e ------->")
from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
McDonalds = Restaurant('McDonalds', 'burger', '911', 'big mac', 3.99)

def Restaurant_change_price(rest: Restaurant, price_add: float) -> Restaurant:
    '''takes two arguments, a Restaurant object and a number, and returns
    a Restaurant object with the same contents as the parameter except
    that the price has been increased by the specified number'''
    return Restaurant(rest.name, rest.cuisine, rest.phone, rest.dish, rest.price + price_add)

assert Restaurant_change_price(McDonalds, 1.00) == Restaurant('McDonalds', 'burger', '911', 'big mac', 4.99)

print("<------- f ------->")

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]

print("<------- f.1 ------->")

def alphabetical(rests: 'List of Restaurants') -> 'List of Restaurants':
    '''takes a list of restaurants and returns that list
    in alphabetical order by name'''
    return sorted(rests)

print(alphabetical(RL))

print("<------- f.2 ------->")

def alphabetical_names(rests: 'List of Restaurants') -> 'List of Strings':
    '''takes a list of restaurants and returns a list of the names of
    all the restaurants in alphabetical order by name'''
    answer = []
    rests = sorted(rests)
    for rest in rests:
        answer.append(rest.name)
    return answer

print(alphabetical_names(RL))

print("<------- f.3 ------->")

def all_Thai(rests: 'List of Restaurants') -> 'List of Restaurants':
    '''takes a list of restaurants and returns a list of all the Thai restaurants'''
    answer = []
    for rest in rests:
        if rest.cuisine == "Thai":
            answer.append(rest)
    return answer

print(all_Thai(RL))

print("<------- f.4 ------->")

def select_cuisine(rests: 'List of Restaurants', cui: str) -> 'List of Restaurants':
    '''takes a list of restaurants and a string representing a cuisine. It
    should return a list of all the
    restaurants that serve the specified cuisine.'''
    answer = []
    for rest in rests:
        if rest.cuisine == cui:
            answer.append(rest)
    return answer

print(select_cuisine(RL, "Italian"))

print("<------- f.5 ------->")

def select_cheaper(rests: 'List of Restaurants', num: float) -> 'List of Restaurants':
    '''takes a list of restaurants and a number (a float) and returns a list
    of all the restaurants whose price is less than the specified number.'''
    answer = []
    for rest in rests:
        if rest.price < num:
            answer.append(rest)
    return answer

print(select_cheaper(RL, 10.00))

print("<------- f.6 ------->")

def average_price(rests: 'List of Restaurants') -> float:
    '''takes a list of restaurants and returns the
    average price of (the best dishes at) those restaurants.'''
    answer = 0
    for rest in rests:
        answer += rest.price
    return answer/len(rests)
print(average_price(RL))

print("<------- f.7 ------->")

print(average_price(select_cuisine(RL, "Indian")))

print("<------- f.8 ------->")

print(average_price((select_cuisine(RL, "Chinese")) + select_cuisine(RL, "Thai")))

print("<------- f.9 ------->")

print(alphabetical_names(select_cheaper(RL, 15.00)))

print("<------- g ------->")

import tkinter              

my_window = tkinter.Tk()    

my_canvas = tkinter.Canvas(my_window, width=500, height=500)
my_canvas.pack()            

def create_rectangle_from_center(x: int, y: int, height: int, width: int):
    '''creates a rectangle in tkinter with the specified height and width
    with the center being the x and y coordinates provided'''
    my_canvas.create_rectangle(x - ((1/2) * width), y - ((1/2) * height),
                              x + ((1/2) * width), y + ((1/2) * height))

create_rectangle_from_center(250, 250, 100, 200)
