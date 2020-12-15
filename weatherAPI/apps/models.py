from django.db import models

# Create your models here.
class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=False, null=False)
    temp = models.DecimalField(default=0,blank=False,null=False,max_digits=5, decimal_places=2)
    maxtp = models.DecimalField(default=0,blank=False,null=False,max_digits=5, decimal_places=2)
    mintp = models.DecimalField(default=0,blank=False,null=False,max_digits=5, decimal_places=2)
    humidity = models.DecimalField(default=0,blank=False,null=False,max_digits=5, decimal_places=2)
    describ = models.CharField(max_length=255, blank=False,null=False)


    class Meta:
        db_table = 'History'