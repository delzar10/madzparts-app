from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>', views.detail, name='detail')
    #    path('<int:user_id>', views.detail, 'detail')
]
