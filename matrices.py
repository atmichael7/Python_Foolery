'''
This demonstrates the algorithm to go through each matrix of varying dimensions
The matrices dont have to be evenly distributed in themselves in order to be printed
Thus they can be expanded or retracted in several scenarios as long as their dimensionality is retained 

There is some output formmating but when it gets to 3d the labeling is ambiguous, refer to the for loop printing there 
'''

matrix_1d = [1, 2, 3, 4, 5]

matrix_2d = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

matrix_3d = [[[1, 2], [3, 4]],
             [[5, 6], [7, 8]],
             [[9, "A"], ["B", "C"]]]
             
matrix_2d_uneven = [[1],
                    [2, 3],
                    [4, 5, 6]]

matrix_3d_uneven = [[[1, 2]],
                    [[3, 4], [5]],
                    [[6],    [7, 8, 9]]]
             
def goThruMatrix(dimensions, matrix):
    if dimensions == 1:
        print("Row 1: ", end="")
        for curr_index in range(len(matrix)):
            print(matrix[curr_index], end=", ")
    
    elif dimensions == 2:
        for curr_row in range(len(matrix)): # goes through each row index
            amount_of_columns = len(matrix[curr_row])
            print("Row {}: ".format(curr_row+1), end="")
            
            for curr_col in range(amount_of_columns):
                print(matrix[curr_row][curr_col], end=", ")
                
            print("")
                
    else: # dimensions == 3 
        for curr_row in range(len(matrix)): # goes through each row 
            amount_of_columns = len(matrix[curr_row]) # gather how many entries are in the current row
            print("Row {}: ".format(curr_row))
            
            for curr_col in range(amount_of_columns):
                amount_of_entries = len(matrix[curr_row][curr_col])
                print("Entry {}: ".format(curr_col+1)) # wording here is ambiguous, this is listing each column, but each column has sub entries 
                
                for curr_entry in range(amount_of_entries):
                    print(matrix[curr_row][curr_col][curr_entry], end=", ")
                    
                print("")
            
            print("")
                
        
        
# testing loop
test = [matrix_1d, matrix_2d, matrix_3d, matrix_2d_uneven, matrix_3d_uneven]
par_test = [1, 2, 3, 2, 3]

for eachTest in range(5):
    print("\n==================== TEST {} ====================".format(eachTest+1))
    goThruMatrix(par_test[eachTest], test[eachTest])
