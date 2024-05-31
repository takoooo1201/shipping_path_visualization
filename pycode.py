import pandas as pd
import json

# Load the provided CSV file
monthly_weights_path = 'Monthly_Port_Weights_with_Complete_Ports.csv'
tw_ports_coords_path = '台灣港經緯度.xlsx'
dest_ports_coords_path = '目的港經緯度.xlsx'

monthly_weights_df = pd.read_csv(monthly_weights_path)
tw_ports_coords_df = pd.read_excel(tw_ports_coords_path)
dest_ports_coords_df = pd.read_excel(dest_ports_coords_path)

# Process port coordinates
tw_ports_coords_df.rename(columns={'臺灣港': 'Port'}, inplace=True)
dest_ports_coords_df.rename(columns={'目的港': 'Port'}, inplace=True)
all_ports_coords_df = pd.concat([tw_ports_coords_df, dest_ports_coords_df], ignore_index=True)
port_coordinates = {row['Port']: [row['緯度'], row['經度']] for _, row in all_ports_coords_df.iterrows()}

# Process routes data
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
            'endPort': 'SomeDestination',  # Replace this with actual destination port
            'weight': weight,
            'color': 'red'  # Assign colors as needed
        })

# Save to JSON files
with open('port_coordinates.json', 'w', encoding='utf-8') as f:
    json.dump(port_coordinates, f, ensure_ascii=False, indent=4)

with open('routes_data.json', 'w', encoding='utf-8') as f:
    json.dump(routes_data, f, ensure_ascii=False, indent=4)
