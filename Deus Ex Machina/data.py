#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

class Data(object):

    def __init__(self):
        self.array = []
	
    @property
    def array(self):
        return self.__data
	
    @array.setter
    def array(self, arr):
        self.__data = arr

    # generate and return a array of size 3x3 containing random numbers between 0 and 9
    def collectData(self):
        self.array = np.random.randint(10, size=(3, 3))

    # multiply each element by the scalar 5 and calculate the transposed
    def processData(self, scalar=1):
        self.array = np.transpose(self.array * scalar)
