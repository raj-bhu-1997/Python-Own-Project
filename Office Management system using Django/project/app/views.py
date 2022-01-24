from django.shortcuts import render, redirect
from .models import Ownership, Profile
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OwnershipForm, ProfileForm, DueForm
from django.urls import reverse_lazy
from .mail import SendMail
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .filter import OrderFilter


# Create your views here.
def home_page(request):
  return render(request, 'home.html')

class ProfilePage(View, LoginRequiredMixin):
  def get(self, request, *args, **kwargs):
    user = request.user
    print(user)
    profile = Profile.objects.get(user_name = user)
    #user = profile.user_name
    context = {'user_profile': profile}
    return render(request, 'profile_page.html', context)
    
class UpdateProfile(UpdateView, LoginRequiredMixin):
  model = Profile
  fields = '__all__'
  success_url = reverse_lazy('profile')
  template_name = 'update_user.html'
  
  
class EngineData(View, LoginRequiredMixin):
  """
  view class to show ownership table
  """
  def get(self, request, *args, **kwargs):
    author = request.user
    owner = Ownership.objects.filter(author = author)
    user_detail = User.objects.all()
    context = { 'owner': owner, 'user': user_detail}
    return render(request, 'table.html', context)
 # def post(self, request, *args, **kwargs):

class AdminEngineData(View, LoginRequiredMixin):
  def get(self, request, *args, **kwargs):
    total = Ownership.objects.all()
    context = {'total' : total}
    return render(request, 'admin_table.html', context)

class AdminTotalDueStatus(View, LoginRequiredMixin):
  def get(self, request, *args, **kwargs):
    total = Ownership.objects.all()
    total_engine = len(total)
    obj = Ownership()
    total_b = len(obj.is_bcheck_due(total))
    total_battery = len(obj.is_battery_due(total))
    total_coolant = len(obj.is_coolant_due(total))
    total_airfilter = len(obj.is_airfilter_due(total))
    total_amc = len(obj.is_amc_due(total))
    orderfilter = OrderFilter(request.GET, queryset = total)
    context = { 'b': total_b,'battery': total_battery, 'coolant':total_coolant, 'airfilter':total_airfilter, 'total':total_engine, 'amc': total_amc, 'order': orderfilter}
    print('haiikkkiii')
    return render(request, 'total_due.html', context)

class AdminSelectOwner(View, LoginRequiredMixin):
  def get(self, request, *args, **kwargs):
    user_detail = User.objects.all()
    name1 = 'rajesh'
    context = {'user': user_detail }
    return render(request, 'user_list.html', context)

class CreateCustomer(CreateView, LoginRequiredMixin):
  model = Ownership
  form_class = OwnershipForm
  template_name = 'create_customer.html'
  success_url = reverse_lazy('ownership')
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
    
    
class UpdateCustomer(UpdateView, LoginRequiredMixin):
  model = Ownership
  fields = ['customer_name', 'esn','model','cpcb_norms','visit','kva', 'amc_start', 'amc_end', 'contact_person','phone_num','mail_id', 'last_b', 'last_b_hour','last_c','last_c_hour', 'last_d', 'last_d_hour', 'last_coolant', 'last_coolant_hour', 'last_airfilter', 'last_airfilter_hour','last_battery', 'battery_type', 'last_battery_hour', 'controller_type', 'type_coolant', 'equ_model', 'equ_serial', 'last_fueltank_clean', 'last_radiator_clean', 'last_hose_replacement', 'last_plumber_block', 'last_healthcheck', 'last_fiveyearkit', 'recent_hour']
  
  template_name = 'update_customer.html'
  success_url = reverse_lazy('ownership')

class DeleteCustomer(DeleteView, LoginRequiredMixin):
  model = Ownership
  template_name = 'delete_customer.html'
  success_url = reverse_lazy('ownership')
  
class StatusDue(View, LoginRequiredMixin):
  """
  this class is use to filter the maintenance due 
  """
  def get(self, request, *args, **kwargs):
    user = request.user
    obj = Ownership.objects.filter(author = user)
    B = Ownership()
    B_check_due = B.is_bcheck_due(obj)
    num_of_b = len(B_check_due)
    coolant_due_customer = B.is_coolant_due(obj)
    num_of_coolant = len(coolant_due_customer)
    battery_due_customer = B.is_battery_due(obj)
    num_of_battery = len(battery_due_customer)
    airfilter_due_customer = B.is_airfilter_due(obj)
    num_of_airfilter = len(airfilter_due_customer)
    amcdue_customer = B.is_amc_due(obj)
    num_of_amcdue = len(amcdue_customer)
    
    context = {'B_due': B_check_due, 'coolant_due': coolant_due_customer, 'total_b': num_of_b, 'total_coolant': num_of_coolant, 'battery_due': battery_due_customer, 'total_battery':num_of_battery, 'airfilter_due': airfilter_due_customer, 'total_airfilter': num_of_airfilter, 'amc_due': amcdue_customer, 'total_amcdue': num_of_amcdue}
    
    return render(request, 'due.html', context)
    
    
class FormNote(CreateView, LoginRequiredMixin):
  model = Ownership
  form_class = DueForm
  template_name = 'note_form.html'
  success_url = reverse_lazy('due_status')
  
  
