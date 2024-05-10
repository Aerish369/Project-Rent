from django.urls import path
from . import views

urlpatterns = [
   path('test/', views.test, name="test"),
   path('login/', views.loginUser, name="login-page"),
   path('logout/', views.logoutUser, name="logout-page"),

]