from dataclasses import dataclass
from egger.dataclasses.locusclass import Locus
from typing import List

@dataclass
class Bin():
    start: int
    stop: int
    locus_list: List[Locus]

    def locus_count(self):
        '''
        count the total number of loci in this bin
        '''
        pass

    def get_values(self):
        pass
