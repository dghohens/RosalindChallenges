'''Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.'''

print('What is your input file?')
file_name = input()
file_open = open(file_name)
file_content = file_open.read()

rna = ''

for i in file_content:
    if i == 'T':
        rna += 'U'
    else:
        rna += i

print(rna)







file_open.close()