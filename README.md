# TRINIT-MeethiDal-ML01
We have used the YOLO model to run object detecion

## Donwloading and unzipping the provided dataset
We have only dealt with the India Dataset

First creating a python script to download the required dataset onto Google Colab using [urllib](dowloading_zipfile.py)

After which we unzipped the file to get the required images and xml annotatoins using [this python code](unzipping.py)

## Finding out the number of class objects in the given xml files
Since there were various class objects such as D00 D40 etc. , we ran a [code](finding_class_objects.py) to get the following output

![image](https://github.com/vg239/TRINIT-MeethiDal-ML01/assets/139644618/823301b6-7c47-4508-8dd1-e6922c84183d)

## xml to txt
After this we ran a [python code](xml_to_txt.py) using the os library so as to get the relative sizing and coordinates of the class objects from all the xml file into txt files.

## Creation of yaml file and building or training the model
We created the [yaml file](config.yaml) and after that we trained the model using the YOLOv8 model containing both the images and the txt files corresponding to them which contain the coordinates and relative sizing.

```python
from ultralytics import YOLO
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model.train(data="config.yaml", epochs=1)  # train the model
```
