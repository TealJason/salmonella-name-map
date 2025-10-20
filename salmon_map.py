import json
from geopy import distance
import argparse
from geopy.geocoders import Nominatim
import sys

def argument_passing():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--place_name"
    )

    parser.add_argument(
        "--lat"
    )
    
    parser.add_argument(
        "--long"
    )

    args = parser.parse_args()

    if args.place_name is None and (args.lat is None or args.long is None):
            print("You must either give both latitude and longitude (--lat & --long) or a place name (--place_name).")
            sys.exit(1)

    return args

def compare_distances(comparison_coordinate, input_coordinate):
    dist = distance.distance(comparison_coordinate, input_coordinate).km # This package assumes that altitude is equal
    return dist

def lookup_name(geolocator, search_name):

    print("Making api call to get coordiantes for the given place name")
    try:
        location = geolocator.geocode(search_name, timeout=10)
    except:
        print(f"couldn't find {search_name}")
        exit 

    coordinate = (location.latitude, location.longitude)

    return location

def get_closest_serovar(input_coordinate):
    coordinate_map="./name_to_coordinates.json"
    with open(coordinate_map, "r") as f:
        serovar_dict = json.load(f)
        
    closest_distance = float("inf")
    closest_name = None

    for name, coordinate_tuple in serovar_dict.items():
        dist = compare_distances(coordinate_tuple, input_coordinate)
        
        print(f"Comparing to {name}: {dist:.2f} km")
        if dist < closest_distance:
            closest_distance = dist
            closest_name = name
            cloest_coordinates = coordinate_tuple

    return closest_name, closest_distance, cloest_coordinates

def main():
    geolocator = Nominatim(user_agent="geo_classifier")

    args = argument_passing()

    if args.place_name is not None: coordinate = lookup_name(geolocator, args.place_name)
    else: coordinate = (args.lat, args.long)

    print(f"Continuing with the coordinates: {coordinate}")

    closest_name, closest_distance,cloest_coordinates = get_closest_serovar(coordinate)
    print(f"\nClosest location: {closest_name} ({closest_distance:.2f} km away)")
    print(f"Coordinates for this match are {cloest_coordinates}")

if __name__ == "__main__":
    main()
