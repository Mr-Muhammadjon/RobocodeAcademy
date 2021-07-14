from .forms import RegisterForm
from django.contrib import messages
from .models import Register, Post, Course


def form_reg(request):
	footer_post = Post.objects.order_by('-id')[:3]
	form = RegisterForm()
	courses = Course.objects.all()
	context = {'form':form,'footer_post':footer_post, 'courses':courses}

	return context 

