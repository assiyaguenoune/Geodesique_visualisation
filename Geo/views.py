from math import pi
from django.shortcuts import render
from .direct import Direct
from .forms import directform 
from .forms import inverseform
from math import *
from .inverse import Inverse
# Create your views here.
def home(request):
     return render(request,'Home.html')
def contact(request):
    return render(request,'Contact.html')
def direct(request):
     return render(request,'direct.html')
def direct(request):
     if request.method=='POST':
          action=request.POST['action']
          if action=="Calculer":
               form=directform(request.POST)
               latitude,longitude=0,0
               if form.is_valid():
                    latitude=form.cleaned_data.get("latitude")
                    latitude=latitude*pi/180
                    longitude=form.cleaned_data.get("longitude")
                    longitude=longitude*pi/180
                    ellipsoid=form.cleaned_data.get("ellipsoid")
                    a=form.cleaned_data.get("grand")
                    b=form.cleaned_data.get("petit")
                    if a==0 or b==0:
                         if ellipsoid=="wgs":
                             a,b = 6378137,6356752.3142
                         elif ellipsoid == "grs":
                              a,b = 6378137,6356752.3141
                         elif ellipsoid == "clarke":
                              a,b =6378249.145,6356514.870
                         elif ellipsoid=="helmert1906":
                              a,b=6378200,6356818.169627891
                         elif ellipsoid=="clarke1866":
                              a,b=6378206.4,6356583.799998981
                    azimut=form.cleaned_data.get("azimut")
                    azimut=azimut*pi/180
                    s=form.cleaned_data.get("distance_geodesique")
                    phif,lamf,alphaf=Direct(latitude,longitude,azimut,s,a,b)
                    if lamf<0:
                        lam2=str(round(-lamf))+"° O"
                    else:
                        lam2=str(round(lamf))+"° E"
                    if phif<0:
                        phi2=str(round(-phif))+"° S"
                    else:
                        phi2=str(round(phif))+"° N"
                    alpha2=str(round(alphaf))+"°"
                    return render(request, 'direct.html',{'directform':directform , 'latitude2': phi2, 'longitude2':lam2 , 'alpha2':alpha2})
     else:
        form = directform()
        return render(request, 'direct.html', {'directform': form})
def visualisation(request):
    return render(request,'visualisation.html')
def inverse(request):
    if request.method == 'POST':
        form = inverseform(request.POST)
        action = request.POST['action']
        if action == "Calculer":
            latitude, longitude, latitude0, longitude0 = 0, 0, 0, 0
            if form.is_valid():
                ellipsoid = form.cleaned_data.get("ellipsoid")
                a = form.cleaned_data.get("grand")
                b = form.cleaned_data.get("petit")
                if a==0 or not a or b==0 or not b:
                    if ellipsoid == "wgs":
                        a,b = 6378137,6356752.3142
                    elif ellipsoid == "grs":
                        a,b = 6378137,6356752.3141
                    elif ellipsoid == "clarke":
                        a,b =  	6378249.145,6356514.870
                    elif ellipsoid=="helmert1906":
                        a,b=6378200,6356818.169627891
                    elif ellipsoid=="clarke1866":
                        a,b=6378206.4,6356583.799998981  
                latitude= form.cleaned_data.get("latitude")
                longitude= form.cleaned_data.get("longitude")
                latitude0= form.cleaned_data.get("latitude0")
                longitude0= form.cleaned_data.get("longitude0")
                s, az1, az2=Inverse(a, b, latitude*pi/180, longitude*pi/180, latitude0*pi/180, longitude0*pi/180)
                azdirect = str(az1)+"°"
                azinverse = str(az2)+"°"
                distance = str(abs(s))+"m"
                return render(request, 'inverse.html', {'form': form, 'az1': azdirect, 'az2': azinverse, 'distance': distance})
    else:
        form = inverseform()
        return render(request, 'inverse.html', {'form': form})