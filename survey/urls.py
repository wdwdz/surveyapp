from django.contrib import admin
from django.urls import path
from surveyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),

    path('logout/', views.logoutuser, name='logoutuser'),

    # Todos
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.createtodos, name='createtodos'),
    path('current/', views.currenttodos, name='currenttodos'),

]
