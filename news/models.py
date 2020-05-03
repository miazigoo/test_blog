from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):
    title = models.CharField( max_length=100)
    text = RichTextField()
    img = models.ImageField("Изображение", default=None, upload_to="post_img")
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
    
