#import the necessary packages
import argparse
import cv2
import numpy as np
import os
import uuid

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
ref_point = []
points=[]
cropping = False

b = (255,0,0)
g = (0,255,0)
r = (0,0,255)
p = (196,37,244)
colorlist=[r,g,b,p]

label = ["leftleft", "left", "right", "rightright"]

currentFrame=1
image = 0
#uuid_s = str(uuid.uuid4())[:5]

def shape_selection(event, x, y, flags, param):
	# grab references to the global variables
	global ref_point, cropping, image, colorlist

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed

	if event == cv2.EVENT_LBUTTONDOWN:
		cropping = True
	
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		ref_point.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.circle(image,(x,y),5, colorlist[len(points)] ,-1)
		cv2.imshow("image", image)

def load_video(cap):
	time_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	fps = cap.get(cv2.CAP_PROP_FPS)
	frame_seq = time_length * fps -1
	frame_no = (frame_seq / (time_length*fps))
	cap.set(2, frame_no)
	return cap

# load the image, clone it, and setup the mouse callback function
def load_image(image, image_path):
	if image_path =="":
		image = np.zeros((288,800,3), np.uint8)
	else:
		image = cv2.imread(image_path)
		image = cv2.resize(image, dsize=(800,288))

	clone = image.copy()
	cv2.namedWindow("image")
	cv2.setMouseCallback("image", shape_selection)
	return image, clone

def legend():
	global image, points
	image = cv2.rectangle(image, (670,5), (790, 85), (255,255,255), -1)
	image = cv2.circle(image, (680,10), 4, r,-1)
	image = cv2.circle(image, (680,25), 4, g,-1)
	image = cv2.circle(image, (680,40), 4, b,-1)
	image = cv2.circle(image, (680,55), 4, p,-1)
	image = cv2.putText(image, "lane1: leftleft", (689, 15), 0,0.4,(0,0,0))
	image = cv2.putText(image, "lane2: left", (689, 30), 0,0.4,(0,0,0))
	image = cv2.putText(image, "lane3: right", (689, 45), 0,0.4,(0,0,0))
	image = cv2.putText(image, "lane4: rightright", (689, 60), 0,0.4,(0,0,0))
	image = cv2.putText(image, "Now, "+label[len(points)], (675, 75), 0, 0.5, (0,0,0))
	
	image = cv2.rectangle(image, (3,5), (130, 25), (255,255,255), -1)
	image = cv2.putText(image, "Frame: "+str(currentFrame), (5, 18), 0, 0.5, (0,0,0))
	cv2.imshow("image",image)

# keep looping until the 'q' key is pressed
def annot(image_path, clone):
	global image, ref_point, points #, uuid_s
	
	points=[]
	while True:
		count = []
		for laneType in label:
			legend()
			ref_point = []
			print("Annotate {} lane".format(laneType))
			cv2.imshow("image", image)
			cv2.moveWindow("image", 40,30)
			key = cv2.waitKey(0) & 0xFF

			# if the 'r' key is pressed, reset the cropping region
			if key == ord('r'):
				image=clone.copy()
				points =[]
				break

			while(True): # wait until user done keyPT job
				
				if key == 13:
					points.append(ref_point)
					count.append(1)
					break
				key = cv2.waitKey(1) & 0xFF

			print(points)
			print("annot. {} points, and saved!".format(len(ref_point)))

		if len(points)==4:
			break

def make_txt_file(image_path, clone):
	global image, points
	make_binary_image(image_path)
	## DO SAVE, txt format, mkdir, or something good!
	ids = str(currentFrame)
	path = image_path +"_annot"
	try:
		if not os.path.exists(path):
			os.makedirs(path)
	except OSError:
		print('Error: Creating directory of data')
	cv2.imwrite(path+"/"+ids+".jpg",clone)
	with open(path+"/"+ids+".txt", 'w') as output:
		for i, row in enumerate(points):
			output.write(label[i]+ " ")
			for data in row:
				output.write(str(data[0])+" "+str(data[1])+" ")
			output.write('\n')




def make_binary_image(image_path):
	global points
	# path = "./culane/laneseg/video"+uuid_s+"/"+image_path+"_annot"
	path = "./culane/laneseg/video/"+image_path+"_annot"
	try:
		if not os.path.exists(path):
			os.makedirs(path)
	except OSError:
		print('Error: Creating directory of data')
	seg = np.zeros((288,800,1), np.uint8)
	for i, lane in enumerate(points):
		for idx in range(len(lane)-1):
			seg = cv2.line(seg, tuple(lane[idx]), tuple(lane[idx+1]), (i+1), 16)
			#seg = cv2.cvtColor(seg, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(path+"/"+str(currentFrame)+".png",seg)

def main():
	global image, points, currentFrame
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", default="", help="Path to the image")
	ap.add_argument("-v", "--video", default="", help="Path to the video")
	ap.add_argument("-f", "--file", default="", help="Path to the file")
	ap.add_argument("-n", "--start_from_frame", default= 1 , help ="start the video's frame")
	args = ap.parse_args()

	# initialize the path
	image_path = args.image
	video_path = args.video
	file_path = args.file
	currentFrame = int(args.start_from_frame)

	if image_path!="":
		image, clone = load_image(image, image_path)
		annot(image_path, clone)
		make_txt_file(image_path,clone)
	if video_path!="":
		cap = cv2.VideoCapture(video_path)
		#cap = load_video(cap)
		i = 0
		while True:
			ret, image = cap.read()
			if (i<currentFrame):
				i = i+1
				continue
			image = cv2.resize(image, dsize=(800,288))
			clone = image.copy()
			image_path = './'+video_path[: -5]
			cv2.namedWindow("image")
			cv2.setMouseCallback("image", shape_selection)
			annot(image_path, clone)
			make_txt_file(image_path,clone)
			currentFrame+=1


	if file_path!="":
		## Ready for retrieve next frame image, flush, variable or something
		for root, dirs, files in os.walk(file_path):
			for fname in files:
				if fname.endswith(".jpg"):
					image_path = os.path.join(root, fname)
					image, clone = load_image(image, image_path)
					image = cv2.resize(image, dsize=(800,288))
					annot(image_path, clone)
					make_txt_file(image_path,clone)

if __name__ == '__main__':
	main()
