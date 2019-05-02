# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:32:11 2018

@author: MSI
"""
import cv2 
import numpy as np
import glob 
import os

positive_path = 'positive/rawdata'
negative_path = 'negative'

labels = []    
samples = []
bin_n = 16 # Number of bins

def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bins = np.int32(bin_n*ang/(2*np.pi))    # quantizing binvalues in (0...16)
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)     # hist is a 64 bit vector
    return hist

# Get positive samples
for filename in glob.glob(os.path.join(positive_path, '*.bmp')):
    img = cv2.imread(filename, 1)
    hist = hog(img)
    samples.append(hist)
    labels.append(1)

# Get negative samples
for filename in glob.glob(os.path.join(negative_path, '*.jpg')):
    img = cv2.imread(filename, 1)
    hist = hog(img)
    samples.append(hist)
    labels.append(0)

# Convert objects to Numpy Objects
samples = np.float32(samples)
labels = np.array(labels)


# Shuffle Samples
rand = np.random.RandomState(321)
shuffle = rand.permutation(len(samples))
samples = samples[shuffle]
labels = labels[shuffle]    

# Create SVM classifier
svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_RBF) # cv2.ml.SVM_LINEAR
# svm.setDegree(0.0)
svm.setGamma(5.383)
# svm.setCoef0(0.0)
svm.setC(2.67)
# svm.setNu(0.0)
# svm.setP(0.0)
# svm.setClassWeights(None)

# Train
svm.train(samples, cv2.ml.ROW_SAMPLE, labels)
svm.save('svm_data.dat')