import nbconvert
import sys
from pathlib import Path

def convert_notebook_to_html(notebook_path):
    """Convert a Jupyter notebook to HTML format"""
    try:
        # Create an HTML exporter
        html_exporter = nbconvert.HTMLExporter()
        
        # Read and convert the notebook
        notebook_path = Path(notebook_path)
        if not notebook_path.exists():
            raise FileNotFoundError(f"Notebook file {notebook_path} not found")
            
        # Convert the notebook
        (body, resources) = html_exporter.from_filename(str(notebook_path))
        
        # Write the HTML file
        output_file = notebook_path.with_suffix('.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(body)
            
        print(f"Successfully converted {notebook_path} to {output_file}")
        
    except Exception as e:
        print(f"Error converting notebook: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_ipynb_to_html.py <notebook_path>")
        sys.exit(1)
        
    notebook_path = sys.argv[1]
    convert_notebook_to_html(notebook_path)