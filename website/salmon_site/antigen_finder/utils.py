# Create your views here.
import sys
import json
import argparse 

def get_antigens_for_serovar(name):  
    try:
        with open("/home/phe.gov.uk/jason.beard/Desktop/projects/salmon_map/project/salmonella-name-map/website/salmon_site/antigen_finder/data/serovar_name_antigen.json", "r") as f:
            serovar_antigen_dict = json.load(f)
    except IOError:
        print("Couldn't open the JSON file.")
        sys.exit(1)
    
    if name not in serovar_antigen_dict:
        print(f"Serovar '{name}' not found in the JSON file.")
        sys.exit(1)

    filtered_dict = serovar_antigen_dict[name]

    h_antigen = filtered_dict.get("H-Antigen", "unknown")
    o_antigen_p1 = filtered_dict.get("O-AntigenP1", "unknown")
    o_antigen_p2 = filtered_dict.get("O-AntigenP2", "unknown")   
    
    return name, h_antigen, o_antigen_p1, o_antigen_p2
