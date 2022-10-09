from . import views
from django.urls import path

urlpatterns = [

    path ('',views.home,name='index.html'),
    # path('add/',views.addition,name='addition')

    ]