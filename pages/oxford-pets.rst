.. title: Oxford Pets
.. slug: oxford-pets
.. date: 2022-08-01 13:20:51 UTC+12:00
.. tags: object-detection, image-classification, image-segmentation, instance-segmentation
.. category: image-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/oxford-pets.jpg
   :height: 200px
   :alt: Oxford Pets: Shiba Inu
   :align: right

Image classification, object detection, image segmentation and instance segmentation datasets containing 37 categories of cats and dogs.

* `Source <https://www.robots.ox.ac.uk/~vgg/data/pets/>`__
* Original dataset: `images </data/oxford-pets/images.tar>`__ (755MB), `annotations </data/oxford-pets/annotations.tar>`__ (18MB)
* `Image classification dataset </data/oxford-pets/oxford-pets-subdir.zip>`__ (752MB)
* `Image segmentation dataset (animal ROI; bluechannel) </data/oxford-pets/oxford-pets-bluechannel.zip>`__ (769MB)
* `Instance segmentation dataset (animal ROI; MS COCO) </data/oxford-pets/oxford-pets-coco.zip>`__ (729MB)
* `Object detection dataset (head bbox; VOC XML format) </data/oxford-pets/oxford-pets-voc-head.zip>`__ (359MB)
* `Object detection dataset (animal bbox; VOC XML format) </data/oxford-pets/oxford-pets-voc-animal.zip>`__ (710MB)

Conversion from original data:

* Download the *images* and *annotations* archives and extract them, resulting in the *annotations* and *images* directories.
* Create *output* directory at the same level as extracted archives.
* Create virtual environment using `these requirements </conversion/oxford-pets/requirements.txt>`__:

  * `python3 -m venv venv`
  * `./venv/bin/pip install -r requirements.txt`

* Classification

  * Run the `classification.py </conversion/oxford-pets/classification.py>`__ Python script: `./venv/bin/python classification.py . output`
  * The *output/subdir* directory contains the image classification dataset

* Object detection (head ROI)

  * Run the `object_detection.py </conversion/oxford-pets/object_detection.py>`__ Python script: `./venv/bin/python object_detection.py . output`
  * The *output/voc-head* directory contains the object detection dataset with the head ROI annotations

* Object detection, image/instance segmentation (animal ROI)

  * Run the `segmentation.py </conversion/oxford-pets/segmentation.py>`__ Python script: `./venv/bin/python segmentation.py . output`
  * The *output/bluechannel* directory contains the **image segmentation** dataset
  * The *output/adams* directory contains the **instance segmentation** dataset in ADAMS format
  * Convert the ADAMS annotations into MS COCO using the `wai.annotations <https://github.com/waikato-ufdl/wai-annotations>`__ library:

    ``wai-annotations convert from-adams-od -i "./adams/*.report" to-coco-od -o ./coco/annotations.json``

  * Convert the ADAMS annotations into VOC using the `wai.annotations <https://github.com/waikato-ufdl/wai-annotations>`__ library:

    ``wai-annotations convert from-adams-od -i "./adams/*.report" coerce-box to-voc-od -o ./voc-animal``


**License**
`CC-BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`__

**Citation**
`O. M. Parkhi, A. Vedaldi, A. Zisserman, C. V. Jawahar: Cats and Dogs, IEEE Conference on Computer Vision and Pattern Recognition, 2012 <https://www.robots.ox.ac.uk/~vgg/publications/2012/parkhi12a/>`__.
