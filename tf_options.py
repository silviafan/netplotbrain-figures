# Plotting adult, infant, and brain templates pulled from TemplateFlow https://www.templateflow.org

# Import everything needed
import netplotbrain
import pandas as pd
import matplotlib.pyplot as plt
import templateflow.api as tf

# Example node and edges dataframes
atlasinfo = tf.get(template='MNI152NLin6Asym',
       atlas='Schaefer2018',
       desc='100Parcels7Networks',
       extension='.tsv')
atlasinfo = pd.read_csv(atlasinfo, sep='\t')
# Parse the info in to get network names
networks = list(map(lambda x: x.split('_')[2], atlasinfo.name.values))
atlasinfo['yeo7networks'] = networks

# Example node and edges dataframes

fig  = plt.figure()

# Adult brain
ax = fig.add_subplot(131, projection='3d')
netplotbrain.plot(nodes=atlasinfo,
                  nodeimg={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  template_glass_maxalpha=0.05,
                  templatecolor='black',
                  view='R',
                  nodecolorby='yeo7networks',
                  nodecmap='Set3',
                  nodetype='spheres',
                  nodealpha=0.4,
                  arrowaxis=[],
                  showlegend=False,
                  title='Adult template',
                  fig=fig, ax=ax)

# Example node dataframe
nodes = pd.read_csv('./nodes.tsv', sep='\t', index_col=0)

# Rat template
nodes_whs = nodes.copy()
nodes_whs['x'] = nodes_whs['x'] / 8
nodes_whs['y'] = nodes_whs['y'] / 8
nodes_whs['z'] = nodes_whs['z'] / 8

ax = fig.add_subplot(132, projection='3d')
netplotbrain.plot(nodes=nodes_whs,
                  template='WHS',
                  templatestyle='surface',
                  templatecolor='black',
                  templatevoxsize=0.2,
                  view='S',
                  nodescale=20,
                  nodecolorby='community',
                  nodealpha=1,
                  arrowaxis=[],
                  showlegend=False,
                  title='Rat template',
                  fig=fig, ax=ax)

# Infant template
nodes_inf = nodes.copy()
nodes_inf['x'] = nodes_inf['x'] / 1.25
nodes_inf['y'] = nodes_inf['y'] / 1.25
nodes_inf['z'] = nodes_inf['z'] / 1.25

# Setting a larger templatevoxsize will make it slightly quicker
ax = fig.add_subplot(133, projection='3d')
netplotbrain.plot(nodes=nodes_inf,
                  template='MNIInfant',
                  templatestyle='filled',
                  templatecolor='black',
                  view='L',
                  nodecolorby='community',
                  nodescale=40,
                  templatevoxsize=1,
                  showlegend=False,
                  arrowaxis=[],
                  title='Infant template',
                  fig=fig, ax=ax)

fig.savefig('./figures/diff_tftemplates.png', dpi=150)

