from django.urls import path
from menu.views import *

app_name = 'menu'

urlpatterns = [
    path('<int:menu_id>/', view_menu, name='view_menu'),
]