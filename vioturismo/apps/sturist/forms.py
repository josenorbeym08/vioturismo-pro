from django import forms


class addProductForm(forms.Form):
	nombre          = forms.CharField(widget=forms.TextInput())
	descripcion     = forms.CharField(widget=forms.TextInput())
	imagen          = forms.ImageField(required=False)
	contacto		= forms.CharField(required=True)
		

	def clean(self):
		return self.cleaned_data