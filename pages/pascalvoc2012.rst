.. title: Pascal VOC 2012
.. slug: pascalvoc2012
.. date: 2023-02-17 16:10:51 UTC+13:00
.. tags: image-segmentation
.. category: image-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/pascalvoc2012.png
   :alt: Pascal VOC 2012 examples
   :align: right


The purpose of the Pascal VOC 2012(PASCAL Visual Object Classes) dataset is to recognize objects in realistic scenarios
from a variety of visual object types that are not pre-segmented objects and is basically used for the supervised
learning task. The dataset can be used for different object recognition challenges such as classification, detection,
segmentation, and person layout. There are a whole total of twenty object classes chosen. There are 11,530 images in
the train/val data set, including 27,450 ROI-tagged objects and 6,929 segmentations.

* `Source <http://host.robots.ox.ac.uk/pascal/VOC/voc2012/>`__
* `Original dataset </data/pascalvoc2012/VOCtrainval_11-May-2012.tar>`__ (2GB), `documentation <http://host.robots.ox.ac.uk/pascal/VOC/voc2012/devkit_doc.pdf>`__ (500KB)
* `Image segmentation dataset (indexed-png) </data/pascalvoc2012/pascalvoc2012-indexedpng.zip>`__ (315MB)

Conversion from original data into dataset without the borders and void labels (index=255) is achieved with the
`convert.py </conversion/pascalvoc2012/convert.py>`__ Python script:

`./venv/bin/python convert.py <JPEGImages dir> <SegmentationClass dir> <output dir>`


**Citation**

* Everingham, M. and Van Gool, L. and Williams, C. K. I. and Winn, J. and Zisserman, A.,
  The PASCAL Visual Object Classes Challenge 2012 (VOC2012) Results,
  `http://www.pascal-network.org/challenges/VOC/voc2012/workshop/index.html <http://www.pascal-network.org/challenges/VOC/voc2012/workshop/index.html>`__.


**License**

The VOC2012 data includes images obtained from the "flickr" website. Use of these images must respect the corresponding
terms of use:

* `"flickr" terms of use <http://www.flickr.com/terms.gne?legacy=1>`__

For the purposes of the challenge, the identity of the images in the database, e.g. source and name of owner, has been
obscured. Details of the contributor of each image can be found in the annotation to be included in the final release
of the data, after completion of the challenge. Any queries about the use or ownership of the data should be addressed
to the organizers.
