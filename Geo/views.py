from math import pi
from django.shortcuts import render
from .direct import Direct
from .forms import directform
from math import *
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
                    azimut=form.cleaned_data.get("azimut")
                    azimut=azimut*pi/180
                    s=form.cleaned_data.get("distance_geodesique")
                    phif,lamf,alphaf=Direct(latitude,longitude,azimut,s,a,b)
                    if lamf<0:
                         n=int(-lamf)
                         m0=(lamf-n)*60
                         m=int(m0)
                         p=int((m0-m)*60)
                         lam2=str(n)+"° "+str(m)+"' "+str(p)+"'' "+" O"
                    else:
                         n=int(lamf)
                         m0=(lamf-n)*60
                         m=int(m0)
                         p=int((m0-m)*60)
                         lam2=str(n)+"° "+str(m)+"' "+str(p)+"'' "+" E"
                    if phif<0:
                         n=int(phif)
                         m0=(phif-n)*60
                         m=int(m0)
                         p=int((m0-m)*60)
                         phi2=str(n)+"° "+str(m)+"' "+str(p)+"'' "+" S"
                    else:
                         n=int(phif)
                         m0=(phif-n)*60
                         m=int(m0)
                         p=int((m0-m)*60)
                         phi2=str(n)+"° "+str(m)+"' "+str(p)+"'' "+" N"
                    alpha2=str(round(alphaf))+"°"
                    return render(request, 'direct.html',{'directform':directform , 'latitude2': phi2, 'longitude2':lam2 , 'alpha2':alpha2})
     else:
        form = directform()
        return render(request, 'direct.html', {'directform': form})