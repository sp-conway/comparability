#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Wed Jan 29 16:17:46 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'comp'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'computer_n': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/seanconway/Research/Perceptual_CE/comparability/experiment_code/comp_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "exp_params" ---
    # Run 'Begin Experiment' code from params
    import psychopy
    import numpy as np
    d1_r=np.arange(57,133)
    d2_r=np.arange(125,200)
    dim_min = 57
    dim_max = 200
    screen_width=win.size[0]
    screen_height=win.size[1]
    screen_center_x=0
    screen_center_y=0
    r_1_x=-round(screen_width*.33)
    r_2_x=0
    r_3_x=round(screen_width*.33)
    y_jitter=30
    prompt_x_loc=0
    prompt_y_loc=round(-(screen_height/2)*.75)
    # Run 'Begin Experiment' code from fncs_
    def sample_diag (d, intcpt):
        w=np.random.choice(d)
        h=intcpt-w
        stim=np.array([w,h])
        return stim
    
    # --- Initialize components for Routine "pre_trial" ---
    
    # --- Initialize components for Routine "choice_trial" ---
    r_1 = visual.Rect(
        win=win, name='r_1',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0039, 0.0039, 0.0039],
        opacity=None, depth=0.0, interpolate=True)
    r_2 = visual.Rect(
        win=win, name='r_2',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0039, 0.0039, 0.0039],
        opacity=None, depth=-1.0, interpolate=True)
    r_3 = visual.Rect(
        win=win, name='r_3',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0039, 0.0039, 0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    mouse_choice = event.Mouse(win=win)
    x, y = [None, None]
    mouse_choice.mouseClock = core.Clock()
    r_1_label = visual.TextStim(win=win, name='r_1_label',
        text='1',
        font='Arial',
        pos=[0,0], draggable=False, height=5.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    r_2_label = visual.TextStim(win=win, name='r_2_label',
        text='2',
        font='Arial',
        pos=[0,0], draggable=False, height=5.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    r_3_label = visual.TextStim(win=win, name='r_3_label',
        text='3',
        font='Arial',
        pos=[0,0], draggable=False, height=5.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    prompt = visual.TextStim(win=win, name='prompt',
        text='Click on the rectangle with the largest area.\n',
        font='Arial',
        pos=(prompt_x_loc, prompt_y_loc), draggable=False, height=10.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "exp_params" ---
    # create an object to store info about Routine exp_params
    exp_params = data.Routine(
        name='exp_params',
        components=[],
    )
    exp_params.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for exp_params
    exp_params.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    exp_params.tStart = globalClock.getTime(format='float')
    exp_params.status = STARTED
    thisExp.addData('exp_params.started', exp_params.tStart)
    exp_params.maxDuration = None
    # keep track of which components have finished
    exp_paramsComponents = exp_params.components
    for thisComponent in exp_params.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp_params" ---
    exp_params.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            exp_params.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_params.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_params" ---
    for thisComponent in exp_params.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for exp_params
    exp_params.tStop = globalClock.getTime(format='float')
    exp_params.tStopRefresh = tThisFlipGlobal
    thisExp.addData('exp_params.stopped', exp_params.tStop)
    thisExp.nextEntry()
    # the Routine "exp_params" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=3.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('trials.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "pre_trial" ---
        # create an object to store info about Routine pre_trial
        pre_trial = data.Routine(
            name='pre_trial',
            components=[],
        )
        pre_trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from rect_dims
        if effect=="critical":
            h_1_tmp=h_1
            w_1_tmp=w_2
            h_2_tmp=h_2
            w_2_tmp=w_2
            h_3_tmp=h_3
            w_3_tmp=w_3
        elif effect=="filler":
            h_1_tmp=np.random.uniform(dim_min,dim_max,1)
            w_1_tmp=np.random.uniform(dim_min,dim_max,1)
            h_2_tmp=np.random.uniform(dim_min,dim_max,1)
            w_2_tmp=np.random.uniform(dim_min,dim_max,1)
            h_3_tmp=np.random.uniform(dim_min,dim_max,1)
            w_3_tmp=np.random.uniform(dim_min,dim_max,1)
        elif effect=="catch":
            u_1=sample_diag(d3_r, d3_int)
            l_1=sample_diag(d1_r, d1_int)
            l_2=sample_diag(d1_r, d1_int)
            which_upper=np.random.choice(np.arange(3))
            if which_upper==0:
                w_1_tmp=u_1[0]
                h_1_tmp=u_1[1]
                w_2_tmp=l_1[0]
                h_2_tmp=l_1[1]
                w_3_tmp=l_2[0]
                h_3_tmp=l_2[1]
            elif which_upper==1:
                w_1_tmp=l_1[0]
                h_1_tmp=l_1[1]
                w_2_tmp=u_1[0]
                h_2_tmp=u_1[1]
                w_3_tmp=l_2[0]
                h_3_tmp=l_2[1]
            else:
                w_1_tmp=l_1[0]
                h_1_tmp=l_1[1]
                w_2_tmp=l_2[0]
                h_2_tmp=l_2[1]
                w_3_tmp=u_2[0]
                h_3_tmp=u_2[1]
            
        # Run 'Begin Routine' code from rect_locs
        if effect == "critical":
            config_tmp = config
        else:
            config_tmp = np.random.choice([1, 2.1, 2.2, 3])
        
        if config_tmp == 1:
            r_1_y = round(0 + np.random.uniform(-y_jitter, y_jitter, 1))
            r_2_y = round(0 + np.random.uniform(-y_jitter, y_jitter, 1))
            r_3_y = round(0 + np.random.uniform(-y_jitter, y_jitter, 1))  
        elif config_tmp == 2.1:
            r_1_y = -round(screen_height * .33 + np.random.uniform(-y_jitter, y_jitter, 1))
            r_2_y = -round(screen_height * .33 + np.random.uniform(-y_jitter, y_jitter, 1))
            r_3_y = round(screen_height * .33 + np.random.uniform(-y_jitter, y_jitter, 1))
        elif config_tmp == 2.2:
            r_1_y = -round(screen_height * .33 + np.random.uniform(-y_jitter, y_jitter, 1))
            r_2_y = round(screen_height * .33 + np.random.uniform(-y_jitter, y_jitter, 1))
            r_3_y = round(screen_height * .33 + np.random.uniform(-y_jitter, y_jitter, 1))
        elif config_tmp == 3:
            r_1_y = -round(screen_height * .33 + np.random.uniform(-y_jitter, y_jitter, 1))
            r_2_y = round(0 + np.random.uniform(-y_jitter, y_jitter, 1))
            r_3_y = round(screen_height * .33 + np.random.uniform(-y_jitter, y_jitter, 1))
        else:
            raise ValueError(f"Unexpected config_tmp value: {config_tmp}")
        r_1_txt_x=r_1_x
        r_1_txt_y=r_1_y+50
        r_2_txt_x=r_2_x
        r_2_txt_y=r_2_y+50
        r_3_txt_x=r_3_x
        r_3_txt_y=r_3_y+50
        # store start times for pre_trial
        pre_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pre_trial.tStart = globalClock.getTime(format='float')
        pre_trial.status = STARTED
        thisExp.addData('pre_trial.started', pre_trial.tStart)
        pre_trial.maxDuration = None
        # keep track of which components have finished
        pre_trialComponents = pre_trial.components
        for thisComponent in pre_trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pre_trial" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        pre_trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                pre_trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pre_trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pre_trial" ---
        for thisComponent in pre_trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pre_trial
        pre_trial.tStop = globalClock.getTime(format='float')
        pre_trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('pre_trial.stopped', pre_trial.tStop)
        # the Routine "pre_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "choice_trial" ---
        # create an object to store info about Routine choice_trial
        choice_trial = data.Routine(
            name='choice_trial',
            components=[r_1, r_2, r_3, mouse_choice, r_1_label, r_2_label, r_3_label, prompt],
        )
        choice_trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        r_1.setPos((r_1_x, r_1_y))
        r_1.setSize([w_1_tmp, h_1_tmp])
        r_2.setPos((0, 0))
        r_2.setSize([w_2_tmp, h_2_tmp])
        r_3.setPos((0, 0))
        r_3.setSize((w_3_tmp, h_3_tmp))
        # setup some python lists for storing info about the mouse_choice
        mouse_choice.x = []
        mouse_choice.y = []
        mouse_choice.leftButton = []
        mouse_choice.midButton = []
        mouse_choice.rightButton = []
        mouse_choice.time = []
        mouse_choice.clicked_choice = []
        gotValidClick = False  # until a click is received
        r_1_label.setPos((r_1_txt_x, r_1_txt_y))
        r_2_label.setPos((r_2_txt_x, r_2_txt_y))
        r_3_label.setPos((r_3_txt_x, r_3_txt_y))
        # store start times for choice_trial
        choice_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        choice_trial.tStart = globalClock.getTime(format='float')
        choice_trial.status = STARTED
        thisExp.addData('choice_trial.started', choice_trial.tStart)
        choice_trial.maxDuration = None
        # keep track of which components have finished
        choice_trialComponents = choice_trial.components
        for thisComponent in choice_trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "choice_trial" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        choice_trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *r_1* updates
            
            # if r_1 is starting this frame...
            if r_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                r_1.frameNStart = frameN  # exact frame index
                r_1.tStart = t  # local t and not account for scr refresh
                r_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(r_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'r_1.started')
                # update status
                r_1.status = STARTED
                r_1.setAutoDraw(True)
            
            # if r_1 is active this frame...
            if r_1.status == STARTED:
                # update params
                pass
            
            # *r_2* updates
            
            # if r_2 is starting this frame...
            if r_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                r_2.frameNStart = frameN  # exact frame index
                r_2.tStart = t  # local t and not account for scr refresh
                r_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(r_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'r_2.started')
                # update status
                r_2.status = STARTED
                r_2.setAutoDraw(True)
            
            # if r_2 is active this frame...
            if r_2.status == STARTED:
                # update params
                pass
            
            # *r_3* updates
            
            # if r_3 is starting this frame...
            if r_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                r_3.frameNStart = frameN  # exact frame index
                r_3.tStart = t  # local t and not account for scr refresh
                r_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(r_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'r_3.started')
                # update status
                r_3.status = STARTED
                r_3.setAutoDraw(True)
            
            # if r_3 is active this frame...
            if r_3.status == STARTED:
                # update params
                pass
            # *mouse_choice* updates
            
            # if mouse_choice is starting this frame...
            if mouse_choice.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_choice.frameNStart = frameN  # exact frame index
                mouse_choice.tStart = t  # local t and not account for scr refresh
                mouse_choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_choice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_choice.started', t)
                # update status
                mouse_choice.status = STARTED
                mouse_choice.mouseClock.reset()
                prevButtonState = mouse_choice.getPressed()  # if button is down already this ISN'T a new click
            if mouse_choice.status == STARTED:  # only update if started and not finished!
                buttons = mouse_choice.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([r1, r2, r3], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_choice):
                                gotValidClick = True
                                mouse_choice.clicked_choice.append(obj.choice)
                        if not gotValidClick:
                            mouse_choice.clicked_choice.append(None)
                        x, y = mouse_choice.getPos()
                        mouse_choice.x.append(x)
                        mouse_choice.y.append(y)
                        buttons = mouse_choice.getPressed()
                        mouse_choice.leftButton.append(buttons[0])
                        mouse_choice.midButton.append(buttons[1])
                        mouse_choice.rightButton.append(buttons[2])
                        mouse_choice.time.append(mouse_choice.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # *r_1_label* updates
            
            # if r_1_label is starting this frame...
            if r_1_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                r_1_label.frameNStart = frameN  # exact frame index
                r_1_label.tStart = t  # local t and not account for scr refresh
                r_1_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(r_1_label, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'r_1_label.started')
                # update status
                r_1_label.status = STARTED
                r_1_label.setAutoDraw(True)
            
            # if r_1_label is active this frame...
            if r_1_label.status == STARTED:
                # update params
                pass
            
            # *r_2_label* updates
            
            # if r_2_label is starting this frame...
            if r_2_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                r_2_label.frameNStart = frameN  # exact frame index
                r_2_label.tStart = t  # local t and not account for scr refresh
                r_2_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(r_2_label, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'r_2_label.started')
                # update status
                r_2_label.status = STARTED
                r_2_label.setAutoDraw(True)
            
            # if r_2_label is active this frame...
            if r_2_label.status == STARTED:
                # update params
                pass
            
            # *r_3_label* updates
            
            # if r_3_label is starting this frame...
            if r_3_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                r_3_label.frameNStart = frameN  # exact frame index
                r_3_label.tStart = t  # local t and not account for scr refresh
                r_3_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(r_3_label, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'r_3_label.started')
                # update status
                r_3_label.status = STARTED
                r_3_label.setAutoDraw(True)
            
            # if r_3_label is active this frame...
            if r_3_label.status == STARTED:
                # update params
                pass
            
            # *prompt* updates
            
            # if prompt is starting this frame...
            if prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt.frameNStart = frameN  # exact frame index
                prompt.tStart = t  # local t and not account for scr refresh
                prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt.started')
                # update status
                prompt.status = STARTED
                prompt.setAutoDraw(True)
            
            # if prompt is active this frame...
            if prompt.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                choice_trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in choice_trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "choice_trial" ---
        for thisComponent in choice_trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for choice_trial
        choice_trial.tStop = globalClock.getTime(format='float')
        choice_trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('choice_trial.stopped', choice_trial.tStop)
        # store data for trials (TrialHandler)
        trials.addData('mouse_choice.x', mouse_choice.x)
        trials.addData('mouse_choice.y', mouse_choice.y)
        trials.addData('mouse_choice.leftButton', mouse_choice.leftButton)
        trials.addData('mouse_choice.midButton', mouse_choice.midButton)
        trials.addData('mouse_choice.rightButton', mouse_choice.rightButton)
        trials.addData('mouse_choice.time', mouse_choice.time)
        trials.addData('mouse_choice.clicked_choice', mouse_choice.clicked_choice)
        # the Routine "choice_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
