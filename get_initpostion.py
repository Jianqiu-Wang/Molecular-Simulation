# Script Name   :      get_initpostion.py
# Author        :      Jianqiu Wang
# Created       :      12 Jan 2016
# Last Modified :      12 Jan 2016
# Version       :      1.0
# Description   :      get initial postion for all atoms in one coordinate file. Input: coordinate file, output: an array of atom coordinates

def getInitposition(filename):

    with open(filename) as f: 
        for i, line in enumerate(f):
            pass
    totalline = i + 1
    atom = []
    j = -1    

    f = open(filename)
    nmatom = int(f.readline())    # number of atoms in 1 molecule
    f.close() 
    
    nmline = nmatom + 2           # number of lines (nmatom+2)
    nmchain = totalline/nmline                # number of chains in system
    
    f = open(filename)
    for i, line in enumerate(f):
        if i% nmline == 0:
            j =j+1
            atom.append([])
            totalline = totalline+nmline
        if i% nmline >= 2:
            atom[j].append(map(float,line.split()[1:]))
    f.close()
    return atom

# getInitposition('test.xyz')
    
