from django.db import models
from django.utils.timezone import now
# Create your models here.
class contacts(models.Model):
  id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
  username = models.CharField(max_length = 50)
  email = models.EmailField(max_length=100)
  phone = models.CharField(max_length=15)
  message = models.TextField(max_length = 500)
  pub_date = models.DateField(default=now)
  
  def __str__(self):
    return "  %d \t |  \t %s " % (self.id, self.username)

  class Meta:
    db_table = 'contact'

class subscriber(models.Model):
  id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
  username = models.CharField(max_length = 50)
  email = models.EmailField(max_length=100)
  phone = models.CharField(max_length=15)
  city = models.CharField(max_length = 50)
  country = models.CharField(max_length = 50)
  pub_date = models.DateField(default=now)
  
  def __str__(self):
    return "  %d \t |  \t %s " % (self.id, self.username)

  class Meta:
    db_table = 'subscriber'

class announcement(models.Model):
  id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
  subject = models.CharField(max_length = 50)
  message = models.TextField(max_length = 5000)
  pub_date = models.DateField(default=now)
  
  def __str__(self):
    return "  %d \t |  \t %s " % (self.id, self.subject)

  class Meta:
    db_table = 'announcement'