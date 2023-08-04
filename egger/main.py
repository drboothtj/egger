'''
egger: visualise eggnog-mapper data

functions:
    !!!!!!!!
'''
from egger import parser, process, slide

### ADD OTHER FUNCTIONS -list headers -extract-fasta-from-gbk
## add logging
## add error
## plot bar chart and write data
## figureout which categories we can chart
## finish parser make plot used <-
## sort out architecture
## seriously clean up code

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
    #plot.plot_bar_chart(data_points)
    ### Make frame plots for each record ###
    if sw_plot or sw_output:
        all_window_data = slide.get_window_data(records, categories, data_points, window_info)
        for window_data in all_window_data:
            if sw_plot:
                slide.plot_sliding_window(window_data, categories, sw_plot)
            if sw_output:
                slide.output(all_window_data, sw_output)
    print('egger is done!')
