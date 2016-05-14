import cv2
import numpy as np 
import scipy.misc
from PIL import Image, ImageFilter
from pytesseract import image_to_string

def rectify(h):
    h = h.reshape((4,2))
    hnew = np.zeros((4,2),dtype = np.float32)

    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]
     
    diff = np.diff(h,axis = 1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    return hnew

def pre_processing(img_name, base_path="Images/"):
	img_path = base_path + str(img_name)
	img = cv2.imread(img_path)
	print img
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
	return (gray, thresh)

def find_puzzle(img_name):
	
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
	dictionary = split_sudoku_cells(img_name)
	for i in range(9):
		for j in range(9):
			scipy.misc.imsave("intermediates/" + str(i) + str(j) + '.jpg', dictionary[i][j])
			processed_img = pre_processing(str(i) + str(j) + '.jpg', 'intermediates/')[1]
			print processed_img
			scipy.misc.imsave("intermediates/" + str(i) + str(j) + '.jpg', processed_img)

def ocr_image(image_name):
	img = Image.open('intermediates/' + image_name)
	# img = img.filter(ImageFilter.FIND_EDGES)
	img.save("new_img.png")
	return image_to_string(img)
# print write_cells_to_images('sudoku_puzzle.png')

print ocr_image('18.jpg')
# try: 
# 	print Image.open('intermediates/18.jpg')
# 	print image_to_string(Image.open('intermediates/18.jpg'))
# except Exception as e: 
# 	print e

