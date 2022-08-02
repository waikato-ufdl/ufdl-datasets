import os
import re
import shutil
import sys


def convert(input_dir, annotation_dir, output_dir):
    """
    Places the VOC xml files alongside the images, appends the actual category.

    :param input_dir: the image directory ("/some/where/images")
    :type input_dir: str
    :param annotation_dir: the directory with the XML annotations ("/some/where/annotation/xmls")
    :type annotation_dir: str
    :param output_dir: the output directory
    :type output_dir: str
    """
    pattern = re.compile("([a-zA-Z_]+)_[0-9]+.jpg")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    count = 0
    for f in os.listdir(input_dir):
        if not f.endswith(".jpg"):
            continue
        img_file_in = os.path.join(input_dir, f)
        ann_file_in = os.path.join(annotation_dir, f.replace(".jpg", ".xml"))
        if not os.path.exists(ann_file_in):
            print("Missing annotation: %s" % f)
            continue
        match = pattern.match(f)
        category = match.group(1).lower()
        img_file_out = os.path.join(output_dir, f)
        ann_file_out = os.path.join(output_dir, f.replace(".jpg", ".xml"))
        count += 1
        shutil.copy(img_file_in, img_file_out)
        with open(ann_file_in, "r") as fp:
            lines = fp.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("<name>cat</name>", "<name>cat:%s</name>" % category)
            lines[i] = lines[i].replace("<name>dog</name>", "<name>dog:%s</name>" % category)
        with open(ann_file_out, "w") as fp:
            fp.writelines(lines)
        if count % 100 == 0:
            print(count)


input_dir = os.path.join(sys.argv[1], "images")
annotation_dir = os.path.join(sys.argv[1], "annotations/xmls")
output_dir = os.path.join(sys.argv[2], "voc-head")
convert(input_dir, annotation_dir, output_dir)
