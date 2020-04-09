import matplotlib.pyplot as plt
import numpy as np
from math import *

def rotate(p1,p2,c,angle):
    p1 = np.array(p1)
    p2 = np.array(p2)
    c  = np.array(c)
    new_p1 = [p1[0]*np.cos(angle)+p1[1]*np.sin(angle),-p1[0]*np.sin(angle)+p1[1]*np.cos(angle)]
    new_p2 = [p2[0]*np.cos(angle)+p2[1]*np.sin(angle),-p2[0]*np.sin(angle)+p2[1]*np.cos(angle)]
    new_c  = [c[0]*np.cos(angle)+c[1]*np.sin(angle),-c[0]*np.sin(angle)+c[1]*np.cos(angle)]
    return new_p1, new_p2, new_c

def create_fig():
    fig, ax = plt.subplots(figsize=(5,5))
    ax.axis('off')
    ax.set_xlim(-3,3)
    ax.set_ylim(-3,3)
    return fig,ax

def back_circle(ax,label):
    bc = plt.Circle((0,0),1,color='red',fill=False)
    ax.add_artist(bc)
    ax.annotate(label,(2**(.5)/2.5,2**(.5)/2.5),color='red',ha='center',va='center',fontweight='bold')
    return ax

def front_circle(ax,label):
    fc = plt.Circle((0,0),.3,color='black',fill=False)
    ax.annotate(label,(0,0),ha='center',va='center',color='black',fontweight='bold')
    ax.add_artist(fc)
    return ax

def add_back_atoms(ax,labels,reference,angles):
    first_l = labels[1]
    ax.plot([0,0],[1,1.5],color='red')
    c = plt.Circle((0,1.8),.3,color='red')
    ax.add_artist(c)
    ax.annotate(first_l,(0,1.8),ha='center',va='center',fontweight='bold')

    bottom = [0,1]
    top = [0,1.5]
    circle = [0,1.8]

    for i,angle in enumerate(angles):
        angle = radians(360-angle+reference)
        p1,p2,newc = rotate(bottom,top,circle,angle)
        xvals = [p1[0],p2[0]]
        yvals = [p1[1],p2[1]]
        ax.plot(xvals,yvals,color='red')
        circ = plt.Circle(newc,.3,color='red')
        ax.add_artist(circ)
        ax.annotate(labels[i+2],newc,ha='center',va='center',fontweight='bold')
    return ax

def add_front_atoms(ax,labels,angles):
    bottom = [0,.3]
    top = [0,1.5]
    circle = [0,1.8]
    for i,angle in enumerate(angles):
        angle = radians(angle)
        p1,p2,newc = rotate(bottom,top,circle,angle)
        xvals = [p1[0],p2[0]]
        yvals = [p1[1],p2[1]]
        ax.plot(xvals,yvals,'--',color='black')
        circ = plt.Circle(newc,.3,color='black')
        ax.add_artist(circ)
        ax.annotate(labels[i+1],newc,ha='center',va='center',color='white',fontweight='bold')
    return ax

def newman(back_atoms,front_atoms,back_angles,front_angles):
    plt.ioff()
    fig,ax = create_fig()
    ax = back_circle(ax,back_atoms[0])
    ax = front_circle(ax,front_atoms[0])
    ax = add_back_atoms(ax,back_atoms,front_angles[0],back_angles)
    ax = add_front_atoms(ax,front_atoms,front_angles)
    plt.close()

    return fig
