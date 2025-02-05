'''
egger: visualise eggnog-mapper data

functions:
    main() -> None
'''
from egger.window import window
from egger.compare import compare
from egger.parser import parser


## add logging
## figureout which categories we can chart
## finish parser - fix arguments to binary
## sort out architecture
## seriously clean up code
## specify an output directory

def main() -> None:
    '''
    main routine for egger
        returns:
            None
    '''
    args = parser.parse_args()
    if args.command == 'window':
        window.main(args)
    elif args.command == 'compare':
        compare.main(args)
    