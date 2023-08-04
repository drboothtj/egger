'''
produces sliding window graph and data
    functions: !!!
'''
from egger import io
from typing import Dict, List, Tuple
import plotly.graph_objects as go

def slide_window(
    data_points: List[Tuple[str, str, int]], record, categories: List[str],
    window_size: int, step_size: int
    ): #add return hint
    '''
    applies a sliding window to datapoints
        data_points: list of tuples describing the protein midpoint and annotation
        categories: a list of categories to plot
    returns:
        window_data: a list of tuples containing the window midpoint and the ...
    '''
    window_position = 0
    maximum_position = max([point[1] for point in data_points])
    ## ADD CHECK WINDOW SIZE FUNCTON
    if window_size is None:
        window_size = maximum_position/10
    if step_size is None:
        step_size = window_size/2
    ###
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
                try:
                    window_data[window_midpoint][data[2]] += 1 ##except key error split
                except KeyError:
                    for character in data[2]:
                        window_data[window_midpoint][character] += 1
        window_position += step_size
    return window_data

def get_window_data(records, categories, data_points, window_info) -> None:
    '''
    main routine for slide
        arguments:
        retruns: None
    '''
    all_window_data = []
    for record in records:
        data_points = [data for data in data_points if data[0] == record]
        window_data = slide_window(data_points, record, categories, window_info[0], window_info[1])
        all_window_data.append(window_data)
    return all_window_data

def plot_sliding_window(window_data: Dict, categories: List[str], filename: str) -> None:
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
    figure.write_html(filename)
    ##update figure with legends etc.
    ### Output Frame Plot Data ###

def output(contents: List[Dict], output):
    '''
     convert sliding window data into a list of lines for writing
        arguments: 
            contents: list of dictionarys containing window data
        returns:
            lines: list of lines
    '''
    lines = []
    for record in contents:
        #add record names
        for key in record.keys():
            line = [key]
            values = [x for x in record[key].values()]
            line.extend(values)
            lines.append(line)
    io.write_to_tsv(output, lines)
    