
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.home_page, name = 'home'),
    path('profile/', views.ProfilePage.as_view(), name='profile'),
    path('profile/update/<int:pk>', views.UpdateProfile.as_view(), name = 'profile_update'),
    path('ownership/', views.EngineData.as_view(), name = 'ownership'),
    path('total/ownership/', views.AdminEngineData.as_view(), name = 'admin_ownership'),
    
    path('select/owner/', views.AdminSelectOwner.as_view(), name = 'admin_select_owner'),
    
    path('create/customer/', views.CreateCustomer.as_view(), name= 'create'),
    path('update/<int:pk>/', views.UpdateCustomer.as_view(), name = 'update'),
    path('delete/<int:pk>/', views.DeleteCustomer.as_view(), name = 'delete'),
    path('due/status/', views.StatusDue.as_view(),
    name = 'due_status'),
    
    path('due/note/create/', views.FormNote.as_view(), name= 'create_note'),
    path('due/note/update/<int:pk>/', views.NoteDue.as_view(), name= 'note'),
    path('total/due/<str:user_name>/', views.AdminDueStatus.as_view(), name = 'admin_due_status'),
    #path('due/status/user/<str:username>', views.StatusDue.as_view(),
    #name = 'admin_due_status'),
    path('due/status/total', views.AdminTotalDueStatus.as_view(), name = 'admin_total_due_status'),
    
    path('Bcheck-due/customer/detail/<int:pk>', views.BDetailview.as_view(), name = 'list_detail'),
    path('Coolant-due/customer/detail/<int:pk>', views.CoolantDetailview.as_view(), name = 'coolant_list_detail'),
    path('Battery-due/customer/detail/<int:pk>', views.BatteryDetailview.as_view(), name = 'battery_list_detail'),
    path('Airfilter-due/customer/detail/<int:pk>', views.AirfilterDetailview.as_view(), name = 'airfilter_list_detail'),
    path('AMC-due/customer/detail/<int:pk>', views.AMCDetailview.as_view(), name = 'amc_list_detail'),
    path('Bcheck/due/sendmail/<int:pk>', views.sendmail, name = 'remind-customer'),
    path('coolant/due/sendmail/<int:pk>', views.sendmail_coolant, name = 'remind-customer-coolant'),
    path('battery/due/sendmail/<int:pk>', views.sendmail_battery, name = 'remind-customer-battery'),
    path('airfilter/due/sendmail/<int:pk>', views.sendmail_airfilter, name = 'remind-customer-airfilter'),
    path('amc/due/sendmail/<int:pk>', views.sendmail_amc, name = 'remind-customer-amc'),
    
    
    
    
    
    
    
    
    path('customer/response/<int:pk>/<str:due>/', views.CustomerResponse.as_view(), name = 'customer_response'),
    path('customer/response/list', views.CustomerResponseList.as_view(), name = 'customer_response_list'), 
    
    
]
