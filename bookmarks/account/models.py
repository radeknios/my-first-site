from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
from mptt.models import MPTTModel, TreeForeignKey

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
    category = TreeForeignKey('Category', on_delete=models.CASCADE, related_name='post')
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

    '''def get_absolute_url(self):
        return reverse('delete_post', args=[self.id])'''

    class Meta:
        ordering = ('-publish',)

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('list_of_post_by_category', args=[self.slug])

    def __str__(self):
        return self.name

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]
            slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs




    
    



    







