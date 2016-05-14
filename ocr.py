from PIL import Image, ImageFilter
from pytesseract import image_to_string
import image_processing as ip

def ocr_image(image_name, base_path='intermediates/'):
	'''
	DESCRIPTION 
	-----------
	This function takes in your image name and base path 
	and tries to read the text inside of the image using 
	OCR. 

	INPUT PARAMETERS 
	----------------
	image_name: string 
		The name of your image, including extension
	base_path: string 
		The folder that your image is located in. 
	
	OUTPUR PARAMETERS
	-----------------
	return_string: string 
		The string that is inside of your image. 
	'''
	img = Image.open(base_path + image_name)
	# img = img.filter(ImageFilter.FIND_EDGES)
	return_string = image_to_string(img)
	return return_string 

def image_to_array(img_name):
	'''
	DESCRIPTION
	-----------
	This takes in your image name and then processes it 
	using the ocr_image function. Subsequently, it places 
	it in a 2d array to be returned. 

	INPUT PARAMETERS 
	----------------
	image_name: string 
		The name of your image, including extensions
	
	OUTPUT PARAMETERS 
	-----------------
	sudoku_arr: list of lists 
		This list of lists contains the sudoku puzzle
		(i.e. its the number if a number is in cell (i, j)
		and otherwise its None)
	'''
	ocr_string = lambda s: None if s is "" else int(s)
	ip.write_cells_to_images(img_name)
	sudoku_arr = [[None]*9]*9
	for i in range(9):
		for j in range(9):
			sudoku_arr[i][j] = ocr_string(ocr_image(str(i) + str(j) + ".jpg"))
	return sudoku_arr

