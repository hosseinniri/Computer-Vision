import cv2
import numpy as np

I = cv2.imread('polygons.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

ret, T = cv2.threshold(G,220,255,cv2.THRESH_BINARY_INV)

nc1,CC1 = cv2.connectedComponents(T)

for k in range(1,nc1):

    Ck = np.zeros(T.shape, dtype=np.float32)
    Ck[CC1 == k] = 1;
    Ck = cv2.GaussianBlur(Ck,(5,5),0)
    #Ck = cv2.cvtColor(Ck,cv2.COLOR_GRAY2BGR)

    # Now, apply corner detection on Ck
    G = np.float32(Ck)
    window_size = 6
    soble_kernel_size = 3  # kernel size for gradients
    alpha = 0.04
    H = cv2.cornerHarris(G, window_size, soble_kernel_size, alpha)

    # normalize C so that the maximum value is 1
    H = H / H.max()

    # C[i,j] == 255 if H[i,j] > 0.01, and C[i,j] == 0 otherwise
    C = np.uint8(H > 0.01) * 255

    ## connected components
    nc2, CC2 = cv2.connectedComponents(C);
    n = nc2-1

    
    font = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(Ck,'There are %d vertices!'%(n),(20,30), font, 1,(255,255,255),1)

    
    cv2.imshow('corners',Ck)
    cv2.waitKey(0) # press any key



