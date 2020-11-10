from django.db import models
from django.utils import timezone  # for creating datetime object
from django.contrib.auth.models import User  # since user is in separate table, we import the table here
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # since user and post are realted in a one-to-many relationship, we use a foreign key
    # on_delete lets us to control what to do with the post in case the user is deleted. In this case, we delete the post.
    # Keep in mind to rerun migration on making changes to the database! i.e python manage.py makemigrations,
    # then python manage.py migrate

    def __str__(self):
        # for making the post object (Post.objects.all()) more descriptive.
        return self.title

    #we use the reverse fxn to return the post-detail page after posting with setting the primary key 'pk'
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
