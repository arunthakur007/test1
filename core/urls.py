from django.urls import path
from core import views


urlpatterns = [
    path('aboutme/', views.aboutme),
    path('contactme/', views.contactme),
    path('readme/',views.readme)
]