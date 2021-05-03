from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('loggedIn', views.logged_in),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('annotated/<str:key>', views.get_annotated),
    path('edit/<str:key>', views.edit),
    path('<str:key>', views.get_content),
]

