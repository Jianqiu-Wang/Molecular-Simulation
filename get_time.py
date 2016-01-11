# Script Name   :      get_time.py
# Author        :      Jianqiu Wang
# Created       :      11 Jan 2016
# Last Modified :      11 Jan 2016
# Version       :      1.0
# Description   :      get md timestep. Input: output file of lammps, output: a one dimensional array containing timestep of simulation.

def getTime(filename):
    f = open(filename)
    timestep = [] 
    position1 = []
    position2 = [] # effective datas are placed separately in Lammps output file 
    
    for i, line in enumerate(f):
        if 'Setting up run' in line:
            position1.append(i+3)
        if 'Loop time of' in line:
            position2.append(i)
    position2.pop(0)
    if len(position1)!=len(position2):
        print 'Array Length Does NOT Match ERROR'
    f.close

    f = open(filename)
    for i, line in enumerate(f):
        for j in range(len(position1)):
            if i>position1[j] and i<position2[j]:
                timestep.append(int(line.split()[0]))
    f.close()
    
    return timestep

# getTime('in.chloroform.conc.15.out')
