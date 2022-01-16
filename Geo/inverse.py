from math import sqrt, sin, cos, pi, atan, atan2, asin, acos, tan

def Inverse(a, b, lat1, long1, lat2, long2):
    f = (a - b) / a
    if (abs(lat2 - lat1) < 1e-8) and (abs(long2 - long1) < 1e-8):
        return 0.0, 0.0, 0.0
    
    # Calcul des latitudes réduites  beta1 au point de départ et beta2 au point d'arrivé
    if abs(lat1)==90:
        beta1=lat1
    else :
        beta1 = atan((1 - f) * tan(lat1))
    if abs(lat2)==90:
        beta2=lat2
    else :
        beta2 = atan((1 - f) * tan(lat2))
    # Calcul de la différence de longitude delta_lambda
    delta_lambda = long2 - long1
   
    #calcul de la différence de longitude sur la sphère auxiliaire par itération
        #approximation de la valeur initiale
    delta_u = delta_lambda
   
    # calcul des grandeurs suivantes
    sin_carre_sigma = (cos(beta2) * sin(delta_lambda))**2+ ((cos(beta1) * sin(beta2) - sin(beta1) * cos(beta2) * cos(delta_lambda)))**2
    Sin_sigma = sqrt(sin_carre_sigma)
    Cos_sigma = sin(beta1) * sin(beta2) + cos(beta1) * cos(beta2) * cos(delta_lambda)
    sigma = atan(Sin_sigma/Cos_sigma)
    Sin_alpha_e = cos(beta1) * cos(beta2) * sin(delta_lambda) / sin(sigma)
    alpha_e = asin(Sin_alpha_e)
    Cos2sigma_m = cos(sigma) - (2 * sin(beta1) * sin(beta2) / (cos(alpha_e)**2))
   
    # calcul de C Constante de Vincenty
    C = (f / 16) * (cos(alpha_e))**2 * (4 + f * (4 - 3 * (cos(alpha_e))**2))
   
    # calcul de la différence de longitude sur la sphère auxiliaire delta_u
    variation_lambda = delta_lambda

    delta_lambda = delta_u + (1 - C) * f * sin(alpha_e) * (sigma + C * sin(sigma) * \
                                                         (Cos2sigma_m + C * cos(sigma) * (-1 + 2 * (Cos2sigma_m)**2)))

    while variation_lambda - delta_lambda > 1.0e-9:
        
        sin_carre_sigma = (cos(beta2) * sin(delta_lambda))**2+ ((cos(beta1) * sin(beta2) - sin(beta1) * cos(beta2) * cos(delta_lambda)))**2
        Sin_sigma = sqrt(sin_carre_sigma)
        Cos_sigma = sin(beta1) * sin(beta2) + cos(beta1) * cos(beta2) * cos(delta_lambda)
        sigma = atan(Sin_sigma/Cos_sigma)
        Sin_alpha_e = cos(beta1) * cos(beta2) * sin(delta_lambda) / sin(sigma)
        alpha_e = asin(Sin_alpha_e)
        Cos2sigma_m = cos(sigma) - (2 * sin(beta1) * sin(beta2) / (cos(alpha_e)**2))

        C = (f / 16) * (cos(alpha_e))**2 * (4 + f * (4 - 3 * (cos(alpha_e))**2))

        variation_lambda = delta_lambda

        delta_lambda = delta_u + (1 - C) * f * sin(alpha_e) * (sigma + C * sin(sigma) * \
                                                         (Cos2sigma_m + C * cos(sigma) * (-1 + 2 * (Cos2sigma_m)**2)))
    #calcul de la latitude réduite de vertex beta0
    beta0 = acos(sin(alpha_e))
    # Calcul de la constante w_carre
    w_carre = (sin(beta0))**2 * (a * a - b * b) / (b * b)
    # Calcul des constantes de Vincenty A' et B'
    A = 1 + (w_carre / 16384) * (4096 + w_carre * (-768 + w_carre * (320 - 175 * w_carre)))

    B = (w_carre / 1024) * (256 + w_carre * (-128 + w_carre * (74 - 47 * w_carre)))
    # Calcul de delta_sigma
    delta_sigma = B * Sin_sigma * (Cos2sigma_m + (B / 4) * \
                                   (Cos_sigma * (2 * (Cos2sigma_m)**2 - 1) - \
                                    (B / 6) * Cos2sigma_m * (-3 + 4 * sin_carre_sigma) * \
                                    (-3 + 4 * (Cos2sigma_m)**2)))
    # Calcul de la distance géodésique s
    s = b * A * (sigma - delta_sigma)
    # Calcul de l'azimut directe alpha12
    alpha12 = atan2((cos(beta2) * sin(delta_lambda)), \
                    (cos(beta1) * sin(beta2) - sin(beta1) * cos(beta2) * cos(delta_lambda)))
    # Calcul de l'azimut inverse alpha21
    alpha21 = atan2((cos(beta1) * sin(delta_lambda)), \
                    (-sin(beta1) * cos(beta2) + cos(beta1) * sin(beta2) * cos(delta_lambda)))

    if (alpha12 < 0.0):
        alpha12 = alpha12 + 2 * pi
    if (alpha12 > 2 * pi):
        alpha12 = alpha12 - 2 * pi

    alpha21 = alpha21 + 2 * pi / 2.0
    if (alpha21 < 0.0):
        alpha21 = alpha21 + 2 * pi
    if (alpha21 > 2 * pi):
        alpha21 = alpha21 - 2 * pi

    alpha12 = alpha12 * 180 / pi
    alpha21 = alpha21 * 180 / pi
    return round(s), round(alpha12), round(alpha21)