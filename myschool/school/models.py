from django.db import models

# Create your models here.


class Student(models.Model): 

    first_name = models.CharField(max_length=50, verbose_name='Křestní jméno') 

    second_name = models.CharField(max_length=50, verbose_name='Příjmení') 

    email = models.CharField(max_length=50, verbose_name='Email') 

    is_premiant = models.BooleanField(default=True) 

    

    def __str__(self): 

        return f'Student: {self.second_name}' 