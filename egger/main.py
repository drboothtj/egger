'''
egger: visualise eggnog-mapper data

functions:
    !!!!!!!!
'''
from egger import io, parser, process, plot

### ADD OTHER FUNCTIONS -list headers -extract-fasta-from-gbk
## add logging
## add errors
## write raw data
### add bar chart for all contigs
### sort out architecture

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
    ### Get args
    args = parser.parse_args()
    annotation_filename = args.annotations
    gbk_filename = args.genbank
    annotation_type = args.category
    window_size = args.window_size
    step_size = args.step_size
    ### Combine data from .annotation and .gbk ###
    lines = io.read_tsv(annotation_filename)
    annotations = process.process_headers(lines)
    proteins = process.convert_annotations_to_dictionary(annotations)
    proteins = process.add_location_data(gbk_filename, proteins)
    data_points = process.get_data_for_plot(proteins, annotation_type)
    ### ADD WRITE DATAPOINTS
    categories = process.get_categorys(data_points)
    records = set([point[0] for point in data_points])   
    ### Make plots for each record ###
    for record in records:
        data_points = [data for data in data_points if data[0] == record]
        window_data = process.slide_window(data_points, record, categories, window_size, step_size)
        plot.make_figure(window_data, categories)
    print('egger is done!')
