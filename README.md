# netplotbrain: a showcase of visualization examples

### Import necessary packages and load data

```python

import netplotbrain
import pandas as pd
import numpy as np
import templateflow.api as tf
import itertools
import bct
import matplotlib.pyplot as plt

# Node and edge dataframes 

nodes = pd.read_csv('./example_nodes.tsv', sep='\t', index_col=0)
edges = pd.read_csv('./example_edges.tsv', sep='\t', index_col=0)
nodes_custom = pd.read_csv('./example_nodes_fig_4.csv', sep='\t', index_col=0)

```

### Plot each component separately and then all components together

```python
fig = plt.figure()

# Plot only template
ax = fig.add_subplot(141, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='surface',
                  template_alpha=0.08,
                  view='L',
                  arrowaxis=None,
                  title=None,
                  fig=fig, ax=ax)

# Plot only nodes
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},
                  template='MNI152NLin6Asym',
                  template_style=None,
                  template_alpha=0.08,
                  node_type='spheres',
                  view='L',
                  arrowaxis=None,
                  title=None,
                  fig=fig, ax=ax)
                  
# Plot only edges
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},                  
                 edges=edges,
                 template='MNI152NLin6Asym',
                 template_style=None,
                 view='L',
                 node_alpha=0,
                 edge_weights='weight',
                 arrowaxis=None,
                 title=None,
                 fig=fig, ax=ax)

# Plot template, nodes, and edges together
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},                                    
                 edges=edges,
                 template='MNI152NLin6Asym',
                 template_style='surface',
                 view='L',
                 node_type='spheres',
                 edge_weights='weight',
                 arrowaxis=None,
                 title=None,
                 fig=fig, ax=ax)
plt.show()
```
![](./figures/single_components.png)

### Plot different template styles

```python
# Plot glass style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='glass',
                  view='S',
                  arrowaxis=None,
                  title='glass',
                  subtitles=None)
 plt.show()
 ```
![](./figures/glass_template.png)

```python
# Plot surface style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='surface',
                  view='S',
                  arrowaxis=None,
                  title='surface',
                  subtitles=None)
plt.show()
 ```
![](./figures/surface_template.png)

```python
# Plot filled style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='filled',
                  view='S',
                  arrowaxis=None,
                  title='filled',
                  subtitles=None)
plt.show()
 ```
![](./figures/filled_template.png)

```python
# Plot cloudy style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='cloudy',
                  template_voxelsize=2,
                  template_alpha=0.065,
                  view='S',
                  template_edgethreshold=0.6,
                  arrowaxis=None,
                  title='cloudy',
                  subtitles=None)
plt.show()
```
![](./figures/cloudy_template.png)

### Plot different node types

```python
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
plt.show()
```
![](./figures/node_circles.png)

```python
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
plt.show()
```
![](./figures/node_spheres.png)

```python
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
plt.show()
```
![](./figures/node_parcels.png)

### Customize nodes

```python
# Plot 16 nodes with the same color
netplotbrain.plot(nodes=nodes_custom,
                  template='MNI152NLin6Asym',
                  view='S',
                  node_scale=50,
                  title=None,
                  arrowaxis=None)
plt.show()
```
![](./figures/node_same_color.png)

```python
# Plot 16 nodes colored by their community of origin
netplotbrain.plot(nodes=nodes_custom,
                  template='MNI152NLin6Asym',
                  view='S',
                  node_color='Community',
                  node_cmap='tab10',
                  node_scale=50,
                  title=None,
                  arrowaxis=None)
plt.show()
```
![](./figures/node_coloredby_comm.png)

```python
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
plt.show()
```
![](./figures/node_coloredby_comm_and_resized1.png)

```python
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
plt.show()
```
![](./figures/node_coloredby_comm_and_resized2.png)

### Plot different templates pulled from TemplateFlow

