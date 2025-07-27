import numpy as np
import pandas as pd

num_arr1 = np.array([10,20,30,40])
print(type(num_arr1))

num_list1 = [101,102,103,104,105]
num_arr1 = np.array(num_list1) # Overrides the initial assigned values of [10,20,30,40]
print(num_arr1)   # Output is [101 102 103 104 105], note there is no comma between the numbers in the output, indicating it's a numpy array.

num_list2 = [1,2,3,4,5]
num_arr2 = np.array(num_list2) # Creates a numpy array from the list
print(num_arr1 + num_arr2) # Output is [102 104 106 108 110], which is the element-wise addition of the two arrays.

num_zero_arr1 = np.zeros(5) # Creates a numpy array of zeros with 5 elements
print(num_zero_arr1) # Output is [0. 0. 0. 0. 0.]
num_zero_arr2 = np.zeros((3, 4)) # Creates a 3x4 numpy array of zeros
print(num_zero_arr2) # Output is a 3x4 array of zeros

num_ones_arr1 = np.ones(5) # Creates a numpy array of ones with 5 elements
print(num_ones_arr1) # Output is [1. 1. 1. 1. 1.]   
num_ones_arr2 = np.ones((3, 4)) # Creates a 3x4 numpy array of ones
print(num_ones_arr2) # Output is a 3x4 array of ones


num_random_ints_arr = np.random.randint(low=0, high=100, size=(12, 13))
print(num_random_ints_arr) # Output is a 12x13 array of random integers between 0 and 100

num_arr3 = np.arange(0,100,5) # Creates a numpy array with values from 0 to 100 with a step of 5
print(num_arr3) # Output is [ 0  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]
alpha_list = ['a','b','c', 'd', 'e']
alpha_series = pd.Series(alpha_list) # Creates a pandas Series from the list of alphabets
print(alpha_series) # Output is a pandas Series with indices and values from the alpha_list



#numpy.arange([start,] stop, [step,] dtype=None)



'''

num_list2 = [1,2,3,4,5]
print(type(num_list1))

print(type(num_arr2))

print(num_arr1) #[101 102 103 104 105]
print(num_list1) #[101, 102, 103, 104, 105]
print(num_arr2) #[101 102 103 104 105]

'''