from math import *

def Direct(lat1,long1,alpha1,s,a,b):
  
    #Ellipsoide paramétres
    f=(a-b)/a
    ep=sqrt((a**2-b**2)/b**2)
    #B1 au point P1
    TanB1=(1-f)*tan(lat1)
    beta1=atan(TanB1)
    #B0 au vertex H0
    CosB0=cos(beta1)*sin(alpha1)
    beta0=acos(CosB0)
    #la constante w
    w2=(ep*sin(beta0))**2
    #distance angulaire au P1
    sigma1=atan(TanB1/cos(alpha1))
    #azimut de la geodésique à l'équateur
    SinalphaE=cos(beta0)
    alphaE=asin(SinalphaE)
    #constantes de Vincenty A B
    A=1.0+(w2/16384)*(4096+w2*(-768+w2*(320-175*w2)))
    B=(w2/1024)*(256+w2*(-128+w2*(74-47*w2)))
    #distance angulaire sur le grand cercle de la sphére auxilaire
    sigma_0=s/b*A
    
    sigma_m=(2.0*sigma1+sigma_0)/2
    
    delta_sigma=B*sin(sigma_0)*(cos(2*sigma_m)+(B/4)*(cos(sigma_0)*(2*pow(cos(2*sigma_m),2)-1))
                -(B/6*cos(2*sigma_m))*(-3+4*pow(sin(sigma_0),2))*(-3+4**pow(cos(2*sigma_m),2)))
    
    sigma=(s/(b*A))+delta_sigma
    
    while(abs(sigma-sigma_0)>0.00001):
        sigma_0=sigma
        sigma_m=(2.0*sigma1+sigma_0)/2
        delta_sigma=B*sin(sigma_0)*(cos(2*sigma_m)+(B/4)*(cos(sigma_0)*(2*pow(cos(2*sigma_m),2)-1))
                -(B/6*cos(2*sigma_m))*(-3+4*pow(sin(sigma_0),2))*(-3+4**pow(cos(2*sigma_m),2)))
    
        sigma=(s/(b*A))+delta_sigma
        #latitude reduite B2
    tanbeta2=(sin(beta1)*cos(sigma)+cos(beta1)*sin(sigma)*cos(alpha1))/sqrt(sin(alphaE)**2+((sin(beta1)*sin(sigma)-cos(beta1)*cos(sigma)*cos(alpha1)))**2)
        #tan(phi2)
    tanphi2=tanbeta2/(1-f) 
        #calcul de phi2
    phi2=atan(tanphi2)
        #calcul de la difference de longitude sur la sphére auxiliaire
    delta_u=sin(sigma)*sin(alpha1)/(cos(beta1)*cos(sigma)-sin(beta1)*sin(sigma)*cos(alpha1))
        #la constante C de vincenty
    C=(f/16)*cos(alphaE)**2*(4+f*(4-3*cos(alphaE)**2))
        #differnce de longitude deltalamda
    delta_lamda=delta_u-(1-C)*f*sin(alphaE)*(sigma+C*sin(sigma)*(cos(2*sigma_m)+C*cos(sigma)*(-1+2*cos(2*sigma_m)**2)))
       #lamda final
    lam2=long1+delta_lamda
        #azimut de alpha2
    alpha2=atan(sin(alphaE)/(cos(beta1)*cos(alpha1)*cos(sigma)-sin(beta1)*sin(sigma)))
    
    if alpha2<0.0:
        alpha2=alpha2+2*pi
    if alpha2>2*pi :
        alpha2=alpha2-2*pi
    phi2=phi2*180/pi
    lam2=lam2*180/pi
    alpha2=alpha2*180/pi
    if lam2>180:
        lam2=lam2-360
    if lam2<-180:
        lam2=lam2+360
    return phi2,lam2,alpha2
  
    
        
    
    
        
  
    
    
    
    