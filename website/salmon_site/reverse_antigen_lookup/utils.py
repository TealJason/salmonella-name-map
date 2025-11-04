# Create your views here.
import sys
import json
import argparse 
import os 

def get_antigens_for_serovar(antigenic_formula):  

    coordinate_path = os.path.join(os.path.dirname(__file__), "data", "serovar_name_antigen.json")
    o_antigen,h_antigen_p1,h_antigen_p2 = antigenic_formula.strip().split(":")

    try:
        with open(coordinate_path, "r") as f:
            serovar_antigen_dict = json.load(f)
    except IOError:
        raise FileNotFoundError("Couldn't open the name-to-antigen JSON.")

    for serovar, anitgens in serovar_antigen_dict.items():
        if anitgens["O-Antigen"] == o_antigen and anitgens["H-AntigenP1"] == h_antigen_p1 and anitgens["H-AntigenP2"]:
            serovar_name = serovar
    
    result_dict = {
        "o_antigen":o_antigen,
        "h_AntigenPhase1":h_antigen_p1,
        "h_AntigenPhase2":h_antigen_p2,
        "serovar_name":serovar_name,
        "antigenic_formula":antigenic_formula
    }

    return result_dict
