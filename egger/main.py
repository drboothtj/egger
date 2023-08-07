'''
egger: visualise eggnog-mapper data

functions:
    !!!!!!!!
'''
from egger import chart, parser, process, slide

## add logging
## add error
## figureout which categories we can chart
## finish parser - fix arguments to binary
## sort out architecture
## seriously clean up code
## make plots pretty
## specify an output directory

def main() -> None:
    '''
    main routine for egger
        arguments:
            annotation_filename: path to .annotations file
            gbk_filename: path to .gbk file
            annotation_type: annotation header to plot
        returns:
            None
    '''
    ### Get args -- move to parser
    args = parser.parse_args()
    annotation_filename = args.annotations
    gbk_filename = args.genbank
    annotation_type = args.category
    window_info = args.window_size, args.step_size
    sw_output = args.sliding_window_output #os.path!
    sw_plot = args.sliding_window_plot #os.path!
    if sw_plot is None and sw_output is None: ## UPDATE FOR BAR CHART
        print('No output specified. Exiting...')
        exit() #raise error instead
    ### Combine data from .annotation and .gbk ###
    data_points, categories, records = process.process(
        annotation_filename, gbk_filename, annotation_type
        )
    ### Make Bar Chart
    bar.plot_bar_chart(data_points, records)
    ### Make frame plots for each record ###
    if sw_plot or sw_output:
        for record in records:
            window_data = slide.get_window_data(record, categories, data_points, window_info) 
            #parse out slide.get_window_data and slide.slide_window
            if sw_plot:
                slide.plot_sliding_window(window_data, categories, sw_plot, record)
            if sw_output:
                slide.output(window_data, sw_output, record)
    print('egger is done!')
