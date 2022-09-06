# netplotbrain: a showcase of visualization examples

### Import necessary packages and load data

```python

import netplotbrain
import pandas as pd
import numpy as np
import templateflow.api as tf
import itertools
import matplotlib.pyplot as plt

# Node and edge dataframes 

nodes = pd.read_csv('./example_nodes.tsv', sep='\t', index_col=0)
edges = pd.read_csv('./example_edges.tsv', sep='\t', index_col=0)

```

### Plot each component separately and then all components together

```python
fig = plt.figure()

# Plot only template
ax = fig.add_subplot(141, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='surface',
                  templatealpha=0.08,
                  view='L',
                  arrowaxis=None,
                  subitles=None,
                  fig=fig, ax=ax)

# Plot only nodes
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle=None,
                  templatealpha=0.08,
                  nodetype='spheres',
                  view='L',
                  arrowaxis=None,
                  subtitles=None,
                  fig=fig, ax=ax)
                  
# Plot only edges
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},                  
                 edges=edges,
                 template='MNI152NLin6Asym',
                 templatestyle=None,
                 view='L',
                 nodealpha=0,
                 edgeweights='weight',
                 edgealpha=5,
                 arrowaxis=None,
                 subtitles=None,
                 fig=fig, ax=ax)

# Plot template, nodes, and edges together
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},                                    
                 edges=edges,
                 template='MNI152NLin6Asym',
                 templatestyle='surface',
                 templatealpha=0.08,
                 view='L',
                 nodetype='spheres',
                 nodecolor='Salmon',
                 edgeweights='weight',
                 edgealpha=5,
                 arrowaxis=None,
                 subtitles=None,
                 fig=fig, ax=ax)
plt.show()
```
![](./figures/single_components.png)

### Plot different template styles

```python
fig = plt.figure()

# Plot glass style 
ax = fig.add_subplot(141, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='S',
                  arrowaxis=None,
                  subtitles='glass',
                  fig=fig, ax=ax)

# Plot surface style 
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='surface',
                  view='S',
                  arrowaxis=None,
                  subtitles='surface',
                  fig=fig, ax=ax)

# Plot filled style 
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='filled',
                  view='S',
                  arrowaxis=None,
                  subtitles='filled',
                  fig=fig, ax=ax)

# Plot cloudy style 
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='cloudy',
                  templatevoxelsize=2,
                  templatealpha=0.065,
                  view='S',
                  templateedgethreshold=0.6,
                  arrowaxis=None,
                  subtitles='cloudy',
                  fig=fig, ax=ax)
plt.show()
```
![](./figures/template_styles.png)

### Plot different node types

```python
fig = plt.figure()

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
                  subtitles='circles',
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
                  subtitles='spheres',
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
                  subtitles='parcels',
                  fig=fig, ax=ax)

plt.show()
```
![](./figures/node_types.png)

### Customize nodes

```python
fig = plt.figure()

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
               
plt.show()
```
![](./figures/nodes_customization.png)

### Plot different templates pulled from TemplateFlow

```python
fig = plt.figure()

# Adult brain MNI152NLin6Asym
ax = fig.add_subplot(141, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='L',
                  arrowaxis=None,
                  subtitles='MNI152NLin6Asym',
                  fig=fig, ax=ax)

# Infant template MNIInfant_cohort-3
# Setting a larger templatevoxsize will make it slightly quicker
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(template='MNIInfant_cohort-3',
                  templatestyle='glass',
                  view='L',
                  arrowaxis=None,
                  subtitles='MNIInfant_cohort-3',
                  fig=fig, ax=ax)

# Rat template WHS
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(template='WHS',
                  templatestyle='glass',
                  view='L',
                  arrowaxis=None,
                  subtitles='WHS',
                  fig=fig, ax=ax)

# Squirrel monkey VALiDATe29 
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(template='VALiDATe29',
                  templatestyle='glass',
                  view='L',
                  arrowaxis=None,
                  subtitles='VALiDATe29',
                  fig=fig, ax=ax)
                  
plt.show()
```
![](./figures/diff_tftemplates.png)

### Plot different views and rotations

#### Multiple views on multiple rows

```python
# 6 views
netplotbrain.plot(nodes=nodes,
                  edges=edges,
                  edgescale=5,
                  edgealpha=3,
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='preset-6',
                  nodecolor='community',
                  nodecmap='viridis',
                  nodetype='circles',
                  nodescale=30,
                  nodealpha=1,
                  arrowaxis=None,
                  showlegend=False)
                  
plt.show()
```
![](./figures/preset6.png)

```python
# 4 views
netplotbrain.plot(nodes=nodes,
                  edges=edges,
                  edgescale=5,
                  edgealpha=3,
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='preset-4',
                  nodecolor='community',
                  nodecmap='viridis',
                  nodetype='circles',
                  nodescale=30,
                  nodealpha=1,
                  arrowaxis=None,
                  showlegend=False)
                  
plt.show()
```
![](./figures/preset4.png)

#### AP rotation with 4 frames

```python
netplotbrain.plot(nodes=nodes,
                  edges=edges,
                  edgescale=5,
                  edgealpha=3,
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view=['AP'],
                  frames=4,
                  nodecolor='community',
                  nodecmap='viridis',
                  nodetype='circles',
                  nodescale=30,
                  nodealpha=1,
                  showlegend=False)
                  
plt.show()
```
![](./figures/4framesrot.png)

#### AP rotation with 5 frames

```python
netplotbrain.plot(nodes=nodes,
                  edges=edges,
                  edgescale=5,
                  edgealpha=3,
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view=['AP'],
                  frames=5,
                  nodecolor='community',
                  nodecmap='viridis',
                  nodetype='circles',
                  nodescale=30,
                  nodealpha=1,
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
                  templatestyle='glass',
                  nodescale=20,
                  nodecolor='yeo7networks',
                  edgethreshold=0,
                  edgethresholddirection='>',
                  seed=2022)
plt.show()
```
![](./figures/springlayout.png)

