import numpy as np
import cv2  
import matplotlib.pyplot as plt
import math
import os
#The focal length is 3740 pixels, and the baseline is 160mm
focal=3740
baseline=160

def calculateSSD(leftbloc,rightbloc):
    print(np.sum((leftbloc-rightbloc)**2))
    return np.sum((leftbloc-rightbloc)**2)

def getSimilairPoint(pix,bloc,right,premisse):
    minimumSSD=+math.inf
    simX=0
    i=premisse
    w_bloc=bloc.shape[1]
    h_bloc=bloc.shape[0]
    seuil=5
    for j in range(3,width-3):
        if(abs(pix-right[i][j])<seuil):
            debx=max(0,j- int(w_bloc/2))
            deby=max(0,i- int(h_bloc/2))
            finx=min(width,j+ int(w_bloc/2))
            finy=min(height,i+ int(h_bloc/2))
            #print(debx,"  ",finx)
            rightSSD=np.zeros((w_bloc,h_bloc),dtype=np.uint8)
            #print(rightSSD)
            rightSSD[:]=right[deby:finy+1,debx:finx+1]
            currentSSD=calculateSSD(bloc,rightSSD)
            #rint("cur ",currentSSD)
            if(currentSSD<minimumSSD):
                simX=j
                minimumSSD=currentSSD
    print("le min est: ",minimumSSD)
    return simX


def mouse_event(event,x,y,flags,param):
    new_left = np.copy(left)
    new_right = np.copy(right)
    '''debx=max(0,x- int(window_size/2))
    deby=max(0,y- int(window_size/2))
    finx=min(width,x+ int(window_size/2))
    finy=min(height,y+ int(window_size/2))'''
    
    if event==cv2.EVENT_LBUTTONDOWN:
        debx=max(0,x- int(window_size/2))
        deby=max(0,y- int(window_size/2))
        finx=min(width,x+ int(window_size/2))
        finy=min(height,y+ int(window_size/2))
        premisse=y
        pix=left[y][x]
        thisbloc=np.zeros((finy-deby+1,finx-debx+1),dtype=np.uint8)
        thisbloc[:]=new_left[deby:finy+1,debx:finx+1]
        rightX=getSimilairPoint(pix,thisbloc,new_right,premisse)
        rightY=premisse

        cv2.namedWindow('left')
        cv2.rectangle(new_left, (debx, deby), (finx, finy),(1, 0.5, 0.6),2)
        cv2.imshow('left', new_left)

        cv2.namedWindow('right')
        cv2.rectangle(new_right, (rightX, rightY), (rightX+5, rightY+5),(1, 0.5, 0.6),2)
        cv2.imshow('right', new_right)
        print(x,"---->",rightX)

        print(y,"---->",rightY)


'''

'''
window_size=9
resize_ratio=50
left  = cv2.imread("laundry/view0.png",0)
right = cv2.imread("laundry/view6.png",0)


width  = int(left.shape[1] * resize_ratio / 100)
height = int(left.shape[0] * resize_ratio / 100)
dim = (width, height)
left = cv2.resize(left, dim, interpolation = cv2.INTER_AREA)
right = cv2.resize(right, dim, interpolation = cv2.INTER_AREA)

cv2.imshow("left",left)
cv2.imshow("right",right)
cv2.setMouseCallback('left',mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
