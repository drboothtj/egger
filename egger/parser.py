'''
args parser for egger
    functions:
        get_parser()
        parse_args
'''
import argparse

def get_parser():
    ''''Create a parser object specific to skewer'''
    parser = argparse.ArgumentParser(
        "egger",
        description=
        "egger: a python package to visualise eggnog annotations.",
        epilog="Written by Dr. Thom Booth, 2023."
        )
    parser.add_argument(
        '-a',
        '--annotations',
        type=str,
        default=None,
        help='path to a fasta file containing nucleotide sequences'
        )
    parser.add_argument(
        '-g',
        '--genbank',
        type=str,
        default=None,
        help='path to a genbank file containing nucleotide sequences'
        )
    parser.add_argument(
        '-c',
        '--category',
        type=str,
        default='COG_category',
        help='the category of annotations to plot (default: )'
        )
    parser.add_argument(
        '-w',
        '--window-size',
        type=int,
        default=None,
        help='the category of annotations to plot (default: )'
        )
    parser.add_argument(
        '-s',
        '--step-size',
        type=int,
        default=None,
        help='the category of annotations to plot (default: )'
        )
    parser.add_argument(
        '-p',
        '--plot',
        action='store_true',
        help='the category of annotations to plot (default: )'
        )
    parser.add_argument(
        '-o',
        '--output',
        action='store_true',
        help='the category of annotations to plot (default: )'
        )
    parser.add_argument(
        '-l',
        '--logging',
        help='the logging level for egger (default: )'
        )
    return parser

def parse_args():
    '''get the arguments from the console via the parser'''
    parser = get_parser()
    args = parser.parse_args()
    return args
    