# Plot each component individually and then together

# Import everything needed
import netplotbrain
import pandas as pd
import matplotlib.pyplot as plt

# Example edges dataframe

edges = pd.read_csv('./example_edges.tsv', sep='\t', index_col=0)

fig  = plt.figure()

# Plot only template
ax = fig.add_subplot(141, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='surface',
                  template_alpha=0.08,
                  view='L',
                  arrowaxis=None,
                  title=None,
                  fig=fig, ax=ax)

# Plot only nodes
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},
                  template='MNI152NLin6Asym',
                  template_style=None,
                  template_alpha=0.08,
                  node_type='spheres',
                  view='L',
                  arrowaxis=None,
                  title=None,
                  fig=fig, ax=ax)
# Plot only edges
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},                  
                 edges=edges,
                 template='MNI152NLin6Asym',
                 template_style=None,
                 view='L',
                 node_alpha=0,
                 edge_weights='weight',
                 arrowaxis=None,
                 title=None,
                 fig=fig, ax=ax)

# Plot template, nodes, and edges together
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},                                    
                 edges=edges,
                 template='MNI152NLin6Asym',
                 template_style='surface',
                 view='L',
                 node_type='spheres',
                 edge_weights='weight',
                 arrowaxis=None,
                 title=None,
                 fig=fig, ax=ax)

fig.savefig('./figures/single_components.png', dpi=300)