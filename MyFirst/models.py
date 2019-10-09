from django.db import models

# Create your models here.
class empData(models.Model):
    empID = models.IntegerField(primary_key=True, editable=False)
    empName = models.CharField(max_length=20, null=True)
    empMobile = models.IntegerField(null=True)
    empAddress = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.empID