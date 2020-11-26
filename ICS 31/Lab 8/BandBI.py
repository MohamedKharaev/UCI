#Mohamed Kharaev 43121144 & Elizabeth Chen 75557458. Lab Section 7

infile_name = input("What file would you like to read?: ")
infile = open(infile_name, 'r')
outfile = open('outfile.txt', 'w')

bedrooms = []


def readcommand(statement: str):
    '''Reads the command provided in the infile'''
    command = statement.strip().split()[0]
    rest_of_statement = statement.strip()[3:] + "\n"
    
    if command.lower() == 'pl':
        outfile.write(rest_of_statement)
    elif command.lower() == 'ab':
        bedrooms.append(statement.split()[1])
    elif command.lower() == 'bl':
        bedrooms_amount = 'Number of bedrooms in service:  {}\n'.format(len(bedrooms))
        outfile.write(bedrooms_amount)
        outfile.write('------------------------------------\n')
        for bedroom in bedrooms:
            outfile.write(bedroom)
            outfile.write("\n")

for line in infile:
    readcommand(line)
    
outfile.close()
