from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
	path('', views.CustomersListView.as_view(), name='customers'),
]