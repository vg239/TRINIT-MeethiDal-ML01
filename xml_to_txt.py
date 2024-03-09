import xml.etree.ElementTree as ET
import os

def convert_annotation(image_id, class_dict):
    in_file = open('{}.xml'.format(image_id))
    out_file = open('{}.txt'.format(image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in class_dict or int(difficult) == 1:
            continue
        cls_id = class_dict[cls]
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
        bb = (b[0]/w, b[1]/h, b[2]/w, b[3]/h)  # normalize bounding box coordinates
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


class_dict = {"D40": 0}

path = 'RDD2022_India\\India\\train\\annotations\\xmls\\'


files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# filter out non-xml files
xml_files = [f for f in files if f.endswith('.xml')]


# apply function to each file
for file in xml_files:
    full_path = os.path.join(path, file)
    try:
    
        convert_annotation(full_path[0:-4], class_dict)
    except AttributeError:
        continue
    
