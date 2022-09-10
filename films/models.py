from django.db import models
from django.core import validators
from sorl.thumbnail import ImageField 

# Create your models here.
class Genre(models.Model):
    """Genre Table name for store Genre Data"""

    # TODO: Genre Table name for store Genre Data
    name = models.CharField(max_length=255)
    

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name


class Film(models.Model):
    """Film Model for store film data."""

    # TODO: Define fields here
    title = models.CharField( max_length=255)
    length = models.PositiveIntegerField(blank=True, null= True)
    year = models.PositiveIntegerField(blank=True, null=True)
    score = models.FloatField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,blank=True,null=True)
    poster = ImageField(blank=True, null= True,upload_to='images/')
    

    def __str__(self):
        """Unicode representation of MODELNAME."""
        if self.year:
            return f"{self.title} ({self.year})"
        return self.title
    