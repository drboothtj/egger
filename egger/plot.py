'''
plot graphs for egger
    functions:
        !!!
'''
from typing import Dict, List, Tuple
import plotly.graph_objects as go

def make_figure(window_data: Dict, categories: List[str]) -> None:
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
