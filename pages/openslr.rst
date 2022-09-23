.. title: Open Speech and Language Resources (OpenSLR)
.. slug: openslr
.. date: 2022-09-23 14:13:51 UTC+12:00
.. tags: speech
.. category: speech-dataset
.. link: 
.. description: 
.. type: text
.. hidetitle: True

.. image:: /images/openslr.png
   :alt: OpenSLR logo
   :height: 100px
   :align: right

Speech datasets obtained from the `OpenSRL <http://openslr.org/>`__ project:

* Javanese

  * `Source <http://openslr.org/41/>`__
  * Original: `jv_id_female.zip </data/openslr/jv_id_female.zip>`__ (48kHz, 967MB), `jv_id_male.zip </data/openslr/jv_id_male.zip>`__ (48kHz, 923MB), `convert.sh </conversion/openslr/convert.sh>`__
  * `Festvox </data/openslr/slr41-festvox.tar.gz>`__ (48kHz, 1.9GB)
  * `Coqui STT </data/openslr/slr41-coqui.tar.gz>`__ (16kHz, 655MB)

Notes on the archives:

* Festvox

  * ``annotations.txt`` - the annotations

* Coqui STT

  * ``samples.csv`` - the annotations

Conversion into other formats can be achieved with the `wai.annotations <https://github.com/waikato-ufdl/wai-annotations>`__ library.


**License**

`CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`__
