# Salmonella-map
A repo for creating a way to find the closet city/place to you where a salmonella serovar/type is named after.

Salmonella servar/serotypes are defined by the O and H antigens they have which results in classifications like "30 i e,n,z15" for the O antigen and phase1 and phase2 H antigens.
To make things easier salmonella stains are traditionally given a shorthand name based on where they were first discovered such as Salmonella Kentucky or Salmonella Middlesbrough.

In this reposoitory I will be adding means to find the closest serovar to you!
At the current time its written in python using the data taken from here for the serovar names -> https://www.researchgate.net/publication/310673247_Antigenic_formulae_of_the_salmonella_servovars_Who_collab
And using geopy to pull data from openstreetmap to match the serovar names to places with coordinates.

Currently it is VERY basic you can enter in a set of coordinates and it will get cloeset salmonella location to you
In the furture I will go about having it showing you on the map where the cloeset salmonella location is.
