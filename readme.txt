Flåm Railway Wear Analysis Repository
This repository contains the code, data, and visualizations used in my thesis on rail wear analysis for the Flåm Railway. While the repository structure is not fully organized due to time constraints, this document provides an overview of the contents and instructions for usage.

Repository Structure
1. Data
datasheets_cleaned/: Contains cleaned data files used in the analysis.
Flåm – Roger1000_data.xlsx: Original data file containing measurements collected using the Roger1000 system.
coordinates_km.csv and coordinates_km_interpolated.csv: Coordinate data files used for mapping and interpolation.
map_data.csv: Mapping data for route visualization.
openstreetmap.xml: XML data for route mapping.
2. Illustrasjoner (Illustrations)
Contains various PNG images used in the thesis for visualizing wear patterns, curvature, and relationships.
Examples:
Curvature.png
RelationshipTurnWear.png
wearrate2021.png
3. Koordinater (Coordinates)
flam_railway_route.html: Interactive map showing the Flåm railway route.
myrdal_flom_route_5m_intervals_with_km.csv: Detailed route data segmented at 5-meter intervals.
myrdal-flom.geojson: GeoJSON file for geographic visualizations.
railway_segments_with_wear.csv: Data linking wear patterns to specific railway segments.
4. Code Files
curvy.ipynb: Notebook for curvature calculation and classification.
dataanalyse.ipynb: Main analysis notebook for wear trends and patterns.
segments.ipynb: Handles segmentation of the railway route for analysis.
wear_rate_plots.ipynb: Generates wear rate visualizations.
Roger1000.py: Python script for processing Roger1000 data.


Known Issues
The current structure is not fully organized. Files with similar purposes (e.g., illustrations, data, and scripts) are spread across folders.
Please refer to this README to navigate the repository effectively.
Contact
For questions or clarifications, please contact me at samisa@stud.ntnu.no.