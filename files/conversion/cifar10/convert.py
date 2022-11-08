import numpy as np
import os
import pickle

from PIL import Image


CLASSES = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]

BATCH_FILES = [
    "./cifar-10-batches-py/data_batch_1",
    "./cifar-10-batches-py/data_batch_2",
    "./cifar-10-batches-py/data_batch_3",
    "./cifar-10-batches-py/data_batch_4",
    "./cifar-10-batches-py/data_batch_5",
    "./cifar-10-batches-py/test_batch",
]


def unpickle(file):
    with open(file, 'rb') as fo:
        d = pickle.load(fo, encoding='bytes')
    return d


for batch_file in BATCH_FILES:
    print(batch_file)

    # output directory
    if "test_batch" in batch_file:
        out_dir = "./test"
    else:
        out_dir = "./train"

    # load data
    batch = unpickle(batch_file)
    labels = batch[b'labels']
    filenames = batch[b'filenames']
    data = batch[b'data']
    for i in range(data.shape[0]):
        act_out_dir = os.path.join(out_dir, CLASSES[labels[i]])
        if not os.path.exists(act_out_dir):
            os.makedirs(act_out_dir)
        out_file = os.path.join(act_out_dir, filenames[i].decode("utf-8"))
        img_array = data[i]
        img_data = np.reshape(img_array, (32, 32, 3), order='F')
        img = Image.fromarray(img_data, 'RGB')
        img = img.rotate(270)
        with open(out_file, "wb") as fp:
            img.save(fp)
        if (i+1) % 1000 == 0:
            print("%d / %d" % (i+1, data.shape[0]))
