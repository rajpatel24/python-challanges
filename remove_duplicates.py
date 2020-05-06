"""
Remove Duplicates.

Given a string, the task is to remove duplicates from it.

Input:
raaj

Output:
raj

"""

from collections import OrderedDict 

def removeDupWithoutOrder(str):  
    return "".join(set(str))

def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))  
  

if __name__ == "__main__": 
    str = input("Enter a string to remove duplicates: ") 
    print ("With Order: ",removeDupWithOrder(str))
    print ("Without Order: ",removeDupWithoutOrder(str))