```python
# Adult brain MNI152NLin6Asym
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='glass',
                  view='L',
                  arrowaxis=None,
                  title='MNI152NLin6Asym',
                  subtitles=None)                
plt.show()
```
![](./figures/adultMNI.png)

```python
# Infant template MNIInfant_cohort-3
# Setting a larger templatevoxsize will make it slightly quicker
netplotbrain.plot(template='MNIInfant_cohort-3',
                  template_style='glass',
                  view='L',
                  arrowaxis=None,
                  title='MNIInfant_cohort-3',
                  subtitles=None)
plt.show()
```
![](./figures/infantMNIcohort3.png)

```python
# Rat template WHS
netplotbrain.plot(template='WHS',
                  template_style='glass',
                  view='L',
                  arrowaxis=None,
                  title='WHS',
                  subtitles=None)                  
plt.show()
```
![](./figures/ratWHS.png)               

```python
# Squirrel monkey VALiDATe29 
netplotbrain.plot(template='VALiDATe29',
                  template_style='glass',
                  view='L',
                  arrowaxis=None,
                  title='VALiDATe29',
                  subtitles=None)                  
plt.show()
```
![](./figures/squirrelmonkeyValidate29.png)

### Plot different views and rotations

#### Multiple views on multiple rows

```python
# 6 views
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
plt.show()
```
![](./figures/preset6.png)

```python
# 4 views
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
plt.show()
```
![](./figures/preset4.png)

#### AP rotation with 4 frames

```python
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
plt.show()
```
![](./figures/4framesrot.png)

#### AP rotation with 5 frames

```python
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
plt.show()
```
![](./figures/5framesrot.png)

### Spring layout subplot 

```python
# Set random seed for reproducibility
np.random.seed(2022)

# Download 100 nodes from the Schaefer atlas from templateflow
atlas = {'template': 'MNI152NLin2009cAsym',
         'atlas': 'Schaefer2018',
        'desc': '100Parcels7Networks'}
atlasinfo = tf.get(extension='.tsv', **atlas)
atlasinfo = pd.read_csv(atlasinfo, sep='\t')
# Resolution argument needed in atlas later nii.gz file
atlas['resolution'] = 1
# Parse the info in to get network names
networks = list(map(lambda x: x.split('_')[2], atlasinfo.name.values))
atlasinfo['yeo7networks'] = networks
# Rename longer network names
atlasinfo['yeo7networks'].replace('DorsAttn', 'DA', inplace=True)
atlasinfo['yeo7networks'].replace('SalVentAttn', 'VA', inplace=True)
atlasinfo['yeo7networks'].replace('Default', 'DMN', inplace=True)
atlasinfo['yeo7networks'].replace('SomMot', 'SM', inplace=True)

# Create empty cognitive matrix
edges = np.random.normal(0, 0.025, [100, 100])

# Set within network connectivity to be stronger
for network in atlasinfo['yeo7networks'].unique():
    idx =  atlasinfo[atlasinfo['yeo7networks']==network].index
    idx_pairs = np.array(list(itertools.combinations(idx, 2)))
    edges[idx_pairs[:, 0], idx_pairs[:, 1]] = np.random.normal(0.5, 0.025, [len(idx_pairs)])
    edges[idx_pairs[:, 1], idx_pairs[:, 0]] = np.random.normal(0.5, 0.025, [len(idx_pairs)])
    
# Plot it all
netplotbrain.plot(template='MNI152NLin2009cAsym',
                  nodes=atlas,
                  nodes_df=atlasinfo,
                  edges=edges,
                  view='LSs',
                  template_style='glass',
                  node_scale=20,
                  node_color='yeo7networks',
                  edge_threshold=0,
                  edge_alpha=0.2,
                  edge_thresholddirection='>',
                  seed=2022)
plt.show()
```
![](./figures/springlayout.png)

### Network based statistics 

```python
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
fig.show()
```
![](./figures/NBS.png)
