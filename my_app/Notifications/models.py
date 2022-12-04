from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User

class notification(models.Model):
    date = models.DateTimeField(default=now, editable=False)
    Information =models.CharField(max_length=256)
    photo=models.FileField(blank=True,upload_to='Notifications/')
    Action_required = models.CharField(max_length=256)
    Action_taken = models.TextField(max_length=256,blank=True) 
    Action_date = models.DateTimeField(auto_now=True, editable=False)   
    Raised_by=models.CharField(max_length=256)
    Resp = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    status_choices =(("open", "open"),("closed","closed"))
    Status=models.CharField(max_length=256,choices = status_choices,default ="open",null=True,blank=True )
    Remarks = models.CharField(max_length=256,blank=True)
    def get_absolute_url(self):
        return reverse ("notification_detail",kwargs={'pk':self.pk})
