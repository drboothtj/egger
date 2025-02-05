'''
egger: visualise eggnog-mapper data

functions:
    main() -> None
'''
from egger.window import window
from egger.compare import compare
from egger.parser import parser

## TODO
## add logging
## figureout which other categories we can chart
## change arguments to binary instead of prefix input
## specify an output directory
## produce percentage counts for each category

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
    
