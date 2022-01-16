from django.urls import path
from . import views

urlpatterns = [
  path('', views.home , name="home"),
  path('Contact', views.contact , name="contact"),
  path('Direct', views.direct , name="direct"),
  path('inverse', views.inverse, name="inverse"),
]