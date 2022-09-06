# Plotting templates pulled from TemplateFlow https://www.templateflow.org

# Import everything needed
import netplotbrain
import matplotlib.pyplot as plt

# Example node and edges dataframes

fig  = plt.figure()

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

fig.savefig('./figures/diff_tftemplates.png', dpi=300)
