import pandas as pd
import os

def combine_csv_files():
    # Directory containing the CSV files
    csv_dir = r'D:\School\ITC\Y3\Semet 2\Mini Project\Project Folder\Corn-Disease-Detection\datasets\finalized-data\csv'  # Adjust this path as needed
    
    # List to store individual dataframes
    dfs = []
    
    # Get all CSV files in the directory
    csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
    
    # Read each CSV file and append to the list
    for file in csv_files[:3]:  # Limit to first 3 files
        file_path = os.path.join(csv_dir, file)
        df = pd.read_csv(file_path)
        dfs.append(df)
    
    # Combine all dataframes
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Save the combined dataframe to a new CSV file
    output_path = r'D:\School\ITC\Y3\Semet 2\Mini Project\Project Folder\Corn-Disease-Detection\datasets\finalized-data\csv\combined_data.csv'
    combined_df.to_csv(output_path, index=False)
    print(f"Combined CSV saved to: {output_path}")

if __name__ == "__main__":
    combine_csv_files()