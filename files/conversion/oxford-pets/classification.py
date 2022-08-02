import os
import re
import shutil
import sys


def convert(input_dir, output_dir):
    """
    Extracts the category from the image filename and copies the image
    into the appropriate output directory (creates it if necessary).

    :param input_dir: the input directory ("/some/where/images")
    :type input_dir: str
    :param output_dir: the output directory
    :type output_dir: str
    """
    pattern = re.compile("([a-zA-Z_]+)_[0-9]+.jpg")
    count = 0
    for f in os.listdir(input_dir):
        if not f.endswith(".jpg"):
            continue
        count += 1
        match = pattern.match(f)
        category = match.group(1).lower()
        sub_dir = os.path.join(output_dir, category)
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)
        shutil.copy(os.path.join(input_dir, f), os.path.join(sub_dir, f))
        if count % 100 == 0:
            print(count)


input_dir = os.path.join(sys.argv[1], "images")
output_dir = os.path.join(sys.argv[2], "subdir")
convert(input_dir, output_dir)
