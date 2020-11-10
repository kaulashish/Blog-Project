from django.db.models.signals import post_save
from django.contrib.auth.models import User  #Sender (sends signal)
from django.dispatch import receiver  # Reciever (gets the sender signal and performs some tasks)
from .models import Profile  #to create profile from fxn


# the reciever recieves the sender signal(included in the decorator)
# i.e when a user is saved, send the (post_save) signal which is recieved by the reciever
# the reciever is the create_profile fxn(since the create_profile fxn is decorated)
# which takes the following arguments that is passed to the post_save signal.
# So if the user is created then created then create a profile object with the user = instance of the user that is created.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


#saves the profile when the user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


#for this to work we need to import the signals inside the ready fxn of Users/apps.py file
