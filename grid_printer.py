"""
Update below functions with code to print different grids based on the input parameters.

NOTE: do not print anything besides the grid boxes in your functions.
"""

# Kate Pollock
# Python 310
# Assignment 2: Grid Printer

# PART 1
# print a 2x2 grid using a function

def print_grid1():
    size = 4
    rows_cols = 2
    for i in range(rows_cols):
        print(rows_cols * ('+ ' + ('- ' * size)) + '+')
        for j in range(size):
            print(rows_cols * ('| ' + ('  ' * size)) + '|')
    print(rows_cols * ('+ ' + ('- ' * size)) + '+')


# PART 2
# print a 2x2 grid using a function that has one parameter 'size'
# 'size' is assumed to be the number of characters between the borders
# in the case that 'size' is an odd number, use '//' to round down

def print_grid2(size):
    n = size // 2
    for i in range(2):
        print(2 * ('+ ' + (n * '- ')) + '+')
        for j in range(n):
            print(2 * ('| ' + (n * '  ')) + '|')
    print(2 * ('+ ' + (n * '- ')) + '+')



# PART 3
# print a grid using a function that has 2 parameters
# box_size represents the number of rows or columns which are equivalent
# cell_size represents the number of spaces between the borders of the rows or columns

def print_grid3(box_size, cell_size):
    for i in range(box_size):
        print(box_size * ('+ ' + (cell_size * '- ')) + '+')
        for j in range(cell_size):
            print(box_size * ('| ' + (cell_size * '  ')) + '|')
    print(box_size * ('+ ' + (cell_size * '- ')) + '+')


# executes your grid functions below
if __name__ == "__main__":
    print_grid1()
    
    print_grid2(3)
    
    print_grid3(3, 4)
    
