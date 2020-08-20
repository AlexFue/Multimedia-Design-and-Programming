#Authors: Prince Rios and Alex Espinoza
#Last modified: 8 March 2020
#Description: This program uses a class to create a GUI that allows a user to enter text into a box and search for an image
#using QLineEdit. There is also a QPushButton in the gui to allow the user to search for the image. Once the user clicks the 
#search button, the image they chose is displayed in a new window, which has a combo box under the iamge to allow the user to
#choose between a sepia, negative, grayscale, or thumbnail version of the image.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow
# from task2 import Window
from PyQt5.QtGui import QPixmap
import PIL.Image
# from PIL import Image
# self.im = PIL.Image.open('34694102243_3370955cf9_z.jpg')
# self.im.show()
class Image(QWidget):
	def __init__(self):
		super().__init__()
		self.UI()
		self.show()
	def UI(self):
		self.setGeometry(500, 300, 200, 100)
		self.setWindowTitle('Image Search')
		self.InitUI()
		self.show()
	def InitUI(self):
		# Label, Line Edit, and Push button created in this function.
		self.label = QLabel(self)
		self.label.setText('Search by id, title, flickr user, or tag')
		self.search_button = QPushButton(self)
		self.search_button.setText('Search')
		self.line_edit = QLineEdit(self)
		vbox = QVBoxLayout()
		vbox.addWidget(self.label)
		vbox.addWidget(self.line_edit)
		vbox.addWidget(self.search_button)
		self.setLayout(vbox)
		self.show()
		self.search_button.clicked.connect(self.btn_clicked)
	# Function created to show image once the button is clicked
	def btn_clicked(self):
		ls = ['Sepia', 'Negative', 'Grayscale', 'Thumbnail', 'None']
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
		# this just sets all the layouts for the guis and get the pictures from the folder
		self.new_window = QWidget()
		self.new_window.setGeometry(0, 0, 600, 600)
		self.label2 = QLabel(self.new_window)
		new_list = self.line_edit.text().split()
		for i in range(len(new_list)):
			new_list[i] = new_list[i].lower()
		for i in range(len(image_info)):
			for j in range(len(image_info[i]['tags'])):
				image_info[i]['tags'][j] = image_info[i]['tags'][j].lower()
		counter = 0
		tag_list = []
		for i in range(len(image_info)):
			for key, value in image_info[i].items():
				if key != 'tags' and self.line_edit.text().lower() == value.lower():
					self.img = image_info[i]["id"]
					self.image = QPixmap(f'{image_info[i]["id"]}.jpg')
				for j in range(len(new_list)):
					if new_list[j] in image_info[i]["tags"]:
						counter += 1
						if counter == 2:
							self.img = image_info[i]["id"]
							self.image = QPixmap(f'{image_info[i]["id"]}.jpg')
						else:
							self.img = image_info[i]["id"]
							self.image = QPixmap(f'{self.img}.jpg')
		self.label2.setPixmap(self.image)
		self.combo = QComboBox(self.new_window)
		for i, value in enumerate(ls):
			self.combo.addItem(value)
		self.combo.move(0, 477)
		self.label3 = QLabel(self.new_window)
		self.combo.currentTextChanged.connect(self.combo_change)
		self.new_window.show()
	#Function created to activate the designated image manipulation functions once the combo text is changed.
	def combo_change(self):
		text = self.combo.currentText()
		if text == 'Negative':
			self.negative()
		elif text == 'Grayscale':
			self.grayscale()
		elif text == 'Thumbnail':
			self.thumbnail()
		elif text == 'Sepia':
			self.sepia()
	# functions are just to convert image to whatever colors 
	def negative(self):
		self.im = PIL.Image.open(f'{self.img}.jpg')
		new_list = []
		for p in self.im.getdata():
 			temp = (int(p[0]*.5), p[1], p[2])
 			new_list.append(temp)
		self.im.putdata(new_list)
		# self.im.save(f'negative_{self.img}.jpg')
		self.im.show()
	def grayscale(self):
		self.im = PIL.Image.open(f'{self.img}.jpg')
		new_list = map(lambda a : (int((a[0]+a[1]+a[2])/3),) * 3, self.im.getdata())
		self.im.putdata(list(new_list))
		# self.im.save(f'grayscale_{self.img}.jpg')
		self.im.show()
	def thumbnail(self):
		self.im = PIL.Image.open(f'{self.img}.jpg')
		self.xcenter = self.im.width/2
		self.ycenter = self.im.height/2
		self.x1 = self.xcenter - 100
		self.y1 = self.ycenter - 100
		self.x2 = self.xcenter + 100
		self.y2 = self.ycenter + 100
		self.cropped = self.im.crop((self.x1, self.y1, self.x2, self.y2))
		# self.cropped.save(f'thumbnail_{self.img}.jpg')
		self.cropped.show()
	#Attribution for sepia filter: Tessaracter from stack overflow
	def sepia(self):
		self.im = PIL.Image.open(f'{self.img}.jpg')
		self.width, self.height = self.im.size
		self.pixels = self.im.load() # create the pixel map
		for y in range(self.height):
			for x in range(self.width):
				r, g, b = self.im.getpixel((x, y))
				tr = int(0.393 * r + 0.769 * g + 0.189 * b)
				tg = int(0.349 * r + 0.686 * g + 0.189 * b)
				tb = int(0.272 * r + 0.534 * g + 0.131 * b)
				if tr > 255:
					tr = 255
				if tg > 255:
					tg = 255
				if tb > 255:
					tb = 255
				self.pixels[x, y] = (tr, tg, tb)
		self.im.show()
app = QApplication(sys.argv)

image = Image()

sys.exit(app.exec_())