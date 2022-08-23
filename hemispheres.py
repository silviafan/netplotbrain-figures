# Plotting different template styles

# Import everything needed
import netplotbrain
import pandas as pd
import matplotlib.pyplot as plt

# Example node and edges dataframes

edges = pd.read_csv('./example_edges.tsv', sep='\t', index_col=0)
nodes = pd.read_csv('./example_nodes.tsv', sep='\t', index_col=0)

netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='surface',
                  view=['SSS'],
                  hemisphere=['L', 'R', ''],
                  nodecolor='darkcyan',
                  subtitles=['left hemisphere', 'right hemisphere', 'whole brain'],
                  nodes=nodes,
                  arrowaxis=None,
                  edges=edges)

plt.savefig('./figures/hemispheres.png', dpi=300)