import numpy as np
import sys
import random as rand
#--------------------------------------------------------------
#create a random array with dimension og height and width
def create_random_matrix(height, width):
    output = []
    for index1 in range(height):
        new_row = []
        for index2 in range(width):
            new_row.append(rand.uniform(0,1))
        output.append(new_row)
    return np.array(output)

#--------------------------------------------------------------
#vector matrix multiplication
def vec_matr_mult(vec,matr):
    if len(vec) != len(matr):
        print("Vector and matrix do not have the same dimension")
        sys.exit(0)
    else:
        output = np.zeros(len(matr[0]))
        for index in range(len(matr[0])):
            for mul in range(len(vec)):
                output[index] += vec[mul]*matr[mul][index]
        return output

#--------------------------------------------------------------
