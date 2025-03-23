from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='')
    heading = models.CharField(max_length=255)
    intro_descp = models.CharField(max_length=255)
    background_img = models.ImageField(upload_to='')
    phone_icon_name = models.CharField(max_length=13)
    taskease_phone = models.CharField(max_length=13)
    email_icon_name = models.CharField(max_length=13)
    taskease_email = models.EmailField()
    location_icon_name = models.CharField(max_length=13)
    location = models.TextField()
    location_map = models.TextField()
    service_descrpt = models.TextField()
    services_title = models.CharField(max_length=255)
    whyus_background_img = models.ImageField(upload_to='')
    helpers_title = models.CharField(max_length=255)
    hiringform_title = models.CharField(max_length=255)
    contact_title = models.CharField(max_length=255)
    faq_title = models.CharField(max_length=255)
    newsletter_title = models.CharField(max_length=255)
    newsletter_decrpt = models.TextField()
    

class About(models.Model):
    about_title = models.CharField(max_length=255)
    about_descp1 = models.TextField()
    about_descp2 = models.TextField()
    about_list1 = models.TextField()
    about_list2 = models.TextField()
    about_list3 = models.TextField()
    
class Whyus(models.Model):
    whyus_question = models.TextField()
    whyus_answer = models.TextField()

class Service(models.Model):
    service_name = models.CharField(max_length=255)
    service_icon_name = models.CharField(max_length=255)
    
class Callus(models.Model):
    callus_title = models.CharField(max_length=255)
    callus_descrpt = models.TextField()
    callus_num = models.CharField(max_length=13)
    callus_button_title = models.CharField(max_length=13)
    
class Helpers(models.Model):
    helper_name = models.CharField(max_length=255)
    helper_age = models.PositiveIntegerField()  # Ensure age is an integer
    helper_designation = models.CharField(max_length=100)
    filter_designation = models.CharField(max_length=100)
    status = models.BooleanField(default=True)  # Assuming helpers are active by default
    helper_image = models.ImageField(upload_to='')

    # New Fields with Default Values
    experience = models.PositiveIntegerField(default=0)  # Default experience is 0 years
    location = models.CharField(max_length=255, default="Not Specified")  # Default location
    
class Hiringform(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    home_address = models.TextField()
    phone = models.CharField(max_length=13)
    # helper_id = models.ForeignKey(Helpers, on_delete=models.CASCADE, related_name='helpers')
    helperid = models.IntegerField()
    
class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    data_delay = models.IntegerField()
    faq_listid = models.IntegerField()
    
class Contact(models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    client_subject = models.CharField(max_length=100)
    client_message = models.TextField()

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', default='default.jpg')  

    def __str__(self):
        return f'{self.user.username} Profile'
    
    
