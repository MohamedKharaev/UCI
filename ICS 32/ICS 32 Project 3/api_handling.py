# Mohamed Kharaev 43121144 Lab Sec 13
import urllib.request
import urllib.parse
import json

key = 'fGDWSglF2bOXhzNjdKLq0SEocLgKeSMe'

base_url = 'http://open.mapquestapi.com/'

def create_destination_url(locations: [str]) -> str:
    '''Creates a url for mapquests route api using the given locations'''
    destination_url = base_url + 'directions/v2/route?'
    url_parameters = [
        ('key', key),
        ('from', locations[0])]
    for destination in locations[1:]:
        url_parameters.append(('to', destination))
    result_url = destination_url + urllib.parse.urlencode(url_parameters)
    return result_url


def parse_url(url: str) -> str:
    '''parses a url's text and returns a json dictionary'''
    response = urllib.request.urlopen(url)
    json_text = response.read().decode(encoding = 'utf-8')
    response.close()
    return json.loads(json_text)


def create_elevation_url(latLngs: dict) -> str:
    '''Creates a url for mapquests elevation api using the given latitudes and longitudes dictionary'''
    base_elevation_url = base_url + 'elevation/v1/profile?'
    latLng_string = ""
    for latLng in latLngs:
        latLng_string += str(latLng['lat']) + ','
        latLng_string += str(latLng['lng']) + ','
    latLng_string = latLng_string[:-1]
    url_parameters = [
        ('key', key),
        ('latLngCollection', latLng_string),
        ('unit', 'f')]
    result_url = base_elevation_url + urllib.parse.urlencode(url_parameters)
    return result_url
