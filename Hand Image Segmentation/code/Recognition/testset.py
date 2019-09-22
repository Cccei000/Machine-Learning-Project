import os
import numpy as np
from PIL import Image
from scipy import ndimage

testdir = 'data/raw/test'
testlist = os.listdir(testdir)

def img_process(path):
    img_PIL = Image.open(path)
    img_np = np.array(img_PIL)
    img_np = img_np/img_np.max()
    img_np = ndimage.zoom(img_np,(1/6,1/8))
    return img_np

imglist = []

for filename in testlist:
    filepath = testdir+'/'+filename
    img = img_process(filepath)
    imglist.append(img)
    
img_file = np.array(imglist)
img_file.tofile('data/processed/test_img')