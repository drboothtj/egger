'''
plot bar charts for egger
    functions:
        !!!
'''
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict
from collections import Counter

def draw_barchart(labels: List, counters: List[Counter], categories: List, filename: str) -> None:
    '''
    Uses matplotlib to draw a bar chart
    '''
    data = np.array([[counter.get(category, 0) for category in categories] for counter in counters])
    # Set up parameters for the plot
    fig, ax = plt.subplots(figsize=(10, 6)) #maybe change the size?
    n_counters = len(counters)
    bar_width = 10 / (n_counters * 12) #adjust the bar width to the number of samples
    index = np.arange(len(categories))
    # Plot each counter
    for i in range(n_counters):
        ax.bar(index + i * bar_width, data[i], bar_width, label=labels[i]) #color=colors[i]
    # Add labels and titles
    ax.set_xlabel('COG Category')
    ax.set_ylabel('Count')
    ax.set_xticks(index + bar_width * (n_counters / 2 - 0.5))
    ax.set_xticklabels(categories)
    ax.legend(title="Source")
    # Save as svg
    plt.savefig(filename + '.svg') #add options

def plot_bar_chart(proteomes: List[Dict], categories, filename: str) -> None:
    '''
    plot the bar chart in plotly
        arguments: 
            !!!
        returns:
            None
    '''
    labels = [proteome['name'] for proteome in proteomes]
    counters = [proteome['category_counts'] for proteome in proteomes]
    draw_barchart(labels, counters, categories, filename)
