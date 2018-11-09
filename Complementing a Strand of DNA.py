'''Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.'''

print('What is your input file?')
file_name = input()
file_open = open(file_name)
file_content = file_open.read()

compliment = ''

for i in range(len(file_content)):
    b = file_content[-i-1]
    if b == 'A':
        compliment += 'T'
    elif b == 'T':
        compliment += 'A'
    elif b == 'C':
        compliment += 'G'
    elif b == 'G':
        compliment += 'C'

print(compliment)




file_open.close()