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

# Surface style 
ax = fig.add_subplot(141, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='surface',
                  view='A',
                  arrowaxis=[],
                  title='surface',
                  fig=fig, ax=ax)

# Filled style 
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='filled',
                  view='A',
                  arrowaxis=[],
                  title='filled',
                  fig=fig, ax=ax)

# Cloudy style 
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='cloudy',
                  view='A',
                  arrowaxis=[],
                  title='cloudy',
                  fig=fig, ax=ax)

# Glass style 
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='A',
                  arrowaxis=[],
                  title='glass',
                  fig=fig, ax=ax)
plt.show()
```
![](./figures/template_styles.png)
