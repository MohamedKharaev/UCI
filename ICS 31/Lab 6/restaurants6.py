# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2015

#Nic Obias 54865038 AND Lindsay Bennett 26838645 ICS 31 Sec.7 Lab asst 5.
# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection.
 r:  Remove a restaurant from the collection.
 s:  Search the collection for selected restaurants.
 e:  Add a dish to a restaurant.
 p:  Print all the restaurants.
 c:  Change prices for the dishes served.
 f:  Select restaurants with some prices at or below a given value.
 v:  Search for restaurants with a certain cuisine, and print the average price.
 w:  Search for restaurants that contain a certain dish.
 q:  Quit.
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=="e":
            rst = Ask_restaurant(C)
            if rst == None:
                print("That restaurant isn't in the collection!")
            else:
                mnu = Menu_enter(rst)
                rst._replace(menu = mnu)
        elif response=='p':
            print(Collection_str(C))
        elif response=="c":
            C = Change_restaurant_prices(C)
        elif response=="f":
            Return_priced_restaurants(C)
        elif response=="v":
            Return_cuisine_average(C)
        elif response=="w":
            Return_certain_dish(C)
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Return_certain_dish(C: list) -> None:
    '''print all the restaurants with a certain dish''' 
    inpt = input("Type the dish name or part of it.")
    for rst in C:
        for d in rst.menu:
            if inpt.strip().lower() in d.name.strip().lower():
                print(Restaurant_str(rst))

def Return_cuisine_average(C: list) -> None:
    '''print restaurants with a certain cuisine and their average'''
    inpt = input("What type of cuisine do you want to search for?")
    for rst in C:
        if inpt.strip().lower() == rst.cuisine:
            print(Restaurant_str(rst))
 
def Restaurant_str(self: Restaurant) -> str:
    '''return the display string for a restaurant'''
    string = "=====\n"
    string += "Name:     " + self.name + "\n" + \
        "Cuisine:  " + self.cuisine + "\n" + \
        "Phone:    " + self.phone + "\n" + \
        "Menu::" + "\n"
    if len(self.menu) == 0:
        string += "The menu's empty!" + "\n"
    else:
        for i in self.menu:
            string += Dish_str(i) + "\n"
        total_price = 0
        total_calories = 0
        for i in self.menu:
            total_price += i.price
            total_calories += i.cal
        avg_price = total_price/len(self.menu)
        avg_cal = total_calories/len(self.menu)
        string += "Avarage price:   ${:.2f}.   Average calories:   {:.1f}\n".format(avg_price, avg_cal)
        string += "=====\n"
    return string

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    rst = Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        []) #start w/ empty menu
    new_menu = Menu_enter(rst)
    rst = rst._replace(menu = new_menu)
    return rst

def Ask_restaurant(C: list) -> None:
    inpt = input("What is the name of the restaurant whose menu you want to edit?")
    for i in C:
        if i.name == inpt:
            return i
            break
    else:
        return None

def Change_restaurant_prices(C: list) -> list:
    '''returns new restaurants with raised prices'''
    p = float(input("What percentage do you want to change all the dish prices by?"))
    new_C = []
    for rst in C:
        mnu = rst.menu
        new_menu = []
        for dish in mnu:
            new_menu.append(dish._replace(price=dish.price + p/100*dish.price))
        new_C.append(rst._replace(menu=new_menu))
    return new_C

def Return_priced_restaurants(C: list) -> None:
    '''returns restaurants with at least one dish below a specified price'''
    inpt = float(input("What price do you want to compare?"))
    res = []
    for rst in C:
        if len(rst.menu) == 0:
            continue
        else:
            for dsh in rst.menu:
                if dsh.price > inpt:
                    break
            else:
                res.append(rst)
    if len(res) == 0:
        print("Sorry, there aren't any restaurants with prices that are at most that value.")
    else:
        print("Here's your list:")
        for i in res:
            print(Restaurant_str(i))
    

#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
#    res = []
#    res.append(Restaurant("Restaurant1", "thai", "123-456-789", []))
#    res.append(Restaurant("Restaurant2", "vegan", "123-456-789",
#                          [Dish("Food Burger", 2.5, 250), Dish("Taco Bu", 1.87, 450)]))
#    return res
    return []

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result


#### DISHES
#code for dishes
Dish=namedtuple ("Dish", "name price cal")
def Dish_str(Dish: Dish) -> str:
    '''Returns name, price, calories'''
    result = "Dish: {0.name} (${0.price:.2f}): {0.cal} cal".format(Dish)
    return result

def Dish_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the dish's price:  ")),
        float(input("Please enter the dish's calorie count:  ")))


#### MENUS
#code for menus
def Menu_enter(rst: Restaurant) -> None:
    '''edit menus'''
    current_menu = rst.menu
    print("Going to edit the menu now.")
    while True:
        inpt = input("Do you want to add a dish?")
        if inpt.strip().lower() == 'yes':
            current_menu.append(Dish_get_info())
        elif inpt.strip().lower() == 'no':
            print("Here's the current menu so far:")
            if len(current_menu) == 0:
                print("The menu's empty!")
            else:
                for i in current_menu:
                    print(Dish_str(i))
            return current_menu
        else:
            print("That's not a valid input!")
            


restaurants()

