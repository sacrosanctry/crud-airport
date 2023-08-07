"""
URL configuration for cw_airport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from airport import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),

    path('passenger', views.passenger, name='passenger'),
    path('add_passenger', views.add_passenger, name='add_passenger'),
    path('edit_passenger/<int:id>', views.edit_passenger, name='edit_passenger'),
    path('update_passenger/<int:id>', views.update_passenger, name='update_passenger'),
    path('delete_passenger/<int:id>', views.delete_passenger, name='delete_passenger'),

    path('flight', views.flight, name='flight'),
    path('add_flight', views.add_flight, name='add_flight'),
    path('edit_flight/<int:id>', views.edit_flight, name='edit_flight'),
    path('update_flight/<int:id>', views.update_flight, name='update_flight'),
    path('delete_flight/<int:id>', views.delete_flight, name='delete_flight'),

    path('registration', views.registration, name='registration'),
    path('add_registration', views.add_registration, name='add_registration'),
    # path('edit_registration/<int:id>', views.edit_registration, name='edit_registration'),
    path('update_registration/<int:id>', views.update_registration, name='update_registration'),
    path('delete_registration/<int:id>', views.delete_registration, name='delete_registration'),

    path('luggage', views.luggage, name='luggage'),
    path('add_luggage', views.add_luggage, name='add_luggage'),
    # path('edit_luggage/<int:id>', views.edit_luggage, name='edit_luggage'),
    path('update_luggage/<int:id>', views.update_luggage, name='update_luggage'),
    path('delete_luggage/<int:id>', views.delete_luggage, name='delete_luggage'),

    path('interpol', views.interpol, name='interpol'),
    path('add_interpol', views.add_interpol, name='add_interpol'),
    # path('edit_interpol/<int:id>', views.edit_interpol, name='edit_interpol'),
    path('update_interpol/<int:id>', views.update_interpol, name='update_interpol'),
    path('delete_interpol/<int:id>', views.delete_interpol, name='delete_interpol'),
]
