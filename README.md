# netplotbrain: a showcase of visualization examples

### Import necessary packages and load data

```python

import netplotbrain
import pandas as pd
import matplotlib.pyplot as plt
import templateflow.api as tf

# Node and edge dataframes 
atlasinfo = tf.get(template='MNI152NLin6Asym',
       atlas='Schaefer2018',
       desc='100Parcels7Networks',
       extension='.tsv')
atlasinfo = pd.read_csv(atlasinfo, sep='\t')
# Parse the info in to get network names
networks = list(map(lambda x: x.split('_')[2], atlasinfo.name.values))
atlasinfo['yeo7networks'] = networks

nodes = pd.read_csv('./nodes.tsv', sep='\t', index_col=0)
edges = pd.read_csv('./edges.tsv', sep='\t', index_col=0)

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
                  arrowaxis=[],
                  title='',
                  fig=fig, ax=ax)
                  
# Plot only nodes
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(nodes=atlasinfo,
                  nodeimg={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle=None,
                  templatealpha=0.08,
                  nodetype='spheres',
                  view='L',
                  arrowaxis=[],
                  title='',
                  fig=fig, ax=ax)
                 
# Plot only edges
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(nodes=atlasinfo,
                 nodeimg={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},                  
                 edges=edges,
                 template='MNI152NLin6Asym',
                 templatestyle=None,
                 view='L',
                 nodealpha=0,
                 edgeweights='weight',
                 edgealpha=5,
                 arrowaxis=[],
                 title='',
                 fig=fig, ax=ax)
                 
# Plot template, nodes, and edges together               
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(nodes=atlasinfo,
                 nodeimg={'atlas': 'Schaefer2018',
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
                 arrowaxis=[],
                 title='',
                 fig=fig, ax=ax)
plt.show()
```
![](./figures/single_components.png)

### Plot different template styles

```python
fig = plt.figure()

# Plot surface style 
ax = fig.add_subplot(141, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='surface',
                  view='A',
                  arrowaxis=None,
                  subtitles='surface',
                  fig=fig, ax=ax)

# Plot filled style 
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='filled',
                  view='A',
                  arrowaxis=None,
                  subtitles='filled',
                  fig=fig, ax=ax)

# Plot cloudy style 
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='cloudy',
                  templatevoxelsize=2,
                  templatealpha=0.065,
                  view='A',
                  arrowaxis=None,
                  subtitles='cloudy',
                  fig=fig, ax=ax)

# Plot glass style 
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='A',
                  arrowaxis=None,
                  subtitles='glass',
                  template_glass_maxalpha=0.035,
                  fig=fig, ax=ax)
plt.show()
```
![](./figures/template_styles.png)

### Plot different node styles

```python
fig = plt.figure()

# Circles
ax = fig.add_subplot(131, projection='3d')
netplotbrain.plot(nodeimg={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  template_glass_maxalpha=0.03,
                  view='S',
                  nodecolor='blue',
                  nodetype='circles',
                  nodescale=40,
                  nodealpha=1,
                  arrowaxis=[],
                  title='Circles',
                  fig=fig, ax=ax)

# Spheres
ax = fig.add_subplot(132, projection='3d')
netplotbrain.plot(nodeimg={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle='glass',
                  template_glass_maxalpha=0.03,
                  view='S',
                  nodecolor='blue',
                  nodetype='spheres',
                  nodealpha=1,
                  arrowaxis=[],
                  title='Spheres',
                  fig=fig, ax=ax)

# Parcels
ax = fig.add_subplot(133, projection='3d')
netplotbrain.plot(nodeimg={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle=None,
                  view=['S'],
                  nodetype='parcels',
                  nodealpha=1,
                  nodecolor='tab20c',
                  arrowaxis=[],
                  title='Parcels',
                  fig=fig, ax=ax)

plt.show()
```
![](./figures/node_types.png)

### Plot different templates pulled from TemplateFlow

```python
fig = plt.figure()

# Adult template
ax = fig.add_subplot(131, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                         'desc': '100Parcels7Networks',
                         'resolution': 1},
                  template='MNI152NLin6Asym',
                  templatestyle='surface',
                  view='S',
                  nodecolor='blue',
                  nodealpha=1,
                  nodescale=15,
                  arrowaxis=None,
                  showlegend=False,
                  subtitles='Adult template MNI152NLin6Asym',
                  fig=fig, ax=ax)
                  
# Rat template
nodes_whs = nodes.copy()
nodes_whs['x'] = nodes_whs['x'] / 8
nodes_whs['y'] = nodes_whs['y'] / 8
nodes_whs['z'] = nodes_whs['z'] / 8

ax = fig.add_subplot(132, projection='3d')
netplotbrain.plot(nodes=nodes_whs,
                  template='WHS',
                  templatestyle='surface',
                  templatealpha=0.3,
                  view='S',
                  nodescale=15,
                  nodecolor='blue',
                  nodealpha=1,
                  arrowaxis=None,
                  showlegend=False,
                  subtitles='Rat template WHS',
                  fig=fig, ax=ax)

# Infant template
nodes_inf = nodes.copy()
nodes_inf['x'] = nodes_inf['x'] / 1.25
nodes_inf['y'] = nodes_inf['y'] / 1.25
nodes_inf['z'] = nodes_inf['z'] / 1.25

# Setting a larger templatevoxsize will make it slightly quicker
ax = fig.add_subplot(133, projection='3d')
netplotbrain.plot(nodes=nodes_inf,
                  template='MNIInfant_cohort-3',
                  templatestyle='surface',
                  templatealpha=0.3,
                  view='S',
                  nodecolor='blue',
                  nodescale=15,
                  showlegend=False,
                  arrowaxis=None,
                  subtitles='Infant template MNIInfant',
                  fig=fig, ax=ax)
                  
plt.show()
```
![](./figures/diff_tftemplates_test.png)

### Plot different views and rotations

#### Multiple views on multiple rows

```python
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
                  arrowaxis=None,
                  showlegend=False)
                  
plt.show()
```
![](./figures/views.jpg)

#### AP rotation with 8 frames

```python
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
                  frames=8,
                  nodecolorby='yeo7networks',
                  nodecmap='cividis',
                  nodetype='circles',
                  nodescale=10,
                  nodealpha=1,
                  arrowaxis=None,
                  showlegend=False)
                  
plt.show()
```
![](./figures/rotation_8frames.png)

#### AP rotation with 5 frames

```python
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
                  frames=5,
                  nodecolorby='yeo7networks',
                  nodecmap='cividis',
                  nodetype='circles',
                  nodescale=10,
                  nodealpha=1,
                  arrowaxis=None,
                  showlegend=False)
                  
plt.show()
```
![](./figures/rotation_5frames.png)
