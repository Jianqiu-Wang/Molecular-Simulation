# Script Name   :      getbox.py
# Author        :      Jianqiu Wang
# Created       :      05 Dec 2015
# Last Modified :      17 Dec 2015
# Version       :      1.0
# Description   :      get indexes of box for simulation. Input: datafile of lammps, output: a list contains 3 lengths and 3 tilt values for each time.

def getBox(f):
    file = open(f,'r')
    box=[]
    position=[]
    position2=[]
    for i, line in enumerate(file):
        if 'Lx Ly Lz Xy Xz Yz' in line:
            position.append(i)
        if 'Loop time of' in line:
            position2.append(i);
    file.close()
    file = open(f,'r')
    for i, line in enumerate(file):
        for j in range(len(position)):
            if i> position[j] and i< position2[j]:
                box.append(map(float,line.split()[7:12]))
    file.close()
    for i in range(3):
        box.pop(0)
    return box
    # print box
    
getBox('in.chloroform.conc.15.out')


