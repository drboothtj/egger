'''
perform spearman's rank correlation analysis for egger's compare module
    functions:
        !!!
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict
from scipy.stats import spearmanr, pearsonr
from scipy.cluster import hierarchy

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
            correlation_matrix[i, j] = correlation
            correlation_matrix[j, i] = correlation
            pvalue_matrix[i, j] = pvalue
            pvalue_matrix[j, i] = pvalue
    return correlation_matrix ,pvalue_matrix

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

    # Perform hierarchical clustering
    dendro = hierarchy.linkage(correlation_matrix, method='ward')  # check if ward is best!
    dendro_idx = hierarchy.dendrogram(dendro, no_plot=True)['leaves']  

    # Plot heatmap with dendrogram
    plt.figure(figsize=(10, 8))
    sns.clustermap(correlation_matrix, cmap='coolwarm', annot=True, fmt='.2e',
        cbar_kws={'label': 'Spearman\'s Rank Correlation'}, #fix 
        xticklabels=labels,
        yticklabels=labels)
    plt.title('Heatmap of Spearman\'s Rank Correlation with Hierarchical Clustering') # fix
    plt.savefig(filename + '.png')