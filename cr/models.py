from django.db import models

class MyImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # 'images/' is the upload path

# Create your models here.
class historyy(models.Model):
    status=models.BooleanField(default=True)
    subject=models.CharField(max_length=10)
    course=models.CharField(max_length=50)
    day=models.CharField(max_length=10)
    teacher=models.CharField(max_length=100)
    year=models.IntegerField()
    room=models.IntegerField()
    time=models.CharField(max_length=50)
    color=models.CharField(max_length=50, default="red")
    
    def __str__(self) -> str:
        return super().__str__()
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    feedback = models.TextField()

class cancel(models.Model):
    status=models.BooleanField(default=True)
    subject=models.CharField(max_length=10)
    course=models.CharField(max_length=50)
    day=models.CharField(max_length=10)
    teacher=models.CharField(max_length=100)
    year=models.IntegerField()
    room=models.IntegerField()
    time=models.CharField(max_length=50)
    color=models.CharField(max_length=50, default="red")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()