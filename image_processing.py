import cv2
import numpy as np 
import scipy.misc


def rectify(h):
	'''
	DESCRIPTION 
	-----------
	This function basically takes your numpy array and 
	finds your corners for the actual sudoku puzzle. 

	INPUT PARAMETERS
	----------------
	h: np.array 
		This is the original numpy array that you are finding 
		the corner coordinates to. 

	OUTPUT PARAMETERS 
	-----------------
	hnew: np.array
		This contains the four corners of np.array
	'''
	h = h.reshape((4,2))
 	hnew = np.zeros((4,2),dtype = np.float32)

	add = h.sum(1)
	hnew[0] = h[np.argmin(add)]
	hnew[2] = h[np.argmax(add)]
     
	diff = np.diff(h,axis = 1)
	hnew[1] = h[np.argmin(diff)]
	hnew[3] = h[np.argmax(diff)]

	return hnew

def pre_processing(img_name, base_path="inputs/"):
	'''
	DESCRIPTION
	-----------
	This function basically preprocesses the image so that 
	a gray threshold is applied to it to make all of the borders 
	and numbers are significantly clearer

	INPUT PARAMETERS
	----------------
	img_name: string 
		This is the actual name of your image, including extensions
	base_path 
		This is the folder that your image is located in
	'''
	img_path = base_path + str(img_name)
	img = cv2.imread(img_path)
	print img
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
	return (gray, thresh)

def find_puzzle(img_name):
	'''
	DESCRIPTION 
	-----------
	This function finds the general area where your sudoku puzzle
	is located and then returns a new images that eliminates 
	all of the noise in your old image and only has the portion that 
	you want. 

	INPUT PARAMETERS 
	----------------
	img_name: string 
		the name of the file that you are passing in 

	OUTPUT PARAMETERS 
	-----------------
	warp: np.array 
		This contains the numpy array that represents your return 
		image, which is only the section of the original image that 
		contains your sudoku puzzle. 
	'''
	gray, thresh = pre_processing(img_name)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	biggest = None 
	max_area = 0
	for i in contours: 
		area = cv2.contourArea(i)
		if area > 100: 
			peri = cv2.arcLength(i, True)
			approx = cv2.approxPolyDP(i, 0.02*peri, True)
			if area > max_area and len(approx == 4):
				biggest = approx
				max_area = area
	if biggest is not None: 
		biggest = rectify(biggest)
		h = np.array([ [0,0],[449,0],[449,449],[0,449] ],np.float32)
		retval = cv2.getPerspectiveTransform(biggest,h)
		warp = cv2.warpPerspective(gray,retval,(450,450))
		return warp

def split_sudoku_cells(img_name):
	'''
	DESCRIPTION 
	-----------
	This function takes in an image name, finds your puzzle, and then 
	splits the image into 81 numpy arrays, each if which represents 
	cell (i, j) of your sudoku puzzle. 

	INPUT PARAMETERS 
	----------------
	img_name: string 
		This string represents the actual name of the image that you 
		are working on, including extensions.  

	OUTPUT PARAMETERS 
	-----------------
	dictionary: dictionary 
		Each entry (i, j) includes a numpy array that represents the image 
		that corresponds to sudoku cell (i, j)
	'''
	dictionary = {}
	warp = find_puzzle(img_name)
	print "part 1_-______--____do we get here -_____SASDA_SAA"
	
	arr = np.split(warp, 9)
	for i in range(9):
		dictionary[i] = {}
		for j in range(9):
			dictionary[i][j] = []

	for i in range(9):
		for j in range(9):
			print "part 2_-______--____do we get here -_____SASDA_SAA"
	
			for a in range(len(arr[i])):
				# print len(arr[i])
				cells = np.split(arr[i][a], 9)
				# print cells[j]
				# print len(cells[j])
				dictionary[i][j].append(np.array(cells[j]))

			dictionary[i][j] = np.array(dictionary[i][j])
	return dictionary

def write_cells_to_images(img_name):
	'''
	DESCRIPTION 
	-----------
	This function calls split_sudoku_cells and then saves these images in 
	an "intermediates" files. 

	INPUT PARAMETERS 
	-----------------
	img_name: string 
		This is the name of the string corresponds to the image 
		that you are reading and saving from, including file 
		extension. 

	OUTPUT PARAMETERS 
	-----------------
	None (a bunch of images) ij.jpg that correspond to entry (i, j)
	of your dictionary will be saved to the "intermediates" folder)
	'''
	dictionary = split_sudoku_cells(img_name)
	for i in range(9):
		for j in range(9):
			scipy.misc.imsave("intermediates/" + str(i) + str(j) + '.jpg', dictionary[i][j])
			processed_img = pre_processing(str(i) + str(j) + '.jpg', 'intermediates/')[1]
			scipy.misc.imsave("intermediates/" + str(i) + str(j) + '.jpg', processed_img)
