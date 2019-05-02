import cv2
import numpy as np
import glob,os
from digits import evaluate_model


labels = []
samples = []
SZ=20
bin_n = 16
positive_path = 'positive/rawdata'
negative_path = 'negative'

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

for filename in glob.glob(os.path.join(positive_path,'*.bmp')):
  img = cv2.imread(filename, 0)
  hist = hog(img)
  samples.append(hist)
  labels.append(1)

for filename in glob.glob(os.path.join(negative_path,'*.jpg')):
    img = cv2.imread(filename, 0)
    hist = hog(img)
    samples.append(hist)
    labels.append(0)

samples = np.float32(samples)
labels = np.array(labels)

svm = cv2.ml.SVM_create()
svm.setKernel(cv2.ml.SVM_RBF)
svm.setType(cv2.ml.SVM_C_SVC)
svm.setC(2.67)
svm.setGamma(5.383)

svm.train(samples, cv2.ml.ROW_SAMPLE, labels)
svm.save('svm_data.dat')
