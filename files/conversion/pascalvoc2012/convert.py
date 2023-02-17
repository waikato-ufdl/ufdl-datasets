import numpy as np
import os
import shutil
import sys

from PIL import Image

# expects three arguments
# 1. JPEGImages dir
# 2. SegmentationClass dir
# 3. output directory for indexed dataset

if len(sys.argv) != 4:
    raise Exception("Expected parameters: <JPEGImages dir> <SegmentationClass dir> <output dir>")
for i in range(1, 4):
    if not os.path.exists(sys.argv[i]):
        raise Exception("Path does not exist: %s" % sys.argv[i])

jpeg_dir = sys.argv[1]
class_dir = sys.argv[2]
output_dir = sys.argv[3]

count = 0
for f in os.listdir(class_dir):
    if not f.endswith(".png"):
        continue
    count += 1
    class_file_in = os.path.join(class_dir, f)
    class_file_out = os.path.join(output_dir, f)
    jpeg_file_in = os.path.join(jpeg_dir, os.path.splitext(f)[0] + ".jpg")
    jpeg_file_out = os.path.join(output_dir, os.path.splitext(f)[0] + ".jpg")

    # copy jpeg
    shutil.copy(jpeg_file_in, jpeg_file_out)

    # fix png
    im = Image.open(class_file_in)
    palette = im.getpalette()
    indexed = np.array(im)

    # remove void labels (index 255)
    indexed[indexed == 255] = 0

    im_new = Image.fromarray(indexed)
    im_new.putpalette(palette)
    with open(class_file_out, "wb") as fp:
        im_new.save(fp)

    if (count % 100) == 0:
        print("Processed %d..." % count)

print("Total processed: %d" % count)
