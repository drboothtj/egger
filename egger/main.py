'''
egger: visualise eggnog-mapper data

functions:
    !!!!!!!!
'''
import sys
from typing import Dict, List, Tuple
from egger import io, process
import plotly.graph_objects as go


### SORT OUT ARCHITECTURE!
###MAKE A PROPER PARSER
### ADD OTHER FUNCTIONS -list headers -extract-fasta-from-
##add logging
##add errors
##write raw data

ANNOTATION_FILE = sys.argv[1]
GBK_FILE = sys.argv[2]
ANNOTATION_TYPE = sys.argv[3]
#NUMBER_OF_BINS = sys.argv[4]
### WINDOW_SIZE

def slide_window(data_points: List[Tuple[str, str, int]], categories: List[str]): #add return hint
    '''
    applies a sliding window to datapoints
        data_points: list of tuples describing the protein midpoint and annotation
        categories: a list of categories to plot
    returns:
        window_data: a list of tuples containing the window midpoint and the ...
    '''
    window_size = 50000 ## catch stupid window size
    window_position = 0
    maximum_position = max([point[1] for point in data_points])
    window_data = {}
    while window_position < maximum_position:
        window_end = window_position + window_size
        window_midpoint = window_position + window_size / 2
        #print(
        #    'window start: %s, window_end: %s, window_midopoint; %s'
        #    % (window_position, window_end, window_midpoint)
        #    )
        #print(maximum_position)
        window_data[window_midpoint] = {category: 0 for category in categories}
        for data in data_points:
            if window_position < data[1] < window_end: #check if missing or counted twice in between
                window_data[window_midpoint][data[2]] += 1 ##except key error split
        window_position += window_size
    return window_data

def make_figure(window_data: Dict) -> None:
    '''
    make and write plotly graph object from traces
        arguments: 
            window_data: List of graph objects for each category to be plotted
        returns:
            None
    '''
    figure_title = f'Distribution of XXX in XXX.' ## add to figure
    figure = go.Figure()
    for category in categories:
        x_values = list(window_data.keys())
        y_values = [window_data[x_value][category] for x_value in x_values]
        trace = go.Scatter(x=x_values, y=y_values, mode="lines", name=category)
        figure.add_trace(trace)
    figure.write_html('plot.html')
    ##update figure with legends etc.

def plot_data(data_points, record) -> None:
    '''
    plots datapoints for a given record
        arguments:
            datapoints: list of tuples describing the protein midpoint and annotation
            record: the record to plot
        returns:
            None
    '''
    data_to_plot = [data for data in data_points if data[0] == record]
    categories = set([data[2] for data in data_points])
    categories = ''.join(categories)
    categories = set(categories)
    window_data = slide_window(data_to_plot, categories) ### CONTINUE FROM HERE
    make_figure(window_data)

def main(annotation_filename: str, gbk_filename: str, annotation_type: str) -> None:
    '''
    main routine for egger
        arguments:
            annotation_filename: path to .annotations file
            gbk_filename: path to .gbk file
            annotation_type: annotation header to plot
        returns:
            None
    '''
    ### Combine data from .annotation and .gbk ###
    lines = io.read_tsv(annotation_filename)
    annotations = process.process_headers(lines)
    proteins = process.convert_annotations_to_dictionary(annotations)
    proteins = process.add_location_data(gbk_filename, proteins)
    data_points = process.get_data_for_plot(proteins, annotation_type)

    ### Write datapoint to file
    ### DO THIS!

    ### Make plots for each record ###
    records = set([point[0] for point in data_points])
    for record in records:
        plot_data(data_points, record)

    #bin data?
    #make plots

main(ANNOTATION_FILE, GBK_FILE, ANNOTATION_TYPE) #NUMBER_OF_BINS
