from django.urls import path,include
from . import views

urlpatterns = [
    
    #customer login
    path('accounts/', include('allauth.urls')),
    path('login',views.user_login,name='user_login'),
    path('signup',views.user_signup,name='user_signup'),
    path('customer_dashboard/',include('customer.urls')),

    #manager login
    path('manager_login',views.manager_login,name='manager_login'),
    path('manager_signup',views.manager_signup,name='manager_signup'),
    path('manager_dashboard/',include('manager.urls')),
    path('add-room/',include('manager.urls')),

]