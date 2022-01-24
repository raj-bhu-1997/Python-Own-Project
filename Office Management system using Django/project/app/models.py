from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import datetime
from django.contrib.auth.models import User

# class to save the ESN model, customer name etc
class Ownership(models.Model):
  """
  This class save the esn, model, customer name, last B check, last coolant and last air filter data
  """
  author = models.ForeignKey(User, on_delete = models.CASCADE)
  cpcb_norm = [('C1', 'CPCB1'), ('C2', 'CPCB2')]
  battery_make = [('CUMMINS', 'CUMMINS'), ('OTHER', 'OTHER')]
  coolant_choice = [('DCA4', 'DCA4'), ('DCA2', 'DCA2'), ('OTHER', 'OTHER'), ('WATER', 'WATER')]
  controller_detail = [('Cluster', 'Cluster'), ('ECP', 'ECP'), ('ECPG', 'ECPG'), ('POWERCOM', 'POWERCOM'), ('PCC0301', 'PCC0301'), ('PCC1301', 'PCC1301'), ('PCC1302', 'PCC1302'), ('PCC2100', 'PCC2100'), ('PCC3100', 'PCC3100'), ('PCC3201', 'PCC3201'), ('PCC3.3', 'PCC3.3'), ('OTHER', 'OTHER')]
  
  # define field here
  customer_name = models.CharField(max_length = 100)
  esn = models.DecimalField(max_digits = 10, decimal_places = 0, null = True)
  model = models.CharField(max_length = 10, null = True)
  cpcb_norms = models.CharField(choices = cpcb_norm, max_length = 2, default = 'C1')
  visit = models.IntegerField(null = True)
  kva = models.IntegerField(null = True)
  amc_start = models.DateField(null = True)
  amc_end = models.DateField(null = True)
  
  contact_person = models.CharField(max_length = 20, null = True)
  phone_num= models.CharField(max_length= 10, null = True)
  mail_id = models.EmailField(max_length = 50, null = True)
  
  
  last_b = models.DateField(null = True)
  last_b_hour = models.IntegerField(blank = True, null = True)
  last_c = models.DateField(null = True, blank = True)
  last_c_hour = models.IntegerField(null = True, blank = True)
  last_d = models.DateField(null = True, blank = True)
  last_d_hour = models.IntegerField(null = True, blank = True)
  last_coolant = models.DateField(null = True)
  last_coolant_hour = models.IntegerField(null= True, blank= True)
  last_airfilter = models.DateField(null = True)
  last_airfilter_hour = models.IntegerField(null=True, blank = True)
  last_battery = models.DateField(null = True)
  battery_type = models.CharField(choices = battery_make, max_length = 7, default = 'CUMMINS')
  last_battery_hour = models.IntegerField(null= True, blank = True)
  
  genset_type = models.CharField(max_length = 20, null = True, blank = True)
  controller_type = models.CharField(choices = controller_detail, max_length =10, blank = True, null = True, default = None)
  
  type_coolant = models.CharField(choices = coolant_choice, max_length = 6, default = None, blank = True, null = True)
  equ_model = models.CharField(max_length = 10, blank = True, null = True)
  equ_serial = models.CharField(max_length = 10, blank = True, null = True)
  last_fueltank_clean = models.DateField(null = True, blank = True)
  last_radiator_clean = models.DateField(null = True, blank = True)
  last_hose_replacement = models.DateField(null = True, blank = True)
  last_plumber_block = models.DateField(null = True, blank = True)
  last_healthcheck = models.DateField(null = True, blank = True)
  last_fiveyearkit = models.DateField(null = True, blank = True)
  recent_hour = models.IntegerField(blank = True, null = True)
  
  # reminder count for customer

  reminder_count_b = models.IntegerField(blank = True, null = True)
  reminder_count_coolant = models.IntegerField(blank = True, null = True)
  reminder_count_battery = models.IntegerField(blank = True, null = True)
  reminder_count_airfilter = models.IntegerField(blank = True, null = True)
  reminder_count_amcdue = models.IntegerField(blank = True, null = True)
  
  # remark what is the reason for due

  remark_b = models.CharField(max_length = 150, blank = True, null = True)
  remark_coolant = models.CharField(max_length = 150, blank = True, null = True)
  remark_battery = models.CharField(max_length = 150, blank = True, null = True)
  remark_airfilter = models.CharField(max_length = 150, blank = True, null = True)
  remark_amcdue = models.CharField(max_length = 150, blank = True, null = True)
  
  # customer response
  customer_response = models.BooleanField(default = False)
  
  def input_validator(self, phone):
    if not phone.isdigit() and len(phone) == 10:
      raise ValueError('please enter the valid format')
  
  
  
  def __str__(self):
    return self.customer_name
    
  #check wheather B check due or not  
  def is_bcheck_due(self, b_obj):
    b_check_customer = b_obj
    b_check_list = []
    for customer in b_check_customer:
      if customer.last_b:
        diff_month = round((datetime.date.today() - customer.last_b).days / 30, 0)
        if customer.cpcb_norms == 'C1' and diff_month >= 6:
          b_check_list.append(customer)
        elif customer.cpcb_norms == 'C2' and diff_month >= 12:
          b_check_list.append(customer)
        else:
          customer.reminder_count_b = 0
          customer.remark_b = ''
    return b_check_list
 
 # check whether coolant due or not
  def is_coolant_due(self, coolant_obj):
    coolant_customer = coolant_obj
    coolant_due_customer = []
    for ele in coolant_customer:
      if ele.last_airfilter:
        diff_month = round((datetime.date.today() - ele.last_airfilter).days /30, 0)
        if diff_month > 24:
          coolant_due_customer.append(ele)
        else:
          ele.reminder_count_coolant = 0
          ele.remark_coolant = ''
    return coolant_due_customer
