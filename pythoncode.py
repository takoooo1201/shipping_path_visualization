import pandas as pd

# Load the provided CSV file
monthly_weights_path = 'Monthly_Port_Weights_with_Complete_Ports.csv'
monthly_weights_df = pd.read_csv(monthly_weights_path)

# Display the first few rows to inspect the data
monthly_weights_df.head()

# Load the provided Excel files
tw_ports_coords_path = '台灣港經緯度.xlsx'
dest_ports_coords_path = '目的港經緯度.xlsx'

tw_ports_coords_df = pd.read_excel(tw_ports_coords_path)
dest_ports_coords_df = pd.read_excel(dest_ports_coords_path)

# Display the first few rows to inspect the data
tw_ports_coords_df.head(), dest_ports_coords_df.head()

###

tw_ports_coords_df.rename(columns={'臺灣港': 'Port'}, inplace=True)
dest_ports_coords_df.rename(columns={'目的港': 'Port'}, inplace=True)

# Concatenate the two DataFrames
all_ports_coords_df = pd.concat([tw_ports_coords_df, dest_ports_coords_df], ignore_index=True)

# Create a dictionary for port coordinates
port_coordinates = {
    row['Port']: [row['緯度'], row['經度']] for _, row in all_ports_coords_df.iterrows()
}

# Process the monthly weights data to create a list of route dictionaries
routes_data = []
for _, row in monthly_weights_df.iterrows():
    year_month = row['年月']
    year, month = year_month.split('/')
    for port in ['台中港', '基隆港', '花蓮港', '高雄港']:
        weight = row[port]
        routes_data.append({
            'year': year,
            'month': month,
            'startPort': port,
            'endPort': 'SomeDestination',  # You need to provide the actual destination port here
            'weight': weight,
            'color': 'red'  # Assign colors as needed
        })

import json

# Convert the port coordinates and routes data to JSON format
port_coordinates_json = json.dumps(port_coordinates, ensure_ascii=False)
routes_data_json = json.dumps(routes_data, ensure_ascii=False)

port_coordinates_json, routes_data_json