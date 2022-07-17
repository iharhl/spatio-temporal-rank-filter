import numpy as np
import time

######## SPATIOTEMPORAL RANK FILTER #########

def st_rank_filter(data,rank,size=3,bitrate=8): 
    '''
    Args:
        data - 3d numpy array \n
        rank - 0.0 to 1.0 \n
        size - only 3 (3x3 window)
    '''
    
    (t, w, h) = data.shape
    data_filt = np.zeros((w,h))

    if bitrate == 16:
        btype = np.uint16
    elif bitrate == 8:
        btype = np.uint8
    else:
        print("Bitrate of the image can only be 8 or 16")
        exit(1)

    rank = int(rank * t * size**2 - 1)
    if rank < 0:
        rank = 0

    
    # matrix = [[0]*(w-2) for i in range(h-2)]
    # start1 = time.perf_counter()
    # for i in range(w-2):
    #     for j in range(h-2):
    #         #- Extrude the 3x3xImages array from data and put into matrix
    #         matrix[i][j] = np.array([data[z][u][v] for z in range(0,t,1) for u in range(i,i+size,1) for v in range(j,j+size,1)])
    # end1 = time.perf_counter()

    # start2 = time.perf_counter()
    # for i in range(w-2):
    #     for j in range(h-2):
    #         #- Assing the central pixel with value which idx == rank
    #         data_filt[i+1][j+1] = np.sort(matrix[i][j])[rank]
    # end2 = time.perf_counter()

    # print(end1-start1)
    # print(end2-start2)

    for i in range(w-2):
        for j in range(h-2):

            # Fastest method so far
            data_filt[i+1][j+1] = np.sort(np.array([data[z][u][v] for z in range(0,t,1) for u in range(i,i+size,1) for v in range(j,j+size,1)]))[rank]
           
    return np.array(data_filt, dtype=btype)
    