def row_legal(item, x, y, puzzle_matrix):
	'''
	DESCRIPTION
	-----------
	Determines if the placement of x is allowed based 
	on the values that are already in that row, column, 
	and 3x3 sector. 

	INPUT PARAMETERS
	----------------
	item: int
		This is the item that you are trying to place (1-9)
	x: int
		Your x coordinate (index from 0)
	y: int 
		Your y coordinate (index from 0)
	puzzle_matrix: list of lists
		This is your Sudoku pizzle

	OUTPUT PARAMETERS
	-----------------
	is_legal: boolean 
		Tells you if that move is legal or not.
	'''
	for j in range(9):
		if puzzle_matrix[x][j] == item and j is not y: 
			return False 
	return True

def column_legal(item, x, y, puzzle_matrix):
	'''
	DESCRIPTION
	-----------
	Determines if the placement of x is allowed based on 
	the values that are already in that row, column, and 
	3x3 sector. 

	INPUT PARAMETERS
	----------------
	item: int
		This is the item that you are trying to place (1-9)
	x: int
		Your x coordinate (index from 0)
	y: int 
		Your y coordinate (index from 0)
	puzzle_matrix: list of lists
		This is your Sudoku pizzle

	OUTPUT PARAMETERS
	-----------------
	is_legal: boolean 
		Tells you if that move is legal or not.
	'''
	for i in range(9):
		if puzzle_matrix[i][y] == item and x is not i: 
			return False 
	return True

def quadrant_legal(item, x, y, puzzle_matrix):
	'''
	DESCRIPTION
	-----------
	Determines if the placement of x is allowed 
	based on the values that are already in that row, 
	column, and 3x3 sector. 

	INPUT PARAMETERS
	----------------
	item: int
		This is the item that you are trying to place (1-9)
	x: int
		Your x coordinate (index from 0)
	y: int 
		Your y coordinate (index from 0)
	puzzle_matrix: list of lists
		This is your Sudoku pizzle

	OUTPUT PARAMETERS
	-----------------
	is_legal: boolean 
		Tells you if that move is legal or not.
	'''
	#0, 1, or 2
	qx = x / 3
	qy = y / 3
	i_list = range(3*qx, 3*qx + 3)
	j_list = range(3*qy, 3*qy + 3)
	for i in i_list: 
		for j in j_list: 
			if puzzle_matrix[i][j] == item and x is not i and y is not j:
				return False 
	return True

def legal_move_ignoring_current_cell(item, x, y, puzzle_matrix):
	'''
	DESCRIPTION
	-----------
	Determines if the placement of x is allowed based 
	on the values that are already in that row, 
	column, and 3x3 sector. This is ignoring the item that is currently in your row. 

	INPUT PARAMETERS
	----------------
	item: int
		This is the item that you are trying to place (1-9)
	x: int
		Your x coordinate (index from 0)
	y: int 
		Your y coordinate (index from 0)
	puzzle_matrix: list of lists
		This is your Sudoku puzzle. 

	OUTPUT PARAMETERS
	-----------------
	is_legal: boolean 
		Tells you if that move is legal or not.
	'''
	if x > 8 or x < 0: 
		return False 
	if y > 8 or y < 0: 
		return False 
	if item > 9 or item < 1: 
		return False 
	
	r = row_legal(item, x, y, puzzle_matrix)
	c = column_legal(item, x, y, puzzle_matrix)
	q = quadrant_legal(item, x, y, puzzle_matrix)
	is_legal = (r and c and q)
	return is_legal

def legal_move(item, x, y, puzzle_matrix):
	'''
	DESCRIPTION
	-----------
	Determines if the placement of x is allowed based 
	on the values that are already in that row, 
	column, and 3x3 sector. 

	INPUT PARAMETERS
	----------------
	item: int
		This is the item that you are trying to place (1-9)
	x: int
		Your x coordinate (index from 0)
	y: int 
		Your y coordinate (index from 0)
	puzzle_matrix: list of lists
		This is your Sudoku puzzle. 

	OUTPUT PARAMETERS
	-----------------
	is_legal: boolean 
		Tells you if that move is legal or not.
	'''
	if puzzle_matrix[x][y] is not None: 
		return False
	is_legal = legal_move_ignoring_current_cell(item, x, y, puzzle_matrix)
	return is_legal

if __name__ == '__main__':
	matrix = [
		[None, None, None, 2, 6, None, 7, None, 1], 
		[6, 8, None, None, 7, None, None, 9, None],
		[1, 9, None, None, None, 4, 5, None, None], 
		[8, 2, None, 1, None, None, None, 4, None], 
		[None, None, 4, 6, None, 2, 9, None, None],
		[None, 5, None, None, None, 3, None, 2, 8],
		[None, None, 9, 3, None, None, None, 7, 4], 
		[None, 4, None, None, 5, None, None, 3, 6], 
		[7, None, 3, None, 1, 8, None, None, None]
	]
	# print row_legal(2, 0, 0, matrix) == False
	print legal_move(2, 0, 0, matrix) == False
	print legal_move_ignoring_current_cell(2, 0, 3, matrix) == True
	print legal_move_ignoring_current_cell(7, 0, 3, matrix) == False
	
	# print quadrant_legal(3, 3, 2, matrix) == True
	print legal_move(3, 0, 0, matrix)
	test_matrix = [
		[None, None, None, None, None, None, 4, None, None], 
		[None, None, None, 9, None, None, 3, 6, None], 
		[None, 3, 1, 2, 4, None, 8, 9, None], 
		[1, 5, 6, 8, 9, 4, 2, 7, 3], 
		[7, 8, 2, 5, 6, 3, 9, 1, 4], 
		[None, 9, None, 7, 1, 2, 5, 8, 6], 
		[None, 1, None, None, 5, 8, 7, 4, None], 
		[None, 6, 8, None, None, 9, 1, None, None], 
		[None, None, None, None, None, None, 6, None, None]
	]
	print row_legal(9, 6, 8, test_matrix)






