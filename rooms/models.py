from django.db import models

class timetable(models.Model):
    status=models.BooleanField(default=True)
    subject=models.CharField(max_length=10, blank=True)
    course=models.CharField(max_length=50)
    day=models.CharField(max_length=10)
    teacher=models.CharField(max_length=100, blank=True)
    year=models.IntegerField()
    room=models.IntegerField()
    time=models.CharField(max_length=50)
    name=models.CharField(max_length=100,blank=True)
    color=models.CharField(max_length=50, default="White")
    
    def __str__(self):
        return f'{self.day} - {self.time}: {self.subject}'
    class Meta:
        db_table='timetable'