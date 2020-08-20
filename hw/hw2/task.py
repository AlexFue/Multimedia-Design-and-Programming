# Created by: Alex Espinoza and Prince Rios
# Assignment: Homework 2
# Summary: this code takes 11 images all the same but with one different object and removes that object to create a new image
# Refrences: Ivan Mendoza, Edward Cluster, Aundre Labrador

from PIL import Image
import glob
from math import floor

# creates the list for all the images
all_files = glob.glob("../../images/[0-9]*.png") 
im_data = []
car_images = []

# puts the images into a new list
new_image_data = []
for i in all_files:
    car_images.append(Image.open(i))

# gets the data of each image to put it in data image
for picture in car_images:
    im_data.append(list(picture.getdata()))

    # gets the height and width of the first image
image_width, image_heigth = car_images[1].size

# this gets the size to create the last image
middle = floor((len(car_images) + 1) / 2) - 1
print(middle)


# finds the middle value
for tuple in range(len(im_data[0])):
    each_tuple = []
    # saves the tuple value to use
    for image in range(len(im_data)):
        each_tuple.append(im_data[image][tuple])
        # sorting the tuples and taking the middle one, saving it to our new image data
    each_tuple.sort()
    new_image_data.append(each_tuple[middle])

# creating the new image
# using putdata() to put all the data from our array of data into the new image and then displaying it.
new_pic = Image.new("RGB", (image_width, image_heigth))
new_pic.putdata(new_image_data)
new_pic.show()
new_pic.save("new_save.png")


