from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('HomePage/', views.HomePage,name='HomePage'),
    path('LoginPage/', views.LoginPage,name='LoginPage'),
    path('registerPage/', views.registerPage,name='registerPage'),
    path('Translator/', views.Translator,name='Translator'),
    path('Translator/logout', views.logout, name='logout'),
    path('About_us',views.About_us, name='About_us'),
    path('services',views.services, name='services'),
    path('Shedule',views.Shedule, name='Shedule'),
    path('LearnHomePage',views.LearnHomePage, name='LearnHomePage'),
    path('Books', views.Books, name='Books'),
]
