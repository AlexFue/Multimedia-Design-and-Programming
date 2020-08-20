# Alex Espinoza-Fuentes and Prince Rios
# Last modified 4/11/20
# this code creates a web application that random generates 3 random 
# pictures and the user is allowed to pick each of the 3 to get more info 
# on it. the picture refresh each time you log back to the home page
from flask import Flask
from flask import Flask, render_template, url_for
import random
from PIL import Image
from flask_bootstrap import Bootstrap 

# allows app to run and formats it to Bootstrap
app = Flask(__name__)
Bootstrap(app)

# dictionary of the pictures
image_info = [
     {
           "id" : "34694102243_3370955cf9_z.jpg",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"]
      },
      {
           "id" : "37198655640_b64940bd52_z.jpg",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "36909037971_884bd535b1_z.jpg",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "36604481574_c9f5817172_z.jpg",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "36885467710_124f3d1e5d_z.jpg",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "37246779151_f26641d17f_z.jpg",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "36523127054_763afc5ed0_z.jpg",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "35889114281_85553fed76_z.jpg",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "34944112220_de5c2684e7_z.jpg",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "36140096743_df8ef41874_z.jpg",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]

# the home page
@app.route('/')
def home():
	lst = []
	rands = []
# loop gets 3 random numbers to get pictures 
	for i in range(3):
		x = random.randint(0,9)
		if x in rands:
			while x in rands:
				x = random.randint(0,9)
		# list of numbers already chose to not be chose again
		rands.append(x)
		# list of the 3 random pictures 
		lst.append(image_info[x])
	# sneds the information to the template
	return render_template('template.html', image = lst, dict = image_info)


# the info page of the picture
# this route sets it to the id of the picture
@app.route('/picture/<string:url>')
def picture(url):
	# loop gets the correct picture to access the info by testing if it matches the url
	for x in image_info:
		if url == x['id']:
			image = x
			break

	# opens the picture from folder and gets all the following 
	# information for the template
	im = Image.open('static/' + url)
	imformat = im.format
	immode = im.mode
	height = im.height
	width = im.width
	# sends the information to the info template
	return render_template('img_temp.html', image = image, url = url, height = height, width = width, mode = immode, format = imformat)




