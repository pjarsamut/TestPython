from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2)
    education = models.CharField(max_length=100)
    gpa = models.FloatField()
    birthday = models.DateField()

    def __str__(self):
        return self.field1