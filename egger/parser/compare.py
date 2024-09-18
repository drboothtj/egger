'''
subparser for compare plot module of egger

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
                the parser for the compare module
    '''
    parser = subparsers.add_parser(
        'compare', help='plot data from multiple genomes and compare between them'
        )
    parser.add_argument(
        'annotations',
        nargs='+',
        default=None,
        help='paths to the eggnog annotations files to compare (default: %(default)s)'
    )
