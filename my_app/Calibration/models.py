from django.db import models
from datetime import datetime,timedelta
import datetime
from dateutil.relativedelta import relativedelta




class Instruments_List(models.Model):
    result=(   ("Accepted","Accepted"),
                ("Rejected","Rejected"),
                ("Conditionally_accepted","Conditionally_accepted"),
                 ("Not_Claibrated","Not_calibrated")
                )
    Description = models.CharField(max_length=100,blank=True,null=True)
    Intrument_Serial_No = models.CharField(max_length=100,blank=True,null=True)
    Range = models.CharField(max_length=100,blank=True,null=True)
    Least_count = models.CharField(max_length=100,blank=True,null=True)
    Make = models.CharField(max_length=100,blank=True,null=True)
    Intrument_ID = models.CharField(max_length=100,blank=True,null=True)
    Calibration_Freq = models.IntegerField(blank=True,null=True)
    Calibration_Plan =models.DateField(null=True,blank=True)
    Date_of_Calibration =models.DateField(null=True,blank=True)
    Next_calibration_Due =models.DateField(editable=False,null=True,blank=True)
    def save(self):
        if self.Date_of_Calibration == None:
            self.Next_calibration_Due=self.Calibration_Plan
            super(Instruments_List, self).save()
        else:           
            from dateutil.relativedelta import relativedelta
            self.Next_calibration_Due=self.Date_of_Calibration + relativedelta(months=self.Calibration_Freq)
            super(Instruments_List, self).save()
  
    Status = models.CharField(max_length=100,choices = result)
    Report_No= models.CharField(max_length=100,blank=True,null=True)
    Calibration_report1 =models.FileField(upload_to='Calibration/Instruments',blank=True,null=True)
    Calibration_report2 =models.FileField(upload_to='Calibration/Instruments',blank=True,null=True)
    FN = models.CharField(max_length=100, default="REV-01 14.05.2022",blank=True,null=True)


class Checkpoint(models.Model):
    Check_point1 =models.CharField(max_length=256,blank=True,null=True,unique=True)

    def __str__(self):
        return str(self.Check_point1)
 

    

class CheckSheet(models.Model):
    Check_point1 =models.ForeignKey(Checkpoint,on_delete=models.SET_NULL,null=True,related_name="check_point1")
    Check_point_1 =models.CharField(max_length=256,blank=True,null=True)
    Check_point2 =models.ForeignKey(Checkpoint,on_delete=models.SET_NULL,null=True)
    Check_point_2 =models.CharField(max_length=256,blank=True,null=True)

    def __str__(self):
        return str(f"Inspection report")
  
    


class Fixture_List(models.Model):
    Customer  = models.CharField(max_length=256,blank=True,null=True)
    result=(   ("Accepted","Accepted"),
                ("Rejected","Rejected"),
                ("Conditionally_accepted","Conditionally_accepted"),
                ("Not_verified","Not_verified")
                )

    Product_description  = models.CharField(max_length=100,blank=True,null=True)
    Sub_Assembly  = models.CharField(max_length=100,blank=True,null=True)
    Fixture_or_Template_ID = models.CharField(max_length=100,blank=True,null=True)
    Description = models.CharField(max_length=100,blank=True,null=True)
    Location_used = models.CharField(max_length=100,blank=True,null=True)
    Verification_Freq = models.IntegerField()
    Verification_Plan =models.DateField(null=True,blank=True)
    Verified_on =models.DateField(null=True,blank=True)
    Next_Verification_Due =models.DateField(editable=False,null=True,blank=True)
    def save(self):
        if self.Verified_on == None:
            self.Next_Verification_Due=self.Verification_Plan
            super(Fixture_List, self).save()
        else:           
            from dateutil.relativedelta import relativedelta
            self.Next_Verification_Due=self.Verified_on+relativedelta(months= self.Verification_Freq)
            super(Fixture_List, self).save()
       
      

        
    Status = models.CharField(max_length=100,choices = result)
    Remarks =models.CharField(max_length=256,null=True,blank=True)
    Verification_report1 =models.FileField(upload_to='Calibration/Fixture_or_Templates',null=True,blank=True)
    Verification_report2 =models.FileField(upload_to='Calibration/Fixture_or_Templates',null=True,blank=True)
    checksheet = models.OneToOneField(CheckSheet,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return str(self.Description)
