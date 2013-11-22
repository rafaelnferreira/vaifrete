import djangoforms
from django import forms
from models import *

Vehicles = (
         ('Moto','Moto'),
         ('Bicicleta','Bicicleta'),
         ('Helicoptero','Helicoptero'),
         ('Van','Van'),
        )

UserTypes = (
		('Entregador','Entregador'),
		('Usuario','Usuario'),
	)

class AppUserForm(djangoforms.ModelForm):
  real_user = forms.EmailField(label='Usuario',widget=forms.TextInput(attrs={'size':'50','maxlength':'50'} ))
  #name = forms.CharField(label='Identificacao',widget=forms.TextInput(attrs={'size':'50','maxlength':'50'} ))
  vehicle = forms.TypedChoiceField(choices=Vehicles, initial='Moto')
  user_type = forms.TypedChoiceField(choices=UserTypes, initial='Usuario')
  class Meta:
    model = AppUser
    exclude = ['last_status', 'last_position', 'user_email']

class DeliverFeeForm(djangoforms.ModelForm):
	source_address = forms.CharField(label='Origem',widget=forms.TextInput(attrs={'size':'50','maxlength':'50'} ))
	destination_address = forms.CharField(label='Destino',widget=forms.TextInput(attrs={'size':'50','maxlength':'50'} ))
	item = forms.CharField(label='Item',widget=forms.Textarea)
	class Meta:
		model = DeliverFee
		exclude = ['dest_lng','dest_lat', 'source_lat', 'source_lng','request_user', 'item', 'request_date_time', 'closed', 'state']