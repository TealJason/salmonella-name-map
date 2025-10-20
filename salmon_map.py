import json
from geopy import distance

def get_user_input():
    print("Please enter latitude in degrees Eorth:")
    lat = float(input())
    print("Please enter longitude in degrees East:")
    lon = float(input())
    return lat, lon


def compare_distances(comparison_coordinate, input_coordinate):
    dist = distance.distance(comparison_coordinate, input_coordinate).km # This package assumes that altitude is equal
    return dist

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
    lat, lon = get_user_input()
    coordinate = (lat, lon)
    print(f"Input coordinates: {coordinate}")

    closest_name, closest_distance,cloest_coordinates = get_closest_serovar(coordinate)
    print(f"\nClosest location: {closest_name} ({closest_distance:.2f} km away)")
    print(f"Coordinates for this match are {cloest_coordinates}")

if __name__ == "__main__":
    main()
