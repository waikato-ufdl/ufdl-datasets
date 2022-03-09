.. title: Stanford Dogs
.. slug: stanford-dogs
.. date: 2022-03-04 14:40:51 UTC+13:00
.. tags: object-detection, image-classification
.. category: image-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/stanford-dogs.jpg
   :height: 200px
   :alt: Stanford Dogs: English foxhound
   :align: right

Image classification and object detection datasets containing 20,580 images consisting of 120 species of dogs (**Warning:** Images in this dataset were taken from ImageNet).

* `Source <http://vision.stanford.edu/aditya86/ImageNetDogs/main.html>`__ (`README </data/raw/stanford-dogs/README.txt>`__)
* Original dataset: `images </data/raw/stanford-dogs/images.tar>`__ (794MB), `annotations </data/raw/stanford-dogs/annotation.tar>`__ (22MB)
* `Image classification dataset </data/image_classification/stanford-dogs/stanford-dogs-subdir.zip>`__ (775MB)
* `Object detection dataset (VOC XML format) </data/object_detection/stanford-dogs/stanford-dogs-voc.zip>`__ (781MB)

Conversion from original data:

* Download the *images* and *annotations* archives and extract them, resulting in the *Annotation* and *Images* directories.
* Create *voc* directory at the same level as extracted archives.
* Create virtual environment:

  * `python3 -m venv venv`
  * `./venv/bin/pip install defusedxml`

* Run this `Python script </data/conversion/stanford-dogs/fix_dogs.py>`__ in the top-level directory to fix/move the annotations into the *voc* directory: `./venv/bin/python fix_dogs.py`
* Move all images into *voc* directory: `mv Images/**/* voc/`
* Copy the images from `this archive </data/conversion/stanford-dogs/fixed_dogs.zip>`__ into the *voc* directory, replacing the originals. These are the images that we found with binary issues, that were hand edited to fix.
* Run: `wai-annotations convert from-voc-od -i "voc/*.xml" od-to-ic -m single to-subdir-ic -o subdir` (tested with `wai.annotations==0.7.4 <https://github.com/waikato-ufdl/wai-annotations>`__)
* From inside the resulting *subdir* directory, run `xargs -I{} rm "{}" < path/to/remove.txt` with the `remove.txt </data/conversion/stanford-dogs/remove.txt>`__ file to remove other damaged images (these could not be hand-fixed).
* The resulting *voc* and *subdir* directories are the **object detection** and **image classification** versions of this dataset.

**License** (according to ImageNet website)

*No, ImageNet does not own the copyright of the images. ImageNet only compiles an accurate list of web images for each synset of WordNet. For researchers and educators who wish to use the images for non-commercial research and/or educational purposes, we can provide access through our site under certain conditions and terms.*