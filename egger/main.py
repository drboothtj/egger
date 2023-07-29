from egger.dataclasses.locusclass import Locus
from egger import annotation_reader
from typing import List, Tuple

def get_bins(genome_length: int, n_bins: int) -> List[Tuple]:
        '''
        automatically allocate the bin start and end points depending on the genome size
            Arguments:
                genome_length: 
                    the length of the genome in base pairs
                n_bins: 
                    the number of bins specified by the user
            Returns:
                bins_list: 
                    a list of tuples indicating the start and end point of the each bin
        '''
        bin_size = genome_length // n_bins
        bins_list = []
        bin_start = 1
        #if not divisable shoot a warning
        for _bin in range(0, n_bins):
            bin_end = bin_start + bin_size - 1
            bin_tuple = (bin_start, bin_end)
            bins_list.append(bin_tuple)
            bin_start = bin_end + 1
        return bins_list

def populate_bins(locus_list: List[Locus], bins_list: List[Tuple]):
    '''
    create a dictionary for each bin containing data for each loci that falls within its limits
        Arguments:
            locus_list:
                list of loci annotated with names, functions and positional info
        Returns:
            bins_dicts:
                list of dictionarys ???
    '''
    for locus in locus_list:
        if locus.start is not None and locus.stop is not None: #remove None values earlier
            midpoint = locus.midpoint()
            for _bin in bins_list:
                if midpoint > _bin[0] and midpoint < _bin[1]: #inclusive
                    print('hit')
                    break


def main():
    '''main routine for egger'''   
    ###get args###
    genome_size = 1000000
    number_of_bins = 20
    annotations_path = '/home/thoboo/git/egger/example_data/sco_example.annotations'
    gbk_path = '/home/thoboo/git/egger/example_data/streptomyces_coelicolor.gb'
    ###get args###

    locus_list = annotation_reader.get_loci(annotations_path, gbk_path)
    bins_list = get_bins(genome_size, number_of_bins)
    histogram_data = populate_bins(locus_list, bins_list)
    
    ###plot histogram###
    #blah blah blah
    ###plot histogram###
    
    '''
    tests = ['aaa', 'bbb', 'ccc']
    test_classes = []
    for item in tests:
        test_classes.append(Locus(name=item))
    print(test_classes)
    '''

