# Mohamed Kharaev 43121144 & Jarod Robinson 87289947. Lab sec 7

#---------------Stage 1-----------------
from collections import namedtuple
import datetime
Reservation = namedtuple('Reservation', 'roomNum arrivalDate departureDate name confirmation')
confirmationNum = 1        

bedroom_list = []
command_list = ['ab', 'bl', 'pl', '**', 'bd', 'nr', 'rl', 'rd', 'rb', 'rc', 'la', 'ld', 'lf', 'lo']
reservation_list = []

def fixDate(d: datetime)-> str:
    ''' formats datetime as a string, removing hours
    '''
    temp = str(d).replace('00:00:00', '').split('-')
    return '{}/{}/{}'.format(temp[1], temp[2].strip(), temp[0])

def confirmationAdd():
    ''' adds one to the confirmation number
    '''
    global confirmationNum
    confirmationNum += 1

def readContent(line: str):
    ''' returns the contents of the string disregarding commands
    '''
    for command in command_list:
        if command in line.lower():
            return line.strip().replace(line.strip()[:2], '').strip()

def addBedroom(line: str):
    ''' adds the given bedroom in line to bedroom_list if it's
    not already on the list
    '''
    checkRoom = readContent(line).replace(' ', '')
    for room in bedroom_list:
        if room == checkRoom:
            print("Sorry, can't add room {} again; it's already on the list.".format(checkRoom))
            return
    bedroom_list.append(checkRoom)

def printBedrooms():
    ''' print all of the available bedrooms by line
    '''
    print('Number of bedrooms in service:{:3d}'.format(len(bedroom_list)))
    print('------------------------------------')
    bedroom_list.sort()
    for num in bedroom_list:
        print(num)

def deleteBedroom(line: str):
    ''' deletes the given room from bedroom_list
    '''
    room = readContent(line)
    try:
        bedroom_list.remove(room)
    except ValueError:
        print("Sorry, can't delete", readContent(line), "it is not in service now.")
    for reserve in reservation_list[:]:
        if reserve.roomNum == room:
            print('Deleting room {} forces cancellation of this reservation:'.format(room))
            print('      {} arriving {} and departing {} (Conf. #{})'.format(reserve.name, fixDate(reserve.arrivalDate), fixDate(reserve.departureDate), reserve.confirmation))
            reservation_list.remove(reserve)

def convertToDate(elem: str) -> datetime:
    ''' converts a str object to datetime
    '''
    return datetime.datetime.strptime(elem, '%m/%d/%Y')

def createReservation(line: str):
    ''' creates a reservation given the parameters in the line
    '''
    elem = readContent(line).split(' ')
    while '' in elem:
        elem.remove('')    
    name = ''
    for n in elem[3:]:
        name += n + ' '
    checkReserve = Reservation(elem[0],
                               convertToDate(elem[1]),
                               convertToDate(elem[2]),
                               name,
                               confirmationNum)

    def checkRoomAvailable() -> bool:
        ''' check if the room is available
        '''
        for num in bedroom_list:
            if checkReserve.roomNum == num:
                return True
        return False
    
    def checkValidReservation() -> bool:
        ''' Checks if the requested reservation is valid
        '''
        

        #check if the reservation conflicts with another
        for reserve in reservation_list:
            if reserve.roomNum == checkReserve.roomNum:
                if checkReserve.arrivalDate >= reserve.arrivalDate and checkReserve.arrivalDate < reserve.departureDate:
                    print("Sorry, can't reserve room {} ({} to {});".format(checkReserve.roomNum, fixDate(checkReserve.arrivalDate), fixDate(checkReserve.departureDate)))
                    print("    it's already booked (Conf. #{})".format(reserve.confirmation))
                    return False
                elif checkReserve.departureDate > reserve.arrivalDate and checkReserve.departureDate <= reserve.departureDate:
                    print("Sorry, can't reserve room {} ({} to {});".format(checkReserve.roomNum, fixDate(checkReserve.arrivalDate), fixDate(checkReserve.departureDate)))
                    print("    it's already booked (Conf. #{})".format(reserve.confirmation))
                    return False

        #check if the arrival and departure dates confict
        if checkReserve.arrivalDate > checkReserve.departureDate:
            print("Sorry, you can't reserve room {} ({} to {});".format(checkReserve.roomNum, fixDate(checkReserve.arrivalDate), fixDate(checkReserve.departureDate)))
            print("    can't leave before you arrive.")
            return False
        elif checkReserve.arrivalDate == checkReserve.departureDate:
            print("Sorry, you can't reserve room {} ({} to {});".format(checkReserve.roomNum, fixDate(checkReserve.arrivalDate), fixDate(checkReserve.departureDate)))
            print("    can't arrive and leave on the same day.")
            return False

        return True
        
            
    if checkValidReservation() and checkRoomAvailable():
        print('Reserving room {} for {} -- Confirmation #{}'.format(checkReserve.roomNum, checkReserve.name, checkReserve.confirmation))
        print('      (arriving {}, departing {})           '.format(fixDate(checkReserve.arrivalDate), fixDate(checkReserve.departureDate)))
        reservation_list.append(checkReserve)
        confirmationAdd()

