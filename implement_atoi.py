"""
Implement Atoi.

Input:
123

Output:
123

"""


def atoi(str):
    resultant = 0
    for i in range(len(str)):

        #Below is ASCII substraction 
        resultant = resultant * 10 + (ord(str[i]) - ord('0'))
    return resultant


if __name__ == '__main__':
    str = input("Enter string to be converted: ")
    sum = atoi(str)
    print(sum)
    
