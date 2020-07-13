#!/bin/sh
if [ ! -e coco-labels-paper.txt ]; then
    wget https://raw.githubusercontent.com/amikelive/coco-labels/master/coco-labels-paper.txt
fi
wget http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz
tar xvzf ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz
rm ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz
