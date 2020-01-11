from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User



class OurForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'password2')


	def save(self, commit=True):
		user = super(OurForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()

		return user
					

#from django import forms
#from .models import User


#class UserForm(forms.ModelForm):

    #class Meta:
        #model = User
        #fields = ('fullname','mobile','emp_code','position')
        #labels = {
            #'fullname':'Full Name',
            #'emp_code':'EMP. Code'
        #}

    #def __init__(self, *args, **kwargs):
        #super(register,self).__init__(*args, **kwargs)
        #self.fields['position'].empty_label = "Select"
        #self.fields['emp_code'].required = False

