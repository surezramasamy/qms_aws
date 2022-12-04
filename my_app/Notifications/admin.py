from django.contrib import admin
from .models import notification

class Admin(admin.ModelAdmin):

    class Meta:
        model = notification
    list_display = ['date','Information','photo','Action_required','Resp','Action_taken','Action_date','Raised_by','Status','Remarks']
    list_editable= ['Information','Action_required','Status','Remarks']


admin.site.register(notification,Admin)
# Register your models here.
