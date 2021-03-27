 from django.db import models
 class Profile(models.Model):
   user=models.CharField(max_length=30 , blank=False)
  
  
   def __str__(self):
    return self.user
  
  class student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    contact=models.CharField(max_length=10)
    department=models.CharField(max_length=5)
    
    def __str__(self):
      return self.name
  
