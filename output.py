import pandas as pd
import json

# Load the provided CSV file
file_path = '0528出口貨物.csv'
df = pd.read_csv(file_path)

# Define the ports with all codes
ports_with_all_codes = ['TWTXG', 'TWHUN', 'TWKEL', 'TWKHH']#, '臺中港(TWTXG)'
destination_ports = ["上海港(CNSHA)", "香港港(HKHKG)", "大阪港(JPOSA)", "釜山港(KRPUS)"]

# Filter the dataframe for the specified ports and destination ports
# df_filtered_complete = df[(df['臺灣港'].isin(ports_with_all_codes)) & (df['目的港'].isin(destination_ports))]

# Standardize the port names
# df_filtered_complete['臺灣港'] = df_filtered_complete['臺灣港'].str.replace(r'\(.*\)', '', regex=True)

# Group by '年月', '臺灣港', and '目的港', then sum the '重量'
df_grouped_complete = df.groupby(['年月', '臺灣港', '目的港'])['重量'].sum().reset_index()

# Define a dictionary to map each start port to a unique color
color_mapping = {
    'TWTXG': 'red',
    'TWHUN': 'blue',
    'TWKEL': 'green',
    'TWKHH': 'yellow',
    '臺中港': 'red'  # Assuming '臺中港' is the same as '台中港'
}

# Prepare the data in the required JSON format
routes_data = []
for _, row in df_grouped_complete.iterrows():
    year_month = row['年月']
    month, year = year_month.split('-')
    start_port_name = row['臺灣港'].replace('(TWTXG)', '').replace('(TWHUN)', '').replace('(TWKEL)', '').replace('(TWKHH)', '')
    color = color_mapping.get(start_port_name.strip(), 'black')  # Default to black if port not found
    routes_data.append({
        "year": year,
        "month": month,
        "startPort": row['臺灣港'],
        "endPort": row['目的港'],
        "weight": row['重量'],
        "color": color
    })

# Save the result to a JSON file
output_path = 'myroutes_data.json'  # Update the path where you want to save the JSON file
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(routes_data, f, ensure_ascii=False, indent=4)

print(f"JSON file has been saved to {output_path}")