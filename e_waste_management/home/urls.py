from django.urls import path
#from home.views import About,Index
from . import views
urlpatterns = [
    path('',views.Index, name = "index"),
    path('about/',views.about, name = "about"),
    path('contact/',views.contact, name = "contact"),
]

3