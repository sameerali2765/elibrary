from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    


    def __str__(self):
        return self.name