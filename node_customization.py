# This notebook goes through some simple netplotbrain examples to customize nodes 

# Import everything needed
import netplotbrain
import pandas as pd
import matplotlib.pyplot as plt

nodes = pd.read_csv('./example_nodes.tsv', sep='\t', index_col=0)

fig  = plt.figure()

# Plot 16 nodes with the same color
ax = fig.add_subplot(131, projection='3d')
netplotbrain.plot(nodes=nodes,
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='S',
                  nodetype='spheres',
                  nodecolor='magenta',
                  nodealpha=0.1,
                  highlightnodes=[1,5,9,13,16,18,19,20,21,24,23,26,28,30,31,32], 
                  arrowaxis=None,
                  subtitles=None,
                  fig=fig, ax=ax)

# Plot 16 nodes colored by their community of origin
ax = fig.add_subplot(132, projection='3d')
netplotbrain.plot(nodes=nodes,
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='S',
                  nodetype='spheres',
                  highlightnodes=[1,5,9,13,16,18,19,20,21,24,23,26,28,30,31,32], 
                  nodecolor='community',
                  nodecmap='cool',
                  nodealpha=0.1,
                  arrowaxis=None,
                  subtitles=None,
                  nodecolorlegend=False,
                  fig=fig, ax=ax)

# Plot 16 nodes colored by their community of origin and re-sized according to centrality measure
ax = fig.add_subplot(133, projection='3d')
netplotbrain.plot(nodes=nodes,
                  template='MNI152NLin6Asym',
                  templatestyle='glass', 
                  view='S',
                  highlightnodes=[1,5,9,13,16,18,19,20,21,24,23,26,28,30,31,32],
                  nodetype='spheres', 
                  nodecolor='community',
                  nodecmap='cool',
                  nodesize='centrality_measure2',
                  nodealpha=0.1,
                  nodescale=9,
                  subtitles=None,
                  arrowaxis=None,
                  nodecolorlegend=False,
                  nodesizelegend=False,
                  fig=fig, ax=ax)

fig.savefig('./figures/nodes_customization.png', dpi=300)
