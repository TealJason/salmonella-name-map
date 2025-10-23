import json

data_path = "./serovar_dirty.tsv"
cleaned_data_path = "./full_name_to_serovar.json"

serovar_dictionary = {}

with open(data_path, 'r') as dirty_serovar_data:
    for line_number, line in enumerate(dirty_serovar_data, start=1):
        print(line)
        parts = line.strip().split(":")
        name=parts[0].lower()
        hantigen=parts[1]
        o_antigenp1=parts[2]
        o_antigenp2=parts[3]
        
        serovar_dictionary[name] = {"H-Antigen":hantigen,"O-AntigenP1":o_antigenp1,"O-AntigenP2":o_antigenp2}

with open(cleaned_data_path, 'w') as cleaned_file:
    json.dump(serovar_dictionary, cleaned_file, indent=4)

print(f"Cleaned data written to: {cleaned_data_path}")
print(f"Total valid entries: {len(serovar_dictionary)}")
