#<a href="https://bhuntr.com/tw/competitions/49613611210209102w">Big data competition</a> held by Taiwan Post office


***********************
- File Name: weight(OtoD).ipynb

- Objective: attain the loading weight of every postoffice

- Tools: python(numpy, pandas), SQL

- Input: origin office number, central office number, and weights per page from database

- Output(weight.csv): the loading weight of every postoffice and their central postoffice.


***********************
- File Name: loadings_of_postoffices.ipynb

- Objective: It is aims to visualize the loading of each postoffice in Taiwan and the relations between center postoffices and regional postoffices.

- Tools: python(numpy, pandas, folium), SQL

- Input: 
	- from database: office number, office name , office name in system, latitude, longitude
	- the result(weight.csv) of file "weight(OtoD).ipynb": the loading weight of every postoffice and their central postoffice.

- Output: A map with the loading of each postoffice in Taiwan and the relations between center postoffices and regional postoffices.

***********************
- File Name: distance.ipynb

- Objective: get the distance and traveling time between two points

- Tools: python(pandas, googlemaps)

- Input: origin_latitude, origin_longitude, destination_latitude, destination_longitude

- Output: distance and duration between two points

***********************
- File Name: GPS_AQX-7810.ipynb

- Objective: access the route of a post car in one day and see which postoffices has it passed

- Tools: python(numpy, pandas, folium, webbrowser), SQL

- Input: AQX-7810's GPS data on 2018-01-03 which includes latitude, longitude, time, status

- Output(AQX-7810(2018-01-03).html): the route of the post car (AQX-7810) in Tainan on 2018-01-03 and its stop points and the offices along the way

***********************













