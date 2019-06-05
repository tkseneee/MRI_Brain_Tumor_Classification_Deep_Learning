# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:58:44 2019

@author: senthilku
"""

import pandas as pd
import numpy as np
import os
import shutil

data=pd.read_csv('tumor_label1.csv')

id_1=data['Tumor Type']==1
data1=data.loc[id_1]

id_2=data['Tumor Type']==2
data2=data.loc[id_2]

id_3=data['Tumor Type']==3
data3=data.loc[id_3]

m1=list(data1['Img ID'])
m2=list(data2['Img ID'])
m3=list(data3['Img ID'])

src="D:/Brain_MRI/Complete_MRI_Brain_Data"
dst1="D:/Brain_MRI/Train/menigioma"
dst2="D:/Brain_MRI/Train/glioma"
dst3="D:/Brain_MRI/Train/pituitary"

for i in m1:
    fnam1=os.path.join(src, "img_%d.jpg"%i)
    shutil.move(fnam1, dst1)
for j in m2:
    fnam2=os.path.join(src, "img_%d.jpg"%j)
    shutil.move(fnam2, dst2)
for k in m3:
    fnam3=os.path.join(src, "img_%d.jpg"%k)
    shutil.move(fnam3, dst3)


r11=data1.sample(n=round(len(data1)*0.2))
r1=list(r11['Img ID'])
r22=data2.sample(n=round(len(data2)*0.2))
r2=list(r22['Img ID'])
r33=data3.sample(n=round(len(data3)*0.2))
r3=list(r33['Img ID'])
#import random
#r1=random.sample(range(1,len(data1)),round(len(data1)*0.2))
#r2=random.sample(range(len(data1),len(data1)+len(data2)),round(len(data2)*0.2))
#r3=random.sample(range(len(data1)+len(data2),len(data1)+len(data2)+len(data3)),round(len(data3)*0.2))

for i in r1:
    dst1="D:/Brain_MRI/Test/menigioma"
    src1="D:/Brain_MRI/Train/menigioma"
    fnam1=os.path.join(src1, "img_%d.jpg"%i)
    shutil.move(fnam1, dst1)
    
for j in r2:
    dst2="D:/Brain_MRI/Test/glioma"
    src2="D:/Brain_MRI/Train/glioma"
    fnam2=os.path.join(src2, "img_%d.jpg"%j)
    shutil.move(fnam2, dst2)

for k in r3:
    dst3="D:/Brain_MRI/Test/pituitary"
    src3="D:/Brain_MRI/Train/pituitary"
    fnam3=os.path.join(src3, "img_%d.jpg"%k)
    shutil.move(fnam3, dst3)    
   
#    dst2="D:/Brain_MRI/Test/glioma"
#    dst3="D:/Brain_MRI/Test/pituitary"
#    src="D:/Brain_MRI/Complete_MRI_Brain_Data"
#    fnam1=os.path.join(src, "img_%d.jpg"%i)
#    shutil.move(fnam1, dst1)
#    fnam2=os.path.join(src, "img_%d.jpg"%j)
#    shutil.move(fnam2, dst2)
#    fnam3=os.path.join(src, "img_%d.jpg"%k)
#    shutil.move(fnam3, dst3)
#import glob
#src="D:/Brain_MRI/jpeg_images/Complete_MRI_images/.*jpg"
#for 
#for filename in glob.glob((os.path.join(src, "img%d.jpg"%d)):):
    
    


