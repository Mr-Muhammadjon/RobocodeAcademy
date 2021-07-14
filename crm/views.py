from django.shortcuts import render
from django.views.generic import ListView
from main.models import Register
# Create your views here.


class CustomersListView(ListView):
	model = Register
	template_name = 'list.html'