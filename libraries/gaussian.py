# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
'''
#-------------------------------------------------------------------------------
# FEDERAL UNIVERSITY OF UBERLANDIA - UFU
# Faculty of Electrical Engineering - FEELT
# Biomedical Engineering Lab - Biolab
#-------------------------------------------------------------------------------
# Description:
#-------------------------------------------------------------------------------
'''
#-------------------------------------------------------------------------------
import numpy as np
#-------------------------------------------------------------------------------
#this class defines the gaussian parameters that behave as the receptive field
#of the artificial spiking neuron
#-------------------------------------------------------------------------------
class gaussianModel():
    def __init__(self, width_gauss = 0, mean_gauss = 0):
        self.widthGauss = width_gauss
        self.meanGauss = mean_gauss

    #create any number of neurons to cover the input
    def create(number_neurons, nmin, nmax, beta):
        listObj = []
        for i in range(number_neurons):
            mean_gauss = nmin + ((2*i-3)/2) * ((nmax-nmin)/(number_neurons-2))
            width_gauss = (nmax - nmin) / (beta * (number_neurons-2))
            gObj = gaussianModel(width_gauss,mean_gauss)
            listObj.append(gObj)
        return listObj
#-------------------------------------------------------------------------------
#this function converts the input into spikes based on the gaussian properties
#of the neuron
def conv_input2spikes(gaussObj, input_val, Imax):
    Ineurons = []
    for i in range(len(gaussObj)):
        Im = Imax * np.exp(-1 * (np.power((input_val-gaussObj[i].meanGauss),2))/(2*np.power(gaussObj[i].widthGauss,2)))
        Ineurons.append(Im)
    return Ineurons
#-------------------------------------------------------------------------------
#example
if __name__ == '__main__':
    #plot figure
    import matplotlib.pyplot as plt

    #input signal parameters
    minVal = -32768 #minimum value of the input
    maxVal = 32767 #maximum value of the input

    #parameters for creating the neurons
    numbNeurons = 5 #number of neurons
    vbeta = 1.5 #adjustment factor
    maxIm = 10 #maximum value for the input current to the neuron


    #generate the gaussians
    gaussianNeurons = gaussianModel.create(numbNeurons, minVal, maxVal, vbeta)

    #generate an input
    inputvals = np.arange(-65536,65536)

    gaussResponse =  conv_input2spikes(gaussianNeurons, inputvals, maxIm)

    #plot the gaussians as a function of the input
    plt.figure()
    [plt.plot(inputvals, x) for x in gaussResponse]
    plt.show()
