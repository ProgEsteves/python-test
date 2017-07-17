#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from deus_ex_machina import DeusExMachine as FSM
import sys

def exit():
    print('FSM ended.')
    sys.exit(0)

def main():
    myfsm = FSM()
    while True:
        print("Previous state  : {}\nCurrent state   : {}".format(myfsm.getPreviousState(),myfsm.getCurrentState()))
        print("------------\nPossibilities: start - collect - process - stop - exit\nCommand to state: ")
        cmd = input()
		
		# exit FSM when exit typed
        if (cmd == 'exit'):
            exit()
			
		# set new state to FSM
        myfsm.setCurrentState(cmd)
		
		# print array after data collected
        if (myfsm.isstate('collecting')):
            print(myfsm.data.array)
			
		# print array after data processed
        if (myfsm.isstate('processing')):
            print(myfsm.data.array)

if __name__ == "__main__":
    main()
