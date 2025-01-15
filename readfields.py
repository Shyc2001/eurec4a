import os
import xarray as xr

def load_nc_file(time, number):
    # Define the path to the NC file
    file_path = f'./Output.Bomex.4fd96/fields/{time}/{number}.nc'

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return None

    # Load and return the NC file content using xarray
    ds = xr.open_dataset(file_path)

    return ds

def main():
    # User input for time and number
    time = input("Enter the time (e.g., 3600): ")
    number = input("Enter the number (e.g., 0): ")

    # Load the NC file content
    ds = load_nc_file(time, number)

    # Check if data is loaded successfully
    if ds is not None:
        print("NC file content:")
        print(ds)

if __name__ == "__main__":
    main()
