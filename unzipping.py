import zipfile

# Open the zip file
with zipfile.ZipFile('dataset.zip', 'r') as zip_ref:
    # Extract all the files in the zip file
    zip_ref.extractall('.')

with zipfile.ZipFile('dataset.zip', 'r') as zip_ref:
    zip_ref.extractall('Images')
