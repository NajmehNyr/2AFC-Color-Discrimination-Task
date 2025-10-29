# 2AFC Color Discrinmination Task
## Aims
This experiment aims to estimate the threshold of two opponent colors—blue and yellow—using a two-alternative forced choice task in PsychoPy. The goal is to study the intraocular transfer phenomenon of adaptation. As you will see, adapting to blue will increase the threshold for blue, causing you to perceive colors with a small amount of blue as yellow.

## Experimental Description
Twenty color stimuli (10 yellow and 10 blue) will be presented 20 times to each participant. When the code is executed, a dialog box will appear, allowing you to choose between 'No Adaptation' and 'Adaptation'.
This code can be used for experiments relevent to Krauskopf et al 1992.
### No Adaptation
The colors will be displayed randomly, and you must press 'Y' for yellow or 'B' for blue to get to the next trial.
### Adaptation
Adaptation stimulus (RGB: 0, 0, 255) will be presented for 30 seconds. Following this, the experiment will start, and the colors will be displayed, with the adaptation stimulus shown again for 5 seconds between each trial.
> Color spectrum is accessible in colorbar.ipynb.

references:
Krauskopf J, Gegenfurtner K. Color discrimination and adaptation. Vision Res. 1992 Nov;32(11):2165-75. doi: 10.1016/0042-6989(92)90077-v. PMID: 1304093.
