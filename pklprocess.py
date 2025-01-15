import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

def load_pkl_file(time, number):
    # Define the path to the PKL file
    file_path = f'./Output.Bomex.4fd96/Restart/{time}/{number}.pkl'

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return None

    # Load and return the PKL file content
    with open(file_path, 'rb') as file:
        data = pickle.load(file)

    return data

data = load_pkl_file(600,0)

# Extract specific variable values from PV
pv = data.get('PV', {})
# Assuming 'pv' is already defined
values = pv.get('values', [])
variable_length = 76800  # Length of each variable
grid_dimensions = (32, 32, 75)  # Assumed grid dimensions

# Extract the index of 'qt' variable
qt_index = pv.get('name_index', {}).get('qt', None)

if qt_index is not None:
    # Extract the values for 'qt' variable
    qt_values = values[qt_index * variable_length : (qt_index + 1) * variable_length]
    # Reshape the values into the grid dimensions
    qt_values_reshaped = np.reshape(qt_values, grid_dimensions)
    # Compute the mean over the horizontal dimensions (32x32)
    qt_mean_vertical = np.mean(qt_values_reshaped, axis=(0, 1))*1000
    print(qt_mean_vertical)
else:
    print("Variable 'qt' not found in 'name_index'")
    
# Generate the height array (3 km divided into 75 parts)

heights = np.linspace(0, 3, 75)

# Plotting
plt.figure(figsize=(4, 8))
plt.plot(qt_mean_vertical, heights, color='blue', label='qt')
plt.xlabel('qt: g kg$^{-1}$')
plt.ylabel('Height: KM')
plt.legend()
plt.grid(True)
plt.title('qt_600s')
plt.show()
