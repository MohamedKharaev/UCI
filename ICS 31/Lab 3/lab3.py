#Mohamed Kharaev 43121144 & Dylan Leighton 62407404. Lab Section 7

#<--------Part C-------->

#C.1
def abbreviate(month: str) -> str:
    #Returns the abbrevitaion of the parameter
    month_abb = ""
    for i in range(3):
        month_abb += month[i]
    return month_abb
assert abbreviate('January') == 'Jan'
assert abbreviate('April') == 'Apr'
assert abbreviate('December') == 'Dec'

#C.2
def find_area_square(length: int) -> int:
    #Returns the area of a square with parameter length
    return length ** 2

assert find_area_square(2) == 4
assert find_area_square(10) == 100
assert find_area_square(5) == 25

#C.3
    #Retrurns the area of a circle with paramter radius
import math
def find_area_circle(radius: int) -> float:
    return math.pi * (radius ** 2)

assert find_area_circle(1) == 3.141592653589793
assert find_area_circle(5) == 78.53981633974483

#C.4
    #Returns the even numbers in parameter list
def print_even_numbers(lst: list):
    for number in lst:
        if number % 2 == 0:
            print(number)


#C.5
def calculate_shipping(weight: float) -> float:
    #Returns the cost of shipping a package with parameter weight
    if weight < 2:
        return 2.00
    elif weight < 10:
        return 5.00
    else:
        return 5.00 + ((weight - 10) * 1.50)

assert calculate_shipping(1) == 2.00
assert calculate_shipping(5) == 5.00
assert calculate_shipping(15) == 12.50

#C.6   
import tkinter
def create_square(x: int, y: int, length: int):
    #draws a square with the top left coordinate (x, y) and a specified length
    my_window = tkinter.Tk()
    my_canvas = tkinter.Canvas(my_window, width = 500, height = 500)
    my_canvas.pack()

    my_canvas.create_rectangle(x, y, x + length, y + length)

    tkinter.mainloop()

#C.7  
def create_circle(x: int, y: int, diameter: int):
    #draws a circle with a specifed diameter and a top left coordinate (x,y)
    my_window = tkinter.Tk()
    my_canvas = tkinter.Canvas(my_window, width = 500, height = 500)
    my_canvas.pack()

    my_canvas.create_oval(x, y, x + diameter, y + diameter)

    tkinter.mainloop()

# <----------Part D---------->

from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

#D.1
def restaurant_price(rest: Restaurant) -> int:
    #Returns the price of the most expensive dish at a given restaurant
    return rest.price
assert restaurant_price(RC[1]) == 5.50
assert restaurant_price(RC[4]) == 5.50

#D.2
RC.sort(key=restaurant_price)

#D.3
def costliest(rests: list) -> str:
    #Returns the restaurant name of the
    #restaurant with the dish of the highest price within a list
    RC.sort(key=restaurant_price)
    return(RC[-1].name)
assert costliest(RC) == "Noma"

#D.4
def costliest2(rests: list) -> str:
    #Returns the restaurant name of the restaurant with the dish of the
    #highest price without altering the original list
    RC2 = sorted(RC, key=restaurant_price)
    return(RC[-1].name)
assert costliest2(RC) == "Noma"

print("<--------Part E-------->")

# <----------Part E---------->
Book = namedtuple('Book', 'author title genre year price instock')

BSI = [
    Book("Dr.Seuss", "Green Eggs and Ham", "Children's Literature", 1960, 5.99, 50),
    Book("J.K.Rowling", "Harry Potter 1", "Fantasy", 1997, 13.99, 70),
    Book("Ken Kesey", "One Flew Over the Cuckoo's Nest", "Fiction", 1962, 9.99, 60),
    Book("Harper Lee", "To Kill a Mockingbird", "Southern Gothic", 1960, 5.99, 10),
    Book("Suzanne Collins", "Hunger Games", "Adventure", 2008, 10.99, 50),
    Book("Stephanie Meyer", "Twilight", "Romance", 2005, 14.99, 60),
    ]

#E.1
for book in BSI:
    print(book.title)

#E.2
def book_title(book: Book) -> str:
    return book.title

BSI2 = sorted(BSI, key=book_title)
for book in BSI2:
    print(book.title)

#E.3
for book in BSI:
    book = book._replace(price = book.price * 1.1)

#E.4
for book in BSI:
    if book.genre == "Technology":
        print(book.title)

#E.5
Classic = []
Recent = []
for book in BSI:
    if book.year < 2000:
        Classic.append(book)

for book in BSI:
    if book.year >= 2000:
        Recent.append(book)

print("More titles before 2000 (", len(Classic), "vs.", len(Recent), ")") 

#E.6
def inventory_value(book: Book) -> int:
    #Returns the value of inventory of the parameter book
    return book.price * book.instock
assert inventory_value(BSI[0]) == 299.5
assert inventory_value(BSI[1]) == 979.3


def top_value(books: list):
    #prints the book from a list with the highest inventory value
    answer = books[0]
    for book in books:
        if inventory_value(book) > inventory_value(answer):
            answer = book
    print("The highest-value book is", answer.title, "by",
          answer.author, "at a value of", inventory_value(answer))

top_value(BSI)

#F
import tkinter
import tkinter              

my_window = tkinter.Tk()    

my_canvas = tkinter.Canvas(my_window, width=500, height=500)
my_canvas.pack()            


def draw_face(x, y, diameter):
    #Draws a face with a given diameter and top left coordinates (x, y)
    my_canvas.create_oval(x, y, x + diameter, y + diameter)
    draw_eye(x + (diameter/10), y + (3*diameter/10), 3*diameter/10, 3*diameter/20)
    draw_eye(x + (3 * diameter/5), y + (3*diameter/10), 3*diameter/10, 3*diameter/20)
    draw_nose(x + (diameter/2), y + (diameter/2), diameter/10, 3 * diameter/50)
    draw_mouth(x + (diameter/4), y + (7 * diameter/10), diameter/7, diameter/2)

def draw_eye(topleftx, toplefty, lengtheye, heighteye):
    #Draws an eye with given parameter
    my_canvas.create_oval(topleftx, toplefty,
                          topleftx + lengtheye, toplefty + heighteye)

    my_canvas.create_oval(topleftx + (lengtheye/2) - (heighteye/2),
                          toplefty + heighteye,
                          topleftx + (lengtheye/2) + (heighteye/2),
                          toplefty) 

    my_canvas.create_oval(topleftx + (lengtheye/2) - (heighteye/4),
                          toplefty + heighteye - (1/4) * heighteye,
                          topleftx + (lengtheye/2) + (heighteye/4),
                          toplefty + (1/4) * heighteye)

def draw_nose(topleftx, toplefty, height, length):
    #Draws an nose with given top left coordinate (topleftx, topleft y) and
    # height and length
    my_canvas.create_line(topleftx, toplefty, topleftx, toplefty + height,
                          topleftx + length, toplefty + height)

def draw_mouth(topleftx, toplefty, height, length):
    #Draws a mouth with given top left coordinate (topleftx, topleft y) and
    #height and length
    my_canvas.create_line(topleftx, toplefty,
                          topleftx + length/2, toplefty + height,
                          topleftx + length, toplefty)
    
draw_face(0, 0, 100)
draw_face(100, 100, 300)
draw_face(400, 400, 50)
