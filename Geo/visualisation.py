from math import *
import matplotlib.pyplot as plt
import numpy as np

def transformation(a,e, latitude, longitude,h):
  phi=latitude
  lamda=longitude
  sinphi=sin(phi)
  e2=e**2
  n=a/sqrt(1-e2*sinphi**2)
  r=(n+h)*cos(phi)
  x=r*cos(lamda)
  z=(n*(1-e2)+h)*sinphi
  return x,z
  
def points(phi1,lamda1,a,b,s):
  n=500
  #pas
  s=s/(n-1)
  