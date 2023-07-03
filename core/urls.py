from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lead-generator/', views.lead_generator, name='lead-generator')
]
