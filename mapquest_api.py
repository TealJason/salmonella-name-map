import subprocess

def make_mapbox_image(coordinate):
    
    with open ("./.api_map_box.key", 'r') as f:
        line = f.readline().strip()
        token = line

    lat, long = coordinate
    subprocess.run(f"curl -g 'https://api.mapbox.com/styles/v1/mapbox/streets-v12/static/{long},{lat},10,0,0/600x600?access_token={token}' --output mapbox-static-1.png", shell=True)