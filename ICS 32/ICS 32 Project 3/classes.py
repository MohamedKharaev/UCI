# Mohamed Kharaev 43121144 Lab Sec 13
import api_handling

class totaldistance():
    def output(json_dict: dict) -> None:
        '''Prints a formatted version of the distance of a json dictionary for a trip'''
        miles = json_dict['route']['distance']
        print('TOTAL DISTANCE: {} miles'.format(round(miles)))

class totaltime():
    def output(json_dict: dict) -> None:
        '''Prints a formatted version of the total time of a json dictionary for a trip'''
        seconds = json_dict['route']['time']
        print('TOTAL TIME: {} minutes'.format(round(seconds/60)))

class steps():
    def output(json_dict: dict) -> None:
        '''Prints a formatted version of the steps of a json dictionary for a trip'''
        steps = list()
        for leg in json_dict['route']['legs']:
            for maneuver in leg['maneuvers']:
                steps.append(maneuver['narrative'])
        print('STEPS')
        for step in steps:
            print(step)

class latlong():
    def _format_latlong(latlong: dict) -> str:
        '''creates a formated string using a dictionary containing a latitude and longitutde'''
        lat = '{:.2f}'.format(latlong['lat'])
        lng = '{:.2f}'.format(latlong['lng'])
        format_lat = ''
        format_lng = ''
        if lat[0] == '-':
            format_lat = lat[1:] + 'S'
        else:
            format_lat = lat + 'N'
        if lng[0] == '-':
            format_lng = lng[1:] + 'W'
        else:
            format_lng = lng + 'E'
        return '{} {}'.format(format_lat, format_lng)

    def get_latlongs(json_dict: dict) -> dict:
        '''returns a dictionary with latlongs from a json dictionary'''
        latlongs = list()
        for location in json_dict['route']['locations']:
            latlongs.append(location['latLng'])
        return latlongs
    
    def output(json_dict: dict) -> None:
        '''Prints a formatted version of the latitudes and longitudes of a json dictionary for a trip'''
        print('LATLONGS')
        latlongs = latlong.get_latlongs(json_dict)
        for latlong_obj in latlongs:
            print(latlong._format_latlong(latlong_obj))
            

class elevation():
    def _create_elevation_json(json_dict: dict) -> dict:
        '''returns a json dictionary containing the infromation from MapQuest Elevation using a MapQuest Route json dictionary'''
        elevation_url = api_handling.create_elevation_url(latlong.get_latlongs(json_dict))
        elevation_json = api_handling.parse_url(elevation_url)
        return elevation_json

    def output(json_dict: dict) -> None:
        '''Prints a formatted version of the elevations of a json dictionary for a trip'''
        elevation_json_dict = elevation._create_elevation_json(json_dict)
        print('ELEVATIONS')
        for profile in elevation_json_dict['elevationProfile']:
            print(round(profile['height']))
