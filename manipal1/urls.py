from django.urls import path
from manipal1 import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('products/<int:productid>',views.products,name='products'),
    path('products/details/<int:uniqueproid>',views.details,name='details')
]