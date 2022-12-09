from django.db import models

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/images/')
    productkey = models.IntegerField()
    def __str__(self):
        return self.title

class subproducts(models.Model):
    productname = models.CharField(max_length = 50)
    subproductskey = models.IntegerField()
    productimage = models.ImageField(upload_to='static/images/')
    productdescription = models.TextField()
    uniqueproductid = models.IntegerField()
    
    def __str__(self):
        return self.productname
class ord(models.Model):
    productname = models.CharField(max_length=100)
    userid = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    
# class product(models.Model):
#     # productname = subproducts.productname
#     description = models.CharField(max_length = 5000)
    


