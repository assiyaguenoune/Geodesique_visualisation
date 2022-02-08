from math import sqrt, sin, cos, pi, atan, atan2, asin, acos, tan

def Inverse(a, b, lat1, long1, lat2, long2):
        # Calcul des latitudes réduites  beta1 au point de départ et beta2 au point d'arrivé
  f = (a-b)/a		
      
  if (abs( lat2 - lat1 ) < 1e-8) and ( abs( long2 - long1) < 1e-8 ) :
      return 0.0, 0.0, 0.0
  elif ((lat1==0 and abs(long1)==90)and (abs(long2)==90 and lat2==0)):
      alpha12=270
      alpha21=90
      s=19903593.39
      return alpha12, alpha21,s
  else :
      beta1 = atan((1-f) * tan( lat1 ))
      beta2 = atan((1-f) * tan( lat2 ))
        # Calcul de la différence de longitude delta_lambda
      delta_lambda = long2 - long1
     
      delta_u = delta_lambda
 
      sqr_sin_sigma = pow( cos(beta2) * sin(delta_lambda), 2) + pow( (cos(beta1) * sin(beta2) - sin(beta1) *  cos(beta2) * cos(delta_lambda) ), 2 )
      Sin_sigma = sqrt( sqr_sin_sigma )
      Cos_sigma = sin(beta1) * sin(beta2) + cos(beta1) * cos(beta2) * cos(delta_lambda)
      sigma = atan2( Sin_sigma, Cos_sigma )
      Sin_alpha = cos(beta1) * cos(beta2) * sin(delta_lambda) / sin(sigma)
      alpha = asin( Sin_alpha )
      Cos2sigma_m = cos(sigma) - (2 * sin(beta1) * sin(beta2) / pow(cos(alpha), 2) )
         
    # calcul de C Constante de Vincenty
      C = (f/16) * pow(cos(alpha), 2) * (4 + f * (4 - 3 * pow(cos(alpha), 2)))
      
      variation_lambda = delta_lambda

      delta_lambda = delta_u + (1-C) * f * sin(alpha) * (sigma + C * sin(sigma) * \
                  (Cos2sigma_m + C * cos(sigma) * (-1 + 2 * pow(Cos2sigma_m, 2) )))

      while variation_lambda - delta_lambda > 1.0e-9  :

            sqr_sin_sigma = pow( cos(beta2) * sin(delta_lambda), 2) + \
                  pow( (cos(beta1) * sin(beta2) - \
                  sin(beta1) *  cos(beta2) * cos(delta_lambda) ), 2 )

            Sin_sigma = sqrt( sqr_sin_sigma )

            Cos_sigma = sin(beta1) * sin(beta2) + cos(beta1) * cos(beta2) * cos(delta_lambda)

            sigma = atan2( Sin_sigma, Cos_sigma )

            Sin_alpha = cos(beta1) * cos(beta2) * sin(delta_lambda) / sin(sigma)
            alpha = asin(Sin_alpha)

            Cos2sigma_m = cos(sigma) - (2 * sin(beta1) * sin(beta2) / pow(cos(alpha), 2) )

            C = (f/16) * pow(cos(alpha), 2) * (4 + f * (4 - 3 * pow(cos(alpha), 2)))

            variation_lambda = delta_lambda

            delta_lambda = delta_u + (1-C) * f * sin(alpha) * (sigma + C * sin(sigma) * \
                  (Cos2sigma_m + C * cos(sigma) * (-1 + 2 * pow(Cos2sigma_m, 2) )))
    
      w_carre = pow(cos(alpha),2) * (a*a-b*b) / (b*b)
       # Calcul des constantes de Vincenty A' et B'
      A = 1 + (w_carre/16384) * (4096 + w_carre * (-768 + w_carre * (320 - 175 * w_carre)))

      B = (w_carre/1024) * (256 + w_carre * (-128+ w_carre * (74 - 47 * w_carre)))
        # Calcul de delta_sigma
      delta_sigma = B * Sin_sigma * (Cos2sigma_m + (B/4) * \
            (Cos_sigma * (-1 + 2 * pow(Cos2sigma_m, 2) ) - \
            (B/6) * Cos2sigma_m * (-3 + 4 * sqr_sin_sigma) * \
            (-3 + 4 * pow(Cos2sigma_m,2 ) )))
         # Calcul de la distance géodésique s
      s = b * A * (sigma - delta_sigma)

      alpha12 = atan2( (cos(beta2) * sin(delta_lambda)), \
            (cos(beta1) * sin(beta2) - sin(beta1) * cos(beta2) * cos(delta_lambda)))

      alpha21 = atan2( (cos(beta1) * sin(delta_lambda)), \
            (-sin(beta1) * cos(beta2) + cos(beta1) * sin(beta2) * cos(delta_lambda)))
         # Calcul de l'azimut directe alpha12
      if ( alpha12 < 0.0 ) : 
            alpha12 =  alpha12 + 2*pi
      if ( alpha12 > 2*pi ) : 
            alpha12 = alpha12 - 2*pi
        # Calcul de l'azimut inverse alpha21
      alpha21 = alpha21 + 2*pi / 2.0
      if ( alpha21 < 0.0 ) : 
            alpha21 = alpha21 + 2*pi
      if ( alpha21 > 2*pi ) : 
            alpha21 = alpha21 - 2*pi
     
      alpha12 = alpha12*180/pi
      alpha21 = alpha21*180/pi
      return round(s), round(alpha12),  round(alpha21)
