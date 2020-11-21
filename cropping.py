# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:43:04 2019

@author: Talha Bilal
"""

from PIL import Image
import cv2
import numpy as np
'''img = cv2.imread('C:\\Users\\Talha Bilal\\Desktop\\Braintumor\\validation\\images\\2.0---90284-i873.bmp',1)
crop_img = img[163:241, 256:335]
cv2.imshow("image",crop_img)
cv2.imwrite('C:\\Users\\Talha Bilal\\Desktop\\New folder (3)\\mengomia\\g20.jpg',crop_img)
cv2.waitKey(0)'''
img = cv2.imread('D:\\DIPA_Brain_DataSet\\Orignal\\m20.jpg',1)
cv2.imwrite('D:\\DIPA_Brain_DataSet\\Orignal\\m20.bmp',img)
cv2.waitKey(0)