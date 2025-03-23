import os
import shutil
from pathlib import Path

# Define source folders and destination folder
source_folders = [
    r"D:\School\ITC\Y3\Semet 2\Mini Project\Project Folder\Corn-Disease-Detection\datasets\Corn Diseases.v2-no-tile.multiclass\test",  # Replace with your first folder path
    r"D:\School\ITC\Y3\Semet 2\Mini Project\Project Folder\Corn-Disease-Detection\datasets\Corn Diseases.v2-no-tile.multiclass\train",  # Replace with your second folder path
    r"D:\School\ITC\Y3\Semet 2\Mini Project\Project Folder\Corn-Disease-Detection\datasets\Corn Diseases.v2-no-tile.multiclass\valid"   # Replace with your third folder path
]

destination_folder = r"D:\School\ITC\Y3\Semet 2\Mini Project\Project Folder\Corn-Disease-Detection\datasets\finalized-data\raw-data"  # Replace with your destination folder path

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Function to combine images
def combine_images():
    for folder in source_folders:
        if not os.path.exists(folder):
            print(f"Source folder {folder} does not exist!")
            continue
        
        # Get all files from the source folder
        files = os.listdir(folder)
        
        # Filter for image files (you can modify extensions as needed)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        
        # Copy each image to destination folder
        for image in image_files:
            source_path = os.path.join(folder, image)
            # Add folder name as prefix to avoid naming conflicts
            # new_name = f"{os.path.basename(folder)}_{image}"
            destination_path = os.path.join(destination_folder, image)
            
            try:
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {image} to {destination_path}")
            except Exception as e:
                print(f"Error copying {image}: {str(e)}")

if __name__ == "__main__":
    combine_images()
    print("Image combination complete!")