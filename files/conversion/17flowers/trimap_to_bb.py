import cv2
import numpy as np
import glob

# load image
pngFilenamesList = glob.glob('./trimaps/*.png')
output_folder = "./voc"
map = {0:"Daffodil",1:"Snowdrop",2:"LilyValley",3:"Bluebell",4:"Crocus",5:"Iris",6:"Tigerlily",7:"Tulip",8:"Fritillary",9:"Sunflower",10:"Daisy",11:"Dandelion",12:"ColtsFoot",13:"Cowslip",14:"Buttercup",15:"Windflower",16:"Pansy"}

for f in pngFilenamesList:
    s_imgnum = f[-8:-4]
    n_imgnum = int(s_imgnum)
    n_class = n_imgnum // 80
    s_class = map[n_class]
    s_filename = "image_"+s_imgnum+".jpg"
    new_filename = "image_"+s_imgnum+".xml"
    new_full_filename = output_folder+"/"+new_filename
    print(f)
    print(n_class)
    print(s_class)
    img = cv2.imread(f);
    height, width, channels = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    thresh = cv2.inRange(gray, 30, 55);

    # contour
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
    #find biggest, w*h
    maxa = -1
    fx1 = 10000
    fy1 = 10000
    fx2 = 0
    fy2 = 0
    for c in contours:
        x,y,w,h = cv2.boundingRect(c);
        if w*h < 20:
            continue
        if w*h > maxa:
            maxa = w*h
            fx=x;
            fy=y;
            fw=w;
            fh=h;
        if x < fx1:
            fx1 = x
        if y < fy1:
            fy1 = y
        if x+w > fx2:
            fx2 = x+w
        if y+h > fy2:
            fy2 = y+h
        w1 = fx2 - fx1
        h1 = fy2 - fy1
    
    cv2.rectangle(img,(fx,fy),(fx+fw,fy+fh),(0,255,0),2);
    cv2.rectangle(img,(fx1,fy1),(fx1+w1,fy1+h1),(0,0,255),2);

    # show
    cv2.imshow("Thresh", thresh);

    # make voc
    annot = "<annotation>\n"
    annot += "\t<folder></folder>\n"
    annot += "\t<filename>"+s_filename+"</filename>\n"
    annot += "\t<path>"+s_filename+"</path>\n"
    annot += "\t<source>\n"
    annot += "\t\t<database>Unknown</database>\n"
    annot += "\t</source>\n"
    annot += "\t<size>\n"
    annot += "\t\t<width>"+str(width)+"</width>\n"
    annot += "\t\t<height>"+str(height)+"</height>\n"
    annot += "\t\t<depth>3</depth>\n"
    annot += "\t</size>\n"
    annot += "\t<segmented>0</segmented>\n"
    annot += "\t<object>\n"
    annot += "\t\t<name>"+s_class+"</name>\n"
    annot += "\t\t<pose>0</pose>\n"
    annot += "\t\t<truncated>0</truncated>\n"
    annot += "\t\t<difficult>0</difficult>\n"
    annot += "\t\t<occluded>0</occluded>\n"
    annot += "\t\t<bndbox>\n"
    annot += "\t\t\t<xmin>"+str(fx1)+"</xmin>\n"
    annot += "\t\t\t<xmax>"+str(fx1+w1)+"</xmax>\n"
    annot += "\t\t\t<ymin>"+str(fy1)+"</ymin>\n"
    annot += "\t\t\t<ymax>"+str(fy1+h1)+"</ymax>\n"
    annot += "\t\t</bndbox>\n"
    annot += "\t</object>\n"
    annot += "</annotation>\n"

    with open(new_full_filename, 'w') as f:
        f.write(annot)

