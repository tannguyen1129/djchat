from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Profile
 
 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username, last_name=instance.last_name, first_name=instance.first_name)
        
  
@receiver(post_save, sender=Profile)
def update_profile(sender, created, instance, **kwargs):
    if created:
        pass

    
    else:
        user = instance.user 
        print(user.username)
        print("okakkkt")
        user.username = instance.username
        user.first_name = instance.first_name
        user.last_name = instance.last_name 
        user.save()
