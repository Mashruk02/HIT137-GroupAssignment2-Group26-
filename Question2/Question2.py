import os
import csv
import pandas as pd
from collections import defaultdict

# Define paths and constants
input_folder = "temperature_data"
average_temp_file = "temperature_data/average_temp.txt"
largest_temp_range_file = "temperature_data/largest_temp_range_station.txt"
warmest_coolest_file = "temperature_data/warmest_and_coolest_station.txt"

# Helper function to clean column names (removes BOM character)
def clean_column_names(fieldnames):
    return [name.lstrip('\ufeff') for name in fieldnames]

# Helper function to calculate average temperature for each month
def calculate_monthly_averages():
    monthly_data = defaultdict(list)
    station_data = defaultdict(list)

    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return {}, {}

    if not os.path.isdir(input_folder):
        print(f"Error: '{input_folder}' is not a directory.")
        return {}, {}

    # Months to identify and reshape wide-format files
    month_columns = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            try:
                df = pd.read_csv(file_path)
                columns = [col.strip('\ufeff') for col in df.columns]

                # Detect wide format if month names are in columns
                if any(month in columns for month in month_columns):
                    if "STATION_NAME" not in columns:
                        print(f"Skipping {filename}: missing 'STATION_NAME' column.")
                        continue
                    df.columns = columns  # Clean BOM characters
                    df_long = df.melt(id_vars=["STATION_NAME"],
                                      value_vars=[m for m in month_columns if m in df.columns],
                                      var_name="Month",
                                      value_name="Temperature")
                    df_long.rename(columns={"STATION_NAME": "Station"}, inplace=True)
                else:
                    # Assume it's already in the correct long format
                    df_long = df
                    df_long.columns = [col.strip('\ufeff') for col in df_long.columns]  # Clean BOM

                for _, row in df_long.iterrows():
                    month = row.get('Month')
                    temp = row.get('Temperature')
                    station = row.get('Station')

                    if month and temp and station:
                        try:
                            temp = float(temp)
                            monthly_data[month].append(temp)
                            station_data[station].append(temp)
                        except ValueError:
                            print(f"Skipping invalid temperature in {filename}: {temp}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Calculate monthly averages
    monthly_averages = {
        month: sum(temps) / len(temps) for month, temps in monthly_data.items()
    }

    return monthly_averages, station_data


# Find station(s) with the largest temperature range
def find_largest_temperature_range(station_data):
    largest_range = float('-inf')
    stations_with_largest_range = []

    for station, temps in station_data.items():
        temp_range = max(temps) - min(temps)
        if temp_range > largest_range:
            largest_range = temp_range
            stations_with_largest_range = [station]
        elif temp_range == largest_range:
            stations_with_largest_range.append(station)

    return stations_with_largest_range, largest_range


# Find warmest and coolest station(s)
def find_warmest_and_coolest_station(station_data):
    warmest_temp = float('-inf')
    coolest_temp = float('inf')
    warmest_stations = []
    coolest_stations = []

    for station, temps in station_data.items():
        avg_temp = sum(temps) / len(temps)

        if avg_temp > warmest_temp:
            warmest_temp = avg_temp
            warmest_stations = [station]
        elif avg_temp == warmest_temp:
            warmest_stations.append(station)

        if avg_temp < coolest_temp:
            coolest_temp = avg_temp
            coolest_stations = [station]
        elif avg_temp == coolest_temp:
            coolest_stations.append(station)

    return warmest_stations, coolest_stations, warmest_temp, coolest_temp


# Save monthly averages to file
def save_monthly_averages(averages):
    if not averages:
        print("No data to save.")
        return

    with open(average_temp_file, 'w') as file:
        for month, avg_temp in sorted(averages.items()):
            file.write(f"Month {month}: {avg_temp:.2f}\n")


# Save largest temperature range station(s) to file
def save_largest_temp_range_station(stations, temp_range):
    with open(largest_temp_range_file, 'w') as file:
        for station in stations:
            file.write(f"Station {station} has the largest temperature range: {temp_range:.2f}°C\n")


# Save warmest and coolest station(s) to file
def save_warmest_and_coolest_station(warmest_stations, coolest_stations, warmest_temp, coolest_temp):
    with open(warmest_coolest_file, 'w') as file:
        file.write(
            f"Warmest Station(s): {', '.join(warmest_stations)} with an average temperature of {warmest_temp:.2f}°C\n")
        file.write(
            f"Coolest Station(s): {', '.join(coolest_stations)} with an average temperature of {coolest_temp:.2f}°C\n")


# Main function to calculate and save results
def main():
    monthly_averages, station_data = calculate_monthly_averages()

    # Save monthly averages
    save_monthly_averages(monthly_averages)

    # Find and save the station(s) with the largest temperature range
    stations_with_largest_range, largest_range = find_largest_temperature_range(station_data)
    save_largest_temp_range_station(stations_with_largest_range, largest_range)

    # Find and save the warmest and coolest station(s)
    warmest_stations, coolest_stations, warmest_temp, coolest_temp = find_warmest_and_coolest_station(station_data)
    save_warmest_and_coolest_station(warmest_stations, coolest_stations, warmest_temp, coolest_temp)


# Run the program
if __name__ == "__main__":
    main()
