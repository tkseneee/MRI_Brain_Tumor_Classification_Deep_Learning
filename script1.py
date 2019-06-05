# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:15:42 2019

@author: senthilku
"""
import numpy as np
import h5py 
import cv2

import glob
d=1
lab=[]
for filename in glob.glob('D:/Brain_MRI/part1/*.mat'):
    f = h5py.File(filename,'r') 
    data = f.get('cjdata')
    #im1=data.get('image')
    #im=np.array(im1)
    mask1=data.get('tumorMask')
    mask=np.array(mask1)
    ret,thresh1 = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
    cv2.imwrite("jpeg_images/part1/img_%d.jpg"%d,thresh1)
    d=d+1
    lab1=data.get('label')
    lab.append(np.array(lab1))

label_part1=np.array(lab)
label_part1=np.squeeze(label_part1)
np.save('D:/Brain_MRI/labels/label_part1.npy',label_part1)
 

d=767
lab=[]
for filename in glob.glob('D:/Brain_MRI/part2/*.mat'):
    f = h5py.File(filename,'r') 
    data = f.get('cjdata')
    #im1=data.get('image')
    #im=np.array(im1)
    mask1=data.get('tumorMask')
    mask=np.array(mask1)
    ret,thresh1 = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
    cv2.imwrite("jpeg_images/part2/img_%d.jpg"%d,thresh1)
    d=d+1
    lab1=data.get('label')
    lab.append(np.array(lab1))

label_part2=np.array(lab)
label_part2=np.squeeze(label_part2)
np.save('D:/Brain_MRI/labels/label_part2.npy',label_part2)


d=1533
lab=[]
for filename in glob.glob('D:/Brain_MRI/part3/*.mat'):
    f = h5py.File(filename,'r') 
    data = f.get('cjdata')
    #im1=data.get('image')
    #im=np.array(im1)
    mask1=data.get('tumorMask')
    mask=np.array(mask1)
    ret,thresh1 = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
    cv2.imwrite("jpeg_images/part3/img_%d.jpg"%d,thresh1)
    d=d+1
    lab1=data.get('label')
    lab.append(np.array(lab1))

label_part3=np.array(lab)
label_part3=np.squeeze(label_part3)
np.save('D:/Brain_MRI/labels/label_part3.npy',label_part3)
 

d=2299
lab=[]
for filename in glob.glob('D:/Brain_MRI/part4/*.mat'):
    f = h5py.File(filename,'r') 
    data = f.get('cjdata')
    #im1=data.get('image')
    #im=np.array(im1)
    mask1=data.get('tumorMask')
    mask=np.array(mask1)
    ret,thresh1 = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
    cv2.imwrite("jpeg_images/part4/img_%d.jpg"%d,thresh1)
    d=d+1
    lab1=data.get('label')
    lab.append(np.array(lab1))

label_part4=np.array(lab)
label_part4=np.squeeze(label_part4)
np.save('D:/Brain_MRI/labels/label_part4.npy',label_part4)

tumor_label=np.concatenate((label_part1,label_part2,
                            label_part3,label_part4),axis=0)
import pandas as pd
df=pd.DataFrame(tumor_label)
df.to_csv('tumor_label.csv')
 
#f = h5py.File('1.mat','r') 
#data = f.get('cjdata')
#    #im1=data.get('image')
#    #im=np.array(im1)
#mask1=data.get('tumorMask')
#mask=np.array(mask1)
#ret,thresh1 = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
#
#lab=data.get('label')
#lab=np.array(lab)
