from django.db import models

# Create your models here.

class FacebookUser(models.Model):
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10, null=True)
    cookie = models.TextField(null=True)
    fa2 = models.CharField(max_length=255)
    number_of_friend = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
