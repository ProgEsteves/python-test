#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from deus_ex_machina import DeusExMachina as FSM
import unittest 

class FsmTest(unittest.TestCase):

    def testFlowStartCollectProcessStop(self):
        myfsm = FSM()
        self.assertEqual(myfsm.getCurrentState(), 'stopped')
        myfsm.setCurrentState('start')
        self.assertEqual(myfsm.getCurrentState(), 'started')
        myfsm.setCurrentState('collect')
        self.assertEqual(myfsm.getCurrentState(), 'collecting')
        myfsm.setCurrentState('process')
        self.assertEqual(myfsm.getCurrentState(), 'processing')
        myfsm.setCurrentState('stop')
        self.assertEqual(myfsm.getCurrentState(), 'stopped')

    def testFlowStartStop(self):
        myfsm = FSM()
        self.assertEqual(myfsm.getCurrentState(), 'stopped')
        myfsm.setCurrentState('start')
        self.assertEqual(myfsm.getCurrentState(), 'started')
        myfsm.setCurrentState('stop')
        self.assertEqual(myfsm.getCurrentState(), 'stopped')
		
    def testFlowStartCollectStop(self):
        myfsm = FSM()
        self.assertEqual(myfsm.getCurrentState(), 'stopped')
        myfsm.setCurrentState('start')
        self.assertEqual(myfsm.getCurrentState(), 'started')
        myfsm.setCurrentState('collect')
        self.assertEqual(myfsm.getCurrentState(), 'collecting')
        myfsm.setCurrentState('stop')
        self.assertEqual(myfsm.getCurrentState(), 'stopped')
		
if __name__ == "__main__":
    unittest.main()
