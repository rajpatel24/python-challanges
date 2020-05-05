"""

Reverse words in a given string.

Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.

Input:
Hello Gateway

Output:
Gateway Hello
"""


def reverse_word(data):
    
    #splitting the string by spaces
    words = data.split()

    #Reversing the words
    words = list(reversed(words))
    return words

if __name__ == '__main__':
    data = input("Enter the string: ")
    result = reverse_word(data)

    #Joining the words and print
    print(" ".join(result))
