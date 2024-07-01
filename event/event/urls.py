"""
URL configuration for event project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eventapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('customer_login/',views.login_cust,name='customer_login'),
    path('host_login/',views.login_host,name='host_login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/customer',views.register_cust,name='register_cust'),
    path('register/host',views.register_host,name='register_host'),
    path('create_event/',views.create_event,name='create_event'),
    path('ticket_information/<int:event_id>/', views.ticket_information, name='ticket_information'),

]
