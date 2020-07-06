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
# LIBRARIES
#-------------------------------------------------------------------------------
import numpy as np
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class alpha_synapse():
    def __init__(self, _weight = 1, _tau = 0.5):
        self.weight = _weight
        self.tau = _tau
        self.synout = []

    def integrate(self, t, t_spike):
        if t_spike is None:
            synv = 0
        elif t < t_spike:
            synv = 0
        else:
            #debugging
            #print(t,t_spike,(((t-t_spike)/self.tau) * np.exp(1 - (((t-t_spike)/self.tau)))))
            synv = self.weight * (((t-t_spike)/self.tau) * np.exp(1 - (((t-t_spike)/self.tau))))

        self.synout.append(synv)
        return synv
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import spiking_neurons as spkn

    #synapse
    synapsem = alpha_synapse(8, 2.8)
    synapsem = alpha_synapse(-8, 2.8)
    #tspikes = [10, 18, 19, 20, 21, 22, 29, 60, 80, 88, 92, 96, 150,151,152,153]
    tspikes = [120,121,127,128,129,130,131,135,139,142,148,154,160,170,190]
    dt = 1
    time = np.arange(0,250,dt)
    aux_cont = 0
    tspk = tspikes[0]
    synapse_output = []

    #output neuron
    nrn1 = spkn.model.izhikevich()
    vneuron = []

    for i in range(len(time)):

        synapse_output.append(synapsem.integrate(time[i], tspk))
        resp = nrn1.integrate(synapse_output[-1], dt=dt)
        vneuron.append(resp[1])

        if(aux_cont < len(tspikes)):
            if(time[i] >= tspikes[aux_cont]):
                tspk = tspikes[aux_cont]
                aux_cont += 1

    simul = spkn.simulation(t0=0,tf=len(time),dt=dt,neurons=[nrn1],I=[synapse_output])
    simul.optIzhikevich()

    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(time,synapse_output)
    plt.scatter(tspikes,[11]*len(tspikes),marker='|',color='black')
    plt.subplot(2,1,2)
    plt.plot(simul.vneurons[0])

    plt.show()
