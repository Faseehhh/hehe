from django import forms

class IrisPredictionForm(forms.Form):
    cet = forms.FloatField(label='Cet')
    gpa = forms.FloatField(label='Gpa')
    strand = forms.CharField(max_length= 100, label='Strand')
# from .models import User

# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email', 'name', 'password']

#     def clean_confirm_password(self):
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError('Password do not match.')

#         return confirm_password