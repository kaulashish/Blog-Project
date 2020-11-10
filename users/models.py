from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    # the profile must have one to one relationship with the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile-pics')

    def __str__(self):
        return f'{self.user.username} Profile.'

    def save(self):
        #We are overriding this method(which is already in the parent class).
        #Runs after the model is saved. (for changing image size before uploading)
        #super runs the save method of out parent class first.
        super().save()

        #grabbing the saved image to resize it using Pillow.
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
