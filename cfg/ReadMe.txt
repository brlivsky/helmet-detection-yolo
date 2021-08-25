Updates in yolov3.cfg
Replaced all "filters=255" into "filters=24"
Each YOLO layer outputs 255 values: 85 values [4 box coordinates + 1 object confidence + 80 class confidences] per anchor, times 3 anchors.
Since we are having only 3 classes, we only require 85 outputs value [4 box coordinates + 1 object confidence + 3 class confidences] per anchor, times 3 anchors.