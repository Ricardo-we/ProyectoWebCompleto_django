from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    intro_content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog')
    #BIG_PRESENTATION
    content = models.TextField(null=False)
    image1 = models.ImageField(upload_to='posts', null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
    image2 = models.ImageField(upload_to='posts', null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)
    image3 = models.ImageField(upload_to='posts', null=True, blank=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


