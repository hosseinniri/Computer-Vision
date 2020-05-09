import cv2
import numpy as np
from matplotlib import pyplot as plt

fname = 'crayfish.jpg'
#fname = 'office.jpg'

img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

f, axes = plt.subplots(2, 3)

axes[0,0].imshow(img, 'gray', vmin=0, vmax=255)
axes[0,0].axis('off')

axes[1,0].hist(img.flatten(),256,[0,256]);




a=100
b=200

J = (img-a) * 255.0 / (b-a)
J[J < 0] = 0
J[J > 255] = 255
J = J.astype(np.uint8)

axes[0,1].imshow(J, 'gray', vmin=0, vmax=255)
axes[1,1].axis('off')

axes[1,1].hist(J.ravel(),256,[0,256]);

K = cv2.equalizeHist(img)
axes[0,2].imshow(K, 'gray', vmin=0, vmax=255)
axes[1,2].axis('off')
axes[1,2].hist(K.ravel(),256,[0,256]);



plt.show()


