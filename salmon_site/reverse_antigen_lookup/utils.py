# Create your views here.
import sys
import json
import argparse 
import os 

def get_antigens_for_serovar(antigenic_formula):  
    print(f"recieved formula {antigenic_formula}")
    parts = antigenic_formula.strip().split(":")
    if parts.__len__() == 3:
        coordinate_path = os.path.join(os.path.dirname(__file__), "data", "serovar_name_antigen.json")
        o_antigen,h_antigen_p1,h_antigen_p2 = antigenic_formula.strip().split(":")

        print(f"split formula in to parts  {o_antigen} : {h_antigen_p1} : {h_antigen_p2}")
        
        try:
            with open(coordinate_path, "r") as f:
                serovar_antigen_dict = json.load(f)
        except IOError:
            raise FileNotFoundError("Couldn't open the name-to-antigen JSON.")

        for serovar, antigens in serovar_antigen_dict.items():
            if antigens["O-Antigen"] == o_antigen and antigens["H-AntigenP1"] == h_antigen_p1 and antigens["H-AntigenP2"] == h_antigen_p2:
                serovar_name = serovar
                break # stop loop on match
            else:
                serovar_name = None
    else:
        serovar_name = None
                   
    if serovar_name is not None:
        result_dict = {
            "o_antigen":o_antigen,
            "h_AntigenPhase1":h_antigen_p1,
            "h_AntigenPhase2":h_antigen_p2,
            "serovar_name":serovar_name,
            "antigenic_formula":antigenic_formula
        }
        
    else:
        result_dict = {
            "o_antigen":"Unable to find match in database",
            "h_AntigenPhase1":"Unable to find match in database",
            "h_AntigenPhase2":"Unable to find match in database",
            "serovar_name":"Unable to find match in database",
            "antigenic_formula":antigenic_formula
        }
    return result_dict
