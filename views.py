# Plotting different views and rotations

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

edges = pd.read_csv('./edges.tsv', sep='\t', index_col=0)

# Multiple views on multiple rows
netplotbrain.plot(nodes=atlasinfo,
                  nodeimg={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  edges=edges,
                  edgescale=5,
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  template_glass_maxalpha=0.03,
                  view=['LSR', 'AIP'],
                  nodecolorby='yeo7networks',
                  nodecmap='inferno',
                  nodetype='circles',
                  nodescale=10,
                  nodealpha=1,
                  showlegend=False)

plt.savefig('./figures/views.png', dpi=150)

# Rotations AP with 6 frames
netplotbrain.plot(nodes=atlasinfo,
                  nodeimg={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  edges=edges,
                  edgescale=5,
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  template_glass_maxalpha=0.03,
                  templatecolor='black',
                  view=['AP'],
                  frames=6,
                  nodecolorby='yeo7networks',
                  nodecmap='cividis',
                  nodetype='circles',
                  nodescale=10,
                  nodealpha=1,
                  showlegend=False)

plt.savefig('./figures/rotation_6frames.png', dpi=150)

# Rotations AP with 4 frames
netplotbrain.plot(nodes=atlasinfo,
                  nodeimg={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  edges=edges,
                  edgescale=5,
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  template_glass_maxalpha=0.03,
                  templatecolor='black',
                  view=['AP'],
                  frames=4,
                  nodecolorby='yeo7networks',
                  nodecmap='cividis',
                  nodetype='circles',
                  nodescale=10,
                  nodealpha=1,
                  showlegend=False)

plt.savefig('./figures/rotation_4frames.png', dpi=150)
