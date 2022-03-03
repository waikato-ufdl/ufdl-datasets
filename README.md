# ufdl-datasets
Nikola website making the UFDL datasets publicly available.

The generated site is available here:

https://datasets.cms.waikato.ac.nz/ufdl/


## Installation

For developing the site locally:

* create virtual environment

  ```
  virtualenv -p /usr/bin/python3 venv
  ```

* install Nikola

  ```
  ./venv/bin/pip install nikola aiohttp watchdog
  ```

## Adding content

* [Nikola handbook](https://getnikola.com/handbook.html)
* Content is written in [reStructured Text](http://docutils.sourceforge.net/rst.html)
* Pages are located in `pages`
* News items (aka blog posts) are located in `posts`; should have a date prefix in the name

### How to add/list datasets

* `datasets.cms.waikato.ac.nz/var/www/html/ufdl/data/`

  * `raw` - for the original data
  * `conversion` - any data/script/etc that is required for converting the original data into the downloadable one
  * use the same sub-directory in `raw`, `conversion` and the various domain directories 
  * add `LINK` text file to original dataset in the `raw` and various domain directories

* Update the relevant pages:

  * `index.rst` - contains links to domain pages that list/link the actual datasets
  * `image-classification.rst` - page for listing image classification datasets
  * `object-detection.rst` - page for listing object detection datasets

* Deploy the site


### How to announce datasets

* Add a news item in the `posts` directory (`YYYY-MM-DD-title-of-post.rst`)
* Deploy the site 


## Serving

The following command not only serves the website on `localhost:8000`, but also detects changes 
in files and automatically rebuilds the website:

```
./venv/bin/nikola auto
```

## Deploying

Use the following command to build and deploy the website:

```
rm -R output && ./venv/bin/nikola clean && ./venv/bin/nikola build && ./venv/bin/nikola deploy
```
