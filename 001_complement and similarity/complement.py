"""
File: complement.py
Name: Peter Lin 20201003
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Algorithm：find out the complement of template.
    """
    template = str(input('Please give me a DNA strand and I\'ll find the complement: '))
    complement = build_complement(template)
    print('The complement of ' + template + ' is ' + complement)


def build_complement(input_data):
    """
    :param input_data: str
    :return: str
    """
    output = ''  # start w/ an empty string
    for i in range(len(input_data)):  # loop over the old string
        bp = input_data[i]
        if bp.islower():  # convert to the uppercase
            bp = bp.upper()
        if bp == 'A':
            output += 'T'
        elif bp == 'T':
            output += 'A'
        elif bp == 'C':
            output += 'G'
        else:  # assume the smart user key in a,t,c,g only
            output += 'C'
    return output


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
