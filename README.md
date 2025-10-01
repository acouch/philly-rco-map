# Philly RCO Map
This was created to make it easier to find your local RCO. The city publishes a <a href="https://openmaps.phila.gov/">map of RCOs</a>, however it is not as colorful! 

This map was built with a GeoJSON file <a href="https://opendataphilly.org/datasets/registered-community-organizations-rco-boundaries/">shared on OpenDataPhilly.org</a>, and adds additional information like <a href="https://github.com/acouch/philly-rco-map/blob/main/data-updates.csv">website and mission</a>. The project is <a href="https://github.com/acouch/philly-rco-map">hosted on github</a>.

## Data Updates

To add data to the map:

1. Install geojson-precision: `npm i -g geojson-precision`
2. Download latest city geosjon file from: https://opendataphilly.org/datasets/registered-community-organizations-rco-boundaries/ as `Zoning_RCO.geojson`
3. run `geojson-precision -p 6 Zoning_RCO.geojson Zoning_RCO-6p.geojson` to reduce number of digits used for geojson which reduces files size by approximately half.
4. Make any changes needed to `data-updates.csv`
5. Run `python data-update.py` to update the `data.geojson` file that drives the site. If there are any missing orgs in `data-updates.csv`, they will be printed. Add them to `data-updates.csv` and re-run until no messages appear. 

This is designed to support future updates of the City's GeoJSON file, hosted: https://opendataphilly.org/datasets/registered-community-organizations-rco-boundaries/ .

### Dictionary

The data for the map is stored in the `data.geojson` file. The map information is stored in the `geometry` attribute. The `properties` attribute contains the following data:

<details>
  <summary>Data origin</summary>

| Item | Origin |
|----|----|
|OBJECTID| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|ORGANIZATION_NAME| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|ORGANIZATION_ADDRESS| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|MEETING_LOCATION_ADDRESS| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|PREFFERED_CONTACT_METHOD|[opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|PRIMARY_NAME| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|PRIMARY_ADDRESS| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|PRIMARY_EMAIL| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|PRIMARY_PHONE| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|P_PHONE_EXT| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|ALTERNATE_NAME| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|ALTERNATE_ADDRESS| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|ALTERNATE_EMAIL| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|ALTERNATE_PHONE| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|A_PHONE_EXT| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|EXPIRATIONYEAR| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|EFFECTIVE_DATE| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|LNI_ID| [opendataphilly.org](https://opendata.arcgis.com/datasets/efbff0359c3e43f190e8c35ce9fa71d6_0.geojson) |
|ORG_TYPE_LABEL | `data-updates.csv` |
|ORG_WEBSITE| `data-updates.csv` |
|ORG_MISSION| `data-updates.csv` |
|ORG_LOGO| `data-updates.csv` |
</details>

## Misc

Ten smallest RCOs, by size:

1. Cedar Point Park Neighborhood Association (22,644 sq. meters)
1. Price-Knox Neighbors Assn. (50,782)
1. Woodland Terrace HomeOwners Association (56,1924 sq. meters)
1. Allegheny Empowerment Civic Association (60,4134 sq. meters)
1. Concerned Neighbors for Change (84,7364 sq. meters)
1. Residents Organized for Advocacy and Direction (164,5124 sq. meters)
1. Hunting Park Connected (177,9764 sq. meters)
1. Viola Street Residents Association (188,4884 sq. meters)
1. West Chelten Neighbors Association (189,0164 sq. meters)
1. Holly Street Neighbors CDC (204,5094 sq. meters)

Ten largest RCOs, by size:

1. Eastwick United CDC	(32,287,698 sq. meters)
1. Northeast Community Civic Alliance	(26,583,063 sq. meters)
1. Eastwick Community Network	(26,036,719 sq. meters)
1. Friends of the Wissahickon	(24,585,110 sq. meters)
1. Somerton Civic Association	(13,495,643 sq. meters)
1. Paschall Betterment League, Inc	(13,098,208 sq. meters)
1. Greater Bustleton Civic League	(12,062,496 sq. meters)
1. North East Quality of Life Coalition	(11,369,140 sq. meters)
1. Upper Roxborough Civic Association	(10,32,4503 sq. meters) 
1. Veterans Stadium Neighbors Civic Association	(9,820,788 sq. meters)
