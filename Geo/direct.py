from math import *

def Direct(lat1,long1,alpha_direct,s,a,b) :
        
        # calcul de l'aplatissement 'f' :
        f = (a-b)/a
        
        # calcul de la latitude réduite 'beta1' :  
        if abs(lat1)==90:
                beta1=lat1
        else:		
               Tanbeta1 = (1-f) * tan(lat1)
               beta1 = atan(Tanbeta1)
               
        # calcul de la latitude réduite 'beta0' du vertex :  
        cosBeta0 = cos(beta1) * sin(alpha_direct)
        sinBeta0 = 1.0 - cosBeta0 * cosBeta0
        
        # calcul de la constante 'w_carré' :
        w_carré = sinBeta0 * (a * a - b * b ) / (b * b)
        
        # calcul de la distance angulaire 'sigma1' sur la dphère auxiliaire : 
        sigma1 = atan2( Tanbeta1, cos(alpha_direct) )
        
        # calcul des constantes de Vincenty A et B :        
        A = 1.0 + (w_carré / 16384) * (4096 + w_carré * (-768 + w_carré * \
                (320 - 175 * w_carré) ) )
        B = (w_carré / 1024) * (256 + w_carré * (-128 + w_carré * (74 - 47 * w_carré) ) )

        # start avec approximation :
        sigma = (s / (b * A))
        last_sigma = 2.0 * sigma + 2.0
        two_sigma_m = (2 * sigma1 + sigma)/2
        
        #  until there is no significant change in sigma 
        delsig = B*sin(sigma)*(cos(2*two_sigma_m)+0.25*B*(cos(sigma)*(2*cos(2*two_sigma_m)**2-1)-B/6*cos(2*two_sigma_m)*(-3+4*sin(sigma)**2)*(-3+4*cos(2*two_sigma_m)**2)))
        # two_sigma_m , delta_sigma
        count = 0
        while ( abs( two_sigma_m) > 0.01 and count<200) :
                two_sigma_m = 2 * sigma1 + sigma

                delta_sigma = B * sin(sigma) * ( cos(two_sigma_m) 
                        + (B/4) * (cos(sigma) * 
                        (-1 + 2 * pow( cos(two_sigma_m), 2 ) -  
                        (B/6) * cos(two_sigma_m) * \
                        (-3 + 4 * pow(sin(sigma), 2 )) *  \
                        (-3 + 4 * pow( cos (two_sigma_m), 2 ))))) 
                
                last_sigma = sigma
                sigma = (s / (b * A)) + delta_sigma
                count = count+1
        
        # calcul de latitude_2 'lat2' :
        lat2 = atan2 ( (sin(beta1) * cos(sigma) + cos(beta1) * sin(sigma) * cos(alpha_direct) ), \
                ((1-f) * sqrt( pow(cosBeta0, 2) +  \
                pow(sin(beta1) * sin(sigma) - cos(beta1) * cos(sigma) * cos(alpha_direct), 2))))

        lembda = atan2( (sin(sigma) * sin(alpha_direct )), (cos(beta1) * cos(sigma) -  \
                sin(beta1) *  sin(sigma) * cos(alpha_direct)))

        C = (f/16) * sinBeta0 * (4 + f * (4 - 3 * sinBeta0 ))

        omega = lembda - (1-C) * f * cosBeta0 *  \
                (sigma + C * sin(sigma) * (cos(two_sigma_m) + \
                C * cos(sigma) * (-1 + 2 * pow(cos(two_sigma_m),2) )))
        
        # calcul de longitude_2 'long2' :
        long2 = long1 + omega
        
        # calcul de azimut inverse 'alpha_inverse' :
        alpha_inverse = atan2 ( cosBeta0, (-sin(beta1) * sin(sigma) +  \
                cos(beta1) * cos(sigma) * cos(alpha_direct)))
        alpha_inverse = alpha_inverse + 2*pi / 2.0
        
        # etude des conditions de azimut inverse :
        if ( alpha_inverse < 0.0 ) :
                alpha_inverse = alpha_inverse + 2*pi
        if ( alpha_inverse > 2*pi ) :
                alpha_inverse = alpha_inverse - 2*pi
        
        # convertion de radian vers degrée :
        lat2 = lat2*180/pi
        long2= long2*180/pi
        alpha_inverse   = alpha_inverse*180/pi
        
        # etude des conditions de longitude_2 :
        if long2>180:
                long2 =long2-360
        if long2<-180:
                long2 = long2+360
                
        return lat2,long2, alpha_inverse 


    
        
    
    
        
  
    
    
    
    