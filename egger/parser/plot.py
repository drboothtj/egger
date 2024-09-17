'''
subparser for basic plot module of egger

functions:
xxxx
'''
def get_parser(subparsers):
    '''
    create the plot subparser
        arguments:
            subparsers: 
                the subparsers object from argparse
        returns:
            parser: 
                the parser for the plot module
    '''
    parser = subparsers.add_parser('plot', help='plots data from a single genome')

    parser.add_argument(
        '-a',
        '--annotations',
        type=str,
        default=None,
        help='path to a fasta file containing nucleotide sequences',
        required = True
        )
    parser.add_argument(
        '-g',
        '--genbank',
        type=str,
        default=None,
        help='path to a genbank file containing nucleotide sequences',
        required = True
        )
    parser.add_argument(
        '-c',
        '--category',
        type=str,
        default='COG_category',
        help='the category of annotations to plot (default: %(default)s)'
        )
    parser.add_argument(
        '-w',
        '--window-size',
        type=int,
        default=None,
        help='the category of annotations to plot (default: %(default)s)'
        )
    parser.add_argument(
        '-s',
        '--step-size',
        type=int,
        default=None,
        help='the category of annotations to plot (default: %(default)s)'
        )
    parser.add_argument(
        '-swp',
        '--sliding-window-plot',
        type=str,
        default = None,
        help='path to save the sliding window plot (default: %(default)s)'
        )
    parser.add_argument(
        '-swo',
        '--sliding-window-output',
        type=str,
        default = None,
        help='path to save the sliding window output data table (default: %(default)s)'
        )
    parser.add_argument(
        '-l',
        '--logging',
        help='the logging level for egger (default: %(default)s)'
        )
    return parser
