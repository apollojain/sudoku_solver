import copy, legal_moves

def construct_legal_moves_dictionary(sudoku_matrix):
	'''
	DESCRIPTION 
	-----------
	This function constructs a matrix that contains 
	lists of all possible legal moves

	INPUT PARAMETERS
	----------------
	sudoku_matrix: list of lists
		This is basically a representation of your sudoku matrix, 
		where entries that haven't been filled in yet are None

	OUTPUT PARAMETERS 
	-----------------
	return_dictionary: dict
		The first key is your row and the second key is your column. The 
		entry is the list of legal numbers you can put in that square.
	'''
	return_dictionary = {}
	is_legal_move = lambda k, i, j: legal_moves.legal_move(k, i, j, sudoku_matrix)
	for i in range(9):
		if i not in return_dictionary.keys():
			return_dictionary[i] = {}
		for j in range(9):
			if j not in return_dictionary[i].keys():
				return_dictionary[i][j] = []
			for k in range(1, 10):
				if is_legal_move(k, i, j):
					return_dictionary[i][j].append(k)
	return return_dictionary

def is_solved(sudoku_matrix):
	'''
	DESCRIPTION
	-----------
	This function tells you if a sudoku puzzle is solved or not. 

	INPUT PARAMETERS
	----------------
	sudoku_matrix: list of lists
		This is basically a representation of your sudoku matrix, 
		where entries that haven't been filled in yet are None

	OUTPUT PARAMETERS 
	-----------------
	return_boolean: boolean
		Tells you if your sudoku is completely solved
	'''
	is_legal = lambda item, x, y: legal_moves.legal_move_ignoring_current_cell(item, x, y, sudoku_matrix)
	for i in range(9):
		for j in range(9):
			item = sudoku_matrix[i][j]
			if item == None or is_legal(item, i, j) == False: 
				return False 
	return True

def is_solvable(sudoku_matrix, sudoku_dictionary):
	'''
	DESCRIPTION
	-----------
	This function tells you if a sudoku puzzle is solvable or not. 

	INPUT PARAMETERS
	----------------
	sudoku_matrix: list of lists
		This is basically a representation of your sudoku matrix, 
		where entries that haven't been filled in yet are None
	sudoku_dictionary: dictionary
		Each entry (i, j) corresponds to a list that includes all 
		possible numbers that can be placed in that square

	OUTPUT PARAMETERS 
	-----------------
	return_boolean: boolean
		Tells you if your sudoku is solvable
	'''
	if is_solved(sudoku_matrix):
		return True
	else:
		for i in range(9):
			for j in range(9):
				if sudoku_matrix[i][j] == None and len(sudoku_dictionary[i][j]) == 0: 
					return False 
		return True

def has_guarantees(sudoku_dictionary):
	'''
	DESCRIPTION 
	-----------
	This function checks if your Sudoku dictionary has 
	any list entries of length 1. This is useful in determining
	whether to use solve_for_guarantees or to brute force
	the thing. 

	INPUT PARAMETERS
	----------------
	sudoku_dictionary: dictionary
		Each entry (i, j) corresponds to a list that includes all 
		possible numbers that can be placed in that square

	OUTPUT PARAMETERS
	-----------------
	boolean
		Thsi boolean tells whether there are entries in your dictionary
		that are lists of length 1
	'''
	for i in range(9):
		for j in range(9):
			if len(sudoku_dictionary[i][j]) == 1:
				return True
	return False
