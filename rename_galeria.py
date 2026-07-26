import os
import glob

# Path to the directory
directory = r"C:\Users\CNT\Documents\ProjetosDev2026\sopa-de-casa-website\images\Galeria"

# Get all jpeg/jpg files
files = glob.glob(os.path.join(directory, "*.jpeg")) + glob.glob(os.path.join(directory, "*.jpg"))

for i, filepath in enumerate(files, 1):
    new_name = f"galeria-{i}.jpg"
    new_filepath = os.path.join(directory, new_name)
    os.rename(filepath, new_filepath)
    print(f"Renamed: {os.path.basename(filepath)} -> {new_name}")
