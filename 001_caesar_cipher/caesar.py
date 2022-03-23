"""
File: caesar.py
Name: Peter Lin 20201003
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    ALGORITHM : find out the index of the ciphered string, and convert into the deciphered index!
    """
    rule = int(input('Secret number: '))
    code = str(input('What\'s the ciphered string?'))
    ans = decipher(rule, code)
    print('The deciphered string is: ' + ans)


def decipher(a, b):
    """
    :param a: int
    :param b: str
    :return: str
    """
    new = ''
    b = b.upper()  # convert code to the upper case for case-insensitive
    for ch in b:
        if ch.isalpha():  # if the ch is the alphabet, decipher!
            index = ALPHABET.find(ch)  # find out the ciphered index
            index += a
            if index > 25:
                index -= 26
            new += ALPHABET[index]
        else:  # if the ch is not the alphabet, print!
            new += ch
    return new


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
