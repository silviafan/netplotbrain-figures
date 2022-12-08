# Plotting templates pulled from TemplateFlow https://www.templateflow.org

# Import everything needed
import netplotbrain
import matplotlib.pyplot as plt

# Adult brain MNI152NLin6Asym
netplotbrain.plot(template='MNI152NLin6Asym',
                  template_style='glass',
                  view='L',
                  arrowaxis=None,
                  title='MNI152NLin6Asym',
                  subtitles=None)

plt.savefig('./figures/adultMNI.png', dpi=300)

# Infant template MNIInfant_cohort-3
# Setting a larger templatevoxsize will make it slightly quicker
netplotbrain.plot(template='MNIInfant_cohort-3',
                  template_style='glass',
                  view='L',
                  arrowaxis=None,
                  title='MNIInfant_cohort-3',
                  subtitles=None)

plt.savefig('./figures/infantMNIcohort3.png', dpi=300)

# Rat template WHS
netplotbrain.plot(template='WHS',
                  template_style='glass',
                  view='L',
                  arrowaxis=None,
                  title='WHS',
                  subtitles=None)

plt.savefig('./figures/ratWHS.png', dpi=300)


# Squirrel monkey VALiDATe29 
netplotbrain.plot(template='VALiDATe29',
                  template_style='glass',
                  view='L',
                  arrowaxis=None,
                  title='VALiDATe29',
                  subtitles=None)

plt.savefig('./figures/squirrelmonkeyValidate29.png', dpi=300)
