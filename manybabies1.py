#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on May 10, 2017, at 10:47
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')

from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'manybabies1'  # from the Builder filename that created this script
expInfo = {u'participant': u'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=1,
    allowGUI=False, allowStencil=False,
    monitor='DellMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "attention"
attentionClock = core.Clock()
baby = visual.MovieStim3(
    win=win, name='baby',
    noAudio = False,
    filename='Stimuli\\baby.wmv',
    ori=0, pos=(0, 0), opacity=1,
    depth=0.0,
    )

eyetracker =False#will change if we get one!

from psychopy.iohub import EventConstants,ioHubConnection,load,Loader, EyeTrackerConstants
from psychopy.data import getDateStr
# Load the specified iohub configuration file converting it to a python dict.
io_config=load(file('SMI_iview.yaml','r'), Loader=Loader)

# Add / Update the session code to be unique. Here we use the psychopy getDateStr() function for session code generation
session_info=io_config.get('data_store').get('session_info')
session_info.update(code="S_%s"%(getDateStr()))


#u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
# Rename file we are writing to
datastore = io_config.get('data_store')
datastore.update(filename = 'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date']))

# Create an ioHubConnection instance, which starts the ioHubProcess, and informs it of the requested devices and their configurations.
io=ioHubConnection(io_config)

#iokeyboard=io.devices.keyboard
#mouse=io.devices.mouse

if io.getDevice('tracker'):
    eyetracker=io.getDevice('tracker')
    win.fullscr=False
    win.winHandle.set_fullscreen(False)
    win.winHandle.minimize()
    win.flip()

    eyetracker.runSetupProcedure(starting_state = EyeTrackerConstants.TRACKER_FEEDBACK_STATE)
    eyetracker.runSetupProcedure(starting_state = EyeTrackerConstants.CALIBRATION_STATE)
    eyetracker.runSetupProcedure(starting_state = EyeTrackerConstants.VALIDATION_STATE)

    win.winHandle.maximize()
    win.winHandle.activate()
    win.fullscr=True
    win.winHandle.set_fullscreen(True)
    win.flip()
x,y=0,0
look_time = 0

# Initialize components for Routine "trial"
trialClock = core.Clock()
checkerboard = visual.ImageStim(
    win=win, name='checkerboard',
    image='Stimuli\\checkerboard.jpg', mask=None,
    ori=0, pos=(0, 0), size=(.5,.5),
    color='black', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
audio = sound.Sound('A', secs=-1)
audio.setVolume(1)
look_away_time = 0

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('order1.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "attention"-------
    t = 0
    attentionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    baby.seek(0)
    if eyetracker:
        io.sendMessageEvent("Attention_Start")
        io.clearEvents('all')
        eyetracker.setRecordingState(True)
        last_time = core.getTime()
        this_time = last_time
        look_time = 0
    attention_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    attentionComponents = [baby, attention_key]
    for thisComponent in attentionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "attention"-------
    while continueRoutine:
        # get current time
        t = attentionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *baby* updates
        if t >= 0.0 and baby.status == NOT_STARTED:
            # keep track of start time/frame for later
            baby.tStart = t
            baby.frameNStart = frameN  # exact frame index
            baby.setAutoDraw(True)
        if baby.status == FINISHED:  # force-end the routine
            continueRoutine = False
        if attention_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            if len(theseKeys) > 0:
                baby.pause()
                continueRoutine = False
        if eyetracker:
            # get /eye tracker gaze/ position 
            gpos=eyetracker.getPosition()
            this_time = core.getTime()
            if type(gpos) in [list,tuple]:
                x,y=gpos[0], gpos[1]
        
                # check if gaze is on attention getter
                if baby.contains(gpos):
                    look_time = look_time + (this_time - last_time)
        
            last_time = this_time
        
            if look_time > 2:
                io.sendMessageEvent("Attention_End")
                baby.pause()
                continueRoutine = False
        
        # *attention_key* updates
        if t >= 0.0 and attention_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            attention_key.tStart = t
            attention_key.frameNStart = frameN  # exact frame index
            attention_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(attention_key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if attention_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                attention_key.keys = theseKeys[-1]  # just the last key pressed
                attention_key.rt = attention_key.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in attentionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "attention"-------
    for thisComponent in attentionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    if eyetracker:
        eyetracker.setRecordingState(False)
    # check responses
    if attention_key.keys in ['', [], None]:  # No response was made
        attention_key.keys=None
    trials.addData('attention_key.keys',attention_key.keys)
    if attention_key.keys != None:  # we had a response
        trials.addData('attention_key.rt', attention_key.rt)
    # the Routine "attention" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    audio.setSound("Stimuli\\"+Stimulus+".wav", secs=-1)
    if eyetracker:
        io.clearEvents('all')
        eyetracker.setRecordingState(True)
        last_time = core.getTime()
        this_time = last_time
        look_away_time = 0
        io.sendMessageEvent("Trial_Start")
    trial_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [checkerboard, audio, trial_key]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *checkerboard* updates
        if t >= 0.0 and checkerboard.status == NOT_STARTED:
            # keep track of start time/frame for later
            checkerboard.tStart = t
            checkerboard.frameNStart = frameN  # exact frame index
            checkerboard.setAutoDraw(True)
        # start/stop audio
        if t >= 0.0 and audio.status == NOT_STARTED:
            # keep track of start time/frame for later
            audio.tStart = t
            audio.frameNStart = frameN  # exact frame index
            audio.play()  # start the sound (it finishes automatically)
        if eyetracker:
            # get /eye tracker gaze/ position 
            gpos=eyetracker.getPosition()
            this_time = core.getTime()
        
            if type(gpos) in [list,tuple]:
                x,y=gpos[0], gpos[1]
        
                # check if gaze is on checkerboard
                if checkerboard.contains(gpos):
                    look_time = 0
            else:
                look_away_time = look_away_time + (this_time - last_time)
        
            last_time = this_time
        
            if look_away_time > 2:
                io.sendMessageEvent("Trial_End")
                continueRoutine = False
        
        # *trial_key* updates
        if t >= 0.0 and trial_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_key.tStart = t
            trial_key.frameNStart = frameN  # exact frame index
            trial_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(trial_key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if trial_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                trial_key.keys = theseKeys[-1]  # just the last key pressed
                trial_key.rt = trial_key.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    audio.stop()  # ensure sound has stopped at end of routine
    if eyetracker:
        eyetracker.setRecordingState(False)
    # check responses
    if trial_key.keys in ['', [], None]:  # No response was made
        trial_key.keys=None
    trials.addData('trial_key.keys',trial_key.keys)
    if trial_key.keys != None:  # we had a response
        trials.addData('trial_key.rt', trial_key.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


if eyetracker:
    eyetracker.setConnectionState(False)
    io.quit()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
