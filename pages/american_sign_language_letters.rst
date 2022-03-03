.. title: American Sign Language Letters
.. slug: american-sign-language-letters
.. date: 2022-03-03 15:02:51 UTC+13:00
.. tags: object-detection, image-classification
.. category: image-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

Object detection and image classification dataset containing 1,728 images in total for all ASL letters (in case of object detection with a bounding box).

* `Source <https://public.roboflow.com/object-detection/american-sign-language-letters/1>`__
* `Original dataset </data/raw/american-sign-language-letters/American%20Sign%20Language%20Letters.v1-v1.voc.zip>`__
* `Image classification dataset </data/image_classification/american-sign-language-letters/american-sign-language-letters-imgcls.zip>`__
* `Object detection dataset (VOC XML format) </data/object_detection/american-sign-language-letters/american-sign-language-letters-voc.zip>`__

Conversion from original data:

* Download the dataset in Pascal VOC format from the URL (use default settings). If the download does not work, double-check you are logged in to Roboflow, as the website is not very good at indicating this.
* Extract and move all images/xml annotations into a single directory called *voc*. This is the **object-detection** form of the dataset.
* Run: `wai-annotations convert from-voc-od -i "voc/*.xml" od-to-ic to-subdir-ic -o subdir` (requires the `wai.annotations <https://github.com/waikato-ufdl/wai-annotations>`__ library; tested with 0.7.4)
* The resulting *subdir* directory is the **image classification** form of the dataset.

**License** (according to Roboflow website)

Public domain