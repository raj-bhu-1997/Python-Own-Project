
import datetime
from django.core.mail import send_mail
from project import settings
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMessage, EmailMultiAlternatives
from pathlib import Path
from .models import Profile
from django.template import Template, Context
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



class SendMail:
  """
  this class set the mail server settings and send mail to customer 
  """
  def __init__(self, customer_object):
    self.company_name = customer_object.customer_name
    self.person_name = customer_object.contact_person
    self.phone_no = customer_object.phone_num
    self.esn = customer_object.esn
    self.model = customer_object.model
    self.kva = customer_object.kva
    self.mail_id = customer_object.mail_id
    self.last_b = customer_object.last_b
    self.last_b_hour = customer_object.last_b_hour
    self.last_coolant = customer_object.last_coolant
    self.last_coolant_hour = customer_object.last_coolant_hour
    self.last_airfilter = customer_object.last_airfilter
    self.last_airfilter_hour = customer_object.last_airfilter_hour
    self.last_battery = customer_object.last_battery
    self.last_battery_hour = customer_object.last_battery_hour
    self.amc_start = customer_object.amc_start
    self.amc_end = customer_object.amc_end
    
    
    self.author = customer_object.author
    self.pk = customer_object.pk
    
    self.context_data = {'company_name': self.company_name, 'contact_person': self.person_name, 'phone_num':self.phone_no, 'esn': self.esn, 'model':self.model, 'kva':self.kva, 'last_b': self.last_b, 'last_b_hour': self.last_b_hour,'last_coolant':self.last_coolant, 'last_coolant_hour': self.last_coolant_hour,'last_airfilter':self.last_airfilter, 'last_airfilter_hour': self.last_airfilter_hour, 'last_battery': self.last_battery, 'last_battery_hour': self.last_battery_hour, 'amc_start':self.amc_start, 'amc_end': self.amc_end, 'pk': self.pk }
   
    
  def send_bcheck(self, user):
    html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">


  
  <title>Document</title>
  <style type="text/css" media="all">
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
body{
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  
}
.main{
 
}
.main .heading{
  display: flex;
  text-align: center;
  width: 100%;
  background-color: #ff1a1a;
}
.main .heading h4{
  color: white;
  font-size: 20px;
  margin-left: 30px;
 
}
.main .heading img{
  width: 40%;
  height: 30%;
  margin-top: 5px;
  margin-right: 15px;
  margin-bottom:5px;
}

.main .image img{
  width: 80%;
  margin: 0 10% 0 10%;
}
.table h5{
  text-align: center;
  font-size: 15px;
}
.table table{
  width: 100%;
}

.table table tbody tr td{
  padding: 8px 0px 8px 10px;
}

.body{
  padding-left: 10px;
  padding-right: 10px;
}

.body a{
    display: block;
    width: 115px;
    height: 25px;
    background: #4d4dff;
    padding: 10px;
    margin-top: 70px;
    text-align: center;
    border-radius: 5px;
    color: white;
    font-weight: bold;
    line-height: 25px;
    text-decoration: none;
}

  </style>
</head>
<body>
  <div class="main">
    <div class="heading">
      <h4>Greetings from JN machineries</h4>
      <img src="cid:image1" alt="">
    </div>
    <div class="image">
     <img src="cid:image2" alt=""> 
    </div> 
    <div class="table">
      <h5>Dg set - general maintenance - due alert</h5>
      <table>
        <tbody>
             <tr>
              <td>ESN</td>
              <td>{{ esn }}</td>
            </tr>
            <tr>
              <td>MODEL</td>
              <td>{{ model }}</td>
            </tr>
            <tr>
              <td>KVA</td>
              <td>{{ kva }}</td>
            </tr>
            
            <tr>
              <td>LAST B CHECK DATE</td>
              <td>{{ last_b }}</td>
            </tr>
            <tr>
              <td>LAST B CHECK HOURS</td>
              <td>{{ last_b_hour }}</td>
            </tr>
        </tbody>
      </table>
      <h5 style="color:red;">B check due</h5>
    </div>
    <div class="body">
     <h4 class="mt-5">Dear sir/mam,</h4>
        <p class="mt-2"> we observe <b style="color:red;">B check</b> due in the above mentioned ESN <b style="color:blue;">{{ esn }}</b> on <b style="color:blue;">{{ last_b }}</b>. So please do the B check as soon as possible for trouble free operation.. </p>
           <p>Any clarification  please feel free to contact us on 044-424244444 after office hours please contact phone number 9445037117 our executive will speak with you..</p>
        <h5>If you what quote please click the below button </h5>
        <a class="button">Request Quote</a>
    </div>
    
    <div class="footer">
      
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>


