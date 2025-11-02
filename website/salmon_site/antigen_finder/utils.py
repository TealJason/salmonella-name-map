# Create your views here.
import sys
import json
import argparse 
import os 

def get_antigens_for_serovar(name):  

    coordinate_path = os.path.join(os.path.dirname(__file__), "data", "serovar_name_antigen.json")
    
    name = name.capitalize()

    try:
        with open(coordinate_path, "r") as f:
            serovar_antigen_dict = json.load(f)
    except IOError:
        raise FileNotFoundError("Couldn't open the name-to-antigen JSON.")

    if name not in serovar_antigen_dict:
        print(f"Serovar '{name}' not found in the JSON file.")
        empty = {}
        return empty 

    try:
        filtered_dict = serovar_antigen_dict[name]
    except:
        print("Debug unable to find serovar in the json file")
   
    
    h_antigen = filtered_dict.get("H-Antigen", "unknown")
    o_antigen_p1 = filtered_dict.get("O-AntigenP1", "unknown")
    o_antigen_p2 = filtered_dict.get("O-AntigenP2", "unknown")   
    
    full_formula = f"{h_antigen}:{o_antigen_p1}:{o_antigen_p2}"

    result_dict = {
        "h_antigen":h_antigen,
        "o_AntigenPhase1":o_antigen_p1,
        "o_AntigenPhase2":o_antigen_p2,
        "serovar_name":name,
        "antigenic_formula":full_formula
    }

    return result_dict
