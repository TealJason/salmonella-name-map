# Salmonella-map
A repo for creating a way to find the closet city/place to you where a salmonella serovar/type is named after.

Salmonella servar/serotypes are defined by the O and H antigens they have which results in classifications like "30 i e,n,z15" for the O antigen and phase1 and phase2 H antigens.
To make things easier salmonella stains are traditionally given a shorthand name based on where they were first discovered such as Salmonella Kentucky or Salmonella Middlesbrough.

In this reposoitory I will be adding means to find the closest serovar to you!
At the current time its written in python using the data taken from here for the serovar names -> https://www.researchgate.net/publication/310673247_Antigenic_formulae_of_the_salmonella_servovars_Who_collab
And using geopy to pull data from openstreetmap to match the serovar names to places with coordinates.

Mapbox is currently being used to generate an overhead image of the closest salmonella serovar

I believe there are still some false positives in the data in that the place name coordinate set might not 100% link up to where the serovar was named for.
I think most are correct but some tedious validation still needs to be done

Currently it is very basic you can enter in a set of coordinates or a place names and it will get cloeset salmonella location to you.
In the furture I would like to get to a point where you can simply click on a map click find and it will show you on the map where the cloeset salmonella location is.

## Example usages
Look for the cloest servoar to the city Baden-Baden  
```python3 salmon_map.py --place_name Baden-Baden``` 

Look for the closet servoar to a set of input coordinates and enable a verbose printout to the console for the distance to all salmonella serovars  
```python3 salmon_map.py --lat 30.213 --long -2.5 -v```

Look for the cloest serovar to monaco and generate a static image of the cloest city (requires api key)  
```python3 salmon_map.py --place_name singapore --get_image```

### All argument
```
--place_name
    text

--lat
    text

--long
    text

--get_image
    text

--verbose, -v
    text

--coordiante
    text

```
