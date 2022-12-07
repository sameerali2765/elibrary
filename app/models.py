from django.db import models
from categories.models import category
# Create your models here.   
class Author(models.Model):
    name=models.CharField(max_length=350)
    description = models.TextField(blank=True, null= True)
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)

    def __str__(self):
        return self.name

class slider(models.Model):
    Image = models.ImageField(upload_to='media/slider_imgs')
    Name =models.CharField(max_length=200)
    Category =models.ForeignKey(category,on_delete=models.CASCADE)
    Author=models.ForeignKey(Author,on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)


    def __str__(self):
        return self.Name

class Publisher(models.Model):
    name=models.CharField(max_length=350)
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    
    def __str__(self):
        return self.name