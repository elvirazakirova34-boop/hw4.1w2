from django.urls import path
from .views import index, contacts

app_name = 'nurai'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
]
