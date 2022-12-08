# Plotting a TemplateFlow atlas as circles, spheres, and parcels

# Import everything needed
import netplotbrain
import matplotlib.pyplot as plt

# Circles
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  template='MNI152NLin6Asym',
                  template_style='glass',
                  view='S',
                  node_type='circles',
                  node_scale=40,
                  node_alpha=1,
                  arrowaxis=None,
                  title='circles',
                  subtitles=None)

plt.savefig('./figures/node_circles.png', dpi=300)

# Spheres
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  template='MNI152NLin6Asym',
                  template_style='glass',
                  view='S',
                  node_type='spheres',
                  node_alpha=1,
                  arrowaxis=None,
                  title='spheres',
                  subtitles=None)

plt.savefig('./figures/node_spheres.png', dpi=300)

# Parcels
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},
                  template='MNI152NLin6Asym',
                  template_style=None,
                  view='S',
                  node_type='parcels',
                  node_alpha=1,
                  node_color='tab20c',
                  arrowaxis=None,
                  title='parcels',
                  subtitles=None)

plt.savefig('./figures/node_parcels.png', dpi=300)