</body>
</html>
    '''
    self.context_data['due'] = 'bcheck'
    sub = 'B check due alert'
    user = user
    res = self.send_mail(html, self.context_data, sub, user)
    return res
    
    
  def send_coolant(self):
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style type="text/css" media="all">
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
body{
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  
}
.main{
  
}
.main .heading{
  display: flex;
  justify-content: center;
  width: 100%;
  background-color: #ff1a1a;
}
.main .heading h4{
  color: white;
  font-size: 25px;
  text-align: center;
}
.main .heading img{
  width: 40%;
  height: 30%;
  margin-top: 5px;
  margin-right: 15px;
  margin-bottom: 5px;
}

.main .image img{
  width: 80%;
  margin: 0 10% 0 10%;
}
.table h5{
  text-align: center;
  font-size: 15px;
}
.table table{
  width: 100%;
}

.table table tbody tr td{
  padding: 8px 0px 8px 10px;
}

.body{
  padding-left: 10px;
  padding-right: 10px;
}
.body a{
    display: block;
    width: 115px;
    height: 25px;
    background: #4d4dff;
    padding: 10px;
    margin-top: 70px;
    text-align: center;
    border-radius: 5px;
    color: white;
    font-weight: bold;
    line-height: 25px;
    text-decoration: none;
}


  </style>
</head>
<body>
  <div class="main">
    <div class="heading">
      <h4>Greetings from JN machineries</h4>
      <img src="cid:image" alt="">
    </div>
    <div class="image">
     <img src="cid:image1" alt=""> 
    </div> 
    <div class="table">
      <h5>Dg set - general maintenance - due alert</h5>
      <table>
        <tbody>
             <tr>
              <td>ESN</td>
              <td>{{ esn }}</td>
            </tr>
            <tr>
              <td>MODEL</td>
              <td>{{ model }}</td>
            </tr>
            <tr>
              <td>KVA</td>
              <td>{{ kva }}</td>
            </tr>
            
            <tr>
              <td>LAST COOLANT REPLACEMENT DATE</td>
              <td>{{ last_coolant }}</td>
            </tr>
            <tr>
              <td>LAST COOLANT REPLACEMENT HOURS</td>
              <td>{{ last_coolant_hour }}</td>
            </tr>
        </tbody>
      </table>
      
      <h5 style="color:red;">Coolant due</h5>
    </div>
    <div class="body">
     <h4 class="mt-5">Dear sir/mam,</h4>
        <p class="mt-2"> we observe <b style="color:red;">coolant</b> due in the above mentioned ESN <b style="color:blue;">{{ esn }}</b> on <b style="color:blue;">{{ last_coolant }}</b>. So please replace the coolant as soon as possible for trouble free operation.. </p>
          <p>Any clarification  please feel free to contact us on 044-424244444 after office hours please contact phone number 9445037117 our executive will speak with you..</p>
        <h5>If you what quote please click the below link </h5>
        <a class="button">Request Quote</a>
    </div>
    
    <div class="footer">
      
    </div>
  </div>
  
</body>
</html>
    '''
    self.context_data['due'] = 'Coolant'
    sub = 'Coolant due alert'
    res = self.send_mail(html, self.context_data, sub)
    return res
    
    
  def send_battery(self):
    html = '''
    <!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style type="text/css" media="all">
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
body{
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  
}
.main{
}
.main .heading{
  display: flex;
  justify-content: center;
  width: 100%;
  background-color: #ff1a1a;
}
.main .heading h4{
  color: white;
  font-size: 25px;
  text-align: center;
}
.main .heading img{
  width: 40%;
  height: 30%;
  margin-top: 5px;
  margin-right: 15px;
}

.main .image img{
  width: 80%;
  margin: 0 10% 0 10%;
}
.table h5{
  text-align: center;
  font-size: 15px;
}
.table table{
  width: 100%;
}

.table table tbody tr td{
  padding: 8px 0px 8px 10px;
}

.body{
  padding-left: 10px;
  padding-right: 10px;
}

.body a{
    display: block;
    width: 115px;
    height: 25px;
    background: #4d4dff;
    padding: 10px;
    margin-top: 70px;
    text-align: center;
    border-radius: 5px;
    color: white;
    font-weight: bold;
    line-height: 25px;
    text-decoration: none;
}


  </style>
</head>
<body>
  <div class="main">
    <div class="heading">
      <h4>Greetings from JN machineries</h4>
      <img src="cid:image" alt=""> ---->
    </div>
    <div class="image">
     <img src="cid:image1" alt=""> 
    </div>
    <div class="table">
      <h5>Dg set - general maintenance - due alert</h5>
      <table>
        <tbody>
             <tr>
              <td>ESN</td>
              <td>{{ esn }}</td>
            </tr>
            <tr>
              <td>MODEL</td>
              <td>{{ model }}</td>
            </tr>
            <tr>
              <td>KVA</td>
              <td>{{ kva }}</td>
            </tr>
            
            <tr>
              <td>LAST BATTERY REPLACEMENT DATE</td>
              <td>{{ last_coolant }}</td>
            </tr>
            <tr>
              <td>LAST BATTERY REPLACEMENT HOURS</td>
              <td>{{ last_coolant_hour }}</td>
            </tr>
        </tbody>
      </table>
      
      <h5 style="color:red;">Battery due</h5>
    </div>
    <div class="body">
     <h4 class="mt-5">Dear sir/mam,</h4>
        <p class="mt-2"> we observe <b style="color:red;">battery</b> due in the above mentioned ESN <b style="color:blue;">{{ esn }}</b> on <b style="color:blue;">{{ last_battery }}</b>. So please replace the battery as soon as possible for trouble free operation.. </p>
          <p>Any clarification  please feel free to contact us on 044-424244444 after office hours please contact phone number 9445037117 our executive will speak with you..</p>
        <h5>If you what quote please click the below link </h5>
      <a class="button">Request Quote</a>
    </div>
    
    <div class="footer">
      
    </div>
  </div>
  
</body>
</html>
    '''
    sub = 'Battery due alert'
    res = self.send_mail(html, self.context_data, sub)
    return res
    
    
  def send_airfilter(self):
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style type="text/css" media="all">
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
body{
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  
}
.main{

}
.main .heading{
  display: flex;
  justify-content: center;
  width: 100%;
  background-color: #ff1a1a;
}
.main .heading h4{
  color: white;
  font-size: 25px;
  text-align: center;
}
.main .heading img{
  width: 40%;
  height: 30%;
  margin-top: 5px;
  margin-right: 15px;
}

