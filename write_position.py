# Script Name   :   write_position.py 
# Author        :   Jianqiu Wang
# Created       :   12 Jan 2016
# Version       :   1.0
# Last Modified :   12 Jan 2016
# Description   :   put atoms back into original position for each timestep

def writePosition(atom,filename):
        
    output =  open('NewPostion'+filename,'w')
    with open(filename) as f:
        for i, line in enumerate(f):
            pass
    totalline = i + 1
    
    f = open(filename)
    nmatom = int(f.readline())
    nmline = nmatom + 2

    for i in range(totalline):
        if i% nmline == 0:
            output.write(str(nmatom)+'\n')
        elif i% nmline == 1:
            output.write('Timestep:'+str(i/nmline)+'\n')
        else:                                                             
            ii = i/nmline                                                   
            jj = i%nmline-2                                                 
            output.write('S '+str(atom[ii][jj][0])+' '+str(atom[ii][jj][1])+' '+str(atom[ii][jj][2])+'\n')
