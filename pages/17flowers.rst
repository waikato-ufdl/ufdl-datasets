.. title: 17 Flowers
.. slug: 17flowers
.. date: 2022-03-08 11:40:51 UTC+13:00
.. tags: image-classification, object-detection
.. category: image-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/17flowers.jpg
   :height: 200px
   :alt: 17 flowers: Daffodil
   :align: right

Image classification dataset containing 1360 images consisting of 17 species of flowers (trimaps/bounding box annotations only available for 16):

* `Source <https://www.robots.ox.ac.uk/~vgg/data/flowers/17/>`__ (`README </data/raw/17flowers/README.txt>`__)
* `Original images </data/raw/17flowers/17flowers.zip>`__ (60MB), `original trimaps </data/raw/17flowers/trimaps.zip>`__ (60MB)
* `Image classification dataset </data/image_classification/17flowers/17flowers-subdir.zip>`__ (33MB)
* `Object detection dataset </data/object_detection/17flowers/17flowers-voc.zip>`__ (58MB)

Conversion from original data:

* Decompress images and trimaps archives
* Create directory *voc*
* Copy all images from *jpg* directory into *voc*
* Run `Python script </data/conversion/17flowers/trimap_to_bb.py>`__ (`requirements.txt </data/conversion/17flowers/requirements.txt>`__) from the directory with *jpg* and *voc* directories to generate the bounding boxes in VOC XML format
* The *voc* directory contains the **object detection** dataset
* Run: `wai-annotations convert from-voc-od -i "voc/*.xml" od-to-ic to-subdir-ic -o subdir` (requires the `wai.annotations <https://github.com/waikato-ufdl/wai-annotations>`__ library; tested with 0.7.4)
* The *subdir* directory contains the **image classification** dataset

**License**

Unclear.