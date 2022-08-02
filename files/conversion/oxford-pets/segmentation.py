import cv2
import numpy as np
import os
import re
import shutil
import sys
from wai.annotations.image_utils import mask_to_polygon, polygon_to_lists
from wai.common.adams.imaging.locateobjects import LocatedObject, LocatedObjects
from wai.common.geometry import Polygon, Point
from wai.common.file.report import save as save_report
from shapely.geometry import Polygon as SPolygon

# determine cat categories (in xmls dir):
# grep ">cat<" *.xml | sed s/".xml:.*"//g | sed s/"_[0-9]*$"//g | sort -u
CATS = [
    "abyssinian",
    "bengal",
    "birman",
    "bombay",
    "british_shorthair",
    "egyptian_mau",
    "maine_coon",
    "persian",
    "ragdoll",
    "russian_blue",
    "siamese",
    "sphynx",
]


def to_polygon(located_object):
    """
    Turns the located object into a shapely polygon.

    :param located_object: the object to convert
    :type located_object: LocatedObject
    :return: the polygon
    :rtype: SPolygon
    """
    coords = []
    for point in located_object.get_polygon().points:
        coords.append((point.x, point.y))
    return SPolygon(coords)


def convert(input_dir, annotation_dir, output_dir, min_points=400, min_area_ratio=0.3, debug=False):
    """
    Generates bluechannel image segmentation and ADAMS instance segmentation annotations.

    :param input_dir: the image directory ("/some/where/images")
    :type input_dir: str
    :param annotation_dir: the directory with the trimaps ("/some/where/annotation/trimaps")
    :type annotation_dir: str
    :param output_dir: the output directory
    :type output_dir: str
    :param min_points: minimum number of points for polygon to be considered valid, use <=0 to accept any
    :type min_points: int
    :param min_area_ratio: the minimum ratio between polygon and bbox
    :type min_area_ratio: float
    :param debug: whether to output debugging information
    :type debug: bool
    """
    pattern = re.compile("([a-zA-Z_]+)_[0-9]+.jpg")
    bluechannel_dir = os.path.join(output_dir, "bluechannel")
    if not os.path.exists(bluechannel_dir):
        os.makedirs(bluechannel_dir)
    adams_dir = os.path.join(output_dir, "adams")
    if not os.path.exists(adams_dir):
        os.makedirs(adams_dir)
    count = 0
    invalid_blue = 0
    invalid_adams = 0
    for f in sorted(os.listdir(input_dir)):
        if not f.endswith(".jpg"):
            continue
        img_file_in = os.path.join(input_dir, f)
        ann_file_in = os.path.join(annotation_dir, f.replace(".jpg", ".png"))
        if not os.path.exists(ann_file_in):
            print("Missing annotation: %s" % f)
            invalid_blue += 1
            invalid_adams += 1
            continue
        # extract category
        match = pattern.match(f)
        category = match.group(1).lower()
        if category in CATS:
            category = "cat:" + category
        else:
            category = "dog:" + category
        # segmentation
        img_file_out = os.path.join(bluechannel_dir, f)
        ann_file_out = os.path.join(bluechannel_dir, f.replace(".jpg", ".png"))
        img = cv2.imread(ann_file_in)
        img = np.where(img == 1, 1, img)  # 1=yellow
        img = np.where(img == 2, 0, img)  # 2=blue
        img = np.where(img == 3, 1, img)  # 3=red
        cv2.imwrite(ann_file_out, img)
        shutil.copy(img_file_in, img_file_out)
        # adams
        img_file_out = os.path.join(adams_dir, f)
        ann_file_out = os.path.join(adams_dir, f.replace(".jpg", ".report"))
        img = cv2.imread(ann_file_in)
        img = np.where(img == 1, 255, img)  # 1=yellow
        img = np.where(img == 2, 0, img)  # 2=blue
        img = np.where(img == 3, 255, img)  # 3=red
        # remove any annotations on border to allow contour detection to succeed
        img = cv2.rectangle(img, (0, 0), (img.shape[1] - 1, img.shape[0] - 1), (0, 0, 0), 1)
        img = img/255.0
        poly = mask_to_polygon(img[:, :, 0], mask_threshold=0.9, mask_nth=1)
        if len(poly) > 0:
            poly_x, poly_y = polygon_to_lists(poly[0], swap_x_y=True)
            if (min_points > 0) and (len(poly_x) < min_points):
                print("Polygon too few points (%d < %d): %s" % (len(poly_x), min_points, f))
                invalid_adams += 1
                continue
            x0 = np.min(poly_x)
            x1 = np.max(poly_x)
            y0 = np.min(poly_y)
            y1 = np.max(poly_y)
            points = []
            for i in range(len(poly_x)):
                points.append(Point(poly_x[i], poly_y[i]))
            if debug:
                print("#points: %s = %d" % (f, len(poly_x)))
            lobj = LocatedObject(int(x0), int(y0), int(x1-x0+1), int(y1-y0+1))
            lobj.metadata["type"] = category
            lobj.set_polygon(Polygon(*points))
            spoly = to_polygon(lobj)
            area_ratio = spoly.area / lobj.get_rectangle().area()
            if debug:
                print("area ratio: %s = %f" % (f, area_ratio))
            if area_ratio < min_area_ratio:
                print("Area ratio too small (%f < %f): %s" % (area_ratio, min_area_ratio, f))
                invalid_adams += 1
                continue
            lobjs = LocatedObjects([lobj])
            report = lobjs.to_report()
            save_report(report, ann_file_out)
            shutil.copy(img_file_in, img_file_out)
        else:
            print("Failed to determine polygon outline: %s" % f)
        # progress
        count += 1
        if count % 100 == 0:
            print(count)

    print("Bluechannel (total/invalid): %d/%d" % (count, invalid_blue))
    print("ADAMS (total/invalid): %d/%d" % (count, invalid_adams))


input_dir = os.path.join(sys.argv[1], "images")
annotation_dir = os.path.join(sys.argv[1], "annotations/trimaps")
output_dir = sys.argv[2]
convert(input_dir, annotation_dir, output_dir)
