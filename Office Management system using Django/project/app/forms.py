from django import forms
from .models import Ownership, Profile

class DateInput(forms.DateInput):
  pass

class OwnershipForm(forms.ModelForm):
  """
  show all Ownership model data details in table format
  """
  #amc_start = forms.DateField()
  class Meta:
    model = Ownership
    fields = ['customer_name', 'esn','model','cpcb_norms','visit','kva', 'amc_start', 'amc_end', 'contact_person','phone_num','mail_id', 'last_b', 'last_b_hour','last_c','last_c_hour', 'last_d', 'last_d_hour', 'last_coolant', 'last_coolant_hour', 'last_airfilter', 'last_airfilter_hour','last_battery', 'battery_type', 'last_battery_hour', 'controller_type', 'type_coolant', 'equ_model', 'equ_serial', 'last_fueltank_clean', 'last_radiator_clean', 'last_hose_replacement', 'last_plumber_block', 'last_healthcheck', 'last_fiveyearkit', 'recent_hour']
    widgets = {
'amc_start': DateInput(attrs={'type': 'date'}),
'amc_end': DateInput(attrs={'type': 'date'}),
'last_b': DateInput(attrs={'type': 'date'}),
'last_c': DateInput(attrs={'type': 'date'}),
'last_d': DateInput(attrs={'type': 'date'}),
'last_battery': DateInput(attrs={'type': 'date'}),
'last_coolant': DateInput(attrs={'type': 'date'}),
'last_airfilter': DateInput(attrs={'type': 'date'}), 'last_fueltank_clean': DateInput(attrs={'type': 'date'}), 'last_radiator_clean': DateInput(attrs={'type': 'date'}), 'last_hose_replacement': DateInput(attrs={'type': 'date'}), 'last_plumber_block': DateInput(attrs={'type': 'date'}), 'last_healthcheck': DateInput(attrs={'type': 'date'}), 'last_fiveyearkit': DateInput(attrs={'type': 'date'})
    }

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'
    
    
class DueForm(forms.ModelForm):
  class Meta:
    model = Ownership
    fields = ['remark_b',]