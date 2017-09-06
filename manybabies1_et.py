#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on June 01, 2017, at 14:54
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

import psychopy.iohub.devices.eyetracker.hw.smi.iviewx.pyViewX as pyViewX
from ctypes import byref, c_longlong ,c_int, c_void_p,POINTER, c_char
import time

import PIL
import cv2

from scipy.misc import toimage
import math

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'manybabies1'  # from the Builder filename that created this script

dlg = gui.Dlg(title="ManyBabies 1", labelButtonOK = 'Start', labelButtonCancel = "Cancel")
dlg.addField("Participant: ", 1)
dlg.addField("Record Video", choices = ["Yes", "No"])
ok_data = dlg.show()  # show dialog and wait for OK or Cancel
if dlg.OK:  # or if ok_data is not None
    print(ok_data)
else:
    core.quit()

participant = ok_data[0]
record = ok_data[1]

expInfo = {u'participant': str(participant).encode()}
expInfo['record'] = str(record).encode()
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\iView\\Documents\\ManyBabies\\ET\\manybabies1.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window( #(1920, 1080
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

# Setup window for monitoring
et_win = visual.Window(size=(1200, 900), fullscr=False, screen=0,
    monitor='testMonitor', colorSpace = 'rgb', useFBO=True, color = .5)
    
#eye_img = visual.ImageStim(win=et_win, image=None, pos = (-200,-325), units = "pix")    
monitor_img = visual.ImageStim(win=et_win, image=None, pos = (0,-325), units = "pix")
accuracy_img = visual.ImageStim(win=et_win, image=None, pos = (400,-310), units = "pix")
copy_img = visual.ImageStim(win=et_win, image=None, pos = (0,100), units = "pix")
cam_img = visual.ImageStim(win=et_win, image=None, pos = (-350,-325), units = "pix")

#gaze position
gaze_dot = visual.GratingStim(et_win,tex=None, mask="circle",
                              pos=(0,0),size=(25,25),color='red',
                              units="pix")
    
def showEyeImage(eye_image):
    try:
        img_loc = eyetracker.getEyeImage() 
    except TypeError:
        return
        
    if img_loc != None:
        eye_image.setImage(img_loc)
        eye_image.draw()
        
def showCam(cam_image):

    if(record):
        frame = cap.video_frame
    else:
        ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    img = toimage(frame).transpose(PIL.Image.FLIP_LEFT_RIGHT)
    img.thumbnail((320,240))
    
    cam_image.setImage(img)
    cam_image.draw()

def showTrackingMonitor(monitor_image):
    try:
        img_loc = eyetracker.getTrackingMonitor()
    except TypeError:
        return

    if img_loc != None:
        monitor_image.setImage(img_loc)
        monitor_image.draw()
            
def showAccuracyImage(accuracy_image):
    try:
        img_loc = eyetracker.getAccuracyImage()
    except TypeError:
        return

    if img_loc != None:
        accuracy_image.setImage(img_loc)
        accuracy_image.size = (370,261)
        accuracy_image.setAutoDraw(True)

def showCalibrationQualityImage(accuracy_image):
    try:
        img_loc = eyetracker.getCalibrationQualityImage()
    except TypeError:
        return

    if img_loc != None:
        accuracy_image.setImage(img_loc)
        accuracy_image.size = (370,261)
        accuracy_image.setAutoDraw(True)
            
            
def updateWins():
    #showEyeImage(et_win, eye_img)
    showCam(cam_img)
    showTrackingMonitor(monitor_img)
    
    win.flip()
    win_frame = win.getFrame()
    win_frame.thumbnail((960,540))
    copy_img.setImage(win_frame)
    copy_img.draw()
    
    if eyetracker:
        gpos = eyetracker.getPosition()
        if type(gpos) in [tuple,list]:
            # If we have a gaze position from the tracker,
            # redraw the background image and then the
            # gaze_cursor at the current eye position.
            #
            gaze_dot.setPos([math.floor(gpos[0]/2),math.floor(gpos[1]/2)+100])
            gaze_dot.draw()
    
    et_win.flip()
    
from psychopy.visual.helpers import pointInPolygon

def insideObj(pos, obj, buff):

    buff_pos = ([[buff, -buff], [-buff, -buff], [-buff, buff], [buff, buff]])
    obj_vertices = obj.verticesPix + buff_pos

    return psychopy.visual.helpers.pointInPolygon(pos[0], pos[1], poly=obj_vertices)
eyetracker =False#will change if we get one!

import sys

from AVRecordeR import *

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

keyboard=io.devices.keyboard
#mouse=io.devices.mouse
calib_audio = sound.Sound(u'Stimuli\\07 Mrs. Robinson.wav', secs=-1)
calib_audio.setVolume(.5)


if(record):
    cap = start_AVrecording(filename)
else:
    cap = cv2.VideoCapture(0)


if io.getDevice('tracker'):
    eyetracker=io.getDevice('tracker')
    #win.fullscr=False
    #win.winHandle.set_fullscreen(False)
    #win.winHandle.minimize()

    #updateWins()
    #win.winHandle.maximize()
    win.winHandle.activate()
    #win.fullscr=True
    #win.winHandle.set_fullscreen(True)
x,y=0,0
# look_time = 0.0

from psychopy.visual.helpers import pointInPolygon

def insideObj(pos, obj, buff):

    buff_pos = ([[buff, -buff], [-buff, -buff], [-buff, buff], [buff, buff]])
    obj_vertices = obj.verticesPix + buff_pos

    return psychopy.visual.helpers.pointInPolygon(pos[0], pos[1], poly=obj_vertices)

def setCalibPoint():
    try:
        num, x, y = eyetracker.getCurrentCalibrationPoint()
        (win_x, win_y) = win.size
        return (num, x - (win_x/2), y - (win_y/2))

    except TypeError:
        pass    

def calibPointQuality(point_num):
    try:
        qual_ret = eyetracker.getCalibrationQuality(point_num)
        if type(qual_ret) in [list,tuple]:
            num, quality = qual_ret
            print str(num) + str(quality)
        else:
            print qual_ret
    except TypeError:
        pass 
        
# Initialize components for Routine "attention"
attentionClock = core.Clock()
attention_getter = visual.MovieStim3(
    win=win, name='attention_getter',units='pix', 
    noAudio = False,
    filename='Stimuli\\attention getter (hoehle circles and chimes).avi',
    ori=0, pos=(0, 0), opacity=1,
    size=200,
    depth=0.0,
    )
  
# Initialize components for Routine "trial"
trialClock = core.Clock()
checkerboard = visual.ImageStim(
    win=win, name='checkerboard',units='pix', 
    image='Stimuli\\checkerboard.jpg', mask=None,
    ori=0, pos=(0,0), size=(950,636),
    color='black', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
audio = sound.Sound('A', secs=-1)
audio.setVolume(1)
look_away_time = 0

# Initialize components for Routine "intro"
introClock = core.Clock()
intro_movie = visual.MovieStim(
    win=win, name='intro_movie',units='pix', 
  #  noAudio = False,
    filename='Stimuli\\Elmos World The Sky Active.wmv',
    ori=0, pos=(0, 0), opacity=1,
    size = (480,360),
    depth=0.0,
    )


# Initialize components for Routine "elmo"
elmoClock = core.Clock()
thanks = sound.Sound('Stimuli/thanks.wav', secs=-1)
thanks.setVolume(1)
goodbye = visual.ImageStim(
    win=win, name='goodbye',
    image='Stimuli/elmo_slide.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
    
# Initialize components for Routine "calibration"
calibrationClock = core.Clock()
chime = sound.Sound('Stimuli/chime.wav', secs=-1)
chime.setVolume(1)
calibBackSound = sound.Sound('Stimuli/07 Mrs. Robinson.wav', secs=-1)
calibBackSound.setVolume(1)
calibImage = visual.ImageStim(
    win=win, name='calibImage',
    image='Stimuli/elmo/1.png', units = "pix")    

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

def setupTracker(type = "calibrate", lastType = "none", startMusic = False):
    next = "break"
    # ------Prepare to start Routine "calibration"-------
    t = 0
    calibrationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    acceptPoint = event.BuilderKeyResponse()
    # update component parameters for each repeat
    # keep track of which components have finished
    calibrationComponents = [calibImage, calibBackSound,acceptPoint]
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    endExpNow = False
    
    if type == "showAccuracy":
        if(lastType == "validate"):
            showAccuracyImage(accuracy_img)
        else:
            showCalibrationQualityImage(accuracy_img)
            
        while continueRoutine:
           # get current time
            t = calibrationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            
            # update/draw components on each frame
            if t >= 0.0 and calibImage.status == NOT_STARTED:
                # keep track of start time/frame for later
                calibImage.tStart = t
                calibImage.frameNStart = frameN  # exact frame index\
                calibImage.setAutoDraw(True)
             # start/stop background audio
            if t >= 0.0 and calibBackSound.status == NOT_STARTED:
                # keep track of start time/frame for later
                calibBackSound.tStart = t
                calibBackSound.frameNStart = frameN  # exact frame index
                if startMusic:
                    calibBackSound.play()  # start the sound (it finishes automatically)
            if t >= 0.0 and chime.status == NOT_STARTED:
                # keep track of start time/frame for later
                chime.tStart = t
                chime.frameNStart = frameN  # exact frame index
            if t >= 0.0 and acceptPoint.status == NOT_STARTED:
                # keep track of start time/frame for later
                acceptPoint.tStart = t
                acceptPoint.frameNStart = frameN  # exact frame index
                acceptPoint.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')

            calibImage.image = "Stimuli/elmo/" + str(int((math.floor(t / .1)) % 8) + 1) + ".png"
                    
            if acceptPoint.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "return" in theseKeys:
                    next = "break"
                    calibBackSound.stop()  # ensure sound has stopped at end of routine
                    continueRoutine = False
                if "c" in theseKeys:  # accept calib point
                    next = "calibrate"
                    continueRoutine = False
                if "v" in theseKeys:  # accept calib point
                    next = "validate"
                    continueRoutine = False
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
                
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in calibrationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                updateWins()
    else:
    
        if type == "calibrate":
            eyetracker.internalCalib()
            next = "showAccuracy"
            lastType = "calibrate"
        elif type == "validate":
            eyetracker.internalValid()
            next = "showAccuracy"
            lastType = "validate"
        else:
            print "Wrong type!!"
            return

        calib_num, goal_x, goal_y = setCalibPoint()
        calibImage.pos = (goal_x, goal_y)
            
        # -------Start Routine "calibration"-------
        while continueRoutine:
            # get current time
            t = calibrationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

            # update/draw components on each frame
            if t >= 0.0 and calibImage.status == NOT_STARTED:
                # keep track of start time/frame for later
                calibImage.tStart = t
                calibImage.frameNStart = frameN  # exact frame index\
                calibImage.setAutoDraw(True)
             # start/stop background audio
            if t >= 0.0 and calibBackSound.status == NOT_STARTED:
                # keep track of start time/frame for later
                calibBackSound.tStart = t
                calibBackSound.frameNStart = frameN  # exact frame index
                if startMusic:
                    calibBackSound.play()  # start the sound (it finishes automatically)
            if t >= 0.0 and chime.status == NOT_STARTED:
                # keep track of start time/frame for later
                chime.tStart = t
                chime.frameNStart = frameN  # exact frame index
            if t >= 0.0 and acceptPoint.status == NOT_STARTED:
                # keep track of start time/frame for later
                acceptPoint.tStart = t
                acceptPoint.frameNStart = frameN  # exact frame index
                acceptPoint.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if acceptPoint.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if "space" in theseKeys:  # accept calib point
                    print "accepting: " + str(eyetracker.acceptCalibrationPoint())
                
            frameRemains = 0.0 + 3.2- win.monitorFramePeriod * 0.75  # most of one frame period left
           
            calibImage.image = "Stimuli/elmo/" + str(int((math.floor(t / .1)) % 8) + 1) + ".png"
                
            try: 
                pt_num, goal_x, goal_y = setCalibPoint()
                
                if pt_num != calib_num: 
                    chime.play()  # start the sound (it finishes automatically)
                    calib_num = pt_num
            
                if [float(pos) for pos in calibImage.pos] != [float(goal_x), float(goal_y)]: 
                    cur_pos = calibImage.pos
                    #calibImage.pos = cur_pos + (.25 * (goal_x - cur_pos[0]), .25 * (goal_y - cur_pos[1]))
                    calibImage.pos = (goal_x,goal_y)
                    
            except TypeError:
                continueRoutine = False
           
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
                
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in calibrationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                updateWins()

    # -------Ending Routine "calibration"-------
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
   
    chime.stop()
    # the Routine "calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
        
    if next == "break":
        return
    else: 
        setupTracker(type = next, lastType = lastType)

        
# ------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
intro_movie.seek(0)
intro_key = event.BuilderKeyResponse()
# keep track of which components have finished
introComponents = [intro_movie, intro_key]
for thisComponent in introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "intro"-------
while continueRoutine:
    # get current time
    t = attentionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *attention_getter* updates
    if t >= 0.0 and intro_movie.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_movie.tStart = t
        intro_movie.frameNStart = frameN  # exact frame index
        intro_movie.setAutoDraw(True)
    if intro_movie.status == FINISHED:  # force-end the routine
        continueRoutine = False
    if intro_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:
            intro_movie.pause()
            continueRoutine = False
    
    # *intro_key* updates
    if t >= 0.0 and intro_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_key.tStart = t
        intro_key.frameNStart = frameN  # exact frame index
        intro_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(intro_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
  
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        updateWins()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "attention" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()     

setupTracker(startMusic = True)

order = participant % 4
if order == 0:
    order = 4

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('order' + str(order) + '.csv'),
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
    attention_getter.seek(0)
    if eyetracker:
        io.sendMessageEvent("Attention_Start")
        io.clearEvents('all')
        eyetracker.setRecordingState(True)
        last_time = core.getTime()
        this_time = last_time
        look_time = 0.0
    attention_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    attentionComponents = [attention_getter, attention_key]
    for thisComponent in attentionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "attention"-------
    while continueRoutine:
        # get current time
        t = attentionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *attention_getter* updates
        if t >= 0.0 and attention_getter.status == NOT_STARTED:
            # keep track of start time/frame for later
            attention_getter.tStart = t
            attention_getter.frameNStart = frameN  # exact frame index
            attention_getter.setAutoDraw(True)
        if attention_getter.status == FINISHED:  # force-end the routine
            continueRoutine = False
       
        if eyetracker:
            # get /eye tracker gaze/ position 
            gpos=eyetracker.getPosition()
            this_time = core.getTime()
            if type(gpos) in [list,tuple]:
                x,y=gpos[0], gpos[1]
        
                # check if gaze is on attention getter
                if insideObj(gpos, attention_getter, 150):
                    look_time = look_time + (this_time - last_time)
        
            last_time = this_time
            #
            "look_time " + str(look_time)
            #sys.stdout.flush()
        
            if look_time > 2:
                io.sendMessageEvent("Attention_End")
                attention_getter.pause()
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
                io.sendMessageEvent("Attention_End")
                continueRoutine = False
        
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
            updateWins()
    
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
    
        start_time = last_time
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
                #    print "board"
                #    print str(look_away_time)
                    look_away_time = 0
                else:
                    look_away_time = look_away_time + (this_time - last_time)
            else:
                look_away_time = look_away_time + (this_time - last_time)
        
            last_time = this_time
        
            if look_away_time > 2:
                io.sendMessageEvent("Trial_End")
                continueRoutine = False
        
            if this_time - start_time > 18:
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
                io.sendMessageEvent("Trial_End")
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
            updateWins()
    
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


# ------Prepare to start Routine "elmo"-------
t = 0
elmoClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
elmoComponents = [thanks, goodbye]
for thisComponent in elmoComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "elmo"-------
while continueRoutine:
    # get current time
    t = elmoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop thanks
    if t >= 0.0 and thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks.tStart = t
        thanks.frameNStart = frameN  # exact frame index
        thanks.play()  # start the sound (it finishes automatically)
    
    # *goodbye* updates
    if t >= 0.0 and goodbye.status == NOT_STARTED:
        # keep track of start time/frame for later
        goodbye.tStart = t
        goodbye.frameNStart = frameN  # exact frame index
        goodbye.setAutoDraw(True)
    frameRemains = 0.0 + 3.2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if goodbye.status == STARTED and t >= frameRemains:
        goodbye.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in elmoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        updateWins()

# -------Ending Routine "elmo"-------
for thisComponent in elmoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thanks.stop()  # ensure sound has stopped at end of routine
# the Routine "elmo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

if eyetracker:
    eyetracker.setConnectionState(False)
    io.quit()

if(record):
    stop_AVrecording(filename)
else:
    cap.release()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
