import bct
import numpy as np
import matplotlib.pyplot as plt
import netplotbrain

def generate_group_cm(nodes, subjects, community_size, community_str, scale=0.25, seed=2022):
    """
    Quick way to simulate group differences for visualization purposes.

    Input
    -----
    nodes : int
        number of nodes
    subjects : int
        number of subjects
    community_size : list
        list of number of nodes in each community
    community_str : list
        list of mean str for within community connections
    scale : float
        scale (STD) of normal distribution.
    """
    np.random.seed(seed)
    mu = np.zeros([nodes, nodes, 1])
    np.fill_diagonal(mu[:, :, 0], 1)
    ci = 0
    for i, c in enumerate(community_size):
        mu[ci:ci+c, ci:ci+c, :] = community_str[i]
        ci += c

    # Simulate data
    g = np.random.normal(mu, scale, size=[nodes, nodes, subjects])
    # Force to be symmetric
    ind_i, ind_j = np.triu_indices(g.shape[0], k=1)
    g[ind_j, ind_i] = g[ind_i, ind_j]
    return g

# Specify variable for generating data
nodes = 100
subjects_per_group = 50
community_size = [13, 7, 35, 15, 20, 5]

g1_community_str = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
g2_community_str = [0.17, 0.7, 0.13, 0.1, 0.15, 0.6]

g1 = generate_group_cm(nodes, subjects_per_group, community_size, g1_community_str)
g2 = generate_group_cm(nodes, subjects_per_group, community_size, g2_community_str)

# g1 and g2 are both (Node, Node, Subject) in size.
# The third input argument is the cluster threshold (set far too high here, but to ensure we just get the 2 extreme communities).
# Note, k=100 is set for speed purposes. Should be larger.  
p, adj, null = bct.nbs_bct(g1, g2, 4, k=100, seed=2022)

fig, ax = plt.subplots(1, 3)
ax[0].imshow(np.mean(g1, axis=-1), cmap='RdBu_r', vmin=-0.5, vmax=0.5)
ax[0].set_title('Group 1 (mean)')
ax[1].imshow(np.mean(g2, axis=-1), cmap='RdBu_r', vmin=-0.5, vmax=0.5)
ax[1].set_title('Group 2 (mean)')
ax[2].imshow(adj, cmap='binary')
ax[2].set_title('Significant Clusters')

# For out edges let's plot the group different.
gdif = np.mean(g2,axis=-1) - np.mean(g1,axis=-1)

fig, ax = netplotbrain.plot(template='MNI152NLin2009cAsym',
                            nodes={'atlas': 'Schaefer2018',
                                     'desc': '100Parcels7Networks',
                                     'resolution': 1},
                            edges=gdif,
                            highlight_edges=adj,
                            template_style='glass',
                            view=['LSR'],
                            title='NBS integration',
                            subtitles=None,
                            node_type='circles',                            
                            highlightlevel=0.5)