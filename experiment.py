from psychopy import visual, core, event, data, gui
import numpy as np
from constants import *


#making the dialog box
info = gui.Dlg(title="2AFC Color Discrimination")
info.addField("Participant ID:")
info.addField("eye:", choices=["Left", "Right"])
info.addText('Choose the non-adapted eye in adaptation condition.')
info.addField("Adaptation status:", choices=["No_Adaptation", "Adaptation"])


#displaying the box and saving the data
okdata = info.show()
if not okdata: core.quit()
IDs = okdata[0]
eye = okdata[1] if len(okdata) > 1 else "" 
adapstatus = okdata[2] if len(okdata) > 2 else ""


#Generating experiment's main colors
rand = np.linspace(0,0.7,10)

blue = []
for each_b in rand: 
    rgb = [0, 0, each_b]
    blue.append({'rgb': rgb})

yellow = []
for each_y in rand: 
    rgb = [each_y, each_y, 0]
    yellow.append({'rgb': rgb})


#create a window
win =visual.Window(size=DISPSIZE, units='norm', fullscr=True, color=BGC)


#categorize everything about colors for output.csv
color_data = yellow + blue
yellow_rgbs = [c['rgb'] for c in yellow]
colors = [{'index': i, 'rgb': c['rgb'], 'name': 'yellow' if c['rgb'] in yellow_rgbs else 'blue'}
          for i, c in enumerate(color_data)]


#defining the trial and saving essential info
trials = data.TrialHandler(colors, nReps=reps, method='random')
trials.extraInfo = {'participant': IDs, 'eye': eye, 'adaptstatus': adapstatus}


#shapes and texts
stim = visual.Rect(win, width=2, height=2, fillColor='white')
circle = visual.Circle(win, radius=6, edges=64, units='pix', lineColor=BGC, fillColor=BGC, pos=(0, 0))
instruct = visual.TextStim(win, text= "Look at the color with one eye.\n"
                                   "Press 'b' for blue, 'y' for yellow.\n"
                                   "Press 'space' to start", pos=(0, 0))


#show instructions, quit button
instruct.draw()
win.flip()
keys = event.waitKeys(keyList=['space', 'escape'])
if 'escape' in keys: core.quit()


#collect the data
exp = data.ExperimentHandler(dataFileName=f'{IDs}_{eye}_{adapstatus}.csv')
exp.addLoop(trials)


#define the first adaptation status (30")
if adapstatus == "Adaptation":
    adaptstim = visual.Rect(win, width=2, height=2, fillColor=adaptcolor )
    adaptstim.draw()
    circle.draw()
    win.flip()
    core.wait(long)


#start trials
for trial in trials:
    stim.fillColor = trial['rgb']
    stim.draw()
    circle.draw()
    win.flip()
    core.wait(0.2)

 #keys that you can choose
    keys = event.waitKeys(keyList=['b', 'y', 'escape'])
    if 'escape' in keys: core.quit()
    trials.addData('response', keys[0])

 #save whether they chose the right key(1), or not(0)
    if keys[0] == 'y' and trial['name'] == 'yellow' :
        answer = '1'
    elif keys[0] == 'b' and trial['name'] == 'blue' :
        answer = '1'
    else :
        answer = "0"

 #save the data of each trial, move to next one
    trials.addData('answer', answer)
    exp.nextEntry()
    win.flip()
    core.wait(0.2)

 #show the adaptation color for 10' between trials
    if adapstatus == "Adaptation":
        adaptstim.draw()
        circle.draw()
        win.flip()
        core.wait(short)
        win.flip()


#save csv, end it
exp.saveAsWideText(f'{IDs}_{eye}_{adapstatus}.csv')
exp.close()
win.close()
core.quit()