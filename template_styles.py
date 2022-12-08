# Plotting different template styles

# Import everything needed
import netplotbrain
import matplotlib.pyplot as plt

# Plot glass style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='glass',
                  view='S',
                  arrowaxis=None,
                  title='glass', 
                  subtitles=None)

plt.savefig('./figures/glass_template.png', dpi=300)

# Plot surface style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='surface',
                  view='S',
                  arrowaxis=None,
                  title='surface',
                  subtitles=None)

plt.savefig('./figures/surface_template.png', dpi=300)

# Plot filled style 
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='filled',
                  view='S',
                  arrowaxis=None,
                  title='filled',
                  subtitles=None)

plt.savefig('./figures/filled_template.png', dpi=300)

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

plt.savefig('./figures/cloudy_template.png', dpi=300)