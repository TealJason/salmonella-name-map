from geopy.geocoders import Nominatim
import time
import json
import os

# Initialize geolocator
geolocator = Nominatim(user_agent="geo_classifier")

# Input JSON file
json_path = "./cleaned_data.json"

with open(json_path) as json_file:
    serovar_dictionary = json.load(json_file)


def write_to_file(name_list, sort_type):
    """Writes results to a file, creating directories if needed."""
    path = f"./{sort_type}.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w") as f:
        for item in name_list:
            # Write tuples or strings cleanly
            if isinstance(item, tuple):
                name, lat, lon = item
                f.write(f"{name}\t{lat}\t{lon}\n")
            else:
                f.write(f"{item}\n")


def search_for_locations(serovar_dictionary):
    locations = 0
    noncations = 0
    location_list = []
    nonlocation_list = []
    
    for i, name in enumerate(serovar_dictionary.keys(), start=1):
        try:
            location = geolocator.geocode(name, timeout=10)
            if location:
                locations += 1
                location_list.append((name, location.latitude, location.longitude))
                print(f"[{i}] {name}: found ({location.latitude}, {location.longitude})")
            else:
                noncations += 1
                nonlocation_list.append(name)
                print(f"[{i}] {name}: not found")
            time.sleep(1)
        
        except Exception as e:
            print(f"Error for {name}: {e}")
            nonlocation_list.append(name)
            continue

    # Write results to files
    write_to_file(location_list, "sorted")
    write_to_file(nonlocation_list, "unsorted")

    print(f"{locations} locations found")
    print(f"{noncations} not found")
    print("Results saved to 'sorted.txt' and 'unsorted.txt'")


# Run the search
search_for_locations(serovar_dictionary)
