from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return '{}'.format(self.name)
    
class Book(models.Model):
    title=models.CharField(max_length=200,null=True)
    description = models.CharField(max_length = 500, default=None)
    price=models.IntegerField(null=True)
    
    image=models.ImageField(upload_to='book.media')
    
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    book_available=models.BooleanField(default=False)
    quantity=models.IntegerField()
    
    
    def __str__(self):
        return self.title
    
    
