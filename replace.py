import os

directory_to_scan = os.getcwd()

def replace_in_file(file_path, search_text, replace_text, exclude_text=None):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    new_lines = []
    for line in lines:
        if exclude_text and exclude_text in line:
            new_lines.append(line)
        else:
            new_lines.append(line.replace(search_text, replace_text))
    
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

for root, dirs, files in os.walk(directory_to_scan):
    for file in files:
        if file.endswith(".pyx") or file.endswith(".pxd") or file.endswith(".h"):
            file_path = os.path.join(root, file)
            replace_in_file(file_path, 'noexcept', 'nogil', exclude_text='with nogil')

print("Replacement complete.")
