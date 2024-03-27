import csv

def read_filter_csv(input_file, min_val=-2, max_val=2.2):
    """
    Reads sensor data from a CSV file, filters based on a specific column's value,
    and returns the filtered and sorted data.
    """
    filtered_rows = []
    
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        
        for row in reader:
            try:
                if min_val < float(row[19]) < max_val:
                    filtered_rows.append([row[11], row[12], row[13], row[19]])
            except ValueError:
                continue
    
    return sorted(filtered_rows, key=lambda x: float(x[3]))

def write_to_csv(output_file, data, headers=["Header1", "Header2", "Header3", "SensorReading"]):
    """
    Writes given data to a CSV file, including optional headers.
    """
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

# Usage example
input_csv_path = "path_to_your_sensor_data.csv"  # Path to your input CSV file
output_csv_path = "filtered_sensor_data.csv"     # Path for the output CSV file

# Read, filter, and sort data from the input CSV
filtered_data = read_filter_csv(input_csv_path)

# Write the filtered data to a new CSV file
write_to_csv(output_csv_path, filtered_data)
