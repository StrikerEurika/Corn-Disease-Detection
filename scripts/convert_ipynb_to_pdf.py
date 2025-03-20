import subprocess

def convert_ipynb_to_pdf(ipynb_path, pdf_path):
    command = f'jupyter nbconvert --to pdf "{ipynb_path}" --output "{pdf_path}"'
    subprocess.run(command, shell=True)

# Example usage
ipynb_path = 'D:\\School\\ITC\\Y3\\Semet 2\\Mini Project\\Project Folder\\Corn-Disease-Detection\\notebooks\\eda.ipynb'
pdf_path = 'D:\\School\\ITC\\Y3\\Semet 2\\Mini Project\\Project Folder\\Corn-Disease-Detection\\assets\\pdf\\eda.pdf'
convert_ipynb_to_pdf(ipynb_path, pdf_path)