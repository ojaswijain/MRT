# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:45:21 2021

@author: ojasw
"""

import numpy as np
#Trying out various loss functions with a crude dataset

#for classification models
def logLoss(ystar, y):
    if y==1:
        return -np.log(ystar)
    elif y==0:
        return -np.log(1-ystar)

#for regression models
def MSE(ystar, y):
    return np.sum((ystar-y)**2)/y.size()

