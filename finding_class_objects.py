import os
import xml.etree.ElementTree as ET
from collections import defaultdict

def convert_annotation(image_id):
    in_file = open('{}.xml'.format(image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()

    classes = []
    for obj in root.iter('object'):
        cls = obj.find('name').text
        classes.append(cls)

    in_file.close()
    return classes

# specify your path
path = 'RDD2022_India\\India\\train\\annotations\\xmls\\'

# get all files in directory
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# filter out non-xml files
xml_files = [f for f in files if f.endswith('.xml')]

# dictionary to hold counts of each class
class_counts = defaultdict(int)

# apply function to each file
for file in xml_files:
    full_path = os.path.join(path, file)
    classes_in_file = convert_annotation(full_path[0:-4])
    for cls in classes_in_file:
        class_counts[cls] += 1

# print counts of each class
for cls, count in class_counts.items():
    print(f"{cls}: {count}")
