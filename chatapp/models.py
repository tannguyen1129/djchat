from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "profiles")
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    
    def __str__(self):
        return self.username

  
class FriendRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_request")
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.sender.username} sent {self.receiver.username} a friend request"


class Notification(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender_notification")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver_notification")
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    seen = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return f"Hi {self.sender.username} accepted your friend request"

class ChatMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender_chats")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver_chats")
    message = models.TextField()
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    n_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    seen = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["n_created"]
    
    def __str__(self):
        return self.message
