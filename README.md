# Helmet Detection using YOLOv3

## Motivation & Credits
The project was inspired from [Dr. C. Krishna Mohnan](https://www.iith.ac.in/~ckm/)'s M2Smart Project at IIT H. The code was forked from an earlier version of [yolov3](https://github.com/ultralytics/yolov3) maintained by [Glenn Jocher](https://github.com/glenn-jocher). Link to the original paper [[here](https://arxiv.org/abs/1804.02767)].

## Prerequisites
Knowledge in one or more of the following will be helpful.
1. Deep Learning
2. Computer Vision 
3. PyTorch
4. Google Colab

## Dataset
Dataset can be requested from this [link](https://www.iith.ac.in/~ckm/vigil/resources.html). Do provide a well written reason for the request. The video datset has to be converted to images and labeled manually. We've used [LabelImg](https://github.com/tzutalin/labelImg) to annotate the classes, the classnames being Helmet and Bike. 

## Implementation
Users are requested to go thoroughly through the original [repo](https://github.com/ultralytics/yolov3). Here is a walkthrough of the steps we've followed.
1. Set up the environment in Google Colab
2. Downloaded the dataset
3. Converted the videos to image frames (code given)
4. Annotated around 1000+ images manually using LabelImg, the more the merrier
5. Uploaded the dataset (images + annotation file) to the Drive associated with Colab
6. Used pretrained weights of COCO dataset to initialize the model (refer orginal repo)
7. Trained on the new dataset uploaded
8. Downloaded the weights and ran detection on PC
9. Modified detect.py to enable webcam

## Results
An image after detection of helmet and motorbike.

![Result](https://user-images.githubusercontent.com/6930097/130743558-46887d57-4603-4522-ae02-7bb8cc6598b4.jpg)

Parameters on how good the model is in identifying the objects trained. 

![download](https://user-images.githubusercontent.com/6930097/130744000-e60129bf-88d1-455c-9095-1a0d4c908d55.png)

## Future Work
For those who would like to extend the project, we would recommend adding the following features
1. Number Plate Detection using OCR
2. Seat Belt Detection
3. A web interface to identify the traffic rule violatores and manage the system

## Note and Disclaimer
* This project was done as part of our Bachelor's Thesis in 2019 and is not actively maintained.
