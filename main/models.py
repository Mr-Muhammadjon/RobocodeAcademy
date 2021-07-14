from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Status(models.Model):
	STATUS = (
		('keladi','Keladi'),
		('kemedi','Kelmaydi'),
		('aniqmas','Aniq emas'),
		)
	status = models.CharField('Status', max_length=50, choices=STATUS)
	comment = models.TextField('Sababi/Qo\'shimcha xabar')

	def __str__(self):
		return self.status


class Register(models.Model):
	COURSES = (
		('lego','Bolalar uchun dasturlash'),
		('arduino', 'Arduino'),
		('web','Web dasturlash'),
		('grafika','Grafik dizayn',),
		('computer','Computer Science'),
		)
	name = models.CharField('Ismi-Familya', max_length=50)
	age = models.CharField('Yosh', max_length=50)
	phone = models.CharField('Telefon', max_length=15)
	course = models.CharField('Kurs', choices=COURSES, max_length=50)
	message = models.TextField("Qo'shimcha xabar")
	date = models.DateTimeField('Sanasi', auto_now_add=True)

	status = models.ForeignKey(
		Status,
		on_delete=models.CASCADE,
		related_name='customer_status',
		null=True,
		)
	inner = models.BooleanField('Keladi', default=False, blank=True, null=True)
	outer = models.BooleanField('Kemedi', default=False, blank=True, null=True)
	unknown = models.BooleanField('Aniq emas', default=False, blank=True, null=True)


	class Meta:
		verbose_name="A'zo bo'lgan"
		verbose_name_plural="A'zo bo'lganlar"

	def __str__(self):
		return self.name

class Contact(models.Model):
	name = models.CharField('Ismi-Familya', max_length=50)
	phone = models.CharField('Telefon', max_length=15)
	subject = models.CharField('Mavzu', max_length=250)
	message = models.TextField("Qo'shimcha xabar")

	class Meta:
		verbose_name="Aloqa"
		verbose_name_plural="Aloqalar"

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField('Nomi', max_length=50)
	body = RichTextField()
	youtube_link = models.CharField('You tube link', max_length=250)
	image = models.ImageField('Rasmi', upload_to='posters/')
	author = models.CharField('Muallif', max_length=50)
	published = models.DateTimeField('Sanasi', auto_now_add=True)

	class Meta:
		verbose_name="Maqola"
		verbose_name_plural="Maqolalar"

	def get_absolute_url(self):
		return reverse('main:detail', kwargs={'post_id':self.id})

	def __str__(self):
		return self.title


class Course(models.Model):
	# COURSES = (
	# 	('Bolalar uchun dasturlash','lego'),
	# 	('Arduino', 'arduino'),
	# 	('Web dasturlash','web'),
	# 	('Grafik dizayn','grafika'),
	# 	('Video montaj','video'),
	# 	)
	title = models.CharField('Kurs nomi', max_length=100)
	slug = models.SlugField('*', max_length=100, unique=True)
	short_desc = models.CharField('Qisqacha info', max_length=300)
	# course = models.CharField('Kurs', choices=COURSES, max_length=100)
	desc = RichTextField()
	image = models.ImageField('Kurs rasmi kichkina', upload_to='course_poster/')
	high_image = models.ImageField('Kurs rasmi asosiy', upload_to='course_poster/',blank=True, null=True)

	class Meta:
		verbose_name="Kurs"
		verbose_name_plural="Kurslar"
		ordering = ['-id']

	def get_absolute_url(self):
		return reverse('main:course_detail', kwargs={'course_slug':self.slug})


	def __str__(self):
		return self.title