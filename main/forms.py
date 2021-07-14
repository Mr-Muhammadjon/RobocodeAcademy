from django import forms
from .models import Register, Contact


class RegisterForm(forms.ModelForm):

	class Meta:
		model = Register
		fields = '__all__'
		exclude = ['status','inner','outer', 'unknown']
		widgets = {
			'message':forms.TextInput(),
			'phone':forms.TextInput(attrs={'value':'+998','oninput':"this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\\..*)\\./g, '$1');"}),
			'age':forms.TextInput(attrs={'oninput':"this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\\..*)\\./g, '$1');"}),
		}

#fdjfdjfldjfdlsj

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = '__all__'
		# exclude = ('course',)
		widgets = {
			'message':forms.Textarea(attrs={'rows':4,'cols':50}),
			'phone':forms.TextInput(attrs={'value':'+998','oninput':"this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\\..*)\\./g, '$1');"}),
		}