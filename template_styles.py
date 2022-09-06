# Plotting different template styles

# Import everything needed
import netplotbrain
import matplotlib.pyplot as plt

fig  = plt.figure()

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

fig.savefig('./figures/template_styles.png', dpi=300)