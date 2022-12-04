from django.contrib import admin
from . models import Instruments_List,Fixture_List,CheckSheet,Checkpoint
from import_export import fields,resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from rangefilter.filters import DateRangeFilter

class Resource1(resources.ModelResource):
    def export_field(self, field, obj):
        v = super(Resource1, self).export_field(field, obj)
        if type(v) == str:
            v = ILLEGAL_CHARACTERS_RE.sub('', v)
        return v
    class Meta:
        model = Instruments_List
        fields = ('id','Description','Intrument_Serial_No','Range','Least_count','Make','Intrument_ID','Calibration_Freq','Date_of_Calibration','Next_calibration_Due','Report_No','Calibration_report1','FN')

        export_order = ['id','Description','Intrument_Serial_No','Range','Least_count','Make','Intrument_ID','Calibration_Freq','Date_of_Calibration','Next_calibration_Due','Report_No','Calibration_report1','FN']

class Resource2(resources.ModelResource):
    def export_field(self, field, obj):
        v = super(Resource2, self).export_field(field, obj)
        if type(v) == str:
            v = ILLEGAL_CHARACTERS_RE.sub('', v)
        return v


    class Meta:
        model = Fixture_List
        fields = ('id','Customer','Product_description','Sub_Assembly','Fixture_or_Template_ID','Description','Location_used','Verification_Freq','Verification_Plan','Verified_on','Next_Verification_Due','checksheet','Verification_report1','Verification_report2','Status','Remarks','FN')

        export_order = ['id','Customer','Product_description','Sub_Assembly','Fixture_or_Template_ID','Description','Location_used','Verification_Freq','Verification_Plan','Verified_on','Next_Verification_Due','Verification_report1','Verification_report2','Status','Remarks','FN']






class Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource1
    class Meta:
        model = Instruments_List
    list_display = ['Description','Intrument_Serial_No','Range','Least_count','Make','Intrument_ID','Calibration_Freq','Date_of_Calibration','Next_calibration_Due','Report_No','Calibration_report1']

    list_filter = [('Date_of_Calibration',DateRangeFilter),('Next_calibration_Due',DateRangeFilter),'Intrument_ID','Description','Make']
    search_fields =['Intrument_ID','Description','Make','Date_of_Calibration','Next_calibration_Due']

class Admin1(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource2
    class Meta:
        model = Fixture_List
    list_display = ['Customer','Product_description','Sub_Assembly','Fixture_or_Template_ID','Description','Location_used','Verification_Freq','Verification_Plan','Verified_on','Next_Verification_Due','Status','checksheet','Verification_report1','Verification_report2','Remarks']
    
    list_filter=[('Verified_on',DateRangeFilter),('Next_Verification_Due',DateRangeFilter),'Customer','Product_description','Sub_Assembly','Location_used','Status',]
    search_fields =['Customer','Product_description','Sub_Assembly','Location_used','Verified_on','Next_Verification_Due']
   




admin.site.register(Instruments_List,Admin)
admin.site.register(Fixture_List,Admin1)
admin.site.register(Checkpoint)
admin.site.register(CheckSheet)

