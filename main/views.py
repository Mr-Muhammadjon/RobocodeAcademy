from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from .forms import RegisterForm,ContactForm

# from django.shortcuts import render_to_response
# from django.template import RequestContext


import telebot
TOKEN = '1268682258:AAHDv2-qOy_nPYUFCKuuboygvViNSoe-LVg'
bot = telebot.TeleBot(TOKEN)
# g_id = -1001383923135
g_id = 668618297

# Create your views here.

def index(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			contact_form.save()
			u = Contact.objects.last()
			bot.send_message(g_id, f"Saytdan xabar bor:\nIsmi: {u.name}\nTelefon: {u.phone}\n Mavzu: {u.subject}\nXabar: {u.message}")
			messages.add_message(request, messages.SUCCESS , "Qabul qilindi ! \n Tez orada siz bilan bog'lanamiz.")
		else:
			messages.add_message(request, messages.WARNING , "Xatolik ! \n Iltimos qaytadan urinib ko'ring")
	else:
		contact_form = ContactForm()
	# if request.method == 'POST':
	# 	name = request.POST.get('name', None)
	# 	phone = request.POST.get('phone', None)
	# 	subject = request.POST.get('subject', None)
	# 	message = request.POST.get('message', None)
	# 	if name and phone and subject and message:
	# 		Contact.objects.create(
	# 			name=name,phone=phone,subject=subject,message=message)
	# 		bot.send_message(g_id, f"Saytdan xabar bor:\nIsmi: {name}\nMavzu: {subject}\nTelefon: {phone}\nXabar: {message}")
	# 		messages.add_message(request, messages.SUCCESS , "Qabul qilindi ! \n Tez orada siz bilan bog'lanamiz.")
	# 	else:
	# 		messages.add_message(request, messages.WARNING , "Xatolik ! \n Iltimos qaytadan urinib ko'ring")
	posts = Post.objects.all().order_by('-id')[:3]
	courses = Course.objects.all()
	context = {
		# 'form':form,
		'posts':posts,
		'courses':courses,
		'contact_form':contact_form,
	}
	return render(request, 'index.html', context)

def detail(request, post_id):
	more = Post.objects.all().order_by('-id')[:6]
	post = Post.objects.get(id=post_id)
	return render(request, 'post.html', {'post':post, 'more':more})


def course_detail(request, course_slug):

	course = Course.objects.get(slug=course_slug)
	return render(request, 'courses.html', {'course':course})




def form_reg(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			u = Register.objects.last()
			bot.send_message(g_id, f"A'zo bo'lganlar bor:\nIsmi: {u.name}\nYoshi: {u.age}\nKursi: #{u.course}\nTelefon: {u.phone}\nXabar: {u.message}")
			messages.add_message(request, messages.SUCCESS , "Qabul qilindi ! \n Tez orada siz bilan bog'lanamiz.")
		else:
			messages.add_message(request, messages.WARNING , "Xatolik ! \n Iltimos qaytadan urinib ko'ring")

	else:
		form = RegisterForm()


	return HttpResponseRedirect('/') 


# def handler404(request, exception=None):   
#     return render(request,'404.html')

# def handler500(request, exception=None):   
#     return render(request,'404.html')
