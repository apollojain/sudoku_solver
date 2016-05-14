import pdfkit

def sudoku_html_table(sudoku_dictionary):
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