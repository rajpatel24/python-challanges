"""
Permutation of given string.

Given a string S. The task is to print all permutations of a given string.

Input:
ABC

Output:
ABC
ACB
BAC
BCA
CAB
CBA
"""


# Function to find permutations of a given string 
from itertools import permutations 
  
def allPermutations(data): 
     # Get all permutations of string 
     permList = permutations(data)
     return permList
  
           
# Driver program 
if __name__ == "__main__": 
    data = input("Enter the string: ")
    allPermutations(data)
    o_data = allPermutations(data)
    # print all permutations 
    for perm in list(o_data): 
         print (''.join(perm))
