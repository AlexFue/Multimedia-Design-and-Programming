#created by alex espinoza and eric chavez 
#last modified 2/16/20
#this code takes transforms data into tuples and counts how many times each rgb value appears from 0 - 255
import pickle as pkl
from PIL import Image
import numpy as np
#import hist_machine as hp
file = open('image_matrix', 'rb')
pixel_list = pkl.load(file)
def task2(pixel_list):
    red_list = []
    green_list = []
    blue_list = []
    img = Image.fromarray(np.uint8(pixel_list), 'RGB')
    width, height = img.size
    # puts zeros in the lists before we check the counts 
    for i in range(0, 256):
        red_list.append(0)
        green_list.append(0)
        blue_list.append(0)
# checks the rgb values to count if it is in a section 0 - 255 
    for i in range(height):
        for j in range(width):
            for z in range(0, 256):
                if pixel_list[i][j][0] == z:
                    red_list[z] += 1
                if pixel_list[i][j][1] == z:
                    green_list[z] += 1
                if pixel_list[i][j][2] == z:
                    blue_list[z] += 1
    return red_list, green_list, blue_list
print(task2(pixel_list))
#hp.hist_plotter(task2(file))
