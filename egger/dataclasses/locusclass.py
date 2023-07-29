from dataclasses import dataclass

class LocusError(Exception):
    '''Called if there is a problem with locus information'''
    pass

@dataclass
class Locus():
    '''
    dataclass for locus information
        Arguments:
            name: the name of the locus
            start: the start location as an integer
            stop: the stop location as an integer
            value: the value assigned to the locus by emapper
    '''

    #figure out how to make perminant i.e. cannot add attributes

    def __init__(self, name: str=None, start: int=None, stop: int=None, value: str=None):
        self.name = name
        self.start = start
        self.stop = stop 
        self.value = value

    def check_start_stop(self):
        '''
        check to avoid issues with start and stop values
        '''
        assert self.start
        assert self.stop
        self.start is not None and self.stop is not None:
            if self.start > self.stop:
                raise LocusError('The start point of the locus is after the stop point!')

    def length(self) -> int:
        '''return the length of the locus
            Arguments: 
                self: Locus object
            Returns:
               length: the length of the locus in base pairs'''
        self.check_start_stop()
        length = self.stop - self.start 
        return length

    def midpoint(self) -> float:
        '''return the midpoint of the locus
            Arguments: 
                self: Locus object
            Returns:
                midpoint: the midpoint of the gene as a float'''
        self.check_start_stop()
        midpoint = self.start + self.length()/2
        return midpoint
