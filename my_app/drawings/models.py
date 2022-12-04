from django.db import models


class Model_Name(models.Model):
    model =models.CharField(max_length=256)
    def __str__(self):
            return self.model
    class Meta:
        ordering = ['model']

class Sub_Assembly(models.Model):
    sub_assembly =models.CharField(max_length=256)
    def __str__(self):
        return self.sub_assembly
class Material(models.Model):
    material =models.CharField(max_length=256)
    def __str__(self):
        return self.material

class Drawings_2D(models.Model):
    Model_Name = models.ManyToManyField(Model_Name,related_name='model_names',through=None,blank=True,null=True)


    def All_parts_model(self):
        return "\n".join([p.model for p in self.Model_Name.all()])
    Sub_Assembly_Name = models.ForeignKey(Sub_Assembly,on_delete=models.CASCADE,null=True,blank=True)
    Child_part = models.CharField(max_length=256,null=True,blank=True)
    def get_upload_path(instance, filename):
        return '{0}/{1}/{2}' .format('drawings',instance.Sub_Assembly_Name,filename)
    Drawing1 = models.FileField(upload_to=get_upload_path,blank=True,null=True)
    Drawing2 = models.FileField (upload_to=get_upload_path,blank=True,null=True)
    Photo1 = models.FileField (upload_to=get_upload_path,blank=True,null=True)
    Photo2 = models.FileField (upload_to=get_upload_path,blank=True,null=True)
    Process_Instructions = models.CharField(max_length=256,null=True,blank=True,help_text='optional')
