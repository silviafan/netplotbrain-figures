# Plotting templates pulled from TemplateFlow https://www.templateflow.org

# Import everything needed
import netplotbrain
import matplotlib.pyplot as plt

# Adult brain MNI152NLin6Asym
netplotbrain.plot(template='MNI152NLin6Asym',
                  templatestyle='glass',
                  view='L',
                  arrowaxis=None,
                  subtitles='MNI152NLin6Asym')

plt.savefig('./figures/adultMNI.png', dpi=300)

# Infant template MNIInfant_cohort-3
# Setting a larger templatevoxsize will make it slightly quicker
netplotbrain.plot(template='MNIInfant_cohort-3',
                  templatestyle='glass',
                  view='L',
                  arrowaxis=None,
                  subtitles='MNIInfant_cohort-3')

plt.savefig('./figures/infantMNIcohort3.png', dpi=300)

# Rat template WHS
netplotbrain.plot(template='WHS',
                  templatestyle='glass',
                  view='L',
                  arrowaxis=None,
                  subtitles='WHS')

plt.savefig('./figures/ratWHS.png', dpi=300)


# Squirrel monkey VALiDATe29 
netplotbrain.plot(template='VALiDATe29',
                  templatestyle='glass',
                  view='L',
                  arrowaxis=None,
                  subtitles='VALiDATe29')

plt.savefig('./figures/squirrelmonkeyValidate29.png', dpi=300)
