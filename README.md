# ufdl-datasets
Nikola website making the UFDL datasets publicly available.

## Generation

### Requirements

* Nikola (>= 8.0.3)


### Installation

* create virtual environment

  ```
  virtualenv -p /usr/bin/python3 venv
  ```

* install Nikola

  ```
  ./venv/bin/pip install nikola aiohttp watchdog
  ```

### Adding content

* [Nikola handbook](https://getnikola.com/handbook.html)
* Content is written in [reStructured Text](http://docutils.sourceforge.net/rst.html)
* Pages are located in `pages`
* News items (aka blog posts) are located in `posts`; should have a date prefix in the name

### Serving

The following command not only serves the website on `localhost:8000`, but also detects changes 
in files and automatically rebuilds the website:

```
./venv/bin/nikola auto
```

### Deploying

Use the following command to build and deploy the website:

```
rm -R output && ./venv/bin/nikola clean && ./venv/bin/nikola build && ./venv/bin/nikola deploy
```
