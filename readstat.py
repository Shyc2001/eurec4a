import os
import xarray as xr

def load_nc_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return None

    # Load and return the NC file content using xarray
    ds = xr.open_dataset(file_path)

    return ds

def main():
    # Define the paths to the NC files
    cond_stats_path = './Output.Bomex.4fd96/cond_stats/CondStats.Bomex.nc'
    stats_path = './Output.Bomex.4fd96/stats/Stats.Bomex.nc'

    # Load the NC file contents
    cond_stats_ds = load_nc_file(cond_stats_path)
    stats_ds = load_nc_file(stats_path)

    # Check if data is loaded successfully and print the contents
    if cond_stats_ds is not None:
        print("CondStats.Bomex.nc content:")
        print(cond_stats_ds)

    if stats_ds is not None:
        print("Stats.Bomex.nc content:")
        print(stats_ds)

if __name__ == "__main__":
    main()
