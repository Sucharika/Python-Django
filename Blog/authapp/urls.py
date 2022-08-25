from django.urls import path
from authapp import views

urlpatterns = [
    path('Register',views.register, name ='Register'),
    path('Login',views.sign_in, name ='Login'),
    path('Logout',views.sign_out, name ='Logout')

   
]