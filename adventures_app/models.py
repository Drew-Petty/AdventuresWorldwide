from django.db import models
from django.contrib.auth.models import User

class Guide(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    type = models.CharField(default='basic',max_length=10)
    about_me = models.TextField()
    picture = models.ImageField(default='default_guide.png', upload_to = 'guides', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.user.first_name +" "+ self.user.last_name

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().save(*args, **kwargs)

class Location(models.Model):
    name = models.CharField(max_length =50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length =50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name

class Trip(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    duration = models.IntegerField(verbose_name='Days Long:')
    cost = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Total Cost')
    capacity= models.IntegerField()
    picture= models.ImageField(default='default_trip.jfif',upload_to='trips',null=True, blank=True)
    guide = models.ForeignKey(Guide,related_name='trips', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='trips', verbose_name='Categories', blank=True)
    location = models.ForeignKey(Location, related_name='trips', on_delete = models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name


