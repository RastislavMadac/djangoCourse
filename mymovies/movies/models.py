from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=80, verbose_name='Názov filmu')

    length=models.IntegerField(validators=[MinValueValidator(45),MaxValueValidator(200)], default=90, verbose_name='Dĺžka (min)')

    is_for_adults= models.BooleanField(default=False, verbose_name='Iba pre dospelích')
    description = models.TextField(blank=True, null=True, verbose_name='Popis')
    rating = models.IntegerField( 

        validators=[MinValueValidator(0), MaxValueValidator(5)], 

        verbose_name='Hodnocení' 

    ) 

    def __str__(self): 

        return f'{self.title} ({self.length} min)' 