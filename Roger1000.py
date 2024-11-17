import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point


# File path 
file_path_new = 'Flåm - Roger1000 data.xlsx'

xls = pd.ExcelFile(file_path_new)

# Let's load the data for 2021 06 06 and plot wear data against geographic coordinates
data_2021_06_03 = pd.read_excel(file_path_new, sheet_name='2021 06 03')



''' #Plot 1 - Horizontal wear consumption for RX and LX against geographic coordinates#  '''
# Display the first few rows of the station data
df_stations = pd.read_excel(xls, sheet_name='Stasjon og Koordinater')


# Clean the data and convert coordinates to float


def to_float_safe(value):
    try:
        # Fjern '° N' eller '° E' og konverter til float
        return float(str(value).replace('° N', '').replace('° E', '').strip())
    except ValueError:
        return None  # Returner None hvis konvertering feiler


import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point


# Clean the data by dropping irrelevant or empty rows
data_2021_06_03_clean = data_2021_06_03.dropna(how='all')


# Prepare the data for mapping
# Extract relevant columns: Latitude, Longitude, RX and LX wear
map_data = data_2021_06_03_clean[['Km', 'Latitude', 'Longitude', 'RX_HorizontalWearConsumption', 'LX_HorizontalWearConsumption', 'RX_VerticalWear', 'LX_VerticalWear']]

map_data_clean = map_data.dropna(subset=['Latitude', 'Longitude'])

map_data['Latitude'] = map_data['Latitude'].apply(to_float_safe)
map_data['Longitude'] = map_data['Longitude'].apply(to_float_safe)

# Convert latitude and longitude to numeric values
map_data['Latitude'] = map_data['Latitude'].apply(lambda x: str(x).replace('° N', '')).astype(float)
map_data['Longitude'] = map_data['Longitude'].apply(lambda x: str(x).replace('° E', '')).astype(float)

# Create a geometry column for mapping
geometry = [Point(xy) for xy in zip(map_data['Longitude'], map_data['Latitude'])]
gdf = gpd.GeoDataFrame(map_data, geometry=geometry)

# Plot the data on a map with wear severity
fig, ax = plt.subplots(1, 2, figsize=(15, 8))

# Plot RX og LX (Right/Left) horizontal og vertical wear separat
fig, ax = plt.subplots(2, 2, figsize=(15, 12))

# Horizontal Wear Right (RX)
gdf.plot(column='RX_HorizontalWearConsumption', cmap='coolwarm', legend=True, ax=ax[0, 0])
ax[0, 0].set_title('Horizontal Wear Right (RX)')
ax[0, 0].set_xlabel('Longitude')
ax[0, 0].set_ylabel('Latitude')

# Horizontal Wear Left (LX)
gdf.plot(column='LX_HorizontalWearConsumption', cmap='coolwarm', legend=True, ax=ax[0, 1])
ax[0, 1].set_title('Horizontal Wear Left (LX)')
ax[0, 1].set_xlabel('Longitude')
ax[0, 1].set_ylabel('Latitude')

# Vertical Wear Right (RX)
gdf.plot(column='RX_VerticalWear', cmap='coolwarm', legend=True, ax=ax[1, 0])
ax[1, 0].set_title('Vertical Wear Right (RX)')
ax[1, 0].set_xlabel('Longitude')
ax[1, 0].set_ylabel('Latitude')

# Vertical Wear Left (LX)
gdf.plot(column='LX_VerticalWear', cmap='coolwarm', legend=True, ax=ax[1, 1])
ax[1, 1].set_title('Vertical Wear Left (LX)')
ax[1, 1].set_xlabel('Longitude')
ax[1, 1].set_ylabel('Latitude')

plt.tight_layout()
plt.scatter(df_stations['Longitude'], df_stations['Latitude'], color='red', label='Stations', s=100)
plt.show()

'''Slutt plott1'''


'''Plot 2 - Gjennomsnittlig slitasjeendring for kilometreintervaller#'''

# # Vi ser på dataene fra 3. juni og 9. september 2021
# data_2021_06_03_new = pd.read_excel(file_path_new, sheet_name='2021 06 03')
# data_2021_09_09_new = pd.read_excel(file_path_new, sheet_name='2021 09 09')


# # Remove rows with all missing values, Kan evt prøve å tilnærme manglende verdier senere
# data_2021_06_03_clean_new = data_2021_06_03_new.dropna(how='all')
# data_2021_09_09_clean_new = data_2021_09_09_new.dropna(how='all')
# data_2021_09_09_clean_new.loc[:, 'Km'] = data_2021_09_09_clean_new['Km'] / 10000


# # Velg kolonnene som viser Wear Consumption, men wear consumption i 09 09 arket har feil format, de må deles på 100

# columns_of_interest_corrected = ['Km', 'RX_HorizontalWearConsumption', 'LX_HorizontalWearConsumption', 
#                                   'RX_VerticalWear', 'LX_VerticalWear']
# data_2021_06_03_subset_new = data_2021_06_03_clean_new[columns_of_interest_corrected]

