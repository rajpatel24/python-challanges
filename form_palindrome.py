"""
Form a palindrome.

Given a string, find the minimum number of characters to be inserted to convert it to palindrome.

Input:
raj

Output:
2
"""


import sys 
  
# Recursive function to find minimum  
# number of insertions 
def findMinInsertions(str, l, h): 
  
    # Base Cases 
    if (l > h): 
        return sys.maxsize
    
    if (l == h): 
        return 0
    if (l == h - 1): 
        return 0 if(str[l] == str[h]) else 1
  
    # Check if the first and last characters are 
    # same. On the basis of the comparison result,  
    # decide which subrpoblem to call 
      
    if(str[l] == str[h]): 
        return findMinInsertions(str, l + 1, h - 1) 
    else: 
        return (min(findMinInsertions(str, l, h - 1), 
                    findMinInsertions(str, l + 1, h)) + 1)

    
if __name__ == "__main__": 
      
    str = input("Enter the string: ")
    print(findMinInsertions(str, 0, len(str) - 1))
