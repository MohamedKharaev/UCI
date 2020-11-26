# Mohamed Kharaev 43121144 & Ricardo Almazen 17738751. ICS Lab Sec 7

#c.1
hours = int(input("How many hours? "))
print('This many hours:', hours)
rate = float(input('How many dollars per hour? '))
print('This many dollars per hour:  $', rate)
print('Weekly salary:  $', hours * rate)

#c.2
name = input("What is your name? ")
print('Hello,', name)
print("It's nice to meet you.")
age = int(input('How old are you? '))
print("Next year you will be", age + 1)
print('Good-bye')

#d
KRONE_PER_EURO = 7.46
KRONE_PER_POUND = 8.60
KRONE_PER_DOLLAR = 6.62

print ('Please provide this information:')
name = input('business name: ')
euros = float(input('Number of euros: '))
pounds = float(input('Number of pounds: '))
dollars = float(input('Number of dollars: '))
print ('')
print ('Copenhagen Chamber of Commerce')
print ('Business name: ', name)
print (euros, 'euros is', (euros * KRONE_PER_EURO))
print (pounds, 'pounds is', (pounds * KRONE_PER_POUND))
print (dollars, 'dollars is', (dollars * KRONE_PER_DOLLAR))
print('Total krone: ', ((euros * KRONE_PER_EURO) +
                        (pounds * KRONE_PER_POUND) +
                        (dollars * KRONE_PER_DOLLAR)))
                     
#e
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)

#e.1
print(still_another[0])
#e.2
print(another[3])
#e.3
print((favorite[3] + another[3] + still_another[3])/3)
#e.4
print(favorite[2] < 1900)
#e.5
still_another2 = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 26.00)
print(still_another[3])
#e.6
still_another3 = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 26.00 * 1.20)
print(still_another[3])

#f
Animal = namedtuple('Animal', 'name species age weight favoriteFood')
Elephant = Animal('Jumbo', 'elephant', '50', '1000', 'peanuts')
Platypus = Animal('Perry', 'platypus', '7', '1.7', 'shrimp')
print(Elephant[3] < Platypus[3])

#g
booklist = [favorite, another, still_another]

#g.1
print(booklist[0][3] < booklist[1][3])
#g.2
print(booklist[0][2] > booklist[-1][2])

#h
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

#h.1
print(RC[2][0])
#h.2
print(RC[0][1] == RC[3][1])
#h.3
print(RC[-1][3])
#h.4
RC.sort()
print(RC[0][0], RC[1][0], RC[2][0], RC[3][0], RC[4][0], RC[5][0], RC[6][0])
#h.5
print(RC[-1][3])
#h.6
RC2 = [
    RC[0], RC[1], RC[-2], RC[-1]]
print(RC2)

#i
import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window
"""
#i.1
my_canvas.create_line(100, 100, 100, 300, fill='orange') # Draw orange line
my_canvas.create_line(100, 100, 300, 100, fill='blue')   # Draw blue line
my_canvas.create_line(300, 100, 300, 300, fill='orange') # Draw orange line
my_canvas.create_line(100, 300, 300, 300, fill='blue')   # Draw blue line

#i.2
my_canvas.create_line(100, 200, 200, 100)
my_canvas.create_line(200, 100, 300, 200)
my_canvas.create_line(300, 200, 200, 300)
my_canvas.create_line(200, 300, 100, 200)

#i.3
my_canvas.create_rectangle(200, 200, 400, 400)
my_canvas.create_line(200, 200, 300, 100, 400, 200)
my_canvas.create_rectangle(275, 400, 325, 325)
my_canvas.create_rectangle(275, 225, 325, 275)
my_canvas.create_line(300, 225, 300, 275)
my_canvas.create_line(275, 250, 325, 250)
"""

#i.4
my_canvas.create_oval(100, 100, 500, 300)
my_canvas.create_oval(200, 100, 400, 300)
my_canvas.create_oval(275, 175, 325, 225)


tkinter.mainloop()          # Combine all the elements and display the window


