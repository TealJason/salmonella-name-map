import json

data_path = "/home/phe.gov.uk/jason.beard/Desktop/projects/salmon_map/found_places.tsv"
cleaned_data_path = "/home/phe.gov.uk/jason.beard/Desktop/projects/salmon_map/name_to_coordinates.json"

serovar_dictionary = {}

with open(data_path, 'r') as dirty_serovar_data:
    for line_number, line in enumerate(dirty_serovar_data, start=1):
        parts = line.strip().split("\t")
        
        # Skip empty or malformed lines
        if len(parts) < 3:
            print(f"Skipping malformed line {line_number}: {parts}")
            continue

        name, lat, long = parts
        serovar_dictionary[name] = (lat,long)

with open(cleaned_data_path, 'w') as cleaned_file:
    json.dump(serovar_dictionary, cleaned_file, indent=4)

print(f"Cleaned data written to: {cleaned_data_path}")
print(f"Total valid entries: {len(serovar_dictionary)}")