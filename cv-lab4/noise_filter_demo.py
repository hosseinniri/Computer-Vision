import numpy as np
import cv2

I = cv2.imread('branches2.jpg').astype(np.float64) / 255

noise_sigma = 0.04  # initial standard deviation of noise

m = 5  # initial filter size,

gm = 5  # gaussian filter size

size = 5  # bilateral filter size
sigmaColor = 0.3
sigmaSpace = 75

# with m = 1 the input image will not change
filter = 'b'  # box filter

while True:

    # add noise to image
    N = np.random.rand(*I.shape) * noise_sigma
    N=N.astype(np.float32)
    J = I + N
    J=J.astype(np.float32)

    if filter == 'b':
        K=cv2.blur(J,(m,m))
    elif filter == 'g':
        # filter with a Gaussian filter
        K=cv2.GaussianBlur(J,(gm,gm),0)
    elif filter == 'l':
        # filter with a bilateral filter
        K=cv2.bilateralFilter(J,size, sigmaColor, sigmaSpace)

    # filtered image

    cv2.imshow('demo ', K)
    key = cv2.waitKey(30) & 0xFF

    if key == ord('b'):
        filter = 'b'  # box filter
        print('Box filter')

    elif key == ord('g'):
        filter = 'g'  # filter with a Gaussian filter
        print('Gaussian filter')

    elif key == ord('l'):
        filter = 'l'  # filter with a bilateral filter
        print('Bilateral filter')

    elif key == ord('+'):
        # increase m
        m = m + 2
        print('m=', m)

    elif key == ord('-'):
        # decrease m
        if m >= 3:
            m = m - 2
        print('m=', m)
    elif key == ord('u'):
        # increase noise
        noise_sigma=noise_sigma+0.1
        print('noise sigma=',noise_sigma)
    elif key == ord('d'):
        # decrease noise
        if noise_sigma>=0.1:
            noise_sigma = noise_sigma - 0.1
        print('noise sigma=',noise_sigma)
    elif key == ord('p'):
        # increase gm
        gm=gm+2
        print('gm=',gm)
    elif key == ord('n'):
        # decrease gm
        if gm>=3:
            gm=gm-2
        print('gm=',gm)
    elif key == ord('>'):
        # increase size
        size=size+2
        print('size',size)
    elif key == ord('<'):
        # decrease size
        if size>=3:
            size=size-2
            print('size=',size)
    elif key==ord('w'):
         sigmaColor=sigmaColor+0.1
         print('sigmacolor=',sigmaColor)
    elif key==ord('s'):
         if(sigmaColor>=0.1):
             sigmaColor = sigmaColor - 0.1
             print('sigmacolor=', sigmaColor)
    elif key == ord('q'):
        break  # quit

cv2.destroyAllWindows()
