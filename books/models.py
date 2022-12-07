from django.db import models
from app.models import Author
from app.models import Publisher
from categories.models import category
# Create your models here.
class Add_book(models.Model):
    name=models.CharField(max_length=350)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    publish_year = models.CharField(max_length=100)
    description = models.TextField(blank=True, null= True)
    image=models.ImageField(upload_to='media/book_imgs')
    pdf = models.FileField(upload_to='media/bookapp/pdfs/')
    download = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)


    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
    