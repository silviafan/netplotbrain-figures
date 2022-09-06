# Plotting a TemplateFlow atlas as circles, spheres, and parcels

# Import everything needed
import netplotbrain
import matplotlib.pyplot as plt

# Example node and edges dataframes

fig  = plt.figure()

# Circles
ax = fig.add_subplot(131, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='S',
                  nodetype='circles',
                  nodescale=40,
                  nodealpha=1,
                  arrowaxis=None,
                  title='circles',
                  fig=fig, ax=ax)

# Spheres
ax = fig.add_subplot(132, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='S',
                  nodetype='spheres',
                  nodealpha=1,
                  arrowaxis=None,
                  title='spheres',
                  fig=fig, ax=ax)

# Parcels
ax = fig.add_subplot(133, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle=None,
                  view='S',
                  nodetype='parcels',
                  nodealpha=1,
                  nodecolor='tab20c',
                  arrowaxis=None,
                  title='parcels',
                  fig=fig, ax=ax)

fig.savefig('./figures/node_types.png', dpi=300)

