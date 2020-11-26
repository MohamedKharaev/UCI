# Mohamed Kharaev 43121144 Lab Sec 13
import api_handling
import classes
import sys

def input_locations() -> [str]:
    '''returns a list of user-entered locations'''
    result = list()
    for i in range(int(input())):
        result.append(input())
    return result

def output_classes() -> ['class instances']:
    '''returns a list of user-entered class instances'''
    result = list()
    for i in range(int(input())):
        instance = 'classes.' + input().lower()
        result.append(eval(instance))
    return result
        

if __name__ == '__main__':
    locations = input_locations()
    destination_url = api_handling.create_destination_url(locations)
    try:
        destination_json = api_handling.parse_url(destination_url)
    except:
        print('MAPQUEST ERROR')
        sys.exit()
    outputs = output_classes()
    for class_instance in outputs:
        try:
            class_instance.output(destination_json)
            print()
        except(KeyError):
            print('NO ROUTE FOUND')
            break
        except:
            print('MAPQUEST ERROR')
            break
        
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.')
