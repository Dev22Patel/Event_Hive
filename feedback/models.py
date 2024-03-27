from django.db import models  
  
class Review(models.Model):  
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='images')  
    current_status = models.CharField(max_length=50,null=True)

    def __str__(self):  
        return self.name