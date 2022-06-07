.. title: CamVid Database
.. slug: camvid
.. date: 2022-06-07 10:10:51 UTC+12:00
.. tags: image-segmentation
.. category: image-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/camvid.jpg
   :height: 200px
   :alt: CamVid examples
   :align: right

Image segmentation dataset generated from dash cam videos, consisting of 700 images (and their associated annotations.
The dataset comprises 32 labels.

* `Source <http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/>`__
* Original dataset: `images </data/raw/camvid/701_StillsRaw_full.zip>`__ (557MB), `annotations </data/raw/camvid/LabeledApproved_full.zip>`__ (16MB), `label colors </data/raw/camvid/label_colors.txt>`__
* `Image segmentation dataset (blue-channel) </data/image_segmentation/camvid/camvid-bluechannel.zip>`__ (163MB)

Conversion from original data into dataset storing the label index in the blue channel of the RGB PNG image (1-32):

* Download the *images* and *annotations* archives and extract them, resulting in the *701_StillsRaw_full* and *LabeledApproved_full* directories.
* Create *bluechannel* directory at the same level as extracted archives.
* Run this `Python script </conversion/camvid/bluechannel.py>`__ (`requirements.txt </conversion/camvid/requirements.txt>`__) in the top-level directory to create images/annotations in the *bluechannel* directory: `./venv/bin/python bluechannel.py`

**NB:** This conversion script skips image/annotation pair `Seq05VD_f02610` as it contains colors other than the defined
labels, which reduces the number of images from the original 701 to 700.


**Citation**

* Brostow, Gabriel J., Jamie Shotton, Julien Fauqueur, and Roberto Cipolla. "Segmentation and recognition using structure
  from motion point clouds." In European conference on computer vision, pp. 44-57. Springer, Berlin, Heidelberg, 2008.
* Gabriel J. Brostow, Julien Fauqueur, Roberto Cipolla, Semantic object classes in video: A high-definition ground truth database,
  Pattern Recognition Letters, Volume 30, Issue 2, 2009, Pages 88-97, ISSN 0167-8655, https://doi.org/10.1016/j.patrec.2008.04.005.

**License**

Unclear.
