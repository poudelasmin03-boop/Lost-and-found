from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Itemdetails(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  itemName = models.CharField(max_length=100)
  itemDescription =  models.TextField()
  itemTag = models.TextField(null=True,blank=True,default="electronic")
  itemImage = models.ImageField(upload_to='Items/')
  location = models.TextField(max_length=300,default="ktm")
  foundDate = models.DateField(auto_now=True)
  phoneNo = models.CharField(max_length=20,default="98989898")
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return f"{self.user.username} - {self.itemName}"