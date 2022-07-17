import numpy as np
from glob import glob
from matplotlib import pyplot as plt
import png
from PIL import Image
import STRfilter
import time

import os
path = os.path.abspath(os.getcwd())

def loadImgArr(folder):
    '''
    Args:   name of folder with .png files
    Return: np array of arrays with pixel grayscale values 
    '''
    imgArr = []
    for filename in glob(f"{path}/{folder}/*.png"): 
        imgArr.append(np.array(Image.open(filename)))
    return np.array(imgArr)

def saveImage(name,gray,pixels):
    '''
    Args:
        name    - name of the image \n
        gray    - np array of grayscale values \n
        pixels  - resolution of the picture (pixels x pixels)
    '''
    if not gray.shape == (pixels,pixels):
        gray = np.reshape(gray, (pixels, pixels))

    with open(name, 'wb') as f:
        writer = png.Writer(width=gray.shape[1], height=gray.shape[0], bitdepth=8, greyscale=True)
        gray_list = gray.tolist()
        writer.write(f, gray_list)


def showImg(imgArr, no, grayMax=255, imgTitle=None):
    '''
    Args:
        imgArr   - array of images to plot (8-bit)
        no       - number of images to plot (from 2 to 4)  
        imgTitle - array of image titles
    '''

    if imgTitle is None:
        imgTitle = []
        for i in range(no):
            imgTitle.append(' ')

    if no == 1:
        plt.imshow(imgArr[0],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[0])
        plt.xticks([]), plt.yticks([])
        plt.show()
    elif no == 2:
        plt.subplot(121),plt.imshow(imgArr[0],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[0])
        plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(imgArr[1],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[1])
        plt.xticks([]), plt.yticks([])
        plt.show()
    elif no == 3:
        plt.subplot(131),plt.imshow(imgArr[0],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[0])
        plt.xticks([]), plt.yticks([])
        plt.subplot(132),plt.imshow(imgArr[1],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[1])
        plt.xticks([]), plt.yticks([])
        plt.subplot(133),plt.imshow(imgArr[2],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[2])
        plt.xticks([]), plt.yticks([])
        plt.show()
    elif no == 4:
        plt.subplot(141),plt.imshow(imgArr[0],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[0])
        plt.xticks([]), plt.yticks([])
        plt.subplot(142),plt.imshow(imgArr[1],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[1])
        plt.xticks([]), plt.yticks([])
        plt.subplot(143),plt.imshow(imgArr[2],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[2])
        plt.xticks([]), plt.yticks([])
        plt.subplot(144),plt.imshow(imgArr[3],cmap='gray',vmin=0,vmax=grayMax),plt.title(imgTitle[3])
        plt.xticks([]), plt.yticks([])
        plt.show()
    else:
        print("ERROR < Number of images should be between 2 and 4 >")

def main():
    array = np.array(loadImgArr("img"))

    # start = time.perf_counter()
    filt_image = STRfilter.st_rank_filter(array, 0.5)
    # end = time.perf_counter()
    # print(end-start)

    showImg([filt_image],1)

main()