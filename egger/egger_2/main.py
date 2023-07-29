'''
egger: visualise eggnog-mapper data

functions:
    !!!!!!!!
'''
import csv
import sys
from typing import Dict, List, Tuple
from Bio import SeqIO

###MAKE A PROPER PARSER
### ADD OTHER FUNCTIONS -list headers -extract-fasta-from-
##add logging

ANNOTATION_FILE = sys.argv[1]
GBK_FILE = sys.argv[2]
ANNOTATION_TYPE = sys.argv[3]
NUMBER_OF_BINS = sys.argv[4]

def read_tsv(filename: str) -> List[str]:
    '''
    read a tsv file
        arguments: 
            filename: path to .tsv file
        returns:
            lines: list of lines from the .tsv file'''

    with open(filename, 'r') as file: #os.path?
        reader = csv.reader(file, delimiter='\t')
        lines = []
        for row in reader:
            lines.append(row)
        return lines

def process_headers(lines: List[str]) -> Tuple[str, List[str]]:
    '''
    remove metadata from .annotations and return the headers and data
    arguments:
        lines: list of lines from .annotations file
    returns:
        header: header string
        annotation_data: data lines from the annotation file with headers and metadata removed
    '''
    annotation_data = []
    for line in lines:
        if line[0][0] == '#':
            if line[0][1] != '#':
                header = line
        else:
            annotation_data.append(line)
    assert header,annotation_data #add error catching
    return (header, annotation_data)

def convert_annotations_to_dictionary(annotations: Tuple[str, List[str]]) -> List[Dict[str, str]]:
    '''
    converts annotation data to a dictionary
    arguments: 
        annotations: tuple containing the header string and list of data lines
    returns:
        proteins: a list of dictionarys each containing annotations of a single protein
    '''
    proteins = []
    header, data = annotations
    for line in data:
        protein = {}
        for head, value in zip(header, line):
            #print('head: %s, dataum: %s' % (head, value))
            protein[head] = value
        proteins.append(protein)
    return proteins

def get_cds_locations(filename: str) -> List[Tuple[str,int]]:
    '''
    read a genbank file and return a dictionary with CDS location information
    arguments:
        filename: path to genbank file
    returns:
        locations:
            a list of dictionarys with CDS location information
    '''
    locations_list = []
    for record in SeqIO.parse(filename, 'genbank'): #catch BAD FILE TYPE
        for feature in record.features:
            if feature.type == 'CDS':
                cds_name = feature.qualifiers['locus_tag'][0]
                start = int(feature.location.start)
                stop = int(feature.location.end)
                midpoint = start + ((stop-start)/2)
                locations_list.append((cds_name, midpoint))
    return locations_list

def add_location_data(filename: str, proteins: List[Dict]) -> List[Dict]:
    '''reads location information from genbank file and adds it to protein dictionary
        arguments:
            filename: path to a genbank file
            proteins: list of protein annotation dictionarys
        returns:
            proteins: updated dictionary with locaiton info
    '''
    cds_locations = get_cds_locations(filename)
    for cds in cds_locations:
        for protein in proteins:
            if cds[0] in protein['#query']:
                protein['midpoint'] = cds[1]
    return proteins

def get_data_for_plot(
    proteins: List[Dict[str, str]], annotation_type: str
    ) -> List[Tuple[int, str]]:
    '''
    takes annotation dictionarys and returns data for line plots
    arguments:
        proteins: list of protein dictionarys containing annotaitons
        annotation_type: the header of the annotation to extract
    returns:
        data_points: list of tuples describing the protein midpoint and annotation
    '''
    data_points = []
    for protein in proteins:
        data_point = (protein['midpoint'], protein[annotation_type])
        ##ADD ERROR FOR BAD ANNOTATION TYPE or missing midpoit
        data_points.append(data_point)
    return data_points

def main(annotation_filename: str, gbk_filename: str, annotation_type: str) -> None:
    '''
    main routine for egger
    arguments:
        annotation_filename: path to .annotations file
        gbk_filename: path to .gbk file
        annotation_type: annotation header to plot
    returns:
        None
    '''
    lines = read_tsv(annotation_filename)
    annotations = process_headers(lines)
    proteins = convert_annotations_to_dictionary(annotations)
    proteins = add_location_data(gbk_filename, proteins)
    data_points = get_data_for_plot(proteins, annotation_type)
    print(data_points)
    #bin data?
    #make plots

main(ANNOTATION_FILE, GBK_FILE, ANNOTATION_TYPE) #NUMBER_OF_BINS
