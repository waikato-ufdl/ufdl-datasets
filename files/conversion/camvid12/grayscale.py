# classes:
# sky building pole road pavement tree signsymbol fence car pedestrian bicyclist unlabelled

import cv2
import numpy as np
import os
import shutil
import sys


def convert(in_dir_img, in_dir_ann, out_dir, combined_out_dir):
    for f in os.listdir(in_dir_img):
        if not f.endswith(".png"):
            continue
        print(f)
        # paths
        img_in = os.path.join(in_dir_img, f)
        img_out = os.path.join(out_dir, os.path.splitext(f)[0] + ".jpg")
        img_comb = os.path.join(combined_out_dir, os.path.splitext(f)[0] + ".jpg")
        ann_in = os.path.join(in_dir_ann, f)
        ann_out = os.path.join(out_dir, f)
        ann_comb = os.path.join(combined_out_dir, f)
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        # image
        img = cv2.imread(img_in)
        cv2.imwrite(img_out, img)
        # annotation
        shutil.copy(ann_in, ann_out)
        # combined output dir
        if not os.path.exists(combined_out_dir):
            os.mkdir(combined_out_dir)
        shutil.copy(img_out, img_comb)
        shutil.copy(ann_out, ann_comb)


input_dir = os.path.join(sys.argv[1], "CamVid")
output_dir = sys.argv[2]
combined_output_dir = sys.argv[3]

img_dirs = ["train", "test", "val"]
annot_dirs = ["trainannot", "testannot", "valannot"]
out_dirs = ["train", "test", "val"]

for i in range(len(img_dirs)):
    print("--> %s/%s" % (img_dirs[i], annot_dirs[i]))
    convert(os.path.join(input_dir, img_dirs[i]), 
            os.path.join(input_dir, annot_dirs[i]), 
            os.path.join(output_dir, out_dirs[i]), 
            combined_output_dir)

