import os
import numpy as np
from PIL import Image
from scipy import ndimage

negativedir = 'data/raw/negative'
positivedir = 'data/raw/positive'
negativelist = os.listdir(negativedir)
positivelist = os.listdir(positivedir)

def img_process(path):
    img_PIL = Image.open(path)
    img_np = np.array(img_PIL)
    img_np = img_np/img_np.max()
    img_np = ndimage.zoom(img_np,(1/6,1/8)) 
    return img_np

imglist = []
labellist = []

for dirname in negativelist:
    dirpath = negativedir+'/'+dirname
    filelist = os.listdir(dirpath)
    for filename in filelist:
        img = img_process(dirpath+'/'+filename)
        imglist.append(img)
        labellist.append(0)

for dirname in positivelist:
    dirpath = positivedir+'/'+dirname
    filelist = os.listdir(dirpath)
    for filename in filelist:
        img = img_process(dirpath+'/'+filename)
        imglist.append(img)
        labellist.append(1)

img_file = np.array(imglist)
img_file.tofile('data/processed/train_img')
label_file = np.array(labellist)
label_file.tofile('data/processed/train_label')