# check wheather battery due or not
  def is_battery_due(self, battery_obj):
    battery_customer = battery_obj
    battery_due_customer = []
    for ele in battery_customer:
      if ele.last_battery:
        if round((datetime.date.today() - ele.last_battery).days /30 , 0) >24:
          battery_due_customer.append(ele)
        else:
          ele.reminder_count_battery = 0
          ele.remark_airfilter = ''
    return battery_due_customer

# check wheather the air filter due or not
  def is_airfilter_due(self, airfilter_obj):
    airfilter_customer = airfilter_obj
    airfilter_due_customer = []
    for ele in airfilter_customer:
      if ele.last_airfilter:
        airfilter_diff = round((datetime.date.today()- ele.last_airfilter).days /30, 0)
        if airfilter_diff > 12:
          airfilter_due_customer.append(ele)
        else:
          ele.reminder_count_airfilter = 0
          ele.remark_airfilter = ''
    return airfilter_due_customer
    
  
  def is_amc_due(self, amc_obj):
    amc_due = amc_obj
    amc_due_customer = []
    for ele in amc_due:
      if ele.amc_end:
        due_diff = round((ele.amc_end - datetime.date.today()).days /30, 0)
        if due_diff <= 2:
          amc_due_customer.append(ele)
        else:
          ele.reminder_count_amcdue = 0
          ele.remark_amcdue = ''
    return amc_due_customer
  
  def set_customer_response(self, pk):
    customer = Ownership.objects.get(pk = pk)
    customer.customer_response = True
    

    


class Profile(models.Model):
  user_name = models.OneToOneField(User, on_delete= models.CASCADE, related_name = 'profile', verbose_name = 'user', null= True)
  #owner = models.ForeignKey(Ownership, on_delete = models.CASCADE)
  emp_code = models.IntegerField(null = True, blank = True)
  user_mail = models.EmailField(max_length= 50, null= True)
  user_mail_password = models.CharField(max_length=30, null = True)
  manager_mail = models.EmailField(max_length= 50, null = True)
  advicer_mail = models.EmailField(max_length= 50, null = True)
  amc_department_mail = models.EmailField(max_length= 50, null = True)


@receiver(post_save, sender= User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user_name = instance)
    print('user profile created')

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()