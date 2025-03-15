import os
import shutil
import pandas as pd
import sys

# load csv
def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        data.columns = data.columns.str.strip()
        return data
    except Exception as e:
        print(f"Failed to load CSV: {file_path}")
        return None
    
# Move image ti respective folder
def move_images(data:pd.DataFrame, image_dir, output_dir):
    # check output folder existence
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # create classes folders in output
    classes = ['Corn Rust', 'Grey Leaf Spot', 'Leaf Blight'] 	 	 
    for class_name in classes:
        class_dir = os.path.join(output_dir, class_name)
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)
        
    # move images based on labels in csv
    for index, row in data.iterrows():
        filename =  row['filename']
        file_path = os.path.join(image_dir, filename)
        
        if os.path.exists(file_path):
            if row['Corn Rust'] == 1:
                shutil.move(file_path, os.path.join(output_dir, 'Corn Rust'))
            elif row['Grey Leaf Spot'] == 1:
                shutil.move(file_path, os.path.join(output_dir, 'Grey Leaf Spot'))
            elif row['Leaf Blight'] == 1:
                shutil.move(file_path, os.path.join(output_dir, 'Leaf Blight'))
            else:
                print(f"No classes asigned for {filename}. Skipping...")
        else:
            print(f"File {filename} not Found. Skipping...")

# Main Funstion
def main():
    csv_file_path = r'D:\School\ITC\Y3\Semet 2\Mini Project\Project Folder\Corn-Disease-Detection\datasets\Corn Diseases.v2-no-tile.multiclass\csv\valid_classes.csv'
    image_dir = r'D:\School\ITC\Y3\Semet 2\Mini Project\Project Folder\Corn-Disease-Detection\datasets\Corn Diseases.v2-no-tile.multiclass\valid'
    output_dir = r'D:\School\ITC\Y3\Semet 2\Mini Project\Project Folder\Corn-Disease-Detection\datasets\finalized-data\valid'
    
    data = load_csv(csv_file_path)
    if data is not None:
        move_images(data, image_dir, output_dir)


if __name__ == '__main__':
    main()