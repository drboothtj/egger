'''
functions for input and output of files for egger
    functions:
        read_tsv(filename: str) -> List[str]
'''
import csv
from typing import List

def read_tsv(filename: str) -> List[str]:
    '''
    read a tsv file
        arguments: 
            filename: path to .tsv file
        returns:
            lines: list of lines from the .tsv file
    '''

    with open(filename, 'r') as file: #os.path?
        reader = csv.reader(file, delimiter='\t')
        lines = []
        for row in reader:
            lines.append(row)
        return lines

