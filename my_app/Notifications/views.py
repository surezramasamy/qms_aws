from django.shortcuts import render
from django.views.generic import ListView,DeleteView,UpdateView,CreateView
from .import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class NotificationListView(LoginRequiredMixin,ListView):
    context_object_name='notify'
    model = models.notification
    template_name= 'notification.html'
    def get_queryset(self): 
        if self.request.user.is_superuser:
            return(models.notification.objects.all())
        else:
            return (models.notification.objects.filter(Resp=self.request.user))
    
class NoteCreateView(CreateView):
    fields = ('Information','Action_required','Raised_by','Resp')
    model =models.notification
    success_url = ('/index')

class NoteUpdateView(UpdateView):    
    model =models.notification
    fields = ('Action_taken','Remarks','Status') 
    success_url = ('/index')
   
