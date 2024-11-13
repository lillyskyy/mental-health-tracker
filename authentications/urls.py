from django.urls import path
from .views import login, register
from authentications.views import logout

app_name = 'authentications'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]