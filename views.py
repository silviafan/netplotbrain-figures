# Plotting different views and rotations

# Import everything needed
import netplotbrain
import pandas as pd
import matplotlib.pyplot as plt

nodes = pd.read_csv('./example_nodes.tsv', sep='\t', index_col=0)
edges = pd.read_csv('./example_edges.tsv', sep='\t', index_col=0)


# 6 views on multiple rows
netplotbrain.plot(nodes=nodes,
                  edges=edges,
                  edge_scale=5,
                  template='MNI152NLin6Asym',
                  template_style='glass',
                  view='preset-6',
                  node_color='community',
                  node_cmap='viridis',
                  node_scale=30,
                  node_alpha=1,
                  arrowaxis=None,
                  showlegend=False)

plt.savefig('./figures/preset6.png', dpi=300)

# 4 views on multiple rows
netplotbrain.plot(nodes=nodes,
                  edges=edges,
                  edge_scale=5,
                  template='MNI152NLin6Asym',
                  template_style='glass',
                  view='preset-4',
                  node_color='community',
                  node_cmap='viridis',
                  node_scale=30,
                  node_alpha=1,
                  arrowaxis=None,
                  showlegend=False)

plt.savefig('./figures/preset4.png', dpi=300)

# Rotations AP with 4 frames
netplotbrain.plot(nodes=nodes,
                  edges=edges,
                  edge_scale=5,
                  template='MNI152NLin6Asym',
                  template_style='glass',
                  view='AP',
                  frames=4,
                  node_color='community',
                  node_cmap='viridis',
                  node_scale=30,
                  node_alpha=1,
                  showlegend=False)

plt.savefig('./figures/4framesrot.png', dpi=300)

# Rotations AP with 5 frames
netplotbrain.plot(nodes=nodes,
                  edges=edges,
                  edge_scale=5,
                  template='MNI152NLin6Asym',
                  template_style='glass',
                  view='AP',
                  frames=5,
                  node_color='community',
                  node_cmap='viridis',
                  node_scale=30,
                  node_alpha=1,
                  showlegend=False)

plt.savefig('./figures/5framesrot.png', dpi=300)
