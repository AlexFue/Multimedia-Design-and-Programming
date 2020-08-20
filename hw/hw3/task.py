import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox,
                                QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image
import PIL.ImageOps

image_info = [
     {
           "id" : "34694102243_3370955cf9_z",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"]
      },
      {
           "id" : "37198655640_b64940bd52_z",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "36909037971_884bd535b1_z",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "36604481574_c9f5817172_z",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "36885467710_124f3d1e5d_z",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "37246779151_f26641d17f_z",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "36523127054_763afc5ed0_z",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "35889114281_85553fed76_z",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "34944112220_de5c2684e7_z",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "36140096743_df8ef41874_z",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]
manipulations = [False, False, False, False, False]
images = ['34694102243_3370955cf9_z.jpg', '34944112220_de5c2684e7_z.jpg', '35889114281_85553fed76_z.jpg', '36140096743_df8ef41874_z.jpg', '36523127054_763afc5ed0_z.jpg', '36604481574_c9f5817172_z.jpg', '36885467710_124f3d1e5d_z.jpg', '36909037971_884bd535b1_z.jpg', '37198655640_b64940bd52_z.jpg', '37246779151_f26641d17f_z.jpg']
        

class MyWindow(QWidget):
	def __init__(self):
		super().__init__()

		userinput = ""
		picture = QLabel(self)
		pixmap = QPixmap(images[9])
		#picture.setPixmap(pixmap)

		self.label1 = QLabel('Enter a word: ')
		self.line_edit = QLineEdit()
		self.enter = QPushButton("Enter")
		userinput = self.enter.clicked.connect(self.on_pushButtonOK_clicked)

		hbox1 = QHBoxLayout()
		hbox1.addWidget(self.label1)
		hbox1.addWidget(self.line_edit)
		hbox1.addWidget(self.enter)

		gbox1 = QGroupBox('Group Box 1')
		gbox1.setLayout(hbox1)

		self.label2 = QLabel('Image manipulations:')
		b1 = QPushButton('sepia')
		b1.clicked.connect(self.click_b1)
		b2 = QPushButton('negative')
		b2.clicked.connect(self.click_b2)
		b3 = QPushButton('grayscale')
		b3.clicked.connect(self.click_b3)
		b4 = QPushButton('thumbnail')
		b4.clicked.connect(self.click_b4)
		b5 = QPushButton('none')
		b5.clicked.connect(self.click_b5)

		hbox2 = QHBoxLayout()
		hbox2.addWidget(self.label2)

		hbox3 = QHBoxLayout()
		hbox3.addWidget(b1)
		hbox3.addWidget(b2)
		hbox3.addWidget(b3)
		hbox3.addWidget(b4)
		hbox3.addWidget(b5)

		vbox2 = QVBoxLayout()
		vbox2.addLayout(hbox2)
		vbox2.addLayout(hbox3)

		gbox2 = QGroupBox("Group Box 2")
		gbox2.setLayout(vbox2)

		mbox = QVBoxLayout()
		mbox.addWidget(gbox1)
		mbox.addWidget(gbox2)

		b = QPushButton("submit")
		b.clicked.connect(self.find_image)
		mbox.addWidget(b)
		mbox.addWidget(picture)

		self.setLayout(mbox)
		self.setWindowTitle("CST 205 App")


	#@pyqtSlot()
	def click_b1(self):
		manipulations[0] = True

	def click_b2(self):
		manipulations[1] = True

	def click_b3(self):
		manipulations[2] = True

	def click_b4(self):
		manipulations[3] = True

	def click_b5(self):
		manipulations[4] = True

	def on_pushButtonOK_clicked(self):
		global userinput 
		userinput = self.line_edit.text()
		return userinput

	def to_sepia(image):
		for p in image.getdata():
			if p[0] < 63:
				r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
			# tint midtones
			elif p[0] > 62 and p[0] < 192:
				r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
			# tint highlights
			else:
				r = int(p[0] * 1.08)
				if r > 255:
					r = 255
				g,b = p[1], int(p[2] * 0.5)
		#return r, g, b

	def to_grayscale(p):
		new_red = int(p[0] * 0.299)
		new_green = int(p[1] * 0.587)
		new_blue = int(p[2] * 0.114)
		lumi = new_red + new_green + new_blue
		return (lumi,) * 3

	def to_negative(p):
		return tuple(map(lambda a : 255 - a, pixel))
	# def to_thumbnail(self):

	def find_image(self):
		# picture = QLabel(self)
		for i in range(len(image_info)):
			for info in image_info[i]:
				if info == 'title':
					if userinput == image_info[i][info]:
						print(image_info[i][info])
						index_of_image = i
						im = Image.open(images[index_of_image])
						im.show()
						break
				if info == 'tags':
					for tag in range(len(image_info[i][info])):
						if userinput == image_info[i][info][tag]:
							print(image_info[i][info][tag])
							print(manipulations[2])
							index_of_image = i
							im = Image.open(images[index_of_image])
							for manip in range(len(manipulations)):
								if manipulations[manip] == True:
									#to_sepia(im)
									# for x in range(im.width()):
									# 	for y in range(im.height()):
									new_list = []
									for p in im.getdata():
										if p[0] < 63:
											temp = (int(p[0] * 1.1), p[1], int(p[2] * 0.9))
											new_list.append(temp)
											# r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
										# tint midtones
										elif p[0] > 62 and p[0] < 192:
											temp = (int(p[0] * 1.15), p[1], int(p[2] * 0.85))
											new_list.append(temp)
											# r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
										# tint highlights
										else:
											r = int(p[0] * 1.08)
											if r > 255:
												
												r = 255
											g,b = p[1], int(p[2] * 0.5)
											temp = (r, g, b)
											new_list.append(temp)
									im.putdata(list(new_list))
									im.show()
									break
								elif manipulations[manip] == True:
									for i in range(0, im.size[0]-1):
										for j in range(0, im.size[1]-1):
											# Get pixel value at (x,y) position of the image
											pixelColorVals = im.getpixel((i,j));
											# Invert color
											redPixel    = 255 - pixelColorVals[0]; # Negate red pixel
											greenPixel  = 255 - pixelColorVals[1]; # Negate green pixel
											bluePixel   = 255 - pixelColorVals[2]; # Negate blue pixel
											# Modify the image with the inverted pixel values
											im.putpixel((i,j),(redPixel, greenPixel, bluePixel));
											# to make sure it shows 
									im.show()
									break


								elif manipulations[manip] == True:
									new_list = []
									for p in im.getdata():
										new_red = int(p[0] * 0.299)
										new_green = int(p[1] * 0.587)
										new_blue = int(p[2] * 0.114)
										#lumi = new_red + new_green + new_blue
										#temp = (lumi)*3
										temp = (new_red, new_green, new_blue)
										new_list.append(temp)
									im.putdata(list(new_list))
									im.show()
									break

								# elif manipulations[manip] == True:

								# elif manipulations[manip] == True:

							
app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())





