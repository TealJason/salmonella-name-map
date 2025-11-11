import subprocess
import sys

def make_mapbox_image(coordinate):
    try:    
        with open ("./.api_map_box.key", 'r') as f:
            line = f.readline().strip()
            token = line
    except IOError as e:
        print(f"couldn't get the api key {e}")
        print("get a valid key or use coordinates as an input")
        sys.exit(1)
        
    lat, long = coordinate
    subprocess.run(f"curl -g 'https://api.mapbox.com/styles/v1/mapbox/streets-v12/static/{long},{lat},10,0,0/600x600?access_token={token}&attribution=false'  --output serovar-location.png", shell=True)