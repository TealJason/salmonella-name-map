# Create your views here.
import os
import json
from geopy import distance # type: ignore
from geopy.geocoders import Nominatim # type: ignore
import sys
import subprocess
from django.conf import settings # type: ignore
import requests # type: ignore


def make_mapbox_image(coordinate):
    api_key_path = os.path.join(os.path.dirname(__file__), "data", ".api_map_box.key")
    try:
        with open(api_key_path, 'r') as f:
            token = f.readline().strip()
    except IOError as e:
        print(f"Couldn't get the API key: {e}")
        raise

    lat, long = coordinate

    url = f"https://api.mapbox.com/styles/v1/mapbox/streets-v12/static/{long},{lat},10,0,0/600x600?access_token={token}&attribution=false"

    r = requests.get(url)
    r.raise_for_status()

    return r.content

def compare_distances(comparison_coordinate, input_coordinate):
    """Return distance (km) between two coordinate pairs."""
    return distance.distance(comparison_coordinate, input_coordinate).km


def lookup_name(geolocator, search_name):
    """Convert a place name into coordinates using geopy."""
    print("Making API call to get coordinates for the given place name")
    location = geolocator.geocode(search_name, timeout=10)
  
    if location is None:
        print(f"Couldn't find {search_name}")
        return None

    return (location.latitude, location.longitude)


def get_closest_serovar(input_coordinate, coordinate_map):
    """Find the serovar closest to the given coordinate."""
    try:
        with open(coordinate_map, "r") as f:
            serovar_dict = json.load(f)
    except IOError:
        raise FileNotFoundError("Could not find the coordinate JSON file.")     

    closest_distance = float("inf")
    closest_name = None
    closest_coordinates = None

    for name, coordinate_tuple in serovar_dict.items():
        dist = compare_distances(coordinate_tuple, input_coordinate)

        if dist < closest_distance:
            closest_distance = dist
            closest_name = name
            closest_coordinates = coordinate_tuple

    return closest_name, closest_distance, closest_coordinates


def get_antigens_for_serovar(closest_name):
    """Return antigen info for a given serovar name."""
    closest_name = closest_name.capitalize()

    coordinate_path = os.path.join(os.path.dirname(__file__), "data", "serovar_name_antigen.json")
    try:
        with open(coordinate_path, "r") as f:
            serovar_antigen_dict = json.load(f)
    except IOError:
        raise FileNotFoundError("Couldn't open the name-to-antigen JSON.")

    filtered_dict = serovar_antigen_dict.get(closest_name)
    if not filtered_dict:
        return None, None, None
    return (
        filtered_dict.get("O-Antigen"),
        filtered_dict.get("H-AntigenP1"),
        filtered_dict.get("H-AntigenP2"),
    )

def return_empty_dic_for_failures():
    
    empty_dict= {
        "input_coordinates": "Unable to find location",
        "closest_serovar": "-",
        "distance_km": "-",
        "match_coordinates": "-",
        "antigens": {
            "O": "-",
            "H1": "-",
            "H2": "-",
        },} 
    
    mapbox_image =  None
    return empty_dict, mapbox_image 


def run_lookup_logic(lat, long, place_name,get_image, verbose=False):
    """Main logic function — returns dict of results instead of printing."""
    geolocator = Nominatim(user_agent="geo_classifier")

    try:
        coordinate_path = os.path.join(os.path.dirname(__file__), "data", "serovar_name_to_coordinates.json")
    except Exception as e:
        print(f"couldn't find the json file {e}")

    # Determine input coordinate
    if lat is not None and long is not None:
        input_coordinate = (lat, long)
    elif place_name:
        input_coordinate = lookup_name(geolocator, place_name)
        if not input_coordinate:
            empty_dict, dummy_mapbox = return_empty_dic_for_failures()
            print(f"Could not find location for '{place_name}'")
            return empty_dict, dummy_mapbox
    else:
        empty_dict, dummy_mapbox = return_empty_dic_for_failures()
        print(f"You must provide either coordinates or a place name.")
        return empty_dict, dummy_mapbox

    # Find the closest serovar
    closest_name, closest_distance, closest_coordinates = get_closest_serovar(input_coordinate, coordinate_path)

    if not closest_name:
        empty_dict, dummy_mapbox = return_empty_dic_for_failures()
        print("No serovar data available.")
        return empty_dict, dummy_mapbox

    # Get antigenic info
    o_antigen, h_antigen_p1, h_antigen_p2 = get_antigens_for_serovar(closest_name)

    if get_image:
        mapbox_image = make_mapbox_image(closest_coordinates)
    else:
        mapbox_image = None
        
    # Return results 
    return {
        "input_coordinates": input_coordinate,
        "closest_serovar": closest_name,
        "distance_km": round(closest_distance, 2),
        "match_coordinates": closest_coordinates,
        "antigens": {
            "O": o_antigen,
            "H1": h_antigen_p1,
            "H2": h_antigen_p2,
        },
    }, mapbox_image
