# Philly RCO Map
This was created to make it easier to find your local RCO. The city publishes a <a href="https://openmaps.phila.gov/">map of RCOs</a>, however it is not as colorful! 

This map was built with a GeoJSON file <a href="https://opendataphilly.org/datasets/registered-community-organizations-rco-boundaries/">shared on OpenDataPhilly.org</a>, and adds additional information like <a href="https://github.com/acouch/philly-rco-map/blob/main/data-updates.csv">website and mission</a>. The project is <a href="https://github.com/acouch/philly-rco-map">hosted on github</a>.

## Data Updates

To add data to the map, update `data-updates.csv` and run `python clean.py`. 

This is designed to support future updates of the City's GeoJSON file, hosted: https://opendataphilly.org/datasets/registered-community-organizations-rco-boundaries/ .