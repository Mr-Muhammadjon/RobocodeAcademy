from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
	path('', views.index, name='home'),
	path('post/<str:post_id>', views.detail, name='detail'),
	path('registration/', views.form_reg, name='form_reg'),

	# path('404/', views.handler404),
	# path('500/', views.handler500),
	path('kurs/<str:course_slug>/', views.course_detail, name='course_detail'),

]
