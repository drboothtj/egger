'''
perform spearman's rank correlation analysis for egger's compare module
    functions:
        !!!
'''
from typing import List, Dict

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import spearmanr, pearsonr
from scipy.cluster import hierarchy

def write_dendro_heatmap(correlation_matrix, labels: List, filename: str) -> None:
    '''
    creates and writes a dendrogram heatmap from the provided matrix
        arguments:
            correlation_matrix: a numpy matrix for all vs all spearmans or pearsons correlations
            labels: list of labels for the rows of the matrix
            filename: string for the filename prefix
        returns:
            None
    '''
    # Perform hierarchical clustering
    dendro = hierarchy.linkage(
        correlation_matrix, method='ward', optimal_ordering=True
        )  # check if ward is best!
    #dendro_idx = hierarchy.dendrogram(dendro, no_plot=True)['leaves']

    # Plot heatmap with dendrogram
    plt.figure(figsize=(10, 8))
    sns.clustermap(correlation_matrix, cmap='coolwarm', annot=False, fmt='.2e',
        cbar_kws={'label': 'Correlation'}, #fix
        xticklabels=labels,
        yticklabels=labels)
    plt.savefig(filename + '.svg')

def get_matracies(counters, categories, analysis_type):
    '''
    get the correlation and p-value matracies for Spearmans rank analysis
        arguments:
            !!!
        returns
    '''
    n_counters = len(counters)
    data = np.array([[counter.get(cat, 0) for cat in categories] for counter in counters])
    correlation_matrix = np.zeros((n_counters, n_counters))
    pvalue_matrix = correlation_matrix
    for i in range(n_counters):
        for j in range(i + 1, n_counters):
            if analysis_type == 'spearmans':
                correlation, pvalue = spearmanr(data[i], data[j])
            if analysis_type == 'pearsons':
                correlation, pvalue = pearsonr(data[i], data[j])
            #rais error if correlation None
            correlation_matrix[i, j] = correlation
            correlation_matrix[j, i] = correlation
            pvalue_matrix[i, j] = pvalue
            pvalue_matrix[j, i] = pvalue
    return correlation_matrix, pvalue_matrix

def rank(proteomes: List[Dict], categories: List, filename: str, analysis_type: str):
    '''
    perform an all vs. all spearmans rank analysis on provided annotated proteomes
        arguments:
            !!!
        returns:
            None
    '''
    labels = [proteome['name'] for proteome in proteomes]
    labels = [label[:10] for label in labels]
    counters = [proteome['category_counts'] for proteome in proteomes]

    correlation_matrix, pvalue_matrix = get_matracies(counters, categories, analysis_type)
    write_dendro_heatmap(correlation_matrix, labels, filename)
    #write matracies to file pvalues too!

    # add clustering output - do it later - difficult as requires thresholding
