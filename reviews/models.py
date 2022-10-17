from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie_name = models.CharField(max_length=20)
    grade = models.IntegerField(validators=[MinValueValidator(0),
                                MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    
    thumbnail = ProcessedImageField(
        blank=True,
        upload_to="articles/images",
        processors=[Thumbnail(100, 100)],
        format="JPEG",
        options={"quality": 60},
    )