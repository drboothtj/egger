from egger.dataclasses.locusclass import Locus
from typing import List
from Bio import SeqIO

def read_annotations(annotations_path: str) -> List[Locus]:
    '''
    reads locus name and location from eggnogmappers .annotations file
        arguments:
            decorated_gff_path:
                absolute path to the .decorated.gff file
        returns:
            locus_list:
                list of locus objects
    '''
    file_to_read = open(annotations_path, 'r') 
    read_lines = file_to_read.readlines()
    locus_list = []
    for line in read_lines:
        line = line.split('\t')
        if len(line) > 7: 
            locus = Locus()
            locus.name = line[0]
            locus.value = line[6]
            locus_list.append(locus)
    return locus_list

def get_positional_info(locus_list: List[Locus], record) -> List[Locus]:
    '''
    extracts locus information from the provided record and uses it to update the locus_list
        Arguments:
            locus_list: the list of Locus objects
            record: the genbank record from Biopython
        Returns:
            locus_list:
                updated locus list with positional data
    '''
   

def read_gbk(locus_list: List[Locus], gbk_path: str) -> List[Locus]:
    '''
    read position information from the .gbk file and annotate corresponding Locus objects
        Arguments:
            locus_list: list of Locus objects
            gbk_path: path to the genbank file
        Returns:
            new_locus_list: the input list of loci annottated with positional information
    '''
    records = SeqIO.parse(gbk_path, "genbank")
    for record in records:
        for feature in record.features:
            if feature.type == 'CDS':
                locus_tag = feature.qualifiers.get('locus_tag')[0]
                for locus in locus_list:
                    if locus_tag in locus.name:
                        locus.start = int(feature.location.start)
                        locus.stop = int(feature.location.end)
    return locus_list

def get_loci(annotations_path: str, gbk_path: str) -> List[Locus]:
    '''
    main function for annotation reader
        Arguments:
            annotations_path: path to eggnogmapper .annotations
            gbk_path: path to genbank file the proteins were extracted from
        Returns:
            locus_list: a list of locus objects with extracted information
    '''
    locus_list = read_annotations(annotations_path)
    locus_list = read_gbk(locus_list, gbk_path)
    return locus_list