# # # Del på 100 for å få riktig format
# data_2021_09_09_subset_new = data_2021_09_09_clean_new[columns_of_interest_corrected]
# # For the first DataFrame
# data_2021_09_09_subset_new.loc[:, 'RX_HorizontalWearConsumption'] = data_2021_09_09_subset_new['RX_HorizontalWearConsumption'] / 100
# data_2021_09_09_subset_new.loc[:, 'LX_HorizontalWearConsumption'] = data_2021_09_09_subset_new['LX_HorizontalWearConsumption'] / 100
# data_2021_09_09_subset_new.loc[:, 'RX_VerticalWear'] = data_2021_09_09_subset_new['RX_VerticalWear'] / 100
# data_2021_09_09_subset_new.loc[:, 'LX_VerticalWear'] = data_2021_09_09_subset_new['LX_VerticalWear'] / 100

# # For the second DataFrame


# # Ønsker å sammenligne wear på lokasjon mellom 3. juni og 9. september 2021
# comparison_df_corrected_km = pd.merge(data_2021_06_03_subset_new, data_2021_09_09_subset_new, on='Km', suffixes=('_2021_06_03', '_2021_09_09'))


# # Compute the differences in wear between the two dates for each measurement
# comparison_df_corrected_km['RX_Horizontal_change'] = (comparison_df_corrected_km['RX_HorizontalWearConsumption_2021_09_09'] - comparison_df_corrected_km['RX_HorizontalWearConsumption_2021_06_03']).round(2)
# comparison_df_corrected_km['LX_Horizontal_change'] = (comparison_df_corrected_km['LX_HorizontalWearConsumption_2021_09_09'] - comparison_df_corrected_km['LX_HorizontalWearConsumption_2021_06_03']).round(2)
# comparison_df_corrected_km['RX_Vertical_change'] = (comparison_df_corrected_km['RX_VerticalWear_2021_09_09'] - comparison_df_corrected_km['RX_VerticalWear_2021_06_03']).round(2)
# comparison_df_corrected_km['LX_Vertical_change'] = (comparison_df_corrected_km['LX_VerticalWear_2021_09_09'] - comparison_df_corrected_km['LX_VerticalWear_2021_06_03']).round(2)



# #Let's create visualizations for the changes in horizontal and vertical wear between the two dates

# import matplotlib.pyplot as plt


# comparison_df_corrected_km['Km_interval'] = (comparison_df_corrected_km['Km'] // 0.5) * 0.5

# # Beregn gjennomsnittlig slitasjeendring for hvert intervall
# aggregated_data = comparison_df_corrected_km.groupby('Km_interval').mean()

# # Plot for aggregerte data for RX og LX
# plt.figure(figsize=(12, 8))

# # Plot RX horizontal wear changes (aggregert)
# plt.subplot(2, 2, 1)
# plt.plot(aggregated_data.index, aggregated_data['RX_Horizontal_change'], marker='o')
# plt.title('Aggregert RX Horisontal slitasjeendring')
# plt.xlabel('Km (Aggregert)')
# plt.ylabel('Gjennomsnittlig slitasjeendring')

# # Plot LX horizontal wear changes (aggregert)
# plt.subplot(2, 2, 2)
# plt.plot(aggregated_data.index, aggregated_data['LX_Horizontal_change'], marker='o')
# plt.title('Aggregert LX Horisontal slitasjeendring')
# plt.xlabel('Km (Aggregert)')
# plt.ylabel('Gjennomsnittlig slitasjeendring')

# # Plot RX vertical wear changes (aggregert)
# plt.subplot(2, 2, 3)
# plt.plot(aggregated_data.index, aggregated_data['RX_Vertical_change'], marker='o')
# plt.title('Aggregert RX Vertikal slitasjeendring')
# plt.xlabel('Km (Aggregert)')
# plt.ylabel('Gjennomsnittlig slitasjeendring')

# # Plot LX vertical wear changes (aggregert)
# plt.subplot(2, 2, 4)
# plt.plot(aggregated_data.index, aggregated_data['LX_Vertical_change'], marker='o')
# plt.title('Aggregert LX Vertikal slitasjeendring')
# plt.xlabel('Km (Aggregert)')
# plt.ylabel('Gjennomsnittlig slitasjeendring')

# plt.tight_layout()
# plt.show()
'''SLUTT PLOTT 2'''


# plt.figure(figsize=(12, 6))

# # Plot horizontal wear changes for RX and LX
# plt.subplot(1, 2, 1)
# plt.plot(comparison_df_corrected_km['Km'], comparison_df_corrected_km['RX_Horizontal_change'], marker='o', label='RX Horizontal Wear Change')
# plt.plot(comparison_df_corrected_km['Km'], comparison_df_corrected_km['LX_Horizontal_change'], marker='o', linestyle='--', label='LX Horizontal Wear Change')
# plt.title('Horizontal Wear Changes (June to September 2021)')
# plt.xlabel('Km')
# plt.ylabel('Wear Change')
# plt.legend()

# # Plot vertical wear changes for RX and LX
# plt.subplot(1, 2, 2)
# plt.plot(comparison_df_corrected_km['Km'], comparison_df_corrected_km['RX_Vertical_change'], marker='x', label='RX Vertical Wear Change')
# plt.plot(comparison_df_corrected_km['Km'], comparison_df_corrected_km['LX_Vertical_change'], marker='x', linestyle='--', label='LX Vertical Wear Change')
# plt.title('Vertical Wear Changes (June to September 2021)')
# plt.xlabel('Km')
# plt.ylabel('Wear Change')
# plt.legend()

# # Adjust layout to avoid overlapping
# plt.tight_layout()

# # Display the plot
# plt.show()


