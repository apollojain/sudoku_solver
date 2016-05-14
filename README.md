What this is
============
This project allows you to take in a sudoku file, process it, and output a completed sudoku puzzle pdf. It works on both text files and images. See an example input in the "inputs" folder and an example output in "out.pdf," which corresponds to "sudoku_puzzle.txt."

How to use it
=============
You can use this solver in two ways. First of all, drop your input file into the "inputs" folder. Next, if you have a text file (in this case sudoku_puzzle.txt), you simply type 
```
$ python sudoku.py sudoku_puzzle.txt
```
and if you have an image (in this case, sudoku_puzzle.png), you'd simply type 
```
$ python sudoku.py sudou_puzzle.png
```
That's it!

How it works
============

Image Processing
----------------
The actual Image Processing portion of this project is done through OpenCV2 for Python. The project pre-processes the image in order to make the cells more recognizable, finds the largest square in the inputted image (which is the puzzle itself), and then divides the puzzles into 81 cells. Each cell is inverted so it appears as if it is a word document and then is read using pytesseract, an OCR library for python.  

The Solver
----------
The solver itself basically starts by creating a dictionary of all possible solutions to each cell. If entry (i, j) has an entry that contains a list of length 1, then that means that there is only one possible solution to that puzzle. It'll fill in all of these "guaranteed entries." After all of these entries are exhausted, the solver will try a backtracking algorithm. 

Acknowledgements
================
I will be the first to admit that I'm no expert in Computer Vision. I could not have completed this project with the help of [this tutorial](http://opencvpython.blogspot.com/2012/06/sudoku-solver-part-2.html), which shows how to detect where a sudoku puzzle is inside of the image and then how to cut the sudoku puzzle out of the image and save it. Also, there were a number of StackOverflow posts that were immensely helpful in understanding how to use OpenCV and pytesseract. 

