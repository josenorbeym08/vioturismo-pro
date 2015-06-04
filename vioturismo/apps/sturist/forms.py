from django import forms
from vioturismo.apps.sturist.models import producto
from vioturismo.apps.sturist.models import servicio
from vioturismo.apps.sturist.models import experiencia


class addProductForm(forms.ModelForm):
	class Meta:
		model   = producto
		exclude = {'status',}



"""
class addProductForm(forms.Form):
	nombre          = forms.CharField(widget=forms.TextInput())
	descripcion     = forms.CharField(widget=forms.TextInput())
	imagen          = forms.ImageField(required=False)
	contacto		= forms.CharField(required=True)
	
		

	def clean(self):
		return self.cleaned_data
"""



class addServicForm(forms.ModelForm):
	class Meta:
		model   = servicio
		exclude = {'status',}


"""
class addServicForm(forms.Form):
	nombre          = forms.CharField(widget=forms.TextInput())
	descripcion     = forms.CharField(widget=forms.TextInput())
	imagen          = forms.ImageField(required=False)
	contacto		= forms.CharField(required=True)
	precio 			= forms.CharField(required=True)
		

	def clean(self):
		return self.cleaned_data

"""


class addExperiencForm(forms.ModelForm):
	class Meta:
		model   = experiencia
		exclude = {'status',}


""""
class addExperiencForm(forms.Form):
	
	imagen          = forms.ImageField(required=False)
	nombre          = forms.CharField(widget=forms.TextInput())
	descripcion     = forms.CharField(widget=forms.Textarea())
		

	def clean(self):
		return self.cleaned_data

"""

