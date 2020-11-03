#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.1),
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import pandas as pd
import collections
import psignifit as ps
import random
from random import randint


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.1'
expName = 'StaircaseBlock1'
expInfo = {'participant': '', 'session': '', 'vf': ''}

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName)


logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units = 'deg')


# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='''Welcome to the experiment!\n\n
In this part of experiment you are expected to look at the center of the screen when the gratings appear.\n\n
You need to pay attention to gratings WITHOUT LOOKING AT THEM and indiacte the direction of the last seen grating \n\n
If you perceive second grating as tilted to;\n\n
Right:press right arrow key ->\n\n
Left: press left arrow key <-\n\n
Feel free to ask any questions before you start to experiment...\n\n
If you are ready, please press SPACE to start.\n''',
    font='Arial',
    pos=(0, 0), height=0.8, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0, units = 'deg');

#Initialize components for Routine "Adaptation"
AdaptationClock = core.Clock()

fixationPoint = visual.ShapeStim(
    win=win, name='fixationPoint', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),units='deg',
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

adaptorGrating = visual.GratingStim(
    win=win, name='adaptorGrating',units='deg',
    tex='sin', mask='gauss',
    ori=15.0, pos=[0,0], size=(3, 3), sf=1.44, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0 ,blendmode='avg',
    texRes=256, interpolate=True, depth=-2.0)

# Initialize components for Routine "Blank_1"
Blank_1Clock = core.Clock()

blankScreen1 = visual.TextStim(win=win, name='blankScreen1',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Test"
TestClock = core.Clock()

testGrating = visual.GratingStim(
    win=win, name='grating',units='deg',
    tex='sin', mask='gauss', pos=[0,0], size=(3, 3), sf=1.44, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0 ,blendmode='avg',
    texRes=256, interpolate=True, depth=-1.0)


# Initialize components for Routine "Blank_2"
Blank_2Clock = core.Clock()

textBlank = visual.TextStim(win=win, name='blankScreen2',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Thanks_Screen"
Thanks_ScreenClock = core.Clock()

thanksText = visual.TextStim(win=win, name='thanksText',
    text='''This part of the experiment is complete!\n
          Please press SPACE to continue.''',
    font='Arial', units = 'deg',
    pos=(0, 0), height = 0.8, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Break_Screen"
Break_ScreenClock = core.Clock()

break_text = visual.TextStim(win=win, name='breakText',
    text='''This part of the experiment is complete!\n
          You can take a break now.\n When you are ready
          to continue, please press SPACE to continue.''',
    font='Arial', units = 'deg',
    pos=(0, 0), height = 0.8, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine


# ------Prepare to start Routine "Welcome_Screen"-------
t = 0
Welcome_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True

# update component parameters for each repeat
welcome_resp = event.BuilderKeyResponse()

# keep track of which components have finished
Welcome_ScreenComponents = [welcome_text, welcome_resp]

for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *welcome_text* updates
    if t >= 0.0 and welcome_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_text.tStart = t
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.setAutoDraw(True)

    # *welcome_resp* updates
    if t >= 0.0 and welcome_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_resp.tStart = t
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if welcome_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


def mainRoutine(sc_states):
    '''
    Staircase has fixed trial number = 25.
    So, it will repeat 25 times at each spatial location.
    '''

    endExpNow = False

    #Initialize the components of data frame
    staircase_no = []
    testLoc_xs = []
    testLoc_ys = []
    raw_test_locs = []
    correct_answers = []
    test_keys = []
    response_corrs = []
    rts = []
    orientations = []


    vf = expInfo['vf']

    #grating location
    if vf == 'r':
        grating_location = (10.5, 0)
    else:
        grating_location = (-10.5, 0)

    #If test grating is on the left side of the screen
    if grating_location < (0, 0):
        for l in range(0, len(sc_states)):
            temp_x = sc_states[l][0][0]
            new_x = -temp_x
            sc_states[l][0][0] = new_x

    #shuffle staircase sc_states
    random.shuffle(sc_states)

    #index list
    index_list = 25 * [0, 1, 2, 3, 4, 5]
    random.shuffle(index_list)

   ######THIS PART OF THE EXPERIMENT IS REMOVED BECAUSE WORK IS IN PUBLICATION PROCESS. CONTACT ME FOR THIS PART#####################

        # -------Ending Routine "Adaptation"-------
        for thisComponent in AdaptationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # -------Start Routine "Blank_1"-------
        continueRoutine = True

        #time variables
        t = 0
        Blank_1Clock.reset()  # clock
        frameN = -1
        routineTimer.add(0.200000)

        # update component parameters for each repeat
        # keep track of which components have finished
        Blank_1Components = [blankScreen1, fixationPoint]

        for thisComponent in Blank_1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Blank_1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *fixationPoint* updates
            if t >= 0.0 and fixationPoint.status == NOT_STARTED:
                fixationPoint.setAutoDraw(True)

            # *blankScreen1* updates
            if t >= 0.0 and blankScreen1.status == NOT_STARTED:
                # keep track of start time/frame for later
                blankScreen1.tStart = t
                blankScreen1.frameNStart = frameN  # exact frame index
                blankScreen1.setAutoDraw(True)
            frameRemains = 0.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blankScreen1.status == STARTED and t >= frameRemains:
                blankScreen1.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "Blank_1"-------
        for thisComponent in Blank_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # ------Start Routine "Test"-------
        continueRoutine = True

        #time variables
        t = 0
        TestClock.reset()  # clock
        frameN = -1

        #we have 10 different staircase situations and we need to randomly show each
        #25 times
        ind = index_list[i]
        this_sc = sc_states[ind][0]
        next_ori = 0

        #get location and store
        testLoc_x = this_sc[0]
        testLoc_xs.append(testLoc_x)
        testLoc_y = this_sc[1]
        testLoc_ys.append(testLoc_y)
        rawLoc = this_sc[3]
        raw_test_locs.append(rawLoc)

        #set test grating location
        testLoc = (testLoc_x, testLoc_y)
        testGrating.setPos(testLoc)


        #get staircase number and store
        sc_num = this_sc[2]
        staircase_no.append(sc_num)

        #set test grating orientation and correct answers
        ori_list = sc_states[ind][1]
        ori = ori_list[-1]
        orientations.append(ori)
        testGrating.setOri(ori)

        if ori > 0:
            corrTestAns = 'right'
        elif ori < 0:
            corrTestAns = 'left'
        else:
            corrTestAns = 'vertical'

        correct_answers.append(corrTestAns)

        #Initialize test response
        testResponse = event.BuilderKeyResponse()

        # keep track of which components have finished
        TestComponents = [fixationPoint, testGrating, testResponse]
        for thisComponent in TestComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        while continueRoutine:
            # get current time
            t = TestClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *fixationPoint* updates
            if t >= 0.0 and fixationPoint.status == NOT_STARTED:
                fixationPoint.setAutoDraw(True)

            # *testGrating* updates
            if t >= 0.0 and testGrating.status == NOT_STARTED:
                # keep track of start time/frame for later
                testGrating.tStart = t
                testGrating.frameNStart = frameN  # exact frame index
                testGrating.setOpacity(1)
                testGrating.setAutoDraw(True)
            frameRemains = 0.0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if testGrating.status == STARTED and t >= frameRemains:
                testGrating.setAutoDraw(False)

            # *testResponse* updates
            if t >= 0.3 and testResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                testResponse.tStart = t
                testResponse.frameNStart = frameN  # exact frame index
                testResponse.status = STARTED

                # keyboard checking is just starting
                win.callOnFlip(testResponse.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')

            if testResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=['right', 'left'])

              ######THIS PART OF THE EXPERIMENT IS REMOVED BECAUSE WORK IS IN PUBLICATION PROCESS. CONTACT ME FOR THIS PART#####################

        # check responses
        if testResponse.keys in ['', [], None]:  # No response was made
            testResponse.keys="None"
            # was no response the correct answer?!
            if str(corrTestAns).lower() == 'none':
               testResponse.corr = 1;  # correct non-response
            else:
               testResponse.corr = "None";  # failed to respond (incorrectly)

        #store response correlations
        response_corrs.append(testResponse.corr)

        #store test keys
        test_keys.append(testResponse.keys)

        #store rts
        rts.append(testResponse.rt)

        # the Routine "Test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # ------Prepare to start Routine "Blank_2"-------
        t = 0
        Blank_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)

        # update component parameters for each repeat
        # keep track of which components have finished
        Blank_2Components = [textBlank, fixationPoint]

        for thisComponent in Blank_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "Blank_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Blank_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *fixationPoint* updates
            if t >= 0.0 and fixationPoint.status == NOT_STARTED:
                fixationPoint.setAutoDraw(True)

            # *textBlank* updates
            if t >= 0.0 and textBlank.status == NOT_STARTED:
                # keep track of start time/frame for later
                textBlank.tStart = t
                textBlank.frameNStart = frameN  # exact frame index
                textBlank.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left

            if textBlank.status == STARTED and t >= frameRemains:
                textBlank.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running

            for thisComponent in Blank_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "Blank_2"-------
        for thisComponent in Blank_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

    df = pd.DataFrame({'StaircaseNo': staircase_no,
          'TestLoc_x':testLoc_xs,
          'TestLoc_y':testLoc_ys,
          'rawTestLoc': raw_test_locs,
          'Orientation': orientations,
          'CorrectAns': correct_answers,
          'TestKey': test_keys,
          'ResponseCorr': response_corrs,
          'RT': rts
          })

    # this function returns StairCase
    return df


######THIS PART OF THE EXPERIMENT IS REMOVED BECAUSE WORK IS IN PUBLICATION PROCESS. CONTACT ME FOR THIS PART#####################

sc_states = [sc_states1, sc_states2, sc_states3]
random.shuffle(sc_states)

sc_list1 = sc_states[0]
sc_list2 = sc_states[1]
sc_list3 = sc_states[2]

# Run mainRoutine-1
df1 = mainRoutine(sc_list1)


# ------Prepare to start Routine "Break_Screen"-------
######THIS PART OF THE EXPERIMENT IS REMOVED BECAUSE WORK IS IN PUBLICATION PROCESS. CONTACT ME FOR THIS PART#####################
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break_Screen"-------
for thisComponent in Break_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Thanks_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Run mainRoutine -2
df2 = mainRoutine(sc_list2)

# ------Prepare to start Routine "Break_Screen"-------
t = 0
Break_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
break_resp = event.BuilderKeyResponse()
# keep track of which components have finished
Break_ScreenComponents = [break_text, break_resp]
for thisComponent in Break_ScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Break_Screen"-------
while continueRoutine:
    # get current time
    t = Break_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *thanksText* updates
    if t >= 0.0 and break_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        break_text.tStart = t
        break_text.frameNStart = frameN  # exact frame index
        break_text.setAutoDraw(True)

    # *thanks_resp* updates
    if t >= 0.0 and break_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        break_resp.tStart = t
        break_resp.frameNStart = frameN  # exact frame index
        break_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if break_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Break_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break_Screen"-------
for thisComponent in Break_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Thanks_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#Run mainRoutine-3
######THIS PART OF THE EXPERIMENT IS REMOVED BECAUSE WORK IS IN PUBLICATION PROCESS. CONTACT ME FOR THIS PART#####################

# ------Prepare to start Routine "Thanks_Screen"-------
t = 0
Thanks_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
thanks_resp = event.BuilderKeyResponse()
# keep track of which components have finished
Thanks_ScreenComponents = [thanksText, thanks_resp]
for thisComponent in Thanks_ScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thanks_Screen"-------
while continueRoutine:
    # get current time
    t = Thanks_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.setAutoDraw(True)

    # *thanks_resp* updates
    if t >= 0.0 and thanks_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks_resp.tStart = t
        thanks_resp.frameNStart = frameN  # exact frame index
        thanks_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if thanks_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thanks_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks_Screen"-------
for thisComponent in Thanks_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Thanks_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