class NoteDue(UpdateView, LoginRequiredMixin):
  model = Ownership
  fields = ['remark_b',]
  success_url = reverse_lazy('due_status')
  template_name = 'note.html'

class AdminDueStatus(View, LoginRequiredMixin):
  def get(self, request, user_name = None, *args, **kwargs):
    user = str(user_name)
    B = Ownership()
    obj = Ownership.objects.filter(author__username = user)
    B_check_due = B.is_bcheck_due(obj)
    num_of_b = len(B_check_due)
    coolant_due_customer = B.is_coolant_due(obj)
    num_of_coolant = len(coolant_due_customer)
    battery_due_customer = B.is_battery_due(obj)
    num_of_battery = len(battery_due_customer)
    airfilter_due_customer = B.is_airfilter_due(obj)
    num_of_airfilter = len(airfilter_due_customer)
    amcdue_customer = B.is_amc_due(obj)
    num_of_amcdue = len(amcdue_customer)
    
    context = {'B_due': B_check_due, 'coolant_due': coolant_due_customer, 'total_b': num_of_b, 'total_coolant': num_of_coolant, 'battery_due': battery_due_customer, 'total_battery':num_of_battery, 'airfilter_due': airfilter_due_customer, 'total_airfilter': num_of_airfilter, 'amc_due': amcdue_customer, 'total_amcdue': num_of_amcdue}
    
    return render(request, 'due.html', context)
    
# show individual B check customer list
class BDetailview(View, LoginRequiredMixin):
  """
  when click the button this class shows the details of Battery  due customer 
  """
  def get(self, request, pk, *args, **kwargs):
    author = request.user
    list_detail = Ownership.objects.filter(pk = pk)
    context = {'customer_detail': list_detail}
    return render(request, 'bcheck_detail.html', context)
    
# show individual coolant customer list    
class CoolantDetailview(View, LoginRequiredMixin):
  """
  when click the button this class shows the details of individual coolant due customer
  """
  def get(self, request, pk, *args, **kwargs):
    author = request.user
    list_detail = Ownership.objects.filter(pk = pk)
    context = {'customer_detail': list_detail}
    return render(request, 'coolant_detail.html', context)

# show individual Battery due customer
class BatteryDetailview(View, LoginRequiredMixin):
  """
  when click the button this class shows the details of individual battery due customer
  """
  def get(self, request, pk, *args, **kwargs):
    author = request.user
    list_detail = Ownership.objects.filter(pk = pk)
    context = {'customer_detail': list_detail}
    return render(request, 'battery_detail.html', context)
   
   
# shoe individual air filter due customer 
class AirfilterDetailview(View, LoginRequiredMixin):
  """
  when click the button this class shows the details of individual Airfilter due  customer
  """
  def get(self, request, pk, *args, **kwargs):
    author = request.user
    list_detail = Ownership.objects.filter(pk = pk)
    context = {'customer_detail': list_detail}
    return render(request, 'airfilter_detail.html', context)
    
class AMCDetailview(View, LoginRequiredMixin):
  """
  when click the button this class shows the details of individual Airfilter due  customer
  """
  def get(self, request, pk, *args, **kwargs):
    author = request.user
    list_detail = Ownership.objects.filter(pk = pk)
    context = {'customer_detail': list_detail}
    return render(request, 'amc_detail.html', context)
    
    
#send mail and message to customer
def sendmail(request, pk):
  send_object = Ownership.objects.filter(pk= pk)
  user = request.user
  for ele in send_object:
    obj = SendMail(ele)
    result = obj.send_bcheck(user)
    messages.info(request, result)
    return redirect('list_detail', pk= pk)

# send remainder mail to customer if coolant due
def sendmail_coolant(request, pk):
  send_object = Ownership.objects.filter(pk = pk)
  for ele in send_object:
    obj = SendMail(ele)
    result = obj.send_coolant()
    messages.info(request, result)
  return redirect('coolant_list_detail', pk= pk)
  
# send remainder mail to customer if battery due
def sendmail_battery(request, pk):
  send_object = Ownership.objects.filter(pk = pk)
  for ele in send_object:
    obj = SendMail(ele)
    result = obj.send_battery()
    messages.info(request, result)
  return redirect('battery_list_detail', pk = pk)
  
# send remainder mail to customer if Airfilter due
def sendmail_airfilter(request, pk):
  send_object = Ownership.objects.filter(pk = pk)
  for ele in send_object:
    obj = SendMail(ele)
    result = obj.send_airfilter()
    messages.info(request, result)
  return redirect('airfilter_list_detail', pk = pk)
  
# send remainder mail to customer if AMC due 

def sendmail_amc(request, pk):
  send_object = Ownership.objects.filter(pk = pk)
  for ele in send_object:
    obj = SendMail(ele)
    result = obj.send_amc()
    messages.info(request, result)
  return redirect('amc_list_detail', pk = pk)
  


class CustomerResponse(View, LoginRequiredMixin):
  def get(self, request, pk, due, *args, **kwargs):
    customer = Ownership()
    customer.set_customer_response(pk)
    
  
class CustomerResponseList(View, LoginRequiredMixin):
  def get(self, request, *args, **kwargs):
    customer_list = Ownership.objects.filter(customer_response = True)
    context = {'customer_list': customer_list }
    return render(request, 'customer_response_list.html', context)