.main .image img{
  width: 80%;
  margin: 0 10% 0 10%;
}
.table h5{
  text-align: center;
  font-size: 15px;
}
.table table{
  width: 100%;
}

.table table tbody tr td{
  padding: 8px 0px 8px 10px;
}

.body{
  padding-left: 10px;
  padding-right: 10px;
}

.body a{
    display: block;
    width: 115px;
    height: 25px;
    background: #4d4dff;
    padding: 10px;
    margin-top: 70px;
    text-align: center;
    border-radius: 5px;
    color: white;
    font-weight: bold;
    line-height: 25px;
    text-decoration: none;
}


  </style>
</head>
<body>
  <div class="main">
    <div class="heading">
      <h4>Greetings from JN machineries</h4>
      <img src="cid:image" alt="">
    </div>
    <div class="image">
     <img src="cid:image1" alt=""> 
    </div>
    <div class="table">
      <h5>Dg set - general maintenance - due alert</h5>
      <table>
        <tbody>
             <tr>
              <td>ESN</td>
              <td>{{ esn }}</td>
            </tr>
            <tr>
              <td>MODEL</td>
              <td>{{ model }}</td>
            </tr>
            <tr>
              <td>KVA</td>
              <td>{{ kva }}</td>
            </tr>
            
            <tr>
              <td>LAST BATTERY REPLACEMENT DATE</td>
              <td>{{ last_airfilter }}</td>
            </tr>
            <tr>
              <td>LAST BATTERY REPLACEMENT HOURS</td>
              <td>{{ last_airfilter_hour }}</td>
            </tr>
        </tbody>
      </table>
      
      <h5 style="color:red;">Airfilter due</h5>
    </div>
    <div class="body">
     <h4 class="mt-5">Dear sir/mam,</h4>
        <p class="mt-2"> we observe <b style="color:red;">Airfilter</b> due in the above mentioned ESN <b style="color:blue;">{{ esn }}</b> on <b style="color:blue;">{{ last_airfilter }}</b>. So please replace the Airfilter as soon as possible for trouble free operation.. </p>
          <p>Any clarification  please feel free to contact us on 044-424244444 after office hours please contact phone number 9445037117 our executive will speak with you..</p>
        <h5>If you what quote please click the below link </h5>
        <a class="button">Request Quote</a>
    </div>
    
    <div class="footer">
      
    </div>
  </div>
  
