# This notebook goes through some simple netplotbrain examples to customize nodes 

# Import everything needed
import netplotbrain
import pandas as pd
import matplotlib.pyplot as plt

nodes_custom = pd.read_csv('./example_nodes_fig_4.csv', sep='\t', index_col=0)


# Plot 16 nodes with the same color
netplotbrain.plot(nodes=nodes_custom,
                  template='MNI152NLin6Asym',
                  view='S',
                  node_scale=50,
                  title=None,
                  arrowaxis=None)

plt.savefig('./figures/node_same_color.png', dpi=300)

# Plot 16 nodes colored by their community of origin
netplotbrain.plot(nodes=nodes_custom,
                  template='MNI152NLin6Asym',
                  view='S',
                  node_color='Community',
                  node_cmap='tab10',
                  node_scale=50,
                  title=None,
                  arrowaxis=None)

plt.savefig('./figures/node_coloredby_comm.png', dpi=300)


# Plot 16 nodes colored by their community of origin and re-sized according to centrality measure 1
netplotbrain.plot(nodes=nodes_custom,
                  template='MNI152NLin6Asym',
                  view='S',
                  node_color='Community',
                  node_cmap='tab10',
                  node_size='Measure-1',
                  node_scale=50,
                  title=None,
                  arrowaxis=None)

plt.savefig('./figures/node_coloredby_comm_and_resized1.png', dpi=300)

# Plot 16 nodes colored by their community of origin and re-sized according to centrality measure 2
netplotbrain.plot(nodes=nodes_custom,
                  template='MNI152NLin6Asym',
                  view='S',
                  node_color='Community',
                  node_cmap='tab10',
                  node_size='Measure-2',
                  node_scale=50,
                  title=None,
                  arrowaxis=None)

plt.savefig('./figures/node_coloredby_comm_and_resized2.png', dpi=300)