"""
{
    "Aarhus": [
        "56.1496278",
        "10.2134046"
    ],
    "Aba": [
        "31.9015694",
        "102.2229237"
    ]
}

I need to turn an above styled JSON into a GeoJSON with a format similar to this:

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "Serovar": "Arhus",
        "Antigenic Formula": "N,I:2:-"
      },
      "geometry": {
        "coordinates": [
          26.74783230319494,
          23.799085478387596
        ],
        "type": "Point"
      },
      "id": 0
    },
    {
      "type": "Feature",
      "properties": {
        "Serovar": "juba",
        "Antigenic Formula": "A:2,4,5:zn"
      },
      "geometry": {
        "coordinates": [
          31.646284508517425,
          4.892425703828778
        ],
        "type": "Point"
      },
      "id": 1
    }
  ]
  
}

"""
"""
{
    "Aarhus": [
        "56.1496278",
        "10.2134046"
    ],
    "Aba": [
        "31.9015694",
        "102.2229237"
    ]
}

I need to turn an above styled JSON into a GeoJSON with a format similar to this:

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "Serovar": "Arhus",
        "Antigenic Formula": "N,I:2:-"
      },
      "geometry": {
        "coordinates": [
          26.74783230319494,
          23.799085478387596
        ],
        "type": "Point"
      },
      "id": 0
    },
    {
      "type": "Feature",
      "properties": {
        "Serovar": "juba",
        "Antigenic Formula": "A:2,4,5:zn"
      },
      "geometry": {
        "coordinates": [31.646284508517425,4.892425703828778],
        "type": "Point"
      },
      "id": 1
    }
  ]
  
}

"""
import json

json_file = "serovar_name_to_coordinates.json"
antigen_file = "serovar_name_antigen.json"

coordinate_dict = json.load(open(json_file))
antigen_dict = json.load(open(antigen_file))
geo_json_file = "/mnt/j/dev/python-root/salmonella-name-map/salmon_site/salmon_explorer/data/serovar_coordinates.geojson"

for key in coordinate_dict:
    country = coordinate_dict[key]
    coodinates = coordinate_dict[key]
    
    with open(geo_json_file, "w") as geojson_f:
        geojson_f.write('{\n')
        geojson_f.write('  "type": "FeatureCollection",\n')
        geojson_f.write('  "features": [\n')
        
        for idx, (serovar, coords) in enumerate(coordinate_dict.items()):
            lat = coords[0]
            lon = coords[1]
            
            antigenic_formula = '["' + antigen_dict[serovar]["O-Antigen"] + ":" + antigen_dict[serovar]["H-AntigenP1"] + ":" + antigen_dict[serovar]["H-AntigenP2"] + '"]'

            geojson_f.write('{\n')
            geojson_f.write('"type": "Feature",\n')
            geojson_f.write('"properties": {\n')
            geojson_f.write(f'"Serovar": "{serovar}",\n')
            geojson_f.write(f'"Antigenic Formula": {antigenic_formula}\n')
            geojson_f.write('},\n')
            geojson_f.write('"geometry": {\n')
            geojson_f.write('"coordinates": \n')
            geojson_f.write(f'[{lon},{lat}],\n')
            geojson_f.write('"type": "Point"\n},\n')
            geojson_f.write(f'"id": {idx}\n')
            geojson_f.write('},\n')

        
        geojson_f.write(']\n')
        geojson_f.write('}\n')
        geojson_f.close()