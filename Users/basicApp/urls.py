from django.urls import path,include
from basicApp import views

app_name='basicApp'

urlpatterns=[

    path('register/',views.register,name="register"),
    path('userlogin/',views.user_login,name="login")
]