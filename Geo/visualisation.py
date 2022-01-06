from math import *

def transformation(a,e, latitude, longitude,h):
  phi=latitude
  lamda=longitude
  sinphi=sin(phi)
  e2=e**2
  n=a/sqrt(1-e2*sinphi**2)
  r=(n+h)*cos(phi)
  x=r*cos(lamda)
  z=(n*(1-e2)+h)*sinphi
  return x,y,z
  
  
  