from django.urls import path
from.import views

app_name='schoolapp'

urlpatterns = [

path("",views.main,name="main"),
path('reg/',views.reg,name='reg'),
path('reg2/',views.reg2,name='reg2'),
path('logout/',views.logout,name="logout"),
path('login/',views.login,name="login"),



]