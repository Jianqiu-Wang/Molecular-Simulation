# Script Name   :      get_newpostion.py
# Author        :      Jianqiu Wang
# Created       :      12 Jan 2016
# Last Modified :      12 Jan 2016
# Version       :      1.0
# Description   :      get recovered postion for 1 molecule. Input: coordinates of 1 molecule and box index(3*3 matrix in Lammps), output: new position of the molecule

def getNewposition(box,atom):
    
    # box: 6 element array [xhi-xlo,yhi-ylo,zhi-zlo,xtilt,ytilt,ztilt]
    # atom: array of atom coords (order by xyz file)
    
    box_x=[box[0],0,0]              # [xhi-xlo ,0       ,0       ]
    box_y=[box[3],box[1],0]         # [xtilt   ,yhi-ylo ,0       ]
    box_z=[box[4],box[5],box[2]]    # [ytilt   ,ztilt   ,zhi-zlo ]
    box_matrix= [box_x,box_y,box_z]

    for i in range(len(atom)-1):    # for  n atoms, only deal with n-1 times   
        for j in range(3):          # loop over x,y and z
            if atom[i+1][j]-atom[i][j]>30:
                for k in range(3):
                    atom[i+1][k] = atom[i+1][k]-box_matrix[j][k]
            if atom[i+1][j]-atom[i][j]< -30:
                for k in range(3):
                    atom[i+1][k] = atom[i+1][k]+box_matrix[j][k]

    return atom
