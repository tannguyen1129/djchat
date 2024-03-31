from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    request_sent = models.BooleanField(default=False)
    # email = models.EmailField()
    
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ('username',)
    
    def __str__(self):
        return self.username

