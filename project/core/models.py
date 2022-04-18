from django.db import models
#from django.contrib.gis.db import models
from users.models import CustomUser

class Post(models.Model):
    image = models.ImageField(null=True,blank=True)
    author_post = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.author_post.username

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

class CustomerCordinate(models.Model):
    customeruser = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cordinates')
    #point = models.PointField()
