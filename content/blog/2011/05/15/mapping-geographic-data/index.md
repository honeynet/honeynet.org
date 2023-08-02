---
title: "Mapping geographic data"
authors: ["Oguz Yarimtepe"]
date: "2011-05-15"
tags: 
  - "django-d68"
  - "geodjango-d96"
  - "python-d32"
---

Visualization is a niche area especially at the security analysis. As mentioned in a well-known sentence; "A picture is worth a thousand words". The importance and the power of the visualization in the security area stands out with the ability to define multi-dimensional data with a single shape. When addressing the creating a mesh tiled 3D view on an Earth map, i was reading about the geoweb application development. A geoweb application consists of some components.  
  

  

Spatial Data

  

  
This is the geographical information. It can be latitude and longitude of a point on a map, or some other metric definition depending on the spatial reference system used.  

  

Rendering

  

  
The geographic points should be rendered to create a meaningful map. There are already some open source solutions like [Mapnik](http://mapnik.org/), [Tilemill](http://tilemill.com/) and [Geoserver](http://geoserver.org). Mapnik and Tilemill are based on Python though Geoserver is written via Java. It is possible to create custom maps with them, read ESRI shape files or [GDAL formats](http://www.gdal.org/). They are compatible with services like Google Earth and Google Maps.  

  

Adding Layers and Tiles

  

  
This is where a layer is defined that has some tiles, aiming to give additional view to the map. Heat map is a sample example for this issue. By using some APIs like [GHeat](http://code.google.com/p/gheat/) or [HeatMapAPI](http://www.heatmapapi.com/), it is possible to add heat mp tiles to the 2D maps.  

  
  

  
  
While i was searching for the ways of handling spatial data, i encountered with the [GeoDjango](http://geodjango.org/) project which a Django add-on that enables using PostgreSQL, creating spatial specific databases and handling them over API. [A sample GIS application](http://invisibleroads.com/tutorials/geodjango-googlemaps-build.html) was presented at 2009 Python conference.  
  
Here is my pros for GeoDjango:  
  

  
- Using the power of Django: Web programming using MTV structure, handling the database queries over the supplied PostgreSQL API  
    
- Creating spatial databases and handling them using postgis API  
    
- Ability to use Google Maps and interacting them via jquery frameworks  
    

  
  
Current sample GIS application required Django 1.2 or over. I tested the code over Kubuntu 11.04. It was easy to find the required dependencies (libgeos-c1 libgeos-3.2.0 libgeos-dev gdal-bin python-gdal libgdal1-dev postgresql postgresql-devel postgresql-server postgresql-devel python-psycopg2 libgeotiff-epsg postgis postgresql-8.4-postgis)  
  
The rest requires creating the required database and tables. Table definitions are written in models.py as class definitions and they are created by typing "python manage.py syncdb" on the fly with the aid of Django DB API. settings.py file include the database connection information, installed application, global environmental variables, template directory information and more. Django comes with a development server so running the development server and checking http://localhost:8000 will give the created map using Google Maps. It can be seen that, it is possible to send objects to the html template files and dynamically create them using a javascript API.  
  
At the 2009 Python Conference, it is represented that the interaction is done via JQeury. Instead of JQuery, i will be using processing.js and trying to create 3D mesh tiles over the Google Map. A 3D mesh is a grid structure that had Z axis defined. With the color change at the tiles and the height, i think more valuable information will be given about the number of malwares and attacks on the geographic locations.
