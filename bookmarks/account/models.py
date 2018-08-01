from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)

    def _str_(self):
        return 'Profil użytkownika {}.'.format(self.user.username)

class Available(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start = models.DateField(blank=True, null=True, verbose_name="Początek")
    end = models.DateField(blank=True, null=True, verbose_name="Koniec")


class PublishedManager(models.Manager):
        def get_queryset(self):
            return super(PublishedManager, self).get_queryset()
 
class Post(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='post')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)
    objects = models.Manager()
    published = PublishedManager()
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])

    class Meta:
        ordering = ('-publish',)

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same 
                                                 #slug 

    '''def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent                          

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' / '.join(full_path[::-1])'''




    
    



    







