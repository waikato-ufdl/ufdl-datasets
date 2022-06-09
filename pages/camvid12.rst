.. title: CamVid-12 Database
.. slug: camvid12
.. date: 2022-06-10 11:30:51 UTC+12:00
.. tags: image-segmentation
.. category: image-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/camvid12.jpg
   :height: 200px
   :alt: CamVid-12 example
   :align: right

Image segmentation dataset generated from dash cam videos, consisting of 701 images (and their associated annotations.
The dataset comprises 12 labels as opposed to the original `CamVid <link://slug/camvid>`__ dataset with 32.

* `Source <https://github.com/alexgkendall/SegNet-Tutorial>`__
* Original dataset: `SegNet-Tutorial-master.zip </data/camvid12/SegNet-Tutorial-master.zip>`__ (179MB)
* `Image segmentation dataset (grayscale) </data/camvid12/camvid12-grayscale.zip>`__ (51MB)
* `Image segmentation dataset (grayscale/split) </data/camvid12/camvid12-grayscale-split.zip>`__ (51MB)

Conversion from original data:

* Download the *SegNet-Tutorial-master* archive and extract it, resulting in the *SegNet-Tutorial-master* directory.
* In the same directory, create the following sub-directories: grayscale, grayscale-split
* Run this `Python script </conversion/camvid12/grayscale.py>`__ (`requirements.txt </conversion/camvid12/requirements.txt>`__) in the top-level directory to create images/annotations in the *grayscale* and *grayscale-split* directories:

  `./venv/bin/python grayscale.py SegNet-Tutorial-master grayscale-split grayscale`

* The *grayscale-split* directory contains the train/val/test splits just like in the original data zip,
  but the dash cam image itself converted to JPG and the annotation in the same directory.
* The *grayscale* directory contains all the images from the train/val/test directories, e.g.,
  for converting it into other formats (e.g., bluechannel) or for generating different splits.

**License**

Unclear, like original `CamVid <link://slug/camvid>`__ dataset.
