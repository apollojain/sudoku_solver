import pdfkit, ocr

def sudoku_html_table(sudoku_dictionary):
	'''
	DESCRIPTION
	-----------
	This 
	'''
	string = open("sudoku.html", 'r').read()
	string_arr = string.split("|")
	return_string = ""
	counter = 0
	for i in range(9):
		for j in range(9):
			return_string += string_arr[counter]
			return_string += str(sudoku_dictionary[i][j])
			counter += 1
	while counter < len(string_arr):
		return_string += string_arr[counter]
		counter += 1
	pdfkit.from_string(return_string, 'out.pdf')

def read_from_image(img_name):
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
	sudoku_arr = ocr.image_to_array(img_name)
	return sudoku_arr

def read_from_file(file_name, base_path = 'inputs/'): 
	'''
	DESCRIPTION 
	-----------
	This function takes in a text file containing a 
	2d list and processes it into an actual 2d array that
	represents your sudoku puzzle

	INPUT PARAMETERS
	----------------
	file_name: string 
		This file_name contains your sudoku puzzle, 
		which is a list of lists that is an int of there is 
		an item in index (i, j) and None otherwise. 

	OUTPUT PARAMETERS
	-----------------
	sudoku_arr: list of lists 
		This list of lists contains the sudoku puzzle
		(i.e. its the number if a number is in cell (i, j)
		and otherwise its None)
	'''
	file_name = base_path + file_name
	with open(file_name, 'r') as f: 
		read_string = f.read()
	sudoku_string = ''.join(''.join(read_string.split('\n')).split('\t'))
	sudoku_arr = eval(sudoku_string)
	return sudoku_arr
