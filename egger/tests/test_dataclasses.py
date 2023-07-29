import unittest
from egger.dataclasses.locusclass import Locus, LocusError
from egger.dataclasses.binclass import Bin

class TestLocus(unittest.TestCase):

    def test_init(self):
        '''tests for locus input'''
        #first check a correctly formatted locus
        good_locus = Locus('name', 10, 100, 'A')
        assert good_locus.name == 'name'
        assert good_locus.start == 10
        assert good_locus.stop == 100
        assert good_locus.value == 'A'
        #then check for locus with flip start and stop locations
        with self.assertRaisesRegex(LocusError, 'after the stop'):
            bad_start_stop_locus = Locus('name', 100, 10, 'A')
        ##now check a locus with bad typing
        with self.assertRaisesRegex(TypeError, ''):
            bad_typing_locus = Locus('locus', 'one-hundered', 'ten' 'A') 

    def test_length(self):
        '''tests for Locus.length() function'''
        #test correct function
        good_locus = Locus('name', 10, 100, 'A')
        good_locus_length = good_locus.length()
        assert good_locus_length == 90
        #test bad start stop data
        bad_locus = Locus()
        bad_locus.start = 100
        bad_locus.stop = 10
        with self.assertRaisesRegex(LocusError, 'after the stop'):
            length = bad_locus.length()

    def test_midpoint(self):
        '''tests for the Locus.midpoint() function'''
        #test for correct calculation of midpoint
        locus_1 = Locus('name', 10, 100, 'A')
        midpoint_1 = locus_1.midpoint()
        assert midpoint_1 == 55
        #now test for correct return of float
        locus_2 = Locus('name', 10, 101, 'A')
        midpoint_2 = locus_2.midpoint()
        assert midpoint_2 == 55.5


        ###deal with switched values!