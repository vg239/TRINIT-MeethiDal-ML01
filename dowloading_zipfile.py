import urllib.request

# Define the URL of the zip file
url = 'https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_India.zip'

# Define the filename to save the zip file
filename = 'dataset.zip'

# Download the zip file
urllib.request.urlretrieve(url, filename)
