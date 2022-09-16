.. title: Common Voice
.. slug: common-voice
.. date: 2022-09-08 11:10:51 UTC+12:00
.. tags: speech
.. category: speech-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/common-voice.png
   :alt: Common Voice logo
   :align: right

Speech datasets obtained from the `Common Voice <https://commonvoice.mozilla.org/en/datasets>`__ project:

* Dutch

  * `Common Voice (10.0-2022-07-04) </data/common-voice/cv-corpus-10.0-2022-07-04-nl.tar.gz>`__ (2.7GB)

* Japanese

  * `Common Voice (10.0-2022-07-04) </data/common-voice/cv-corpus-10.0-2022-07-04-ja.tar.gz>`__ (1.1GB)
  * `Coqui STT (10.0-2022-07-04) </data/common-voice/cv-corpus-10.0-2022-07-04-ja-coqui.tar.gz>`__ (1.8GB), `conversion </data/common-voice/cv-corpus-10.0-2022-07-04-ja-coqui.txt>`__

* Norwegian Nynorsk

  * `Common Voice (10.0-2022-07-04) </data/common-voice/cv-corpus-10.0-2022-07-04-nn-NO.tar.gz>`__ (18.5MB)
  * `Coqui STT (10.0-2022-07-04) </data/common-voice/cv-corpus-10.0-2022-07-04-nn-NO-coqui.tar.gz>`__ (1.8GB), `conversion </data/common-voice/cv-corpus-10.0-2022-07-04-nn-NO-coqui.txt>`__

Relevant datasets to use from the archives:

* Common Voice

  * ``train.tsv`` - the training set
  * ``dev.tsv`` - the validation set
  * ``test.tsv`` - the test set

* Coqui STT

  * ``train.csv`` - the training set
  * ``dev.csv`` - the validation set
  * ``test.csv`` - the test set

Conversion into other formats can be achieved with the `wai.annotations <https://github.com/waikato-ufdl/wai-annotations>`__ library.


**License**

`CC-0 <https://creativecommons.org/publicdomain/zero/1.0/>`__