def readReservations():
    ''' prints a list of reservations formatted accordingly
    '''
    print('Number of reservations: {}'.format(len(reservation_list)))
    print('No. Rm.  Arrive       Depart      Guest')
    print('----------------------------------------------')
    reservation_list.sort(key=lambda x: x.arrivalDate)
    for r in reservation_list:
          print('{:3d} {:3} {} {} {}'.format(r.confirmation, r.roomNum, fixDate(r.arrivalDate), fixDate(r.departureDate), r.name))

def deleteReservation(line: str):
    ''' deletes reservation with given comfirmation # from the list
    '''
    flag = 0
    for r in reservation_list:
        if readContent(line) == str(r.confirmation):
            reservation_list.remove(r)
            flag+=1
    if flag == 0:
        print("Sorry, can't cancel reservation; no confirmation number {}".format(readContent(line)))

def reservationsByBedroom(line: str):
    ''' prints all reservations under the given room number
    '''
    print('Reservations for room {}:'.format(readContent(line)))
    for reserve in reservation_list:
        if reserve.roomNum == readContent(line):
            print('  {:10s} to {:10s}:  {}'.format(fixDate(reserve.arrivalDate), fixDate(reserve.departureDate), reserve.name))

def reservationsByGuest(line: str):
    ''' print all of a single guest's reservations
    '''
    print('Reservations for {}'.format(readContent(line)))
    for reserve in reservation_list:
        if reserve.name.strip() == readContent(line):
            print('  {:10s} to {:10s}: {}'.format(fixDate(reserve.arrivalDate), fixDate(reserve.departureDate), reserve.roomNum))
            
def guestArrivals(line: str):
    ''' prints all guests arriving on the given day
    '''
    print('Guests arriving on {}:'.format(readContent(line)))
    for reserve in reservation_list:
        if fixDate(reserve.arrivalDate) == readContent(line):
            print('  {} ({})'.format(reserve.name, reserve.roomNum))

def guestDepartures(line: str):
    ''' prints all guests arriving on the given day
    '''
    print('Guests departing on {}:'.format(readContent(line)))
    for reserve in reservation_list:
        if fixDate(reserve.departureDate) == readContent(line):
            print('  {} ({})'.format(reserve.name, reserve.roomNum))

def rooms(line: str, flag: bool):
    ''' prints all of the free bedrooms between two given dates if True, and all of the occupied rooms if False
    '''
    arrival = convertToDate(readContent(line).split()[0])
    departure = convertToDate(readContent(line).split()[1])
    lst = []
    for reserve in reservation_list:
        if arrival > reserve.arrivalDate and arrival < reserve.departureDate:
            lst.append(reserve.roomNum)
        elif departure > reserve.arrivalDate and departure < reserve.departureDate:
            lst.append(reserve.roomNum)
    if flag:
        print('Bedrooms free between {} and {}'.format(fixDate(arrival), fixDate(departure)))
        for room in bedroom_list:
            if room not in lst:
                print(room)
    else:
        print('Bedrooms occupied between {} and {}'.format(fixDate(arrival), fixDate(departure)))
        for room in lst:
            print(room)
    

            
def readLine(line: str):
    ''' reads and runs the commands on the given line
    '''
    command = line.strip().lower()[:2]
    if command == '**':
        return
    elif command == 'pl':
        print(readContent(line))
    elif command == 'ab':
        addBedroom(line)
    elif command == 'bl':
        printBedrooms()
    elif command == 'bd':
        deleteBedroom(line)
    elif command == 'nr':
        createReservation(line)
    elif command == 'rl':
        readReservations()
    elif command == 'rd':
        deleteReservation(line)
    elif command == 'rb':
        reservationsByBedroom(line)
    elif command == 'rc':
        reservationsByGuest(line)
    elif command == 'la':
        guestArrivals(line)
    elif command == 'ld':
        guestDepartures(line)
    elif command == 'lf':
        rooms(line, True)
    elif command == 'lo':
        rooms(line, False)


def interpret_input(file: str):
    ''' takes the input file and runs the commands given
    '''
    for line in file.readlines():
        readLine(line)



def addBedrooms():
    for room in bedroom_list:
        newFile.write('ab {}\n'.format(room))

def addReservations():
    for r in reservation_list:
        newFile.write('nr {} {} {} {}\n'.format(r.roomNum, fixDate(r.arrivalDate), fixDate(r.departureDate), r.name))

while True:
    try:
        last = input("Enter the name of yesterday's file: ")
        previousFile = open(last)
        interpret_input(previousFile)
        previousFile.close()
        break
    except FileNotFoundError:
        print('\nInvalid file name, please try again. (Note: file extensions are necessary)\n')

while True:
    try:
        current = input("Now enter the name of today's file: ")
        currentFile = open(current)
        interpret_input(currentFile)
        currentFile.close()
        break
    except FileNotFoundError:
        print('\nInvalid file name, please try again. (Note: file extensions are necessary)\n')


name = input('Enter the name of your new file: ')
newFile = open(name + '.txt', 'w+')
print('Your file has been saved! Goodbye.')

addBedrooms()
addReservations()
newFile.close()
