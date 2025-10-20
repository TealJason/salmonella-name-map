import pycountry
import geonamescache
import json

# Initialize GeoNamesCache
gc = geonamescache.GeonamesCache()

# Build lookup sets for fast matching
country_names = {country['name'].lower() for country in gc.get_countries().values()}
country_names.update({country.name.lower() for country in pycountry.countries})

#  input list
json_path="/home/phe.gov.uk/jason.beard/Desktop/projects/salmon_map/cleaned_data.json"

with open (json_path) as json_file:
    serovar_dictionary = json.load(json_file)

def search_for_locations(serovar_dictionary):
    classified = {}
    cities = 0
    countries = 0
    noncations = 0
    
    for name in serovar_dictionary.keys():
        lower_name = name.lower().strip()
        if lower_name in country_names:
            classification = "Country"
            countries+=1
        elif gc.search_cities(lower_name):
            classification = "City"
            cities+=1
        else:
            classification = "Not a location"
            noncations+=1
            
    classified[name] = classification
    print(f"there were {cities} cities {countries} countires and {noncations} unsorted locations")

search_for_locations(serovar_dictionary)