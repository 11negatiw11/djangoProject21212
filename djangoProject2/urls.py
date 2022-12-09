from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login',views.MainLoginView.as_view()),
    path('Aboutes', views.via),
    path('home', views.home),
    path('forfrfrf', views.fof),
    path('fofr', views.fofr),
    path('konez', views.konez),

]
