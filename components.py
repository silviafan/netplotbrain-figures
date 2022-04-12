# This notebook goes through some netplotbrain examples to plot each component individually and then together

# Import everything needed
import numpy as np
import netplotbrain
import pandas as pd
import matplotlib.pyplot as plt

# Example node and edges dataframes
url = 'https://raw.githubusercontent.com/ThomasYeoLab/CBIG/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/MNI/Centroid_coordinates/Schaefer2018_100Parcels_7Networks_order_FSLMNI152_2mm.Centroid_RAS.csv'
nodes = pd.read_csv(url,index_col=0, parse_dates=[0])
nodes.columns = ['name', 'x', 'y', 'z']
networks = list(map(lambda x: x.split('_')[2], nodes.name.values))
nodes['community'] = networks

edges = pd.read_csv('./edges.tsv', sep='\t', index_col=0)

fig  = plt.figure()

# Plot only template
ax = fig.add_subplot(141, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='surface',
                  templatealpha=0.08,
                  view='L',
                  arrowaxis=[],
                  title='',
                  fig=fig, ax=ax)

# Plot only nodes
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(nodes=nodes,
                 template='MNI152NLin6Asym',
                 templatestyle=None,
                 view='L',
                 nodetype='spheres',
                 nodecolor='Salmon',
                 arrowaxis=[],
                 title='',
                 fig=fig, ax=ax)

# Plot only edges
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(nodes=nodes,
                 edges=edges,
                 template='MNI152NLin6Asym',
                 templatestyle=None,
                 view='L',
                 nodealpha=0,
                 edgeweights='weight',
                 edgealpha=5,
                 arrowaxis=[],
                 title='',
                 fig=fig, ax=ax)

# Plot template, nodes, and edges together
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(nodes=nodes,
                 edges=edges,
                 template='MNI152NLin6Asym',
                 templatestyle='surface',
                 templatealpha=0.07,
                 view='L',
                 nodetype='spheres',
                 nodecolor='Salmon',
                 edgeweights='weight',
                 edgealpha=5,
                 arrowaxis=[],
                 title='',
                 fig=fig, ax=ax)

fig.savefig('./figures/showcase.png', dpi=150)