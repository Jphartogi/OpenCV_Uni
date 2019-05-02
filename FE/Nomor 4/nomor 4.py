# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 13:10:05 2018

@author: MSI
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 12:45:12 2018

@author: MSI
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:28:12 2018

@author: MSI
"""

import cv2
import numpy as np
from SVM import hog
from digits import deskew

# Load the image
img_predict = cv2.imread('predict.jpeg', 0)

# Preprocessing: this image is inverted compared to the training data
# Here it is inverted back
img_predict = np.invert(img_predict)

# Preprocessing: it also has a completely different size
# This resizes it to the same size as the training data
img_predict = cv2.resize(img_predict, (20, 20), interpolation=cv2.INTER_CUBIC)

# Extract the features
img_predict_ready = np.float32(hog(deskew(img_predict)))

# Reload the trained svm
# Not necessary if predicting is done in the same session as training
svm = cv2.ml.SVM_create()
svm.load("svm_data.dat")

# Run the prediction
prediction = svm.predict(img_predict_ready)
print int(prediction)