# Script Name   :   move_back.py 
# Author        :   Jianqiu Wang
# Created       :   04 Dec 2015
# Last Modified :   12 Jan 2016
# Modifications :   20 Dec 2015 : unify coords change by bbbox
#                   11 Jan 2016 : get timestep from get_time.py 
# Description   :   put atoms back into original position for each timestep


import get_box
import get_newposition
import get_initposition
import write_position

def moveBack(filename,data_file):
    #use function moveBack to get original coordinates of atoms f is the filename'''
    
    atom = get_initposition.getInitposition(filename)
    box = get_box.getBox(data_file)
    for i in range(len(atom)):                                     # for each Timestep
        atom[i] = get_newposition.getNewposition(box[i],atom[i]) 
    write_position.writePosition(atom,filename)                    # write final position

# move_back('test.xyz','in.chloroform.conc.15.out')
