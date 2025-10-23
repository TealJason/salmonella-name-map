import sys
import json
import argparse 

def argument_passing():
    parser = argparse.ArgumentParser(description="Get antigenic formula for a serovar.")
    
    parser.add_argument(
        "--name",
        "-n",
        required=True, 
        help="Name of the serovar"
    )
    
    args = parser.parse_args()
    return args

def get_antigens_for_serovar(closest_name):
    try:
        with open("./get_distance/serovar_name_antigen.json", "r") as f:
            serovar_antigen_dict = json.load(f)
    except IOError:
        print("Couldn't open the name:antigen JSON file.")
        sys.exit(1)
    
    if closest_name not in serovar_antigen_dict:
        print(f"Serovar '{closest_name}' not found in the JSON file.")
        sys.exit(1)

    filtered_dict = serovar_antigen_dict[closest_name]

    h_antigen = filtered_dict.get("H-Antigen", "unknown")
    o_antigen_p1 = filtered_dict.get("O-AntigenP1", "unknown")
    o_antigen_p2 = filtered_dict.get("O-AntigenP2", "unknown")   
    
    print(f"The antigenic formula is {h_antigen}:{o_antigen_p1}:{o_antigen_p2}")

def main():
    args = argument_passing()
    get_antigens_for_serovar(args.name)

if __name__ == "__main__":
    main()
