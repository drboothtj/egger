'''
functions for processing annotation data for egger plotting
    functions:
        !!!!
'''
from egger.utils import io
from typing import Dict, List, Tuple
from Bio import SeqIO

def get_categorys(data_points):
    '''
    !!!
    '''
    categories = set([data[2] for data in data_points])
    categories = ''.join(categories)
    categories = set(categories)
    return categories

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
                header = line #make sure this is '#query' or error
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

def get_cds_locations(filename: str) -> List[Tuple[str, str, int, int, float]]:
    '''
    read a genbank file and return a dictionary with CDS location information
        arguments:
            filename: path to genbank file
        returns:
            locations_list:
                a list of tuples containing the cds name, the record name 
                and the midpoint of the cds
    '''
    locations_list = []
    for record in SeqIO.parse(filename, 'genbank'): #catch BAD FILE TYPE #add record info
        record_name = record.name
        for feature in record.features:
            if feature.type == 'CDS':
                cds_name = feature.qualifiers['locus_tag'][0]
                start = int(feature.location.start)
                stop = int(feature.location.end)
                midpoint = start + ((stop-start)/2)
                locations_list.append((cds_name, record_name, start, stop, midpoint))
    return locations_list

def add_location_data(filename: str, proteins: List[Dict]) -> List[Dict]:
    '''
    reads location information from genbank file and adds it to protein dictionary
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
                protein['record_name'] = cds[1] #missing record error
                protein['start'] = cds[2]
                protein['stop'] = cds[3]
                protein['midpoint'] = cds[4]
    return proteins

def get_data_for_plot(
    proteins: List[Dict[str, str]], annotation_type: str
    ) -> List[Tuple[str, str, int]]:
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
        try:
            data_point = (
                protein['record_name'], protein['midpoint'], protein[annotation_type]
            )
        except KeyError:
            print(
                'Warning: %s is missing information and so was excluded.' % protein['#query']
            )
        ##ADD ERROR FOR BAD ANNOTATION TYPE or missing midpoint
        data_points.append(data_point)
    return data_points

def process(annotation_filename, gbk_filename, annotation_type):
    '''
    main routine for process
        arguments:!!
        returns: !!
    '''
    lines = io.read_tsv(annotation_filename)
    annotations = process_headers(lines)
    proteins = convert_annotations_to_dictionary(annotations)
    proteins = add_location_data(gbk_filename, proteins)
    data_points = get_data_for_plot(proteins, annotation_type)
    categories = get_categorys(data_points) #list of categories
    records = set([point[0] for point in data_points])   #list of record names
    return data_points, categories, records
