'''Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.'''

print('What is your input file?')
file_name = input()
file_open = open(file_name)
file_content = file_open.read()

dna = {'A':0, 'C':0, 'G':0, 'T':0,}

for i in file_content:
    if i == 'A':
        dna['A'] += 1
    elif i == 'C':
        dna['C'] += 1
    elif i == 'G':
        dna['G'] += 1
    elif i == 'T':
        dna['T'] += 1

print(dna.values())









file_open.close()