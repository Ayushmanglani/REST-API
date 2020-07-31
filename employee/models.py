from django.db import models

# Create your models here.
class Info(models.Model):
    employee_id = models.IntegerField(unique=True)
    employee_name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField(null=True, blank=True)
    #Ranking = models.FloatField()

    def upload_photo(self,filename):
        path = 'employee/photo/{}'.format(filename)
        return path

    photo = models.ImageField(upload_to=upload_photo, null=True, blank=True)

    def __str__(self):
        return f'{self.employee_id} - {self.employee_name} - {self.salary}'