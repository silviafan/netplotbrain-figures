# Plotting adult, infant, and brain templates pulled from TemplateFlow https://www.templateflow.org

# Import everything needed
import netplotbrain
import pandas as pd
import matplotlib.pyplot as plt

# Example node and edges dataframes

fig  = plt.figure()

# Adult brain
ax = fig.add_subplot(131, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                         'desc': '100Parcels7Networks',
                         'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle='surface',
                  view='S',
                  nodecolor='blue',
                  nodealpha=1,
                  nodescale=15,
                  arrowaxis=None,
                  showlegend=False,
                  subtitles='Adult template MNI152NLin6Asym',
                  fig=fig, ax=ax)

# Example node dataframe
nodes = pd.read_csv('./example_nodes.tsv', sep='\t', index_col=0)

# Rat template
nodes_whs = nodes.copy()
nodes_whs['x'] = nodes_whs['x'] / 8
nodes_whs['y'] = nodes_whs['y'] / 8
nodes_whs['z'] = nodes_whs['z'] / 8

ax = fig.add_subplot(132, projection='3d')
netplotbrain.plot(nodes=nodes_whs,
                  template='WHS',
                  templatestyle='surface',
                  templatealpha=0.3,
                  view='S',
                  nodescale=15,
                  nodecolor='blue',
                  nodealpha=1,
                  arrowaxis=None,
                  showlegend=False,
                  subtitles='Rat template WHS',
                  fig=fig, ax=ax)

# Infant template
nodes_inf = nodes.copy()
nodes_inf['x'] = nodes_inf['x'] / 1.25
nodes_inf['y'] = nodes_inf['y'] / 1.25
nodes_inf['z'] = nodes_inf['z'] / 1.25

# Setting a larger templatevoxsize will make it slightly quicker
ax = fig.add_subplot(133, projection='3d')
netplotbrain.plot(nodes=nodes_inf,
                  template='MNIInfant_cohort-3',
                  templatestyle='surface',
                  templatealpha=0.3,
                  view='S',
                  nodecolor='blue',
                  nodescale=15,
                  showlegend=False,
                  arrowaxis=None,
                  subtitles='Infant template MNIInfant',
                  fig=fig, ax=ax)

fig.savefig('./figures/diff_tftemplates.png', dpi=150)
