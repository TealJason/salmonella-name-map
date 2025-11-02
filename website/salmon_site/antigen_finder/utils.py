# Create your views here.
import sys
import json
import argparse 
import os 

def get_antigens_for_serovar(name):  

    coordinate_path = os.path.join(os.path.dirname(__file__), "data", "serovar_name_antigen.json")
    
    
    search_name = name.capitalize()

    try:
        with open(coordinate_path, "r") as f:
            serovar_antigen_dict = json.load(f)
    except IOError:
        raise FileNotFoundError("Couldn't open the name-to-antigen JSON.")

    if search_name not in serovar_antigen_dict:
        print(f"Serovar '{name}' not found in the JSON file.")
        empty = {}
        return empty 

    try:
        filtered_dict = serovar_antigen_dict[search_name]
    except:
        print("Debug unable to find serovar in the json file")
   
    
    o_antigen = filtered_dict.get("O-Antigen", "unknown")
    h_antigen_p1 = filtered_dict.get("H-AntigenP1", "unknown")
    h_antigen_p2 = filtered_dict.get("H-AntigenP2", "unknown")   
    
    full_formula = f"{o_antigen}:{h_antigen_p1}:{h_antigen_p2}"

    result_dict = {
        "o_antigen":o_antigen,
        "h_AntigenPhase1":h_antigen_p1,
        "h_AntigenPhase2":h_antigen_p2,
        "serovar_name":name,
        "antigenic_formula":full_formula
    }

    return result_dict
