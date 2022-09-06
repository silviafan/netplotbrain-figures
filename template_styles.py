# Plotting different template styles

# Import everything needed
import netplotbrain
import matplotlib.pyplot as plt

# Plot glass style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='S',
                  arrowaxis=None,
                  subtitles='glass')

plt.savefig('./figures/glass_template.png', dpi=300)

# Plot surface style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='surface',
                  view='S',
                  arrowaxis=None,
                  subtitles='surface')

plt.savefig('./figures/surface_template.png', dpi=300)

# Plot filled style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='filled',
                  view='S',
                  arrowaxis=None,
                  subtitles='filled')

plt.savefig('./figures/filled_template.png', dpi=300)

# Plot cloudy style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='cloudy',
                  templatevoxelsize=2,
                  templatealpha=0.065,
                  view='S',
                  templateedgethreshold=0.6,
                  arrowaxis=None,
                  subtitles='cloudy')

plt.savefig('./figures/cloudy_template.png', dpi=300)