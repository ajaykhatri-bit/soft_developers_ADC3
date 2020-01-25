from django import forms
#from .models import software
from software.models import software

class OForm(forms.ModelForm):
	class Meta:
		model = software
		fields = ('title', 'name', 'stw')