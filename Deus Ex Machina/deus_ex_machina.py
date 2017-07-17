#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lib Fysom implements a FSM behavior based on a dictionaty structure
from fysom import Fysom, FysomError
from data import Data 

class DeusExMachina(object):

    # event occurs when state change to collect
    def oncollect(self, e):
        self.data.collectData()

	# event occurs when state change to process
    def onprocess(self, e):
	    # process data with scalar 5
        self.data.processData(5)

	# event occurs when state change
    def onchangestate(self, e):
	    # save previous state
        self.prevState = e.src

    # check current state by string
    def isstate(self, s):
        return self.fsm.isstate(s)

    def __init__(self):
        self.prevState = None
        self.data = Data()
		
		# starts FSM (Fysom) rules, like described in state transitions table
        self.fsm = Fysom({'initial': 'stopped',
                'events': [
                    {'name': 'start', 'src': 'stopped', 'dst': 'started'},
                    {'name': 'collect', 'src': 'started', 'dst': 'collecting'},
                    {'name': 'stop', 'src': 'started', 'dst': 'stopped'},
                    {'name': 'process', 'src': 'collecting', 'dst': 'processing'},
                    {'name': 'stop', 'src': 'collecting', 'dst': 'stopped'},
                    {'name': 'stop', 'src': 'processing', 'dst': 'stopped'}],
                'callbacks': {
                    'oncollect': self.oncollect,
                    'onprocess': self.onprocess}})
        self.fsm.onchangestate = self.onchangestate

    def getPreviousState(self):
        return self.prevState

    def getCurrentState(self):
        return self.fsm.current

    def setCurrentState(self, value):
        try:
            options = {
                'start': self.fsm.start,
                'stop': self.fsm.stop,
                'process': self.fsm.process,
                'collect': self.fsm.collect
            }
            options[value]()
        except KeyError:
            print('An error ocorred when you send a command to FSM: Command unregonized.')
        except FysomError:
            print('An error ocorred when you send a command to FSM: Invalid state.')
	