</body>
</html>
    '''
    sub = 'Airfilter due Alert'
    res = self.send_mail(html, self.context_data, sub)
    return res
    
    
    
  def send_amc(self):
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style type="text/css" media="all">
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
body{
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  
}
.main{
  
}
.main .heading{
  display: flex;
  justify-content: center;
  width: 100%;
  background-color: #ff1a1a;
}
.main .heading h4{
  color: white;
  font-size: 25px;
  text-align: center;
}
.main .heading img{
  width: 40%;
  height: 30%;
  margin-top: 5px;
  margin-right: 15px;
}

.main .image img{
  width: 80%;
  margin: 0 10% 0 10%;
}
.table h5{
  text-align: center;
  font-size: 15px;
}
.table table{
  width: 100%;
}

.table table tbody tr td{
  padding: 8px 0px 8px 10px;
}

.body{
  padding-left: 10px;
  padding-right: 10px;
}


  </style>
</head>
<body>
  <div class="main">
    <div class="heading">
      <h4>Greetings from JN machineries</h4>
      <img src="cid:image" alt="">
    </div>
    <div class="image">
     <img src="cid:image1" alt=""> 
    </div>
    <div class="table">
      <h5>DG AMC DUE REMINDER</h5>
      <table>
        <tbody>
          <tr>
              <td>Company Name</td>
              <td>{{ company_name }}</td>
            </tr>
            <tr>
              <td>Contact Person</td>
              <td>{{ contact_person }}</td>
            </tr>
            <tr>
              <td>Contact Number</td>
              <td>{{ phone_num }}</td>
            </tr>
             <tr>
              <td>ESN</td>
              <td>{{ esn }}</td>
            </tr>
            <tr>
              <td>MODEL</td>
              <td>{{ model }}</td>
            </tr>
            <tr>
              <td>KVA</td>
              <td>{{ kva }}</td>
            </tr>
            
            <tr>
              <td>AMC START DATE</td>
              <td>{{ amc_start }}</td>
            </tr>
            <tr>
              <td>AMC END DATE</td>
              <td>{{ amc_end }}</td>
            </tr>
        </tbody>
      </table>
      
      <h5 style="color:red;">AMC due</h5>
    </div>
    <div class="body">
     <h4 class="mt-5">Dear sir/mam,</h4>
        <p class="mt-2"> we observe <b style="color:red;">AMC</b> due in the above mentioned ESN <b style="color:blue;">{{ esn }}</b> AMC start date on <b style="color:blue;">{{ amc_start }}</b>AMC end date on <b style="color:blue;">{{ amc_end }}</b>. So please send the reminder AMC quote to customer. If quote Already send please remind what is the status. </p>
    
    <div class="footer">
      
    </div>
  </div>
  
</body>
</html>
    '''
    sub = 'AMC due reminder'
    res = self.send_mail(html, self.context_data, sub)
    return res
    
  
  def send_mail(self,  html, context_data, sub, user):
    try:
      msgRoot = MIMEMultipart('related')
      html_text = Template(html)
      content_html = html_text.render(Context(context_data))
      msgText = MIMEText(content_html, 'html', 'utf-8')
      msgRoot.attach(msgText)
      image_path = settings.STATIC_DIR + '/images/image.png'
      fp = open(image_path, 'rb')
      msgImage = MIMEImage(fp.read())
      fp.close()
      msgImage.add_header('Content-ID', '<image1>')
      msgRoot.attach(msgImage)
      image_path2 = settings.STATIC_DIR + '/images/image1.png'
      fp2 = open(image_path2, 'rb')
      msgImage2 = MIMEImage(fp2.read(), _subtype="png")
      fp2.close()
# Define the image's ID as referenced above
  
      msgImage2.add_header('Content-ID', '<image2>')
      msgRoot.attach(msgImage2)
     # recipe = self.mail_id
      recipe = 'boobalaneee5@gmail.com'
      #print(user)
      user_profile = Profile.objects.filter(user_name__username = 'raja')
      #user_profile = Profile.objects.all()
      for ele in user_profile:
        print(ele.user_name)
        print(ele.emp_code)
        print(ele.user_mail_password)
      sender = settings.APPLICATION_EMAIL
 # image_name = Path(image_path).name
      mail = EmailMessage(sub, None, sender, [recipe,])
      mail.attach(msgRoot)
      mail.send()
     # email_html_template = get_template(html_tpl_path).render(context_data)
    #  receiver_email = self.mail_id
     # email_msg = EmailMessage('B check due Alert', email_html_template, settings. APPLICATION_EMAIL,[receiver_email])
     # email_msg.content_subtype = 'html'
  #    email_msg.send(fail_silently=False)
      res = 'Mail send successfully'
      return res
      
      
      
    except Exception as e:
      error = f'Mail not send due to {e}'
      return error
  