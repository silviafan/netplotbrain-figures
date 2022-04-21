# Plotting different template styles

# Import everything needed
import netplotbrain
import matplotlib.pyplot as plt

fig  = plt.figure()

# Plot surface style 
ax = fig.add_subplot(141, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='surface',
                  view='A',
                  arrowaxis=[],
                  title='surface',
                  fig=fig, ax=ax)

# Plot filled style 
ax = fig.add_subplot(142, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='filled',
                  view='A',
                  arrowaxis=[],
                  title='filled',
                  fig=fig, ax=ax)

# Plot cloudy style 
ax = fig.add_subplot(143, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='cloudy',
                  view='A',
                  arrowaxis=[],
                  title='cloudy',
                  fig=fig, ax=ax)

# Plot glass style 
ax = fig.add_subplot(144, projection='3d')
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='A',
                  arrowaxis=[],
                  title='glass',
                  fig=fig, ax=ax)

fig.savefig('./figures/template_styles.png', dpi=150)