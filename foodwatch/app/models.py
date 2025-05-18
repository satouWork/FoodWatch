from django.db import models
from django.contrib.auth.models import AbstractUser

# 
class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'users'
    