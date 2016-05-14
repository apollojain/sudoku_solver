import legal_moves, copy, helpers, read_write

def solve_for_guarantees(sudoku_matrix):
	'''
	DESCRIPTION 
	-----------
	This function helpers.constructs a matrix that contains 
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
	sudoku_dictionary = helpers.construct_legal_moves_dictionary(sudoku_matrix)
	for i in range(9):
		for j in range(9):
			sudoku_list = sudoku_dictionary[i][j]
			if len(sudoku_list) == 1:
				sudoku_matrix[i][j] = sudoku_list[0]
	return sudoku_matrix

def brute_force_helper(sudoku_matrix, sudoku_dictionary, x, y):
	'''
	DESCRIPTION 
	-----------
	This function basically allows you to take in a sudoku dictionary
	and a sudoku matrix and then brute force a solution out of it at the 
	index (x, y).

	INPUT PARAMETERS
	----------------
	sudoku_matrix: list of lists
		This is basically a representation of your sudoku matrix, 
		where entries that haven't been filled in yet are None
	sudoku_dictionary: dictionary
		Each entry (i, j) corresponds to a list that includes all 
		possible numbers that can be placed in that square
	x: int 
		This is the row of the sudoku entry you want to change
	y: int
		This is the column of the sudoku entry that you want to change

	OUTPUT PARAMETERS
	-----------------
	solution: list of lists
		This is the solution to your sudoku puzzles
	'''
	for item in sudoku_dictionary[x][y]:

		new_matrix = copy.deepcopy(sudoku_matrix)
		new_matrix[x][y] = item
		new_dictionary = helpers.construct_legal_moves_dictionary(new_matrix)
		# solution = brute_force_solve(new_matrix, new_dictionary)
		solution = sudoku_solve(new_matrix)
		if solution is not None: 
			return solution
	else:
		solution = None
		return solution

def brute_force_solve(sudoku_matrix, sudoku_dictionary):
	'''
	DESCRIPTION
	-----------
	This function basically brute forces a solution for 
	your sudoku puzzle when you have reached the point where
	there are no single entry lists left in your dictionary. 

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
	return_matrix: list of lists
		The solution to your sudoku puzzle
	'''
	if helpers.is_solved(sudoku_matrix):
		return_matrix = sudoku_matrix
		return return_matrix
	else:
		if helpers.is_solvable(sudoku_matrix, sudoku_dictionary):
			for i in range(9):
				for j in range(9):
					if len(sudoku_dictionary[i][j]) > 0:
						return_matrix = brute_force_helper(sudoku_matrix, sudoku_dictionary, i, j)
						return return_matrix
		else:
			return_matrix = None
			return return_matrix

def sudoku_solve(sudoku_matrix):
	'''
	DESCRIPTION
	-----------
	This function solves your function by both the size one list
	'guarantees' and by brute force. 

	INPUT PARAMETERS
	----------------
	sudoku_matrix: list of lists
		This is basically a representation of your sudoku matrix, 
		where entries that haven't been filled in yet are None
	
	OUTPUT PARAMETERS 
	-----------------
	solved_matrix: list of lists
		The solution to your sudoku puzzle
	'''
	sudoku_dictionary = helpers.construct_legal_moves_dictionary(sudoku_matrix)
	while helpers.has_guarantees(sudoku_dictionary):
		if helpers.is_solvable(sudoku_matrix, sudoku_dictionary):
			sudoku_matrix = solve_for_guarantees(sudoku_matrix)
			sudoku_dictionary = helpers.construct_legal_moves_dictionary(sudoku_matrix)
		else: 
			return None	
	sudoku_dictionary = helpers.construct_legal_moves_dictionary(sudoku_matrix)
	solved_matrix = brute_force_solve(sudoku_matrix, sudoku_dictionary)
	return solved_matrix

if __name__ == '__main__':
	matrix = [
		[None, None, None, None, 7, 2, None, None, None], 
		[9, None, None, None, None, None, None, 3, None],
		[None, 6, None, 1, None, None, 4, None, None], 
		[None, 8, None, None, 3, None, 5, None, None], 
		[None, 7, 5, None, None, None, 2, 9, None],
		[None, None, 6, None, 4, None, None, 8, None],
		[None, None, 7, None, None, 8, None, 2, None], 
		[None, 1, None, None, None, None, None, None, 9], 
		[None, None, None, 9, 1, None, None, None, None]
	]
	result = sudoku_solve(matrix)
	print "-----------"
	print read_write.sudoku_html_table(result)
