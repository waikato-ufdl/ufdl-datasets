.. title: CIFAR-10
.. slug: cifar10
.. date: 2022-11-09 11:15:51 UTC+13:00
.. tags: image-classification
.. category: image-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/cifar10.png
   :height: 200px
   :alt: Examples of CIFAR-10 images
   :align: right

The CIFAR-10 dataset is a labeled subset of the `80 million tiny images <http://people.csail.mit.edu/torralba/tinyimages/>`__
dataset consisting of 10 classes. They were collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton:

* `Source <https://www.cs.toronto.edu/~kriz/cifar.html>`__ (`CLASSES </data/cifar10/CLASSES>`__)
* `Original images </data/cifar10/cifar-10-python.tar.gz>`__ (162MB, contains Python pickled objects)
* Image classification dataset: `train </data/cifar10/cifar10-subdir-train.zip>`__ (120MB), `train </data/cifar10/cifar10-subdir-test.zip>`__ (24MB)

Conversion from original data:

* Decompress the images
* Run `Python script </conversion/cifar10/convert.py>`__ (`requirements.txt </conversion/cifar10/requirements.txt>`__) from the directory with the *.tar.gz* file
* The *train* and *test* directories contain training and test sets with the the class labels as sub-directories

**License**

Unclear.
