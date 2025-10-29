# Create your views here.
import os
import json
from geopy import distance
from geopy.geocoders import Nominatim
import sys

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


def get_closest_serovar(input_coordinate, coordinate_map, verbose_mode=False):
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
        
        if verbose_mode is True:
            print(f"Comparing to {name}: {dist:.2f} km")

        if dist < closest_distance:
            closest_distance = dist
            closest_name = name
            closest_coordinates = coordinate_tuple

    return closest_name, closest_distance, closest_coordinates


def get_antigens_for_serovar(closest_name):
    """Return antigen info for a given serovar name."""

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
        filtered_dict.get("H-Antigen"),
        filtered_dict.get("O-AntigenP1"),
        filtered_dict.get("O-AntigenP2"),
    )


def run_lookup_logic(lat, long, place_name, verbose=False):
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
            return {"error": f"Could not find location for '{place_name}'"}
    else:
        return {"error": "You must provide either coordinates or a place name."}

    # Find the closest serovar
    closest_name, closest_distance, closest_coordinates = get_closest_serovar(input_coordinate, coordinate_path, verbose)

    if not closest_name:
        return {"error": "No serovar data available."}

    # Get antigenic info
    h_antigen, o_antigen_p1, o_antigen_p2 = get_antigens_for_serovar(closest_name)

    # Return results as structured JSON
    return {
        "input_coordinates": input_coordinate,
        "closest_serovar": closest_name,
        "distance_km": round(closest_distance, 2),
        "match_coordinates": closest_coordinates,
        "antigens": {
            "H": h_antigen,
            "O1": o_antigen_p1,
            "O2": o_antigen_p2,
        },
    }
