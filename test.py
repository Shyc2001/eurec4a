import netCDF4 as nc

def inspect_group(group, indent=0):
    indent_str = '  ' * indent
    print(f"{indent_str}Group: {group.path}")
    print(f"{indent_str}Dimensions:")
    for dim in group.dimensions.values():
        print(f"{indent_str}  {dim.name}: {dim.size}")

    print(f"{indent_str}Variables:")
    for var in group.variables.values():
        print(f"{indent_str}  {var.name}: {var.shape}, {var.dtype}")

    for subgrp in group.groups.values():
        inspect_group(subgrp, indent + 1)

def inspect_nc_file(file_path):
    try:
        ds = nc.Dataset(file_path)
        print(f"Inspecting {file_path}:\n")
        inspect_group(ds)
    except Exception as e:
        print(f"Error inspecting {file_path}: {e}")

def main():
    cond_stats_path = './Output.Bomex.4fd96/cond_stats/CondStats.Bomex.nc'
    stats_path = './Output.Bomex.4fd96/stats/Stats.Bomex.nc'

    inspect_nc_file(cond_stats_path)
    inspect_nc_file(stats_path)

if __name__ == "__main__":
    main()
