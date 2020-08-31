from turtle import*
from random import*
from math import*
import datetime
from platform import*
import os

speed(10)
Date=datetime.datetime.now()
DATE="{}/{}/{}".format(Date.day,Date.month,Date.year)
X=[]
Y=[]
S,N,i=0,random(),0
pensize(width=4)
#N=int(N)
penup()
def write(x,y,DATE):
    f=open("coordinates_of_the_{}.txt".format(DATE),"w")
    f.write("\n=========== A few stats ======================\nFile path:{}\nDate of the creation of the file:{}\nos:{}\n=========== End of a few stats ======================\n")
def set_pixel(x,y):
    setx(int(200*x))
    sety(int(200-200*y))
def point_red(x,y):
    pencolor("red")
    set_pixel(x,y)
    pendown()
    dot(5)
    penup()
def point_blue(x,y):
    pencolor("blue")
    set_pixel(x,y)
    pendown()
    dot(5)
    penup()

while i<N+1:
    x,y=random(),random()            
    if hypot(x, y)<1:
        S+=1
        point_red(x,y)
        X.append(x)
        Y.append(y)
    else:
        point_blue(x,y)
        X.append(x)
        Y.append(y)
    print("x={}\ny={}".format(X,Y))
