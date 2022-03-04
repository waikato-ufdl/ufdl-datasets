.. title: Caltech-UCSD Birds-200-2011
.. slug: caltech-ucsd_birds-200-2011
.. date: 2022-03-04 14:20:51 UTC+13:00
.. tags: object-detection, image-classification
.. category: image-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/caltech-ucsd_birds-200-2011.jpg
   :height: 200px
   :alt: Caltech-UCSD Birds-200-2011: Black footed Albatross
   :align: right

Image classification and object detection datasets containing 11,788 images consisting of 200 species of birds (**Warning:** Images in this dataset overlap with images in ImageNet).

* `Source <http://www.vision.caltech.edu/visipedia/CUB-200-2011.html>`__ (`README </data/raw/caltech-ucsd_birds-200-2011/README.txt>`__)
* `Original dataset </data/raw/caltech-ucsd_birds-200-2011/CUB_200_2011.tgz>`__ (1.2GB)
* `Image classification dataset </data/image_classification/caltech-ucsd_birds-200-2011/caltech-ucsd_birds-200-2011-imgcls.zip>`__ (1.1GB)
* `Object detection dataset (VOC XML format) </data/object_detection/caltech-ucsd_birds-200-2011/caltech-ucsd_birds-200-2011-voc.zip>`__ (1.1GB)

Conversion from original data:

* Rename *images* folder to *subdir*. This is the **image-classification** form of the dataset.
* Run the attached `Python script </data/conversion/caltech-ucsd_birds-200-2011/fix_birds.py>`__ (requires the `wai.annotations <https://github.com/waikato-ufdl/wai-annotations>`__ library; tested with 0.7.4) in the CUB-200-2011 directory to parse the *bounding_boxes.txt* into Pascal VOC format. The data in the *voc* directory is the **object-detection** form of the dataset.

**License** (according to Caltech website)

*We do not own the copyrights to these images. Their use is restricted to non-commercial research and educational purposes.*