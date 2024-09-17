'''
plot bar charts for egger
    functions:
        !!!
'''
from collections import Counter
from typing import List, Tuple
import plotly.graph_objects as go
from egger.utils import io

def remove_dual_categories(category_count: Counter) -> Counter:
    '''
    removes items from a counter who's name is longer than 1 character
        arguments:
            category_count: !!!
        returns:
            category_count: !!!
    '''
    categories_to_remove = []
    for category in category_count:
        if len(category) > 1:
            categories_to_remove.append(category)
    for category in categories_to_remove:
        del category_count[category]
    return category_count

def count_dual_categories(categories: List[str]) -> List[str]:
    '''
    removes categories with more than one letter and adds to singles total
        arguments:
            categories: !!! 
        returns:
            new_categories: !!!
    '''
    dual_category = []
    for category in categories:
        if len(category) > 1:
            dual_category.append(category)
    #dual_counts = Counter([list(category) for category in dual_category])
    dual_category_for_counts = []
    for category in dual_category:
        dual_category_for_counts.extend(list(category))
    dual_category_counter = Counter(dual_category_for_counts)
    return dual_category_counter

def plot_bar_chart(data_points: List[Tuple[str, int, str]], records: List) -> None:
    '''
    plot the bar chart in plotly
        arguments: 
            data_points: list of tupples containing CDS record, midpoint and category
            records: list of record names
        returns:
            None
    '''
    figure = go.Figure()
    count_lines = []
    for record in records:
        categories = [datapoint[2] for datapoint in data_points if datapoint[0] == record]
        category_count = Counter(categories)
        category_count = remove_dual_categories(category_count)
        dual_category_count = count_dual_categories(categories)
        combined_count = category_count + dual_category_count
        sorted_count = sorted(combined_count.items())
        #plot the trace
        x_category = [item[0] for item in sorted_count]
        y_values = [item[1] for item in sorted_count]
        total_y_values = sum(y_values)
        y_values = [y_value/total_y_values*100 for y_value in y_values]
        figure.add_trace(go.Bar(x=x_category, y=y_values, name=record))
        #if asked for get data
        count_line = []
        count_line.append(record)
        count_line.extend(y_values)
        count_lines.append(count_line)
    #save the figure
    figure.write_html('barchart.html') #update when parsed argument
    #print data
    lines = []
    header = ['record']
    header.extend(x_category)
    lines.append(header)
    for line in count_lines:
        lines.append(line)
    io.write_to_tsv('barchart.tsv', lines)
