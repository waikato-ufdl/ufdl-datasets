import csv
import cv2
import os
import numpy as np

LABELS_FILE = "./label_colors.txt"
IMAGE_DIR = "./701_StillsRaw_full"
ANNOTATION_DIR = "./LabeledApproved_full"
OUTPUT_DIR = "./bluechannel"
BLACKLIST = set(["Seq05VD_f02610.png", "Seq05VD_f02610_L.png"])


def to_hex(color):
    result = "#"
    color = color.copy()
    color.reverse()  # BGR -> RGB
    for i in range(len(color)):
        c_hex = hex(color[i])[2:]
        if len(c_hex) == 1:
            c_hex = "0" + c_hex
        result += c_hex
    return result


# load labels
print("\nReading %s..." % LABELS_FILE)
colors = dict()
colors_blue = dict()
labels = []
with open(LABELS_FILE, "r") as fp:
    i = 0
    for line in fp.readlines():
        i += 1
        line = line.strip().replace("\t\t", "\t")
        rgb, label = line.split("\t")
        color = [int(x) for x in rgb.split(" ")]
        color.reverse()  # RGB -> BGR
        colors[label] = color
        colors_blue[label] = (i, 0, 0)  # BGR
        labels.append(label)
print("%d label colors read" % len(colors))
with open(OUTPUT_DIR + "/labels.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow(["label", "color_old", "color_new"])
    for label in labels:
        writer.writerow([label, to_hex(colors[label]), to_hex(list(colors_blue[label]))])

# convert images
print("\nConverting images to JPG...")
files = os.listdir(IMAGE_DIR)
files.sort()
for f in files:
    if not f.endswith(".png"):
        continue
    if f in BLACKLIST:
        print("Skipping blacklisted file: %s" % f)
        continue
    print(f)
    img = cv2.imread(os.path.join(IMAGE_DIR, f))
    cv2.imwrite(os.path.join(OUTPUT_DIR, os.path.splitext(f)[0] + ".jpg"), img)

# convert annotations
print("\nConverting annotations to bluechannel PNG...")
files = os.listdir(ANNOTATION_DIR)
files.sort()
for f in files:
    if not f.endswith(".png"):
        continue
    if f in BLACKLIST:
        print("Skipping blacklisted file: %s" % f)
        continue
    print(f)
    img = cv2.imread(os.path.join(ANNOTATION_DIR, f))
    for i, label in enumerate(labels, start=1):
        img[np.all(img == colors[label], axis=-1)] = colors_blue[label]
    unique, counts = np.unique(img, return_counts=True)
    if np.max(unique) > len(labels):
        print(unique)
        print(counts)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f.replace("_L.png", ".png")), img)
