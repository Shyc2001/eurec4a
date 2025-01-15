import os
import pickle

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

def main():
    # User input for time and number
    time = input("Enter the time (e.g., 3600): ")
    number = input("Enter the number (e.g., 0): ")

    # Load the PKL file content
    data = load_pkl_file(time, number)

    # Check if data is loaded successfully
    if data is not None:
        print("PKL file content:")
        print(data)

if __name__ == "__main__":
    main()
